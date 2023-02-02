import re

file = open('input.txt','r')
x = file.read()
print(len(re.findall(r'[:;]-*(\[+|\(+|\)+|\]+)', x)))
file.close()