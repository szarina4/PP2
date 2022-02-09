line=input()
ch=input()
array=[]
for i in range(len(line)):
    if(line[i]==ch):
        array.append(i)

if len(array)==1:
    print(array[0])
else:
   print(array[0], array[len(array)-1])
#можно было еще .find(),rfind() использовать
