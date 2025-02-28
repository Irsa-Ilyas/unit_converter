
import streamlit as st
st.markdown("<h1 style='color:blue;text-align:center'>Code With Irsa 👩‍💻</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:blue; text-align:center; padding:10px;'>🔄 Professional Unit Converter 📏⚖️</h3>", unsafe_allow_html=True)

category = st.selectbox("Enter the Quantity ", ["Length", "Weight", "Temperature", "Volume", "Time"])
value = st.number_input("Enter value:", min_value=0.00, step=0.01)

if category == "Length":
    from_unit = st.selectbox("Convert from", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    to_unit = st.selectbox("Convert to", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    
elif category == "Weight":
    from_unit = st.selectbox("Convert from", ["kilogram", "gram", "milligram", "pound", "ounce"])
    to_unit = st.selectbox("Convert to", ["kilogram", "gram", "milligram", "pound", "ounce"])
    
elif category == "Temperature":
    from_unit = st.selectbox("Convert from", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("Convert to", ["celsius", "fahrenheit", "kelvin"])
    
elif category == "Volume":
    from_unit = st.selectbox("Convert from", ["liter", "milliliter", "cubic meter", "gallon"])
    to_unit = st.selectbox("Convert to", ["liter", "milliliter", "cubic meter", "gallon"])
    
elif category == "Time":
    from_unit = st.selectbox("Convert from", ["second", "minute", "hour", "day", "week", "year"])
    to_unit = st.selectbox("Convert to", ["second", "minute", "hour", "day", "week", "year"])

def length_converter(value, from_unit, to_unit):
    length_units = {"meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000, "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701}
    return (value / length_units[from_unit]) * length_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32

def volume_converter(value, from_unit, to_unit):
    volume_units = {"liter": 1, "milliliter": 1000, "cubic meter": 0.001, "gallon": 0.264172}
    return (value / volume_units[from_unit]) * volume_units[to_unit]

def time_converter(value, from_unit, to_unit):
    time_units = {"second": 1, "minute": 1/60, "hour": 1/3600, "day": 1/86400, "week": 1/604800, "year": 1/31536000}
    return (value / time_units[from_unit]) * time_units[to_unit]

if st.button("Convert"):
    if category == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif category == "Volume":
        result = volume_converter(value, from_unit, to_unit)
    elif category == "Time":
        result = time_converter(value, from_unit, to_unit)
  
    
    st.markdown(f"<h3>Converted Value: {result}</h3>", unsafe_allow_html=True)
st.markdown("<p>Created by <span style='color:blue;font-weight:bolder'>IRSA ILYAS</span></p>", unsafe_allow_html=True)