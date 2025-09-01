i = 1
c = 3
b=[]
while i <= c:
 try:
  a=int(input("Enter:")) 
  b.append(a)
  i+=1 
 except:
  print("Error")
print(b)
