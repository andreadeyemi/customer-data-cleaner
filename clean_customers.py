"""
Customer Data Cleaner Script

This script cleans raw customer data by:
- Dropping rows with missing email addresses
- Removing duplicates based on email
- Standardizing column headers

Ideal for SaaS onboarding workflows.
"""

import pandas as pd

# Load data
df = pd.read_csv('sample_customers.csv')

# Drop rows with missing emails
df = df.dropna(subset=['email'])

# Clean column headers
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Remove duplicate emails
df = df.drop_duplicates(subset='email')

# Save cleaned data
df.to_csv('cleaned_customers.csv', index=False)

print("✅ Data cleaned. Output saved to 'cleaned_customers.csv'")
