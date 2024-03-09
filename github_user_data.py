import requests


def fetch_user_repositories(gituser):
    response = requests.get(f'https://api.github.com/users/{gituser}/repos')
    repositories_info = []

    if response.status_code == 200:
        api_data = response.json()
        for repo in api_data:
            repo_info = {
                'name': repo['name'],
                'description': repo.get('description', 'No description provided'),
                'language': repo.get('language', 'Not specified'),
                'stars': repo['stargazers_count'],
                'url': repo['url']
            }
            repositories_info.append(repo_info)
    else:
        print(f"Error in fetching repos for {gituser}. Status code: {response.status_code}")

    return repositories_info


def display_repository_info(repositories):
    for repo in repositories:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"URL: {repo['url']}")
        print(f"Language: {repo['language']}")
        print(f"Stars: {repo['stars']}")
        print('-' * 40)


def main():
    gituser = input("Enter a GitHub username: ")
    repositories = fetch_user_repositories(gituser)
    display_repository_info(repositories)


if __name__ == "__main__":
    main()
