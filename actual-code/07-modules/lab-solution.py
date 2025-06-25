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

  

headline1 = Headline("World peace created", "Some fantasy")  # building, meal, object, instance
headline2 = Headline("Trump strikes again", "BBC")
# title, source (url, date, byline, ....)

print(headline1.title)
print(headline1.source)

print(headline1)
print(headline2)

print([headline1, headline2])  # __repr__ - machine readable 


# str -> repr -> ugly fallback

print(len(headline1.title.split()))
print(headline1.word_count())
print(headline2.word_count())

headlines = [
    Headline("General election: Labour and Tories clash over tax", "BBC News"),
    Headline("England crowned T20 world champions", "Sky Sports"),
    Headline("Summer travel chaos feared as airline strikes loom", "The Guardian"),
    Headline("UK inflation rate falls to lowest level in three years", "Reuters"),
    Headline("New David Hockney exhibition opens in London", "BBC News"),
    Headline("Science discovers new way to tackle plastic waste", "Nature"),
    Headline("Government announces new funding for NHS", "BBC News"),
    Headline("Stock market hits record high on tech boom", "Financial Times"),
    Headline("Debate rages over future of Artificial Intelligence", "The Economist"),
    Headline("Classic Doctor Who episodes to be released in colour", "BBC News")
]

for headline in headlines:                                      # get_word_count(headline.title)
  print(f"From {headline.source}: {headline.title} (word count: {headline.word_count()})")