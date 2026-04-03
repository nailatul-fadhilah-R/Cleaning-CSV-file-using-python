# Cleaning CSV file using python

## Project Overview
This project focuses on transforming a messy, synthetic employee dataset into a clean, structured, and analysis-ready format. Real-world data often arrives with encoding issues, inconsistent date formats, mixed types, and noise. This repository demonstrates a robust, repeatable 5-stage workflow (Load, Inspect, Clean, Review, Export) using Python and Pandas.

## Project Functionality
The primary function of this project is to automate the rectification of common data entry and system export errors. Key functionalities include:
* **Data Standardisation:** Normalising categorical values, fixing capitalization, and removing hidden whitespace.
* **Type Casting:** Ensuring numeric, boolean, and date columns are explicitly defined to prevent silent errors during computation.
* **Missing Value Imputation:** Handling null values in critical columns like 'Age' and 'Salary' using statistical methods (median) to maintain dataset integrity.
* **Feature Engineering:** Splitting complex columns (e.g., Department-Region) into separate, more granular attributes for better reporting.
* **Anomaly Correction:** Identifying and fixing logical errors, such as negative phone numbers or invalid date entries.

## Technologies Used
* **Pandas Library:** For data manipulation and transformation.
* **NumPy:** For handling numerical operations and null values.
* **VSCode:** For interactive development and visualization of the cleaning steps.

## The 5-Stage Workflow

### 1. Load
The dataset is loaded with explicit handling for multiple null variants (`N/A`, `NaN`, `null`) to ensure all missing data is recognized by the Pandas engine from the start.

### 2. Inspect
Initial audit using `.info()`, `.describe()`, and `.unique()` to identify:
* Inconsistent date strings.
* Leading/trailing spaces in names and categories.
* The presence of negative values in the 'Phone' column.
* The split character (`-`) in the `Department_Region` column.

### 3. Clean
* **Dates:** Converted `Join_Date` to `datetime64[ns]` using `pd.to_datetime` with `errors='coerce'`.
* **Strings:** Stripped whitespace and standardized text across `First_Name`, `Last_Name`, and `Status`.
* **Splitting:** Separated `Department_Region` into two distinct columns: `Department` and `Region`.
* **Negative Correction:** Applied absolute values to the `Phone` column.
* **Imputation:** Filled missing `Age` and `Salary` entries with the median values of their respective groups.

### 4. Review (Audit)
A final check is performed to verify:
* Zero null values across the entire DataFrame.
* Correct column data types (Dtypes).
* Logical consistency in categories (e.g., only 'Active', 'Pending', 'Inactive' remain).

### 5. Export
The refined data is exported to `Cleaned_Employee_Dataset.csv` for use in BI tools (PowerBI, Tableau) or machine learning models.

## Results 
The final output is a high-integrity CSV file that eliminates 100% of the initial formatting errors, providing a reliable foundation for any HR-related data analysis or reporting tasks.
