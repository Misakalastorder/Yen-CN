from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI()

# 用于渲染HTML的Jinja2模板
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, num1: float = Form(...), num2: float = Form(...), operation: str = Form(...)):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    else:
        result = "Invalid operation"

    return templates.TemplateResponse("calculator.html",
                                      {"request": request, "result": result, "num1": num1, "num2": num2,
                                       "operation": operation})


# 将静态文件目录挂载到 "/static" 路径
app.mount("/static", StaticFiles(directory="static"), name="static")

