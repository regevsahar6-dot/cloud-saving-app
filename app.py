import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Skill Analyzer", layout="wide")

# כותרת המוצר
st.title("🤖 Cloud Code AI Skill Analyzer")
st.subheader("ניתוח עלויות ושימוש בטוקנים לפי סקיל")

# 1+2. הגדרת ה"סקילים" והעלויות שלהם (מחיר ל-1,000 טוקנים)
skills_pricing = {
    "Code Generation": 0.03,  # מחיר לדוגמה
    "Unit Test Creator": 0.01,
    "Refactoring Tool": 0.02,
    "Documentation Bot": 0.005
}

# 3. הדמיית נתונים שמגיעים מ-Cloud Code (API Simulation)
# נניח שזה המידע שהמערכת שלך "שאבה" מהלוגים של החברה
raw_logs = [
    {"user": "Alice", "skill": "Code Generation", "tokens": 15000},
    {"user": "Bob", "skill": "Code Generation", "tokens": 22000},
    {"user": "Charlie", "skill": "Unit Test Creator", "tokens": 50000},
    {"user": "Alice", "skill": "Refactoring Tool", "tokens": 8000},
    {"user": "Dave", "skill": "Documentation Bot", "tokens": 12000},
    {"user": "Eve", "skill": "Code Generation", "tokens": 5000},
]

df = pd.DataFrame(raw_logs)

# 4+5. חישוב עלויות ופירוט טוקנים
df['cost_per_1k'] = df['skill'].map(skills_pricing)
df['total_cost'] = (df['tokens'] / 1000) * df['cost_per_1k']

# תצוגת מדדים כלליים (Dashboard Metrics)
total_tokens = df['tokens'].sum()
total_spend = df['total_cost'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("סה-כ טוקנים שנצרכו", f"{total_tokens:,}")
col2.metric("בזבוז כולל (USD)", f"${total_spend:.2f}")
col3.metric("סקיל הכי יקר", df.groupby('skill')['total_cost'].sum().idxmax())

st.divider()

# גרף עלויות לפי סקיל
st.subheader("ניתוח עלויות לפי סקיל")
fig_cost = px.pie(df, values='total_cost', names='skill', hole=0.4, 
                 title="חלוקת תקציב לפי סקילים (ב-$)")
st.plotly_chart(fig_cost, use_container_width=True)

# פירוט טוקנים (Table)
st.subheader("פירוט שימוש וטוקנים")
detailed_df = df.groupby('skill').agg({
    'tokens': 'sum',
    'total_cost': 'sum'
}).reset_index()

st.table(detailed_df.style.format({"total_cost": "${:.2f}", "tokens": "{:,}"}))

# כפתור שמדמה שליחת דוח למנהל
if st.button("הפק דוח חיסכון למנהל"):
    st.info("מנתח נתונים... נמצא כי סקיל 'Unit Test Creator' חורג מהתקציב ב-15%")
