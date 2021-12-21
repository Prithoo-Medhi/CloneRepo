import os
import pwd
import pathlib as path
import pandas as pd
from git import repo
import os

def scrape_login(file:path.Path = 'datasets/uid.csv' ):
    login = pd.read_csv(file)
    login_list =[]

    for row in login.itertuples():
        body={
            'uid': row.uid,
            'token': row.token
        }
        login_list.append(body)
    
    return login_list


if __name__ == "__main__":
    print(os.getcwd())