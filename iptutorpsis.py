import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Initialize session state for user information
if "registered_email" not in st.session_state:
    st.session_state.registered_email = ""
if "registered_password" not in st.session_state:
    st.session_state.registered_password = ""
if "username" not in st.session_state:
    st.session_state.username = ""
if "lecturer_email" not in st.session_state:
    st.session_state.lecturer_email = ""
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Ideas"

# Function to send email
#def send_email(sender_email, sender_password, receiver_email, subject, body, image_data):
def send_email(sender_email, sender_password, receiver_email, subject, body, image_data=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if image_data is not None:
        image = MIMEImage(image_data, name="symbol.png")
        msg.attach(image)

    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# Function to get user details      
def get_user_details():
    if not st.session_state.lecturer_email:
        with st.form("user_details_form"):
            st.session_state.lecturer_email = st.text_input("Enter your lecturer's email:", value=st.session_state.lecturer_email)
            if st.form_submit_button("Save Details"):
                st.success("Details saved successfully!")
                st.rerun()
    else:
        st.write(f"Lecturer's Email: {st.session_state.lecturer_email}")
        if st.button("Update Details"):
            st.session_state.lecturer_email = ""
            st.rerun()

# Main application structure
def main():
    if not st.session_state.logged_in:
        # Title only appears on the main (login) page
        st.markdown(
            """
            <div style='text-align: center;'>
                <h1>iPTutor: Interactive Personalized Tutor for Learning Data Flow Diagram</h1>
             </div>
            """,
            unsafe_allow_html=True
        )


        #st.image(r"D:\PSIS\JTMK\DH52\inovasidfd\ladytutor3removebg.png", width='100', use_column_width="auto")
        background = Image.open("ladytutor3removebgsmall.png")
        col1, col2, col3 = st.columns([1.5, 5, 0.2])
        col2.image(background, use_column_width="auto")
              
        # Add the tutor image in the sidebar
        st.sidebar.image("psis2019a.png", use_column_width="auto")

        # Add some space after the image
        st.sidebar.markdown("<br>", unsafe_allow_html=True)

        # Use a markdown span for styled text
        st.sidebar.markdown(
        "<span style='color: black; font-weight: bold; font-style: italic;'>"
        "Please register with your Outlook email and password to access the application."
        "</span>",
    unsafe_allow_html=True
)
        
        # Sidebar for registration
        st.sidebar.markdown(
        "<span style='color: black; font-weight: bold;'>Student Login.</span>",
        unsafe_allow_html=True
        )
        with st.sidebar.form("registration_form"):
            email = st.text_input("Email (*Institution registered email only):", value=st.session_state.registered_email)
            password = st.text_input("Password (*Institution registered password only):", type="password", value=st.session_state.registered_password)
            if st.form_submit_button("Login"):
                st.session_state.registered_email = email
                st.session_state.registered_password = password
                st.session_state.logged_in = True
                st.session_state.current_page = "Ideas"
                st.rerun()

            
    if st.session_state.logged_in:
        st.sidebar.write("Navigation Menu")
        page = st.sidebar.selectbox("Select a page:", ["Guideline", "Interactive Tutorial", "Question Scenarios","iPTutor Assistance","Interactive Quiz", "Student Feedback", "Logout"], key="page_select")
        

        if page == "Logout":
            logout()
        elif page == "Guideline":
            show_ideas_page()
        elif page == "Interactive Tutorial":
            # Update to use the correct function
            show_interactive_tutorial_page()
        elif page == "Question Scenarios":
            show_question_scenarios_page()
        elif page == "iPTutor Assistance":
            show_iPTutor_Assistance()
        elif page == "Interactive Quiz":
            show_interactive_quiz_page()
        elif page == "Student Feedback":
            show_user_feedback_page()

        # Set the current page in session state
        st.session_state.current_page = page


    # Footer (appears on all pages)
    st.markdown("""<div style='text-align: center; margin-top: 50px;'>
    <p style='font-size: 14px;'><b>iPTutor: Developed by [Ts. Ainie Hayati Noruzman][ainie_hayati@psis.edu.my]©[2024]</p>""", unsafe_allow_html=True)

# Logout function
def logout():
    # Clear session state
    st.session_state.logged_in = False
    st.session_state.registered_email = ""
    st.session_state.registered_password = ""
    st.session_state.username = ""
    st.session_state.lecturer_email = ""
    st.session_state.current_page = "Ideas"
    st.sidebar.warning("Logged out successfully.")
    st.rerun()

def show_ideas_page():
    #st.title("Guideline for Data Design Model")
    col1, mid, col2 = st.columns([1,1,20])
    with col1:
        st.image("ladytutorico.png", width=95)
    with col2:
        st.title("Guideline for Data Design Model")

    st.header("Introduction to Context Diagrams")
    st.write("""
    A context diagram (CD) is a high-level, simplified representation of a system that shows the system's boundaries and its interactions with external entities.
    Key components include:
    - **System**: The central process or system being analyzed.
    - **External Entities**: People, systems, or organizations that interact with the system.
    - **Data Flows**: Arrows that represent the flow of information between the system and external entities.
    """)

    st.header("Introduction to Data Flow Diagram")
    st.write("""
    A Data Flow Diagram (DFD) is a graphical representation of the flow of data through an information system.
    It shows how data enters the system, gets processed, and exits the system. The two main types of notation 
    used for data flow diagrams are Yourdon-Coad and Gane-Sarson. All data flow diagrams include four
    main elements: 
    - **External Entities**: Represented by squares or rectangles, they interact with the system but are outside of it.
    - **Processes**: Represented by circles or rectangular with rounded corrners. Every process has a name that identifies
             the function it performs.
    - **Data Stores**: Represented by open-ended rectangles, they store data.
    - **Data Flows**: Represented by arrows, they show the flow of data.
    
    """)

   # Instead of download link, display the image
    st.write("Table below represent differences between two main types of notation used in DFD:")
    image_path = "NOTATION.png"
    st.image(image_path, caption="DFD Notes", use_column_width=True)

    # Adding a downloadable PDF file for the context diagram section
    st.write("Download your notes here:")
    with open("context_diagram_notes.pdf", "rb") as file:
        btn = st.download_button(
            label="Notes",
            data=file,
            file_name="context_diagram_notes.pdf",
            mime="application/pdf"
        )


# Tutorial Data
tutorial_steps = [
    {
        "title": "Step 1: Draw external entity for customer",
        "content": "",
        "exercise": "###### Use a rectangle to represent the customer and label it as 'Customer'.",
    },
    {
        "title": "Step 2: Draw a process that represents the order processing",
        "content": "",
        "exercise": "###### Use a circle or rounded rectangle to represent the process and label it as 'Order'.",
    },
    {
        "title": "Step 3: Draw a data store that represents the inventory of products",
        "content": "",
         "exercise": "###### Use an open-ended rectangle to represent the data store and label it as 'Product DB'.",
    },
    {
        "title": "Step 4: Draw the data flow between the external entity, process, and data store",
        "content": "",
        "exercise": "###### Use arrows to represent the data flow. Label the flows as 'Customer Order'.",
    },
    {
        "title": "Complete Tutorials",
        "content": "###### Draw a simple DFD that includes a 'Customer', 'Processing Order' (process), and 'Order Database' (data store).Use appropriate symbols and connect them with arrows to represent data flow.",
        "exercise": "###### Use all the notations that you already learned and try to make a complete DFD.",
    },
    {
        "title": "Congratulations!",
        "content": "You've completed the tutorial on DFDs. You've learned about processes, data stores, data flows, and external entities.",
        "exercise": None
    }
]

def show_tutorial_step(step_index):
    st.write(f"Logged in as: {st.session_state.registered_email}")

    if step_index < 0 or step_index >= len(tutorial_steps):
        st.error("Invalid tutorial step. Resetting to the beginning.")
        st.session_state.tutorial_step = 0
        step_index = 0
    
    step = tutorial_steps[step_index]
    st.header(step["title"])
    st.write(step["content"])
    
    if step["exercise"]:
        st.write("### Exercise")
        st.write(step["exercise"])
        
        # Initialize canvas
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=3,
            stroke_color="#000000",
            background_color="#eee",
            update_streamlit=True,
            height=300,
            drawing_mode="freedraw",
            key=f"canvas_{step_index}",
        )

        # Button to check the answer
        if st.button("Check Answer", key=f"check_answer_{step_index}"):
            if canvas_result.image_data is not None:
        # Check the drawing
             is_correct = check_drawing(step["title"], canvas_result.image_data)
        
            if is_correct:
                st.success("Congratulations! Your answer is correct.")
            else:
                st.error("Not quite right. Try again!")

                 
    # Navigation buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if step_index > 0:
            if st.button("Previous Step", key=f"prev_{step_index}"):
                st.session_state.tutorial_step -= 1
                st.rerun()
        else:
            # Placeholder button to maintain layout
            st.empty()

    with col2:
        if step_index < len(tutorial_steps) - 1:
            if st.button("Next Step", key=f"next_{step_index}"):
                st.session_state.tutorial_step += 1
                st.rerun()
        else:
            st.write("You've reached the end of the tutorial.")

    # Note about question scenarios
    if step_index == len(tutorial_steps) - 1:
        st.info("Note: To practice with question scenarios and submit your work to your lecturer, please visit the 'Question Scenarios' page.")

    if step_index == len(tutorial_steps) - 1:  # Check if it is the conclusion step
        st.markdown("### Download Your Tutorial Answer")
        with open("tutorial_summary.pdf", "rb") as file:
            btn = st.download_button(
            label="Tutorial Answer",
            data=file,
            file_name="tutorial_summary.pdf",
            mime="application/pdf"
        )


# screnarios iPTutor page
def show_iPTutor_Assistance():
    # Center the title using HTML
    #st.markdown("<h1 style='text-align: center;'>iPTutor Assistance</h1>", unsafe_allow_html=True)

    # Use an iframe to embed the Flask application
    st.markdown(
        """
        <iframe src="http://127.0.0.1:5000" 
                width="100%" 
                height="600" 
                frameborder="0">
        </iframe>
        """,
        unsafe_allow_html=True
    )


# screnarios question page
def show_question_scenarios_page():
    #st.title("DFD Question Scenarios")
    col1, mid, col2 = st.columns([1,1,20])
    with col1:
        st.image("ladytutorico.png", width=95)
    with col2:
        st.title("DFD Question Scenarios")
    
    st.markdown("##### Instruction: Please enter the email address of your dedicated class teacher for submission purposes")
    st.write(f"Logged in as: {st.session_state.registered_email}")
    # Display the logged-in message aligned to the right
   # st.markdown(f"<div style='text-align: right;'>Logged in as: {st.session_state.registered_email}</div>", unsafe_allow_html=True)
    
    get_user_details()

    if st.session_state.lecturer_email:
        st.write("Select a scenario to draw the corresponding DFD:")

        scenario = st.selectbox("Select a scenario:", ["Scenario 1", "Scenario 2", "Scenario 3"])

        if scenario == "Scenario 1":
            st.write("""
            **Scenario 1: Online Shopping System**
            Draw a DFD to represent an online shopping system where a customer can browse products, add items to a cart, and complete a purchase.
            """)
        elif scenario == "Scenario 2":
            st.write("""
            **Scenario 2: Library Management System**
            Draw a CD (context diagram) to represent a library management system where a user can search for books, borrow books, and return books.
            """)
        elif scenario == "Scenario 3":
            st.write("""
            **Scenario 3: Student Registration System**
            Draw a DFD to represent a student registration system where students can register for courses, view grades, and update personal information.
            """)

        st.write("Draw the corresponding DFD:")

        dfd_canvas = st_canvas(
            fill_color="rgba(173, 216, 230, 0.3)",
            stroke_width=2,
            stroke_color='#000',
            background_color='#fff',
            update_streamlit=True,
            height=400,
            drawing_mode="freedraw",
            key="dfd_canvas",
        )

        if st.button("Save and Submit DFD"):
            if dfd_canvas.image_data is not None:
                img = Image.fromarray(dfd_canvas.image_data.astype('uint8'), 'RGBA')

                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{st.session_state.username}_{scenario}_{timestamp}.png"

                # Save image to bytes
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()

                # Prepare email
                subject = f"DFD Submission: {scenario}"
                body = f"Student: {st.session_state.username}\nScenario: {scenario}\nTimestamp: {timestamp}"

                # Send email using registered email
                if send_email(st.session_state.registered_email, st.session_state.registered_password, st.session_state.lecturer_email, subject, body, img_byte_arr):
                    st.success(f"DFD for {scenario} submitted successfully to {st.session_state.lecturer_email}!")
                    st.image(img, caption=f"Submitted DFD for {scenario}")
                else:
                    st.error("Failed to submit DFD. Please try again or contact support.")
            else:
                st.error("No DFD drawn. Please draw the DFD before submitting.")

def show_interactive_quiz_page():
    #st.title("Interactive Quiz")
    col1, mid, col2 = st.columns([1,1,20])
    with col1:
        st.image("ladytutorico.png", width=95)
    with col2:
        st.title("Interactive Quiz")
    st.write("### Multiple Choice Questions on DFD and Context Diagram")
       
    st.write(f"Logged in as: {st.session_state.registered_email}")
    st.markdown("##### Instruction: Please answer all questions")
    

    # Define MCQs
    mcqs = [
        {
            "question": "Which symbol is used to represent a process in a DFD?",
            "options": ["Select an answer", "Rectangle", "Circle", "Triangle", "Hexagon"],
            "answer": "Circle"
        },
        {
            "question": "In a context diagram, how many processes should there be?",
            "options": ["Select an answer", "One", "Two", "Three", "Many"],
            "answer": "One"
        },
        {
            "question": "What does a data store represent in a DFD?",
            "options": ["Select an answer", "A process", "An external entity", "A data storage", "A data flow"],
            "answer": "A data storage"
        },
        {
            "question": "What symbol represents an external entity in a DFD?",
            "options": ["Select an answer", "Oval", "Rectangle", "Circle", "Diamond"],
            "answer": "Rectangle"
        },
        {
            "question": "What does a data flow represent?",
            "options": ["Select an answer", "Movement of data", "Storage of data", "Transformation of data", "Data creation"],
            "answer": "Movement of data"
        }
    ]

    score = 0

    # Display MCQs
    for i, mcq in enumerate(mcqs):
        st.write(f"**Q{i+1}: {mcq['question']}**")
        user_answer = st.radio("", mcq["options"], key=f"mcq_{i}")  # No default selection

        # Feedback on the answer
        if user_answer != "Select an answer":
            if user_answer == mcq["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error("Incorrect. Try again.")

    st.write("Thank you for completing the questions!")
    st.write(f"Your score is: {score} out of {len(mcqs)}")

    if score == len(mcqs):
        st.balloons()


def show_interactive_tutorial_page():
    #st.title("Interactive Tutorial")
    col1, mid, col2 = st.columns([1,1,20])
    with col1:
        st.image("ladytutorico.png", width=95)
    with col2:
        st.title("Interactive Tutorial")
    st.markdown("##### Instruction: Please follow the step for each tutorial given")

    
    # Add a reset button
    if st.button("Reset Tutorial", key="reset_tutorial"):
        st.session_state.tutorial_step = 0
        st.rerun()
    
    # Make sure tutorial step is initialized
    if 'tutorial_step' not in st.session_state:
        st.session_state.tutorial_step = 0

    # Show the tutorial step
    show_tutorial_step(st.session_state.tutorial_step)


import cv2
import numpy as np
from PIL import Image
import io

# check drawing
def check_drawing(drawing_type, image_data):
    # Convert image_data to OpenCV format
    image = Image.fromarray(image_data.astype('uint8'), 'RGBA')
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGR)
    
    # Preprocess the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    if drawing_type == "Step 1: Draw external entity for customer":
        # Check for rectangular shape
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
            if len(approx) == 4:  # A rectangle has 4 corners
                return True
        return False
    
    elif drawing_type == "Step 2: Draw a process that represents the order processing":
        # Check for circular shape
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
            if len(approx) > 8:  # Assuming a circle has more than 8 sides when approximated
                return True
        return False
    
    elif drawing_type == "Step 3: Draw a data store that represents the inventory of products":
        # Check for open-ended rectangle (data store)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
            if len(approx) == 4:  # A rectangle has 4 corners
                return True
        return False
    
    elif drawing_type == "Step 4: Draw the data flow between the external entity, process, and data store":
        # Check for arrow-like shape
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
        if lines is not None and len(lines) >= 2:
            return True
        return False
    
    elif drawing_type == "Complete Tutorials":
        # Initialize flags for all components
        has_external_entity = check_drawing("Step 1: Understanding External Entities", image_data)
        has_process = check_drawing("Step 2: Understanding Processes", image_data)
        has_data_store = check_drawing("Step 3: Understanding Data Stores", image_data)
        has_data_flow = check_drawing("Step 4: Understanding Data Flows", image_data)

        # Check if all components are present
        return has_external_entity and has_process and has_data_store and has_data_flow
    
    # Return False if none of the conditions met
    return False


#check feedback
def show_user_feedback_page():
    #st.title("Student Feedback")
    col1, mid, col2 = st.columns([1,1,20])
    with col1:
        st.image("ladytutorico.png", width=95)
    with col2:
        st.title("Student Feedback")
    st.markdown("##### Instruction: Please give a feedback to improve our services and enhance your learning experience.")



    # Default developer email
    developer_email = "ainie_hayati@psis.edu.my"  # Developer's email address

    if st.session_state.logged_in:
        st.write(f"Logged in as: {st.session_state.registered_email}")

        # Optional: Display Google Form link
        st.write("##### Kindly provide your feedback through this Google Form: https://forms.gle/DnKSGkycntsPoWDn6")
        
        st.write("### Suggestion for Improvement")
        feedback = st.text_area("Enter your suggestion here:", key="user_feedback_textarea")
        if st.button("Submit Here", key="submit_feedback_button"):
            if feedback:
                # Prepare email
                subject = "Student Feedback Submission"
                body = f"User: {st.session_state.registered_email}\n\nFeedback:\n{feedback}"
                
                # Send email using registered email to the developer
                if send_email(st.session_state.registered_email, st.session_state.registered_password, developer_email, subject, body):
                    st.success("Thank you for your feedback! It has been sent successfully to the developer.")
                else:
                    st.error("Failed to submit feedback. Please try again or contact support.")
            else:
                st.warning("Please enter your feedback before submitting.")
    else:
        st.warning("Please log in to submit feedback.")

 
  
if __name__ == "__main__":
    main()
 