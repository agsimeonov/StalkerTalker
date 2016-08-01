from client import StalkerClient
from common import get_data


class Guide(StalkerClient):
  def __init__(self, television):
    StalkerClient.__init__(self, television.stalker_session)
    self.television = television

  def get_week(self):
    payload = {
     'type': 'epg',
     'action': 'get_week',
    }
    return self.load(payload)

  def get_days(self):
    week = get_data(self.get_week())
    return [day['f_mysql'] for day in week]

  def get_epg(self, channel_id, day):
    payload = {
      'type': 'epg',
      'action': 'get_simple_data_table',
      'ch_id': channel_id,
      'date': day
    }
    return self.paginate(payload)
