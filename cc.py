# wraps https://docs.github.com/en/rest/commits/commits#compare-two-commits
import argparse
import os

import requests


def main():
    # parse arguments from CLI
    parser = argparse.ArgumentParser("Compares two GitHub commits.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--baseurl", help="GitHub API base url.", default="https://api.github.com")
    parser.add_argument("--token", help="GitHub Token, otherwise uses environment variable GITHUB_TOKEN", required=False)
    parser.add_argument("--page", help="Page number of the results to fetch.", type=int, default=1)
    parser.add_argument("--per_page", help="The number of results per page.", type=int, default=30)
    parser.add_argument("--raw", help="Returns raw JSON from the API.", default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument("owner", help="The account owner of the repository. The name is not case sensitive.")
    parser.add_argument("repo", help="The name of the repository. The name is not case sensitive.")
    parser.add_argument("base", help="The base branch to compare.")
    parser.add_argument("head", help="The head branch to compare.")
    args = parser.parse_args()
    compareCommits(args.owner, args.repo, args.base, args.head, args.baseurl, args.token, args.page, args.per_page, args.raw)


def compareCommits(owner: str, repo: str, base: str, head: str, baseurl="https://api.github.com", token="", page=1,
                   per_page=30, raw=False):
    ''' Compiles a list of Git commit messages between two commits or versions. '''
    # prepare request
    url = str.removesuffix(baseurl, "/")
    url += f"/repos/{owner}/{repo}/compare/{base}...{head}"
    params = {}
    if page:
        params["page"] = page
    if per_page:
        params["per_page"] = per_page
    headers = {"Accept": "application/vnd.github+json"}
    token = token
    if not token:
        token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # make request
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    # parse response
    data = response.json()
    if raw:
        print(data)
        return data
    messages = []
    for commit in data["commits"]:
        message = commit["commit"]["message"]
        # some messages are long / ugly so trim them to 55 characters or at first newline
        if len(message) > 55:
            message = message[0:55] + "..."
        newlinePos = str.find(message, "\n")
        if newlinePos > 0:
            message = message[0:newlinePos]
        message = str.strip(message)
        messages.append(message)
        print(message)
    return messages


if __name__ == "__main__":
    main()
