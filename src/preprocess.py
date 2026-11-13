import pandas as pd

from src.url_features import extract_features

# Load the original dataset
DATA_PATH = "data/url_features_extracted1.csv"

df = pd.read_csv(DATA_PATH)

print("Original dataset shape:", df.shape)

# Remove missing URLs and labels
df = df.dropna(subset=["URL", "ClassLabel"])

# Remove duplicate URLs
df = df.drop_duplicates(subset=["URL"], keep="first")

# Convert labels to integers
df["ClassLabel"] = df["ClassLabel"].astype(int)

# Extract features from each URL
feature_rows = []
valid_indices = []

print("\nExtracting URL features...")

for index, row in df.iterrows():
    try:
        features = extract_features(str(row["URL"]))
        feature_rows.append(features)
        valid_indices.append(index)
    except ValueError:
        continue

# Create a new feature dataset
features_df = pd.DataFrame(feature_rows, index=valid_indices)

# Keep original URLs and their labels
result = pd.concat(
    [
        df.loc[valid_indices, ["URL", "ClassLabel"]],
        features_df
    ],
    axis=1
)

# Save the newly extracted dataset
OUTPUT_PATH = "data/cleaned_dataset.csv"

result.to_csv(OUTPUT_PATH, index=False)

print("\nFeature extraction completed!")
print("Final dataset shape:", result.shape)

print("\nClass distribution:")
print(result["ClassLabel"].value_counts())

print("\nSaved to:", OUTPUT_PATH)