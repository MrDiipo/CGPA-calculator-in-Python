"""
Software Engineer: Elegbede Yusuf Oladipupo
Email Address: elegbedeoladipupo@gnail.com
LinkedIn: Oladipupo Elegbede
Github: @MrDiipo
"""

"""
A cgpa (cumulative grade point average) calculator
to calculate the cgpa for students.

Variables names used are very clear enough to describe the
data it stores.
"""
name = input('Welcome dear students. Please enter your name>>> ')
matric = input('Enter your matric number>>> ')
presentLevel = input('Enter your present level>>> ')
presentSemester = input('Enter the present semester>>> ')

file = open(name, 'w')

print("""\nHello dear student! Welcome to a calculator that returns your
grade point average (GPA) and cumulative grade point average (CGPA) for the courses and grades entered.\n
Please follow the instructions carefully. Thank you!""")

print("""\nBelow are the guidelines for grades and their corresponding exam scores:
\nGrade A is for scores greater and equal to 70 (scores > 70 and scores = 70)
Grade B is for scores between 70 and 60 (scores > 59.99 and scores < 69.99)
Grade C is for scores between 60 and 50 (scores > 49.99 and scores < 59.99)
Grade D is for scores between 50 and 45 (scores > 44.99 and scores < 49.99)
Grade E is for scores between 45 and 40 (scores > 39.99 and scores < 44.99)
Grade F is for scores lower than 39.99 (scores < 39.99)
""")

# Global variables are assigned

updatedGrades = []
updatedUnits = []


"""
The remaining things to do are:
The user should be able to enter details such as name, matric number, the year and semester 
for which the GPA is being calculated. 

After everything, the GPA is calculated and CGPA is returned with number of passed units.
"""


def confirmation(x=None):
    x = input('Please enter 0 to Terminate OR 1 to '
              'Continue>>> ')
    while 1:
        if x == '0':
            print('\nThank you for checking out my application!\n')
            break
        elif x != '0' and x != '1':
            x = input('Invalid input. please enter 0 to Terminate OR 1 to '
                      'Continue >>> ')
            continue
        elif x == '1':
            print('Thank you for staying with us.\n')
            gradesAndScores()
            break


def gradesAndScores():
    courseUnits = []
    gradePoints = []
    courses = []
    grades = []

    print('Dear student, ensure you enter your exam details correctly!\nPress 0 to terminate when course entries are '
          'finished.\n')

    while True:

        def coursesInputs():
            while 1:
                if len(courses) == 14:
                    print('Dear student, you\'ve reached the course limit for students which is 13 courses')
                break
            x = input('Enter your course code: ')
            while len(x.replace(' ', '')) != 6:
                print('Invalid Course input.')
                x = input('Please re enter course or press 0 to terminate>>> ')
                if x == '0':
                    confirmation('0')
                break
            courses.append((x.upper().replace(' ', '')))

        def gradesInputs():
            y = int(
                input(
                    'Enter the respective grade (Press 5 for A. 4 for B. 3 for C. 2 for D. 1 for E. 0 for F): ').strip(
                    ' '))
            while 1:
                if y != 1 and y != 2 and y != 3 and y != 4 and y != 5 and y != 0:
                    print('You entered an invalid option.')
                    b = input('Press 1 to start again or 0 to terminate course and grades input>>> ')
                    if b == '1':
                        gradesAndScores()
                    elif b == '0' and b != '1':
                        confirmation(b)
                        break
                break

            gradeInput = lambda g: (grades.append('A') if g == 5
                                    else grades.append('B') if g == 4
            else grades.append('C') if g == 3
            else grades.append('D') if g == 2
            else grades.append('E') if g == 1
            else grades.append('F'))
            gradeInput(y)
            gradePoints.append(y)
            updatedGrades.append(y)

        def courseUnitsInputs():
            z = int(input("Enter the course units: ").strip(' '))
            while z > 6:
                print('Course unit can\'t be greater than 6 units.')
                a = input('Please re enter course or press 0 to terminate>>> ')
                if a == '0':
                    confirmation('0')
            courseUnits.append(z)
            updatedUnits.append(z)

        print(' ')
        coursesInputs()
        gradesInputs()
        courseUnitsInputs()

        proceedToCgpa = input('Press 0 to view Courses entered and view GPA and CGPA or 1 to continue course input>>> ')
        while 1:
            if proceedToCgpa == '1':
                break
            if proceedToCgpa == '0':
                resultDisplay(courses, grades, courseUnits, gradePoints)
                break
            elif proceedToCgpa != '1' or proceedToCgpa != '0':
                proceedToCgpa = input('Invalid input! Press 0 to view Courses entered and view GPA and CGPA or 1 to '
                                      'continue course input>>> ')
                continue


def resultDisplay(x, y, z, d):

    print('Dear student, below are the courses, grades and course units you\'ve entered.\nPlease preview to ensure '
          'you entered the correct information.\n')
    print('Courses', 'Grades', 'Units', sep='   ')

    courseHistory = zip(x, y, z)
    [print(x, y, z, sep='      ') for x, y, z in courseHistory]
    print(' ')

    while 1:
        a = input('Is the information correct? If YES, press 1 to view GPA and CGPA or press 0 to start again>>> \n')
        if a == '1':
            print('Dear user, your GPA for the present semester is %.2f.' % gpaAlgo(z, d))
            print('Dear user, your CGPA for the present semester is %.2f.\n' % cgpaAlgo())
            break
        if a == '0':
            gradesAndScores()
            break
        if a != '0' and a != 1:
            print('Invalid input!')

    while 1:
        a = input('Press 1 to enter details of ANOTHER SEMESTER or 0 to log out>>>')
        if a == '1':
            gradesAndScores()
        else:
            confirmation()


def gpaAlgo(x, y):
    a = sum(x)
    b = list(zip(x, y))

    tempList = []  # A temporary list

    for i, j in b:
        tempList.append(i * j)

    tempSum = sum(tempList)  # A local variable to store a temporary value
    return tempSum / a


def cgpaAlgo():
    return gpaAlgo(updatedUnits, updatedGrades)


if "__main__" == __name__:
    confirmation()
