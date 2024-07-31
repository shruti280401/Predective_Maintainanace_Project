import streamlit as st
import pandas as pd
import joblib

# Load your model
model = joblib.load('predective_model.pkl')

# Custom CSS for button
st.markdown("""
    <style>
    .stButton > button {
        background-color: #007bff; /* Blue color */
        color: white; /* Text color */
        border: none; /* Remove border */
        padding: 10px 20px; /* Add padding */
        border-radius: 5px; /* Round corners */
        font-size: 16px; /* Font size */
        cursor: pointer; /* Pointer cursor on hover */
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    </style>
""", unsafe_allow_html=True)


# Define the Streamlit app
def main():
    st.title("Predictive Maintainence")

    # Define the input fields

    GGN = st.number_input('Gas Generator rate of revolutions (GGn) [rpm]', min_value=0.000, step=0.01)
    T48 = st.number_input('HP Turbine exit temperature (T48) [C]', min_value=0.0, step=0.1)
    PEXH = st.number_input('Gas Turbine exhaust gas pressure (Pexh) [bar]', min_value=1.0, step=0.1)

    # Create a button to make predictions
    if st.button('Predict'):
        
        # Create a DataFrame for the input
        input_data = pd.DataFrame({
            'GGN': [GGN],
            'T48': [T48],
            'PEXH': [PEXH]
        })

        # Convert categorical data to dummy/indicator variables if needed
        # input_data = pd.get_dummies(input_data)

        # Make predictions
        prediction = model.predict(input_data)

        # Display the prediction

        if prediction[0]<0.987:
            
            st.write('<p style="color:green; font-weight:bold;">The component is safe for now</p>', unsafe_allow_html=True)

        elif prediction[0]>=0.987:

            st.write('<p style="color:red; font-weight:bold;">The component is at RISK!!!</p>', unsafe_allow_html=True)

            

# Run the app
if __name__ == '__main__':
    main()