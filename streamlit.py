import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('Red_Bus.csv')

# Set the title of the app
st.title('Red Bus Service Finder')

# Implement filters
st.sidebar.header('Filter Options')

# Filter by state name
states = data['State_Name'].unique()
selected_state = st.sidebar.selectbox('State', ['All'] + list(states))

# Filter by bus type
bus_types = data['Bus_Type'].unique()
selected_bus_type = st.sidebar.selectbox('Bus Type', ['All'] + list(bus_types))

# Filter by route
routes = data['Route_Name'].unique()
selected_route = st.sidebar.selectbox('Route', ['All'] + list(routes))

# Filter by price range
min_price = data['Price'].min()
max_price = data['Price'].max()
price_range = st.sidebar.slider('Price Range', min_price, max_price, (min_price, max_price))

# Filter by star rating
min_rating = data['Star_Rating'].min()
max_rating = data['Star_Rating'].max()
rating_range = st.sidebar.slider('Star Rating', min_rating, max_rating, (min_rating, max_rating))

# Filter by availability
min_seats = data['Seats_Available'].min()
max_seats = data['Seats_Available'].max()
seats_range = st.sidebar.slider('Seats Available', min_seats, max_seats, (min_seats, max_seats))

# Apply filters
filtered_data = data[
    ((data['State_Name'] == selected_state) | (selected_state == 'All')) &
    ((data['Bus_Type'] == selected_bus_type) | (selected_bus_type == 'All')) &
    ((data['Route_Name'] == selected_route) | (selected_route == 'All')) &
    (data['Price'].between(price_range[0], price_range[1])) &
    (data['Star_Rating'].between(rating_range[0], rating_range[1])) &
    (data['Seats_Available'].between(seats_range[0], seats_range[1]))
]

# Display the filtered data
st.write('### Filtered Bus Services')
st.dataframe(filtered_data)

# Credit at the bottom
st.write('---')
st.write('App created by Vasu Jeyakumar')