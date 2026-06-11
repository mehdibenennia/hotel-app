import streamlit as st

st.set_page_config(page_title="Homework Management System")

# -----------------------------
# Imaginary Database
# -----------------------------

homeworks = [
    {
        "student": "Ahmed",
        "subject": "Python",
        "title": "Variables and Data Types",
        "due_date": "2026-06-20",
        "status": "Pending",
        "professor": "Mr. Karim"
    },
    {
        "student": "Ahmed",
        "subject": "Project Management",
        "title": "Create a Gantt Chart",
        "due_date": "2026-06-18",
        "status": "Submitted",
        "professor": "Ms. Salma"
    },
    {
        "student": "Sara",
        "subject": "Python",
        "title": "Loops Exercise",
        "due_date": "2026-06-21",
        "status": "Pending",
        "professor": "Mr. Karim"
    },
    {
        "student": "Youssef",
        "subject": "Python",
        "title": "Functions Homework",
        "due_date": "2026-06-23",
        "status": "Pending",
        "professor": "Mr. Karim"
    }
]

students = ["Ahmed", "Sara", "Youssef"]
professors = ["Mr. Karim", "Ms. Salma"]

# -----------------------------
# App Title
# -----------------------------

st.title("📚 Homework Management System")

page = st.sidebar.radio(
    "Choose Interface",
    ["Student Portal", "Professor Portal"]
)

# ==================================================
# STUDENT PORTAL
# ==================================================

if page == "Student Portal":

    st.header("Student Portal")

    selected_student = st.selectbox(
        "Select Student",
        students
    )

    st.subheader("My Homework")

    found = False

    for hw in homeworks:
        if hw["student"] == selected_student:

            found = True

            with st.container():
                st.markdown("---")
                st.write(f"**Subject:** {hw['subject']}")
                st.write(f"**Homework:** {hw['title']}")
                st.write(f"**Due Date:** {hw['due_date']}")
                st.write(f"**Status:** {hw['status']}")

    if not found:
        st.info("No homework assigned.")

# ==================================================
# PROFESSOR PORTAL
# ==================================================

else:

    st.header("Professor Portal")

    selected_prof = st.selectbox(
        "Select Professor",
        professors
    )

    st.subheader("Assigned Homework")

    for hw in homeworks:

        if hw["professor"] == selected_prof:

            st.markdown("---")
            st.write(f"Student: {hw['student']}")
            st.write(f"Subject: {hw['subject']}")
            st.write(f"Homework: {hw['title']}")
            st.write(f"Due Date: {hw['due_date']}")
            st.write(f"Status: {hw['status']}")

    st.markdown("---")
    st.subheader("Create New Homework")

    student = st.selectbox(
        "Assign to Student",
        students
    )

    subject = st.text_input("Subject")

    title = st.text_input("Homework Title")

    due_date = st.date_input("Due Date")

    if st.button("Assign Homework"):

        new_homework = {
            "student": student,
            "subject": subject,
            "title": title,
            "due_date": str(due_date),
            "status": "Pending",
            "professor": selected_prof
        }

        homeworks.append(new_homework)

        st.success("Homework assigned successfully!")