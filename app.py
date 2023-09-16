import streamlit as st
import pandas as pd

# Create a Streamlit app
st.title("File Upload and Questions")

# Create the File Upload Zone
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])

# Process the Uploaded File
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # You can adjust this for other file types
    st.write("Uploaded Data:")
    st.dataframe(df)

# Create Collapsible Widget for Questions
with st.expander("Ask a question"):
    user_question = st.text_area("Type your question here")
    if st.button("Submit"):
        # Process and answer the question here
        st.write(f"Question: {user_question}")
        # Add code to answer the question based on the uploaded file

# Run the Streamlit app
if __name__ == "__main__":
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.set_option('deprecation.showPyplotGlobalUse', False)

