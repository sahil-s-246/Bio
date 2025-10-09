import streamlit as st
import random

# Page config
st.set_page_config(page_title="Sahil Parupudi - Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(120deg, #57068c 0%, #330662 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #57068c;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #57068c;
        padding-bottom: 0.5rem;
    }
    .experience-card {
        background: linear-gradient(135deg, #57068c 0%, #330662 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    .skill-tag {
        display: inline-block;
        background: #57068c;
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
    }
    .hobby-card {
        background: #f8f5ff;
        border-left: 4px solid #57068c;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Humorous quotes
humorous_quotes = [
    "Data is the new oil. But unlike oil, it doesn't cause pollution... just confusion. — Unknown",
    "Machine learning is like teenage sex: everyone talks about it, nobody really knows how to do it. — Unknown",
    "My model has 99 problems, but overfitting ain't one... oh wait, it is. — Data Scientist",
    "I'm not arguing, I'm just explaining why my p-value is significant. — Statistician",
    "In data science, garbage in, garbage out. But with enough preprocessing, garbage in, insights out! — Unknown",
    "Neural networks are basically fancy curve fitting with extra steps and GPU costs. — ML Engineer",
    "The only difference between screwing around and science is writing it down. — Adam Savage",
    "My code works! I have no idea why. — Every Data Scientist",
    "There are 10 types of people: those who understand binary and those who don't. — Unknown",
    "Artificial intelligence is no match for natural stupidity. — Unknown",
    "Feature engineering: the art of making your data confess what you want to hear. — Unknown",
    "I have a model with 99% accuracy. It predicts everything as the majority class. — Unknown",
    "Correlation does not imply causation, but it does waggle its eyebrows suggestively. — xkcd",
    "A data scientist is someone who knows more statistics than a programmer and more programming than a statistician. — Josh Wills",
    "The best thing about a Boolean is even if you are wrong, you're only off by a bit. — Unknown",
    "Debugging: Being the detective in a crime movie where you're also the murderer. — Filipe Fortes",
    "99 little bugs in the code, take one down, patch it around, 127 little bugs in the code. — Unknown",
    "To err is human, to really foul things up requires a computer. — Paul Ehrlich",
    "If it's not documented, it didn't happen. If it is documented, nobody read it anyway. — Unknown",
    "The cloud is just someone else's computer that you pay way too much for. — Unknown"
]

st.toast(random.choice(humorous_quotes), icon="✨")

# Header Section
st.markdown('<h1 class="main-header">👋 Hi, I\'m Sahil Parupudi</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">MS Data Science Student @ NYU | AI/ML Enthusiast | Building intelligent systems</p>',
            unsafe_allow_html=True)

# Contact Section
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("🔗 GitHub", "https://github.com/sahil-s-246", use_container_width=True)
with col2:
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/sahilparupudi", use_container_width=True)
with col3:
    st.link_button("📧 Email", "mailto:sahilsrinivas3@gmail.com", use_container_width=True)
with col4:
    st.link_button("📄 Resume", "https://sahil-s-246.github.io/autoCV", use_container_width=True)

st.markdown("---")

# Education Section
st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.markdown("**New York University | Centre for Data Science**")
        st.markdown("*MS Data Science - Industry Concentration*")
        st.caption("📅 Sep 2025 - May 2027")

with col2:
    with st.container(border=True):
        st.markdown("**Dr. D.Y. Patil Institute of Technology, Pimpri**")
        st.markdown("*B.E. Computer Engineering*")
        st.caption("📅 Sep 2021 - Jun 2025")

# Experience Section
st.markdown('<h2 class="section-header">💼 Experience</h2>', unsafe_allow_html=True)

with st.container(border=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### **XDE Studios**")
        st.markdown("*AI/ML Intern*")
    with col2:
        st.markdown("**Oct 2024 - Aug 2025**")
        st.caption("📍 Pune, India")

    st.markdown("""
    - Fine-tuned **YOLOv11** for shipping container (95% recall) and seal number detection (75% recall) with PaddleOCR integration
    - Built scalp image analysis tool with **EfficientNet** for hair density classification (92% accuracy) and YOLOv8 for dandruff detection
    - Developed face recognition pipeline using **InsightFace** and **HDBSCAN** clustering (0.70 silhouette score), deployed on Digital Ocean
    - Designed 360° panorama capture app with photo stitching algorithms
    - Implemented comic generation pipeline via **Stable Diffusion + Gemini APIs**, containerized with Docker and deployed on GCP VM
    """)

st.markdown("")

with st.container(border=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### **Rubiscape**")
        st.markdown("*Project Intern - Data Science*")
    with col2:
        st.markdown("**Jun 2024 - Sep 2024**")
        st.caption("📍 Pune, India")

    st.markdown("""
    - Performed customer segmentation using **K-means clustering** on RFM, product types, and geography (0.65 silhouette score)
    - Developed **Random Forest** model for Employee Attrition prediction (89% accuracy)
    - Created end-to-end workflows for ML models on Rubistudio platform
    """)

# Technical Skills Section
st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("**Programming Languages**")
        skills = ["Python", "Java", "C++"]
        st.markdown(" ".join([f'<span class="skill-tag">{skill}</span>' for skill in skills]), unsafe_allow_html=True)

        st.markdown("**ML/DL Frameworks**")
        libs = ["PyTorch", "Transformers", "Ultralytics", "Scikit-Learn", "TensorFlow"]
        st.markdown(" ".join([f'<span class="skill-tag">{lib}</span>' for lib in libs]), unsafe_allow_html=True)

        st.markdown("**Development Tools**")
        tools = ["FastAPI", "Streamlit", "React", "LangChain", "Docker"]
        st.markdown(" ".join([f'<span class="skill-tag">{tool}</span>' for tool in tools]), unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        st.markdown("**Data & Vector DBs**")
        dbs = ["Weaviate", "ChromaDB", "MongoDB", "MySQL", "Pandas"]
        st.markdown(" ".join([f'<span class="skill-tag">{db}</span>' for db in dbs]), unsafe_allow_html=True)

        st.markdown("**Cloud & DevOps**")
        cloud = ["GCP", "Digital Ocean", "GitHub Actions", "Docker", "Git"]
        st.markdown(" ".join([f'<span class="skill-tag">{tool}</span>' for tool in cloud]), unsafe_allow_html=True)

        st.markdown("**Computer Vision**")
        cv = ["YOLOv11", "EfficientNet", "InsightFace", "OpenCV", "PaddleOCR"]
        st.markdown(" ".join([f'<span class="skill-tag">{tool}</span>' for tool in cv]), unsafe_allow_html=True)

# Projects Section
st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🍽️ Restaurant Menu Dish Recommendation")
        st.markdown("*React, Weaviate, FastAPI*")
        st.markdown("""
        - Hybrid recommendation engine using PyNNDescent-based collaborative filtering and Weaviate vector search
        - Integrated Gemini API for context-aware dish re-ranking based on preferences and dietary filters
        - Published paper on hybrid recommendation approaches
        """)

with col2:
    with st.container(border=True):
        st.markdown("### 🎨 IMagic")
        st.markdown("*Streamlit, Scikit-learn, Stability AI API*")
        st.markdown("""
        - Interactive image processing application with Streamlit interface
        - K-means clustering for image compression and size reduction
        - Integrated Gemini Stability and Stable Diffusion APIs for text extraction and generation
        """)

# Current Focus Section
st.markdown('<h2 class="section-header">🔬 Currently Exploring</h2>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🤖 Agentic AI Systems")
        st.markdown("""
        Diving deep into autonomous agents and multi-agent systems. Experimenting with fastmcp and exploring how agents can chain tools, maintain memory, and reason through complex tasks.
        """)

with col2:
    with st.container(border=True):
        st.markdown("### 📊 Real-time ML Pipelines")
        st.markdown("""
        Learning Mlflow and Pyspark and exploring how to scale ML Pipelines
        """)

# Beyond the Code Section
st.markdown('<h2 class="section-header">🌟 Beyond the Code</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="hobby-card">
    <h4>🏸 Badminton Enthusiast</h4>
    <p> You could probably find me at Brooklyn Badminton Center!</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="hobby-card">
        <h4>🎤 Conference & Seminar Regular</h4>
        <p>Attended NYU CILVR seminars, Text as Data workshops, 
        and various AI/ML conferences.Always fascinating to learn about new developments in the various subfields of Computer Science and intersections with CS like Computation Decision Making, NLP etc
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="hobby-card">
        <h4>🍰 Cheesecake Enthusiast</h4>
        <p> The best thing since sliced bread, arguably!</p>
    </div>
    """, unsafe_allow_html=True)

# Tabs Section
st.markdown('<h2 class="section-header">📜 Certifications & Achievements</h2>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🏆 Certifications", "🎯 Achievements", "🤝 Leadership"])

with tab1:
    with st.container(border=True):
        st.markdown("""
        - **DeepLearning.AI Machine Learning Specialization** (2024)
        - **Rubiscape Advanced Data Visualisation** (2024)
        - **Coursera Advanced Learning Algorithms** (2024)
        - **Coursera Supervised Machine Learning: Regression and Classification** (2024)
        - **Udemy 100 Days of Code: The Complete Python Pro Bootcamp** (2023)
        - **Coursera Introduction to Generative AI** (2023)
        - **Cisco Networking Academy Networking Basics** (2023)
        - **Forage JP Morgan Chase & Co.'s Software Engineering Lite** (2022)
        """)

with tab2:
    with st.container(border=True):
        st.markdown("""
        - **🏅 CodeCraft 4th Place** - 4-Round Coding Competition by Computer Society of India, DIT (2023)
        - **🏸 Badminton 3rd Place** - SPPU Inter-College Badminton Tournament (2023)
        - **☁️ 30 Days of Google Cloud** - Completed challenge on Google's cloud skills boost (2022)
        - **🎃 Hacktoberfest 10 & 9** - Multiple years of open-source contributions (2022-2023)
        """)

with tab3:
    with st.container(border=True):
        st.markdown("""
        **Sr. Data Manager, Association of Computer Engineering Students, DIT (2023-2024)**
        - Co-led a team of four to manage registration & attendance of 1500+ participants using Apps Script

        **Jr. Technical Head, Association of Computer Engineering Students, DIT (2022-2023)**
        - Created and emailed certificates for 900+ participants using Canva and Apps Script
        """)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Built with ❤️ using Streamlit | © 2025 Sahil Parupudi</p>",
            unsafe_allow_html=True)
