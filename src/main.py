# coding: utf-8
import argparse
import requests

class ReposRank:

    def get_repo_info(self, repo: str):
        url = f'https://api.github.com/repos/{repo}'
        info = requests.get(url)
        return info

    def sort_repos(self, repos: list):
        return sorted(repos, key=lambda k: k['stargazers_count'], reverse=True)

    def main(self):
        parser = argparse.ArgumentParser(description='Github repository ranking')
        parser.add_argument('--repositories', type=str, help='Repo list file path')

        args = parser.parse_args()

        repos = []

        filename = args.repositories
        if filename:
            with open(filename, 'r') as file_content:
                for line in file_content:
                    sanitized_line = line.rstrip()
                    repo_info = self.get_repo_info(sanitized_line)
                    repos.append(repo_info.json())
                
                for index, repo in enumerate(self.sort_repos(repos), start=1):
                    print(f"{index}) {repo['full_name']}: {repo['stargazers_count']}")

if __name__ == '__main__':
    repos_rank = ReposRank()
    repos_rank.main()
