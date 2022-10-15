# compare-commits
Compiles a list of Git commit messages between two commits or versions

~~~
usage: Compares two GitHub commits. [-h] [--page PAGE] [--per_page PER_PAGE] owner repo base head

positional arguments:
  owner                The account owner of the repository. The name is not case sensitive.
  repo                 The name of the repository. The name is not case sensitive.
  base                 The base branch to compare.
  head                 The head branch to compare.

options:
  -h, --help           show this help message and exit
  --page PAGE          Page number of the results to fetch.
  --per_page PER_PAGE  The number of results per page (max 100).
~~~