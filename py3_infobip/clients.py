import requests
from py3_infobip.models import SmsTextSimpleBody


class InfobipService:
    def __init__(self, url: str, api_key: str, **kwargs):
        super().__init__()
        self._sesion = requests.Session()
        url = (url or '').strip()
        url = url if url[-1:] != '/' else url[:-1]
        self._url = url
        self._api_key = api_key
        self._auth_prefix = kwargs.get('auth_prefix', 'App')
        self._content_type = kwargs.get('content_type', 'application/json')
        self._sesion.headers.update({'Authorization': f'{self._auth_prefix} {self._api_key}'})
        self._sesion.headers.update({'Content-Type': f'{self._content_type}'})
        self._sesion.headers.update({'accept': 'application/json'})

    def _post(self, method_url: str, body: dict, options: dict = {}):
        return self._sesion.post(url=f'{self._url}/{method_url}', json=body, **options)


class SmsClient(InfobipService):
    def send_sms_text_simple(self, body: SmsTextSimpleBody):
        return self._post('sms/1/text/single', body.to_dict())
