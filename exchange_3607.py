import re

file_in = open('input.txt','r')
x = file_in.read()
file_in.close()
x = re.sub(r'\\circle\{\(((\d)+)\,((\d)+)\)', r'\\circle{(\3,\1)', x)
file_out = open('output.txt','w')
file_out.write(x)
file_out.close()