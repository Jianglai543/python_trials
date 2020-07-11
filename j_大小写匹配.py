import re


str = 'UPPER PYTHON, lower python, Xixed Python'
texts = re.findall('python', str, flags=re.IGNORECASE)
print(texts)

text2 = re.sub('python', 'snake', str, flags=re.IGNORECASE)
print(text2)  # 格式不能匹配

def marchcases(content):
    def replace(m):# <re.Match object; span=(6, 12), match='PYTHON'>
        text = m.group() # 'PYTHON' ...
        if text.isupper():
            return content.upper()
        elif text.islower():
            return content.lower()
        elif text[0].isupper():
            return content.capitalize()
        else:
            return content
    return replace

text3 = re.sub('python', marchcases('snake'), str, flags=re.IGNORECASE)
print(text3)
