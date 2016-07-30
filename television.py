from common import pretty, get_data


class Television(object):
  # TODO: EXTEND SESSIONITE OBJECT HAS STALKER SESSION AND SETS IT.  HAS LOADS METHOD, HAS PAGINATION METHOD
  def __init__(self, stalker_session):
    self.stalker_session = stalker_session
#     self.genres_by_id = self.get_genres_by_id()
#     self.channels_by_id = self.get_channels_by_id()
# 
#     print self.channels_by_id
#     print len(self.channels_by_id)
    print pretty(self.get_ordered_list().json())

#     self.create_link()
#     self.get_epg()

  def create_link(self):
    payload = {
      'type': 'itv',
      'action': 'create_link',
      'cmd': 'ffrt http:///ch/14'
    }
    print pretty(self.load(payload).json())

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
      'p': 5
    }
    return self.load(payload)

  def get_all_channels(self):
    payload = {
      'type': 'itv',
      'action': 'get_all_channels'
    }
    return self.load(payload)

  def get_channels_by_id(self):
    channels_list = get_data(self.get_all_channels())['data']
    return self.get_by_id(channels_list)

  def get_genres(self):
    payload = {
      'type': 'itv',
      'action': 'get_genres'
    }
    return self.load(payload)

  def get_genres_by_id(self):
    genres_list = get_data(self.get_genres())
    return self.get_by_id(genres_list)

  def get_by_id(self, data_list):
    by_id = {}
    for data in data_list:
      by_id[data['id']] = data
    return by_id

  def load(self, payload):
    return self.stalker_session.load(payload)
