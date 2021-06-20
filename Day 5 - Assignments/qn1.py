# to find out the BMI based on Weight(in kg) and height (in meters)
def toFindBMI(weight,height) :
    return round(weight/ (height * height), 1)

age = int(input("Hi Argo, What is your Age?"))
weight = float(input("What is your Weight in Kg?"))
height = float(input("What is your Height in metres?"))
print("The BMI is ",toFindBMI(weight,height))