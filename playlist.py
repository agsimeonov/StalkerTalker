import codecs


class Playlist(object):
  def __init__(self, television):
    self.television = television
    channel_ids = self.__get_sorted_ids(self.television.channels_by_id)
    self.playlist = "#EXTM3U\n"
    for identifier in channel_ids:
      self.playlist += self.__get_tv_track(identifier)
    self.write_playlist('/Users/asosako/Desktop/playlist.m3u8')

  def write_playlist(self, filepath):
    with codecs.open(filepath, 'w', encoding='utf8') as output:
      output.write(self.playlist)

  def __get_tv_track(self, identifier):
    channel = self.television.channels_by_id[identifier]
    genre = self.television.genres_by_id[channel[u'tv_genre_id']]
    track = '#EXTINF:-1 tvg-id="' + identifier + '" group-title="' + genre[u'title'].title() + '",' + channel[u'name'] + '\n'
    link = 'http://localhost:5555/tv/' + identifier + '\n'
    return track + link

  def __get_sorted_ids(self, ids):
    digits = []
    nondigits = []
    for x in ids:
      if x.isdigit():
        digits.append(int(x))
      else:
        nondigits.append(x)
    return [str(x).decode('UTF-8') for x in sorted(nondigits) + sorted(digits)]
