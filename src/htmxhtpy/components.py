import htpy as h
from htmxhtpy.constants import LIMIT
from htmxhtpy.database import LotrCharacter


def head():
    return (
        h.head[
            h.script(
                src="https://unpkg.com/htmx.org@2.0.3/dist/htmx.js",
                crossorigin="anonymous",
            ),
            h.link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css",
                integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u",
                crossorigin="anonymous",
            ),
        ],
    )


def navigation_bar():
    return (
        h.nav(".navbar.navbar-default")[
            h.div(".container")[
                h.div(".navbar-header")[
                    h.button(
                        ".navbar-toggle.collapsed",
                        type="button",
                        data_toggle="collapse",
                        data_target="#bs-example-navbar-collapse-1",
                        aria_expanded="false",
                    )[
                        h.span(".sr-only")["Toggle navigation"],
                        h.span(".icon-bar"),
                        h.span(".icon-bar"),
                        h.span(".icon-bar"),
                    ],
                    h.a(".navbar-brand", href="#")["HTPY + HTMX: LOTR Characters"],
                ],
            ]
        ],
    )


def table(table_rows: list[h.tr]):
    return h.table(".table")[
        h.thead[
            h.tr[
                h.th(scope="col")["Name"],
                h.th(scope="col")["Age"],
                h.th(scope="col")["Gender"],
                h.th(scope="col")["People"],
            ]
        ],
        h.tbody[table_rows],
    ]


def rows(characters: list[LotrCharacter], offset: int) -> list[h.tr]:
    output_html = []
    table_props = {}

    for i in range(len(characters)):
        character = characters[i]
        if i == LIMIT - 1:
            table_props = {
                "hx-get": f"/characters?offset={offset + LIMIT}",
                "hx-trigger": "revealed",
                "hx-swap": "afterend",
                "hx_indicator": "#loading-indicator",
            }

        output_html.append(
            h.tr(**table_props)[
                h.td[character["name"]],
                h.td[character["age"]],
                h.td[character["gender"]],
                h.td[character["people"]],
            ]
        )

    return output_html
