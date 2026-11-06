# 🧠 ResearchMind: Multi-Agent AI Research System

ResearchMind is an advanced, fully autonomous AI research pipeline built with **LangChain (LCEL)** and **Streamlit**. It uses a team of 4 specialized agents to search the web, scrape deep content, draft a structured report, and critique its own work—delivering a polished research document on any topic in seconds.

<img width="1912" height="833" alt="image" src="https://github.com/user-attachments/assets/b582938b-beab-4cf6-927f-3917e3fc33bc" />


## 🚀 Live Demo
Experience it live here: https://researchmind-multiagentai.streamlit.app/

## ✨ Features
*   **Real-time Web Search:** Uses Tavily API to find recent and reliable information.
*   **Deep Web Scraping:** Custom BeautifulSoup tool extracts clean text from top URLs.
*   **Sequential LCEL Pipeline:** Agents hand off context to the next step using LangChain Expression Language.
*   **Self-Correction (Critic Agent):** The final report is reviewed by an AI Critic that scores it out of 10 and suggests improvements.
*   **Bring Your Own Key (BYOK):** A sleek, secure sidebar allows users to input their own Groq and Tavily API keys without hardcoding secrets.
*   **Premium UI:** Features custom CSS, dynamic pipeline tracking (Waiting → Running → Done), glassmorphism cards, and markdown report downloading.

## 🏗️ System Architecture

The pipeline operates in a sequential, 4-step workflow:

1. **🔍 Search Agent (Tool Calling):** Takes the user's topic and uses `web_search` to find titles, URLs, and snippets.
2. **📄 Reader Agent (Tool Calling):** Analyzes the search results, selects the most relevant URL, and uses `scrape_url` to extract deep content (up to 3,000 characters).
3. **✍️ Writer Chain (LCEL):** Combines the search results and the scraped content to draft a detailed, structured research report.
4. **🧐 Critic Chain (LCEL):** Reviews the report and provides a strict evaluation (Score, Strengths, Areas to Improve).

## 🛠️ Tech Stack
*   **Framework:** Streamlit, LangChain
*   **LLM:** Llama 3.3 70B (via Groq API for lightning-fast inference)
*   **Tools:** Tavily API (Search), BeautifulSoup (Scraping)
*   **Language:** Python 3.11+

## 💻 Installation & Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/laxmijin11-cyber/researchmind-multi-agent-research-agent.git
   cd researchmind-multi-agent-research-agent
