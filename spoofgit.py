import json
import os
import time
from resources.git_funcs import _pull_shark, _pair_extraordinaire, fake_readme, get_user_email, github_add_contributors_to_repository, github_add_fake_commits_to_repository, github_open_issue, github_close_issue,github_spoof_contributors_to_repository
from resources import asciitoart
import datetime



SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'


GITHUB_TOKEN =  os.getenv("GITHUB_TOKEN")
USER = None
EMAIL = None
REPO = None

SLEEP_TIME = 5

OPTIONS = ['Spoof Contributors', 'Fake Activity', "Spoof Achievements", "Fake Profile Stats","Exit"]
DONE = []

TOTAL_MERGED_PRS = 0
requirements = [["asciitoart", "asciitoart"]]


def _fakeActivity():
    print("\n[+] Faking Activity")
    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime.now()

    start_date = input("Enter start date   (2022-01-01 00:00:00) : ")
    end_date = input("Enter end date       (2022-04-20 16:20:00) : ")

    print(f"\nStart Date\t: {start_date}")
    print(f"End Date\t: {end_date}")
    
    github_add_fake_commits_to_repository(GITHUB_TOKEN, REPO, EMAIL, USER, start_date, end_date)
    print(f"Activity faked! on - https://github.com/{USER}")


def select(selections):
    i = 0
    print(f"")
    for selection in selections:
        i += 1
        print(f"[{i}] {selection}")

            
    query = int(input(f"\n[?] Select an option (1-{i}) : ").strip())

    
    if query == 0:
        select(selections)
        #return
        
    query = query - 1
    
    if  query >= i :
        print(f"\n[x] Choose upto {i}")
        select(selections)
        #return
    else:
        choice = selections[query]

    #print(choice)
    return choice


def _celeb_cameo():
    print("\n[+] Spoofing contributors")
    users = input("Enter user github username to spoof (separate with [,] for multiple) : ")
    if "," in users:
        users = users.split(",")
        for userx in users:
            print(f"{userx} contributing to https://github.com/{USER}/{REPO}")
            github_spoof_contributors_to_repository(GITHUB_TOKEN, USER, REPO, userx)
            
    else:
        print(f"{users} contributing to https://github.com/{USER}/{REPO}")
        github_spoof_contributors_to_repository(GITHUB_TOKEN, USER, REPO, users)



def _spoof_achievements():
    print("\n[+] Spoofing Achievements")
    print("\n\nselect the achievements you want to add to your profile...")
    achievements_list = ['Quickdraw (closed an issue / pull request within 5 minutes of opening)', 'Pair Extraordinaire (Coauthored commits on merged pull request)', 'Pull Shark (Opened a pull request that has been merged)', 'Exit']
    
    selection = select(achievements_list)

    if selection == 'Exit':
        return
    
    if selection == 'Quickdraw (closed an issue / pull request within 5 minutes of opening)':
        print("Achieving Quickdraw")
        quickdraw()

    if selection == 'Pair Extraordinaire (Coauthored commits on merged pull request)':
        levels = ['1 [1 commit]', '2 [10 commits]', '3 [24 commits]', '4 [48 commits]']
        print("\nselect the level of Pair Extraordinaire you want to achieve...")
        
        selevel = select(levels)
        if selevel == "1 [1 commit]":
            lvl = 1
        if selevel == "2 [10 commits]":
            lvl = 2
        if selevel == "3 [24 commits]":
            lvl = 3
        if selevel == "4 [48 commits]":
            lvl = 4
        
        
        print(f" LVL {lvl}")
        pair_extraordinaire(lvl)

    if selection == 'Pull Shark (Opened a pull request that has been merged)':
        levels = ['1 [2 pull requests]', '2 [16 pull requests]', '3 [128 pull requests]', '4 [1024 pull requests - THIS WILL CONSUME ALOT OF API CALLS]']
        print("\n\nselect the level of Pull Shark you want to achieve...")

        selevel = select(levels)
        if selevel == "1 [2 pull requests]":
            lvl = 1
        if selevel == "2 [16 pull requests]":
            lvl = 2
        if selevel == "3 [128 pull requests]":
            lvl = 3
        if selevel == "4 [1024 pull requests - THIS WILL CONSUME ALOT OF API CALLS]":
            lvl = 4
        

        pull_shark(lvl)

def pair_extraordinaire(lvl=2):
    global TOTAL_MERGED_PRS

    if lvl == 1:
        _pair_extraordinaire(REPO, USER, GITHUB_TOKEN, EMAIL)
        TOTAL_MERGED_PRS += 1
    if lvl == 2:
        for i in range(10):
            _pair_extraordinaire(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            print(f"coauthored {i}/10 commits")
    if lvl == 3:
        for i in range(24):
            _pair_extraordinaire(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            print(f"coauthored {i}/24 commits")
    if lvl == 4:
        for i in range(48):
            _pair_extraordinaire(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            print(f"coauthored {i}/48 commits")
    print(f"Pair Extraordinaire done!")


def pull_shark(lvl=2):
    global TOTAL_MERGED_PRS
    
    if lvl == 1:
        while TOTAL_MERGED_PRS < 2:
            _pull_shark(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            time.sleep(SLEEP_TIME)
    if lvl == 2:
        while TOTAL_MERGED_PRS < 16:
            _pull_shark(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            time.sleep(SLEEP_TIME)
            print(f"merged {TOTAL_MERGED_PRS}/16 pull requests")
    if lvl == 3:
        while TOTAL_MERGED_PRS < 128:
            _pull_shark(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            time.sleep(SLEEP_TIME)
            print(f"merged {TOTAL_MERGED_PRS}/128 pull requests")
    if lvl == 4:
        while TOTAL_MERGED_PRS < 1024:
            _pull_shark(REPO, USER, GITHUB_TOKEN, EMAIL)
            TOTAL_MERGED_PRS += 1
            time.sleep(SLEEP_TIME)
            print(f"merged {TOTAL_MERGED_PRS}/1024 pull requests")
    print(f"Pull Shark done!")



def quickdraw():
    issue_number = github_open_issue(REPO, USER, GITHUB_TOKEN)
    time.sleep(5)
    github_close_issue(issue_number, REPO, USER, GITHUB_TOKEN)
    print(f"Quickdraw done!")

def _fake_profile_stats():
    print("\n[+] Faking profile stats")
    workplace = input("Please enter your desired workplace: ")
    profession = input("Please enter your desired profession: ")
    fake_readme(GITHUB_TOKEN, USER, profession, workplace)



def creds():
    global GITHUB_TOKEN, USER, EMAIL, REPO, OPTIONS
    print("\n[#] Setting up  credentials... ")

    while not GITHUB_TOKEN:
        GITHUB_TOKEN = input("Enter your GitHub token: ")
        if not GITHUB_TOKEN.startswith("ghp_"):
            print("Invalid token!")
            GITHUB_TOKEN = None

    while not USER and not EMAIL:
        if USER and not EMAIL:
            print("did not find user mail, try a different one")
        USER = input("Enter your GitHub username: ")
        if USER != "":
            EMAIL = get_user_email(GITHUB_TOKEN, USER)
    if not REPO:
        REPO = input("Enter the name of the repository you want to manipulate (CASE SENSITIVE!) : ")
    
    print(f"\nUSER\t: {USER}\nREPO\t: {REPO}\nEMAIL\t: {EMAIL}")

def main():
    
    try:banner = asciitoart.asciitoart_format("Spoof Git",font="ansi_shadow")
    except:banner = ""
    print(f"\n{banner}\n\t\t------ Github Account Spoofing Tool ------\n")
    creds()
    selection = select(OPTIONS)
    if selection == 'Spoof Contributors':
        _celeb_cameo()
        
    elif selection == 'Fake Activity':
        _fakeActivity()
        #print(f"You were busy! - https://github.com/{USER}/")
        
    elif selection == "Spoof Achievements":
        _spoof_achievements()
        #print(f"Achievements spoofed! - https://github.com/{USER}")
        
    elif selection == "Fake Profile Stats":
        _fake_profile_stats()
        #print(f"Profile stats faked! - https://github.com/{USER}")
        


main()