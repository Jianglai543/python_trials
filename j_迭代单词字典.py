from collections import defaultdict


summary_words = defaultdict(list)
with open('j_yield.txt') as f:
    words = f.readlines()

for idx, line in enumerate(words):
    words = [w.strip().lower() for w in line.split()]
    for w in words:
        summary_words[w].append(idx)
print(summary_words)
