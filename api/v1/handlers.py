from aiohttp import web, ClientSession
from aiohttp.web import Response
from urllib.parse import urlparse
from config.template import EXCLUDED_HEADERS
import logging

def clear_headers(headers):
    if 'Host' in headers:
        headers['Host'] = urlparse(headers['X-Target-Url']).hostname
    for header in EXCLUDED_HEADERS:
        if header in headers:
            headers.pop(header)
    return headers

async def handle_get(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers =  clear_headers(dict(request.headers))
    path = request.path if request.path!='/' else ''
    async with ClientSession() as session:
        async with session.get(f"{target_url}{path}", headers=headers) as resp:
            logging.info(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result


async def handle_post(request: web.Request)-> Response:
    target_url = request.headers['X-Target-Url']
    headers =  clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path!='/' else ''
    async with ClientSession() as session:
        async with session.post(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result



async def handle_patch(request: web.Request)-> Response:
    target_url = request.headers['X-Target-Url']
    headers =  clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path!='/' else ''
    async with ClientSession() as session:
        async with session.patch(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result



async def handle_put(request: web.Request)-> Response:
    target_url = request.headers['X-Target-Url']
    headers =  clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path!='/' else ''
    async with ClientSession() as session:
        async with session.put(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result



async def handle_delete(request: web.Request)-> Response:
    target_url = request.headers['X-Target-Url']
    headers =  clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path!='/' else ''
    async with ClientSession() as session:
        async with session.delete(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers =  clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(
                body=resp._body,
                status=resp.status,
                reason=resp.reason,
                headers=headers
            )
            return result

