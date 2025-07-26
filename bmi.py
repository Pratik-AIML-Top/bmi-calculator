# bmi.py

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    
    print(f"Your BMI is {bmi:.2f}. You are classified as: {category}")


