import streamlit as st
from openai import OpenAI # ספריה לחיבור ל-AI

st.title("🚀 Cloud Code AI Analyzer (Live)")

# שדה להזנת מפתח - ככה חברות משתמשות בזה
api_key = st.sidebar.text_input("הכנס API Key של החברה", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # בחירת ה"סקיל" להפעלה
    skill = st.selectbox("בחר סקיל להפעלה", ["Code Generation", "Unit Test Creator"])
    user_input = st.text_area("הכנס פקודה למפתח (Prompt)")

    if st.button("הפעל סקיל"):
        # שליחת הבקשה האמיתית ל-AI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        # 1+5. חילוץ נתוני טוקנים מהתשובה האמיתית
        tokens_used = response.usage.total_tokens
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        
        # 2. חישוב עלות (לפי מחירון GPT-3.5)
        cost = (tokens_used / 1000) * 0.002 

        # הצגת התוצאה למפתח
        st.write("### תשובת ה-AI:")
        st.write(response.choices[0].message.content)

        # 4. האנליטיקה שאתה "מוכר" לחברה
        st.divider()
        st.subheader("📊 אנליטיקה לשימוש הנוכחי (זה הערך שלך!)")
        col1, col2, col3 = st.columns(3)
        col1.metric("טוקנים שנצרכו", tokens_used)
        col2.metric("עלות הפעולה", f"${cost:.5f}")
        col3.metric("סוג סקיל", skill)
        
        st.info(f"פירוט: {prompt_tokens} טוקנים בשאלה ו-{completion_tokens} בתשובה.")
else:
    st.warning("אנא הכנס API Key בתפריט הצד כדי להתחיל לנתח שימוש.")
