# test02.py


#in vscode create file app.py
#from fastapi import FastAPI
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import HTMLResponse 
import os
from runapps import runapp, printapp

app= FastAPI()

@app.get("/runapp")
def runapps(sid: int):
    return {"status": runapp(sid)}

@app.get("/s081", response_class=HTMLResponse)
def test(s: str):
    return printapp(s)


@app.get("/s083") #url
def welcome():
    code = (
        "# S083.py\n"
        "mkdir new folder as repo Web-Project\n"
        "open cmd from folder\n"
        "in CMD:\n"
    )
    return code

@app.get("/dlmodels") #url
def DL_Models(s: str, default="cnn, cnn, lstm, plot"):
    if s=="ann": file_path = (r"G:\My Drive\gotoget\200_DL\290_ANN_regression.py")
    if s=="cnn": file_path = (r"G:\My Drive\gotoget\200_DL\206_dl_ANN+CNN_classifi_softmax_keras-cifar10.py")
    if s=="lstm": file_path = (r"G:\My Drive\gotoget\200_DL\260_dl_LSTM_csv_twitter-sentiment.py")
    if s=="plot": file_path = (r"G:\My Drive\gotoget\200_DL\280_plot_image.py")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        with open(file_path, "r") as file:
            code = file.read()
        return Response(content=code, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

#in Powershell trminal  uvicorn app:app --reload
# Get-Process uvicorn \ to see ide
# Stop-Process -Id <ProcessId>