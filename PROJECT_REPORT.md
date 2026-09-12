# SINDHI COLLEGE CHATBOT
## An AI-Powered Student Assistant

---

**Project Report**

Submitted in partial fulfilment of the requirements for the award of the degree of

**Bachelor of Computer Applications (BCA)**

**Sindhi College, Bengaluru**

**Affiliated to Bangalore City University**

**Academic Year: 2025 – 2026**

---

**Submitted by:**

Name: [Your Full Name]
Register Number: [Your Register Number]
Class: [Your Class and Section]

**Under the guidance of:**

[Guide's Name and Designation]

---

## ABSTRACT

The Sindhi College Chatbot is an AI-powered web application designed to help
students, parents, and prospective applicants get instant answers to common
questions about Sindhi College, Bengaluru. The chatbot combines rule-based
keyword matching with a free large language model (Groq's GPT-OSS-120B) and a
lightweight Retrieval-Augmented Generation (RAG) system that reads from a local
knowledge base of college information.

The application is built using Streamlit for the user interface, OpenAI's Python
SDK to communicate with the Groq API, and plain Python for the RAG logic. It is
deployed on Streamlit Community Cloud and version-controlled on GitHub. The
system provides answers about courses, admission, facilities, staff details,
location, and academic topics, while maintaining a zero-cost operation using
free-tier services.

The chatbot also includes an admin dashboard for tracking frequently asked
questions and collecting student feedback, making it useful for the college
administration as well.

---

## 1. INTRODUCTION

### 1.1 Background

Colleges receive hundreds of repetitive queries every admission season —
questions about courses, fees, eligibility, documents, timings, and location.
Answering these individually consumes staff time and delays student responses.
A chatbot that provides instant, accurate, round-the-clock answers reduces this
load significantly.

### 1.2 Motivation

Sindhi College has an active online presence but no conversational interface for
student queries. Students often wait for office hours or search through multiple
web pages. An AI-powered chatbot solves this problem with a single interface.

### 1.3 Problem Statement

To design and develop a chatbot for Sindhi College that:

- Answers student queries accurately and instantly
- Uses the college's real information (not guessed answers)
- Works on any device through a web browser
- Runs at zero cost using free-tier AI services
- Provides administrators with insights into what students ask

---

## 2. OBJECTIVES

1. Build a web-based chatbot interface using Streamlit
2. Store and manage college information in a structured text file
3. Implement rule-based keyword matching for common queries
4. Integrate a free large language model for open-ended questions
5. Use Retrieval-Augmented Generation (RAG) to prevent AI hallucinations
6. Provide an admin dashboard for monitoring questions and feedback
7. Deploy the application on a public cloud platform
8. Maintain the source code on GitHub for collaboration and version control

---

## 3. SYSTEM ARCHITECTURE

### 3.1 High-Level Architecture
