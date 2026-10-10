import pandas as pd
import matplotlib.pyplot as plt

lwd = pd.read_csv("livwell135.csv")

india = lwd.loc[lwd["country_name"] == "India"]
firstYear = india["year"].min()
lastYear = india["year"].max()

print("\nThis dataset covers India from " + str(firstYear) + " to " + str(lastYear) + ".")
print("Research question: What factors cause differences in education between rural and urban females?\n")
input("Press enter to see the data.\n")

startEduc = india.loc[india["year"] == firstYear, "ED_educ_years_mean"].iloc[0]
endEduc = india.loc[india["year"] == lastYear, "ED_educ_years_mean"].iloc[0]
print("Mean years of schooling went from " + str(startEduc) + " in " + str(firstYear) + " to " + str(endEduc) + " in " + str(lastYear) + ".\n")
input("Press enter to see the first graph.\n")

# Graph 1: schooling over time
plt.scatter(india["year"], india["ED_educ_years_mean"], color="red")
plt.grid(True)
plt.title("Mean Years of Schooling in India")
plt.xlabel("Year")
plt.ylabel("Mean Years of Schooling")
plt.ylim(0, 10)
plt.savefig("schooling_over_time.png")
plt.close()

print("The graph has been saved as schooling_over_time.png in your file explorer.\n")
input("Press enter to see the second graph.\n")

# Graph 2: rural vs urban electricity access
plt.plot(india["year"], india["ER_elec_urban_p"], color="blue", label="Urban")
plt.plot(india["year"], india["ER_elec_rural_p"], color="green", label="Rural")
plt.grid(True)
plt.title("Household Electricity Access in India: Urban vs. Rural")
plt.xlabel("Year")
plt.ylabel("Households With Electricity (%)")
plt.ylim(0, 100)
plt.legend()
plt.savefig("electricity_urban_vs_rural.png")
plt.close()

print("The graph has been saved as electricity_urban_vs_rural.png in your file explorer.\n")
print()
print("Conclusion: Schooling in India rose from about 3.1 to 5.9 years between 1993 and 2006, and rural households had less electricity access than urban ones. However, this data doesn't split education by rural and urban areas, so it can't show what causes the gap.\n")
print("Thank you for reading through my data analysis!")