import os
from openai import OpenAI
from rag_helper import get_context
from analytics import log_question

# Works both locally and on Streamlit Cloud
try:
    import streamlit as st
    groq_key = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))
except Exception:
    groq_key = os.environ.get("GROQ_API_KEY")

client = OpenAI(
    api_key=groq_key,
    base_url="https://api.groq.com/openai/v1"
)


# Load college information
def load_college_info():
    with open("data/college_info.txt", "r", encoding="utf-8") as file:
        return file.read()


# Load student FAQ
def load_student_faq():
    with open("data/student_faq.txt", "r", encoding="utf-8") as file:
        return file.read()


college_info = load_college_info()
student_faq = load_student_faq()

last_topic = ""


# Answer student questions
def answer_question(question):
    global last_topic

    q = question.lower().strip()
    log_question(question)

    # Common words/phrases
    q = q.replace("college location", "location")
    q = q.replace("college address", "address")
    q = q.replace("where is sindhi college", "location")
    q = q.replace("where can i find the college", "location")
    q = q.replace("what courses are available", "courses")

    # College questions
    if "where" in q or "location" in q or "address" in q or "located" in q:
        last_topic = "college"
        return "Sindhi College is located at 33/2B, Kempapura, Hebbal, Bengaluru - 560024."

    elif "course" in q or "courses" in q or "program" in q or "programs" in q:
        last_topic = "college"
        return """Sindhi College offers:

UG Courses:
• BCA
• B.Com
• BBA
• B.Sc
• B.A

PG Courses:
• M.Com
• MBA"""

    elif "admission" in q or "eligibility" in q:
        last_topic = "college"
        return """For UG admission, students should have passed 10+2 / II PUC or equivalent.

Admission is generally merit-based."""

    elif "document" in q or "documents" in q:
        last_topic = "college"
        return """Documents commonly required:
• 10th marks card
• 12th / II PUC marks card
• Student Aadhaar card
• Passport-size photograph"""

    elif "facility" in q or "facilities" in q or "campus" in q:
        last_topic = "college"
        return """College facilities include:
• Wi-Fi
• Computer labs
• Library
• Seminar halls
• Auditorium
• Indoor sports stadium
• Canteen
• Placement and career guidance"""

    elif "affiliation" in q or "university" in q:
        last_topic = "college"
        return "Sindhi College is affiliated with Bengaluru City University (BCU)."

    elif "naac" in q or "accreditation" in q:
        last_topic = "college"
        return "Sindhi College is NAAC Accredited with B++ Grade."

    # Student FAQ questions
    elif "python" in q:
        last_topic = "python"
        return "Python is a high-level programming language used for developing applications, websites, automation and data analysis."

    elif "dbms" in q or "database management" in q:
        last_topic = "dbms"
        return """DBMS stands for Database Management System.

It is software used to store, manage and retrieve data from databases."""

    elif "sql" in q:
        last_topic = "sql"
        return """SQL stands for Structured Query Language.

It is used to create, read, update and delete data in databases."""

    elif "java" in q:
        last_topic = "java"
        return "Java is a high-level, object-oriented programming language used to develop applications."

    elif "artificial intelligence" in q or q == "ai" or "what is ai" in q:
        last_topic = "ai"
        return "Artificial Intelligence (AI) is a technology that enables computers to perform tasks that normally require human intelligence."

    elif "machine learning" in q or "machinelearning" in q:
        last_topic = "machine learning"
        return "Machine Learning is a branch of AI where computers learn patterns from data and make predictions or decisions."

    elif "html" in q and "css" not in q:
        last_topic = "html"
        return """HTML stands for HyperText Markup Language.

It is used to create the structure of web pages."""

    elif "css" in q and "html" not in q:
        last_topic = "css"
        return """CSS stands for Cascading Style Sheets.

It is used to style and design web pages."""

    elif "html" in q and "css" in q:
        last_topic = "html css"
        return "HTML creates the structure of a webpage, while CSS controls its design, layout and appearance."

    elif "algorithm" in q:
        last_topic = "algorithm"
        return "An algorithm is a step-by-step procedure used to solve a problem."

    elif "computer network" in q or "network" in q:
        last_topic = "network"
        return "A computer network is a group of connected computers that communicate and share resources."

    elif "normalization" in q:
        last_topic = "normalization"
        return "Normalization is a database process used to organize data and reduce data redundancy."

    elif "operating system" in q or q == "os":
        last_topic = "operating system"
        return "An operating system is system software that manages computer hardware and software resources."

    elif "oops" in q or "oop" in q or "object oriented" in q:
        last_topic = "oop"
        return """OOP stands for Object-Oriented Programming.

It is a programming approach based on objects and classes."""

    elif "data structure" in q:
        last_topic = "data structure"
        return "A data structure is a way of organizing and storing data so that it can be used efficiently."

    elif "cyber security" in q or "cybersecurity" in q:
        last_topic = "cyber security"
        return "Cyber security is the practice of protecting computers, networks and data from unauthorized access and cyber attacks."

    elif "subjects" in q and "bca" in q:
        last_topic = "bca"
        return """BCA commonly includes:
• Programming
• DBMS
• Computer Networks
• Operating Systems
• Java
• Python
• Web Technology
• Software Engineering"""

    elif "bca" in q:
        last_topic = "bca"
        return """BCA stands for Bachelor of Computer Applications.

It is an undergraduate degree related to computer applications and information technology."""

    elif "hello" in q or "hi" in q or "hey" in q:
        return "Hello! 👋 Welcome to Sindhi College Chatbot. How can I help you?"
    elif "principal" in q or "pricipal" in q or "head of college" in q:
        last_topic = "principal"
        return """The Principal of Sindhi College is Dr. Asha N.

Qualifications: M.Com, MBA, M.Phil, Ph.D
Designation: Principal"""
    elif "vice principal" in q or "viceprincipal" in q or "vice principal" in q:
        last_topic = "staff"
        return """The Vice Principal of Sindhi College is Dr. Sashikala U.

Qualifications: MBA, PGDHRM, Ph.D
Designation: Vice Principal"""

    elif "librarian" in q or "library head" in q:
        last_topic = "staff"
        return """The Chief Librarian of Sindhi College is Mr. Devaraju S.

Qualifications: MLISC, MA, M.Phil
Designation: Chief Librarian"""

    elif "staff" in q or "faculty" in q or "professors" in q or "teachers" in q:
        last_topic = "staff"
        return """Sindhi College has a team of 60+ qualified faculty members.

Key Staff:
• Principal: Dr. Asha N (M.Com, MBA, M.Phil, Ph.D)
• Vice Principal: Dr. Sashikala U (MBA, PGDHRM, Ph.D)
• Chief Librarian: Mr. Devaraju S (MLISC, MA, M.Phil)

The college has experienced professors, associate professors, and assistant professors across departments including Commerce, Computer Science, Management, Arts, and Sciences."""

    # If no FAQ answer matches, use AI
    else:
        return ask_ai(question)


# ---------- AI FALLBACK (Groq) ----------
def ask_ai(question):
    context = get_context(question)
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant for Sindhi College. "
                        "Answer the question using ONLY the context below. "
                        "If the answer is not in the context, reply exactly: "
                        "'I do not have that information.'\n\n"
                        f"Context:\n{context}"
                    )
                },
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return "Sorry, I could not reach the AI service right now."

# Test chatbot in PowerShell
if __name__ == "__main__":
    print("======================================")
    print("       SINDHI COLLEGE CHATBOT")
    print("======================================")
    print("Type 'exit' to stop.")
    print()

    while True:
        question = input("Student: ")

        if question.lower().strip() == "exit":
            print("Chatbot: Goodbye!")
            break

        answer = answer_question(question)

        print("Chatbot:", answer)
        print()