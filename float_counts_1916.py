# 		Вещественное число задается следующим образом (форма Бэкуса-Наура): 
# "Number" ::= ["Sign"] "digit" {"digit"}["Separator" "digit" {"digit"}]["Exponent" ["Sign"] "digit" {"digit"}] 
# "digit" ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' 
# "Sign" ::= '+' | '-' 
# "Separator" ::= '.' 
# "Exponent" ::= 'E' | 'e' 

import re

s = input()
match_res = re.fullmatch(r'[+-]?[\d]+(.[\d]+)?([eE][+-]?[\d]+)?', s)
if match_res:
    #print(match_res)
    print("YES")
else:
    print("NO")