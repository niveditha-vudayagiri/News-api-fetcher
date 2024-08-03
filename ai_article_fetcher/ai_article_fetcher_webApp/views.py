from django.shortcuts import render
from .api_integ import APIInteg

def index(request):

    query = "Artificial Intelligence"
    page = int(request.GET.get('page', 1))
    start = (page - 1) * 10+ 1

    articles = APIInteg.fetch_articles(query, start)
    items = articles.get('items', [])[:10]

    # Filter out items with null values for image, title, or url
    filtered_items = [item for item in items if item.get('title') and item.get('pagemap', {}).get('cse_image', [{}])[0].get('src')]

    # Extract details from the articles
    titles = [item.get('title') for item in filtered_items]
    descriptions = [item.get('snippet') for item in filtered_items]
    links = [item.get('link') for item in filtered_items]
    publishers = [item.get('displayLink') for item in filtered_items]
    images = [item.get('pagemap', {}).get('cse_image', [{}])[0].get('src') for item in filtered_items]

    context = {'articles': zip(titles, descriptions, links, publishers,images),'page': page,'has_next': 'nextPage' in articles.get('queries', {})}
    return render(request, 'index.html', context)

def disp_news(request):
    query = "Artificial Intelligence"
    page = int(request.GET.get('page', 1))
    start = (page - 1) * 2+ 1

    #Fetch News
    articles = APIInteg.fetch_news(query, start)
    items = articles.get('articles', [])[:2]

    # Filter out items with null values for image, title, or url
    filtered_items = [item for item in items if item.get('title') and item.get('url') and item.get('urlToImage')]

    # Extract details from the articles
    titles = [item.get('title') for item in filtered_items]
    description = [item.get('description') for item in filtered_items]
    links = [item.get('url') for item in filtered_items]
    author = [item.get('author') for item in filtered_items]
    image = [item.get('urlToImage') for item in filtered_items]

    
    #Fetch Headlines
    head_start = (page-1)*10+1
    headlines = APIInteg.headlines(query, head_start)
    headline_items = headlines.get('articles', [])[:10]

    # Extract details from the articles
    headline_title = [item.get('title') for item in headline_items]
    headline_description = [item.get('description') for item in headline_items]
    headline_links = [item.get('url') for item in headline_items]
    headline_author = [item.get('author') for item in headline_items]
    headline_time = [item.get('publishedAt') for item in headline_items]

    context = {'news': zip(titles, description, links, author,image),
               'headlines':zip(headline_title,headline_description,headline_links,headline_author,headline_time)}

    return render(request, 'disp_news.html', context)