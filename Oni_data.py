import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


def Oni_data():
    GloFood=pd.read_csv("C:/Users/USER/Documents/data analysis/python/Data_Apps/global_food_prices.csv")
    GloFood.rename(columns={
                     GloFood.columns[0]:'Country_id',
                     GloFood.columns[1]:'Country_name',
                     GloFood.columns[2]:'Locality_id',
                     GloFood.columns[3]:'Locality_name',
                     GloFood.columns[4]:'Market_id',
                     GloFood.columns[5]:'Market_name',
                     GloFood.columns[6]:'Commodity_Purchase_id',
                     GloFood.columns[7]:'Commodity_Purchased',
                     GloFood.columns[8]:'currency_id',
                     GloFood.columns[9]:'Currency_name',
                     GloFood.columns[10]:'Market_type_id',
                     GloFood.columns[11]:'Market_type',
                     GloFood.columns[12]:'Measurement_id',
                     GloFood.columns[13]:'Unit_measurement',
                     GloFood.columns[14]:'Month',
                     GloFood.columns[15]:'Year',
                     GloFood.columns[16]:'Price',
                     GloFood.columns[17]:'Commodity_source',
}, inplace=True)
    # dropping empty column
    GloFood.drop(['Commodity_source'], axis=1)
    
    # remove the duplicate names on the lists
    items=[]
    for item_name in list(GloFood.Commodity_Purchased.str.split('-')):
        items.append(item_name[0])
    GloFood.Commodity_Purchased=items
    return GloFood


GloFood = Oni_data()
st.title("Global Food Prices GEORGE O ONI REPORT")
st.write(GloFood.head(50))
# view specific country selected by user
grp_country = GloFood.groupby('Country_name')
# side bar 
with st.sidebar:
    st.subheader('pick a country to view more details')
    selected_country =st.selectbox('select a country',list(GloFood.Country_name.unique()))
selected_country_details =grp_country.get_group(selected_country)
st.subheader(selected_country)
st.write(selected_country_details[['Country_name', 'Commodity_Purchased', 'Year', 'Price']].head(10))
if selected_country:
    #
    with st.sidebar:
        st.subheader('Pick a Commodity')
    comm=st.multiselect('select Commodity_Purchased', list(GloFood.Commodity_Purchased.unique()))
    used_selected_comm= selected_country_details['Commodity_Purchased'].str.split(';')
    temp=st.write(used_selected_comm)
    
    with st.sidebar:
        st.subheader('pick a Year')
        year=st.multiselect('select Year', list(GloFood.Year.unique()))
    used_selected_year= selected_country_details['Year']
    temp=st.write(used_selected_year)
    
    with st.sidebar:
        st.subheader('pick a Price')
        price=st.multiselect('select Price', list(GloFood.Price.unique()))
    used_selected_price= selected_country_details['Price']
    temp=st.write(used_selected_price) 
    
else:
    pass
# pie chart, top 10 countries
pie_data= GloFood['Country_name'].value_counts().head(10)
fig1, ax1 = plt.subplots(figsize=(10,8))
ax1.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
# display the figure and pie chart 
st.pyplot(fig1)
st.write(
"""### Number of Commodity Purchased from top 10 Countries"""
)

# bar chart
st. write(
    """## Mean Price of Commodities By Country"""
)
bar_data = GloFood.groupby(['Country_name'])['Price'].mean().sort_values(ascending=True).head(10)
st.bar_chart(bar_data)
    
    
    