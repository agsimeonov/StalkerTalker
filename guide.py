from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring

from pytz import utc

from client import StalkerClient
from common import get_data


class Guide(StalkerClient):
  def __init__(self, television, database):
    StalkerClient.__init__(self, television.stalker_session)
    self.television = television
    self.database = database

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

  def generate_xmltv(self):
    parent = Element('tv')
    self.generate_xmltv_channels(parent)
    self.generate_xmltv_programmes(parent)
    return tostring(parent, encoding='utf8', method='xml')

  def generate_xmltv_channels(self, parent):
    for key in self.television.channels_by_id.keys():
      channel_attributes = { 'id': key }
      channel = SubElement(parent, 'channel', channel_attributes)
      display_name = SubElement(channel, 'display-name')
      display_name.text = self.television.channels_by_id[key]['name']

  def generate_xmltv_programmes(self, parent):
    programmes = self.database.get_epg(10)
    for element in programmes:
      start = datetime.fromtimestamp(element['start_timestamp'], tz=utc)
      stop = datetime.fromtimestamp(element['stop_timestamp'], tz=utc)
      start = self.format_time(start)
      stop = self.format_time(stop)
      attributes = {
        'start': start,
        'stop': stop,
        'channel': str(element['ch_id'])
      }
      programme = SubElement(parent, 'programme', attributes)
      title = SubElement(programme, 'title')
      title.text = element['name'].decode('utf8')
      if element['descr'].decode('utf8'):
        description = SubElement(programme, 'description')
        description.text = element['descr'].decode('utf8')

  def format_time(self, programme_datetime):
    return programme_datetime.strftime('%Y%m%d%H%M%S %z')

  def write_guide(self, filepath):
    with open(filepath, 'w') as output:
      output.write(self.generate_xmltv())
