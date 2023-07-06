import requests
import pandas as pd
from scrapper.Article_model import Article

class ArticleScrapper(object):

    def __init__(self):
        # Store articles in object format
        self.articles_list = []
        # Store articles in dict format
        self.articles_dict_list = []


    def createArticleList(self):
        """
        Create a list of objects of type "Article"

        """
        base_url = 'https://www.tabnews.com.br/api/v1/contents'
        per_page = 5
        strategy = 'new'


        articles_list = []
        
        #Range defines the number of pages
        for page in range(1,2):
            url = f'{base_url}?page={page}&per_page={per_page}&strategy={strategy}'
            response = requests.get(url)
            articles = response.json()

            for item in articles:
                new_object = Article(item.get('title'), item.get('children_deep_count'), item.get('tabcoins'))
                articles_list.append(new_object)

        return articles_list
    
    def createArticleDataFrame(self, articlesList):
        """
        Transform article list into dataframe
        """
        articles = articlesList
        articles_dict_list = []

        for article in articles: articles_dict_list.append(article.__dict__)
        articles_df = pd.DataFrame(articles_dict_list)
        return articles_df
        




    

