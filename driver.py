from common import pretty, get_data
from database import Database
from guide import Guide
from playlist import Playlist
from radio import Radio
from session import StalkerSession
from television import Television


mac_address = '00:1A:79:C1:D4:2F'
portal_uri = 'http://localhost'

stalker_session = StalkerSession(portal_uri, mac_address)
television = Television(stalker_session)
radio = Radio(stalker_session)
playlist = Playlist(television, radio)
playlist.write_playlist('/Users/asosako/Desktop/playlist.m3u8')
database = Database()

database.cursor.close()
database.connection.close()
