# This is a sample Python script.
import streamlit as st
import random
import time

# humorous_quotes = [
#     "In God we trust. All others must bring data. — W. Edwards Deming",
#     "Artificial intelligence is no match for natural stupidity. — Unknown",
#     "99 little bugs in the code, 99 bugs in the code. Take one down, patch it around, 127 little bugs in the code. — Unknown",
#     "Debugging is like being the detective in a crime movie where you are also the murderer. — Filipe Fortes",
#     "There are two ways to write error-free programs; only the third one works. — Alan J. Perlis",
#     "Programming is like writing a book... except if you miss out a single comma on page 126 the whole thing makes no sense. — Unknown",
#     "AI is the only field where 50 years of research has produced systems that can beat humans at chess, but still struggle to recognize a cat in a picture. — Unknown",
#     "To understand recursion, you must first understand recursion. — Unknown",
#     "The best thing about a Boolean is even if you are wrong, you are only off by a bit. — Unknown",
#     "Experience is the name everyone gives to their mistakes. — Oscar Wilde",
#     "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?' — Unknown",
#     "The hardest part of programming is thinking of good variable names. — Unknown",
#     "I have a joke on programming but it only works on my machine. — Unknown",
#     "Algorithm (noun): Word used by programmers when they don’t want to explain what they did. — Unknown",
#     "Why do programmers prefer dark mode? Because light attracts bugs. — Unknown",
#     "If debugging is the process of removing software bugs, then programming must be the process of putting them in. — Edsger Dijkstra",
#     "A language that doesn’t affect the way you think about programming is not worth knowing. — Alan J. Perlis",
#     "Walking on water and developing software from a specification are easy if both are frozen. — Edward V. Berard",
#     "There are only two kinds of programming languages: those people always complain about and those nobody uses. — Bjarne Stroustrup"
# ]
humorous_quotes = [
    "In God we trust. All others must bring data. — W. Edwards Deming",
    "Artificial intelligence is no match for natural stupidity. — Unknown",
    "99 little bugs in the code, take one down, patch it around, 127 little bugs in the code. — Unknown",
    "Debugging is like being the detective in a crime movie where you are also the murderer. — Filipe Fortes",
    "There are two ways to write error-free programs; only the third one works. — Alan J. Perlis",
    "AI is the only field where 50 years of research has produced systems that can beat humans at chess, but still struggle to recognize a cat. — Unknown",
    "To understand recursion, you must first understand recursion. — Unknown",
    "The best thing about a Boolean is even if you are wrong, you are only off by a bit. — Unknown",
    "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?' — Unknown",
    "The hardest part of programming is thinking of good variable names. — Unknown",
    "In machine learning, computers don’t learn. They just copy things from data. — Unknown",
    "I have a joke on programming but it only works on my machine. — Unknown",
    "Algorithm: Word used by programmers when they don’t want to explain what they did. — Unknown",
    "Why do programmers prefer dark mode? Because light attracts bugs. — Unknown",
    "If debugging is removing bugs, then programming is putting them in. — Edsger Dijkstra",
    "There are two kinds of programming languages: those people complain about and those nobody uses. — Bjarne Stroustrup"
]
st.toast(random.choice(humorous_quotes),icon="✨")
st.title("Hallo, I'm Sahil Parupudi")

"""
A Computer Engineering Student at Dr. D.Y. Patil Institute of Technology,Pimpri.Trying to learn and explore
field of data science and ML whilst being surrounded by trees in a random forest 
"""
col1, col2,col3,col4 = st.columns([1,1,1,1])
with st.expander("Contact Details"):
        st.link_button("Github","https://github.com/sahil-s-246")
        "https: // github.com / sahil - s - 246"
        st.link_button("LinkedIn","https://linkedin.com/sahilparupudi")
        "https: // linkedin.com / sahilparupudi"
        st.link_button("Email","mailto://sahilsrinivas3@gmail.com")
        "sahilsrinivas3 @ gmail.com"
        st.link_button("Resume","https://sahil-s-246.github.io/autoCV")
        "https: // sahil - s - 246.github.io / autoCV"

"Experience:"
{
   "Rubiscape":["Jun-Sep 2025","Project Intern"]
}
"Technologies:"
{
    "Languages":["Python","Java","C++"],
    "Web":["HTML","CSS","JS","Flask"],
    "Libraries":["Pandas","Seaborn","Scikit-learn","BeautifulSoup"],
    "Misc":["Git","Apps Script","MySQL","MongoDB"]
}

tab1,tab2,tab3 = st.tabs(["Certifications","Achievements","Volunteering"])
with tab1:
    """\nRubiscape Advance Data Visualisation: 2024

\nCoursera Advanced Learning Algorithms: 2024
\nCoursera Supervised Machine Learning: Regression and Classification: 2024
\nUdemy 100 Days of Code: The Complete Python Pro Bootcamp for 2023: 2023
\nCoursera Introduction to Generative AI: 2023
\nCisco Networking Academy Networking Basics: 2023
\nForage JP Morgan Chase & Co.’s Software Engineering Lite: 2022 """

with tab2:
    """
\nHacktoberfest 10 Completed Hacktoberfest by submitting 4 accepted Pull Requests: 2023
\nCodeCraft Achieved 4th Place in a 4-Round Coding Competition organized by Computer Society of India, DIT: 2023
\nBadminton 3rd Place in Savitribai Phule Pune University’s Inter-College Badminton tournament: 2023
\nHacktoberfest 9 Contributed to various repositories and completed Hacktoberfest: 2022
\n30 Days of Cloud Challenge Completed the challenge on cloud skills boost: 2022

"""

with tab3:
    """Sr. Data Manager, Association of Computer Engineering Students, DIT (2023 - 2024) =>
Co-led a team of four to manage the registration & attendance of 1500+ participants using Apps Script

Jr. Technical Head, Association of Computer Engineering Students, DIT (2022 - 2023) =>
Created and emailed certificates for 900+ participants of the club’s flagship event using Canva and Apps Script.
"""