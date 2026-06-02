import pandas as pd 
text = "Hello World"

vowels = sum(pd.Series(list(text.lower())).isin(list("aeiou")))

print("Vowel Count:", vowels)


