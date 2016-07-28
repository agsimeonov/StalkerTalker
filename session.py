from copy import copy
from urllib import quote
from urlparse import urlparse, urlunparse, urljoin

from requests.api import get
from requests.sessions import Session

from common import get_data


DEFAULT_HEADER = {
  'Accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 234 Safari/533.3',
  'Connection': 'Keep-Alive',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'en-US,*',
  'X-User-Agent': 'Model: MAG250; Link: WiFi',
}

class StalkerSession(object):
  def __init__(self, portal_uri, mac_address):
    self.session = Session()
    self.portal_uri = portal_uri
    self.mac_address = mac_address
    self.serial_number = '012012N01212'
    self.referer_uri = get(portal_uri).url
    
    parsed = urlparse(self.referer_uri)

    path = parsed.path

    parsed = parsed._replace(path='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')

    self.base_uri = urlunparse(parsed)

    for part in [x for x in path.split('/') if x]:
      self.base_uri = urljoin(self.base_uri, part)
      if part == 'stalker_portal':
        break

    self.base_uri += '/'

    self.referer_uri = urljoin(self.base_uri, 'c/')
    self.load_uri = urljoin(self.base_uri, 'server/load.php')

    cookies = {
      'mac': quote(mac_address),
      'stb_lang': 'en',
      'timezone': quote('America/New_York')
    }

    headers = copy(DEFAULT_HEADER)
    headers['Referer'] = self.referer_uri
    self.session.headers.update(headers)
    self.session.cookies.update(cookies)
    self.session.verify = False

    token = get_data(self._handshake())['token']
    self.session.headers['Authorization'] = 'Bearer ' + token

    self.profile = get_data(self._get_profile())

  def _handshake(self):
    payload = {
      'type': 'stb',
      'action': 'handshake'
    }

    return self.load(payload)

  def _get_profile(self):
    ver = {
      'ImageDescription': '0.2.16-250',
      'ImageDate': '18 Mar 2013 19:56:53 GMT+0200',
      'PORTAL version': '4.9.9',
      'API Version': 'JS API version: 328',
      'STB API version': 134,
      'Player Engine version': '0x566',
    }

    ver = quote(';'.join([":".join([key, ' ' + str(val)]) for key, val in ver.items()]))

    payload = {
      'type': 'stb',
      'action': 'get_profile',
      'hd': 1,
      'sn': self.serial_number,
      'stb_type': 'MAG250',
      'image_version': 216,
      'auth_second_step': 0,
      'JsHttpRequest': '1-xml',
      'hw_version': '1.7-BD-00',
      'num_banks': 1,
      'not_valid_token': 0,
      'device_id': '',
      'device_id2': '',
      'signature': '',
      'ver': ver
    }

    return self.load(payload)

  def load(self, payload):
    return self.session.get(self.load_uri, params= payload)
