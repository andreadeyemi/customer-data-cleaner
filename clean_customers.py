import pandas as pd

df = pd.read_csv('sample_customers.csv')
df = df.dropna(subset=['email'])
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df = df.drop_duplicates(subset='email')
df.to_csv('cleaned_customers.csv', index=False)
print("✅ Data cleaned.")
