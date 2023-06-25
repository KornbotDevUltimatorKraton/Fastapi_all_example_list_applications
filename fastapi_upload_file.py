import uvicorn 
import shutil 
from fastapi import FastAPI, File, UploadFile,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request:Request):
    return templates.TemplateResponse("upload_file.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
     # Save the file to the static directory
    file_path = f"static/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8900)
