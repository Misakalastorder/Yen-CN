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

"""
// 查询自己有没有设置代理，没有按下回车什么内容都不会输出
git config --global http.proxy
// 设置代理的命令(这里要注意一下我开的代理，也就是我们用的vpn,占用的端口是7890，所以我写的7890，看下自己用的哪个端口)
git config --global http.proxy http://127.0.0.1:7890
// 不用的时候最好取消了，不知道为什么突然正常push不上去了，时好时坏的。取消代理的命令
git config --global --unset http.proxy
"""