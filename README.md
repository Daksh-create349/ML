# Machine Learning Repository

A comprehensive collection of machine learning coursework, hands-on lab implementations, and academic assignments covering exploratory data analysis (EDA), data preprocessing, supervised learning (regression and classification), unsupervised learning (clustering), and ensemble methods using Python.

---

## 📂 Repository Structure

```text
├── Clustering/
│   ├── kmeans.ipynb
│   ├── hac.ipynb
│   └── Universities.csv
├── Decision Trees/
│   ├── dec_tree.ipynb
│   └── iris.csv
├── Ensemble Modeling/
│   ├── ensemble_models.ipynb
│   └── pima_indians_diabetes.csv
├── Logistic-Regression/
│   ├── LR.ipynb
│   └── claimants.csv
├── MLR/
│   ├── cars.ipynb
│   └── Cars.csv
├── SLR/
│   ├── Waist_at.ipynb
│   └── WC_AT.csv
├── SVM Class/
│   ├── SVM.ipynb
│   └── pima_indians_diabetes.csv
├── ML Assignment 1/
│   ├── Assignment1.ipynb
│   └── train_houses.csv
├── ML Assignment 2/
│   ├── ass2.ipynb
│   └── WC_AT.csv
├── ML Assignment 3/
│   ├── Assignment3.ipynb
│   └── iris.csv
├── ML Assignment 4/
│   ├── ass4.ipynb
│   ├── employee_data.csv
│   └── employee_data_encoded.csv
├── ML Assignment 5/
│   ├── Assignment5.ipynb
│   ├── train.csv
│   └── titanic_predictions.csv
├── ML Assignment 6/
│   ├── dbscasn.ipynb
│   └── Mall_Customers.csv
├── ML Assignment 7/
│   ├── Knn_classification.ipynb
│   ├── Knn_regression.ipynb
│   ├── Iris.csv
│   └── housing.csv
├── ML Assignment 8/
│   ├── Ensemble_Assignment.ipynb
│   └── winequality-red.csv
├── pandas_practice.ipynb
├── visuals.ipynb
└── Universities.csv
```

---

## 📚 Assignments Overview

| Assignment | Notebook Path | Primary Dataset | Description & Techniques |
| :--- | :--- | :--- | :--- |
| **Assignment 1** | `ML Assignment 1/Assignment1.ipynb` | `train_houses.csv` | Exploratory data analysis, statistical summary, feature visualization, and regression modeling on house prices. |
| **Assignment 2** | `ML Assignment 2/ass2.ipynb` | `WC_AT.csv` | Simple Linear Regression (SLR) analyzing the relationship between waist circumference and adipose tissue. |
| **Assignment 3** | `ML Assignment 3/Assignment3.ipynb` | `iris.csv` | Categorical encoding (Label & One-Hot Encoding), outlier detection using Isolation Forest, and Predictive Power Score (PPS). |
| **Assignment 4** | `ML Assignment 4/ass4.ipynb` | `employee_data.csv` | Feature engineering on employee records: handling missing values, encoding nominal/ordinal variables, and standard scaling. |
| **Assignment 5** | `ML Assignment 5/Assignment5.ipynb` | `train.csv` | Titanic passenger survival prediction: end-to-end ColumnTransformer pipeline (imputation + scaling + encoding), Logistic Regression, and test prediction generation. |
| **Assignment 6** | `ML Assignment 6/dbscasn.ipynb` | `Mall_Customers.csv` | Density-Based Spatial Clustering of Applications with Noise (DBSCAN): k-distance elbow graph for optimal $\varepsilon$, core/border/noise point identification, and customer segmentation. |
| **Assignment 7 (Part 1)** | `ML Assignment 7/Knn_classification.ipynb` | `Iris.csv` | $K$-Nearest Neighbors classification on flower species: pairplot EDA, stratified train-test splitting, feature scaling, confusion matrix heatmap, and classification report. |
| **Assignment 7 (Part 2)** | `ML Assignment 7/Knn_regression.ipynb` | `housing.csv` | $K$-Nearest Neighbors regression on California housing: median value prediction, missing value imputation, one-hot encoding, feature scaling, and evaluation (MAE, MSE, RMSE, $R^2$). |
| **Assignment 8** | `ML Assignment 8/Ensemble_Assignment.ipynb` | `winequality-red.csv` | Ensemble learning for wine quality classification: Random Forest, AdaBoost, and Gradient Boosting benchmarking, confusion matrices, and feature importance analysis. |

---

## 🔬 Topic-Wise Practice & Lab Notebooks

### 1. Data Foundations & Visualization
* **`pandas_practice.ipynb`**: Fundamentals of Pandas: DataFrame operations, indexing, slicing, aggregation, and CSV data ingestion (`Universities.csv`).
* **`visuals.ipynb`**: Data visualization using Matplotlib: line plots, bar charts, scatter plots, and pie charts.

### 2. Regression Analysis
* **`SLR/Waist_at.ipynb`**: Simple Linear Regression implementation modeling adipose tissue as a function of waist circumference using Statsmodels and Scikit-Learn.
* **`MLR/cars.ipynb`**: Multiple Linear Regression modeling fuel efficiency (MPG) using vehicle attributes: multicollinearity diagnostics, Variance Inflation Factor (VIF), residual analysis, and model optimization.

### 3. Classification
* **`Logistic-Regression/LR.ipynb`**: Binary Logistic Regression predicting legal claimant representation: odds ratios, probability thresholds, and confusion matrix evaluation.
* **`Decision Trees/dec_tree.ipynb`**: Decision Tree Classifier on the Iris dataset: tree construction, max depth / criterion tuning (Gini vs. Entropy), and evaluation.
* **`SVM Class/SVM.ipynb`**: Support Vector Machine classification on Pima Indians Diabetes data: RBF kernel analysis, the majority-class collapse trap with unscaled data, and hyperparameter tuning with `GridSearchCV` ($C$ and $\gamma$).

### 4. Clustering (Unsupervised Learning)
* **`Clustering/kmeans.ipynb`**: $K$-Means clustering on university metrics: feature standardization, cluster profiling, Within-Cluster Sum of Squares (WCSS), and Elbow method hyperparameter tuning.
* **`Clustering/hac.ipynb`**: Hierarchical Agglomerative Clustering (HAC): Min-Max normalization, complete linkage calculation, dendrogram visualization, and silhouette score validation.

### 5. Ensemble Modeling
* **`Ensemble Modeling/ensemble_models.ipynb`**: Comparative study of ensemble architectures on diabetes diagnosis: Bagging (Bootstrap Aggregation), Random Forest, AdaBoost, and Voting/Stacking Classifiers with $K$-Fold cross-validation.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ML
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install jupyter pandas numpy matplotlib seaborn scikit-learn statsmodels scipy
   ```

4. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

---

## 📌 Usage Notes

* **Working Directory:** Most notebooks reference datasets relative to their directory or the project root. When executing notebooks in subdirectories, ensure the working directory is set to the respective folder or launch Jupyter directly from the project root.
* **File Naming & Path Cases:** Check dataset casing on Linux/macOS case-sensitive filesystems (e.g., `Universities.csv` vs. `universities.csv`, `iris.csv` vs. `Iris.csv`).
* **Generated Prediction Files:**
  * `ML Assignment 4/employee_data_encoded.csv`: Transformed and encoded output generated by `ass4.ipynb`.
  * `ML Assignment 5/titanic_predictions.csv`: Model predictions generated by `Assignment5.ipynb`.
