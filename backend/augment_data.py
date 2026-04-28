import pandas as pd
import numpy as np
from sklearn.utils import resample

print("Loading original dataset...")

df = pd.read_csv("data/Placement_Data_Full_Class.csv")

print(f"Original rows: {len(df)}")

# Convert important categorical columns into numbers
df['gender_num'] = (df['gender'] == 'M').astype(int)
df['workex_num'] = (df['workex'] == 'Yes').astype(int)
df['status_num'] = (df['status'] == 'Placed').astype(int)

# Convert text categories into numeric IDs
df['degree_t_num'] = pd.factorize(df['degree_t'])[0]
df['specialisation_num'] = pd.factorize(df['specialisation'])[0]
df['hsc_s_num'] = pd.factorize(df['hsc_s'])[0]

# Features we want for our fairness model
features = [
    'gender_num',
    'ssc_p',
    'hsc_p',
    'degree_p',
    'workex_num',
    'etest_p',
    'mba_p',
    'degree_t_num',
    'specialisation_num',
    'status_num'
]

df_clean = df[features].dropna()

print(f"Clean rows after preprocessing: {len(df_clean)}")

# Expand dataset using bootstrap resampling
augmented = resample(
    df_clean,
    n_samples=2000,
    replace=True,
    random_state=42
)

# -----------------------------------
# Inject stronger gender bias for demo
# -----------------------------------

# Reduce positive outcomes for female candidates
female_mask = augmented["gender_num"] == 0

# Randomly force some female placed candidates to rejected
female_placed = augmented[
    (female_mask) &
    (augmented["status_num"] == 1)
].sample(frac=0.30, random_state=42)

augmented.loc[female_placed.index, "status_num"] = 0

# Add small Gaussian noise to avoid exact duplicate rows
numeric_cols = [
    'ssc_p',
    'hsc_p',
    'degree_p',
    'etest_p',
    'mba_p'
]

for col in numeric_cols:
    noise = np.random.normal(0, 0.5, size=len(augmented))
    augmented[col] = (augmented[col] + noise).clip(0, 100)

# Save final augmented dataset
output_path = "data/augmented_hiring.csv"
augmented.to_csv(output_path, index=False)

print("\n=== AUGMENTATION COMPLETE ===")
print(f"Saved file: {output_path}")
print(f"Total rows: {len(augmented)}")
print(f"Overall placement rate: {augmented['status_num'].mean():.2%}")

male_rate = augmented[augmented['gender_num'] == 1]['status_num'].mean()
female_rate = augmented[augmented['gender_num'] == 0]['status_num'].mean()

print(f"Male placement rate: {male_rate:.2%}")
print(f"Female placement rate: {female_rate:.2%}")

if male_rate > female_rate:
    print("Bias pattern exists → good for fairness demo")
else:
    print("Check dataset — expected male rate should be higher")
