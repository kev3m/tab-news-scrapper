
# 💻 TabNews Scraper

The TabNews Scraper is a Python web scraping tool designed to extract posts from the website "tabnews" - a platform that hosts a wide range of tech content. This scraper utilizes the GPT4Free repository for making requests to the website and categorizes each article into one of the five predefined categories. Additionally, it assigns a relevance score to each article based on the number of "tabcoins" and comments it has received.

## 📚 Categories
The posts scraped from the "tabnews" website are categorized into the following five categories:

1. Development and Programming
2. Hosting and Infrastructure
3. Web and Design
4. Learning and Experiences
5. Open Source and Community
6. Games and Entertainment

## 📈 Relevance Score Calculation

The relevance score for each post is calculated using the following formula:

```python
  relevance = round((tabcoins * tabcoin_weight) + (comments *   comment_weight), 3)
```
- Tabcoins is the number of "tabcoins" the article has received.
- Comments is the number of comments the article has received.
- tabcoin_weight is the weight assigned to the number of tabcoins   (default value: 0.65).
- comment_weight is the weight assigned to the number of comments (default value: 0.35).

The relevance score indicates the overall popularity and engagement level of each content.

