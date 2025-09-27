import streamlit as st
import sqlite3
import pandas as pd
import streamlit.components.v1 as components

# =================== CONFIG ===================
st.set_page_config(
    page_title="OLA Ride",
    layout="wide",
)

# =================== CUSTOM CSS ===================
st.markdown(
    """
    <style>
    * { font-family: "Times New Roman", Times, serif !important; }
    .stApp { background-color: #f3fce4; }

    /* Add vertical gap after headings */
    h1 { margin-bottom: 5px !important; }
    h2 { margin-bottom: 5px !important; }
    h3 { margin-bottom: 5px !important; }
    h4 { margin-bottom: 5px !important; }

    .stTabs [data-baseweb="tab-list"] { gap: 20px; justify-content: center; }
    .stTabs [data-baseweb="tab"] {
        background-color: #dce5cd;
        color: black !important;
        border-radius: 10px 10px 0 0;
        padding: 15px 25px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover { background-color: #a7b88c; color: black !important; }
    .stTabs [aria-selected="true"] { background-color: #cadaaf !important; color: black !important; font-weight: 900 !important; font-size: 20px !important; }

    .welcome-box {
        background-color: #d2e1ba;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        font-size: 23px;
        color: #2e4600;
        margin-bottom: 90px;
        line-height: 1;
    }

    .card-row { 
    display: flex; 
    justify-content: center;    /* center the cards */
    gap: 20px;                  /* small gap between cards */
    flex-wrap: wrap;            /* wrap on small screens */
    margin-bottom: 30px; 
    }

    .card {
        flex: 1;
        max-width: 250px;           /* card size limit */
        background-color: #fafcfb;
        padding: 8px;
        border-radius: 15px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
        text-align: center;
        margin-bottom: 30px;
    }

    .card h2, .card h3, .card h4 {
        margin: 0 !important;
        padding: 0 !important;
        color: #2e4600;
        display: flex; 
        justify-content: center;
        gap: 6px; 
        font-size: 25px;
        text-align: center;
        line-height: 2 !important;
    }

    .card p { 
        font-size: 22px; 
        padding: 0 !important;
        margin: 0 !important; 
        color: #444; 
        text-align: center;
        line-height: 2 !important;
    }

    /* Vehicle Table Styling */
    .vehicle-table table { 
        width: 100%; 
        border-collapse: collapse; 
        text-align: left; 
    }
    .vehicle-table th { 
        background-color: #fafcfb; 
        padding: 8px; /* reduced padding */
    }
    .vehicle-table td { 
        border-bottom: 1px solid #ddd; 
        padding: 8px; /* compact cell spacing */
       background-color: #fafcfb; 
    }
    .vehicle-table tr {
        line-height: 1.3; /* compact row height */
    }

    body { background-color: #fafcfb; }

    .vehicle-table {
        border-collapse: collapse;
        width: 100%;
        font-size: 22px; /* slightly smaller text */
    }
    .vehicle-table th, .vehicle-table td {
        border: 2px solid #ccc;
        padding: 8px;
        text-align: center;
    }
    .vehicle-table th {
        background-color: #a7b88c;
        color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =================== NAVIGATION TABS ===================
tabs = st.tabs(["🏠 Home", "📝 SQL Queries", "📊 Dashboard", "ℹ️ About"])

# =================== HOME PAGE ===================
with tabs[0]:
    # Welcome Header
    st.markdown(
        """
        <div style="text-align: center; margin-top:50px;">
            <h1 style="color: #2e4600; margin: 0;">🚖 OLA Ride Insights </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Welcome Box
    st.markdown(
        """
        <div class="welcome-box">
            <h2 style='text-align:center; font-size:28;'>Welcome to the <b>OLA Rider Project Insights</b></h2>
            Explore ride trends, revenue insights, and customer ratings in a stylish, interactive format.  
            Dive into vehicle type performance, top customers, and more — all in one place.  
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- Quick Overview ----------------
    st.markdown(
        """
        <h2 style='text-align:center;'>Quick Overview </h2>
        <div class="card-row">
            <div class="card"><h2>63967</h2><p>Total Rides</p></div>
            <div class="card"><h2>35080467</h2><p>Total Revenue</p></div>
            <div class="card"><h2>Prime Sedan 🏎</h2><p>Top Vehicle Type</p></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- Payment Methods ----------------
    st.markdown(
        """
        <h2 style='text-align:center;'>Payment Methods </h2>
        <div class="card-row">
            <div class="card">
                <p><strong>Cash:</strong> 1088</p>
                <p><strong>UPI:</strong> 804</p>
                <p><strong>Credit Card:</strong> 94</p>
                <p><strong>Debit Card:</strong> 14</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ================== Vehicle Details Table ==================
    st.markdown(
        """
        <h2 style='text-align:center;'>Vehicles – Bookings & Ratings </h2>
        <div style="overflow-x:auto;">
        <table class="vehicle-table">
            <tr>
                <th>Vehicle Type</th>
                <th>Total Bookings</th>
                <th>Avg Driver Rating</th>
                <th>Avg Rider Rating</th>
            </tr>
            <tr>
                <td>🏎 Prime Sedan</td>
                <td>14877</td>
                <td>2.52</td>
                <td>2.52</td>
            </tr>
            <tr>
                <td>🛵 eBike</td>
                <td>14816</td>
                <td>2.48</td>
                <td>2.47</td>
            </tr>
            <tr>
                <td>🛺 Auto</td>
                <td>14755</td>
                <td>2.49</td>
                <td>2.48</td>
            </tr>
            <tr>
                <td>🚙 Prime Plus</td>
                <td>14707</td>
                <td>2.47</td>
                <td>2.47</td>
            </tr>
            <tr>
                <td>🏍 Bike</td>
                <td>14662</td>
                <td>2.48</td>
                <td>2.49</td>
            </tr>
            <tr>
                <td>🚗 Prime SUV</td>
                <td>14655</td>
                <td>2.46</td>
                <td>2.46</td>
            </tr>
            <tr>
                <td>🚕 Mini</td>
                <td>14552</td>
                <td>2.48</td>
                <td>2.48</td>
            </tr>
        </table>
        </div>
        """,
        unsafe_allow_html=True
    )

# =================== SQL QUERIES PAGE ===================
st.markdown(
    """
    <style>
    /* Increase font size, height, and width of selectbox */
    div[data-baseweb="select"] > div > div > div {
        font-size: 23px !important;
        height: 40px !important;      /* taller dropdown */
        min-width: 300px !important;  /* wider dropdown */
    }

    /* Increase font size and padding for buttons */
    div.stButton > button {
        font-size: 23px !important;
        padding: 12px 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with tabs[1]:
    st.markdown(
        """
        <div style="text-align: center; font-size: 23px; color: #2e4600;">
            <h2>📝 SQL Queries Dropdown</h2>
            <p>Select a report to run from the dropdown:</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    from queries import all_queries
    query_options = list(all_queries.keys())

    # Center selectbox
    st.markdown('<div style="display:flex; justify-content:center;">', unsafe_allow_html=True)
    choice = st.selectbox("", query_options)
    st.markdown('</div>', unsafe_allow_html=True)

    # Center button
    st.markdown('<div style="display:flex; justify-content:center; margin-top:15px;">', unsafe_allow_html=True)
    if st.button("Run Query"):
        try:
            db_path = "D:\OLA Rider\database\OLA_DataSet.db"
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query(all_queries[choice], conn)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            conn.close()
    st.markdown('</div>', unsafe_allow_html=True)

# =================== DASHBOARD PAGE ===================
with tabs[2]:
    st.header("📊 Interactive Dashboard")
    st.markdown("Embed your Power BI report below:")
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiODYxYWU0M2QtNzUwMy00NjE5LTkzNmMtZTQzMzljMGExZGJlIiwidCI6IjQyOTUwMzI1LWZiOTgtNDQ0Zi1hZjQxLTY3YzE1NTYwNDkxOSJ9"
    st.components.v1.iframe(power_bi_url, width=1500, height=800)

# =================== ABOUT PAGE ===================
with tabs[3]:
    components.html(
        """
        <div style="text-align: center; font-size: 27px; line-height: 1.8; color: #2e4600;">
            <h1 style="font-size: 50px; color: #1a2e05;">About OLA Rides</h1>

            <p><b>ℹ️ About OLA:</b><br>
            OLA is one of India’s largest ride-hailing companies, connecting millions of customers with drivers through its app.  
            It provides safe, affordable, and convenient transportation across multiple cities.</p>

            <p><b>Services Offered:</b><br>
            🚖 Cabs: Mini, Prime Sedan, Prime SUV, Auto, and more.<br>
            🛵 Bike & e-Bike Rides: Affordable short-distance travel.<br>
            🚌 Outstation & Rentals: Intercity travel and hourly packages.<br>
            🚐 Shared Rides: Cost-effective rides with co-passengers.</p>

            <p><b>Key Features:</b><br>
            - Easy booking via mobile app.<br>
            - Multiple payment options (cash, card, UPI, Ola Money).<br>
            - Real-time driver tracking & estimated fare.<br>
            - Safety features like SOS and driver background checks.</p>

            <p><b>Why OLA?</b><br>
            Affordable rides for everyone.<br>
            Wide variety of vehicle options.<br>
            Expanding globally beyond India.</p>
        </div>
        """,
        height=600,
    )