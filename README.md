# compare-commits
Compiles a list of Git commit messages between two commits or versions.

This code wraps https://docs.github.com/en/rest/commits/commits#compare-two-commits and then prints / returns the commit messages.

Raw API example: https://api.github.com/repos/facebook/react/compare/0.11-stable...0.12-stable

GUI example: https://github.com/facebook/react/compare/0.11-stable...0.12-stable

### Requirements:
[Python](https://www.python.org) (tested with 3.9+ and above)

### Installation:
    pip install -r requirements.txt

### CLI Usage:
~~~
python cc.py [-h] [--baseurl BASEURL] [--token TOKEN] [--page PAGE] [--per_page PER_PAGE]
             [--raw | --no-raw] owner repo base head

positional arguments:
  owner                The account owner of the repository. The name is not case sensitive.
  repo                 The name of the repository. The name is not case sensitive.
  base                 The base branch to compare.
  head                 The head branch to compare.

options:
  -h, --help           show this help message and exit
  --baseurl BASEURL    GitHub API base url. (default: https://api.github.com)
  --token TOKEN        GitHub Token, otherwise uses environment variable GITHUB_TOKEN (default: None)
  --page PAGE          Page number of the results to fetch. (default: 1)
  --per_page PER_PAGE  The number of results per page. (default: 30)
  --raw, --no-raw      Returns raw JSON from the API. (default: False)
~~~

### Library Usage:
~~~
import cc

cc.compareCommits("owner", "repo", "base", "head", ...)
~~~
