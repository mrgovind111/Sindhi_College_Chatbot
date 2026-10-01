import streamlit as st
import pandas as pd
import time
import random
from chatbot import answer_question
from analytics import (
    get_stats, clear_logs,
    log_feedback, get_feedback_stats, clear_feedback,
    log_admission, get_admissions, clear_admissions
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sindhi College Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Page background with college photo — forced */
.stApp {
    background:
        linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.94)),
        url("college_bg.jfif") !important;
    background-size: cover !important;
    background-position: center top !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    background-color: #ffffff;
}

/* Force background on Streamlit's wrapper elements */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.94)),
        url("college_bg.jfif") !important;
    background-size: cover !important;
    background-position: center top !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

.main {
    background: transparent !important;
}

.block-container {
    background: transparent !important;
}

/* Glassmorphism banner */
.banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 60%, #60a5fa 100%);
    padding: 35px 20px;
    border-radius: 18px;
    text-align: center;
    color: white;
    margin-bottom: 22px;
    animation: fadeInDown 0.9s ease-in-out, floatY 4s ease-in-out infinite;
    box-shadow: 0 12px 30px rgba(30, 58, 138, 0.35),
                inset 0 1px 0 rgba(255,255,255,0.3);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255,255,255,0.25);
}
.banner h1 {
    font-size: 36px;
    margin: 0;
    color: white;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.25);
    animation: fadeIn 1.2s ease-in-out;
}
.banner p {
    font-size: 16px;
    margin-top: 10px;
    color: #e0e7ff;
    animation: fadeIn 1.6s ease-in-out;
}

@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-25px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(15px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes floatY {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-6px); }
    100% { transform: translateY(0); }
}
@keyframes bounce {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
    30% { transform: translateY(-6px); opacity: 1; }
}

/* Welcome card */
.card {
    background: rgba(255, 255, 255, 0.92);
    padding: 20px;
    border-radius: 14px;
    border-left: 5px solid #3b82f6;
    margin-bottom: 14px;
    animation: slideUp 0.6s ease-in-out;
    box-shadow: 0 4px 14px rgba(30,58,138,0.08);
    transition: all 0.3s ease;
    backdrop-filter: blur(4px);
}
.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(59,130,246,0.25);
    border-left: 5px solid #1e3a8a;
}

/* Sidebar titles */
.sidebar-title {
    display: flex;
    align-items: center;
    font-weight: bold;
    font-size: 15px;
    color: #1e3a8a;
    margin-top: 12px;
    margin-bottom: 8px;
    padding: 6px 10px;
    background: linear-gradient(90deg, #eff6ff 0%, #ffffff 100%);
    border-radius: 8px;
    border-left: 4px solid #3b82f6;
}

/* Animated buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    color: #1e293b;
    font-weight: 500;
    padding: 10px 6px;
    transition: all 0.25s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    border-color: #3b82f6;
    color: #1e3a8a;
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 6px 16px rgba(59, 130, 246, 0.35);
}
.stButton > button:active {
    transform: translateY(0) scale(0.99);
}

/* Rounded chat bubbles */
.stChatMessage {
    border-radius: 16px !important;
    padding: 12px 16px;
    animation: slideUp 0.4s ease-in-out;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border: 1px solid #e2e8f0;
    background: rgba(255, 255, 255, 0.95);
}

/* BLACK chat input with WHITE text */
.stChatInputContainer textarea {
    border-radius: 12px !important;
    border: 1.5px solid #1e293b !important;
    background: #000000 !important;
    color: #ffffff !important;
    font-weight: 500;
    transition: all 0.2s ease;
}

.stChatInputContainer textarea::placeholder {
    color: #cbd5e1 !important;
    opacity: 0.9;
}

.stChatInputContainer textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.25);
    background: #000000 !important;
    color: #ffffff !important;
}

.stChatInputContainer {
    background: #000000 !important;
    border-radius: 14px !important;
    padding: 4px !important;
}

.stChatInputContainer button {
    background: #3b82f6 !important;
    color: white !important;
}

.stChatInputContainer button:hover {
    background: #1e3a8a !important;
}

/* Custom scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 10px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3b82f6 0%, #1e3a8a 100%);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover { background: #1e3a8a; }

/* Admission form card */
.form-card {
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    padding: 20px 24px;
    border-radius: 16px;
    color: white;
    margin-top: 24px;
    margin-bottom: 16px;
    box-shadow: 0 8px 22px rgba(30, 58, 138, 0.28);
    animation: slideUp 0.6s ease-in-out;
}
.form-card h2 { margin: 0; font-size: 24px; color: white; }
.form-subtitle { margin-top: 6px; font-size: 14px; color: #e0e7ff; }

/* Form inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    border-radius: 10px !important;
    border: 1.5px solid #cbd5e1 !important;
    transition: all 0.2s ease;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.15);
}

/* Submit button */
.stFormSubmitButton > button {
    width: 100%;
    background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%);
    color: white !important;
    font-weight: 600;
    border-radius: 10px;
    padding: 12px;
    border: none;
    box-shadow: 0 4px 14px rgba(59,130,246,0.35);
    transition: all 0.25s ease;
}
.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(59,130,246,0.5);
}

/* Stats bar */
.stats-bar {
    display: flex;
    justify-content: space-around;
    background: linear-gradient(90deg, rgba(239,246,255,0.95) 0%, rgba(219,234,254,0.95) 100%);
    padding: 14px 10px;
    border-radius: 12px;
    margin-bottom: 18px;
    border: 1px solid #bfdbfe;
    animation: slideUp 0.8s ease-in-out;
    backdrop-filter: blur(4px);
}
.stats-bar div { text-align: center; font-size: 13px; color: #1e3a8a; }
.stats-bar b { display: block; font-size: 20px; color: #1e3a8a; }

/* Rotating hint */
.rotating-hint {
    text-align: center;
    color: #1e293b;
    font-size: 14px;
    margin-top: 6px;
    margin-bottom: 12px;
    font-style: italic;
    font-weight: 500;
    animation: fadeIn 2s ease-in-out infinite alternate;
    text-shadow: 0 1px 2px rgba(255,255,255,0.8);
}

/* Suggestion chips */
.chip-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px; margin-bottom: 12px; }
.chip {
    background: #eff6ff;
    color: #1e3a8a;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
    border: 1px solid #bfdbfe;
    transition: all 0.2s ease;
}
.chip:hover { background: #dbeafe; border-color: #3b82f6; transform: translateY(-1px); }

/* Typing dots */
.typing-dots span {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #3b82f6;
    border-radius: 50%;
    margin: 0 3px;
    animation: bounce 1.2s infinite;
}
.typing-dots span:nth-child(2) { animation-delay: 0.15s; }
.typing-dots span:nth-child(3) { animation-delay: 0.3s; }
</style>
""", unsafe_allow_html=True)

# ---------------- BANNER ----------------
st.markdown("""
<div class="banner">
    <h1>🎓 Sindhi College Chatbot</h1>
    <p>AI-Powered Student Assistant • Kempapura, Hebbal, Bengaluru</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STATS BAR ----------------
st.markdown("""
<div class="stats-bar">
    <div><b>60+</b>Faculty</div>
    <div><b>12</b>Courses</div>
    <div><b>1300+</b>Students</div>
    <div><b>B++</b>NAAC</div>
</div>
""", unsafe_allow_html=True)

# ---------------- ROTATING HINT ----------------
hints = [
    "💡 Try asking: Who is the principal?",
    "💡 Try asking: What courses are offered?",
    "💡 Try asking: Where is the college?",
    "💡 Try asking: Who is HOD of BCA?",
    "💡 Try asking: What is the admission process?",
    "💡 Try asking: Tell me about the library",
]
st.markdown(
    f'<div class="rotating-hint">{random.choice(hints)}</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">🏫 College Information</div>', unsafe_allow_html=True)
    st.write("📍 #33/2B, Kempapura, Hebbal, Bengaluru - 560024")
    st.write("📞 080 - 2363 7543 / 44")
    st.write("📧 mail@sindhicollege.com")
    st.write("🌐 www.sindhicollege.com")
    st.write("🏛️ Bangalore City University")
    st.write("⭐ NAAC Accredited B++")

    st.divider()

    st.markdown('<div class="sidebar-title">📚 I Can Help With</div>', unsafe_allow_html=True)
    st.write("• Courses • Admission • Documents")
    st.write("• Facilities • Location • Contact")
    st.write("• Python • DBMS • Java • AI / ML")

    st.divider()

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

        st.divider()
        st.markdown("**📊 Feedback Stats**")

        fb_total, fb_up, fb_down = get_feedback_stats()
        st.write(f"Total feedback: {fb_total}")
        st.write(f"👍 Helpful: {fb_up}")
        st.write(f"👎 Not helpful: {fb_down}")

        if fb_total > 0:
            percent = round((fb_up / fb_total) * 100, 1)
            st.write(f"Helpful rate: {percent}%")

        if st.button("🗑️ Clear Feedback"):
            clear_feedback()
            st.success("Feedback cleared.")

        st.divider()
        st.markdown("**📝 Admission Enquiries**")

        admissions = get_admissions()
        st.write(f"Total enquiries: {len(admissions)}")

        if admissions:
            for i, entry in enumerate(admissions[-10:], 1):
                st.write(
                    f"{i}. **{entry.get('name','')}** — "
                    f"{entry.get('phone','')} — "
                    f"{entry.get('course','')}"
                )
        else:
            st.info("No enquiries yet.")

        if st.button("🗑️ Clear Admission Enquiries"):
            clear_admissions()
            st.success("Admission enquiries cleared.")

        st.divider()
        st.markdown("**📈 Question Analytics**")

        if top:
            df = pd.DataFrame(top, columns=["Question", "Count"])
            st.bar_chart(df.set_index("Question"))
        else:
            st.info("No question data yet.")

        st.markdown("**🥧 Feedback Breakdown**")

        if fb_total > 0:
            fb_df = pd.DataFrame(
                {"Type": ["Helpful", "Not Helpful"], "Count": [fb_up, fb_down]}
            )
            st.bar_chart(fb_df.set_index("Type"))
        else:
            st.info("No feedback data yet.")

# ---------------- BOT GREETING ----------------
st.markdown("""
<div class="card">
    <b>👋 Hi! I'm the Sindhi College assistant.</b><br>
    Ask me anything about our college — courses, admission,
    facilities, staff, or academics. I will give you accurate
    answers from our official college data.
</div>
""", unsafe_allow_html=True)

# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for i, message in enumerate(st.session_state.messages):
    avatar = "🎓" if message["role"] == "assistant" else "🙋"
    with st.chat_message(message["role"], avatar=avatar):
        if (
            message["role"] == "assistant"
            and i == len(st.session_state.messages) - 1
        ):
            placeholder = st.empty()
            typed = ""
            for char in message["content"]:
                typed += char
                placeholder.markdown(typed + " ▌")
                time.sleep(0.005)
            placeholder.markdown(typed)
        else:
            st.write(message["content"])

col_clear, _ = st.columns([1, 3])
with col_clear:
    if st.button("🧹 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# ---------------- FOLLOW-UP SUGGESTIONS ----------------
if st.session_state.messages:
    last_bot_text = ""
    for msg in reversed(st.session_state.messages):
        if msg["role"] == "assistant":
            last_bot_text = msg["content"].lower()
            break

    suggestions = []
    if "principal" in last_bot_text:
        suggestions = ["Who is the Vice Principal?", "Who is the HOD of BCA?"]
    elif "librarian" in last_bot_text:
        suggestions = ["What are the library timings?", "Tell me about the library"]
    elif "bca" in last_bot_text:
        suggestions = ["Who is the HOD of BCA?", "What subjects are in BCA?"]
    elif "hebbal" in last_bot_text or "address" in last_bot_text or "location" in last_bot_text:
        suggestions = ["What are the college timings?", "How do I apply?"]
    elif "course" in last_bot_text:
        suggestions = ["What is the admission process?", "What documents are needed?"]
    else:
        suggestions = ["Who is the principal?", "What courses are offered?", "Where is the college?"]

    if suggestions:
        st.markdown("**💡 You might also ask:**")
        chip_html = '<div class="chip-row">'
        for s in suggestions:
            chip_html += f'<span class="chip">{s}</span>'
        chip_html += "</div>"
        st.markdown(chip_html, unsafe_allow_html=True)

        cols = st.columns(len(suggestions))
        for idx, s in enumerate(suggestions):
            with cols[idx]:
                if st.button(s, key=f"sugg_{idx}_{len(st.session_state.messages)}"):
                    st.session_state.messages.append({"role": "user", "content": s})
                    with st.spinner("🤔 Thinking..."):
                        ans = answer_question(s)
                    st.session_state.messages.append({"role": "assistant", "content": ans})
                    st.rerun()

# ---------------- FEEDBACK ----------------
if st.session_state.messages:
    last_user = None
    last_bot = None
    for msg in reversed(st.session_state.messages):
        if msg["role"] == "assistant" and last_bot is None:
            last_bot = msg["content"]
        elif msg["role"] == "user" and last_user is None:
            last_user = msg["content"]
        if last_user and last_bot:
            break

    if last_user and last_bot:
        st.markdown("**Was the last answer helpful?**")
        fb1, fb2, _ = st.columns([1, 1, 4])

        with fb1:
            if st.button("👍 Helpful", key="fb_up"):
                log_feedback(last_user, last_bot, "up")
                st.success("Thanks for your feedback!")

        with fb2:
            if st.button("👎 Not helpful", key="fb_down"):
                log_feedback(last_user, last_bot, "down")
                st.success("Thanks — we will improve.")

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

# ---------------- ADMISSION ENQUIRY FORM ----------------
st.markdown("""
<div class="form-card">
    <h2>📝 Admission Enquiry</h2>
    <p class="form-subtitle">
        Fill in your details below. The college office will contact you soon.
    </p>
</div>
""", unsafe_allow_html=True)

with st.form("admission_form", clear_on_submit=True):
    col_a, col_b = st.columns(2)

    with col_a:
        name = st.text_input("👤 Full Name *", placeholder="Enter your full name")
        phone = st.text_input("📞 Phone Number *", placeholder="10-digit mobile number")

    with col_b:
        email = st.text_input("📧 Email (optional)", placeholder="your@email.com")

        course = st.selectbox(
            "🎓 Course Interested In *",
            [
                "BCA", "B.Com", "BBA",
                "B.Sc (Computer Science)", "B.Sc (Electronics)",
                "B.A. (Psychology)", "B.A. (Journalism)",
                "M.Com", "MBA", "Other"
            ]
        )

    message = st.text_area(
        "💬 Message (optional)",
        placeholder="Any question you want to ask?"
    )

    submitted = st.form_submit_button("🚀 Submit Enquiry")

    if submitted:
        if not name.strip() or not phone.strip():
            st.error("⚠️ Please fill in Name and Phone Number.")
        else:
            log_admission(name, phone, email, course, message)
            st.success(
                f"✅ Thank you, {name}! Your enquiry has been recorded. "
                "The college office will contact you soon."
            )
            st.balloons()

# ---------------- CHAT INPUT ----------------
question = st.chat_input("💬 Ask me anything about Sindhi College...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    typing_ph = st.empty()
    typing_ph.markdown(
        '<div class="typing-dots"><span></span><span></span><span></span></div>',
        unsafe_allow_html=True
    )
    answer = answer_question(question)
    typing_ph.empty()
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

# ---------------- FOOTER ----------------
st.divider()
st.caption("© 2026 Sindhi College Chatbot • Built with Streamlit + Groq AI")