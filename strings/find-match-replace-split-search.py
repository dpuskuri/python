import re

text = "Deepak is learning python , java"
pattern = r"java"

search = re.search(pattern, text)

if search:
    print("Pattern Found", search.group())
else:
    print("pattern not found")

#match
pattern = r"java"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
print(match)

#replace

replace = "python"
new_replae = re.sub(pattern,replace,text)
print("Replaced text:", new_replae)

#split

pattern = r","

split = re.split(pattern,text)
print("splitted text:",split)
