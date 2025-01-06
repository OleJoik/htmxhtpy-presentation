import htpy as h
import time
from markupsafe import Markup
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

from htmxhtpy import components, database
from htmxhtpy.constants import LIMIT

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


@app.get("/static/bars.svg", include_in_schema=False)
async def loading_indicator():
    return FileResponse("static/bars.svg")


@app.get("/")
def index():
    offset = 0
    initial_rows = database.query(database.data, offset, LIMIT)
    return HTMLResponse(
        h.html[
            components.head(),
            h.body[
                components.navigation_bar(),
                h.div(".container")[
                    components.table(
                        components.rows(initial_rows, offset),
                    )
                ],
                h.center[
                    h.img(
                        id="loading-indicator",
                        class_="htmx-indicator mt-4",
                        width="60",
                        src="/static/bars.svg",
                    )
                ],
            ],
        ]
    )


@app.get("/characters")
def get_more_characters(offset: int = 0):
    next_rows = database.query(database.data, offset, LIMIT)

    time.sleep(0.5)
    return HTMLResponse(
        "".join([str(Markup(row)) for row in components.rows(next_rows, offset)])
    )
