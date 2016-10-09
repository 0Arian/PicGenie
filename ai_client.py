from clarifai.client import ClarifaiApi
import wikipedia
import json

def AICLIENT_get_json_obj_local(filename):
    api = ClarifaiApi();
    result = api.tag_images(open(filename), "rb")
    return json.dumps(result)

def AICLIENT_get_json_obj_remote(url):
    api = ClarifaiApi()
    result = api.tag_image_urls(url);
    return json.dumps(result)

def AICLIENT_get_nth_json_result(json_obj, n):
    obj = json.loads(json_obj)
    return obj["results"][0]["result"]["tag"]["classes"][n]

def AICLIENT_get_wikipedia_desc(tag):
    page = wikipedia.summary(tag, 1)
    return page

