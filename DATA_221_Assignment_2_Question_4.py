import pandas as pd

#Loads the student dataset into a pandas data frame
data_frame_for_portuguese_students_data = pd.read_csv("student.csv")

#Filters the students in terms of their study time, internet, and absences
filtered_students_data = data_frame_for_portuguese_students_data[(data_frame_for_portuguese_students_data["studytime"] >= 3) &
                          (data_frame_for_portuguese_students_data["internet"] == 1) &
                          (data_frame_for_portuguese_students_data["absences"] <= 5)]

#Save the filtered student data into a csv file named high_engagement.csv
filtered_students_data.to_csv("high_engagement.csv", index = False)

#Gets the total number of students that fits the filter
total_number_of_filtered_students = len(filtered_students_data)

#Gets the average grade of all the filtered students' grades
filtered_students_average_grade = filtered_students_data["grade"].mean()

#Displays the total number off filtered students as well as their average grade
print(f"The total number of students are {total_number_of_filtered_students}.\n"
      f"and their average grade is {filtered_students_average_grade:.2f}")
