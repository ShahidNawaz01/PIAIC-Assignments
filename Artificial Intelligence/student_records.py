available_courses = {
    1: 'Artificial Intelligence',
    2: 'Blockchain',
    3: 'Cloud Computing',
    4: 'Internet of Things',
    5: 'Web3.0 and Metaverse Developer'
}

students = list()


class StudentData:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.courses = []


def display_data(students_list):
    for data in students_list:
        print("Student's name: ", data.name)
        print("Student's age: ", data.age)
        print("Student's email: ", data.email)
        print("Courses Enrolled in: ", data.courses)


def add_courses(student_object):
    print('Available courses are: ')
    for course in available_courses:
        print(f"{course}. {available_courses[course]}")
    selected_courses = list()
    while True:
        option = int(input('Enter your course option (1-5): '))
        if available_courses[option] not in selected_courses:
            selected_courses.append(available_courses[option])
        x = input('Do you want to select any other course? (Y/N) ')
        if x.lower() != 'y':
            break
    student_object.courses = selected_courses
    students.append(student_object)
    return students


def add_data():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    email = input("Enter student's email: ")
    student_object = StudentData(name, age, email)
    add_courses(student_object)


def data_entry(user_input):
    count = False
    while count is False:
        if user_input == 1:
            add_data()
            count = True
        elif user_input == 2:
            display_data(students)
            count = True
        elif user_input == 3:
            print('Quiting the program.')
            break
        else:
            print('Incorrect selection.')
            user_input = int(input('Enter input again: '))
            count = False


def available_options():
    print('Available Options.')
    print("1. Add new data")
    print("2. Display existing data")
    print("3. Quit program\n")
    user_input = int(input('Enter your input: '))
    return user_input


def main():
    user_input = 0
    while user_input != 3:
        user_input = available_options()
        data_entry(user_input)


if __name__ == '__main__':
    main()
