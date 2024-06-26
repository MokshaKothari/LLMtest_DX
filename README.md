# EEO Case Management with Streamlit and OpenAI GPT 3.5

This project is a Streamlit web application that manages and analyzes Equal Employment Opportunity (EEO) cases. It leverages OpenAI's GPT 3.5 Language model to categorize, summarize, and analyze case descriptions.

## Features

- **Case Categorization**: Automatically categorizes case descriptions into predefined categories i.e: ["Employment Discrimination", "Harassment", "Unfair Dismissal", "Other"]
- **Case Summarization**: Generates concise summaries of case descriptions.
- **Case Analysis**: Extracts key entities and sentiments from case descriptions.
- **Case Management**: Allows users to view and delete processed cases.

## Prerequisites

- Python 3.6+
- An OpenAI account with access to the necessary API keys.
- Workspace - preferably VS Code

## Installation

1. **Clone the Repository**

    ```sh
    git clone <repository_link>
    cd <repository_directory>
    ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

    ```sh
    python -m venv venv
    ```

    - Activate the virtual environment:
        - On Windows:
          ```sh
          venv\Scripts\activate
          ```
        - On macOS and Linux:
          ```sh
          source venv/bin/activate
          ```

3. **Install Dependencies**

    ```sh
    pip install streamlit openai
    ```
    Or, simply hit "pip install -r requirements.txt" in command prompt after saving all the dependencies in requirements.txt

4. **Technologies used**

    - Python -> Programming language; python 3.6+
    - Streamlit -> Chat Interface
    - GPT 3.5 -> Large Language Model
    - Additionally, 
    -     Storage -> in-memory; using list []
    -     Minimum styling -> css; using st.markdown()
    -     Logging -> event tracking and debugging

5. **Run the Streamlit App locally**

    run the following command in command prompt 

    ```sh
    streamlit run model.py
    ```

6. **Interact with the Application**

    - As soon as you hit "streamlit run model.py", it redirects you to a web browser typically `http://localhost:8501`on localhost.
    - In the opened web browser, use the sidebar to enter a case description within input form and submit it using the "Submit Case" button.
    - A Report is generated where you can view the categorized, summarized, and analyzed case details in the main interface.
    - Use the "Delete Case" button to remove cases from the list as needed.

## Test Cases

Sample Test cases are given in "testcases.txt" for testing purpose.

## Documentation

A fairly detailed documentation file namely "Documentation.pdf" is uploaded that includes:
- Abstract
- Problem Statement
- Approach
- Code Workflow (Diagram & Breakdown)
- Assumptions
- Advantages and Uniqueness
- Timechart
- Vision

## Output Screenshots

The design is kept simple, this project focuses more on the code working.
Screenshots of the output are uploaded in the "Screenshots" folder. It includes a sceenshot of simple UI and a full page shot.

## Code Workflow

Refer to "Workflow.png" for a workflow diagram of the code.