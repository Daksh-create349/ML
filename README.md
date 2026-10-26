# Machine Learning Fundamentals

This repository contains my class notes, practice, and assignments for **Machine Learning Fundamentals**.

## Class content

- **Pandas practice** — creating DataFrames, inspecting data, selecting rows and columns, filtering records, and exploring a CSV dataset.
- **Data visualizations** — introductory line, bar, and pie charts with Matplotlib.
- **Simple linear regression** — exploring the relationship between waist circumference and AT, fitting a regression model, and reviewing its summary with statsmodels.
- **Assignment 1: house prices** — exploring housing data with Pandas, visualizing features and sale prices, and fitting a simple regression model.

## Files

| Path | Description |
| --- | --- |
| `pandas_practice.ipynb` | Pandas and DataFrame exercises |
| `visuals.ipynb` | Basic charting practice |
| `SLR/Waist_at.ipynb` | Waist circumference and AT linear regression exercise |
| `SLR/WC_AT.csv` | Data used by the SLR exercise |
| `ML Assignment 1/Assignment1.ipynb` | Housing data exploration and regression assignment |
| `ML Assignment 1/train_houses.csv` | Housing dataset used by Assignment 1 |
| `Universities.csv` | University data used in the Pandas practice |

## Running the notebooks

Install Python and Jupyter, then install the libraries used in the notebooks:

```bash
python -m pip install jupyter pandas matplotlib seaborn statsmodels
```

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Open a notebook and run its cells. Run notebooks from the repository root so their relative dataset paths resolve as expected.

> **Note:** `pandas_practice.ipynb` refers to `universities.csv` in lowercase, while the file in this repository is named `Universities.csv`. On case-sensitive systems, change the notebook's path to `Universities.csv` if it cannot find the file.
