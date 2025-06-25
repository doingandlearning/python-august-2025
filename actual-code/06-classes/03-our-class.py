class NewsArticle:
  # special ... double underscore ... dunder
  def __init__(self, title, summary, tags=None, authors=None):
    self.title = title
    self.summary = summary
    self.tags = tags if tags else []
    self.authors = authors if authors else []

  def __str__(self):
    return f"{self.title} by {self.authors} {self.tags}"

  def word_count(self):
    return len(self.summary.split())

  def preview(self):
    return self.summary[:50] + "..."
  

article_1 = NewsArticle(
  title="AI Policy Update", 
  summary="The government has introduced new regulations for AI systems across healthcare and finance.",
  tags=["AI", "Policy"],
  authors=["Alex Green"]
)

print(isinstance(article_1, NewsArticle))
print(article_1)
print(article_1.word_count())
print(article_1.preview())

article_1.

# alt_article_1 = {
#   "title": "AI Policy Update",
#   "summary": "The government has introduced new regulations for AI systems across healthcare and finance.",
#   "tags":["AI", "Policy"],
#   "authors": ["Alex Green"]
# }

# print(article_1)
# print(type(article_1))

# print(article_1.title)
# print(article_1.summary)
# print(article_1.tags)
# print(article_1.authors)


# title_1 = "AI Policy Update"
# summary_1 = "The government has introduced new regulations for AI systems across healthcare and finance."
# tags_1 = ["AI", "Policy"]
# author_1 = "Alex Green"

# method is a function inside of a class