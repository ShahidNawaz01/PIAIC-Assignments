student_data = dict()
selected_courses = list()

available_courses = ['AIC', 'BCC', 'CNC', 'IoT', 'Web3.0 and Metaverse Developer']
input_parameters = ['name', 'email', 'age']

for i in range(len(input_parameters)):
    parameter = input(f'Enter your {input_parameters[i]}: ')
    student_data[input_parameters[i]] = student_data.get(input_parameters[i], parameter)

while True:
    courses = int(input('Choose courses you want to enroll in (1 for AIC, 2 for BCC,\
3 for CNC, 4 for IoT, 5 for Web3.0 and Metaverse Developer): '))
    if available_courses[courses-1] not in selected_courses:
        selected_courses.append(available_courses[courses-1])

    x = input('Do you want to select any other course? (Y/N) ')
    if x.lower() != 'y':
        break

student_data['courses'] = selected_courses
print(student_data)