from psycopg2 import connect
from psycopg2.extensions import AsIs
from psycopg2.extras import DictCursor


class Database(object):
  def __init__(self):
    try:
      self.connection = connect("dbname='stalker' user='stalker' host='localhost' password='talker'")
    except:
      print "Unable to establish database connection!"
      exit(-1)
    self.cursor = self.connection.cursor(cursor_factory=DictCursor)

  def upsert(self, table, columns, values, conflict):
    statement = 'INSERT INTO ' + table + ' (%s) VALUES %s ON CONFLICT(' + ','.join(conflict) + ') DO UPDATE SET(%s) = %s'
    columns = AsIs(','.join(columns))
    values = tuple(values)
#     print self.cursor.mogrify(statement, (columns, values, columns, values))
    self.cursor.execute(statement, (columns, values, columns, values))

  def upsert_epg(self, epg_entry):
    columns = epg_entry.keys()
    values = [epg_entry[column] for column in columns]
    table = 'epg'
    conflict = ['id']
    self.upsert(table, columns, values, conflict)

  def get_epg(self, channel_id):
    statement = 'SELECT * FROM epg WHERE ch_id=' + str(channel_id)
    self.cursor.execute(statement)
    return [dict(record) for record in self.cursor]

  def commit(self):
    self.connection.commit()
