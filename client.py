from common import get_data


class StalkerClient(object):
  def __init__(self, stalker_session):
    self.stalker_session = stalker_session

  def paginate(self, payload):
    payload['p'] = 1
    result = []

    while True:
      data = get_data(self.load(payload))['data']
      if not data:
        break
      result += data
      payload['p'] = payload['p'] + 1

    return result

  def load(self, payload):
    return self.stalker_session.load(payload)

  def get_by_id(self, data_list):
    by_id = {}
    for data in data_list:
      by_id[data['id']] = data
    return by_id
