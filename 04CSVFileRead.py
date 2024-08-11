file = open('Emp.csv','r')
for rec in file:
    print(rec)
    # # print(rec.split(","))
    # print(rec.split(",")[1])
    
file.close()