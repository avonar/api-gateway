from aiohttp import web, ClientSession
from aiohttp_apispec import (request_schema, docs)
from schemas import User, Message, UsersList
from config.template import EXCLUDED_HEADERS

def clear_headers(headers):
    for header in EXCLUDED_HEADERS:
        if header in headers:
            headers.pop(header)
    return headers

@docs(summary="Any get query",
      description="use x-app-name, target-servicename",
      responses={
          200: {
              "description": "Ok. User created",
              "schema": Message
          },
          401: {
              "description": "Unauthorized"
          },
          422: {
              "description": "Validation error"
          },
          500: {
              "description": "Server error"
          },
      })

async def handle(request: web.Request):
    return web.json_response({"message": request.raw_path})


async def handle_get(request: web.Request):
    
    async with ClientSession() as session:
        async with session.get(f"{request.headers['X-Target-Url']}{request.path}") as resp:
            print(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result


async def handle_post(request: web.Request):
    pass


async def handle_patch(request: web.Request):
    pass


async def handle_put(request: web.Request):
    pass


async def handle_delete(request: web.Request):
    pass
