# Insurance Premium Prediction Using Machine Learning

This project predicts insurance charges based on medical history, demographic details, and financial attributes using machine learning techniques.

## 📊 Dataset
The dataset consists of approximately 1338 records and 13 features, including:
- Age, Sex, BMI  
- Number of Children  
- Smoking Status  
- Region  
- Claim Amount  
- Hospital Expenditure  
- Annual Salary  

## ⚙️ Preprocessing
- Handled missing values using median imputation  
- Encoded categorical variables using binary and one-hot encoding  
- Removed irrelevant feature (num_of_steps)  
- Cleaned and structured data for model training  

## 🤖 Model
- Models used: Linear Regression, Decision Tree, Random Forest, Gradient Boosting, KNN  
- **Gradient Boosting Regressor** selected as final model  
- Achieved:
  - **MAE ≈ 565**  
  - **RMSE ≈ 1067**  
  - **R² ≈ 0.993**  

## 🚀 Web Application
A **Streamlit web app** was built where users can input personal, medical, and financial details to get predicted insurance charges instantly.

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Streamlit  
- VS Code  

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

📌 Conclusion

This project demonstrates how machine learning can accurately predict insurance premiums and assist in risk assessment and pricing decisions.