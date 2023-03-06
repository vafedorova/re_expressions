import re

file = open('input.txt','r')
file2 = open('output.txt','w')
x = file.read()
x = re.sub(r'(([A-Z][a-zA-Z]* +){2,}[A-Z][A-Za-z]*)', r'"\1"', x)
file2.write(x)
file.close()
file2.close()