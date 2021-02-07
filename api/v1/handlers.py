from aiohttp import web, ClientSession
from aiohttp.web import Response
from urllib.parse import urlparse
from config.template import EXCLUDED_HEADERS
import logging
import functools

stat_cache = {}


def collect_statistics():
    """
    Return the statistics of REST api requests to external servers.
    Example:
    curl -X GET  "http://0.0.0.0:8080/statistics"
    {'https://httpbin.org/anything': {'PUT': {'/': 2}, 'PATCH': {'/': 1}}}%
    """
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args):
            if not stat_cache.get(args[0].headers['X-Target-Url']):
                stat_cache[args[0].headers['X-Target-Url']] = {}
            if not stat_cache[args[0].headers['X-Target-Url']].get(args[0].method):
                stat_cache[args[0].headers['X-Target-Url']][args[0].method] = {}
            if not stat_cache[args[0].headers['X-Target-Url']][args[0].method].get(args[0].path):
                stat_cache[args[0].headers['X-Target-Url']][args[0].method][args[0].path] = 0
            stat_cache[args[0].headers['X-Target-Url']][args[0].method][args[0].path] += 1
            return await func(*args)

        return wrapped

    return wrapper


def clear_headers(headers):
    if 'Host' in headers:
        headers['Host'] = urlparse(headers['X-Target-Url']).hostname
    for header in EXCLUDED_HEADERS:
        if header in headers:
            headers.pop(header)
    return headers


@collect_statistics()
async def handle_get(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers = clear_headers(dict(request.headers))
    path = request.path if request.path != '/' else ''
    async with ClientSession() as session:
        async with session.get(f"{target_url}{path}", headers=headers) as resp:
            logging.info(resp.status)
            headers = clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(body=resp._body, status=resp.status, reason=resp.reason, headers=headers)
            return result


@collect_statistics()
async def handle_post(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers = clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path != '/' else ''
    async with ClientSession() as session:
        async with session.post(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers = clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(body=resp._body, status=resp.status, reason=resp.reason, headers=headers)
            return result


@collect_statistics()
async def handle_patch(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers = clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path != '/' else ''
    async with ClientSession() as session:
        async with session.patch(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers = clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(body=resp._body, status=resp.status, reason=resp.reason, headers=headers)
            return result


@collect_statistics()
async def handle_put(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers = clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path != '/' else ''
    async with ClientSession() as session:
        async with session.put(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers = clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(body=resp._body, status=resp.status, reason=resp.reason, headers=headers)
            return result


@collect_statistics()
async def handle_delete(request: web.Request) -> Response:
    target_url = request.headers['X-Target-Url']
    headers = clear_headers(dict(request.headers))
    data = await request.json()
    path = request.path if request.path != '/' else ''
    async with ClientSession() as session:
        async with session.delete(f"{target_url}{path}", headers=headers, data=data) as resp:
            logging.info(resp.status)
            headers = clear_headers(dict(resp.headers))
            await resp.text()
            result = web.Response(body=resp._body, status=resp.status, reason=resp.reason, headers=headers)
            return result


async def statistics(request: web.Request) -> Response:
    result = web.Response(text=str(stat_cache))
    return result
