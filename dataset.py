import random
import pandas as pd
import csv

# List of common Indian first names with phonetic variations
first_names = {
    "Suresh": ["Suresh", "Shuresh", "Surush"],
    "Rajesh": ["Rajesh", "Rajeshwar", "Rajeesh"],
    "Priya": ["Priya", "Priyaa", "Preya"],
    "Avinash": ["Avinash", "Avinash Kumar", "Avinash Reddy"],
    "Meena": ["Meena", "Meena Kumari", "Meena Devi"],
    "Amit": ["Amit", "Amitabh", "Amitesh"],
    # Add more names as needed
}

# List of common Indian middle names and surnames
middle_names = ["Kumar", "Singh", "Verma", "Patel", "Sharma"]
surnames = ["Kumar", "Singh", "Verma", "Patel", "Sharma", "Gupta", "Mishra"]

# List of Indian cities
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Pune", "Ahmedabad", "Lucknow", "Patna","Ranchi","Kota"]

# Function to generate a unique record
def generate_record():
    first_name = random.choice(list(first_names.keys()))
    variant = random.choice(first_names[first_name])
    middle_name = random.choice(middle_names)
    surname = random.choice(surnames)
    gender = random.choice(["Male", "Female"])
    age = random.randint(20, 60)
    address = random.choice(cities)
    return [first_name, variant, middle_name, surname, gender, age, address]

# Generate 100 unique records
records = []
while len(records) < 100:
    record = generate_record()
    if record not in records:
        records.append(record)

# Create a pandas DataFrame from the records
df = pd.DataFrame(records, columns=["First Name", "Variant", "Middle Name", "Surname", "Gender", "Age", "Address"])

# Add an ID column
df["ID"] = range(1, len(df) + 1)

# Save the DataFrame to a CSV file
df.to_csv("enhanced_indian_names_dataset.csv", index=False)

print("Dataset generated successfully!")