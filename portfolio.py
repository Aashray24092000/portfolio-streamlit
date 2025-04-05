import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- PAGE CONFIG ---
st.set_page_config(page_title="Asharaya's Portfolio", page_icon="🚀", layout="wide")

# --- STYLES ---
st.markdown("""
<style>
    .stApp {
        background-color: #0D0D0D;
        color: #F5F5F5;
    }

    .header {
        font-size: 22px;
        font-weight: bold;
        color: #D4AF37;
        text-align: center;
        padding: 12px;
        background-color: #1C1C1C;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
    }

    .header a {
        color: #D4AF37;
        text-decoration: none;
        margin: 0 20px;
    }

    .header a:hover {
        text-decoration: underline;
        color: #FFD700;
    }

    .footer {
        text-align: center;
        font-size: 16px;
        color: #D4AF37;
        background-color: #1C1C1C;
        padding: 15px;
        border-radius: 10px;
        margin-top: 30px;
    }

    .contact-form {
        background-color: #1C1C1C;
        padding: 10px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    }

    .skill-bar {
        background-color: #2E2E2E;
        border-radius: 10px;
        overflow: hidden;
        height: 20px;
        margin-bottom: 15px;
    }

    .skill-level {
        height: 100%;
        background-color: #D4AF37;
        text-align: right;
        padding-right: 10px;
        font-size: 14px;
        font-weight: bold;
        color: black;
        line-height: 20px;
        transition: width 1s ease-in-out;
    }

    .project-card {
        background-color: #1C1C1C;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(212, 175, 55, 0.2);
    }

    .project-title {
        color: #D4AF37;
        font-size: 20px;
        margin-bottom: 8px;
    }

    .project-tech {
        color: #CCCCCC;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .project-desc {
        color: #F5F5F5;
        font-size: 16px;
    }

    .stButton > button {
        background-color: #1f1f1f;
        color: #FFD700;
        border: 1px solid #FFD700;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: 600;
        transition: 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #FFD700;
        color: #000000;
        border: 1px solid #FFD700;
        box-shadow: 0 0 10px #FFD70088;
    }

    .nav-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
    }

    .nav-button button {
        background-color: #1f1f1f;
        color: #FFD700;
        border: 1px solid #FFD700;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .nav-button button:hover {
        background-color: #FFD700;
        color: black;
        box-shadow: 0 0 10px #FFD70088;
    }

    /* HAMBURGER + TOGGLE */
    .hamburger {
        display: none;
        position: fixed;
        top: 16px;
        left: 16px;
        z-index: 1001;
        cursor: pointer;
    }

    .hamburger div {
        width: 25px;
        height: 3px;
        background-color: #FFD700;
        margin: 5px 0;
        transition: 0.4s;
    }

    #menu-toggle {
        display: none;
    }

    #menu-toggle:checked + .button-scroll-container {
        display: flex !important;
        flex-direction: column;
        position: fixed;
        top: 60px;
        left: 0;
        background-color: #1C1C1C;
        width: 100%;
        z-index: 1000;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }

    @media screen and (max-width: 768px) {
        .hamburger {
            display: block;
        }

        .button-scroll-container {
            display: none;
        }

        .header {
            font-size: 18px;
            padding: 10px;
            flex-direction: column;
            align-items: center;
        }

        .header a {
            margin: 8px 0;
            font-size: 16px;
        }

        .footer {
            font-size: 14px;
            padding: 10px;
        }

        .project-title {
            font-size: 18px;
        }

        .project-desc {
            font-size: 14px;
        }

        .stButton > button {
            padding: 0.4em 0.8em;
            font-size: 14px;
        }

        .contact-form {
            padding: 8px;
        }

        .nav-container {
            flex-direction: column;
            align-items: center;
        }
    }

    .button-scroll-container {
        display: flex;
        overflow-x: auto;
        gap: 10px;
        padding-bottom: 10px;
        margin-bottom: 20px;
        white-space: nowrap;
        justify-content: start;
    }

    .button-scroll-container .element-container {
        min-width: 120px;
        flex-shrink: 0;
    }

    .button-scroll-container::-webkit-scrollbar {
        display: none;
    }

    .button-scroll-container {
        scrollbar-width: none;
    }
</style>

<!-- Hamburger toggle checkbox + icon -->
<div class="hamburger">
    <label for="menu-toggle">
        <div></div>
        <div></div>
        <div></div>
    </label>
</div>
<input type="checkbox" id="menu-toggle" />
""", unsafe_allow_html=True)
st.markdown("""
<script>
    // Automatically toggle menu on click of the hamburger label
    document.addEventListener("DOMContentLoaded", function () {
        const label = document.querySelector(".hamburger label");
        const checkbox = document.getElementById("menu-toggle");

        label.addEventListener("click", function () {
            checkbox.checked = !checkbox.checked;
        });
    });
</script>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "section" not in st.session_state:
    st.session_state.section = "About Me"

# --- Decorative Line ---
st.markdown("""<div style="height: 8px; background-color: #1E1E1E; border-radius: 10px; margin-bottom: 20px;"></div>""", unsafe_allow_html=True)

# --- NAVIGATION BUTTONS ---
st.markdown('<div class="button-scroll-container">', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("About Me"):
        st.session_state.section = "About Me"
with col2:
    if st.button("Experience"):
        st.session_state.section = "Experience"
with col3:
    if st.button("Skills"):
        st.session_state.section = "Skills"
with col4:
    if st.button("Projects"):
        st.session_state.section = "Projects"
with col5:
    if st.button("Contact"):
        st.session_state.section = "Contact"

st.markdown('</div>', unsafe_allow_html=True)
# --- EMAIL FUNCTION ---
def send_email(name, contact, message):
    sender_email = "ashraysingh81@gmail.com"
    password = "ynnh vsar xyyf rwcx"
    receiver_email = "ashraysingh81@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Message from {name} ({contact})"
    msg.attach(MIMEText(f"Name: {name}\nContact: {contact}\nMessage: {message}", 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# --- ABOUT ME ---
if st.session_state.section == "About Me":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("👋 Hi, I'm Asharaya Singh Bhadauriya")
        st.subheader("AI Developer | Python Developer | Data Analyst")
        st.write("""
        As a dedicated AI Intern, I am seeking a full-time position in Data Science or AI related
fields, where I can apply my expertise in machine learning, deep learning, and data
analytics to solve real-world challenges. With hands-on experience in model training,
deployment, and backend integration using Python, FastAPI, and OpenCV, I am eager to
work with complex datasets, develop AI-driven solutions, and optimize systems for
efficiency and accuracy. Passionate about leveraging data to drive innovation, I aim to
contribute to impactful projects that enhance automation and decision-making.
        """)
    with col2:
        try:
            image = Image.open("profile.jpg")
            st.image(image, width=300)
        except:
            st.warning("Profile image not found!")

    st.write("[LinkedIn](https://www.linkedin.com/in/asharaya-singh-) | [GitHub](https://github.com/Aashray24092000) | [Email](mailto:ashraysingh81@gmail.com)")

# --- EXPERIENCE ---
elif st.session_state.section == "Experience":
    st.title("Experience")

    st.markdown("""
    I am a passionate AI Developer with expertise in Machine Learning, Deep Learning, and Robotics. 
    I have hands-on experience in deploying AI models, working with datasets, and creating impactful solutions 
    for real-world challenges.

    During my internship at **KnowledgeFlex Technologies Pvt. Ltd.**, I gained practical experience in:
    - **OpenCV** for real-time computer vision applications  
    - **YOLO** models for object detection and training custom datasets  
    - **Docker** for containerization and scalable deployment  
    - **Linux server** management and operations  
    - **Flask** for deploying a live face recognition system, including automatic capturing of unknown faces  

    I have also expanded my skills in backend and API development:
    - **Django** for building RESTful APIs and managing databases using **MongoDB** and **SQLite**  
    - **FastAPI** for developing high-performance APIs, including integration in a real-time voice bot project  
    - **Flask** for deploying a live face recognition system, including automatic capturing of unknown faces  

    I am currently seeking a **full-time opportunity** where I can contribute my skills, grow with a collaborative team, 
    and drive innovative AI-powered solutions for business growth.
    """)

    # --- PROJECT 1 ---
    st.subheader("Project 1 - Live Face Recognition (Walk-in Security)")
    st.markdown("""
    This project involves real-time face recognition for workplace security.  
    We analyze a person’s face and generate facial embeddings using FaceNet. These embeddings are matched against a database:
    
    - If a match is found, the person is **verified for entry**.  
    - If not, the system detects the user as **unknown**, prompts for registration, and **automatically captures their image**.  
    - The system then stores the embedding along with the entered name, enabling **future verification**.

    Tech stack used: **OpenCV**, **FaceNet**, **Flask**, **SQLite**
    """)

    # --- PROJECT 2 ---
    st.subheader("Project 2 - Voice Bot with Smart Guard Reception")
    st.markdown("""
    In this project, I handled **backend API development** using **FastAPI** for a smart voice bot assistant deployed at the reception of a company:

    - When a person comes in front of the camera, their face is analyzed and matched.  
    - If they are a **company employee**, they are **greeted with their name**.  
    - If they are **not recognized**, the system asks the **reason for visit** and requests the **employee's name** they wish to meet.  
    - A host approval system is then triggered to allow or deny entry.

    Tech stack used: **FastAPI**, **OpenCV**, **FaceNet**, **SMTP Server**, **Linux**
    """)

# --- skills ---
elif st.session_state.section == "Skills":
    st.title("Skills")
    st.write("""
    I am a passionate AI Developerand Data Analyst with expertise in Machine Learning, Deep Learning, and python. 
    ... (your current description here)
    """)

    skills = {
        "Python": 90,
        "Django": 70,
        "SQL": 80,
        "FastAPI": 80,
        "Machine Learning": 70,
        "Linux Server": 60,
        "Docker": 50,
        "CNN": 60,
        "OpenCV": 80,
        "TensorFlow": 70,
        "Data Visualization (Pandas, NumPy, Matplotlib, Seaborn)": 90
    }

    for skill, percent in skills.items():
        st.markdown(f"""
            <div class="skill-container">
                <div class="skill-title">{skill}</div>
                <div class="skill-bar">
                    <div class="skill-level" style="width: {percent}%;">{percent}%</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
# --- PROJECTS ---
elif st.session_state.section == "Projects":
    st.title("My Projects")

    st.image("blink.png", width=500)  # replace with your actual image path
    st.subheader("Blinkit Sales Analysis Dashboard (Power BI)")

    st.markdown("""
    **Tech Used:** Power BI, Excel, DAX, Data Cleaning, Data Visualization  
    **Description:** A detailed business intelligence dashboard to analyze the performance of Blinkit grocery stores:
    - **KPIs Tracked:** Total Sales, Average Sales, Revenue, Average Ratings
    - **Visualizations:** 
        - Donut Charts for Top Performing Outlets
        - Bar Graphs for Fast-Moving Products
        - Line Charts for Sales Trends
        - Area-wise Profit & Loss Analytics
    - **Insights Generated:** Identified high-revenue products and locations with low performance, enabling strategic decisions for better stocking and promotions.
    """)

    st.markdown("---")

    st.image("plant.jpeg", width=500)  # Replace with actual image path
    st.subheader("Plant Disease Image Classification System")

    st.markdown("""
    **Tech Used:** Convolutional Neural Network (CNN), Python, Streamlit, Image Dataset  
    **Description:** A smart agriculture tool built using deep learning to detect diseases from plant leaf images:
    - **Functionality:** Users upload a leaf image, and the system predicts the disease class.
    - **Model:** Trained CNN model capable of multi-class classification
    - **Outputs:** 
        - Predicted Disease Name
        - Confidence Score / Probability of Prediction
    - **Use Case:** Helps farmers and agricultural experts detect crop diseases early, enabling timely treatment and improved crop yield.
    """)
    st.markdown("---")

    st.image("whatspp.jpeg", width=500)  # replace with your actual image path
    st.subheader("WhatsApp Chat Analyzer")

    st.markdown("""
    **Tech Used:** Python, Pandas, Streamlit, Matplotlib, Seaborn, WordCloud, Emojis, RegEx  

    **Description:**  
    An interactive tool to analyze WhatsApp chat exports by uploading `.txt` files of chat history. It visualizes insights through real-time charts and graphs for better understanding of chat behavior.

    - 📨 **Total Statistics:**
        - Total Messages Sent
        - Total Words Typed
        - Media Files Shared
        - Links Shared

    - 👥 **User-wise Analysis:**
        - Most active participants
        - Bar graphs for message distribution
        - Emoji word cloud to display emotional tone

    - 🕒 **Time-based Analytics:**
        - Monthly Timeline with line chart
        - Daily Timeline and Weekly Map
        - Heatmap for message intensity by time & day

    - 🧠 **Message Insights:**
        - Filters out media, links, and deleted messages
        - Most commonly used words via word cloud

    **Outcome:** Helped understand behavioral trends, group engagement, and active time slots in chat groups.
    """)




# --- CONTACT ---
elif st.session_state.section == "Contact":
    st.title("Contact Me")
    st.markdown("<div class='contact-form'>", unsafe_allow_html=True)

    name = st.text_input("Your Name", "")
    contact = st.text_input("Your Contact Number", "")
    message = st.text_area("Your Message", "")

    if st.button("Send"):
        if not name:
            st.error("Please enter your name.")
        elif not contact:
            st.error("Please enter your contact number.")
        elif not message:
            st.error("Please enter a message.")
        else:
            if send_email(name, contact, message):
                st.success("Your message has been sent successfully!")
            else:
                st.error("Failed to send your message. Please try again later.")

    st.markdown("</div>", unsafe_allow_html=True)

import datetime

# --- FOOTER WITH REAL-TIME CLOCK ---
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown(f"""
    📧 Contact: <a href='mailto:ashraysingh81@gmail.com' style='color: #FFD700;'>ashraysingh81@gmail.com</a> | Created by <b>Asharaya Singh Bhadauriya</b><br>
    📱 Contact Number: +91 6394313848<br>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
