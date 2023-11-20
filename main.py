from sys import exit
from os import startfile
from time import strftime

print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
print('{: ^9}|{: ^56}|{: ^9}'.format("", "PAPER CONSOLE", ""))
print('{: ^9}|{: ^56}|{: ^9}'.format("", "VERSION - 1.0", ""))
print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

date = strftime('%d %b %Y')
report_file = open(date + '.txt', 'w')

students_present = list()
students_absent = list()
class_list = list()

def create_class():
    global class_list
    
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "CREATE CLASS", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    class_strength = -1
    while class_strength <= 0:
        print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
        class_strength = int(input('{: ^9}|{}'.format("","ENTER CLASS STRENGTH: ")))

        if class_strength <= 0:
            print('{: ^9}|{}'.format("",f"ERROR: Invalid input!"))

    while len(class_list) < class_strength:
        print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
        student_name = input('{: ^9}|{}'.format("","ENTER STUDENT NAME: ")).strip()

        if student_name == "":
            print('{: ^9}|{}'.format("","ERROR: Invalid input!"))
            
        elif student_name not in class_list:
            class_list.append(student_name)
            print('{: ^9}|{}'.format("",f"SUCCESS: {student_name} added to class."))
            
        else:
            print('{: ^9}|{}'.format("","ERROR: Student exists!"))

    write_class_data()
    mark_attendance()


try:
    data_file = open("My Class.txt", "r+")
    test_string = data_file.readline()
    
except FileNotFoundError:
    data_file = open("My Class.txt", "w+")
    data_file.write("[UNAVAILABLE]\n")
    data_file.flush()
    
    data_file.seek(0)
    test_string = data_file.readline()


def prepare_class_list():
    global class_list
    
    data_file.seek(0)
    data_file.readline()

    class_data = data_file.readlines()
    for i in range(len(class_data)):
        class_data[i] = class_data[i].replace('\n', '')
        
    for i in class_data:
        data = i.split('.')        
        if data[1] not in class_list:
            class_list.append(data[1])

        
def write_class_data():
    global class_list
    
    class_list.sort()
    data_file = open("My Class.txt", "w+")
    
    data_file.seek(0)
    if class_list != []:
        data_file.write("[AVAILABLE]\n")
    else:
        data_file.write("[UNAVAILABLE]\n")
    
    for i in range(len(class_list)):
        data_file.write(f"{i+1}.{class_list[i]}\n")

    data_file.flush()


def display_about():
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "PAPER CONSOLE", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "VERSION - 1.0", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "AUTHOR: SAURABH KUMAR", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))


def edit_class():
    global class_list
    
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "EDIT CLASS", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","1. ADD STUDENT", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","2. REMOVE STUDENT", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","3. RENAME STUDENT", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","4. SHOW CLASS", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","0. SAVE CHANGES", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    while True:
        correct_choice = None
        while correct_choice not in [1, 2, 3, 4, 0]:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            choice = int(input('{: ^9}|{}'.format("","ENTER CHOICE[0: SAVE CHANGES]: ")))
            
            if choice in [1, 2, 3, 4, 0]:
                correct_choice = choice
            else:
                print("{: ^9}|{}".format("", "ERROR: Invalid input!"))

        if choice == 1:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{: ^56}|{: ^9}'.format("", "ADD STUDENT", ""))
            print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            student_name = input("{: ^9}|{}".format("", "ENTER NAME: ")).strip()

            if student_name.isalnum() == False:
                print('{: ^9}|{}'.format("","ERROR: Invalid input!"))
                
            elif student_name not in class_list:
                class_list.append(student_name)
                print('{: ^9}|{}'.format("",f"SUCCESS: {student_name} added to class."))
                
            else:
                print('{: ^9}|{}'.format("","ERROR: Student exists!"))     

        elif choice == 2:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{: ^56}|{: ^9}'.format("", "REMOVE STUDENT", ""))
            print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            student_roll = int(input("{: ^9}|{}".format("", "ENTER ROLL NUMBER: ")))
            
            if 1 <= student_roll <= len(class_list):
                print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                print('{: ^9}|{}'.format("",class_list[student_roll - 1]))

                verify = input('{: ^9}|{}'.format("","REMOVE STUDENT?[y: YES/ n: NO]: ")).strip()
                
                if verify in ["y", "Y"]:
                    class_list.pop(student_roll - 1)
                    print('{: ^9}|{}'.format("",f"SUCCESS: Roll number {student_roll} removed from class."))
                    
            else:
                print('{: ^9}|{}'.format("","ERROR: Roll number does not exist!"))
                    
        elif choice == 3:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{: ^56}|{: ^9}'.format("", "RENAME STUDENT", ""))
            print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            student_roll = int(input("{: ^9}|{}".format("", "ENTER ROLL NUMBER: ")))
            
            if 0 < student_roll <= len(class_list):
                print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                print('{: ^9}|{}'.format("",class_list[student_roll - 1]))

                new_name = input('{: ^9}|{}'.format("","NEW NAME: ")).strip()
                
                if new_name not in class_list:
                    class_list[student_roll - 1] = new_name
                    print('{: ^9}|{}'.format("","SUCCESS: Student renamed."))
            else:
                print('{: ^9}|{}'.format("",f"ERROR: Roll number not found!"))

        elif choice == 4:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{: ^56}|{: ^9}'.format("", "STUDENTS", ""))
            print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            for student in class_list:
                print('{: ^9}|{: <56}|{: ^9}'.format("",f"{class_list.index(student) + 1}. {student}", ""))
                print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                    
        elif choice == 0:
            write_class_data()

            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{: ^56}|{: ^9}'.format("", "CHANGES SAVED.", ""))
            print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            
            break

        
def save_data():    
    global report_file
    global students_present
    global students_absent
    
    report_file.write('Date:' + date + '\n')
    report_file.write('\nTOTAL STUDENTS: ' + str(len(class_list)) + '\n')
    report_file.write('PRESENT: ' + str(len(students_present)) + '\n')
    report_file.write('ABSENT: ' + str(len(students_absent)) + '\n')
    
    report_file.write('\nPRESENT:\n')
    
    if students_present != []:
            for roll in students_present:
                    report_file.write(str(students_present.index(roll) + 1)
                                 + '.' + class_list[roll - 1] + '\n')
                    
    else:
           report_file.write('None\n') 
        
    report_file.write('\nABSENT:\n')
    
    if students_absent != []:
            for roll in students_absent:
                    report_file.write(str(students_absent.index(roll) + 1)
                                 + '.' + class_list[roll - 1] + '\n')
                    
    else:
          report_file.write('None\n')  

    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "ATTENDANCE SAVED.", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    report_file.close()
    startfile(date + '.txt')


def edit_data():    
    global students_present
    global students_absent

    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "EDIT ATTENDANCE", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    verify = 1
    while verify == 1:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            roll = int(input("{: ^9}|{}".format("", "ENTER ROLL NUMBER: ")))
            
            if roll in range(1, len(class_list) + 1):
                    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                    print('{: ^9}|{}'.format("",class_list[roll - 1]))
                    
                    correct_input = 0
                    while correct_input != 1:
                            state = input("{: ^9}|{}".format("", "STATE[p/a]: ")).strip()
                            
                            if state in ['a', 'A', 'p', 'P']:
                                    correct_input = 1
                                    
                            else:
                                    print("{: ^9}|{}".format("", "ERROR: Invalid input!"))
                                    print('\n' + class_list[roll - 1])
                                    
                    if state in ['p', 'P']:
                            if roll not in students_present:
                                    students_present.append(roll)
                                    students_absent.remove(roll)                                                                            
                                            
                    elif state in ['a', 'A']:
                            if roll not in students_absent:
                                    students_absent.append(roll)
                                    students_present.remove(roll)                                            
                                    
            else:
                    print("{: ^9}|{}".format("", "ERROR: Roll number does not exist!"))

            correct_input = 0
            while correct_input != 1:
                    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                    verify = int(input("{: ^9}|{}".format("", "EDIT FURTHER?[0:SAVE/ 1:EDIT]: ")))
                    
                    if verify in [0, 1]:
                            correct_input = 1
                            if verify == 0:
                                    print('\n{: ^9}{:-^58}{: ^9}'.format("", "", ""))
                                    save_data()
                                    
                    else:
                            print("{: ^9}|{}".format("", "ERROR: Invalid input!"))   


def mark_attendance():
    global students_present
    global students_absent

    prepare_class_list()
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "ATTENDANCE", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    
    for roll in range(1, len(class_list) + 1):
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            print('{: ^9}|{}.{}'.format("", roll, class_list[roll - 1]))
            
            correct_input = 0
            while correct_input != 1:
                    state = input("{: ^9}|{}".format("", "STATE[p/a]: ")).strip()
                    
                    if state in ['a', 'A', 'p', 'P']:
                            correct_input = 1
                            
                    else:
                            print("{: ^9}|{}".format("", "INCORRECT STATE! TRY AGAIN."))
                            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
                            print('{: ^9}|{}'.format("",class_list[roll - 1]))
                            
            if state in ['p', 'P']:
                    students_present.append(roll)
                    
            elif state in ['a', 'A']:
                    students_absent.append(roll)

    print('\n{: ^9}{:-^58}{: ^9}'.format("", "", ""))

    correct_input = 0
    while correct_input != 1:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            verify = input("{: ^9}|{}".format("", "SAVE DATA?[y: SAVE/ n: EDIT]: ")).strip()
            
            if verify in ['y', 'Y', 'n', 'N']:
                    correct_input = 1
                    
            else:
                    print("{: ^9}|{}".format("", "ERROR: Invalid input!"))
    
    if verify in ['y', 'Y']:
        save_data()
        
    elif verify in ['n', 'N']:
        edit_data()
        

if test_string == "[AVAILABLE]\n":
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "ACTIONS", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","1. MARK ATTENDANCE", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","2. MY CLASS", ""))
    print('{: ^9}|{:-^56}|{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","3. ABOUT", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","0. QUIT", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    prepare_class_list()
    while True:
        correct_action = None
        while correct_action not in [1, 2, 3, 0]:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            action = int(input('{: ^9}|{}'.format("","CHOOSE ACTION: ")))
        
            if action in [1, 2, 3, 0]:
                correct_action = action
                
            else:
                print("{: ^9}|{}".format("", "ERROR: Invalid input!"))

        if action == 1:
            if class_list == []:
              print("{: ^9}|{}".format("", "ERROR: No class found!"))
            else:
                mark_attendance()
            
        elif action == 2:
            edit_class()

        elif action == 3:
            display_about()
            
        elif action == 0:
            key = input("{: ^9}|{}".format("", "Press enter to quit....")).strip()
            exit()
            
else:
    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("", "WELCOME TEACHER!", ""))
    print('{: ^9}+{:-^56}+'.format("", ""))

    print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: ^56}|{: ^9}'.format("","ACTIONS", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","1. CREATE CLASS", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","2. ABOUT", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
    print('{: ^9}|{: <56}|{: ^9}'.format("","0. QUIT", ""))
    print('{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))

    while True:
        correct_action = None
        while correct_action not in [1, 2, 0]:
            print('\n{: ^9}+{:-^56}+{: ^9}'.format("", "", ""))
            action = int(input('{: ^9}|{}'.format("","CHOOSE ACTION: ")))
        
            if action in [1, 2, 0]:
                correct_action = action

            else:
                print("{: ^9}|{}".format("", "ERROR: Invalid input!"))

        if action == 1:
            create_class()

        elif action == 2:
            display_about()
            
        elif action == 0:
            key = input("{: ^9}|{}".format("", "Press enter to quit....")).strip()
            exit()
