from json import dumps


def get_data(response):
  return response.json()['js']

def pretty(data):
  return dumps(data, indent=2, sort_keys=True)
