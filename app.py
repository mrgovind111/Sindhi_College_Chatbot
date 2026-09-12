import streamlit as st
from chatbot import answer_question
from analytics import get_stats, clear_logs

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sindhi College Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Hide Streamlit default footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Main banner */
.banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    padding: 30px 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}
.banner h1 {
    font-size: 34px;
    margin: 0;
    color: white;
}
.banner p {
    font-size: 16px;
    margin-top: 8px;
    color: #e0e7ff;
}

/* Info card */
.card {
    background: #f8fafc;
    padding: 18px;
    border-radius: 10px;
    border-left: 5px solid #3b82f6;
    margin-bottom: 12px;
}

/* Sidebar section titles */
.sidebar-title {
    font-weight: bold;
    font-size: 15px;
    color: #1e3a8a;
    margin-top: 10px;
    margin-bottom: 6px;
}

/* Quick question buttons */
.stButton > button {
    width: 100%;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    color: #1e293b;
    font-weight: 500;
    padding: 10px 6px;
    transition: 0.2s;
}
.stButton > button:hover {
    background: #eff6ff;
    border-color: #3b82f6;
    color: #1e3a8a;
}

/* Chat messages */
.stChatMessage {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<div class="banner">
    <h1>🎓 Sindhi College Chatbot</h1>
    <p>AI-Powered Student Assistant • Kempapura, Hebbal, Bengaluru</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">🏫 College Information</div>', unsafe_allow_html=True)
    st.write("📍 #33/2B, Kempapura, Hebbal, Bengaluru - 560024")
    st.write("📞 080 - 2363 7543 / 44")
    st.write("📧 mail@sindhicollege.com")
    st.write("🌐 www.sindhicollege.com")
    st.write("🏛️ Bangalore University")
    st.write("⭐ NAAC Accredited B++")

    st.divider()

    st.markdown('<div class="sidebar-title">📚 I Can Help With</div>', unsafe_allow_html=True)
    st.write("• Courses • Admission • Documents")
    st.write("• Facilities • Location • Contact")
    st.write("• Python • DBMS • Java • AI / ML")

    st.divider()

    # Download chat history
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

    # ---------------- ADMIN ----------------
    st.divider()
    st.markdown('<div class="sidebar-title">🔐 Admin</div>', unsafe_allow_html=True)

    admin_password = st.text_input(
        "Enter admin password",
        type="password",
        key="admin_pass"
    )

    if admin_password == "Govind@2223":
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

# ---------------- WELCOME CARD ----------------
st.markdown("""
<div class="card">
    <b>Welcome!</b> Ask me about courses, admission, facilities,
    staff, or any academic topic. I use a combination of offline
    rules and AI to give you accurate answers.
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

col_clear, _ = st.columns([1, 3])
with col_clear:
    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# ---------------- QUICK QUESTIONS ----------------
st.subheader("💡 Quick Questions")

row1 = st.columns(3)
with row1[0]:
    if st.button("📚 Courses"):
        q = "What courses are available?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row1[1]:
    if st.button("📍 Location"):
        q = "Where is Sindhi College located?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row1[2]:
    if st.button("🎓 Admission"):
        q = "What is the admission eligibility?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()

row2 = st.columns(3)
with row2[0]:
    if st.button("📄 Documents"):
        q = "What documents are required?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row2[1]:
    if st.button("🏫 Facilities"):
        q = "What facilities are available?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row2[2]:
    if st.button("👨‍🏫 Principal"):
        q = "Who is the principal?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()

row3 = st.columns(3)
with row3[0]:
    if st.button("📖 Librarian"):
        q = "Who is the librarian?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row3[1]:
    if st.button("☕ Java"):
        q = "What is Java?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()
with row3[2]:
    if st.button("🤖 AI"):
        q = "What is Artificial Intelligence?"
        a = answer_question(q)
        st.session_state.messages += [
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
        st.rerun()

# ---------------- CHAT INPUT ----------------
question = st.chat_input("💬 Ask me anything about Sindhi College...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    answer = answer_question(question)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Sindhi College Chatbot • Built with Streamlit + Groq AI")