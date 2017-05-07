
#write a student grade dictionary in Python


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]

def average(numbers):
    total = sum(numbers)
    result = float(total) / len(numbers)
    return result


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + \
    0.3 * quizzes + 0.6 * tests
  
print "lloyd's average: ", get_average(lloyd)
print "alice's average: ", get_average(alice)
print "tyler's average: ", get_average(tyler)

def get_letter_grade(score):
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
print "lloyd's grade: ", get_letter_grade(get_average(lloyd))
print "alice's grade: ", get_letter_grade(get_average(alice))
print "tyler's grade: ", get_letter_grade(get_average(tyler))

def get_class_average(students):
    results=[]
    for kid in students:
        results.append(round(float(get_average(kid)), 2))
    return average(results)    

print students   
print get_class_average(students)
print get_letter_grade(get_class_average(students))

