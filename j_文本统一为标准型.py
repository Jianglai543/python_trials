import re
import unicodedata

s1 = 'spicy jalape\u00f1o'
s2 = 'spicy jalape\u0303o'
print(s1 == s2)
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s1)
print(t1 == t2)
print(''.join(c for c in t1 if not unicodedata.combining(c)))