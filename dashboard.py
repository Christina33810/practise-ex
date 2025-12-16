import streamlit as st

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region")

monthly_sales = st.number_input("Enter Monthly Sales Target (in USD):", value=0.00)

region = st.selectbox("Select region:",["North", "South", "East", "West"])

if st.button("Submit"):
  st.success("Dashboard updated successfully!")
  st.write(f"The {region} monthly sales target is {monthly_sales} in USD.")

  if monthly_sales > 1000000:
    st.write("Great! You have set an ambitious target!")
                                
