file = open('HRReconds.csv','r')
t=m=f=0
for emp in file:
    t+=1
    if emp.split(','[11]) =='Male':
        m+=1
    else:
        f+=1

print('Total Employee: ', t)
print('Male Employee: ', m)
print('Female Employee: ', f)