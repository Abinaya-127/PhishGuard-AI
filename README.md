🛡️ PhishGuard AI – Intelligent Phishing URL Detection System

📌 Project Overview

PhishGuard AI is a machine-learning-based cybersecurity project designed to identify potentially phishing URLs and classify them as phishing or legitimate.

The system analyzes URL characteristics using feature extraction and machine learning algorithms to help users recognize suspicious website links.

🎯 Objectives

- Detect potentially phishing URLs.
- Extract 16 numerical URL features.
- Apply machine learning for URL classification.
- Display predictions through an interactive Streamlit interface.
- Improve awareness of phishing threats.

🚀 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

🤖 Machine Learning Algorithms

1. Logistic Regression
2. Random Forest Classifier

Random Forest was selected as the primary prediction model based on its evaluation results.

📊 Model Performance

Metric| Logistic Regression| Random Forest
Accuracy| 99.6283%| 99.9405%
Phishing Precision| 99.9288%| 99.9134%
Phishing Recall| 99.4803%| 99.9921%
Phishing F1 Score| 99.7040%| 99.9528%

These results are from a random train-test split of the project dataset and do not establish real-world detection performance.

🔍 Features Extracted

The system extracts 16 numerical URL features:

1. URL Length
2. IP Address Detection
3. Dot Count
4. HTTPS Flag
5. URL Entropy
6. Token Count
7. Subdomain Count
8. Query Parameter Count
9. TLD Length
10. Path Length
11. Hyphen in Domain
12. Number of Digits
13. TLD Popularity
14. Suspicious File Extension
15. Domain Name Length
16. Percentage of Numeric Characters

These are project-defined feature calculations and may differ from the original dataset authors' implementation.

📁 Project Structure

```text
PhishGuard-AI/
│
├── data/
│   ├── url_features_extracted1.csv
│   └── cleaned_dataset.csv
│
├── models/
│   ├── logistic_regression.pkl
│   └── random_forest.pkl
│
├── src/
│   ├── url_features.py
│   ├── preprocess.py
│   └── train_model.py
│
├── tests/
│   └── test_url_features.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/Abinaya-127/PhishGuard-AI.git

2. Navigate to the project folder

cd PhishGuard-AI

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

streamlit run app.py

🧪 Testing

Run automated tests using:

python -m unittest discover -s tests -v

🔮 Future Enhancements

- Improve detection using larger and more diverse datasets.
- Evaluate performance on independent, real-world URL datasets.
- Add more advanced URL analysis techniques.
- Develop a more comprehensive cybersecurity dashboard.
- Explore explainable machine learning techniques.

⚠️ Disclaimer

PhishGuard AI is an educational cybersecurity project. Its predictions are not a guarantee that a website is safe or malicious. Always verify website links through trusted security tools.

👩‍💻 Developed By

Abinaya A

B.Tech Information Technology

GitHub: https://github.com/Abinaya-127