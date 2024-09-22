print("checking the grade...")
marks=int(input("Enter the marks: "))
if marks >= 90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
else:
    print("Grade: D")

print("\nchecking age eligiblity...")
age=int(input("Enter the age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age >= 65:
    print("You are eligible for a pension.")
elif age >= 80:
    print("You are eligible for a retirement fund.")
else:
    print("You are not eligible for any benefits.")

print("\nchecking trafic status...")
light=input("Enter the light color: ")
if(light=="red") or (light=="Red"):
    print("Stop")
elif(light=="yellow") or (light=="Yellow"):
    print("look")
elif(light=="green") or (light=="Green"):
    print("Go")
else:
    print("invalid light color")

#print output for 1. a==5 & g==M,10 2. a==2 & g==F
a=int(input("A: "))
g=input("M/F: ")
if ((a==1 or a==2) and g=="M"):
    print("Fee is 100")
elif (a==3 or a==4 or g=="F"):
    print("Fee is 200")
elif (a==5 and g=="M"):
    print("Fee is 300")
else:
    print("No fee")