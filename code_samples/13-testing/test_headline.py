from headline_module import Headline


def test_headline_length_is_correct():
  text = "This is a headline"
  expected_length = 4
  headline = Headline(text, "BBC")

  assert headline.get_word_count() == 4

def test_character_count():
  text = "1234567"
  expected_length = 7
  headline = Headline(text, "Sky")
  assert headline.get_character_count() == expected_length

def test_shout_headline():
  text = "this is not shouted loudly"
  expected = "THIS IS NOT SHOUTED LOUDLY"
  headline = Headline(text, "Sky")
  assert headline.upper() == expected