import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MCP server configuration
MCP_SERVER_URL = "http://localhost:3000"  # Default MCP server URL

# Streamlit app title and description
st.title("MCP Integration Dashboard")
st.markdown("""
Welcome to the MCP Integration Dashboard! This application allows you to interact with the Model Context Protocol server.

Features:
- View MCP server status
- Send requests to MCP server
- Monitor responses and interactions
""")

# Sidebar configuration
st.sidebar.header("MCP Server Settings")
server_url = st.sidebar.text_input("MCP Server URL", MCP_SERVER_URL)

# Main content
with st.expander("Server Status", expanded=True):
    if st.button("Check Server Status"):
        try:
            response = requests.get(f"{server_url}/status")
            st.json(response.json())
        except Exception as e:
            st.error(f"Error connecting to server: {str(e)}")

# Create a form for sending requests
col1, col2 = st.columns(2)

with col1:
    with st.form("mcp_request_form"):
        st.subheader("Send Request to MCP")
        request_type = st.selectbox("Request Type", ["GET", "POST", "PUT", "DELETE"])
        endpoint = st.text_input("Endpoint", "/api")
        data = st.text_area("Request Data (JSON)", "{}")
        
        if st.form_submit_button("Send Request"):
            try:
                headers = {"Content-Type": "application/json"}
                if request_type == "GET":
                    response = requests.get(f"{server_url}{endpoint}")
                elif request_type == "POST":
                    response = requests.post(f"{server_url}{endpoint}", headers=headers, json=data)
                elif request_type == "PUT":
                    response = requests.put(f"{server_url}{endpoint}", headers=headers, json=data)
                else:
                    response = requests.delete(f"{server_url}{endpoint}")
                
                st.success("Request sent successfully!")
                st.json(response.json())
            except Exception as e:
                st.error(f"Error sending request: {str(e)}")

with col2:
    st.subheader("Response History")
    # This would be implemented with a database or file storage
    st.write("Response history will be shown here")

# Add footer
st.markdown("""
---
Created by: Sainath
Using Streamlit and MCP Protocol
""")