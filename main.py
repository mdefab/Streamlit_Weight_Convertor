import streamlit as st
from weight_conversions import data_conversion_dict


def conversion_calculator():
    try:
        conversion_value = data_conversion_dict[st.session_state.convert_from][st.session_state.convert_to]
        return st.session_state.amount * conversion_value
    except:
        return "Error converting"


st.title("Weight Convertor: ")
if 'convert_from' not in st.session_state:
    st.session_state.convert_from = "lbs"

if 'convert_to' not in st.session_state:
    st.session_state.convert_to = "kg"

if 'amount' not in st.session_state:
    st.session_state.amount = 0


st.selectbox("Pick a unit to convert from: ", list(data_conversion_dict), key='convert_from')
st.selectbox("Pick a unit to convert to: ", list(data_conversion_dict[st.session_state.convert_from]), key='convert_to')
with st.form(key="my_form"): 
    st.number_input(f"How many {st.session_state.convert_from}?", min_value=0.0, max_value=10000000.0, step=0.01, key='amount')
    submit = st.form_submit_button(label="submit")

if submit:
    result = conversion_calculator()
    st.write(f"Result: {st.session_state.amount} {st.session_state.convert_from} is {round(result, 4)}{st.session_state.convert_to}")

