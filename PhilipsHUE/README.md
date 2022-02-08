### Minimal description


https://pypi.org/project/hue-py/

pip install hue-py

# PS. The 

# First timeyou run this. For this to succeed, you must first press the link button on the bridge.
from hue_api import HueApi
api = HueApi()
api.create_new_user(bridge_ip_address)



# After pairing

from hue_api import HueApi
api = HueApi()
api.load_existing()

api.fetch_lights()
api.list_lights()
