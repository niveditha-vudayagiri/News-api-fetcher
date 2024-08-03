# AI News Aggregator

AI News Aggregator is a Django-based web application that fetches and displays articles related to "Artificial Intelligence" using Google Search API and NewsAPI. This project demonstrates the integration of multiple APIs within a Django framework to provide a seamless user experience for accessing the latest AI news.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Environment Variables](#set-up-environment-variables)
  - [Run Migrations](#run-migrations)
  - [Run the Development Server](#run-the-development-server)
- [APIs Used](#apis-used)
  - [Google Search API](#google-search-api)
  - [NewsAPI](#newsapi)

## Prerequisites
- Python 3.x
- Django 3.x or higher
- Git

## Setup

### Clone the Repository
git clone https://github.com/yourusername/ai-news-aggregator.git
cd ai-news-aggregator


### Create a Virtual Environment
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install Dependencies
pip install -r requirements.txt

### Set Up Environment Variables
- GOOGLE_API_KEY=your_google_api_key
- GOOGLE_CX=your_google_cx
- NEWSAPI_KEY=your_newsapi_key

### Run Migrations
python manage.py migrate

### Run the Development Server
python manage.py runserver

## APIs Used

### Google Search API
The Google Search API is used to fetch articles related to “Artificial Intelligence” from across the web. The API returns search results, including titles, descriptions, URLs, publishers, and images. To use this API, you need:

	•	An API key
	•	A custom search engine ID (CX)

Refer to the [Google Custom Search JSON API documentation](https://developers.google.com/custom-search/v1/overview) for more details.

### NewsAPI

NewsAPI is used to fetch the latest news articles related to “Artificial Intelligence” from various news sources. The API provides article titles, descriptions, URLs, authors, and images. To use this API, you need an API key.

Refer to the [NewsAPI documentation](https://newsapi.org/docs/get-started) for more details.

### Adding Pagination
To navigate through pages, use the “Previous Page” and “Next Page” links at the bottom of the page.


