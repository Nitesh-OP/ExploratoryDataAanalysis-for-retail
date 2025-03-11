# 📊 Superstore Sales Performance Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-green)

Comprehensive exploratory data analysis (EDA) of retail superstore data to identify sales patterns, profit drivers, and underperforming regions. Developed during data analytics training to demonstrate business intelligence capabilities.

---

## 📌 Project Overview
**Objective**: Analyze 10,000+ sales records to optimize business strategies  
**Key Insights**:
- Identified 15% duplicate entries requiring data cleaning
- Revealed **Texas** as top profit state ($25k) vs **Pennsylvania** (-$25k loss)
- Discovered **Phones** as best-selling sub-category (17% of total sales)
- Found **Standard Class** shipping generates 60% of total revenue

---

## 📂 Dataset
**Source**: SampleSuperstore Data (Common retail analytics dataset)  

| Feature        | Description                     | Relevance |
|----------------|---------------------------------|-----------|
| **Sales**      | Transaction amount             | Key metric|
| **Profit**     | Net financial gain             | Target    |
| **Quantity**   | Items per transaction          | Volume    |
| **Category**   | Product classification         | Strategy  |
| **Region**     | Geographic division            | Logistics |

**Original Features**: 13 columns • 9,994 cleaned rows

---

## 🛠️ Technical Implementation

### Data Cleaning
```python
# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove irrelevant feature
df.drop(columns="Postal Code", inplace=True)
