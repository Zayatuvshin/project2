import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("export2.csv")
df_c = pd.read_csv("export_countries.csv")

if df['Year'].dtype == 'object': 
    df['Year'] = df['Year'].str.replace(',', '', regex=False) 

if df_c['Year'].dtype == 'object': 
    df_c['Year'] = df_c['Year'].str.replace(',', '', regex=False) 
    
df_c['Year'] = df_c['Year'].astype(int)

st.title('Mongolian Export Data Analysis')


st.write("""
This app visualizes the export data for different goods categories over the years.
""")


total_exports = df.groupby('Goods Category')['Value(USD)'].sum().sort_values(ascending=False)
st.write("Top Export Categories by Total Export Value(USD):")
st.bar_chart(total_exports)
st.write("""
As shown in the bar chart, "mineral products" is the most exported category overall. This category typically includes materials extracted from the earth, such as 
ores (e.g., iron ore, copper ore),
mineral fuels (e.g., coal, oil, natural gas),
industrial minerals (e.g., limestone, gypsum),
processed products (e.g., metals and refined fuels).
""")

st.write("""
You can select a goods category from the dropdown below to see the export values trend.
""")
# Dropdown menu 
goods_categories = df["Goods Category"].unique()  
selected_category = st.selectbox("Select Goods Category", goods_categories)

# Filter the data 
filtered_data = df[df["Goods Category"] == selected_category]

# Displaying the filtered data
st.write(f"Export Data for: {selected_category}")
st.write(filtered_data)

# Line chart to visualize the trend of export values over the years
st.subheader(f"Export Value Trend for {selected_category}")
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data, x="Year", y="Value(USD)", marker='o')
plt.title(f"Export Value(USD) Trend for {selected_category}", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Value(USD0")
plt.xticks(rotation=45)
plt.tight_layout()
plt.xticks(ticks=filtered_data['Year'].unique(), labels=filtered_data['Year'].unique(), rotation=45)
st.pyplot(plt)




# Top Exported Continents bt Total Export Value(USD)
total_export = df_c.groupby('Continent')['Export Value'].sum().sort_values(ascending=False)
st.write("Total Export Value by Continent (2005-2023):")
st.bar_chart(total_export)
st.write("""
The barchart shows that Mongolia mostly exports to other Asian countries. And secondly European countries
""")

 # Dropdown menu for selecting the continent
continents = df_c["Continent"].unique()  
selected_continent = st.selectbox("Select Continent", continents)

# Filter the data for the selected continent
filtered_data1 = df_c[df_c["Continent"] == selected_continent]

# Display the filtered data
st.write(f"Export Data for: {selected_continent}")
st.write(filtered_data1)

# Line chart to visualize the trend of export values over the years
st.subheader(f"Export Value Trend for {selected_continent}")
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_data1, x="Year", y="Export Value", marker='o')
plt.title(f"Export Value Trend for {selected_continent}", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Export Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.xticks(ticks=filtered_data1['Year'].unique(), labels=filtered_data1['Year'].unique(), rotation=45)
# Display the plot in Streamlit
st.pyplot(plt)

st.subheader(f"Exports to each continent year by year")
plt.title(f"Exports to each continent year by year")
pivot_data = df_c.pivot_table(index="Year", columns="Continent", values="Export Value", aggfunc="sum")
sns.heatmap(pivot_data, annot=True, cmap="YlGnBu", fmt=",.0f")
st.pyplot(plt)
st.write("""
While export to Asian countries went up last few years, export to American countries and Australian countries went doen moderately
""")




st.write("""
Mongolia is heavily reliant on its mining sector, which makes up a significant portion of its exports. Key minerals include coal, copper, gold, fluorspar, and uranium. Coal is the largest export commodity, particularly to China, which is Mongolia's largest trading partner. The Tavan Tolgoi coal mine is one of the largest and most famous coal reserves in Mongolia. China is by far Mongolia's largest export destination, receiving around 90% of its exports. The relationship between Mongolia and China is primarily focused on mineral trade.
""")