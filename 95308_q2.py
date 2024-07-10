class Student:
    def ___init____(self, name):
        self.name = name
        self.grades = {} # dict to store subjects and grades

    def add_grade(self,subject,grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values())/ len(self.grades)
    

    class Classroom:
        def __init__(self):
            self.students = []

        def add_student(self,student):
            self.students.append(student)

        def display_all_students(self):
            if not self.students:
                print("No students in the classroom.")
                return
            for student in self.students:
                print(f"Student:{student.name}, Grades: {student.grade}")
        def get_student_average(self, student_name):
            for student in self.students:
                if student.name.lower() == student_name.lower():
                    return student.get_average_grade()
            print(f"student {student_name} not found.")
            return None
        def get_class_average(self,subject):
            total_grade = 0
            count = 0
            for student in self.students:
                if subject in student.grades:
                    total_grade += student.grades[subject]
                    count += 1
            if count == 0:
                print(f"No grades found for subject: {subject}")
                return None
            return total_grade / count
        # demonstrating functionalities
        def main():
            #create an instance of the classroom
            classroom = classroom()

            #Add students to the classroom
            Student1 = Student("Alice")
            Student1.add_grade("Math",90)
            Student1.add_grade("English",85)

            Student2 = Student("Bob")
            Student2.add_grade("Math",80)
            Student2.add_grade("English",67)

            classroom.add_students(Student1)
            classroom.add_students(Student2)

            #Dispaly all the students
            print("\nAll students:")
            classroom.display_all_students()

            #Get average for a specific student
            print(f"\nClass average for Math: {classroom.get_class_average('Math')}")
            print(f"Class average for English:{classroom.get_class_average('English')}")
