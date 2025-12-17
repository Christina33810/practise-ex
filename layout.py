import streamlit as st

st.title("Business Performance Dashboard")
st.write("Objective: Provide insights into revenue, customer feedback, and market trends.")

col2, col2, col3, col4 = st.columns(4)
with col1:
  st.header("Q1 2024")
  st.write("Revenue: $1.2M")
with col2:
  st.header("Q2 2024")
  st.write("Revenue: $1.5M")
with col3:
  st.header("Q3 2024")
  st.write("Revenue: $1.3M")
with col4:
  st.header("Q4 2024")
  st.write("Revenue: $1.6M")

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])

with st.expander("More Information"):
    st.write("Data collected via surveys and reports.")

placeholder = st.empty()

for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1)

placeholder.write("Data loading complete.")
  
selected_quarter = st.selectbox("Select a quarter:", ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"])
growth = st.slider("Adjust growth percentage:", 0, 50, 10)

st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]})
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
