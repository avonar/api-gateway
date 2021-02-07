# routes.py
from aiohttp import web

from api.v1.handlers import handle_get, handle_post, handle_patch, handle_put, handle_delete, statistics

TARGET_URL = '/{tail:.*}'

def setup_routes(app: web.Application) -> None:
    app.router.add_route('GET', '/statistics', statistics)
    app.router.add_route('GET', TARGET_URL, handle_get)
    app.router.add_route('POST', TARGET_URL, handle_post)
    app.router.add_route('PATCH', TARGET_URL, handle_patch)
    app.router.add_route('PUT', TARGET_URL, handle_put)
    app.router.add_route('DELETE', TARGET_URL, handle_delete)