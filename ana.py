str1=input("\nenter your 1st string:")
str2=input("\nenter your 2nd string:")
c1=0
len1=len(str1)
len2=len(str2)
for i in str1:
  if i in str2:
    c1=c1+1

c2=0
for i in str2:
  if i in str1:
    c2=c2+1
    
if(c1==len1)and(c2==len2):
 print("\n\nYES.THIS IS ANAGRAM")
else:
  print("NO.THIS IS NOT ANAGRAM")
  
