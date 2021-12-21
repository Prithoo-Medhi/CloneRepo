import pandas as pd
import pathlib as path
from git import Repo
from os import getcwd

BASE_PATH = f'{getcwd()}/clonedrepos/'
DATASET_PATH = 'datasets/uid.csv'


def scrape_login(file:path.Path = DATASET_PATH):
    login = pd.read_csv(file)
    login_list =[]

    for row in login.itertuples():
        body={
            'uid': row.uid,
            'token': row.token,
            'reponame': row.reponame
        }
        login_list.append(body)
    
    return login_list

def clone_git(uid:str, token:str, repo_name:str):
    url = f'https://{token}@github.com/{uid}/{repo_name}.git'
    Repo.clone_from(url=url, to_path=BASE_PATH+repo_name)


