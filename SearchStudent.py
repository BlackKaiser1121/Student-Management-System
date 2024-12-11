class searchStudent:
    def search_students(self, students_list, id_number):
        # Loop through the list of students
        for student in students_list:
            # Check if the id_number matches the student's id_number
            if student.id_number == id_number:
                # Return the student's details if a match is found
                return f"Name: {student.name}, Age: {student.age}, Email: {student.email}, Phone: {student.phone}"
        # If no match is found, return this message
        return "Student not found."
