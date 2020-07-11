from datetime import datetime


text = '2020-6-1'
y = datetime.strptime(text, '%Y-%m-%d')
print(y)