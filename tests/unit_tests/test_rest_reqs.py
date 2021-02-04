from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
from app import create_app
from parameterized import parameterized
import json


class BaseTestClass(AioHTTPTestCase):
    """Set up server for testing"""
    async def get_application(self):
        return create_app()

    @parameterized.expand([
                ({'args': {}, 'data': 'hello=dsad', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '10', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'Python/3.8 aiohttp/3.7.3'}, 'json': None, 'method': 'PATCH', 'origin': '188.32.187.63', 'url': 'https://httpbin.org/anything'}, "PATCH", '/', {
            "X-Target-Url": "https://httpbin.org/anything"
        }, {
            'hello': 'dsad'
        }),
        ({'args': {}, 'data': 'hello=dsad', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '10', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'Python/3.8 aiohttp/3.7.3'}, 'json': None, 'method': 'PUT', 'origin': '188.32.187.63', 'url': 'https://httpbin.org/anything'}, "PUT", '/', {
            "X-Target-Url": "https://httpbin.org/anything"
        }, {
            'hello': 'dsad'
        }),
        ({
            'args': {},
            'data': 'hello=dsad',
            'files': {},
            'form': {},
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Length': '10',
                'Content-Type': 'application/json',
                'Host': 'httpbin.org',
                'User-Agent': 'Python/3.8 aiohttp/3.7.3'
            },
            'json': None,
            'method': 'POST',
            'origin': '188.32.187.63',
            'url': 'https://httpbin.org/anything'
        }, "POST", '/', {
            "X-Target-Url": "https://httpbin.org/anything"
        }, {
            'hello': 'dsad'
        }),
                    ({
            'args': {},
            'data': '',
            'files': {},
            'form': {},
            'headers': {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'httpbin.org',
                'User-Agent': 'Python/3.8 aiohttp/3.7.3'
            },
            'json': None,
            'method': 'GET',
            'origin': '188.32.187.63',
            'url': 'https://httpbin.org/anything'
        }, "GET", '/', {"X-Target-Url": "https://httpbin.org/anything"}, None)
    ])
    @unittest_run_loop
    async def test_example_get(self, output, method, url, headers, data):
        resp = await self.client.request(method, url, headers=headers, json=data)
        assert resp.status == 200
        text = await resp.text()
        res_text = json.loads(text)
        res_text['headers'].pop('X-Amzn-Trace-Id')
        assert res_text == output
