str1=input("enter your string:")
ch=input("enter your charcter you want count:")
flag=0
# for i in str1:
#   if i!=ch:
#     newstr=new+i
#     print(newstr)
for i in str1:
  if i==ch:
    flag=flag+1
print(flag)  
