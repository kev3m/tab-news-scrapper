## This class represents the default structure of a topic found in the website

class Content:
    def __init__(self, title, coments, tabcoins):
        self.title = title
        self.coments = coments
        self.tabcoins = tabcoins
        self.topic = None

    def set_topic(self, topic):
        self.topic = topic

    def getRelevance(coments, tabcoins):
        tabcoin_weight = 0.65
        coment_weight = 0.35

        relevance = (tabcoins * tabcoin_weight) + (coments * coment_weight)
        return relevance 
