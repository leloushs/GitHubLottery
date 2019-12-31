from github import Github
import random

repository = "david-pzh/A-Eye"
github_username = ""
github_passwoed = ""
N = 8


def get_lucky_dogs():
    # First create a Github instance
    # g = Github()
    # Or you can use your GitHub username and password
    g = Github(github_username, github_passwoed)

    # Get a repo by repo-name
    repo = g.get_repo(repository)

    # Now list the users
    stared_users = []
    for user in repo.get_stargazers():
        stared_users.append(user.login)

    return stared_users


if __name__ == "__main__":
    print("Running...")

    stared_users = get_lucky_dogs()
    print("Found {} ".format(stared_users))
    print("{} stared users in total.".format(len(stared_users)))

    print("\n\n--- Congratulations!!! --- \n\n")
    alist = random.sample(range(0, len(stared_users)), N)
    [print(stared_users[i]) for i in alist]
