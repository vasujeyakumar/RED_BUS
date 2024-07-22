import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('Red_Bus.csv')

# App Title
st.title('Red Bus Ticket Booking')

# Search Form
st.sidebar.header('Bus Search')
from_location = st.sidebar.selectbox('From', options=data['Route_Name'].apply(lambda x: x.split(' to ')[0]).unique())
to_location = st.sidebar.selectbox('To', options=data['Route_Name'].apply(lambda x: x.split(' to ')[1]).unique())
travel_date = st.sidebar.date_input('Travel Date')
passengers = st.sidebar.number_input('Passengers', min_value=1, max_value=10, step=1)

# Filter data based on search
filtered_data = data[(data['Route_Name'].str.contains(from_location)) & 
                     (data['Route_Name'].str.contains(to_location))]

# Display Filtered Buses
st.subheader(f'Available Buses from {from_location} to {to_location} on {travel_date}')
for idx, row in filtered_data.iterrows():
    with st.expander(f"{row['Bus_Name']} - {row['Bus_Type']}"):
        st.write(f"**Departure**: {row['Departing_Time']}")
        st.write(f"**Duration**: {row['Duration']}")
        st.write(f"**Price**: ₹{row['Price']}")
        st.write(f"**Seats Available**: {row['Seats_Available']}")
        st.write(f"**Star Rating**: {row['Star_Rating']}")
        if st.button('Book Now', key=f"book_{idx}"):
            st.session_state['booking_info'] = {
                'bus_name': row['Bus_Name'],
                'bus_type': row['Bus_Type'],
                'departure': row['Departing_Time'],
                'duration': row['Duration'],
                'price': row['Price'],
                'seats': row['Seats_Available'],
                'route': row['Route_Link'],
                'from': from_location,
                'to': to_location,
                'date': travel_date,
                'passengers': passengers
            }
            st.experimental_rerun()

# Booking Details
if 'booking_info' in st.session_state:
    st.subheader('Booking Details')
    booking_info = st.session_state['booking_info']
    st.write(f"**Bus Name**: {booking_info['bus_name']}")
    st.write(f"**Bus Type**: {booking_info['bus_type']}")
    st.write(f"**From**: {booking_info['from']}")
    st.write(f"**To**: {booking_info['to']}")
    st.write(f"**Date**: {booking_info['date']}")
    st.write(f"**Departure**: {booking_info['departure']}")
    st.write(f"**Duration**: {booking_info['duration']}")
    st.write(f"**Price**: ₹{booking_info['price']}")
    st.write(f"**Passengers**: {booking_info['passengers']}")
    st.write(f"**Seats Available**: {booking_info['seats']}")
    st.write(f"**Route Link**: [Book Here]({booking_info['route']})")

# Summary Statistics
st.sidebar.header('Summary Statistics')
st.sidebar.write(f"Average Price: ₹{filtered_data['Price'].mean():.2f}")
st.sidebar.write(f"Average Star Rating: {filtered_data['Star_Rating'].mean():.2f}")

# Contact Form
st.sidebar.subheader('Contact Us')
with st.sidebar.form(key='contact_form'):
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success('Thank you for your message!')

# Footer
st.markdown('---')
st.markdown('Created by Vasu Jeyakumar')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
    }
    .css-1d391kg {
        background-color: #ffffff;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        border: none;
    }
    .st-expander {
        border: 1px solid #4CAF50;
        border-radius: 5px;
    }
    </style>
    """,\
    unsafe_allow_html=True
)
