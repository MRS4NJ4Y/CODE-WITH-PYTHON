#<var>=<val1>if <condition>else<val2>
food=input("food: ")
eat="yes" if food=="cake" else "no"
print(eat)

#<stt1>if<condition>else<stt2>
food=input("food: ")
print("Sweet") if food=="cake" or food=="jelebi" else "no"

#<var>=(false_var, true_var)[<condition]
age=int(input("age: "))
vote=("no","yes") [age>=18]
print(vote)

sal=float(input("salary: "))
tax=sal*(0.1, 0.2)[sal>=300000]
print(tax)