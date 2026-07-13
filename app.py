import streamlit as st


st.set_page_config(
    page_title="DataForge AI",
    page_icon="⚒️",
    layout="wide",
)


st.title("⚒️ DataForge AI")
st.subheader("Transform raw documents into high-quality datasets for LLMs.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload a source document",
    type=["pdf", "txt", "md"],
)

dataset_type = st.selectbox(
    "Choose a dataset format",
    options=[
        "Question Answering (QA)",
        "Supervised Fine-Tuning (SFT)",
        "Study Notes",
    ],
)

number_of_samples = st.slider(
    "Number of samples",
    min_value=5,
    max_value=50,
    value=10,
    step=5,
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

generate_button = st.button(
    "Generate Dataset",
    type="primary",
)

if generate_button:
    if uploaded_file is None:
        st.warning("Please upload a document first.")
    else:
        st.info(
            f"Preparing to generate {number_of_samples} "
            f"{dataset_type} samples from {uploaded_file.name}."
        )
        st.warning("Dataset generation will be implemented in the next stage.")