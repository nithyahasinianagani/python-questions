# choose which of the following are not a pre defined keyword in python
# print all the keywords in first line 
# and all the non keywords in the second line

# and,are,is,not,while,where,for,if,try,catch,except
print("and is not while for it try except")
print("are where catch")

import keyword
words = ["and", "are","is", "not", "while","for","if","try","catch","except"]
keywords = [w for w in words if keyword.iskeyword(w)]
non_keywords = [w for w in words if not keyword.iskeyword(w)]
print(keywords)
print(non_keywords)