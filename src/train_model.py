import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)

# Load dataset
df = pd.read_csv("data/cleaned_dataset.csv")

# Select features
FEATURES = [
    "url_length",
    "has_ip_address",
    "dot_count",
    "https_flag",
    "url_entropy",
    "token_count",
    "subdomain_count",
    "query_param_count",
    "tld_length",
    "path_length",
    "has_hyphen_in_domain",
    "number_of_digits",
    "tld_popularity",
    "suspicious_file_extension",
    "domain_name_length",
    "percentage_numeric_chars"
]

X = df[FEATURES]
y = df["ClassLabel"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create machine-learning models
models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),

    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    )
}

# Create models folder if needed
Path("models").mkdir(exist_ok=True)

# Train and evaluate models
for name, model in models.items():

    print("\n" + "=" * 45)
    print("Training:", name)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    print("\nAccuracy:", accuracy_score(y_test, predictions))
    print("Phishing Precision:", precision_score(y_test, predictions, pos_label=0))
    print("Phishing Recall:", recall_score(y_test, predictions, pos_label=0))
    print("Phishing F1 Score:", f1_score(y_test, predictions, pos_label=0))
    print("ROC-AUC:", roc_auc_score(y_test, probabilities))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    filename = name.lower().replace(" ", "_")
    joblib.dump(model, f"models/{filename}.pkl")

    print("Model saved:", f"models/{filename}.pkl")

print("\nBoth models trained successfully!")