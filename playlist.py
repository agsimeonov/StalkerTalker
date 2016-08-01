import codecs


class Playlist(object):
  def __init__(self, television, radio):
    self.television = television
    self.radio = radio
    self.playlist = "#EXTM3U\n"
    self.populate_playlist(self.television.channels_by_id, self.__get_tv_track)
    self.populate_playlist(self.radio.radios_by_id, self.__get_radio_track)

  def write_playlist(self, filepath):
    with codecs.open(filepath, 'w', encoding='utf8') as output:
      output.write(self.playlist)

  def __get_tv_track(self, identifier):
    channel = self.television.channels_by_id[identifier]
    genre = self.television.genres_by_id[channel[u'tv_genre_id']]
    track = '#EXTINF:-1 tvg-id="' + identifier + '" group-title="' + genre[u'title'].title() + '",' + channel[u'name'] + '\n'
    link = 'http://localhost:55555/tv/' + identifier + '\n'
    return track + link

  def __get_radio_track(self, identifier):
    radio = self.radio.radios_by_id[identifier]
    track = '#EXTINF:-1 radio=true group-title="Radio",' + radio[u'name'] + '\n'
    link = 'http://localhost:55555/radio/' + identifier + '\n'
    return track + link

  def populate_playlist(self, items_by_id, get_track_callback):
    number_to_id = self.__get_number_to_id(items_by_id)
    sorted_numbers = self.__get_sorted(number_to_id.keys())
    for number in sorted_numbers:
      self.playlist += get_track_callback(number_to_id[number])

  def __get_sorted(self, elements):
    digits = []
    nondigits = []
    for x in elements:
      if x.isdigit():
        digits.append(int(x))
      else:
        nondigits.append(x)
    return [str(x).decode('UTF-8') for x in sorted(nondigits) + sorted(digits)]

  def __get_number_to_id(self, items_by_id):
    result = {}
    for key in items_by_id.keys():
      result[items_by_id[key][u'number']] = key
    return result
