from methods import scrape_login, clone_git

def main():
    login_list = scrape_login()

    for item in login_list:
        clone_git(uid=item['uid'], token=item['token'], repo_name=item['reponame'])



if __name__ == "__main__":
    main()