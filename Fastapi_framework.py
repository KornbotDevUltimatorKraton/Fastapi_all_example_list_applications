import uvicorn 
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates 
templates = Jinja2Templates(directory="templates")
app = FastAPI() 

@app.get("/")
def index(request:Request):
           return templates.TemplateResponse("index.html",{"request":request})
if __name__ == "__main__":
    uvicorn.run("Fastapi_framework:app", host="0.0.0.0", port=8000)
