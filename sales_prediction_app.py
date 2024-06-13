import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import os
import pickle

def load_components_function(fp):
    with open(fp,"rb") as f:
        object = pickle.load(f)
    return object

DIRPATH = os.path.dirname(os.path.realpath(__file__))
ml_core_fp = os.path.join(DIRPATH,"Assets","Seizure_Pred_model.pk1")
ml_components_dict = load_components_function(fp=ml_core_fp)


# Streamlit App
st.set_page_config(layout="centered")
st.title("Sales Forecast App for Corporation Favorita") 
st.write("""Welcome to Corporation Favorita Sales Prediction app! This app allows you to predict the Sales for a specific product in a chosen store at Corporation Favorita""")
#Image
st.image("https://images.app.goo.gl/4P89DDQNF eKmpN406")
with st.form(key="information", clear_on_submit=True):
    st.date_input("Date")
    Promotion = st.selectbox("On promotion, for No and 1 for Yes", [0, 1])
    transactions = st.number_input("Enter the number of transactions for the product")
    dcoilwtico = st.number_input("Enter the oil price (dcoilwtico)")

    products = st.selectbox('products', ['AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'BREAD/BAKERY', 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS',
    'FROZEN FOODS', 'GROCERY I', 'GROCERY II', 'HARDWARE','HOME AND KITCHEN I', 'HOME AND KITCHEN II', 'HOME APPLIANCES', 'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE', 'LIQUOR, WINE, BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE', 'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY', 'PREPARED FOODS', 'PRODUCE', 'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD'])
    state = st.selectbox('state', ['Santa Elena', 'El Oro', 'Guayas']) 
    city = st.selectbox('city', ['Salinas', 'Machala', 'Libertad']) 
    weeklysales = st.number_input("weekly Sales,0-Sun and 6-Sat", step=1)