from client import StalkerClient


class Radio(StalkerClient):
  def __init__(self, stalker_session):
    StalkerClient.__init__(self, stalker_session)
    self.radios_by_id = self.get_by_id(self.get_ordered_list())

  def get_ordered_list(self):
    payload = {
      'type': 'radio',
      'action': 'get_ordered_list',
    }
    return self.paginate(payload)
