import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("mumbai house dataset.csv")

# Page title
st.title("📊 Mumbai Real Estate Dashboard")

st.write("Here are some insights from the Mumbai housing dataset:")

# Price distribution
st.subheader("Flat Price Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(data['flat_price'], bins=30, kde=True, ax=ax1, color='skyblue')
ax1.set_xlabel("Price (Crores)")
ax1.set_ylabel("Number of Flats")
st.pyplot(fig1)

# Location vs Average Price
st.subheader("Average Price by Location")
top_locations = data.groupby('location1')['flat_price'].mean().sort_values(ascending=False).head(15)
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.barplot(x=top_locations.values, y=top_locations.index, palette='coolwarm', ax=ax2)
ax2.set_xlabel("Average Price (Crores)")
st.pyplot(fig2)

# Area vs Price
st.subheader("Built-up Area vs Flat Price")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='buildupArea_sqft', y='flat_price', data=data, color='purple', ax=ax3)
ax3.set_xlabel("Built-up Area (sqft)")
ax3.set_ylabel("Price (Crores)")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.caption("Data Source: housing.com (scraped dataset)")
