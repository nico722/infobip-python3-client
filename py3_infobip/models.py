from typing import List
from py3_infobip.utils.u_dict import clean_null_terms


class SmsTextSimpleBody:
    def __init__(self, **kwargs):
        super().__init__()
        self._from: str = kwargs.get('ffrom', None)
        self._to: List[str] = kwargs.get('to', None)
        self._text: str = kwargs.get('text', None)

    @property
    def ffrom(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def text(self):
        return self._text

    def set_ffrom(self, value: str):
        self._from = value
        return self

    def set_to(self, value: List[str]):
        self._to = value
        return self

    def set_text(self, value: str):
        self._text = value
        return self

    def to_dict(self, with_null_values=False):
        json_value = {
            'from': self.ffrom,
            'to': self.to,
            'text': self.text
        }
        if with_null_values is True:
            return json_value
        return clean_null_terms(json_value)
