import streamlit as st


data_conversion_dict = {
    'lbs': {'kg': 0.4536, 'g': 453.592, 'oz': 16, 'Stone': 0.07143},
    'kg': {'lbs': 2.2046, 'oz': 35.274, 'g': 1000, 'Stone': 0.1575},
    'g': {'oz': 0.035, 'kg': 0.001, 'lbs': 0.0022, 'Stone': 0.0001575},
    'oz': {'lbs': 0.0625, 'kg': 0.02835, 'g': 28.3495, 'Stone': 0.0044643},
    'Stone': {'lbs': 14, 'kg': 6.3503, 'oz': 224, 'g': 6350.29}
}


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

