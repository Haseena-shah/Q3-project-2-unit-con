import streamlit as st

st.title("🔁 Unit Converter App")
st.markdown("#### Convert any unit to another unit")
st.write("welcome! select the unit you want to convert")

category = st.selectbox("Select the category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometters to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value  / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value / 2.54
        elif unit == "Inches to Centimeters":
            return value * 2.54
        elif unit == "Feet to Inches":
            return value * 12
        elif unit == "Inches to Feet":
            return value / 12
        
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
        
        
    elif category == "Time":
        if unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("Select the unit", ["Kilometters to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", "Centimeters to Inches", "Inches to Centimeters", "Feet to Inches", "Inches to Feet"])
   
elif category == "Weight":
    unit = st.selectbox("Select the unit", ["Kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Time":
    unit = st.selectbox("Select the unit", ["Hours to Minutes", "Minutes to Hours", "Minutes to Seconds", "Seconds to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")