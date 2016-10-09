from clarifai.client import ClarifaiApi
import wikipedia
import json

def get_name(image):
    guess = get_nth_json_result(get_json_obj_remote(image), 0)
    return guess

'''
def get_json_obj_local(filename):
    api = ClarifaiApi();
    result = api.tag_images(open(filename), "rb")
    return json.dumps(result)
'''

def get_json_obj_remote(url):
    api = ClarifaiApi("GniW5mCUYJX8b11rI8VnoLncgwUeORRNkl9R-q_J", "H-YPKDaogchMM7Wv6hKIC2qTA9uqXy9tWjxZXFJn")
    result = api.tag_image_urls(url)
    return json.dumps(result)

def get_nth_json_result(json_obj, n):
    obj = json.loads(json_obj)
    return obj["results"][0]["result"]["tag"]["classes"][n]

def get_wikipedia_desc(tag):
    page = ""
    try:
        page = wikipedia.summary(tag, 1)
    except wikipedia.exceptions.DisambiguationError as e:
        page = wikipedia.summary(e.options[0], 1);
    return page
