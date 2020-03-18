with open('/usr/share/dict/words') as f:
    words = f.read().strip().split('\n')

print(words[:5])

import pandas as pd
word_df = pd.DataFrame({'words': words})

# lowercase all the words
word_df_lower = word_df['words'].str.lower()


# A triangle word is a word whose alphabetical value (i.e. summing the alphabetical values of each letter) is a triangle number. For example:
# 
# SKY is a triangle word because the alphabetical value of SKY is 19 + 11 + 25 = 55, which is a triangle number.
# ANT is not a triangle word because it's alphabetical value is 1 + 14 + 20 = 35, which is not a triangle number.
# Using the list of words on you mac at /usr/share/dict/words, how many triangle words are there?

def alph_value(ch):
    if ch.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        return 0
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) + 1

def alph_value_word(word):
    return sum([alph_value(ch) for ch in word])

assert alph_value_word('sky') == 55
assert alph_value_word('ant') == 35

word_df = pd.DataFrame({'words': word_df_lower,
                       'value_of_word': word_df_lower.apply(lambda word:alph_value_word(word)),
                       })

def triangular(n):
    return int(n*(n+1)/2)

assert triangular(1) == 1
assert triangular(2) == 3
assert triangular(3) == 6
assert triangular(4) == 10

tri_vr = [triangular(n) for n in range(1,31)]
word_df['is_triangle_word'] = word_df.value_of_word.isin(tri_vr)

word_df.is_triangle_word.value_counts()

