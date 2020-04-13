from unittest import TestCase
from py3_infobip.models import (
    SmsTextSimpleBody
)


class TestSmsTextSimpleBody(TestCase):
    def setUp(self):
        super().setUp()
        self.ffrom = 'some_ffrom'
        self.to = ['some_to']
        self.text = 'some_text'

    def test_init(self):
        service = SmsTextSimpleBody(ffrom=self.ffrom, to=self.to, text=self.text)
        self.assertEqual(self.ffrom, service.ffrom)
        self.assertEqual(self.to, service.to)
        self.assertEqual(self.text, service.text)

    def test_set_methods(self):
        service = SmsTextSimpleBody()
        service \
            .set_ffrom(self.ffrom) \
            .set_to(self.to) \
            .set_text(self.text)
        self.assertEqual(self.ffrom, service.ffrom)
        self.assertEqual(self.to, service.to)
        self.assertEqual(self.text, service.text)

    def test_to_dict(self):
        service = SmsTextSimpleBody(ffrom=self.ffrom, to=self.to, text=self.text)
        self.assertDictEqual(service.to_dict(), {'from': self.ffrom, 'to': self.to, 'text': self.text})

    def test_to_dict_non_null_values(self):
        service = SmsTextSimpleBody(ffrom=self.ffrom, to=self.to, text=None)
        self.assertDictEqual(service.to_dict(), {'from': self.ffrom, 'to': self.to})

    def test_to_dict_with_null_values(self):
        service = SmsTextSimpleBody(ffrom=self.ffrom, to=self.to, text=None)
        self.assertDictEqual(service.to_dict(with_null_values=True), {'from': self.ffrom, 'to': self.to, 'text': None})
