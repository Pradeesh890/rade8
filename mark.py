def calculate_grade(marks):
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    elif marks < 60:
        return 'F'
    else:
        return 'Invalid marks'

def main():
    try:
        marks = float(input("Enter the student's marks: "))
        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            print(f"The grade for {marks} marks is: {grade}")
        else:
            print("Marks should be between 0 and 100.")
    except ValueError:
        print("Please enter a valid numeric value for marks.")

if __name__ == "__main__":
    main()
