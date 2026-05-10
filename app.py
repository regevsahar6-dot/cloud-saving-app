import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cloud Optimizer", layout="wide")
st.title("💰 Cloud Code Optimization Dashboard")

# נתונים לדוגמה
data = {
    "מפתח": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
    "עלות לשעה ($)": [0.5, 1.2, 0.5, 0.8, 2.1],
    "שעות ללא שימוש (Idle)": [12, 2, 45, 8, 15],
    "צוות": ["Backend", "Frontend", "Data", "Backend", "DevOps"]
}
df = pd.DataFrame(data)
df["בזבוז מצטבר ($)"] = df["עלות לשעה ($)"] * df["שעות ללא שימוש (Idle)"]

# הצגת מדדים
col1, col2 = st.columns(2)
col1.metric("סה-כ בזבוז", f"${df['בזבוז מצטבר ($)'].sum():.2f}")
col2.metric("חיסכון חודשי פוטנציאלי", f"${df['בזבוז מצטבר ($)'].sum() * 30:.2f}")

# גרף
fig = px.bar(df, x="מפתח", y="בזבוז מצטבר ($)", color="צוות", title="בזבוז לפי מפתח")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(df)
