import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import warnings
warnings.filterwarnings('ignore')

import logging
logging.getLogger('absl').setLevel(logging.ERROR)

import streamlit as st
import google.generativeai as genai
import io
from dotenv import load_dotenv
from langsmith import traceable
import pandas as pd
import json
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from annotated_text import annotated_text, annotation
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
import re

# Load environment variables
load_dotenv()

# Streamlit app
st.set_page_config(page_title="Gemini 1.5 Flash - 1.5 Pro AI Prompt Generator", page_icon="🤖", layout="wide")

st.subheader("Automated AI Prompt Engineer (APE)")

st.video("media/video/720p-final gemini-pro-aug12.mp4", loop=False, autoplay=True, muted=True)

# Add logo
add_logo("media/images/app-logo.png")

tracing_enabled = os.getenv("LANGCHAIN_TRACING_V2")  # Default to False if not set
api_key = os.getenv("LANGCHAIN_API_KEY")

# Function to load Lottie animations
@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_ai = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_zrqthn6o.json")
lottie_analysis = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_wqypnpu5.json")

# Initialize session state variables
if 'temperature' not in st.session_state:
    st.session_state.temperature = 0.5
if 'max_output_tokens' not in st.session_state:
    st.session_state.max_output_tokens = 8000
if 'model_version' not in st.session_state:
    st.session_state.model_version = "gemini-1.5-flash"
if 'api_configured' not in st.session_state:
    st.session_state.api_configured = False

# Sidebar for API key and model settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Gemini API key", type="password", key="api_key_input")

# Model selection
model_options = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.5-pro-exp-0801"]
st.session_state.model_version = st.sidebar.selectbox("Select Gemini model version:", model_options, index=model_options.index(st.session_state.model_version), key="model_version_select")

# Temperature slider
st.session_state.temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=st.session_state.temperature, step=0.1, key="temperature_slider")

# Max output tokens slider
st.session_state.max_output_tokens = st.sidebar.slider("Max Output Tokens", min_value=50, max_value=8192, value=st.session_state.max_output_tokens, step=50, key="max_output_tokens_slider")

# Function to generate a download link
def get_download_link(content, filename, text):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">{text}</a>'

# Function to process uploaded file
def process_uploaded_file(uploaded_file):
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        return df.to_string()
    else:
        content = uploaded_file.getvalue().decode("utf-8")
        return content

# Function to process image
def process_image(uploaded_file):
    if uploaded_file.type.startswith('image'):
        image = Image.open(uploaded_file)
        return image
    return None

# Gemini API setup
def setup_gemini_api():
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False

@traceable # Langsmith Tracing and Observability

# Function to generate prompt
def generate_prompt(task, variables=""):
    model = genai.GenerativeModel(st.session_state.model_version)
    prompt = f"Task: {task}\nVariables: {variables}\nGenerate a Chain of Thought COT prompt based on the given task and variables."
    
    try:
        response = model.generate_content(prompt,
                                          generation_config=genai.types.GenerationConfig(
                                              temperature=st.session_state.temperature,
                                              max_output_tokens=st.session_state.max_output_tokens,
                                          ))
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

@traceable # Langsmith Tracing and Observability

# Function to generate test data
def generate_test_data(topic, num_pairs):
    model = genai.GenerativeModel(st.session_state.model_version)
    prompt = f"""Generate {num_pairs} pairs of conversation for the topic: {topic}. 
    Each pair should consist of a human message and an AI response. 
    Format the output as a valid JSON array of objects, where each object has 'human' and 'ai' keys.
    Ensure the output is strictly in this format:
    [
        {{"human": "Human message 1", "ai": "AI response 1"}},
        {{"human": "Human message 2", "ai": "AI response 2"}},
        ...
    ]
    Do not include any text before or after the JSON array.
    """
    
    try:
        response = model.generate_content(prompt,
                                          generation_config=genai.types.GenerationConfig(
                                              temperature=st.session_state.temperature,
                                              max_output_tokens=st.session_state.max_output_tokens,
                                          ))
        
        # Attempt to parse the response as JSON
        try:
            json_data = json.loads(response.text)
            if isinstance(json_data, list) and all(isinstance(item, dict) and 'human' in item and 'ai' in item for item in json_data):
                return json_data
            else:
                raise ValueError("Response is not in the expected format")
        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract JSON from the response
            json_match = re.search(r'\[.*\]', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                return json.loads(json_str)
            else:
                raise ValueError("Could not extract valid JSON from the response")
    except Exception as e:
        st.error(f"An error occurred while generating test data: {str(e)}")
        return None

# Setup Gemini API
if not st.session_state.api_configured:
    st.session_state.api_configured = setup_gemini_api()

if st.session_state.api_configured:
    st.sidebar.success("API key configured successfully!")
    
# Main content area
colored_header(
    label="Gemini 1.5 Flash - Gemini 1.5-Pro - Gemini-1.5-Pro-Exp",
    description="Automated AI Prompt Engineer (APE). Easily Generate AI Prompts. Easily Create AI Datasets for Fine-Tuning an AI",
    color_name="red-70"
)

# Horizontal menu
selected = option_menu(
    menu_title=None,
    options=["Generate Prompt", "Analyze File", "Generate Test Data", "Help"],
    icons=["robot", "file-earmark-text", "database", "question-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Generate Prompt":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Generate AI/LLM Prompt")
        task = st.text_area("Enter your question or task:", height=100, key="task_input", help="Click 'Generate Prompt' Button below")
        variables = st.text_input("Enter input variables (comma-separated):", key="variables_input")
        
        # Add example input variables
        st.markdown("""
        **Example input variables:**
        - topic, audience, tone
        - product_name, target_market, unique_selling_point
        - character_name, setting, genre
        """)
        
        if st.button("Generate Prompt", key="generate_button"):
            if task:
                with st.spinner("Generating prompt..."):
                    generated_prompt = generate_prompt(task, variables)
                    if generated_prompt:
                        st.subheader("Generated Prompt:")
                        annotated_text(
                            annotation(generated_prompt, "AI-Generated", "#ff4b4b")
                        )
                        
                        # Download options
                        st.subheader("Download Options")
                        prompt_download = get_download_link(generated_prompt, "generated_prompt.txt", "Download Prompt as TXT")
                        st.markdown(prompt_download, unsafe_allow_html=True)
                        
                        # Create JSONL file
                        jsonl_content = json.dumps({"prompt": generated_prompt, "completion": ""}) + "\n"
                        jsonl_download = get_download_link(jsonl_content, "generated_prompt.jsonl", "Download Prompt as JSONL")
                        st.markdown(jsonl_download, unsafe_allow_html=True)
            else:
                st.warning("Please enter a task.")
    
    with col2:
        st_lottie(lottie_ai, height=300, key="lottie_ai")

elif selected == "Analyze File":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Analyze Uploaded File")
        uploaded_file = st.file_uploader("Upload a CSV, TXT, MD, or Image file", type=["csv", "txt", "md", "jpg", "jpeg", "png"], key="file_uploader")
        
        if uploaded_file is not None:
            if uploaded_file.type.startswith('image'):
                image = process_image(uploaded_file)
                if image:
                    st.image(image, caption="Uploaded Image")
                    # Here you would use any Gemini model to analyze the image
                    st.info("Image analysis functionality not implemented in this version.")
            else:
                file_contents = process_uploaded_file(uploaded_file)
                st.write("File contents:")
                st.code(file_contents, language="plaintext")
            
            analysis_prompt = st.text_area("Enter analysis prompt:", "Analyze the contents of the uploaded file and provide insights.", key="analysis_prompt")
            
            if st.button("Analyze File", key="analyze_button"):
                with st.spinner("Analyzing file..."):
                    analysis_result = generate_prompt(f"{analysis_prompt}\n\nFile contents:\n{file_contents}")
                    if analysis_result:
                        st.subheader("Analysis Result:")
                        annotated_text(
                            annotation(analysis_result, "Analysis", "#afa")
                        )
    
    with col2:
        st_lottie(lottie_analysis, height=300, key="lottie_analysis")

elif selected == "Generate Test Data":
    st.subheader("Generate Test Dataset for Fine Tuning an LLM")
    topic = st.text_input("Enter your text or topic here:", key="test_data_topic")
    num_pairs = st.number_input("Number of conversation pairs to generate:", min_value=1, max_value=100, value=10, step=1, key="num_pairs")
    
    if st.button("Generate Test Data", key="generate_test_data_button"):
        if topic:
            with st.spinner("Generating test data..."):
                test_data = generate_test_data(topic, num_pairs)
                if test_data:
                    st.json(test_data)
                    
                    # Download options
                    st.subheader("Download Options")
                    json_download = get_download_link(json.dumps(test_data, indent=2), "test_data.json", "Download as JSON")
                    st.markdown(json_download, unsafe_allow_html=True)
                    
                    # Create JSONL file
                    jsonl_content = "\n".join(json.dumps(item) for item in test_data)
                    jsonl_download = get_download_link(jsonl_content, "test_data.jsonl", "Download as JSONL")
                    st.markdown(jsonl_download, unsafe_allow_html=True)
        else:
            st.warning("Please enter a topic for test data generation.")

elif selected == "Help":
    st.subheader("How to Use This App")
    st.markdown("""
    1. **Generate Prompt**:
       - Enter your task in the text area.
       - Optionally, provide input variables separated by commas.
       - Click "Generate Prompt" to create an AI-generated prompt.
       - Download the generated prompt as a .txt or JSONL file.

    2. **Analyze File**:
       - Upload a CSV, TXT, Markdown MD, or image file.
       - Enter an analysis prompt to guide the AI.
       - Click "Analyze File" to get insights about the uploaded file.

    3. **Generate Test Data conversation paris and datasets for Fine Tuning AI/LLM Models**:
       - Enter a topic or text for test data (also referred to as synthetic data) generation.
       - Specify the number of conversation pairs to generate.
       - Click "Generate Test Data" to create conversation pairs.
       - Download the generated conversation pairs data as JSON or JSONL

    4. **Sidebar Options**:
       - Enter your Gemini API key.
       - Select the Gemini model version.
       - Adjust temperature and max output tokens for generation.

    5. **Tips for Better Results**:
       - Be specific in your task description.
       - Experiment with different temperature settings.
       - For file analysis, provide clear instructions in the analysis prompt.
    """)

    st.subheader("FAQ")
    faq = {
        "What is the Gemini API?": "The Gemini API is Google's latest and most capable AI model for text generation and analysis.",
        "How do I get an API key?": "You can obtain a Free Gemini API key by signing up at Google AI Studio https://aistudio.google.com.",
        "What file types are supported?": "Currently, the app supports CSV, TXT, Markdown MD, and image file formats for analysis.",
        "Is my data secure?": "Yes! Your data and API key are processed locally and not stored on any servers. Always ensure you're using the app from a trusted source.",
        "What's the difference between the models?": "The flash model is faster and as of Aug 10, 2024 has advanced PDF unstructured text regognition, while the pro models offer larger context windows and more advanced capabilities.",
        "Can I use audio, images or video with all models?": "Yes, all Gemini 1.5 models support multimodal inputs including images, audio, and video.",
        "What are the token limits?": "The flash model has an input limit of 1,048,576 tokens, while the pro models can handle up to 2,000,000 tokens. All models have an output limit of 8,192 tokens."
    }

    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)
            
# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Gregory Kennedy | Powered by Gemini AI")
st.markdown('<a href="https://www.linkedin.com/in/gregorykennedymindfuldude" target="_blank" rel="noopener noreferrer">Contact Gregory</a>', unsafe_allow_html=True)

# Add warning about API key
st.sidebar.warning(
    "Please note: Your API key is not stored and is only used for the current session. "
    "Always keep your API key confidential and do not share it with others."
)

# Add version information
st.sidebar.info(f"App Version: 1.7.0 | Using Gemini Model: {st.session_state.model_version}")

# Debug Information (only visible when running in debug mode)
if os.environ.get("DEBUG_MODE") == "True":
    st.sidebar.subheader("Debug Information")
    st.sidebar.json({
        "Temperature": st.session_state.temperature,
        "Max Output Tokens": st.session_state.max_output_tokens,
        "Model Version": st.session_state.model_version,
        "API Configured": st.session_state.api_configured
    })

# Error Handling
def handle_error(error):
    st.error(f"An error occurred: {str(error)}")
    if os.environ.get("DEBUG_MODE") == "True":
        st.exception(error)

# Wrap main functionality in try-except block
try:
    # Main app logic here (if any additional logic is needed)
    pass
except Exception as e:
    handle_error(e)

# Add a collapsible section for release notes
with st.sidebar.expander("Release Notes"):
    st.markdown("""
     ### Version 1.8.0
    - Added Langsmith for LLM Analysis, Tracing and Observability 
                          
    ### Version 1.7.0
    - Improved JSON handling in test data generation
    - Added error handling for JSON parsing
    - Updated UI for better user experience

    ### Version 1.6.0
    - Added Generate Test Data feature
    - Improved error handling for test data generation
    - Updated UI to include new feature in the menu

    ### Version 1.5.0
    - Added support for newest Gemini 1.5 models
    - Improved error handling and debugging
    - Enhanced user interface and responsiveness
    - Added FAQ section in Help
    
    ### Version 1.4.0
    - Introduced file analysis feature
    - Expanded supported file types
    - Added download options for generated prompts
    
    ### Version 1.3.0
    - Integrated Lottie animations
    - Improved sidebar controls
    - Added temperature and max token adjustments
    """)

# Performance Optimization
@st.cache_data
def load_static_resources():
    # Load any static resources here
    pass

load_static_resources()

@traceable # Langsmith Tracing and Observability

# Ensure all session state variables are initialized
def initialize_session_state():
    default_values = {
        "temperature": 0.5,
        "max_output_tokens": 8000,
        "model_version": "gemini-1.5-pro-flash",
        "api_configured": False,
        "generated_prompts": [],
        "analyzed_files": []
    }
    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_session_state()

# Add this at the very end of your script
if __name__ == "__main__":
    try:
        # Main app execution
        pass
    except Exception as e:
        handle_error(e)