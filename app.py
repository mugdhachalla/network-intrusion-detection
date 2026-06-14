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
            letter-spacing: 0.01em;
        }

        p, label, span, div {
            color: inherit;
        }

        .stMarkdown, .stText, .stDataFrame, .stMetric {
            color: #e5eef8;
        }

        div[data-testid="stFileUploader"] {
            background: rgba(9, 20, 33, 0.72);
            border: 1px solid rgba(102, 194, 255, 0.22);
            border-radius: 16px;
            padding: 1rem;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.28);
        }

        div[data-testid="stMetric"] {
            background: linear-gradient(180deg, rgba(16, 33, 50, 0.95), rgba(10, 19, 29, 0.95));
            border: 1px solid rgba(102, 194, 255, 0.18);
            border-radius: 16px;
            padding: 1rem 1.1rem;
            box-shadow: 0 14px 32px rgba(0, 0, 0, 0.25);
        }

        div[data-testid="stMetric"] label,
        div[data-testid="stMetric"] div {
            color: #e5eef8 !important;
        }

        .stButton > button,
        .stDownloadButton > button {
            background: linear-gradient(135deg, #2ab3ff 0%, #3d7eff 100%);
            color: #ffffff;
            border: none;
            border-radius: 999px;
            padding: 0.6rem 1.1rem;
            font-weight: 600;
            box-shadow: 0 10px 24px rgba(61, 126, 255, 0.32);
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            background: linear-gradient(135deg, #47c4ff 0%, #4f8cff 100%);
            color: #ffffff;
            border: none;
        }

        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #2ab3ff 0%, #4fd1c5 100%);
        }

        [data-testid="stDataFrame"] {
            background: rgba(9, 20, 33, 0.72);
            border: 1px solid rgba(102, 194, 255, 0.18);
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 18px 45px rgba(0, 0, 0, 0.28);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Network Intrusion Detection System")

st.write(
    "Upload network traffic data and detect potential attacks using Machine Learning."
)

model = pickle.load(open("model.pkl", "rb"))

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")

    st.dataframe(data.head())

    try:

        predictions = model.predict(data)

        data["Prediction"] = predictions

        attack_count = (predictions == 1).sum()

        normal_count = (predictions == 0).sum()

        total = len(predictions)

        st.subheader("Detection Summary")

        col1, col2, col3 = st.columns(3)

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

        attack_percentage = (
            attack_count / total
        ) * 100

        st.progress(
            attack_percentage / 100
        )

        st.write(
            f"Attack Percentage: {attack_percentage:.2f}%"
        )

        st.subheader("Prediction Results")

        st.dataframe(data)

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