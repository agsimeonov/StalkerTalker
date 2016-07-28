from common import pretty


class Television(object):
  def __init__(self, stalker_session):
    self.stalker_session = stalker_session

    self.get_channels()

  def get_channels(self):
    # CREATE CHANNELS CLASS AND GO FROM THERE
    payload = {
      'type': 'itv',
      'action': 'get_all_channels'
    }
#     print self.session.get(self.load_uri, params= payload).json()['js']['data'].values()
#     for x in self.session.get(self.load_uri, params= payload).json()['js']['data'].values():
#       if x:
#         for y in x:
#           print y['name']
    print pretty(self.stalker_session.load(payload).json()['js'])