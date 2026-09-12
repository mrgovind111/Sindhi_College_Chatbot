# 🎓 Sindhi College Chatbot

An AI-powered chatbot for Sindhi College, Bengaluru. Built with Streamlit, Groq AI, and a RAG (Retrieval-Augmented Generation) system that reads from a local college knowledge base.

## 🌐 Live Demo

https://sindhi-college-chatbot.streamlit.app

## ✨ Features

- **College Information** — Address, phone, email, affiliation, NAAC grade
- **Courses** — UG and PG courses offered
- **Admission** — Eligibility, documents, process
- **Staff Details** — Principal, Vice Principal, HODs, and faculty
- **Facilities** — Library, labs, sports, canteen, placement
- **Student FAQ** — Academic topics like Python, DBMS, SQL, Java, AI/ML
- **AI Fallback** — Free Groq AI answers questions outside the offline rules
- **RAG (Retrieval-Augmented Generation)** — AI reads college data before answering, so it never makes up fake names
- **Admin Dashboard** — Track top questions asked by students
- **Download Chat History** — Save the conversation as a text file

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | Groq (`openai/gpt-oss-120b`) |
| RAG | Python keyword search over `data/college_info.txt` |
| Hosting | Streamlit Cloud |
| Version Control | Git + GitHub |

## 📁 Project Structure
