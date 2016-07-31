from common import pretty, get_data
from client import StalkerClient


class Television(StalkerClient):
  def __init__(self, stalker_session):
    StalkerClient.__init__(self, stalker_session)
    self.genres_by_id = self.get_genres_by_id()
    self.channels_by_id = self.get_by_id(self.get_ordered_list())

  def create_link(self, cmd):
    payload = {
      'type': 'itv',
      'action': 'create_link',
      'cmd': cmd
    }
    return self.load(payload)

  def get_epg(self):
    payload = {
      'type': 'itv',
      'action': 'get_epg_info',
      'xmltv_id': '1.30_14'
    }
    print pretty(self.load(payload).json())

  def get_ordered_list(self):
    payload = {
      'type': 'itv',
      'action': 'get_ordered_list',
    }
    return self.paginate(payload)

  def get_all_channels(self):
    payload = {
      'type': 'itv',
      'action': 'get_all_channels'
    }
    return self.load(payload)

  def get_genres(self):
    payload = {
      'type': 'itv',
      'action': 'get_genres'
    }
    return self.load(payload)

  def get_genres_by_id(self):
    genres_list = get_data(self.get_genres())
    return self.get_by_id(genres_list)
