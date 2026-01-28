FILE_NAME = "students.txt"

# ADD STUDENT
def add_student():
    print("\n--- ADD STUDENT ---")
    Name = input("\nEnter Student Name: ")
    Roll_Number = int(input("Enter Roll Number: "))
    Hindi = int(input("Marks In Hindi: "))
    English= int(input("Marks In English: "))
    Accountancy = int(input("Marks In Accountancy: "))
    Economics = int(input("Marks In Economics: "))
    Business_Studies = int(input("Marks In Business Studies: "))
    Physical_Education = int(input("Marks In Physical Education: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{Roll_Number},{Name},{Hindi},{English},{Accountancy},{Economics},{Business_Studies},{Physical_Education}\n")
    
    print("\nSTUDENT ADDED SUCCESSFULLY!")

# UPDATE STUDENT
def update_student():
    print("\n--- UPDATE STUDENT ---")
    roll_number_to_update = int(input("\nEnter Roll Number To Update: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        with open(FILE_NAME, "w") as file:
            found = False

            for line in students:
                roll, *_ = line.strip().split(",")

                if roll == roll_number_to_update:
                    found = True
                    print("\nENTER NEW DETAILS:\n")

                    Name_Update = input("Enter Student Name: ")
                    Hindi_Update = int(input("Marks In Hindi: "))
                    English_Update = int(input("Marks In English: "))
                    Accountancy_Update = int(input("Marks In Accountancy: "))
                    Economics_Update = int(input("Marks In Economics: "))
                    Business_Studies_Update = int(input("Marks In Business Studies: "))
                    Physical_Education_Update = int(input("Marks In Physical Education: "))

                    file.write(f"{roll},{Name_Update},{Hindi_Update},{English_Update},{Accountancy_Update},{Economics_Update},{Business_Studies_Update},{Physical_Education_Update}\n")
                else:
                    file.write(line)

        if found:
            print("\nSTUDENT UPDATED SUCCESSFULLY!")
        else:
            print("\nROLL NUMBER NOT FOUND")

    except FileNotFoundError:
        print("\nNO STUDENT FOUND")

# VIEW ALL STUDENTS
def view_all_students():
    print("\n--- VIEW ALL STUDENTS ---")

    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("\nNO STUDENT RECORD FOUND")
                return

            for line in data:
                roll, name, hindi, eng, acc, eco, bus, pe = line.strip().split(",")
                print(f"""
Roll No : {roll}
Name : {name}
Hindi : {hindi}
English : {eng}
Accountancy : {acc}
Economics : {eco}
Business Studies : {bus}
Physical Education : {pe}
--------------------------
""")
    except FileNotFoundError:
        print("\nNO STUDENT FILE")

# DELETE STUDENT
def delete_student():
    print("\n--- DELETE STUDENT ---")
    roll_to_delete = int(input("\nEnter Roll Number To Delete: "))

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        with open(FILE_NAME, "w") as file:
            found = False
            for line in students:
                roll, *_ = line.strip().split(",")
                if roll != roll_to_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print("\nStudent Deleted Successfully!")
        else:
            print("\nROLL NUMBER NOT FOUND")

    except FileNotFoundError:
        print("\nNO STUDENT FILE FOUND")

# MENU
def menu():
    print("\n---------- STUDENT MANAGEMENT SYSTEM ----------")
    while True:       
        print("\n1). Add Student")
        print("2). Update Student Details")
        print("3). View All Students")
        print("4). Delete Student")
        print("5). Exit")

        choice = input("\nEnter Your Choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            view_all_students()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("\nEXITING PROGRAM. BYE!\n")
            break
        else:
            print("\nINVALID CHOICE! TRY AGAIN.\n")

# Program Start
menu()
