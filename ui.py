import streamlit as st
from streamlit_js_eval import get_geolocation
with st.sidebar:
    st.subheader("Credit Card Fraud Detector")

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

data = df
st.write(data)
# print(df)
# st.write(df)
# st.table(df)

st.map(df)

st.write(get_geolocation())