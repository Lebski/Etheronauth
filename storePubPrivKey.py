from etheronauth import secrethandling
from etheronauth import tools

keys = tools.get_json("jwt_keys.json")
secrethandling.write_json_to_file("TestTestTest", "jwt_keys.secure", keys)
