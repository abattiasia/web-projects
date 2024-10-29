# runapps.y

import subprocess

def runapp(sid: int):
    # Run specific PowerShell commands based on the sid parameter
    try:
        if sid == 1:
            subprocess.run("uvicorn app:app --reload", shell=True)
        elif sid == 2:
            subprocess.run("Get-Process uvicorn", shell=True)
        elif sid == 3:
            # Replace <ProcessId> with the actual process ID you want to stop
            process_id = "<ProcessId>"
            subprocess.run(f"Stop-Process -Id {process_id}", shell=True)
        elif sid == 4:
            subprocess.run("uvicorn app02:app --reload", shell=True)
        elif sid == 5:
            subprocess.run("Start-Process -NoNewWindow -FilePath uvicorn -ArgumentList 'app:app', '--reload'", shell=True)
        elif sid == 6:
            subprocess.run("ps uvicorn", shell=True)
        elif sid == 7:
            # Replace 'id' with the actual process ID you want to kill
            process_id = "<ProcessId>"
            subprocess.run(f"kill {process_id}", shell=True)
        else:
            raise ValueError("Invalid sid value")
        return  {"status": "Command executed successfully"}
    except Exception as e:
        return {"error": str(e)}

# Example usage:
#runapp(1)  # This will start `uvicorn app:app --reload` in PowerShell via VSCode terminal.
def printapp(s: str):
    if s == "cnn":
        code = """<h1>
        Run specific PowerShell commands based on the sid parameter</h1>
        <p>S083.py<br>
        mkdir new folder as repo Web-Project<br>
        open cmd from folder<br>
        in CMD</p>
        """
        return code
    else:
        return "<h1>Invalid command</h1>"

# def DL_Models(s: str):
#     if s=="ann": file_path = (r"G:\My Drive\gotoget\200_DL\290_ANN_regression.py")
#     if s=="cnn": file_path = (r"G:\My Drive\gotoget\200_DL\206_dl_ANN+CNN_classifi_softmax_keras-cifar10.py")
#     if s=="lstm": file_path = (r"G:\My Drive\gotoget\200_DL\260_dl_LSTM_csv_twitter-sentiment.py")
#     if s=="plot": file_path = (r"G:\My Drive\gotoget\200_DL\280_plot_image.py")
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404, detail="File not found")

#     try:
#         with open(file_path, "r") as file:
#             code = file.read()
#         return Response(content=code, media_type="text/plain")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")




# from fastapi import FastAPI, HTTPException, Response
# from fastapi.responses import HTMLResponse
# import os


import os
from fastapi import HTTPException
from fastapi.responses import HTMLResponse


def dlmodels(s: str):
    if s == "ann": file_path = r"G:\My Drive\gotoget\200_DL\290_ANN_regression.py"
    elif s == "cnn":  file_path = r"G:\My Drive\gotoget\200_DL\206_dl_ANN+CNN_classifi_softmax_keras-cifar10.py"
    elif s == "lstm":  file_path = r"G:\My Drive\gotoget\200_DL\260_dl_LSTM_csv_twitter-sentiment.py"
    elif s == "plot":  file_path = r"G:\My Drive\gotoget\200_DL\280_plot_image.py"
    else: raise HTTPException(status_code=400, detail="Invalid model type")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        with open(file_path, "r") as file:
            code = file.read()
            code = " choose ann, cnn, lstm, plot \n\n"+"----------------------\n\n"+code
        return HTMLResponse(content=code, media_type="text/html) #plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

