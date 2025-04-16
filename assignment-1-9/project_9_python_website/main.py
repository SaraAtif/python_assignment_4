import streamlit as st

# Page config
st.set_page_config(page_title="MSA Coaching & Tuition Center", layout="wide")

# Header section
st.markdown("""
# 🎓 MSA Coaching & Tuition Center
##### Empowering Students for a Better Tomorrow
---
""")

# Navigation
menu = st.sidebar.selectbox("Navigate", ["Home", "About Us", "Courses", "Contact"])

# Home Page
if menu == "Home":
    
    st.markdown("""
    ## Welcome to MSA Coaching!
    At MSA Coaching & Tuition Center, we strive to unlock every student's potential with personalized guidance and a focus on excellence.
    
    🎯 **Our Mission**: To provide quality education in a supportive environment.

    🌐 **Subjects**: Math, Science, English, Computer Science, and more!

    📍 Location: Karacki, Pakistan
    """)

# About Us Page
elif menu == "About Us":
    st.markdown("""
    ## About MSA Coaching
    Founded in 2010, MSA Coaching Center has helped hundreds of students improve their academic performance and gain confidence.

    Our expert tutors use modern teaching techniques and tools to make learning fun and effective.

    - 🧑‍🏫 Experienced Faculty
    - 📚 Well-structured Curriculum
    - 🧠 Regular Assessments & Feedback
    """)

# Courses Page
elif menu == "Courses":
    st.markdown("## 📘 Courses Offered")
    courses = {
        "Mathematics": "For all grades – Algebra, Geometry, Trigonometry, Calculus",
        "Science": "Physics, Chemistry, Biology with lab support",
        "English": "Grammar, Writing, Literature, Spoken English",
        "Computer Science": "Python, HTML/CSS, JavaScript basics",
    }

    for course, desc in courses.items():
        st.markdown(f"### {course}\n- {desc}")

# Contact Page
elif menu == "Contact":
    st.markdown("## 📞 Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success(f"Thanks {name}, we'll get back to you at {email}!")

    st.markdown("""
    ---
    📧 Email: info@msacoaching.com  
    📞 Phone: 0307-2184255  
    🕒 Hours: Mon - Fri | 3pm - 9pm  
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 MSA Coaching & Tuition Center | Built with ❤️ using Streamlit")

