from collections import Counter


word_list = ['a','b','c','d','a','c']
word_counts = Counter(word_list)  # 算出计数
common_2 = word_counts.most_common(2)  # 找最大项
morewords = ['d','a','c']

for i in morewords:
    word_counts[i] += 1
# word_counts.update(morewords)

b = Counter(morewords)
new_word_counts = word_counts + b # +- 支持
print(new_word_counts)
