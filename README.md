# Machine Learning Fundamentals

This repository contains class practice and assignments covering data handling, visualization, data preprocessing, and introductory machine learning with Python.

## Project contents

### Practice notebooks

| Path | Description | Data |
| --- | --- | --- |
| `pandas_practice.ipynb` | Pandas basics, including DataFrames, selecting and filtering data, and reading CSV files. | `Universities.csv` |
| `visuals.ipynb` | Introductory charts with Matplotlib, including line, bar, and pie charts. | Example values are created in the notebook. |
| `SLR/Waist_at.ipynb` | Explores waist circumference and AT, visualizes their relationship, and fits a simple linear regression model. | `SLR/WC_AT.csv` |
| `MLR/cars.ipynb` | Explores car data and builds a multiple linear regression model. | `MLR/Cars.csv` |
| `Logistic-Regression/LR.ipynb` | Prepares claimant data and trains/evaluates a logistic regression classifier. | `Logistic-Regression/claimants.csv` |

### Assignments

| Path | Description | Data |
| --- | --- | --- |
| `ML Assignment 1/Assignment1.ipynb` | Explores housing data, summarizes and visualizes features, and practices regression. | `ML Assignment 1/train_houses.csv` |
| `ML Assignment 2/ass2.ipynb` | Examines the relationship between waist circumference and AT, then fits and reviews a simple linear regression model. | `ML Assignment 2/WC_AT.csv` |
| `Assignment3/Assignment3.ipynb` | Practices label encoding and one-hot encoding on the Iris data, detects outliers with Isolation Forest, and explores predictive power scores. | `Assignment3/iris.csv` |
| `Assignment4/ass4.ipynb` | Checks employee data, encodes department and city, scales numeric features, and saves the encoded data. | `Assignment4/employee_data.csv` |

### Assignment 4 output files

| Path | Description |
| --- | --- |
| `Assignment4/employee_data_encoded.csv` | Output written by `ass4.ipynb`, containing encoded and scaled employee columns. |
| `Assignment4/employee_data_processed.csv` | Additional employee data file in the project directory for comparison. |

## Setup and running

Use Python 3 and install Jupyter with the libraries used by the notebooks:

```bash
python -m pip install jupyter pandas numpy matplotlib seaborn statsmodels scikit-learn
```

From the project root, start Jupyter:

```bash
jupyter notebook
```

Open a notebook and run its cells in order. For notebooks that load a CSV using a relative path, start Jupyter from the project root or adjust the working directory to the notebook's folder as needed.

## Notes

- `pandas_practice.ipynb` may refer to `universities.csv` in lowercase, while the repository file is named `Universities.csv`. On case-sensitive systems, update the notebook path to match the filename.
- The final cell in `Assignment4/ass4.ipynb` writes `employee_data_encoded.csv`. Its printed message mentions `Employee_data_processed.csv`, which does not match the output filename.
- Some notebooks include `%pip install` cells for packages used in that notebook. Run those cells if the package is not already installed.
