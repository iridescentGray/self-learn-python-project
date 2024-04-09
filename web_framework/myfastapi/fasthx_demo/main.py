import os
from typing import Annotated, Any

import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fasthx import Jinja, hx

basedir = os.path.abspath(os.path.dirname(__file__))

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(basedir, "templates"))
jinja = Jinja(templates)


@app.get("/user-list")
@jinja("user-list.html")
def htmx_or_data() -> dict[str, list[dict[str, str]]]:
    """This route can serve both JSON and HTML, depending on if the request is an HTMX request or not."""
    return {
        "users": [
            {
                "first_name": "Peter",
                "last_name": "Volf",
            },
            {
                "first_name": "Hasan",
                "last_name": "Tasan",
            },
        ]
    }


@app.get("/admin-list")
@jinja.template("user-list.html", no_data=True)
def htmx_only() -> dict[str, list[dict[str, str]]]:
    """This route can only serve HTML, because the no_data parameter is set to True."""
    return {
        "users": [
            {
                "first_name": "John",
                "last_name": "Doe",
            },
        ]
    }


"------------------------------------custom_templating-------------------------------------"


def get_random_number() -> int:
    return 4


DependsRandomNumber = Annotated[int, Depends(get_random_number)]


def render_user_list(
    result: list[dict[str, str]], *, context: dict[str, Any], request: Request
) -> str:
    # The value of the `DependsRandomNumber` dependency is accessible with the same name as in the route.
    random_number = context["random_number"]
    lucky_number = f"<h1>{random_number}</h1>"
    users = "".join(("<ul>", *(f"<li>{u['name']}</li>" for u in result), "</ul>"))
    return f"{lucky_number}\n{users}"


@app.get("/htmx-or-data")
@hx(render_user_list)
def htmx_or_data_custom_templating(
    random_number: DependsRandomNumber,
) -> list[dict[str, str]]:
    return [{"name": "Joe"}]


@app.get("/htmx-only")
@hx(render_user_list, no_data=False)
async def htmx_only_custom_templating(
    random_number: DependsRandomNumber,
) -> list[dict[str, str]]:
    return [{"name": "Joe"}]


@app.get("/")
def index(request: Request) -> HTMLResponse:
    """This route serves the index.html template."""
    return templates.TemplateResponse("index.html", context={"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5555)
