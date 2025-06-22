# PK's league rank fetcher

A simple python script to fetch a player's current ranks on League of Legends


## Prerequisites

- Python (preferably Python 3.11)
- a Riot development API Key


## How to install

1. open a shell in the files directory

2. create a virtual environment with : `python -m venv env`  
(or change "python" with the path of Python 3.11, for example on windows : `C:\Users\User\AppData\Local\Programs\Python\Python311\python.exe -m venv env`)

3. activate the environment with : `env\scripts\activate.ps1` on Windows PowerShell  
(or `env\bin\activate` on Linux or `env\scripts\activate.bat` if using the cmd)

4. install the required packages with `pip install -r requirements.txt`

5. create an `.env` file then write `API_key=(your api key)` inside


## How to start

1. open a shell in the files directory

2. activate the environment with : `env\scripts\activate.ps1` on Windows PowerShell  
(or `env\bin\activate` on Linux or `env\scripts\activate.bat` if using the cmd)

3. run the script with `python main.py`


## How to use

- Enter a RIOT ID (for example `pkrf#728`)
- Enter `q` to close the program