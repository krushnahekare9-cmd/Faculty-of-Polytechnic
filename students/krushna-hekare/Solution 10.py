#problem 1
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F" 
print(classify_grade(95))
print(classify_grade(82))  
print(classify_grade(74))  
print(classify_grade(61))  
print(classify_grade(45))
