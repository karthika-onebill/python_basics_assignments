from sys import argv
def toFindBMI(weight,height) :
    bmi = round(weight/ (height * height), 1)
    if(bmi<18.5) : return "Your BMI is ",bmi,"which means you are low healthy"
    elif(18.5<=bmi and bmi<=24.9) : return "Your BMI is ",bmi,"which means you are healthy"
    else : return "Your BMI is ",bmi,"which means you are obese."
name = argv[1]                  #getting name
height = float(argv[2])         #getting height
weight = float(argv[3])         #getting weight
print("Name : ",name)
print("Height : ",height)
print("Weight : ",weight)
print(toFindBMI(weight,height))
