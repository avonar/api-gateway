# app.py
from aiohttp import web
from aiohttp.abc import Application
from aiohttp_apispec import (
    setup_aiohttp_apispec,
    validation_middleware,
)

from routes import setup_routes

import logging


def create_app() -> Application:
    
    app = web.Application()
    logging.basicConfig(level=logging.INFO)
    setup_routes(app)
    # In-memory toy-database:
    app["users"] = []

    setup_aiohttp_apispec(app, swagger_path="/docs")
    app.middlewares.append(validation_middleware)

    return app


if __name__ == "__main__":
    web_app = create_app()
    web.run_app(web_app, port=8080)

