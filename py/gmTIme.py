import time

NOW=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
print(NOW)
if(4<=h<12):
    print('Good Morning')
elif(12<=h<17):
    print('Good Afternoon')
else:
    print('Good Night')
 