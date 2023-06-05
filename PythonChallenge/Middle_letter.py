#Write a function named mid that takes a string as its parameter. 
#Your function should extract and return the middle letter. 
#If there is no middle letter, your function should return the empty string.
#For example, mid("abc") should return "b" and mid("aaaa") should return ".

def mid (argument):
   mid = int(len(argument))
   if mid % 2 == 0 :
      return  
   else:
       mid = mid // 2 + 1
       return argument[mid - 1] 


print(mid("abc"))
print(mid("aaaa"))