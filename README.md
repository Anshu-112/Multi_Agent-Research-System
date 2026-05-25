🚀 ResearchMind — Multi-Agent AI Research System

A futuristic multi-agent AI research platform powered by LangChain, LangGraph, Mistral AI, Tavily, and Streamlit.
Designed to simulate collaborative AI agents capable of searching, scraping, writing, and critiquing research autonomously.

✨ Overview

ResearchMind is an advanced AI research workflow where multiple specialized agents work together in a coordinated pipeline:

🔍 Search Agent → Finds relevant information from the web
📄 Reader Agent → Scrapes and extracts deeper content
✍️ Writer Chain → Generates structured research reports
🧠 Critic Chain → Reviews and critiques the generated report

The entire workflow runs inside a modern Streamlit interface with a sleek cyberpunk-inspired UI.

🧠 Multi-Agent Workflow
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
⚡ Features

✅ Multi-Agent AI Workflow
✅ Tavily Web Search Integration
✅ Website Scraping with BeautifulSoup
✅ ReAct-style Agent Reasoning
✅ LangGraph + LCEL Pipelines
✅ AI-generated Research Reports
✅ Critic/Reviewer AI Feedback Loop
✅ Futuristic Streamlit UI
✅ Modular Architecture
✅ Mistral AI Integration
✅ Real-Time Pipeline Visualization

🏗️ Tech Stack
Category	Technology
🤖 LLM	Mistral AI
🧠 Agent Framework	LangChain
🔄 Orchestration	LangGraph
🌐 Search Engine	Tavily
🕷️ Web Scraping	BeautifulSoup
🎨 Frontend	Streamlit
🔗 Pipelines	LCEL
🐍 Language	Python
📂 Project Structure
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
⚙️ Installation
1️⃣ Clone the Repository
git clone <your-repository-url>
cd multi-agent-research-system
2️⃣ Create Virtual Environment
Windows
python -m venv .venv

Activate the environment:

.\.venv\Scripts\Activate.ps1
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory.

MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key


🚀 Run the Application
streamlit run app.py
🧩 Core Components
🔍 Search Agent

Responsible for:

Searching the web using Tavily
Finding reliable and recent sources
Passing search results to downstream agents
📄 Reader Agent

Responsible for:

Selecting the best source
Scraping webpages
Extracting meaningful content
✍️ Writer Chain

Responsible for:

Analyzing collected information
Generating research reports
Structuring the final response
🧠 Critic Chain

Responsible for:

Reviewing generated reports
Providing AI feedback
Improving report quality
🎨 UI Highlights

ResearchMind features:

Futuristic dark-themed interface
Animated pipeline stages
Real-time agent progress
Cyberpunk-inspired gradients
Interactive report generation
Minimalist research dashboard

Built completely with Streamlit + Custom CSS.

🔬 Example Research Topics

Try prompts like:

Quantum Computing in Drug Discovery
Future of Artificial General Intelligence
Impact of AI on Cybersecurity
Climate Change and Renewable Energy
Latest Developments in Robotics
🌟 Future Improvements
Autonomous Planning Agents
Async Agent Execution
Memory Systems
Streaming Responses
Vector Databases
RAG Pipelines
PDF Research Export
Docker Deployment
Multi-User Support
Voice-based Research Assistant
📖 Learning Outcomes

This project helps in understanding:

AI Agents
LangChain
LangGraph
ReAct Architecture
LCEL Pipelines
Tool Calling
AI Workflow Orchestration
Web Scraping
Mistral AI Integration
Streamlit UI Design
⚠️ Important Notes
Never upload your .env
Keep API keys secure
Use virtual environments
Start with smaller workflows before scaling
👨‍💻 Author
Anshu Varma
📜 License

MIT License

⭐ Support

If you found this project helpful:

⭐ Star the repository
🍴 Fork the project
🚀 Build your own AI agents
🧠 Explore autonomous workflows
