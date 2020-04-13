import re
import requests_mock
from unittest import TestCase
from py3_infobip.clients import (
    InfobipService,
    SmsClient
)
from py3_infobip.models import (
    SmsTextSimpleBody
)
from tests.mock_data.sms_responses import (
    sms_simple_success,
    sms_simple_error
)


class TestInfobipService(TestCase):
    def test_init(self):
        url = 'some_url'
        api_key = 'some_api_key'
        auth_prefix = 'some_auth_prefix'
        service = InfobipService(url, api_key, auth_prefix=auth_prefix)
        self.assertEqual(url, service._url)
        self.assertEqual(api_key, service._api_key)
        self.assertEqual(auth_prefix, service._auth_prefix)


class TestSmsClient(TestCase):
    def setUp(self):
        super().setUp()
        self.url = 'http://some_url.com'
        self.api_key = 'some_api_key'
        self.auth_prefix = 'some_auth_prefix'
        self.service = SmsClient(self.url, self.api_key, auth_prefix=self.auth_prefix)

    @requests_mock.Mocker()
    def test_send_sms_text_simple_success(self, m: requests_mock.Mocker):
        ffrom = 'InfoFrubana'
        to = ['573000000000']
        text = 'Some test example message'

        re_sms = re.compile('sms/')
        m.post(re_sms, json=sms_simple_success)

        msg = SmsTextSimpleBody(
            ffrom=ffrom,
            to=to,
            text=text
        )
        res = self.service.send_sms_text_simple(msg)
        message = res.json().get('messages', [])[0] or {}
        self.assertEqual(message['to'], to[0])
