import streamlit as st
import joblib
import pandas as pd

from src.url_features import extract_features


# Page configuration
st.set_page_config(
    page_title="PhishGuard AI",
    page_icon="🛡️",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("models/random_forest.pkl")


model = load_model()


# Application title
st.title("🛡️ PhishGuard AI")
st.subheader("Intelligent Phishing URL Detection System")

st.write(
    "Enter a website URL below to check whether it "
    "is potentially phishing or legitimate."
)

st.warning(
    "This tool analyzes URL features only. "
    "It does not visit the website or guarantee safety."
)


# URL input
url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)


# Analyze button
if st.button("🔍 Analyze URL", use_container_width=True):

    if not url.strip():
        st.error("Please enter a URL.")

    else:
        try:
            # Extract URL features
            features = extract_features(url)

            # Prepare features in training order
            input_data = pd.DataFrame([features])

            # Predict URL class
            prediction = int(model.predict(input_data)[0])

            # Display prediction
            if prediction == 0:
                st.error("⚠️ Potential Phishing URL Detected!")

            else:
                st.success("✅ URL Classified as Legitimate")

            # Display confidence
            probabilities = model.predict_proba(input_data)[0]
            class_index = list(model.classes_).index(prediction)
            confidence = probabilities[class_index] * 100

            st.metric(
                label="Prediction Confidence",
                value=f"{confidence:.2f}%"
            )

            # Display extracted features
            with st.expander("View Extracted URL Features"):
                st.dataframe(input_data)

        except (ValueError, TypeError) as error:
            st.error(f"Unable to analyze URL: {error}")

        except Exception as error:
            st.error(f"An unexpected error occurred: {error}")


# Footer
st.divider()

st.caption(
    "PhishGuard AI | Machine Learning Based Cybersecurity Project"
)