# Data Storage, Employees

employees = {}

# Adding Employees to the data

employees[101] = {
    'name' : 'Satya',
    'age' : 27,
    'department': 'HR',
    'salary': 50000
}
print(employees)

# Menu Functionalities

def add_employee():
    while True:
        id_inp = int(input('Enter Employee ID of new employee!'))
        if id_inp in employees:
            print('Employee already Exists!')
            
        else:
            name_inp = input('Enter Employee Name')
            age_inp = int(input('Enter Employee Age'))
            dept_inp = input('Enter Employee Department')
            salary_inp = int(input('Enter Employee Salary'))
            employees[id_inp] = {
                'name' : name_inp, 
                'age' : age_inp, 
                'department' : dept_inp, 
                'salary' : salary_inp
            }
            print('Employee added successfully!')
            break

def view_all_employees():
    if len(employees) == 0:
        print('No Employees available')
    for emp_id in employees:
        print('ID', emp_id)
        print('Name', employees[emp_id]['name'])
        print('Age', employees[emp_id]['age'])
        print('Depratment', employees[emp_id]['department'])
        print('Salary', employees[emp_id]['salary'])
        print()

def search_employee(emp_id):
    if emp_id in employees:
        print('ID', emp_id)
        print('Name', employees[emp_id]['name'])
        print('Age', employees[emp_id]['age'])
        print('Depratment', employees[emp_id]['department'])
        print('Salary', employees[emp_id]['salary'])
    else: 
        print('Employee not found')
        
        

def main_menu():
    while True:
        print()
        print('========================================================')
        print('1. Add')
        print('2. View')
        print('3. Search')
        print('4. Exit')
        print('========================================================')
        print()
        user_inp = input('Choose from Employee Management System to know details: ')
        if user_inp.lower() == 'exit' or user_inp == '4': 
            break
        elif user_inp.lower() == 'search' or user_inp == '3':
            search_inp = int(input('Enter Employee ID for the employee you want to search!'))
            search_employee(int(search_inp))
        elif user_inp.lower() == 'view' or user_inp == '2':
            view_all_employees()
        elif user_inp.lower() == 'add' or user_inp == '1':
            add_employee()
        else:
            print('Invalid Input')


main_menu()
        
