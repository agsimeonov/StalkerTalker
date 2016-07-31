import codecs


class Playlist(object):
  def __init__(self, television):
    self.television = television
    number_to_id = self.__get_number_to_id(self.television.channels_by_id)
    sorted_numbers = self.__get_sorted(number_to_id.keys())
    self.playlist = "#EXTM3U\n"
    for number in sorted_numbers:
      self.playlist += self.__get_tv_track(number_to_id[number])
    self.write_playlist('/Users/asosako/Desktop/playlist.m3u8')

  def write_playlist(self, filepath):
    with codecs.open(filepath, 'w', encoding='utf8') as output:
      output.write(self.playlist)

  def __get_tv_track(self, identifier):
    channel = self.television.channels_by_id[identifier]
    genre = self.television.genres_by_id[channel[u'tv_genre_id']]
    track = '#EXTINF:-1 tvg-id="' + identifier + '" group-title="' + genre[u'title'].title() + '",' + channel[u'name'] + '\n'
    link = 'http://localhost:55555/tv/' + identifier + '\n'
    return track + link

  def __get_sorted(self, elements):
    digits = []
    nondigits = []
    for x in elements:
      if x.isdigit():
        digits.append(int(x))
      else:
        nondigits.append(x)
    return [str(x).decode('UTF-8') for x in sorted(nondigits) + sorted(digits)]

  def __get_number_to_id(self, channels_by_id):
    result = {}
    for key in channels_by_id.keys():
      result[channels_by_id[key][u'number']] = key
    return result
