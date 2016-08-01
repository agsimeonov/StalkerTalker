import os

from flask import Flask, redirect

from common import get_data
from playlist import Playlist
from radio import Radio
from session import StalkerSession
from television import Television


mac_address = '00:1A:79:00:00:00'
portal_uri = 'http://local'

stalker_session = StalkerSession(portal_uri, mac_address)
television = Television(stalker_session)
stalker_radio = Radio(stalker_session)
playlist = Playlist(television, stalker_radio)
playlist.write_playlist('/Users/asosako/Desktop/playlist.m3u8')

app = Flask(__name__)

@app.route('/tv/<identifier>', methods=['GET'])
def tv(identifier):
  channel = television.channels_by_id[str(identifier).decode('UTF-8')]
  data = get_data(television.create_link(channel[u'cmd']))
  link = data[u'cmd']
  if not link:
    link = 'http://149.13.0.80/nrj128.m3u'
  return redirect(link, code=302)

@app.route('/radio/<identifier>', methods=['GET'])
def radio(identifier):
  station = stalker_radio.radios_by_id[str(identifier).decode('UTF-8')]
  link = station[u'cmd']
  if not link:
    link = 'http://149.13.0.80/nrj128.m3u'
  return redirect(link, code=302)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 55555))
  app.run(host='0.0.0.0', port=port)
