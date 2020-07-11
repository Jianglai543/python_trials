import html
from html.parser import HTMLParser
from  xml.sax.saxutils import unescape


s = 'elements<tag>text<tag>'
v_escape = html.escape(s, quote=True)  # 将符号转换为对应文本
print(v_escape)
s = 'spicy jalapeño'
v_encode = s.encode('ascii', errors='xmlcharrefreplace')   # 将非ascll 实体嵌入文本
print(v_encode)

s2 = 'spicy &quotjalape&#241;o&quot;'
un_s2 = html.unescape(s2)# 文本转换为对应符号
print(un_s2)

t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))