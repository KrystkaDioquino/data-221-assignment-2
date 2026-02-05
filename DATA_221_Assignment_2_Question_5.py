import pandas as pd
import numpy as np

#Loads the student dataset into a pandas data frame
data_frame_for_portuguese_students_data = pd.read_csv("student.csv")

#This makes grade ranges to identify categories. High (>=15), Medium (>=10), or Low (rest)
student_grade_range_filters = [(data_frame_for_portuguese_students_data["grade"] >= 15),
                               (data_frame_for_portuguese_students_data["grade"] >= 10),
                               (data_frame_for_portuguese_students_data["grade"] >= 0)]

#This is the name of each category above.
student_grade_range_category = ["High", "Medium", "Low"]

#Creates a new column named grade_band
data_frame_for_portuguese_students_data["grade_band"] = np.select(student_grade_range_filters,
                                                                  student_grade_range_category,
                                                                  default = "Unknown")
#This groups the student's data by their grade band
students_grouped_data = data_frame_for_portuguese_students_data.groupby("grade_band")

#Calculations for the student bands summary
#This is to get the total number of students in each band
number_of_students_per_band = students_grouped_data.size()

#Computes the average absences of students for each band
average_absences_of_students_per_band = students_grouped_data["absences"].mean()

#This computes the percentage of students with internet access for each band
mean_of_students_with_internet_per_band = students_grouped_data["internet"].mean()
percentage_of_students_with_internet_per_band = mean_of_students_with_internet_per_band * 100

#Creates a new data frame with the computed results
student_bands_summary = pd.DataFrame({"number_of_students": number_of_students_per_band,
                                      "average_absences": average_absences_of_students_per_band,
                                      "percentage_internet": percentage_of_students_with_internet_per_band})

#This is to create a uniform decimal value for all the computed values
student_bands_summary = student_bands_summary.round(2)

#Saves the final table to a csv file
student_bands_summary.to_csv("student_bands.csv")