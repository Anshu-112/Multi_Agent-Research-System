import streamlit as st
import time
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind · Multi-Agent AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
    color: #e8e6e1 !important;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none; }

/* ── Hero ── */
.hero-wrapper {
    text-align: center;
    padding: 3rem 1rem 2rem;
}
.hero-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.25em;
    color: #5eff8f;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 6vw, 4.2rem);
    font-weight: 800;
    line-height: 1.05;
    background: linear-gradient(135deg, #ffffff 0%, #5eff8f 60%, #00c9ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.6rem;
}
.hero-sub {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 300;
    color: #888;
    max-width: 480px;
    margin: 0 auto 2rem;
    line-height: 1.6;
}

/* ── Pipeline visual ── */
.pipeline-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0;
    margin: 0 auto 2.5rem;
    max-width: 700px;
    flex-wrap: wrap;
    gap: 0.4rem;
}
.pipe-step {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: #13131a;
    border: 1px solid #222230;
    border-radius: 6px;
    padding: 0.4rem 0.85rem;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: #555;
    white-space: nowrap;
}
.pipe-step .dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #333;
    flex-shrink: 0;
}
.pipe-step.active { border-color: #5eff8f44; color: #5eff8f; }
.pipe-step.active .dot { background: #5eff8f; box-shadow: 0 0 8px #5eff8f88; }
.pipe-sep { color: #2a2a3a; font-size: 1rem; padding: 0 0.2rem; }

/* ── Input area ── */
.stTextInput > div > div > input {
    background: #13131a !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 8px !important;
    color: #e8e6e1 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #5eff8f !important;
    box-shadow: 0 0 0 2px #5eff8f22 !important;
}
.stTextInput > div > div > input::placeholder { color: #444 !important; }

/* ── Button ── */
.stButton > button {
    background: linear-gradient(135deg, #5eff8f, #00c9ff) !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.7rem 2rem !important;
    width: 100% !important;
    transition: opacity 0.2s, transform 0.1s !important;
    cursor: pointer !important;
}
.stButton > button:hover { opacity: 0.88 !important; transform: translateY(-1px) !important; }
.stButton > button:active { transform: translateY(0) !important; }

/* ── Stage cards ── */
.stage-card {
    background: #13131a;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}
.stage-card::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: #2a2a3a;
    border-radius: 3px 0 0 3px;
}
.stage-card.done::before { background: #5eff8f; }
.stage-card.running::before {
    background: linear-gradient(180deg, #5eff8f, #00c9ff);
    animation: pulse-bar 1s ease-in-out infinite alternate;
}
@keyframes pulse-bar {
    from { opacity: 0.5; }
    to   { opacity: 1; }
}

.stage-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
}
.stage-icon {
    font-size: 1.1rem;
    width: 28px;
    text-align: center;
}
.stage-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.92rem;
    color: #e8e6e1;
    flex: 1;
}
.stage-badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    padding: 0.2rem 0.55rem;
    border-radius: 20px;
    background: #1e1e2e;
    color: #555;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.stage-badge.running { background: #1a2e1a; color: #5eff8f; }
.stage-badge.done    { background: #0f2e1a; color: #5eff8f; }

.stage-content {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    line-height: 1.65;
    color: #8a8a9a;
    max-height: 220px;
    overflow-y: auto;
    padding: 0.75rem;
    background: #0d0d14;
    border-radius: 6px;
    border: 1px solid #1a1a28;
    white-space: pre-wrap;
    word-break: break-word;
}
.stage-content::-webkit-scrollbar { width: 4px; }
.stage-content::-webkit-scrollbar-track { background: transparent; }
.stage-content::-webkit-scrollbar-thumb { background: #2a2a3a; border-radius: 4px; }

/* ── Report ── */
.report-wrapper {
    background: #13131a;
    border: 1px solid #5eff8f33;
    border-radius: 12px;
    padding: 1.8rem 2rem;
    margin-top: 1rem;
}
.report-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #5eff8f;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.report-body {
    font-family: 'Inter', sans-serif;
    font-size: 0.95rem;
    line-height: 1.75;
    color: #ccc;
    white-space: pre-wrap;
}

/* ── Feedback ── */
.feedback-wrapper {
    background: #131320;
    border: 1px solid #00c9ff33;
    border-radius: 12px;
    padding: 1.4rem 1.8rem;
    margin-top: 1rem;
}
.feedback-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    color: #00c9ff;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.feedback-body {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    line-height: 1.7;
    color: #aaa;
    white-space: pre-wrap;
}

/* ── Divider ── */
hr { border-color: #1e1e2e !important; margin: 1.5rem 0 !important; }

/* ── Spinner override ── */
[data-testid="stSpinner"] > div { color: #5eff8f !important; }

/* ── Expander ── */
details > summary {
    font-family: 'Syne', sans-serif;
    font-size: 0.88rem;
    color: #666;
    cursor: pointer;
}

/* ── Status text ── */
.status-line {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: #5eff8f;
    padding: 0.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.blink { animation: blink 0.9s step-end infinite; }
@keyframes blink { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)


# ── Helper: render stage card ────────────────────────────────────────────────
def stage_card(icon: str, title: str, badge: str, content: str, state: str, placeholder):
    badge_cls = state  # "idle" | "running" | "done"
    card_cls = state if state in ("running", "done") else ""
    placeholder.markdown(f"""
<div class="stage-card {card_cls}">
  <div class="stage-header">
    <div class="stage-icon">{icon}</div>
    <div class="stage-title">{title}</div>
    <span class="stage-badge {badge_cls}">{badge}</span>
  </div>
  {f'<div class="stage-content">{content}</div>' if content else ''}
</div>
""", unsafe_allow_html=True)


# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrapper">
  <div class="hero-eyebrow">Multi-Agent Research System</div>
  <div class="hero-title">ResearchMind</div>
  <div class="hero-sub">Four specialized AI agents working in concert — search, scrape, write, and critique.</div>
  <div class="pipeline-bar">
    <div class="pipe-step"><span class="dot"></span>Search Agent</div>
    <div class="pipe-sep">→</div>
    <div class="pipe-step"><span class="dot"></span>Reader Agent</div>
    <div class="pipe-sep">→</div>
    <div class="pipe-step"><span class="dot"></span>Writer Chain</div>
    <div class="pipe-sep">→</div>
    <div class="pipe-step"><span class="dot"></span>Critic Chain</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Input ────────────────────────────────────────────────────────────────────
col_l, col_mid, col_r = st.columns([1, 3, 1])
with col_mid:
    topic = st.text_input(
        "",
        placeholder="e.g.  Quantum computing in drug discovery",
        label_visibility="collapsed",
    )
    run_btn = st.button("⚡  Run Research Pipeline", use_container_width=True)

st.markdown("<hr/>", unsafe_allow_html=True)


# ── Pipeline execution ────────────────────────────────────────────────────────
if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    col_stages, col_output = st.columns([5, 7], gap="large")

    with col_stages:
        st.markdown("<p style='font-family:Syne,sans-serif;font-size:0.82rem;color:#555;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.75rem;'>Pipeline Stages</p>", unsafe_allow_html=True)
        ph_search  = st.empty()
        ph_reader  = st.empty()
        ph_writer  = st.empty()
        ph_critic  = st.empty()

    with col_output:
        st.markdown("<p style='font-family:Syne,sans-serif;font-size:0.82rem;color:#555;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.75rem;'>Output</p>", unsafe_allow_html=True)
        ph_report   = st.empty()
        ph_feedback = st.empty()

    # Initial idle state
    stage_card("🔍", "Search Agent",  "idle", "", "idle", ph_search)
    stage_card("📄", "Reader Agent",  "idle", "", "idle", ph_reader)
    stage_card("✍️",  "Writer Chain",  "idle", "", "idle", ph_writer)
    stage_card("🧠", "Critic Chain",  "idle", "", "idle", ph_critic)

    state = {}

    # ── Helper: safely coerce agent .content to plain str ───────────────────
    def to_str(value) -> str:
        """Convert whatever an agent returns (.content can be str or list) to str."""
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            parts = []
            for block in value:
                if isinstance(block, str):
                    parts.append(block)
                elif isinstance(block, dict):
                    parts.append(block.get("text", str(block)))
                else:
                    # LangChain content block objects
                    parts.append(getattr(block, "text", str(block)))
            return "\n".join(parts)
        return str(value)

    # ── Step 1 – Search ──────────────────────────────────────────────────────
    stage_card("🔍", "Search Agent", "running", "Searching the web...", "running", ph_search)
    with col_output:
        ph_report.markdown("<div class='status-line'><span class='blink'>▋</span> Waiting for search results…</div>", unsafe_allow_html=True)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = to_str(search_result["messages"][-1].content)

    preview_search = state["search_results"][:600] + ("…" if len(state["search_results"]) > 600 else "")
    stage_card("🔍", "Search Agent", "done", preview_search, "done", ph_search)

    # ── Step 2 – Reader ──────────────────────────────────────────────────────
    stage_card("📄", "Reader Agent", "running", "Scraping top resource…", "running", ph_reader)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })
    state["scraped_content"] = to_str(reader_result["messages"][-1].content)

    preview_reader = state["scraped_content"][:600] + ("…" if len(state["scraped_content"]) > 600 else "")
    stage_card("📄", "Reader Agent", "done", preview_reader, "done", ph_reader)

    # ── Step 3 – Writer ──────────────────────────────────────────────────────
    stage_card("✍️",  "Writer Chain", "running", "Drafting the report…", "running", ph_writer)
    ph_report.markdown("<div class='status-line'><span class='blink'>▋</span> Writing report…</div>", unsafe_allow_html=True)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )
    raw_report = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })
    state["report"] = to_str(raw_report)

    stage_card("✍️",  "Writer Chain", "done", "Report generated successfully.", "done", ph_writer)
    ph_report.markdown(f"""
<div class="report-wrapper">
  <div class="report-label">📋 Final Report</div>
  <div class="report-body">{state["report"]}</div>
</div>
""", unsafe_allow_html=True)

    # ── Step 4 – Critic ──────────────────────────────────────────────────────
    stage_card("🧠", "Critic Chain", "running", "Reviewing the report…", "running", ph_critic)
    ph_feedback.markdown("<div class='status-line'><span class='blink'>▋</span> Generating critique…</div>", unsafe_allow_html=True)

    raw_feedback = critic_chain.invoke({"report": state["report"]})
    state["feedback"] = to_str(raw_feedback)

    stage_card("🧠", "Critic Chain", "done", "Critique complete.", "done", ph_critic)
    ph_feedback.markdown(f"""
<div class="feedback-wrapper">
  <div class="feedback-label">🧠 Critic Feedback</div>
  <div class="feedback-body">{state["feedback"]}</div>
</div>
""", unsafe_allow_html=True)

    # ── Done banner ──────────────────────────────────────────────────────────
    st.success("✅  Pipeline complete! All four agents have finished.", icon=None)