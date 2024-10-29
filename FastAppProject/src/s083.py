
#S083.py
"""
mkdir new folder as repo Web-Project
open cmd from folder
in CMD:
C:\ProgramData\anaconda3\python -m venv FastAppProject # apps name
cd FastAppDProject  #in powershell cd .\FastAppProject\
source bin/activate # in mac
.\Scripts\activate # in windows in power shell 
\Scripts\activate # in windows in cmd
!pip install "fastapi[standard]"  # install fastapi
code .  # to open vscode

#in vscode create file app.py
from fastapi import FastAPI
#from schemas import

app= FastAPI()

@app.get("/users") #url
def welcome():  # view
    return "Hallo World"

@app.get("/transfer") #url
def test():  # view
    return "Gnerative AI"


in cmd >uvicorn app:app --reload

http methods
get:
post:
put:
patch:
delete:
    
api:
    system_01 has webside= frontend + backend_01
    system_02 has webside= frontend + backend_02
    backend_01 talk with backend_02 through api or request, query

 """   

