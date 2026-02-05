import pandas as pd
import numpy as np

#Loads the dataset from the csv file to pandas dataframe
crimeInformationPerPopulation = pd.read_csv("crime.csv")

#Set the filters for the crime risk levels
crimeRiskFilters = [(crimeInformationPerPopulation["ViolentCrimesPerPop"] >= 0.50),
                    (crimeInformationPerPopulation["ViolentCrimesPerPop"] < 0.50)]

#Name of the crime risk levels category above
crimeRiskCategoryName = ["High-Crime", "LowCrime"]

#Creates a new column named risk
crimeInformationPerPopulation["risk"] = np.select(crimeRiskFilters, crimeRiskCategoryName, default="Unknown")

#Groups the data by their crime risk level category
crimesGroupedByRisk = crimeInformationPerPopulation.groupby("risk")

#Calculates the average percent of unemployment by crime risk level
averagePercentOfUnemployed = crimesGroupedByRisk["PctUnemployed"].mean()

#Stores the data for high crime risk and low crime risk unemployment average percentage
highRiskAveragePercentOfUnemployment = averagePercentOfUnemployed["High-Crime"]
lowRiskAveragePercentOfUnemployment = averagePercentOfUnemployed["LowCrime"]

#Displays the final results with proper formatting
print(f"Average Unemployment Rate by Crime Risk\n"
      f"High-Crime: {highRiskAveragePercentOfUnemployment:.2f}\n"
      f"Low-Crime: {lowRiskAveragePercentOfUnemployment:.2f}")

