import os
import requests
from datetime import datetime
import pytz
import csv

# Set your repo info here.
# Example: for https://github.com/microsoft/TypeScript
OWNER = 'microsoft'
REPO_NAME = 'TypeScript'
USER_TO_IGNORE = 'Automated User'  # Optional

# Adjust num of PRs to be retrieved
MAX_NUM_PAGES = 5
PULL_REQUESTS_PER_PAGE = 10

current_page = 1

# GitHub links
LISTING_BASE_URL = f'https://api.github.com/repos/{OWNER}/{REPO_NAME}/pulls?state=closed&per_page={PULL_REQUESTS_PER_PAGE}&page='
PR_BASE_URL = f'https://api.github.com/repos/{OWNER}/{REPO_NAME}/pulls/'
PR_LINK_SUFFIX = f'https://github.com/{OWNER}/{REPO_NAME}/pull/'

final_dataset = []
date_format = '%Y-%m-%dT%H:%M:%SZ'


class RequestHelper:
    server_timezone = pytz.timezone('UTC')
    tokyo_timezone = pytz.timezone('Asia/Tokyo')  # Using Tokyo time

    # In your shell, export you token: export GITHUB_API_TOKEN=your-token
    github_token = os.environ['GITHUB_API_TOKEN']

    # Or hardcode your token below
    # github_token = 'your-token'

    def fetch_prs_listing_page(self, page):
        url = LISTING_BASE_URL + str(page)
        return self.execute_request(url)

    def fetch_pr(self, pull_request_num):
        url = PR_BASE_URL + str(pull_request_num)
        print(url)

        return self.execute_request(url)

    def fetch_commits(self, pull_request_num):
        url = PR_BASE_URL + str(pull_request_num) + '/commits'
        return self.execute_request(url)

    def fetch_first_commit_date(self, pull_request_num):
        url = PR_BASE_URL + str(pull_request_num) + '/commits'
        res = self.execute_request(url)
        data_dict = res.json()[0]
        date = data_dict.get('commit').get('author').get(
            'date')
        return date

    def localize_datetime_to_tokyo(self, datetime):
        datetime_in_tokyo = self.server_timezone.localize(
            datetime).astimezone(self.tokyo_timezone)
        return datetime_in_tokyo

    def execute_request(self, url):
        auth_info = 'Bearer ' + self.github_token
        return requests.get(url, headers={
            'Authorization': auth_info})


class CSVWriter:
    today = str(datetime.today().date())
    target_csv_file_name = f'pr_data_{REPO_NAME}_{today}.csv'

    def write_to_file(self, dataset):
        print('-----------------')
        print('Writing to csv, Please Wait')
        keys = dataset[0].keys()
        with open(self.target_csv_file_name, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(dataset)


request_helper = RequestHelper()
csv_writer = CSVWriter()

print(
    f'Will start fetching {MAX_NUM_PAGES} pages, each with links to {PULL_REQUESTS_PER_PAGE} pull requests')

# To add first data to res
print(f'Fetching page {current_page} of {MAX_NUM_PAGES}')
res = request_helper.fetch_prs_listing_page(current_page)
print(res)

repos = res.json()

while res.json() != [] and current_page < MAX_NUM_PAGES:
    current_page = current_page + 1

    print(f'Fetching page {current_page} of {MAX_NUM_PAGES}')
    res = request_helper.fetch_prs_listing_page(current_page)
    print(res)
    repos.extend(res.json())

print('PR info retrieval complete. Will start fetching PRs')
print('-----------------')
print('Fetching PRs, Please Wait')
for data in repos:
    result = {}
    pr_num = data['number']

    # Ignore PRs that were not merged
    if data['merged_at'] is None:
        print('Ignoring unmerged PR: ', pr_num)
        continue

    first_commit = request_helper.fetch_first_commit_date(pr_num)

    merged_at = datetime.strptime(data['merged_at'], date_format)
    created_at = datetime.strptime(data['created_at'], date_format)
    closed_at = datetime.strptime(data['closed_at'], date_format)
    first_committed_at = datetime.strptime(
        first_commit, date_format)

    created_at_localized = request_helper.localize_datetime_to_tokyo(
        created_at)
    closed_at_localized = request_helper.localize_datetime_to_tokyo(closed_at)
    merged_at_localized = request_helper.localize_datetime_to_tokyo(merged_at)
    first_committed_at_localized = request_helper.localize_datetime_to_tokyo(
        first_committed_at)

    first_commit_date = first_committed_at.date()

    result['Creation Date'] = created_at_localized.date()

    result['Merge Date'] = merged_at_localized.date()

    result['Closing Date'] = closed_at_localized.date()

    result['First Commit Date'] = first_committed_at_localized.date()

    result['Lead Time'] = round(
        (merged_at_localized - created_at_localized).total_seconds() / 86400, 1)

    result['Time to Merge'] = round(
        (merged_at_localized - first_committed_at_localized).total_seconds() / 86400, 1)

    res = request_helper.fetch_pr(pr_num)
    result['Additions'] = res.json()['additions']
    result['Deletions'] = res.json()['deletions']
    result['PR Size'] = result['Additions'] + result['Deletions']
    result['Changed Files'] = res.json()['changed_files']
    result['Commits'] = res.json()['commits']
    result['Review Comments'] = res.json()['review_comments']
    result['Comments'] = res.json()['comments']
    result['User'] = res.json()['user']['login']
    result['PR Num'] = str(data['number'])
    result['PR Link'] = PR_LINK_SUFFIX + str(data['number'])

    if result['User'] != USER_TO_IGNORE:
        final_dataset.append(result)

if final_dataset:
    csv_writer.write_to_file(final_dataset)
    print('Success. Wrote to file: ', CSVWriter.target_csv_file_name)

print('-------END-------')
