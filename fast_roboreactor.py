import jwt
import uvicorn 
import shutil 
from typing import Union 
from fastapi import FastAPI,File,UploadFile,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#Get the index html value 
@app.get("/")
def index(request:Request):
           return templates.TemplateResponse("index.html",{"request":request})
#Passing_argument_python 
@app.get("/arguement") 
def read_root(request: Request):
    name = "John Doe"
    return templates.TemplateResponse("arguement_passing.html", {"request": request, "name": name})
#Passing arguement from end-point with (number data:int) (String data:str) change this parameters at item_id 
@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(request: Request, item_id: str):
    # Process the item_id or perform any necessary operations
    item_name = f"Item {item_id}"
    return templates.TemplateResponse("item.html", {"request": request, "item_name": item_name})
        
#Data_json 
@app.get("/data_json") 
def datas_json():
      Data_json = {"Data_json":"Hello_world"}
      return Data_json
#Post_request_data 
@app.post("/data") # Get the data from the post request python 
async def receive_data(request: Request):
    data = await request.json()  # Extract JSON data from the request body
    print(data) # Get the data to visualize the json structure 
    return {"received_data": data}

@app.get("/upload_model")
def read_root(request:Request):
    return templates.TemplateResponse("upload_file.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
     # Save the file to the static directory
    file_path = f"static/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
@app.get("/redirect_test")
def redirect_web_page():
  
       return RedirectResponse(url=app.url_path_for("upload_success"))

@app.get("/success")
def upload_success():
    return "File uploaded successfully!"

if __name__ == "__main__":

    uvicorn.run("fast_roboreactor:app", host="0.0.0.0", port=8000)
