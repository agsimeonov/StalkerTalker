from session import StalkerSession
from television import Television


mac_address = '00:1A:79:C1:D4:2F'
portal_uri = 'http://localhost'

stalker_session = StalkerSession(portal_uri, mac_address)
television = Television(stalker_session)
