import streamlit as st
import google.generativeai as genai

# Configure Gemini API
API_KEY = "AQ.Ab8RN6Ix7UstZOaisI5VcRumjmTNf6qHOCtjrxgpP0fpcHZAUw"
genai.configure(api_key=API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.set_page_config(page_title="AI Content Generator", page_icon="🤖")

st.title("🤖 AI Content Generator")
st.write("Generate blogs, captions, posts, and marketing content using Gemini AI.")

# Content type
content_type = st.selectbox(
    "Select Content Type",
    [
        "Blog Post",
        "Instagram Caption",
        "Facebook Post",
        "LinkedIn Post",
        "Product Description",
        "YouTube Video Idea"
    ]
)

# Topic input
topic = st.text_input("Enter Topic")

# Length
length = st.selectbox(
    "Content Length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Content"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        prompt = f"""
        Create a {length} {content_type} about {topic}.
        Make it engaging, professional and attractive.
        """

        with st.spinner("Generating..."):
            response = model.generate_content(prompt)

        st.subheader("Generated Content")
        st.write(response.text)