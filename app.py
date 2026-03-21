import streamlit as st

st.set_page_config(page_title="Thế Giới Di Động Analytics")

# Title
st.markdown("<h1 style='text-align: center; color: orange;'> THẾ GIỚI DI ĐỘNG (TEST DEPLOYMENT AZURE)</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<h3 style='text-align: center;'>Customer Data Analytics Platform</h3>", unsafe_allow_html=True)

# Introduction
st.markdown("## 🏢 About Thế Giới Di Động")

st.write("""
Thế Giới Di Động is one of Vietnam’s leading retail companies specializing in mobile phones, electronics, and consumer technology products. 
The company operates a nationwide network of stores and serves millions of customers across Vietnam.

With the rapid growth of digital transformation, Thế Giới Di Động continuously leverages data to enhance customer experience, optimize business operations, and support strategic decision-making.
""")

# Project Purpose
st.markdown("## 🎯 Project Purpose")

st.write("""
This Customer Data Analytics Platform aims to:

- Analyze customer behavior and purchasing patterns  
- Provide insights for business decision-making  
- Support marketing and sales optimization  
- Enable data-driven strategies  

The platform integrates modern data engineering and analytics tools including Azure Data Lake, Synapse Analytics, and Power BI.
""")

# Technologies
st.markdown("## ⚙️ Technologies Used")

st.write("""
- **Docker**: Containerization of the application  
- **Terraform**: Infrastructure as Code for Azure deployment  
- **Azure Web App**: Cloud hosting platform  
- **GitHub Actions**: CI/CD automation  
- **Power BI**: Data visualization and dashboarding  
""")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Customer Data Analytics Platform</p>", unsafe_allow_html=True)