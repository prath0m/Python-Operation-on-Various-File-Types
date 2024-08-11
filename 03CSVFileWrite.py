# CSV Comma Separated value
no = int(input('Enter Emp Number: '))
nm = input('Enter Name: ')
gn = input('Enter Gender: ')
dp = input('Enter Dept: ')
po = input('Enter post: ')
sl = float(input('Enter Salary: '))

file = open("Emp.csv","a")
file.write(str(no) + "," + nm + "," + gn + "," + dp + "," + po + "," + str(sl)+"\n")
file.close()