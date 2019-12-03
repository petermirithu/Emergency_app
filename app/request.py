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


    