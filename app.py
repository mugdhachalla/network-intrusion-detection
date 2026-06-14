import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Network Intrusion Detection System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle at top, #17324d 0%, #0c1724 45%, #08111a 100%);
            color: #e5eef8;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            color: #e5eef8;
        }

        [data-testid="stSidebar"],
        [data-testid="collapsedControl"] {
            display: none;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #f5fbff;
        }

        div[data-testid="stFileUploader"] {
            background: rgba(9, 20, 33, 0.72);
            border: 1px solid rgba(102, 194, 255, 0.22);
            border-radius: 16px;
            padding: 1rem;
        }

        div[data-testid="stMetric"] {
            background: linear-gradient(
                180deg,
                rgba(16, 33, 50, 0.95),
                rgba(10, 19, 29, 0.95)
            );
            border: 1px solid rgba(102, 194, 255, 0.18);
            border-radius: 16px;
            padding: 1rem;
        }

        .stButton > button,
        .stDownloadButton > button {
            background: linear-gradient(
                135deg,
                #2ab3ff 0%,
                #3d7eff 100%
            );
            color: white;
            border: none;
            border-radius: 999px;
            font-weight: 600;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🛡️ Network Intrusion Detection System")

st.markdown(
    """
    Detect malicious network activity using Machine Learning.

    **Dataset:** NSL KDD  
    **Primary Model:** Random Forest Classifier  
    **Additional Experiment:** Autoencoder Based Anomaly Detection
    """
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("columns.pkl", "rb") as f:
    columns = pickle.load(f)

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        data = pd.read_csv(uploaded_file)

        if "Prediction" in data.columns:
            data = data.drop(
                columns=["Prediction"]
            )

        missing_cols = set(columns) - set(data.columns)

        if missing_cols:

            st.error(
                f"Missing columns: {list(missing_cols)}"
            )

            st.stop()

        extra_cols = set(data.columns) - set(columns)

        if extra_cols:

            st.warning(
                f"Ignoring extra columns: {list(extra_cols)}"
            )

        data = data[columns]

        st.subheader("Uploaded Data")

        st.dataframe(
            data.head()
        )

        predictions = model.predict(data)

        data["Prediction"] = predictions

        attack_count = (
            predictions == 1
        ).sum()

        normal_count = (
            predictions == 0
        ).sum()

        total = len(predictions)

        attack_percentage = (
            attack_count / total
        ) * 100

        risk_level = (
            "🔴 High Risk"
            if attack_percentage > 50
            else "🟡 Medium Risk"
            if attack_percentage > 20
            else "🟢 Low Risk"
        )

        st.subheader(
            "Detection Summary"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Connections",
                total
            )

        with col2:
            st.metric(
                "Attack Connections",
                attack_count
            )

        with col3:
            st.metric(
                "Normal Connections",
                normal_count
            )

        with col4:
            st.metric(
                "Network Risk",
                risk_level
            )

        st.progress(
            attack_percentage / 100
        )

        st.write(
            f"Attack Percentage: {attack_percentage:.2f}%"
        )

        st.markdown("---")

        st.subheader(
            "Model Insights"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                """
                **Random Forest Classifier**

                • Accuracy: 77.3%

                • 120+ engineered features

                • Supervised intrusion detection

                • Best performing model
                """
            )

        with col2:

            st.info(
                """
                **Autoencoder Anomaly Detection**

                • Trained on normal traffic only

                • Normal Error: 0.0028

                • Attack Error: 0.0337

                • ~12× higher anomaly score for attacks
                """
            )

        try:

            importance = pd.read_csv(
                "feature_importance.csv"
            )

            st.subheader(
                "Top Attack Indicators"
            )

            top_features = (
                importance
                .head(10)
            )

            st.bar_chart(
                top_features.set_index(
                    "Feature"
                )["Importance"]
            )

        except:

            st.warning(
                "feature_importance.csv not found."
            )

        st.subheader(
            "Prediction Results"
        )

        st.dataframe(
            data
        )

        csv = data.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "Download Results",
            csv,
            "intrusion_results.csv",
            "text/csv"
        )

    except Exception as e:

        st.error(
            f"Error processing file: {e}"
        )