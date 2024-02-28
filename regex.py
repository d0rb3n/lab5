#ex1
import re
txt = input()
x = re.fullmatch('ab*', txt)
if x:
    print("Match!")
else:
    print("No match!")

#ex2 
import re
txt = input()
x = re.fullmatch('ab{2,3}', txt)
if x:
    print("Match!")
else:
    print("No match!")

#ex3
import re
txt = input()
p = re.compile('[a-z]+_')
z = p.findall(txt)
print(z)

#ex4
import re
txt =input()
p = re.compile('[A-Z][a-z]+')
z = p.findall(txt)
print(z)

#ex5
import re
txt = input()
x = re.fullmatch('^a.+b$', txt)
if x:
    print("Match!")
else:
    print("No match!")

#ex6
import re
txt = input()
p = re.compile('.+')
x = re.sub('[ ,.]', ':', txt)
print(x)

#ex7 
import re
txt = input()
def snake_to_camel(s):
        return ''.join(x.capitalize() or '_' for x in s.split('_'))
print(snake_to_camel(txt))

#ex8
import re
def split(s):
    return re.findall('[A-Z][^A-Z]*', s)
intxt = input()
res = split(intxt)
print(res)
 
#ex9
import re
def func(txt):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
intxt = input()
outtxt = func(intxt)
print(outtxt)

#ex10
import re
def camel_to_snake(camel):
    snakecase = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel).lower()
    return snakecase
camelstr = input()
snakestr = camel_to_snake(camelstr)
print(snakestr)