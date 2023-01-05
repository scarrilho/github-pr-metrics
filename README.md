# github-pr-metrics
Retrieve information from closed pull requests in GitHub

# Overview
This repo has two scripts with the following goals:
- pr_data_retriever.py: Retrieves data from GitHub and computes a table with data to be used for analysis. The data is saved in a CSV file.
- pr_data_plotter.py: Summarizes the table in the CSV file created by pr_data_retriever.py, and shows some plots related to the target metrics.

The metrics used for the analysis are listed below, and were inspired by the article [5 metrics Engineering Managers can extract from Pull Requests](https://sourcelevel.io/blog/5-metrics-engineering-managers-can-extract-from-pull-requests) and the [gilot tool](https://github.com/hirokidaichi/gilot). 
- Pull Request Lead Time
- Pull Request Time to Merge
- Pull Request Size
- Lead Time vs Pull Request Size
- Created vs Merged
- Refactoring Ratio and Engagement

# Usage
**Notes**
- The scripts need Python 3 and were not tested on a Windows machine.
- The PR dates are converted to Japan time (JST - GMT+9). Change the settings as needed.

### pr_data_retriever.py
The mandatory settings are the repo owner and name. For example, for React it would be:
```
OWNER = 'microsoft'
REPO_NAME = 'TypeScript'
```

The script needs the the GitHub token info to execute the requests. You can either export your GitHub Token in the shell running the script, or otherwise hardcode it in the script (not recommended).
```pythonpython
export GITHUB_API_TOKEN=your-token
```
or hardcode it:

```python
# github_token = os.environ['GITHUB_API_TOKEN']
github_token = 'your-token'
```

After setting the OWNER and REPO_NAME, and the token if necessary, just run the command:
```
python3 pr_data_retriever.py
```

### pr_data_plotter.py

```python
# Change this setting as needed
file_for_analysis = 'pr_data_TypeScript_2023-01-05.csv'
```

After setting the file name just run the script: 
```
python3 pr_data_plotter.py
```

# Example
### microsoft/TypeScript
Script ran on 2023/1/5 JST (GMT+9) with the settings. 
```python
OWNER = 'microsoft'
REPO_NAME = 'TypeScript'

# Adjust num of PRs to be retrieved
MAX_NUM_PAGES = 5
PULL_REQUESTS_PER_PAGE = 10
```


The output:

```
---------------------------------------------------
Main stats from 2022-12-06 to 2023-01-04
---------------------------------------------------
43 PRs, managed by 14 developers were analyzed
     Lead Time Time to Merge Additions Deletions PR Size Changed Files Review Comments
max         24            24     4,117       918   4,125           236              13
mean         3             3       250        77     327            12               1
min          0             0         0         0       1             1               0
```

**Plots**

<img src="https://user-images.githubusercontent.com/5166193/210746265-5ebd69f8-5223-456e-a6a4-b6b366648f15.png" width="500"> <img src="https://user-images.githubusercontent.com/5166193/210746727-d8ea9318-d384-4d0d-95aa-4cdd976d27f5.png" width="500">
<img src="https://user-images.githubusercontent.com/5166193/210746788-f1e7022a-a105-4c13-b560-0eb4dd6b90c3.png" width="500">
<img src="https://user-images.githubusercontent.com/5166193/210746821-3765d7b5-3f32-403c-a316-235b0a865e3d.png" width="500">
<img src="https://user-images.githubusercontent.com/5166193/210746852-b8488af9-b6fc-475d-b2b5-f75be12bc1f0.png" width="500">
<img src="https://user-images.githubusercontent.com/5166193/210746873-0cd59b9a-ec06-4635-9d3a-c692c09c9889.png" width="500">
