# SINDHI COLLEGE CHATBOT — PRESENTATION SLIDES

**Total slides:** 14
**Duration:** 8–10 minutes
**Presenter:** [Your Name]

---

## SLIDE 1 — TITLE

**Title:** Sindhi College Chatbot
**Subtitle:** An AI-Powered Student Assistant

- Name: [Your Full Name]
- Register Number: [Your Register Number]
- Class: [Your Class]
- Guide: [Guide's Name]
- Academic Year: 2025 – 2026

---

## SLIDE 2 — INTRODUCTION

**What is the project?**

- A web-based chatbot for Sindhi College, Bengaluru
- Answers student queries instantly, 24/7
- Works on any device through a browser
- Uses free AI — no cost to the college

**Why it matters:**

- Reduces repetitive queries at the college office
- Gives students immediate answers
- Available outside office hours

---

## SLIDE 3 — PROBLEM STATEMENT

**Current challenges:**

- Students wait for office hours for basic information
- College staff answer hundreds of repetitive questions every admission season
- Information is spread across multiple web pages
- No conversational interface exists today

**Our solution:**

- One chatbot that answers all common questions
- Available anytime, on any device
- Uses the college's real data — no guessing

---

## SLIDE 4 — OBJECTIVES

1. Build a Streamlit-based chat interface
2. Store all college information in a structured file
3. Implement keyword rules for common questions
4. Integrate a free large language model (Groq)
5. Use RAG to prevent AI hallucination
6. Provide an admin dashboard for insights
7. Deploy on a free cloud platform
8. Maintain source code on GitHub

---

## SLIDE 5 — SYSTEM ARCHITECTURE

**Flow:**

1. User asks a question
2. Check offline rules first
3. If no match, use RAG + AI
4. Return answer

---

## SLIDE 6 — TECHNOLOGIES USED

| Component | Technology |
|---|---|
| Language | Python 3.13 |
| Web Framework | Streamlit |
| AI Provider | Groq (free) |
| AI Model | openai/gpt-oss-120b |
| RAG | Custom keyword search |
| Hosting | Streamlit Community Cloud |
| Version Control | Git + GitHub |

**All components are free-tier. Zero cost.**

---

## SLIDE 7 — KEY FEATURES

**For Students:**

- Instant chat interface
- 9 quick question buttons
- College info, courses, admission, staff
- Clickable Google Maps link
- Download chat history
- Feedback buttons (👍 / 👎)

**For Admin:**

- Password-protected dashboard
- Total questions counter
- Top 10 questions list
- Feedback statistics
- Question and feedback charts
- Admission enquiry list

---

## SLIDE 8 — RAG (Retrieval-Augmented Generation)

**Problem:** AI models can invent fake facts (hallucination).

**Example:** When asked "Who is the librarian?", a plain AI once
answered "Ms. Ayesha Patel" — a name that does not exist.

**Solution — RAG:**

1. Load `college_info.txt`
2. Split into chunks
3. For each question, find chunks with matching words
4. Send those chunks + question to the AI
5. AI answers using ONLY the provided context
6. If no match, AI replies "I do not have that information."

**Result:** Accurate answers, no fake names.

---

## SLIDE 9 — LIVE DEMONSTRATION

**Open the live app:**

https://sindhi-college-chatbot.streamlit.app

**Demo steps:**

1. Ask "Who is the principal?" → Dr. Asha N
2. Ask "Who is the librarian?" → Mr. Devaraju S
3. Ask "Where is the college?" → Address + map link
4. Ask "What is the capital of France?" → "I do not have that information."
5. Submit an admission enquiry
6. Click 👍 Helpful
7. Open Admin panel → show stats and charts

---

## SLIDE 10 — SCREENSHOTS

Add screenshots here:

1. **Home page** — banner + welcome card
2. **Chat in action** — question and answer
3. **Quick questions grid** — 9 buttons
4. **Admin dashboard** — top questions and stats
5. **Bar charts** — question analytics
6. **Mobile view** — app on phone
7. **Admission form** — filled form

---

## SLIDE 11 — RESULTS

| Test Case | Result |
|---|---|
| Principal query | ✅ Pass |
| Librarian query | ✅ Pass |
| Location query | ✅ Pass |
| Course query | ✅ Pass |
| Unknown query (France) | ✅ Pass — "I do not have that information." |
| Feedback logging | ✅ Pass |
| Admin login | ✅ Pass |
| Public deployment | ✅ Pass |

**All 8 test cases passed.**

---

## SLIDE 12 — ADVANTAGES

1. **Zero cost** — all services use free tiers
2. **Accurate** — RAG prevents fake answers
3. **Fast** — offline rules answer instantly
4. **Portable** — works on any browser
5. **Maintainable** — add info by editing one text file
6. **Insightful** — admin can see what students ask
7. **Scalable** — can be extended to other colleges

---

## SLIDE 13 — FUTURE SCOPE

1. **Bilingual answers** — English + Kannada
2. **Voice input** — speak your question
3. **WhatsApp integration** — chatbot on WhatsApp
4. **Student login** — personalised answers
5. **Multi-college support** — extend to other Sindhi institutions
6. **Analytics dashboard** — trends over time
7. **Mobile app** — native Android/iOS version

---

## SLIDE 14 — CONCLUSION & THANK YOU

**Summary:**

- Built a complete AI chatbot for Sindhi College
- Combines offline rules + free AI + RAG
- Zero cost, accurate, deployable
- Ready for real student use

**Live App:**
https://sindhi-college-chatbot.streamlit.app

**GitHub:**
https://github.com/mrgovind111/Sindhi_College_Chatbot

**Thank you!**

Questions?

---

## DESIGN TIPS

- **Background color:** Light blue or white
- **Heading color:** Dark blue (#1e3a8a — matches the app banner)
- **Font:** Calibri or Arial, size 24–28 for body
- **Slide numbers:** Bottom-right corner
- **Logo:** Add the Sindhi College logo to Slide 1
- **Screenshots:** Use a full-width layout for Slide 10

## TOOLS TO BUILD THE SLIDES

- **Microsoft PowerPoint** — free trial or college lab
- **Google Slides** — free at slides.google.com
- **Canva** — free templates at canva.com
- **LibreOffice Impress** — free open-source alternative

## SUGGESTED TIMING

| Slide | Time |
|---|---|
| 1–3 | 1.5 min |
| 4–6 | 2 min |
| 7–8 | 2 min |
| 9 (demo) | 3 min |
| 10–12 | 1.5 min |
| 13–14 | 1 min |
| **Total** | **~11 min** |