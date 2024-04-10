import pytest
import requests
from datetime import datetime


@pytest.mark.integration_tests
class TestApplication:
    @pytest.mark.parametrize("suffix,additional_headers", [
        ('/', {'Content-Length': '589'}),
        ('/files', {'Content-Length': '69'}),
        ('/login', {'Content-Length': '153', 'Allow': 'POST, OPTIONS'})
    ])
    def test_headers(self, suffix, additional_headers):
        headers_for_all = {
            "Server": 'Werkzeug/3.0.2 Python/3.10.12',
            "Content-Type": 'text/html; charset=utf-8',
            "Connection": 'close'
        }
        url = f'http://ci-cd-app:5000{suffix}'
        try:
            actual = requests.get(url).headers
        except requests.exceptions.RequestException as e:
            assert False, f"Can't GET: {url=}. {e}"
        for header, expected in (headers_for_all | additional_headers).items():
            assert header in actual, f'Missing {header=}'
            assert expected == actual[header], f'{expected=}, {actual[header]=}'

        # Check Date header:
        assert 'Date' in actual, f'Missing "Date" header'
        try:
            actual_date = datetime.strptime(actual['Date'], '%a, %d %b %Y %H:%M:%S %Z')
        except ValueError as e:
            assert False, f"Can't parse 'Date' header: {actual['Date']}. {e}"
        assert abs((datetime.utcnow() - actual_date).seconds) < 10, \
            f'Incorrect "Date" header: {datetime.utcnow()}, {actual_date}'
