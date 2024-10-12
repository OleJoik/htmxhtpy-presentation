import htpy as h
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/ping")
def ping():
    return "Pong"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def landing():
    return HTMLResponse(
        h.html[
            h.head[h.link(rel="stylesheet", href="/static/styles.css")],
            h.body[h.p(class_="w-screen h-screen bg-red-500")["Hello there!"],],
        ]
    )
