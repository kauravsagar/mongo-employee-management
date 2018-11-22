from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()
db = client.employees_records

def add(**kargs):
    employee = db.employees.insert_one(kargs)
    if employee.inserted_id:
        print('added successfully. Employee id is: {}'. format(employee.inserted_id))
    else:
        print('unable to add user.')

def delete(employee_id):
    deleted_employee = db.employees.delete_one({'_id': ObjectId(employee_id)})
    if deleted_employee.deleted_count == 1:
        print('employee deleted successfully')
    else:
        print('unable to delee user')

def update(employee_id, **kargs):
    updated_employee = db.employees.update_one({'_id': ObjectId(employee_id)}, {'$set':kargs})
    if updated_employee.modified_count == 1:
        print('updated successfully')
    else:
        print('unable to update.')

def show(employee_id):
    employee = db.employees.find_one({'_id': ObjectId(employee_id)})
    if employee is None:
        print('Employee not found.')
    else:
        print('First name: {}'.format(employee['first_name']))
        print('Last name: {}'.format(employee['last_name']))
        print('Email: {}'.format(employee['email']))
        print('Age: {}'.format(employee['age']))
    
while True:
    print('1> Add employyee')
    print('2> Show employee')
    print('3> Update employee')
    print('4> Delete employee')
    print('5> Exit')
    print('Choose any options: ', end='')
    user_input = int(input())
    if user_input == 1:
        print('Enter first name: ', end='')
        first_name  = input()
        print('Enter last name: ', end='')
        last_name = input()
        print('Enter email address: ', end='')
        email = input()
        print('Enter age: ', end='')
        age = int(input())
        add(first_name=first_name, last_name=last_name, email=email, age=age)
    elif user_input == 2:
        print('Enter employee id: ', end='')
        employee_id = input()
        show(employee_id)
    elif user_input == 3:
        print('Eneter employee id: ', end='')
        employee_id = input() 
        print('Enter first name: ', end='')
        first_name  = input()
        print('Enter last name: ', end='')
        last_name = input()
        print('Enter email address: ', end='')
        email = input()
        print('Enter age: ', end='')
        age = int(input())
        update(employee_id, first_name=first_name, last_name=last_name, email=email, age=age)
    elif user_input == 4:
        print('Enter employee id: ', end='')
        employee_id  = input()
        delete(employee_id)
    elif user_input == 5:
        break
    else:
        print('Wrong option please try again.')
client.close()
print('Thank you!!!')
