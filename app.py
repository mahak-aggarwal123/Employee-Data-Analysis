
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page settings
st.set_page_config(
    page_title="Employee Data Analysis",
    page_icon="👩‍💼",
    layout="wide"
)

# Load employee data
df = pd.read_csv("employee_data.csv")

# Heading
st.title("👩‍💼 Employee Data Analysis")
st.write("Employee information and salary analysis")

st.divider()

# Summary boxes
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", len(df))
col2.metric("Average Salary", f"₹{df['Salary'].mean():,.0f}")
col3.metric("Highest Salary", f"₹{df['Salary'].max():,}")
col4.metric("Departments", df["Department"].nunique())

st.divider()

# Department chart
st.subheader("Department-wise Employees")

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.countplot(data=df, x="Department", ax=ax1)
ax1.set_xlabel("Department")
ax1.set_ylabel("Number of Employees")
plt.xticks(rotation=20)
st.pyplot(fig1)
plt.close(fig1)

# Salary chart
st.subheader("Employee Salary Comparison")

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(data=df, x="Name", y="Salary", ax=ax2)
ax2.set_xlabel("Employee Name")
ax2.set_ylabel("Salary (₹)")
plt.xticks(rotation=90)
st.pyplot(fig2)
plt.close(fig2)

st.divider()

# Employee details
st.subheader("Employee Details")
st.dataframe(df, use_container_width=True)

st.success("Employee Data Analysis Completed!")
