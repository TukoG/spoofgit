# Spoof Git

Artificially inflate github account stats to look more credible

## Installation

clone the repo 
```
git clone https://github.com/TukoG/spoofgit
```

cd to path
```
cd spoofgit
```

## Prerequisites
* Github token

windows
```
set GITHUB_TOKEN=ghp_xxxxxxxxxxxxxx
```

linux / mac
```
export GITHUB_TOKEN=ghp_xxxxxxxxxx
```




## Usage
Github token is required for the tool to interact with the account to spoof


```
python3 spoofgit.py
```

## Spoofing

### Step 1: Fake Contributors
This step will add fake contributors to the project.

### Step 2: FAKE COMMIT
This step will add fake commits between time range of your choosing

### Step 3: SPOOF ACHIEVEMENTS
Adds fake achievements to the user's profile.

### Step 4: FAKE PROFILE STATS (profile readme)
This step will add fake profile stats to the user's profile.
