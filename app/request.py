import urllib.request,json
from .models import Article,Location

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
cat_url= None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['NEWS_API_KEY']    
    cat_url=app.config['CAT_API_URL']

def article_source():
    article_source_url=cat_url.format(api_key)    
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results

def location():
        # api_key="aef2987237152b5a1f74a260bdc84c91"
        # send_url ='http://api.ipstack.com/172.30.39.151?access_key={}'

        # loc=send_url.format(api_key)    
        loc='http://api.ipstack.com/105.27.206.46?access_key=aef2987237152b5a1f74a260bdc84c91'
        with urllib.request.urlopen(loc) as url:
                data1= url.read()
                response = json.loads(data1)        

                results=process_location(response)          
                
        return results

def process_location(item):
  '''
  function that processes the response from json format
  '''
  results=[]
  
  latitude=item.get('latitude')
  longitude=item.get('longitude')

  loc_object=Location(latitude,longitude)
  results.append(loc_object)

  return results  



