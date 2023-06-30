import requests
import json
import pandas as pd
from scrapper.articlescrapper import ArticleScrapper
from scrapper.article import Article


scraper = ArticleScrapper()

# Create a dataframe of articles
articles_list = scraper.createArticleList()
df = scraper.createArticleDataFrame(articles_list).fillna(0) #Fillna = replace all none values to 0
df.to_csv('./datasets/article_dataset.csv')


