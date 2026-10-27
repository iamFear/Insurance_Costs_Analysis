import csv

# Return a list of iterables dictionaries with the keys being the column names and the values being the values of the row

# List of all header names (keys)
key_values = []

def load_rows(file_path):
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # List of dictionaries with the keys being the column names and the values being the values of the row
        file_rows = []

        # Add the row to the list of dictionaries after converting the numeric values to floats or integers
        for row in reader:
            for key, value in row.items():
                if key in ["age", "children"]:
                    row[key] = int(value)
                elif key in ["charges", "bmi"]:
                    row[key] = float(value)
            file_rows.append(row)

        # print(file_rows)

        # Return a list of dictionaries containing each users values with their right data-type
        return file_rows

# Run from the project directory so this relative path finds the dataset.
file_rows = load_rows("insurance.csv")

# DATA ANALYSIS AND COMPARISONS FUNCTIONALITY:

# Count all instances of an specific key value in a dataset
def count_key_values(key, checker):
    # Add to the key_values variable the header of each column
    with open("insurance.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # List of all header names (keys)
        key_values = reader.fieldnames

        # Check if the key exists, and if so, return the total matches for the checker
        if key in key_values:
            total = 0

            for row in file_rows:
                if row[key] != checker:
                    continue
                else:
                    total += 1

            return total
        else:
            return "Error, key doesn't exist in the `insurance.csv` file."

# Compare smokers BMI vs non-smokers BMI and return the percentage difference
def smoking_vs_BMI(dataset_list):

    # Total smokers and their BMI total sum
    smokers_bmi_sum = 0
    smokers_total = 0

    # Total non-smokers and their BMI total sum
    non_smokers_bmi_sum = 0
    non_smokers_total = 0

    for row in dataset_list:
        if row['smoker'] == 'yes':
            smokers_bmi_sum += row['bmi']
            smokers_total += 1
        # If non-smoker
        else:
            non_smokers_bmi_sum += row['bmi']
            non_smokers_total += 1

    # Average for each group of people
    smokers_average = smokers_bmi_sum / smokers_total
    non_smokers_average = non_smokers_bmi_sum / non_smokers_total

    # Shows the BMI percentage difference between smokers and non-smokers
    percentage_diff = round((smokers_average - non_smokers_average)  / non_smokers_average * 100, 2)

    # Return a string with the results of the BMI analysis between smokers and non-smokers
    return f"The average smoker has a BMI of {round(smokers_average, 2)},\nwhile the average non-smoker has an average BMI of {round(non_smokers_average, 2)},\nshowing us a BMI difference of {percentage_diff}% between the people who smoke and the people who don't."

print(smoking_vs_BMI(file_rows))
