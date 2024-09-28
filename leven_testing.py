import pandas as pd
import Levenshtein as lev
import csv

# Load the dataset
df = pd.read_csv("enhanced_indian_names_dataset.csv")

# Function to calculate distance and accuracy
def calculate_distance_and_accuracy(row):
    first_name = row["First Name"]
    variant = row["Variant"]
    
    # Levenshtein distance
    lev_dist = lev.distance(first_name, variant)
    
    # Accuracy calculation
    max_length = max(len(first_name), len(variant))
    accuracy = (1 - (lev_dist / max_length))*100
    
    return pd.Series([lev_dist, accuracy])

# Apply the function to each row and create new columns for distance and accuracy
df[["Levenshtein Distance", "Accuracy"]] = df.apply(calculate_distance_and_accuracy, axis=1)

# Save the updated DataFrame with the new columns to a new CSV file
df.to_csv("leven.csv", index=False)

print("Levenshtein distance and accuracy calculated and saved successfully!")