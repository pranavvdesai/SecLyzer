# Flipkart GRiD 4.0 - Information Security Challenge

<br>

# 🎡 Problem Statement
#### Open Source Software (OSS) Security Inspector.<br>
Open source software is an integral part of every tech product. There are amazing contributors who actively maintain their repositories. However, every coin has two sides. All OSS repositories may not be maintained properly, because of which, vulnerabilities may get introduced with time. Whereas, some OSS repos could be created by attackers themselves to trick the users. We need an OSS inspector to solve this problem. This tool will help us to identify the genuineness of the repos and perform a security health check.

## 💎 Brief description about the project
We have built an application that can:- <br>
 - Analyze Github, github, pypi and npm repos. <br>
 - Perform the scan with repository link. <br>
 - Provides the rating for the repository based upon <b>OWASP Top 10 vulnerabilities</b> along with few other vulnerabilities. <br>
 - Display snippet of the code having vulnerabilities. <br>
 - There might be some vulnerabilities that may be False positives and We can manually mark those vulnerabilites as false positives or remove them from the detected vulnerabilities.
 - Analyzes the statistics of the repo and the owner’s other repos to check for the genuineness of the repo using parameters such as repo stars, age of repository, time since the last commit, any pending security issues. <br>
 
## 👩🏻‍💻 Tech Stack
 - HTML/CSS/Bootstrap
 - JavaScript
 - Python
 - Flask
 - PostgreSQL
 - Semgrep
 - gunicorn


## 🎬 Getting Started (Linux/Mac)
<a href="https://adamtheautomator.com/install-postgresql-on-a-ubuntu/">Install Postgres</a> and configure `SQLALCHEMY_DATABASE_URI` in `SecLyzer/settings.py`.<br>Format `postgresql://<User>:<Password>@127.0.0.1/<Database_Name>`

#### Steps to set up SecLyzer Locally
```
git clone https://github.com/parikshit3000/SecLyzer_is_back.git
cd SecLyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 global_functions.py initialize-db # Run once to generate database schema
```

##### To run SecLyzer
`./run.sh`

This will run SecLyzer Web application at `http://127.0.0.1:9090`

## ✨ Future Scope
 - Suggestions for removing the vulnerabilites from the code.
 - To give suggestions for removing vulnerabilities from the code.
 - Increasing database of patterns for Semgrep analysis.
 - Better quality patterns to reduce false positives and identify corner cases.
 

 
## 👫 Contributors 
* [Parikshit Juneja](https://github.com/parikshit3000)
* [Pranav Desai](https://github.com/pranavvdesai)
* [Garv Tandon](https://github.com/garvsgit)

Team Name:- `Code Smashers`


## 💻 Screenshots
![image](https://user-images.githubusercontent.com/81351479/182050450-d911f2a0-d35a-41cb-86f5-29c4f0d7078c.png)
![image](https://user-images.githubusercontent.com/81351479/182050461-99b015c3-7b34-4203-9012-e243e1cbf86e.png)
![image](https://user-images.githubusercontent.com/81351479/182050474-e148d540-bee8-48f1-b893-88085489efb2.png)
![image](https://user-images.githubusercontent.com/81351479/182050483-7eee5285-ccb6-4c67-816b-f81410965b70.png)
![image](https://user-images.githubusercontent.com/81351479/182050489-4cb3789d-8942-43b3-8f36-32863e99464b.png)
![image](https://user-images.githubusercontent.com/81351479/182050492-1809628e-3ef0-47d2-9538-3ca302e97cb3.png)
![image](https://user-images.githubusercontent.com/81351479/182050499-09e25ff9-cfca-495d-b9b9-ef2082be6ee2.png)
![image](https://user-images.githubusercontent.com/81351479/182050513-65a1cb79-5308-4909-9cae-873fedd04c7f.png)
![image](https://user-images.githubusercontent.com/81351479/182050517-bc81178b-c3b4-4bf1-87e2-904770f90e2e.png)
