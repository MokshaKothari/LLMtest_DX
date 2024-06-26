import streamlit as st
import openai
import logging

# initialize api key and endpoint
api_base = "https://dxfactor-openai.openai.azure.com/"  
api_key = "ff2303a27c6e48618e17248c4761dfe9"

# logger -> event tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# configure openai api client
openai.api_type = "azure"
openai.api_version = "2024-03-01-preview"
openai.api_base = api_base
openai.api_key = api_key

# predefined categories
categories = ["Employment Discrimination", "Harassment", "Unfair Dismissal", "Other"]

# get response
def get_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            engine="DX-GPT35",  
            messages=[
                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        logging.error(f"Error getting response from OpenAI API: {e}")
        raise

# Streamlit app UI
st.markdown(
    """
    # Equal Employment Opportunity (EEO) Case Management
    *Manages and analyzes EEO cases efficiently*

    <style>
    .case-header {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 5px;
        text-decoration: underline;
    }
    .case-content {
        margin-left: 18px;
        margin-bottom: 10px;
    }
    .delete-button {
        margin-top: 10px;
    }

    h3 {
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 600;
    color: green;
    border: 2px solid lightgrey;
    text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input form
st.sidebar.header(":pencil: Description Box")
case_description = st.sidebar.text_area("Enter your case description here:")

# Submit button functionality
if st.sidebar.button("Submit Case"):
    if case_description:
        logging.info("Case description submitted.")
        
        # Categorization
        category_prompt = f"Categorize the following case description into one of the following categories: {', '.join(categories)}:\n\n{case_description}"
        case_category = get_response(category_prompt)
        logging.info(f"Case categorized as: {case_category}")

        # Summarization
        summary_prompt = f"Summarize the following case description maximum in two concise sentences:\n\n{case_description}"
        case_summary = get_response(summary_prompt)
        logging.info(f"Case summary: {case_summary}")

        # Analysis (entities and sentiments)
        analysis_prompt = f"Extract key entities and sentiments from the following case description:\n\n{case_description}"
        case_analysis = get_response(analysis_prompt)
        logging.info(f"Case analysis: {case_analysis}")

        # In-memory data storage -> list
        if 'cases' not in st.session_state:
            st.session_state.cases = []

        if 'deleted_cases' not in st.session_state:
            st.session_state.deleted_cases = set()

        st.session_state.cases.append({
            "description": case_description,
            "category": case_category,
            "summary": case_summary,
            "analysis": case_analysis
        })

        st.sidebar.success("Your case is processed successfully!")
        logging.info("Case processed and stored successfully.")

# Output
if 'cases' in st.session_state:
    st.header("*Generated Report*")
    for i, case in enumerate(st.session_state.cases):
        if i in st.session_state.deleted_cases:
            st.subheader(f"Case {i+1}")
            st.write(f"**This case has been deleted.**")
        else:
            st.subheader(f"Case {i+1}")
            st.markdown(f"<p class='case-header'>Category</p>", unsafe_allow_html=True)
            st.write(case['category'])
            st.markdown(f"<p class='case-header'>Summary</p>", unsafe_allow_html=True)
            st.write(case['summary'])
            st.markdown(f"<p class='case-header'>Analysis</p>", unsafe_allow_html=True)
            st.write(case['analysis'])
            if st.button(f"Delete Case {i+1}", key=f"delete_button_{i}"):
                st.session_state.deleted_cases.add(i)
                logging.info(f"Case {i+1} deleted.")
                st.rerun() #re-run from top