import argparse


# wraps https://docs.github.com/en/rest/commits/commits#compare-two-commits
def main():
    # parse arguments from CLI
    parser = argparse.ArgumentParser("Compares two GitHub commits.")
    parser.add_argument("--baseurl", help="GitHub API base url.", default="https://api.github.com", required=False)
    parser.add_argument("--token", help="GitHub Token, otherwise uses environment variable GITHUB_TOKEN", required=False)
    parser.add_argument("--page", help="Page number of the results to fetch.", type=int, default=1, required=False)
    parser.add_argument("--per_page", help="The number of results per page (max 100).", type=int, default=30, required=False)
    parser.add_argument("owner", help="The account owner of the repository. The name is not case sensitive.")
    parser.add_argument("repo", help="The name of the repository. The name is not case sensitive.")
    parser.add_argument("base", help="The base branch to compare.")
    parser.add_argument("head", help="The head branch to compare.")
    parser.parse_args()


def hello():
    return "Hello World!"


if __name__ == "__main__":
    main()
