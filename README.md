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
The scripts need Python 3 and were not tested on a Windows machine.

### pr_data_retriever.py
The mandatory settings are the repo owner and name. For example, for React it would be:
```
OWNER = 'facebook'
REPO_NAME = 'react'
```

The script was made to use in internal repos where authentication is needed, therefore the default **NEEDS_AUTHENTICATION** setting is set to True. In this case, you need to export your GitHub Token in the shell running the script, or otherwise hardcode it in the script.
```pythonpython
export GITHUB_API_TOKEN=your-token
```
or hardcode it:

```python
# github_token = os.environ['GITHUB_API_TOKEN']
github_token = 'your-token'
```

If 
or hardcode it:
the repo public like the above, change the setting NEEDS_AUTHETICATION to False.

If you want to use it in public repos, without the need for authentication, just set **NEEDS_AUTHENTICATION** to false.
```python
# True for GitHub Enterprise repos, False for public repos
# If True, in your shell, export you token: export GITHUB_API_TOKEN=your-token
NEEDS_AUTHENTICATION = False
```

After setting the OWNER and REPO_NAME, and the token if necessary, just run the command:
```
python3 pr_data_retriever.py
```

### pr_data_plotter.py
The only setting needed is the CSV filename created by **pr_data_retriever.py**.

```python
# Change this setting as needed
file_for_analysis = 'pr_data_react_2023-01-04.csv'
```

After setting the file name just run the script: 
```
python3 pr_data_plotter.py
```
