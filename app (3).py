# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pM7tsLb0X5UAPjdq8VgrU5Jl38ocdBti
"""

import pickle
import streamlit as st 


pickle_in = open("BankNote.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication():
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("BankNote Prediction")
    variance = st.text_input("variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()