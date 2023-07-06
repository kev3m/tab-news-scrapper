import g4f
import re
import pandas as pd
# from dotenv import 

## print(g4f.Provider.Ails.params)

# #Loading ambient variables
# load_dotenv()

# """
# Classification tool assigns scored categories to bodies of text based on a category list you define.
# Enables a model to classify unseen classes by leveraging transfer learning and its understanding of related concepts.

# """


#Loading csv dataset
df = pd.read_csv('datasets\\article_dataset.csv')

title_column = 'title'
categories = {1: 'Desenvolvimento e programação', 2: 'Hospedagem e infraestrutura', 3: 'Web e design', 4: 'Aprendizado e experiências', 5: 'Open source e comunidade', 6: 'Jogos e entretenimento'}


#Iterating over the dataset
for index,row in df.iterrows():

    article_title = row[title_column]
    #Prompt used in chatGPT model
    prompt_sequency = f"Classifique o artigo com base no titulo: '{article_title}' em uma das seguintes categorias: '{categories.items()}. Responda SOMENTE com o número equivalente a categoria."
    # prompt_sequency = "Quanto é 30 + 20?"
    
    try:
        chat_completion = g4f.ChatCompletion.create(provider = g4f.Provider.AItianhu,
        model='gpt-3.5-turbo', messages=[{'role': 'user', 'content': prompt_sequency}])

        response = re.findall(r'\d+', chat_completion)
        if response:
            df.at[index,'topic'] = response[0]
        else:
            df.at[index,'topic'] = '0'
    except Exception as e:
        print("An error occurred", str(e))

print(df)

