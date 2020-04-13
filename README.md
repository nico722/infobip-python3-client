# Infobip Python3 client
[![PyPI version](https://badge.fury.io/py/py3-infobip.svg)](https://pypi.org/project/py3-infobip/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/py3-infobip.svg)](https://pypi.org/project/py3-infobip/)
[![PyPI license](https://img.shields.io/pypi/l/py3-infobip.svg)](https://pypi.org/project/py3-infobip/)

## Description

A simple python3 client for [infobip service](https://www.infobip.com/)

Infobip is a client communication service with a [REST api](https://dev.infobip.com/), sadly they do not have an python3 client and my attemp to use the 2to3 library to transform the [infobip python2 client](https://github.com/infobip/infobip-api-python-client) failed.

This is why a simple python3 client that could consume the infobip API functionalities was needed

## Dependencies

- Python3.7+

## Installation

```
pip install py3-infobip
```

## Getting Started

If you want to send a text sms to your clients all you need is a list of phone numbers and the message you want to send.  

```
from py3_infobip import (
    SmsClient,
    SmsTextSimpleBody
)

message = SmsTextSimpleBody()
message \
    .set_to([
        '<phone_number>'
    ]) \
    .set_text('some text')

infobip_client = SmsClient(
    url='<infobip_url>',
    api_key='<infobip_apikey>'
)
response = infobip_client.send_sms_text_simple(message)
print(response.json())
```
