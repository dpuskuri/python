text = "deepak learning python"
str = " deepak learning java"
new_str = str.replace("java", "python")
new_text = text.replace("python","Java") 
result = text + str 
uppercase = str.upper()
uppercase = text.upper()
lowercase = str.lower()
Lowercase = text.lower()
#print(new_text, new_str)
print(result, len(result),"Uppercase:",uppercase)
uppercase = result.upper()
lowercase = result.lower()
print("lowercase:", lowercase)
print("Uppercase:", uppercase)
new_result = result.replace("java", ".net")
print(new_result)
