import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Function to fetch data from a public Google Sheet
def fetch_sales_data():
    try:
        # Correct URL for the CSV export of the sheet
        sheet_url = "https://docs.google.com/spreadsheets/d/13A0RVgb7uRW93RXEWN7RSH5i97jShgHnYB4zmvcThpk/gviz/tq?tqx=out:csv&gid=1502421750"
        
        # Read data into a DataFrame
        df = pd.read_csv(sheet_url)

        # Columns to clean (monetary values)
        monetary_cols = ['sept24_rev_gen', 'oct24_rev_gen', 'nov24_rev_gen', 
                         'sept24_target', 'oct24_target', 'nov24_target']
        
        # Clean monetary columns: remove $, replace empty with 0, and convert to float
        for col in monetary_cols:
            if col in df.columns:  # Ensure the column exists
                df[col] = (
                    df[col]
                    .fillna("0")  # Replace missing values with "0"
                    .replace('[\$,]', '', regex=True)  # Remove $ and commas
                    .replace('', '0')  # Handle remaining empty strings
                )
                try:
                    df[col] = df[col].astype(float)  # Convert to float
                except ValueError:
                    st.error(f"Unable to convert column {col} to float. Check for invalid data.")
            else:
                st.warning(f"Column '{col}' is missing in the dataset.")
        
        # Columns for inquiries (replace NaNs with 0)
        inquiry_cols = ['sept24_inq_no', 'oct24_inq_no', 'nov24_inq_no']
        for col in inquiry_cols:
            if col in df.columns:
                df[col] = df[col].fillna(0).astype(int)
            else:
                st.warning(f"Column '{col}' is missing in the dataset.")

        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Mock user database with unique usernames and passwords
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "thomas": {"password": "thomas123", "role": "user"},
    "max": {"password": "max123", "role": "user"},
    "kelvin": {"password": "kelvin123", "role": "user"},
    "soumya": {"password": "soumya123", "role": "user"},
    "rishika": {"password": "rishika123", "role": "user"},
    "akon": {"password": "akon123", "role": "user"},
    "andrew": {"password": "andrew123", "role": "user"},
    "eddy": {"password": "eddy123", "role": "user"},
    "june": {"password": "june123", "role": "user"},
    "rony": {"password": "rony123", "role": "user"},
    "daisy": {"password": "daisy123", "role": "user"},
    "priyanka": {"password": "priyanka123", "role": "user"},
    "annie": {"password": "annie123", "role": "user"},
    "eric": {"password": "eric123", "role": "user"},
    "karisma": {"password": "karisma123", "role": "user"},
    "preetam": {"password": "preetam123", "role": "user"},
    "edward": {"password": "edward123", "role": "user"},
    "summit": {"password": "summit123", "role": "user"}
}

# Authentication function
def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None

# Main app function
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.role = ""

    if not st.session_state.logged_in:
        show_login_page()
    else:
        if st.session_state.role == "admin":
            admin_page()
        else:
            user_page()

# Login page
def show_login_page():
    st.title("Login Page")
    st.subheader("Please log in to access your dashboard")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    login_button = st.button("Login")

    if login_button:
        role = authenticate(username, password)
        if role:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.rerun()  # Refresh the app to load the appropriate dashboard
        else:
            st.error("Invalid username or password.")

# Admin dashboard
def admin_page():
    st.header("Admin Dashboard")
    st.write(f"Welcome, {st.session_state.username}!")
    st.write("This is the admin panel where you can manage users and view stats.")
    
    # Add admin functionalities here
    if st.button("Logout"):
        logout()

# User dashboard
def user_page():
    st.header("User Dashboard")
    st.write(f"Welcome, {st.session_state.username}!")
    st.write("This is your personalized user dashboard.")

    # Fetch and display data
    df = fetch_sales_data()
    if not df.empty:
        st.dataframe(df)

        # Revenue vs. Target bar chart
        fig = go.Figure(data=[ 
            go.Bar(name='September Revenue', x=df['agent_name'], y=df['sept24_rev_gen'], marker_color='blue'),
            go.Bar(name='September Target', x=df['agent_name'], y=df['sept24_target'], marker_color='lightblue'),
            go.Bar(name='October Revenue', x=df['agent_name'], y=df['oct24_rev_gen'], marker_color='red'),
            go.Bar(name='October Target', x=df['agent_name'], y=df['oct24_target'], marker_color='pink'),
            go.Bar(name='November Revenue', x=df['agent_name'], y=df['nov24_rev_gen'], marker_color='green'),
            go.Bar(name='November Target', x=df['agent_name'], y=df['nov24_target'], marker_color='lightgreen')
        ])
        fig.update_layout(barmode='group', title="Revenue vs. Target Comparison by Month")
        st.plotly_chart(fig, use_container_width=True)

        # Inquiry count bar chart
        inquiry_fig = go.Figure(data=[
            go.Bar(name='September Inquiries', x=df['agent_name'], y=df['sept24_inq_no'], marker_color='purple'),
            go.Bar(name='October Inquiries', x=df['agent_name'], y=df['oct24_inq_no'], marker_color='orange'),
            go.Bar(name='November Inquiries', x=df['agent_name'], y=df['nov24_inq_no'], marker_color='cyan')
        ])
        inquiry_fig.update_layout(barmode='group', title="Inquiries Count Comparison by Month")
        st.plotly_chart(inquiry_fig, use_container_width=True)

    if st.button("Logout"):
        logout()

# Logout function
def logout():
    # Reset session state variables
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.rerun()  # Refresh the app to return to the login page

if __name__ == "__main__":
    main()
