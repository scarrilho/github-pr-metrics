import matplotlib.pyplot as plt
import pandas as pd

# Change this setting as needed
file_for_analysis = 'pr_data_TypeScript_2023-01-05_master.csv'


class PlotterHelper:
    def plot_single(self, x, y, x_label, y_label, title, annotation_text, file_name):
        print('Plotting')

        plt.close('all')
        plt.clf()
        plt.bar(x, y, color='g', label=annotation_text)
        plt.xticks(range(len(x)), x, size='small')
        plt.xticks(rotation=25)
        plt.locator_params(nbins=10)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=1, fontsize=10)
        plt.title(title, fontsize=20)
        plt.savefig(file_name)
        plt.show()

    def plot_double(self, x, y1, y2, y1_legend, y2_legend, x_label, y_label, title, file_name):
        print('Plotting')
        plt.close('all')
        plt.plot(x, y1, color='g', label=y1_legend)
        plt.plot(x, y2, color='r', label=y2_legend)

        plt.xticks(range(len(x)), x, size='small')
        plt.xticks(rotation=25)
        plt.locator_params(nbins=10)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title, fontsize=20)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=1, fontsize=10)
        plt.savefig(file_name)

        plt.show()

    def plot_double_filled(self, x, y1, y2, y1_legend, y2_legend, x_label, y_label, title, file_name):
        print('Plotting')
        plt.close('all')
        plt.plot(x, y1, color='g', label=y1_legend)
        plt.fill_between(x, y1, color='g', alpha=0.3)

        plt.plot(x, y2, color='r', label=y2_legend)
        plt.fill_between(x, y2, color='r', alpha=0.3)

        plt.xticks(range(len(x)), x, size='small')
        plt.xticks(rotation=25)
        plt.locator_params(nbins=10)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title, fontsize=20)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=1, fontsize=10)
        plt.savefig(file_name)

        plt.show()

    def plot_triple_filled(self, x, y1, y2, y3, y1_legend, y2_legend, y3_legend, x_label, y_label, title,
                           annotation_text, file_name):
        print('Plotting')
        plt.close('all')
        plt.plot(x, y1, color='g', label=y1_legend)

        plt.plot(x, y2, color='r', label=y2_legend)
        plt.fill_between(x, y1, y2, color='g', alpha=0.3)
        plt.fill_between(x, 0, y2, color='r', alpha=0.4)

        plt.plot(x, y3, color='b', label=y3_legend)

        plt.xticks(range(len(x)), x, size='small')
        plt.xticks(rotation=25)
        plt.locator_params(nbins=10)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title, fontsize=20)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=1, fontsize=10)

        xmin, xmax, ymin, ymax = plt.axis()
        text_x_position = xmax / 2
        text_y_position = ymax - (ymax / 10)

        plt.text(text_x_position, text_y_position, annotation_text, fontsize=13,horizontalalignment="center",
        verticalalignment="center",bbox=dict(facecolor='red', alpha=0.5))

        plt.savefig(file_name)

        plt.show()

    def plot_scatter(self, x, y, x_label, y_label, title, file_name):
        print('Plotting')
        plt.close('all')
        plt.scatter(x, y, color='g', s=100)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title, fontsize=20)
        plt.savefig(file_name)
        plt.show()

    def plot_double_scatter(self, x, y1, y2, y1_legend, y2_legend, x_label, y_label, title, file_name):
        print('Plotting')
        plt.close('all')
        plt.scatter(x, y1, color='g', s=100, label=y1_legend)
        plt.scatter(x, y2, color='r', s=100, label=y2_legend)

        plt.xticks(range(len(x)), x, size='small')
        plt.locator_params(nbins=10)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title, fontsize=20)
        plt.legend(bbox_to_anchor=(1, 1), loc='upper right',
                   borderaxespad=1, fontsize=10)
        plt.savefig(file_name)
        plt.show()

    # Number of new PRs daily
    def plot_pr_count_vs_date(self, df):
        filename = 'count_vs_date.png'
        new_df = df['Creation Date'].value_counts().rename_axis(
            'Date').reset_index(name='counts').sort_values('Date')
        mean = round(new_df['counts'].mean(), 1)
        annotation_text = 'Mean: ' + str(mean)
        self.plot_single(
            new_df['Date'], new_df['counts'], 'Date', 'PR count', 'Daily Created PR Count', annotation_text, filename)

    def plot_pr_vs_review_comments(self, df):
        filename = 'pr_vs_review_comments.png'
        new_df = df[['PR Num', 'Review Comments']]
        mean = round(new_df['Review Comments'].mean())
        annotation_text = 'Mean: ' + str(mean)
        new_df = new_df.sort_values('PR Num')
        new_df['PR Num'] = new_df['PR Num'].apply(str)

        self.plot_single(
            new_df['PR Num'], new_df['Review Comments'], 'PR Number', 'Review Comments', 'Review Comment Count per PR',
            annotation_text, filename)

    def plot_pr_size(self, df):
        filename = 'pr_size.png'
        new_df = df[['PR Num', 'PR Size']]
        mean = round(new_df['PR Size'].mean())
        annotation_text = 'Mean: ' + str(mean)
        new_df = new_df.sort_values('PR Num')
        new_df['PR Num'] = new_df['PR Num'].apply(str)

        self.plot_single(
            new_df['PR Num'], new_df['PR Size'], 'PR Number', 'PR Size', 'PR Sizes', annotation_text, filename)

    # Low lead time == good
    def plot_lead_time_vs_additions_scatter(self, df):
        filename = 'lead_time_vs_additions.png'
        self.plot_scatter(
            df['Lead Time'], df['Additions'], 'Lead Time (days)', 'Additions', 'PR lead time vs additions', filename)

    # Low lead time == good
    def plot_lead_time_vs_pr_size(self, df):
        filename = 'lead_time_vs_pr_size.png'
        self.plot_scatter(
            df['Lead Time'], df['PR Size'], 'Lead Time (days)', 'PR Size (Additions + Deletions)',
            'PR Lead Time vs PR Size', filename)

    # To check balance of created vs closed
    def plot_created_closed_daily(self, df):
        filename = 'create_vs_closed_daily.png'
        new_df = self.compute_daily_created_closed_table(df)
        self.plot_double(
            new_df['Date'], new_df['created'], new_df['closed'], 'Created', 'Closed', 'Date', 'Created/Closed',
            'Created vs closed', filename)

    # To check balance of created vs merged
    def plot_created_merged_daily(self, df):
        filename = 'created_vs_merged_daily.png'
        new_df = self.compute_daily_created_merged_table(df)
        self.plot_double(
            new_df['Date'], new_df['created'], new_df['merged'], 'Created', 'Merged', 'Date', 'Created/Merged',
            'Created vs Merged', filename)

    # Check if keeping the code healthy by refactoring or just adding code
    def plot_additions_deletions_scatter(self, df):
        filename = 'additions_vs_deletions.png'
        self.plot_double_scatter(
            df['Merge Date'], df['Additions'], -df['Deletions'], 'Additions', 'Deletions', 'Merge Date', 'Additions',
            'Additions vs Deletions', filename)

    # Check if keeping the code healthy by refactoring or just adding code
    def plot_additions_deletions_aggregate(self, df):
        filename = 'additions_vs_deletions_aggregate.png'
        new_df = self.compute_daily_added_deleted_table(df)
        self.plot_double_filled(
            new_df['Merge Date'], new_df['Additions'], new_df['Deletions'], 'Additions', 'Deletions', 'Merge Date',
            'Additions/Deletions', 'Additions vs Deletions', filename)

    # Check if keeping the code healthy by refactoring or just adding code
    def plot_additions_deletions_pr_size_aggregate(self, df):
        filename = 'additions_vs_deletions_pr_size_aggregate.png'
        new_df = self.compute_daily_added_deleted_table(df)
        total_modified = new_df['PR Size'].sum()
        total_deleted = new_df['Deletions'].sum()
        refactoring_ratio = round((total_deleted / total_modified), 2)
        annotation_text = 'Refactor ratio: ' + str(refactoring_ratio)

        self.plot_triple_filled(
            new_df['Merge Date'], new_df['Additions'], new_df['Deletions'], new_df['PR Size'], 'Additions', 'Deletions',
            'PR Size', 'Merge Date', 'Additions/Deletions', 'Additions vs Deletions vs PR Size', annotation_text,
            filename)

    # Check if keeping the code healthy by refactoring or just adding code
    def plot_additions_deletions_aggregate_inverse(self, df):
        filename = 'additions_vs_deletions_aggregate_inverse.png'
        new_df = self.compute_daily_added_deleted_table(df)
        new_df['Deletions'] = -new_df['Deletions']

        self.plot_double_filled(
            new_df['Merge Date'], new_df['Additions'], new_df['Deletions'], 'Additions', 'Deletions', 'Merge Date',
            'Additions/Deletions', 'Additions vs Deletions', filename)

    def compute_daily_created_closed_table(self, df):
        pr_creation_dates = df['Creation Date'].value_counts().rename_axis(
            'Date').reset_index(name='created').sort_values('Date')

        pr_closing_dates = df['Closing Date'].value_counts().rename_axis(
            'Date').reset_index(name='closed').sort_values('Date')

        new_df = pd.merge(pr_creation_dates,
                          pr_closing_dates, how='outer', on='Date').sort_values('Date')

        new_df = new_df.fillna(0)

        return new_df

    def compute_daily_created_merged_table(self, df):
        pr_creation_dates = df['Creation Date'].value_counts().rename_axis(
            'Date').reset_index(name='created').sort_values('Date')

        pr_merging_dates = df['Merge Date'].value_counts().rename_axis(
            'Date').reset_index(name='merged').sort_values('Date')

        new_df = pd.merge(pr_creation_dates,
                          pr_merging_dates, how='outer', on='Date').sort_values('Date')

        new_df = new_df.fillna(0)

        return new_df

    def compute_daily_added_deleted_table(self, df):
        aggregation_rule = {'Additions': 'sum',
                            'Deletions': 'sum', 'PR Size': 'sum'}
        df_aggregated = df.groupby('Merge Date', as_index=False).aggregate(
            aggregation_rule).reindex(columns=df.columns)

        return df_aggregated


class StatsHelper:
    def compute_main_stats(df):
        sorted_by_merge_df = df.sort_values('Merge Date')

        start_date = sorted_by_merge_df['Merge Date'].iloc[0]
        end_date = sorted_by_merge_df['Merge Date'].iloc[-1]

        print('---------------------------------------------------')
        print('Main stats from {} to {}'.format(start_date, end_date))
        print('---------------------------------------------------')

        num_of_developers = len(pd.unique(df['User']))
        num_of_prs = len(pd.unique(df['PR Num']))

        df = df.loc[:, df.columns != 'PR Num']
        df = df.loc[:, df.columns != 'Commits']
        df = df.loc[:, df.columns != 'Comments']
        metrics = df.describe().loc[['max', 'mean', 'min']]
        metrics_formatted = metrics.applymap('{:,.0f}'.format)

        print(
            f'{num_of_prs} PRs, managed by {num_of_developers} developers were analyzed')

        print(metrics_formatted)

    def print_data_stats(df):
        print(df.describe())

    def abort_on_empty_df(df):
        if df.empty:
            print('---------------------(✘o✘)-------------------------')
            print('Dataframe is empty, aborting execution!')
            print('---------------------------------------------------')
            exit(1)


class Filter:
    # Optional: Irregular PRs that can be kept out of the statistics
    pull_requests_to_ignore = {}

    def compute_filtered_list(self, df):
        df_filtered = df[~df['PR Num'].isin(self.pull_requests_to_ignore)]
        return df_filtered


plotter = PlotterHelper()
filter = Filter()

df = pd.read_csv(file_for_analysis)
df = filter.compute_filtered_list(df)

StatsHelper.abort_on_empty_df(df)

# Plot info
print(f'Analyzing file: {file_for_analysis}')
StatsHelper.compute_main_stats(df)

plotter.plot_pr_count_vs_date(df)
plotter.plot_lead_time_vs_pr_size(df)
plotter.plot_created_merged_daily(df)
plotter.plot_additions_deletions_pr_size_aggregate(df)
plotter.plot_additions_deletions_aggregate_inverse(df)
plotter.plot_pr_size(df)
plotter.plot_pr_vs_review_comments(df)

print('*************DONE*****************')
