import hashlib
  
# encoding using md5 hash function 
result = hashlib.md5(b'Mohamed Herak')
  
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
