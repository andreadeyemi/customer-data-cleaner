# Customer Data Cleaner

A Python script that simulates real SaaS data cleanup before onboarding.  
It removes bad emails, deletes duplicates, and standardizes messy column headers.

---

## 🧹 What It Does

✅ Removes rows with missing emails  
✅ Drops duplicate email entries  
✅ Converts column headers to lowercase with underscores  
✅ Outputs a clean CSV for import into CRMs or SaaS platforms

---

## 📂 Files

- `clean_customers.py` → Main cleanup script  
- `sample_customers.csv` → Sample messy dataset  
- `cleaned_customers.csv` → Output (generated after running script)

---

## 🔧 Tech

- Python 3.8+
- Pandas

---

## 🏁 Run It

```bash
pip install pandas
python clean_customers.py
