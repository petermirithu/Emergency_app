import urllib.request,json
from .models import Article, Category, Source , Headlines

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
cat_url= None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key ='d375c375d9414540b4b87ffc36728e98'
    source_url= app.config['NEWS_API_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']

def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format('d375c375d9414540b4b87ffc36728e98')
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results
    