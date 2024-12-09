# **Truherb Sales Performance Dashboard**

## **Overview**
The **Truherb Sales Performance Dashboard** is a web-based application developed using **Streamlit**. It provides sales performance insights for both admin and individual users, with features like interactive visualizations, performance ratings, and secure role-based access.

---

## **Features**
### **1. Authentication System**
- Role-based login:
  - **Admin**: Access all agents' data and manage performance insights.
  - **User**: View personalized performance metrics.
- Credentials securely managed through predefined mappings.

### **2. Admin Dashboard**
- View all agents' monthly performance in a tabular format.
- Export performance data as a CSV file.
- Provides individual and overall performance ratings based on targets.

### **3. User Dashboard**
- Access personalized data, including:
  - Revenue vs. target visualizations.
  - Overall ratings and performance insights.
- Interactive bar charts powered by **Plotly**.

### **4. Data Handling**
- Automatically fetches sales data from a public Google Sheet.
- Cleans and formats revenue, targets, and inquiry columns for consistency.

---

## **Technologies Used**
- **Python**: Backend scripting.
- **Streamlit**: Frontend framework for dashboards.
- **Pandas**: Data cleaning and manipulation.
- **Plotly**: Visualization library for charts.

---

## **Setup Instructions**

### **1. Prerequisites**
Ensure the following are installed:
- Python 3.8 or above.
- Recommended: Virtual environment for dependency management.

### **2. Installation**
Clone the repository and install dependencies:

```
git clone <repository-url>
cd <repository-folder>
pip install -r requirements.txt
```
### **3. Running the Application**
Run the app locally:
```
streamlit run app.py
```
The app will open in your default web browser at http://localhost:8501.


