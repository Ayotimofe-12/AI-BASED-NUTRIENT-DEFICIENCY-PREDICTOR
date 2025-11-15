# 🥗 AI-Based Nutrient Deficiency Predictor

An intelligent machine learning system that analyzes dietary intake and predicts potential nutrient deficiencies. This project combines **Data Science**, **Machine Learning**, and **Nutrition Science** to help users understand gaps in their diet and make data-driven health decisions.

---

## 🚀 Project Overview

The AI-Based Nutrient Deficiency Predictor processes user-provided meal information and estimates if they are at risk of deficiencies across key nutrients such as:

- Vitamin C  
- Vitamin B12  
- Calcium  
- Protein  
- Fiber  
- Selenium  
- Fat  

The system uses a supervised machine learning model trained on the **NHANES dietary dataset**, with a complete pipeline for preprocessing, feature scaling, proxy mapping, model training, evaluation, and deployment.

A simple and interactive **Streamlit web app** allows real-time prediction.

---

## 🧠 Key Features

- **Automated Nutrient Prediction**  
  Predicts deficiency levels based on dietary inputs.

- **End-to-End Data Pipeline**  
  Includes cleaning, preprocessing, feature engineering, scaling, and encoding.

- **Custom Proxy Mapping System**  
  Converts user food descriptions into estimated nutrient values.

- **Trained Supervised ML Model**  
  Achieves an accuracy score of ~**0.76**.

- **Streamlit Web Interface**  
  Clean, user-friendly app for interacting with the model.

- **Deployment Ready**  
  Includes compressed ML model and `app.py` for deployment.

---

## 📁 Project Structure
├── data/

│ ├── dietary.csv

│ ├── demographics.csv

│
├── notebooks/

│ └── AI-Based Nutrient Predictor.ipynb

│
├── model/

│ ├── nutrient7_model_compressed.joblib

│
├── app/

│ ├── app.py

│ └── requirements.txt


---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-Learn   
- Jupyter Notebook  
- NHANES Dietary Intake Dataset  
- Streamlit  
- Joblib (for model compression)

---

## 🔬 Machine Learning Workflow

1. **Data Cleaning**  
   Handling missing values, selecting relevant nutrients, removing noise.

2. **Feature Engineering**  
   - Nutrient proxy mapping for user diets  
   - Selecting predictive nutrient features  

3. **Preprocessing & Scaling**    
   - Label encoding for deficiency classes  

4. **Model Training**  
   - Train/test split (80/20)  
   - MultiOutputClassifier / RandomForestClassifier  
   - Final accuracy: **0.76**

5. **Model Compression**  
   Reduced model size using Pickle for easier deployment.

6. **Deployment**  
   Streamlit app built for real-time nutrient deficiency prediction.

---

## 🖥️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/nutrient-deficiency-predictor.git
cd nutrient-deficiency-predictor

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Streamlit App
streamlit run app.py

### 🌐 Live Demo

https://ai-based-nutrient-deficiency-predictor-s4836posvyvkhphi7zwqqs.streamlit.app/.

📈 Use Cases

Students tracking nutrition

Health and fitness applications

Diet planning systems

Personalized health assistants

Early deficiency detection

🔮 Future Improvements

Add more nutrients to the model
Improve proxy mapping using NLP (Text-to-Nutrient)

Integrate direct nutrient databases (USDA, FAO)

Deploy as a REST API

Add mobile-responsive UI

🤝 Contributions

Contributions, issues, and feature requests are welcome.
Feel free to open a pull request.

📧 Contact

Name: Omolola Olorunnishola
Email: (Olorunnisholalola@gmail.com)
