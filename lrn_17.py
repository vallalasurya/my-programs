scores = [95, 82, 67, 54, 76, 88, 91, 45]
pass_count=0
fail_count=0
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    if score >= 60:
        pass_count += 1
        
    else:
        fail_count += 1
    print(f"Score: {score}, Grade: {grade}")
print("pass:",pass_count)        
print("fail:",fail_count)

  

    