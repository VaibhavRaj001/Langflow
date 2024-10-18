import streamlit as st
from langflow.load import run_flow_from_json

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {
        color: #f4a261;
        font-family: 'Arial Black', sans-serif;
        text-align: center;
        font-size: 3em;
        margin-bottom: 20px;
    }
    .sub-title {
        color: #2a9d8f;
        font-family: 'Verdana', sans-serif;
        text-align: center;
        font-size: 1.5em;
        margin-bottom: 20px;
    }
    .text-input {
        background-color: #e9c46a;
        border: 2px solid #264653;
        color: #264653;
        font-size: 1.2em;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .response-box {
        background-color: #f4a261;
        color: white;
        font-size: 1.2em;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .submit-button {
        background-color: #2a9d8f;
        border: none;
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
    }
    .submit-button:hover {
        background-color: #264653;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit interface
st.markdown("<h1 class='main-title'>Rookus Bot</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Ask your question to the Rookus Bot below:</p>", unsafe_allow_html=True)

# Create an input text box with custom style
question = st.text_input("Enter your Question:", key="input", help="Type your question here.", max_chars=200)

# Run the flow when the user submits a question
if st.button("Get Response", key="submit-button", help="Click to get a response from the Rookus Bot"):
    try:
        result = run_flow_from_json(flow="Chatbot.json", input_value=question)
        
        # Access and display the message text
        if result and result[0].outputs:
            message_text = result[0].outputs[0].results['message'].text
            st.markdown(f"<div class='response-box'>Rookus Bot: {message_text}</div>", unsafe_allow_html=True)
        else:
            st.write("No valid output from the flow.")
        
    except FileNotFoundError:
        st.write("The JSON file 'Rookus.in.json' was not found. Please check the path.")
    except Exception as e:
        st.write(f"An error occurred: {e}")

