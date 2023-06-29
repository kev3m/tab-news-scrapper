import requests
import json
import pandas as pd
from scrapper.articlescrapper import ArticleScrapper
from scrapper.article import Article


scraper = ArticleScrapper()
articles_list = scraper.createArticleList()


df = scraper.createArticleDataFrame(articles_list)

print(df)

