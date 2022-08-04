usertext=str(input('type the text: '))
text=usertext
text2=[]
lenght=len(text)
i=0
while i<lenght:
    text2 +=[text[i]]
    i=i+1
a=0
text3=[]
while lenght>a:
    a=a+1
    lenght2=lenght-a
    text3 +=[text2[lenght2]]
print(text2)
print(text3)
if text2==text3:
    print('it is')
else:
    print('it is not')
