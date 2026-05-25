# 🚀 ResearchMind — Multi-Agent AI Research System

> A futuristic multi-agent AI research platform powered by **LangChain**, **LangGraph**, **Mistral AI**, **Tavily**, and **Streamlit**.

ResearchMind simulates a collaborative AI ecosystem where multiple intelligent agents work together to:

* 🌐 Search the web
* 🕷️ Scrape websites
* 🧠 Analyze information
* ✍️ Generate research reports
* 🔍 Critique and improve outputs

---

## ✨ Features

* ✅ Multi-Agent AI Workflow
* ✅ Tavily Web Search Integration
* ✅ Website Scraping with BeautifulSoup
* ✅ ReAct-style Agent Reasoning
* ✅ LangGraph + LCEL Pipelines
* ✅ AI-generated Research Reports
* ✅ Critic/Reviewer AI Feedback Loop
* ✅ Futuristic Streamlit UI
* ✅ Modular Architecture
* ✅ Mistral AI Integration
* ✅ Real-Time Pipeline Visualization

---

## 🧠 Multi-Agent Workflow

```text
User Query
    ↓
🔍 Search Agent
    ↓
📄 Reader Agent
    ↓
✍️ Writer Chain
    ↓
🧠 Critic Chain
    ↓
📋 Final Research Report
```

---

## 🏗️ Tech Stack

| Category           | Technology    |
| ------------------ | ------------- |
| 🤖 LLM             | Mistral AI    |
| 🧠 Agent Framework | LangChain     |
| 🔄 Orchestration   | LangGraph     |
| 🌐 Search Engine   | Tavily        |
| 🕷️ Web Scraping   | BeautifulSoup |
| 🎨 Frontend        | Streamlit     |
| 🔗 Pipelines       | LCEL          |
| 🐍 Language        | Python        |

---

## 📂 Project Structure

```bash
multi-agent-research-system/
│
├── agents.py
├── tools.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd multi-agent-research-system
```

---

### 2️⃣ Create Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.\.venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🚀 Run the Application

```bash
streamlit run app.py
```

---

## 🧩 Core Components

### 🔍 Search Agent

Responsible for:

* Searching the web using Tavily
* Finding reliable sources
* Collecting research information

---

### 📄 Reader Agent

Responsible for:

* Selecting the best source
* Scraping webpage content
* Extracting meaningful information

---

### ✍️ Writer Chain

Responsible for:

* Analyzing collected information
* Generating structured reports
* Producing final research outputs

---

### 🧠 Critic Chain

Responsible for:

* Reviewing generated reports
* Providing AI feedback
* Improving report quality

---

## 🎨 UI Highlights

ResearchMind includes:

* Futuristic dark-themed interface
* Animated pipeline stages
* Real-time agent visualization
* Cyberpunk-inspired design
* Interactive research dashboard

Built completely using **Streamlit + Custom CSS**.

---

## 🔬 Example Research Topics

Try prompts like:

```text
Quantum Computing in Drug Discovery
Future of Artificial General Intelligence
Impact of AI on Cybersecurity
Climate Change and Renewable Energy
Latest Developments in Robotics
```

---

## 🌟 Future Improvements

* Autonomous Planning Agents
* Async Agent Execution
* Memory Systems
* Streaming Responses
* Vector Databases
* RAG Pipelines
* PDF Report Generation
* Docker Deployment
* Voice-based Research Assistant

---

## 📖 Learning Outcomes

This project helps in understanding:

* AI Agents
* LangChain
* LangGraph
* LCEL Pipelines
* ReAct Architecture
* Tool Calling
* Workflow Orchestration
* Web Scraping
* Mistral AI Integration
* Streamlit UI Design

---

## ⚠️ Important Notes

* Never upload your `.env`
* Keep API keys secure
* Use virtual environments
* Start simple and scale gradually

---

## 👨‍💻 Author

### Anshu Varma

---

## 📜 License

MIT License

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🚀 Build your own AI agents
* 🧠 Explore autonomous workflows
