import requests
import pandas as pd
from scrapper.Article_model import Article

class ArticleScrapper(object):

    def __init__(self):
        self.base_url = 'https://www.tabnews.com.br/api/v1/contents'

    def createArticleList(self):
        """
        Create a list of objects of type "Article"

        """
        page = 1
        per_page = 100 #Limit per page = 100
        strategy = 'old'


        articles_list = []
        response_empty = False

        while not response_empty:
            url = f'{self.base_url}?page={page}&per_page={per_page}&strategy={strategy}'
            print(url)
            response = requests.get(url)
            articles = response.json()

            if not articles:  # Verifica se a resposta está vazia
                response_empty = True
            else:
                for item in articles:
                    new_object = Article(item.get('title'), item.get('children_deep_count'), item.get('tabcoins'))
                    new_object.setRelevance()
                    articles_list.append(new_object)

                page += 1

        return articles_list
    
    def updateArticleList(self):
        """
        Create a list of objects of type "Article"

        """
        base_url = 'https://www.tabnews.com.br/api/v1/contents'
        ## ------- AJUSTAS PARAMETROS ----------
        per_page = 100 #Limit per page = 100
        strategy = 'new'


        updated_articles_list = []
        
        #Range defines the number of pages
        for page in range(1,2):
            url = f'{base_url}?page={page}&per_page={per_page}&strategy={strategy}'
            response = requests.get(url)
            articles = response.json()

            for item in articles:
                new_object = Article(item.get('title'), item.get('children_deep_count'), item.get('tabcoins'))
                new_object.setRelevance()
                updated_articles_list.append(new_object)

        return updated_articles_list

    
    def createArticleDataFrame(self, articlesList):
        """
        Transform article list into dataframe
        """
        articles = articlesList
        articles_dict_list = []

        for article in articles: articles_dict_list.append(article.__dict__)
        articles_df = pd.DataFrame(articles_dict_list)
        return articles_df
    
    def updateArticleDataFrame(self):
        df = pd.read_csv("./dasets/article_dataset.csv")


         
         
    






    

