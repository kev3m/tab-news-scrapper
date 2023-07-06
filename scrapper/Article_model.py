## This class represents the default structure of a topic found in the website

class Article:
    def __init__(self, title, coments, tabcoins):
        self.title = title
        self.coments = coments
        self.tabcoins = tabcoins
        self.relevance = None
        self.topic = None

    def setTopic(self, topic):
        self.topic = topic

    def setRelevance(self):
        tabcoin_weight = 0.65
        coment_weight = 0.35

        self.relevance = (self.tabcoins * tabcoin_weight) + (self.coments * coment_weight)
        
