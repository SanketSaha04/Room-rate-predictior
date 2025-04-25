# 🧠 AI-Based Room Rate Prediction using CatBoost

This project predicts flat/room prices dynamically based on their location and features using a two-stage CatBoost model. The app is built using Streamlit.

## 📌 Features
- Stage 1: Predicts base price using location.
- Stage 2: Adjusts prediction using features like area, furnishing, parking, etc.
- Clean Streamlit UI for user interaction.
- Dashboard and insights available on a secondary page.


## 📂 Project Structure
```
project/
 ├── app.py                     # Main Streamlit App
 ├── notebook.ipynb              # EDA
 ├── catboost_stage1_location_model.pkl
 ├── catboost_stage2_correction_model.pkl
 ├── mumbai house dataset.csv    # Original dataset
 ├── locations.csv               # Unique location list
 ├── location_mean_price.csv     # Location price mapping
 ├── pages/
 │   └── 1_Dashboard.py          # Dashboard page
 └── requirements.txt
```


##  Getting Started

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install dependencies: 
```bash
pip install -r requirements.txt

3. Run the app:
```bash
streamlit run app.py


📊 Technologies Used
Python
CatBoost
Streamlit
Pandas, 
Scikit-learn,
Joblib

📝 Authors
Sanket Saha