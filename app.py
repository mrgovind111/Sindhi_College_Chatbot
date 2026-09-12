import streamlit as st
from chatbot import answer_question
from analytics import get_stats, clear_logs

# Custom styling
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 35px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #dddddd;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Sindhi College Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.image("logo.jpg", width=250)

st.markdown(
    '<div class="main-title">🎓 Sindhi College Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Student Assistant</div>',
    unsafe_allow_html=True
)

st.write(
    "Welcome! Ask me about courses, admission, facilities, "
    "college information, or academic topics."
)

st.divider()


# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🏫 Sindhi College")

    st.write("### College Information")
    st.write("📍 #33/2B, Kempapura, Hebbal, Bengaluru - 560024")
    st.write("📞 080 - 2363 7543 / 44")
    st.write("📧 mail@sindhicollege.com")
    st.write("🌐 www.sindhicollege.com")
    st.write("🏛️ Bangalore University")
    st.write("⭐ NAAC Accredited B++")

    st.divider()

    st.write("### 📚 I Can Help With")
    st.write("• Courses")
    st.write("• Admission")
    st.write("• Documents")
    st.write("• Facilities")
    st.write("• College Location")
    st.write("• Python")
    st.write("• DBMS")
    st.write("• Java")
    st.write("• AI / ML")

    st.divider()

    # Download chat history button
    if st.session_state.get("messages"):
        chat_text = ""
        for msg in st.session_state.messages:
            role = "Student" if msg["role"] == "user" else "Chatbot"
            chat_text += f"{role}: {msg['content']}\n\n"

        st.download_button(
            label="📥 Download Chat History",
            data=chat_text,
            file_name="sindhi_college_chat.txt",
            mime="text/plain"
        )

    st.caption("Sindhi College Student Assistant")

    # ---------------- ADMIN DASHBOARD ----------------
    st.divider()
    st.write("### 🔐 Admin")

    admin_password = st.text_input(
        "Enter admin password",
        type="password",
        key="admin_pass"
    )

    if admin_password == "admin123":
        total, top = get_stats()

        st.success(f"Total questions asked: {total}")

        if top:
            st.write("**Top 10 questions:**")
            for q, count in top:
                st.write(f"• {q} — {count} times")
        else:
            st.info("No questions logged yet.")

        if st.button("🗑️ Clear Question Log"):
            clear_logs()
            st.success("Log cleared.")


# ---------------- STUDENT DASHBOARD ----------------
st.subheader("🎓 Student Dashboard")

dash1, dash2, dash3 = st.columns(3)

with dash1:
    st.info("📚\n\n**Academic Help**\n\nPython • Java • DBMS • AI")

with dash2:
    st.info("🏫\n\n**College Help**\n\nCourses • Admission • Facilities")

with dash3:
    st.info("💬\n\n**Chat Assistant**\n\nAsk your questions anytime")

st.divider()


# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.button("🧹 Clear Conversation"):
    st.session_state.messages = []
    st.rerun()


# ---------------- QUICK QUESTIONS ----------------
st.subheader("💡 Quick Questions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📚 Courses"):
        question = "What courses are available?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col2:
    if st.button("📍 Location"):
        question = "Where is Sindhi College located?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col3:
    if st.button("🎓 Admission"):
        question = "What is the admission eligibility?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()


col4, col5, col6 = st.columns(3)

with col4:
    if st.button("📄 Documents"):
        question = "What documents are required?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col5:
    if st.button("🏫 Facilities"):
        question = "What facilities are available?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col6:
    if st.button("💻 BCA"):
        question = "Tell me about BCA"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()


col7, col8, col9 = st.columns(3)

with col7:
    if st.button("🗄️ DBMS"):
        question = "What is DBMS?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col8:
    if st.button("☕ Java"):
        question = "What is Java?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()

with col9:
    if st.button("🤖 AI"):
        question = "What is Artificial Intelligence?"
        answer = answer_question(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()


# ---------------- CHAT INPUT ----------------
question = st.chat_input(
    "💬 Ask me anything about Sindhi College..."
)

if question:

    # Add student question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    # Get chatbot answer
    answer = answer_question(question)

    # Add chatbot answer
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()