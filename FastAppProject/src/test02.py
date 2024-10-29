# test02.py


from fastapi import FastAPI, Response, HTTPException , UploadFile, Form
from fastapi.responses import HTMLResponse 
import os
from runapps import runapp, printapp, dlmodels

app= FastAPI()

@app.get("/dlmodels", response_class=HTMLResponse)
def test(s: str, default="ann, cnn, lstm, plot"):
    return dlmodels(s)

@app.get("/s081", response_class=HTMLResponse)
def test(s: str, default="cnn"):
    return printapp(s)


@app.get("/dl_models") #url
def dl_models(s: str, default="cnn, cnn, lstm, plot"):
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


@app.post("/upload-file", response_class=HTMLResponse)
async def upload_file(file: UploadFile):
    try:
        content = await file.read()
        code_content = content.decode("utf-8")
        return HTMLResponse(content=code_content, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
