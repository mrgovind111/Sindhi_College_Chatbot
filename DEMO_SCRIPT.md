# SINDHI COLLEGE CHATBOT — DEMO SCRIPT

**Duration:** 5–7 minutes
**Presenter:** [Your Name]
**Project:** Sindhi College Chatbot — AI-Powered Student Assistant

---

## 1. OPENING (30 seconds)

> "Good morning/afternoon, respected teachers. My name is [Your Name]
> and my project is the **Sindhi College Chatbot** — an AI-powered
> student assistant for our college.
>
> The goal of this project is to give students, parents, and
> prospective applicants instant answers to common college questions
> — any time, on any device — using a free AI service."

---

## 2. PROBLEM STATEMENT (30 seconds)

> "Every admission season, the college office receives hundreds of
> repetitive questions about courses, fees, admission documents,
> timings, and location. Answering each one takes staff time.
>
> Students often wait for office hours or search through multiple
> web pages to find answers.
>
> My project solves this with a single chatbot that answers all
> these questions instantly."

---

## 3. LIVE DEMONSTRATION (3 minutes)

### 3.1 Open the app

- Open the browser and go to:
  **https://sindhi-college-chatbot.streamlit.app**
- Say:
  > "This is the live application, hosted for free on Streamlit Cloud."

### 3.2 Show the interface

- Point to the **banner** at the top
- Point to the **sidebar** with college contact information
- Point to the **quick question buttons**
- Say:
  > "The interface is clean and works on both desktop and mobile."

### 3.3 Ask a college question

- In the chat box, type:
  **"Who is the principal?"**
- The answer appears: **Dr. Asha N** with qualifications.
- Say:
  > "The chatbot has an offline rule for common questions, so it
  > answers instantly without using any AI."

### 3.4 Ask another college question

- Type:
  **"Who is the librarian?"**
- Answer appears: **Mr. Devaraju S**
- Say:
  > "For any question about our college, the chatbot uses a technique
  > called **RAG — Retrieval-Augmented Generation**. It reads our
  > college knowledge file first, then answers using only that data.
  > This means the AI **cannot make up fake names**."

### 3.5 Ask a general academic question

- Type:
  **"What is Python?"**
- Answer appears with a definition.
- Say:
  > "For general academic topics like Python, DBMS, or Java, the
  > chatbot answers from a built-in FAQ."

### 3.6 Ask an unknown question

- Type:
  **"What is the capital of France?"**
- Answer appears: **"I do not have that information."**
- Say:
  > "This is important — the chatbot only answers about our college.
  > It does not guess or make up facts."

### 3.7 Click the location quick button

- Click **📍 Location**.
- Answer appears with the address and a **clickable Google Maps link**.
- Say:
  > "The location answer includes a direct Google Maps link."

### 3.8 Submit the admission enquiry form

- Scroll down to the **📝 Admission Enquiry** form.
- Enter a test name, phone, and pick a course.
- Click **Submit Enquiry**.
- Say:
  > "Prospective students can submit their details directly through
  > the chatbot. The college office can see these enquiries in the
  > admin panel."

### 3.9 Use the feedback buttons

- Click **👍 Helpful** below the last answer.
- Say:
  > "Students can rate each answer. This helps us improve the system."

### 3.10 Download chat history

- In the sidebar, click **📥 Download Chat History**.
- Say:
  > "Students can save their conversation for later reference."

---

## 4. ADMIN DASHBOARD (1 minute)

- In the sidebar, scroll to **🔐 Admin**.
- Enter the password: **[your admin password]** (do not say it out loud if others are listening — just type it).
- Say:
  > "The admin panel is password-protected."

Point to each section:

1. **Total questions asked**
   > "The admin can see how many questions have been asked."

2. **Top 10 questions**
   > "The most frequently asked questions are listed, so the college
   > knows what students care about."

3. **📊 Feedback Stats**
   > "The helpful rate shows how well the chatbot is performing."

4. **📝 Admission Enquiries**
   > "All submitted enquiries appear here for follow-up."

5. **📈 Question Analytics chart**
   > "A bar chart shows question counts at a glance."

6. **🥧 Feedback Breakdown chart**
   > "A second chart shows helpful vs not helpful feedback."

---

## 5. TECHNICAL OVERVIEW (1 minute)

> "The project uses the following technologies:"

| Component | Technology |
|---|---|
| Frontend | Streamlit (Python web framework) |
| AI Model | Groq API — model `openai/gpt-oss-120b` (free) |
| RAG | Custom Python keyword search over `college_info.txt` |
| Hosting | Streamlit Community Cloud (free) |
| Version Control | Git + GitHub |

> "The entire project runs on **free-tier services**. No payment is
> needed. The API key is stored securely in Streamlit Secrets, not
> in the code."

---

## 6. SOURCE CODE (30 seconds)

- Open: **https://github.com/mrgovind111/Sindhi_College_Chatbot**
- Say:
  > "The complete source code is on GitHub. The repository includes
  > a README, a project report, and all the Python files."

Show the file list:

- `app.py` — the Streamlit UI
- `chatbot.py` — the answer logic
- `rag_helper.py` — the RAG search
- `analytics.py` — logging and feedback
- `data/college_info.txt` — the knowledge base

---

## 7. FUTURE SCOPE (30 seconds)

> "In the future, I plan to add:"

1. **Kannada answers** — bilingual support
2. **Voice input** — students can speak their question
3. **WhatsApp integration** — chatbot on WhatsApp
4. **Student login** — personalised answers
5. **Analytics dashboard** — trends over time

---

## 8. CLOSING (30 seconds)

> "To summarise — the Sindhi College Chatbot is a working AI
> application that answers student queries accurately, at zero cost,
> on any device. It demonstrates the combined use of large language
> models, Retrieval-Augmented Generation, and cloud hosting.
>
> Thank you. I am happy to answer any questions."

---

## COMMON QUESTIONS YOU MAY BE ASKED

**Q: Does this chatbot cost anything to run?**
> A: No. It uses Groq's free API tier and Streamlit Cloud's free
> hosting. Zero cost.

**Q: How does the chatbot avoid giving wrong answers?**
> A: It uses RAG. Before answering, it reads our college knowledge
> file. If the answer is not in the file, it replies
> "I do not have that information."

**Q: Can it answer in Kannada?**
> A: Not yet. That is planned for future scope.

**Q: How do you add new information?**
> A: Just edit `data/college_info.txt` on GitHub. The chatbot uses
> the new information on the next run.

**Q: What if the AI service goes down?**
> A: The chatbot has offline rules for common questions, so those
> still work. Only the AI fallback is affected.

**Q: Can you show the code?**
> A: Yes — open the GitHub repository and show `chatbot.py` and
> `rag_helper.py`.

---

**END OF SCRIPT**