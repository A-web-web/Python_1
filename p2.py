i = 1
c = 3
a=0
b=[]
while i <= c:
 try:
  a=int(input("Enter:")) 
  b.append(a)
  i+=1 
  a=1
 except:
  print("Error") 
  break
if(a==1):
 print(b)


