import streamlit as st
from google import genai
from prompts import PROMPT_MAP

# --- Page Config ---
st.set_page_config(page_title="AI Study Buddy", page_icon="🎓", layout="wide")

# --- Custom Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .header {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 2rem; border-radius: 16px;
        text-align: center; margin-bottom: 2rem;
    }
    .header h1 { color: white; font-size: 2.2rem; margin: 0; }
    .header p { color: rgba(255,255,255,0.85); font-size: 1.05rem; margin-top: 0.5rem; }
    .output-box {
        background: #1a1a2e; border: 1px solid #2a2a4a;
        border-radius: 12px; padding: 1.5rem;
        color: #e0e0e0; line-height: 1.8; white-space: pre-wrap;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white; border: none; border-radius: 10px;
        padding: 0.6rem 2rem; font-weight: 600; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div class="header">
    <h1>🎓 AI Study Buddy</h1>
    <p>Smart Exam Preparation Assistant</p>
</div>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Gemini API Key", type="password")
    st.divider()
    difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"], index=1)
    mode = st.radio("Generation Mode", list(PROMPT_MAP.keys()))
    st.divider()
    st.caption("Built with Streamlit + Gemini API")

# --- Input ---
subject = st.text_input("📚 Subject Name", placeholder="e.g. Data Structures, Physics")
notes = st.text_area("📄 Paste your notes / syllabus", height=200,
                      placeholder="Paste your class notes or syllabus topics here...")
generate = st.button("✨ Generate Study Material")

# --- Generate Output ---
if generate:
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not subject or not notes:
        st.error("Please enter both subject name and notes.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt_fn = PROMPT_MAP[mode]
            prompt = prompt_fn(subject, difficulty, notes)

            with st.spinner("Generating study material..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.subheader(f"📄 {mode}")
            st.markdown(f'<div class="output-box">{response.text}</div>',
                        unsafe_allow_html=True)

            st.download_button(
                "📥 Download as Text", data=response.text,
                file_name=f"{subject}_{mode.replace(' ', '_').lower()}.txt"
            )
        except Exception as e:
            st.error(f"Error: {str(e)}")
