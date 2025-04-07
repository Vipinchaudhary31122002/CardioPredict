# 🫀 CardioPredict - Heart Disease Risk Analyzer

**CardioPredict** is a smart, ML-powered application that helps analyze your risk of heart disease using interactive forms, clinical features, and trained classification models. It's designed with doctors, patients, and health enthusiasts in mind — making heart health prediction more accessible than ever!

---

## 🚀 Features

✅ **Smart Risk Prediction**: Instantly predicts whether a patient is at risk of cardiovascular disease.  
✅ **Interactive Health Form**: User-friendly dropdowns for 18+ symptoms and risk factors.  
✅ **Boolean Mapping**: Uses intuitive True/False and Male/Female inputs.  
✅ **ML Integration**: Seamlessly connects to a trained machine learning model.  
✅ **Dynamic Input Fields**: Reads from a JSON config so you can easily adjust fields.  
✅ **Clean UI/UX**: Sidebar description, emoji-enhanced labels, and structured layout.  
✅ **Safe and Local**: All processing happens on your machine. No data leaves your device.  

---

## 🛠️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vipinchaudhary31122002/CardioPredict
cd CardioPredict
```

### 2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎯 Usage Guide

### 🏁 Start the Application
```bash
streamlit run app.py
```

### 📝 Fill Patient Data
- Use dropdowns to provide information like:
  - **Chest Pain**, **Fatigue**, **Shortness of Breath**
  - **High BP**, **Diabetes**, **Cholesterol**, etc.
  - **Age** and **Gender**
  
### 💡 Get Risk Prediction
- Submit the form to instantly get:
  - ✅ **Low Risk**
  - ⚠️ **High Risk**


## 👨‍💻 Contributing

Contributions are welcome! 🎉  
Want to add enhancements or fix bugs?

1. Fork the repo 🍴  
2. Create a new branch (`feature-name`) 🌱  
3. Make your changes 🛠️  
4. Commit & push (`git commit -m 'Add feature'`) 📌  
5. Open a pull request ✅  

---

## 💡 Future Enhancements

🔹 Add visual analytics (feature importances, SHAP values)  
🔹 Export prediction results as PDF report  
🔹 Deploy to Streamlit Cloud or Hugging Face Spaces  
🔹 Add multilingual support for international use  

---

## 📌 Disclaimer

This app is intended **for educational and demonstrative purposes only**. It is **not a substitute for professional medical diagnosis**. Always consult with certified healthcare providers for medical concerns.

---