import pandas as pd
from algos import damerau_levenshtein_distance

# Load the dataset
df = pd.read_csv("enhanced_indian_names_dataset.csv")

# Function to calculate distance and accuracy
def calculate_damerau_distance_and_accuracy(row):
    first_name = row["First Name"]
    variant = row["Variant"]
    
    # Damerau-Levenshtein distance
    dam_lev_dist = damerau_levenshtein_distance(first_name, variant)
    
    # Accuracy calculation
    max_length = max(len(first_name), len(variant))
    
    # Avoid division by zero
    if max_length == 0:
        accuracy = 100.0  # Both strings are empty
    else:
        accuracy = (1 - (dam_lev_dist / max_length))*100
    
    return pd.Series([dam_lev_dist, accuracy])

# Apply the function to each row and create new columns for distance and accuracy
df[["Damerau-Levenshtein Distance", "Damerau Accuracy"]] = df.apply(calculate_damerau_distance_and_accuracy, axis=1)

# Save the updated DataFrame with the new columns to a new CSV file
df.to_csv("dam_leven.csv", index=False)

print("Damerau-Levenshtein distance and accuracy calculated and saved successfully!")