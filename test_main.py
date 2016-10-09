from ai_client import *
import json
from StringIO import StringIO

obj = AICLIENT_get_json_obj_remote("https://staticdelivery.nexusmods.com/mods/110/images/74627-0-1459502036.jpg")

tag = AICLIENT_get_nth_json_result(obj, 0)

print AICLIENT_get_wikipedia_desc(tag)
