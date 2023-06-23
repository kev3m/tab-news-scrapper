import requests
import pandas as pd
from article import Article

class ContentScrapper(object):

    def __init__(self):
        # Store articles in object format
        self.articles_list = []
        # Store articles in dict format
        self.articles_dict_list = []


    def createArticleList(self):
        """
        Create a list of objects of type "Article"

        """
        domain = 'tabnews.com.br/ww.tabnews.com.br/api/v1/contents/'
        response = requests.get(domain)
        articles = response.json()

        for item in articles:
            new_object = Article(item.get('title'), item.get('children_deep_count'), item.get('tabcoins'))
            self.articles_list.append(new_object)

        return self.articles_list
    
    def createArticleDataFrame(self):
        """
        Transform article list into dataframe
        """
        for article in self.articles_list: self.articles_dict_list.append(article.__dict__)
        articles_df = pd.DataFrame(self.articles_dict_list, columns=['Título','Comentarios','Tabcoins', 'Tópico'])
        return articles_df
        




    

