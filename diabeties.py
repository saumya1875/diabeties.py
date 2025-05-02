import streamlit as st
import joblib

# Load the trained model
model = joblib.load("diabetes.pkl")

def main():
    st.title("Welcome to the Diabetes Predictor")
    
    # Take input from the user
    
    glucose = st.number_input("Choose your Glucose level", min_value=0.0, max_value=200.0, step=1.0)
    bloodpressure = st.number_input("Choose your  bloodpressure  level", min_value=30.0, max_value=120.0, step=80.0)
    insulin = st.number_input("Choose your insulin level", min_value=0.0, max_value=900.0, step=80.0)
    age= st.number_input("Choose your age ", min_value=1, max_value=100, step=30)
    

    if  st.button("Prediction") :
        input_data = [[ glucose, bloodpressure, insulin,   age]]
        
        prediction = model.predict(input_data)
            
        if prediction[0] == 1:
            st.error("The model predicts: Diabetic")
        else:
            st.success("The model predicts: Not Diabetic")
if __name__ == "__main__":
    main()