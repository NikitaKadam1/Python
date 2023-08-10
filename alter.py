str1=input("\nEnter your 1st string: ")
str2=input("\nEnter your 2nd string: ")
new=('')
len1=len(str1)
len2=len(str2)
ful_len=len1+len2
for i in range(ful_len):
  if i<len1:
    new=new+str1[i]
  if i<len2:
    new=new+str2[i]
print(new)
