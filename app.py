import requests
import json
import pandas as pd
from scrapper.articlescrapper import ArticleScrapper
from scrapper.Article_model import Article


STRATEGY = 'new' # new | relevant | old

scraper = ArticleScrapper()

if __name__ == '__main__':
    # Create a dataframe of articles
    articles_list = scraper.createArticleList()
    df = scraper.createArticleDataFrame(articles_list).fillna(0) #Fillna = replace all none values to 0

    df = df.reindex(index=df.index[::-1]) #inverting the index

    df.to_csv('./datasets/test_article_dataset.csv')
    print("Dataframe successfully updated!")

