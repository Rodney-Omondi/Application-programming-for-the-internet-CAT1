#intialize empty list to hold patient records
patients = []
#1.Define a function to add patients
def add_patient(name,age,illness):
    patient = {
        'name': name,
        'age' : age,
        'illness' : illness
    }
patients.append(patients)
print(f"patient {'name'} added successfully.")

#2. Define a function to display all the patients
def display_patients():
    if not patients:
        print("No patients found.")
        return
    for patient in patients:
        print(f"Name: {patient['name']}, Age:{patient['age']}, Illness:{patient['illness']}")

#3. Define a function to search for a patient by name
def search_patient(name):
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Name:{patient['name']}, Age:{patient['age']}, Illness:{patient['ilnesss']}")
            return
    print(f"patient {name} not found.")

#4. Function to remove a patient by name
def remove_patient(name):
    global patients
    patients = [patient for patient in patients if patient['name'].lower != name.lower()]
    print(f"patient {name} removed successfully.")

#5. Function to keep the program running
def main():
    while True:
        print("\n---hospital Management system ---")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. remove a patient by name")
        print("5.Exit")

    if choice =='1':
        name = input ("Enter patient's name:")
        age = input ("Enter patient's age:")
        illness = input ("Enter patient's illness:")
        add_patient(name,age,illness)
    elif choice == '2':
        display_patients()
    elif choice == '3':
        name = input("Enter the name of the patient to search:")
        search_patient(name)
    elif choice == '4':
        name = input("Enter the name of the patient to remove: ")
        remove_patient(name)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
    else:
        print("invalid choice. Please try again.")



    