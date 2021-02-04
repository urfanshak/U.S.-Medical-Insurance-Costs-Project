import csv
import matplotlib.pyplot as plt


#creating empty lists to add to them. this should make it easier for me to work with this information
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
insurance_cost = []

with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)

    #might be slightly long winded but this is adding the respective values from each column into a list which...
    #i will be able to work with later
    for row in insurance_dict:
        ages.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        insurance_cost.append(row['charges'])


# function to return the average age from the whole database
def average_age(ages):
    total_age = 0
    for age in ages:
        total_age += int(age)

    return total_age / len(ages)

average_age = average_age(ages)
#print(average_age)

def majority_region(region):
    regions_count = {"Northeast": 0, "Northwest": 0, "Southeast": 0, "Southwest": 0}

    #counting how many people are in each region and updating the respective value in the dictionary
    for place in region:
        if place == 'northeast':
            regions_count['Northeast'] += 1
        elif place == 'northwest':
            regions_count['Northwest'] += 1
        elif place == 'southeast':
            regions_count['Southeast'] += 1
        else:
            regions_count['Southwest'] += 1

    return regions_count, max(regions_count, key=regions_count.get)

regions_dict, max_region = majority_region(region)
#print(max_region)

def average_insurance_cost_by_age(ages, insurance_cost):

    cost_per_age = {}
    for i in range(18,65):
        cost_per_age[i] = 0

    #adding up a total of insurance costs for each different age
    for age, cost in zip(ages, insurance_cost):
        cost_per_age[int(age)] += float(cost)

    #now we need the average insurance cost for each age
    average_cost_per_age_dict = {}
    for age in cost_per_age:
        average_cost_per_age = cost_per_age[age] / ages.count(str(age))
        average_cost_per_age_dict[age] = average_cost_per_age

    return average_cost_per_age_dict


cost_per_age_dict = average_insurance_cost_by_age(ages, insurance_cost)
#print(cost_per_age_dict)

#plotting age vs insurance cost
def plot_age_vs_insurance_cost(ages, insurance_cost):

    x = [int(age) for age in ages]
    y = [float(cost) for cost in insurance_cost]

    plt.plot(x, y, 'ro', markersize=1)

    plt.show()

#with this plot you can see that there are 'three lines of best fit'. with the strongest correlation being the bottom one
plot_age_vs_insurance_cost(ages, insurance_cost)




