
grade = input('Enter grade: ')

try :
    grade = int(grade)
    print(grade)

    if grade > 100:
        print("Please enter valid grade.")
    elif grade >= 90:
        if grade <= 100:
            print('Grade: A')
    elif grade >= 80:
        if grade <= 89:
            print('Grade: B')
    elif grade >= 70:
        if grade <= 79:
            print('Grade: C')
    elif grade <= 69:
        print('Grade: Needs Improvement')
except :
    print('Score: -1')
    print("Error: Please enter a valid numerical score.")
    exit()

