"""构建转换表"""
s = 'python\fis\tawesome\r'
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None

}
print(s.translate(remap))


import unicodedata
import sys

"""删除所有Unicode组合字符"""
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
s.translate(cmb_chrs)


""""""
digit_map = {c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == "Nd" }
print(len(digit_map))
nums = '\u0661\u0662\u0663'
num = nums.translate(digit_map)
print(num)