class Headline:  # are we just making stuff up!  - blueprint, recipe, abstract
  # pass  # placeholder ... 
  def __init__(self, title, source, url="Unknown"):
    print(f"Init has been called with {title} and {source}")
    self.title = title
    self.source = source
    self.url = url

  def __str__(self):
    return f"'{self.title}' from {self.source}" # human readable understanding of our class

  def __repr__(self):
    return f"Headline('{self.title}', '{self.source}')"

  def word_count(self):
    return len(self.title.split()) 

  