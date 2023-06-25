import uvicorn 
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    name = "John Doe"
    return templates.TemplateResponse("arguement_passing.html", {"request": request, "name": name})
if __name__ =="__main__":

         uvicorn.run("arguement_passing:app",host="0.0.0.0",port=8000)

