#in vscode create file app.py
from fastapi import FastAPI


app01= FastAPI()

@app.get("/s082")   #url
def test():  # view
    return "html css js"

@app.get("/s083") #url
def welcome():
    return (f""" 
S083.py\n
mkdir new folder as repo Web-Project\n
open cmd from folder\n
in CMD:\n """)

@app.get("/s084") #url
def welcome():
    return "welcome"


#in trminal  uvicorn app:app --reload
# Get-Process uvicorn
# Stop-Process -Id <ProcessId>