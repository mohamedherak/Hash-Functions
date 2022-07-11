import hashlib
  
str = "Mohamed Herak"
  
# encoding str using encode()then sending to SHA256()
result = hashlib.sha256(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
