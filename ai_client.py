from clarifai.client import ClarifaiApi

def AICLIENT_get_json_obj_local(filename):
    api = ClarifaiApi();
    result = api.tag_images(open(filename), "rb")
    return result

def AICLIENT_get_json_obj_remote(url):
    api = ClarifaiApi()
    result = api.tag_image_urls(url);
    return result
