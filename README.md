# Simple-Q-A-Chatbot-With-Multiple-Models

This project demonstrates the implementation of a Q&A chatbot using multiple AI language models. The chatbot is built with Streamlit and utilizes the LangChain library for model integration.

## Features
- **Multiple Model Support**: Choose from a variety of language models for generating responses.
- **Customizable Settings**: Adjust the temperature and API key through a user-friendly interface.
- **Streamlit Integration**: A seamless and interactive web application built with Streamlit.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher
- Streamlit Cloud account (optional for deployment)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository/simple-qa-chatbot.git
   cd simple-qa-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.streamlit` folder in your project directory.
   - Inside this folder, create a `secrets.toml` file.
   - Add the following content to the `secrets.toml` file:
     ```toml
     LANGCHAIN_API_KEY = "your_api_key_here"
     LANGCHAIN_TRACING_V2 = "true"
     LANGCHAIN_PROJECT = "Simple Q&A Chatbot with Multiple Models"
     ```

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Configure the Chatbot**:
   - Enter your API key in the sidebar.
   - Select the desired model from the dropdown menu.
   - Adjust the temperature slider as needed.

3. **Ask Questions**:
   - Type your question in the text input field.
   - The chatbot will generate and display a response based on your inputs.

## Code Explanation

### Importing Required Libraries

```python
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv
```
- **langchain_groq**, **langchain_core**, **ChatPromptTemplate**: Libraries for integrating and working with language models.
- **streamlit**: Library for creating the web application.
- **os**: Provides a way of using operating system-dependent functionality.
- **dotenv**: Used for loading environment variables from a `.env` file.

### Load Environment Variables

```python
load_dotenv()
LANGCHAIN_API_KEY = st.secrets['LANGCHAIN_API_KEY']
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_PROJECT = "Simple Q&A Chatbot with Multiple Models"
```
- **load_dotenv()**: Loads the environment variables from the `.env` file.
- **st.secrets**: Access secrets stored in the `.streamlit/secrets.toml` file.

### Setting Up Environment Variables

```python
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Multiple Models"
```
- **os.environ**: Sets environment variables for the application.

### Creating Prompt Template

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the following questions"),
    ("user", "Question:{question}")
])
```
- **ChatPromptTemplate**: Creates a prompt template for the language model, defining the system and user messages.

### Function to Generate Response

```python
def generate_response(question, api_key, engine, temperature):
    llm = ChatGroq(model=engine, api_key=api_key, temperature=temperature)
    output = StrOutputParser()
    chain = prompt | llm | output
    answer = chain.invoke({"question":question})
    return answer
```
- **generate_response**: Function to generate a response from the language model.
  - **question**: User's question.
  - **api_key**: API key for authentication.
  - **engine**: Selected language model.
  - **temperature**: Controls the randomness of the model's output.
  - **chain.invoke**: Calls the model to generate a response based on the input question.

### List of Available Models

```python
model_list = ["gemma-7b-it", "llama-3.1-8b-instant", "mixtral-8x7b-32768", "whisper-large-v3-turbo"]
```
- **model_list**: List of available language models for selection.

### Streamlit Web App Setup

```python
st.title("Simple Q&A Chatbot with Multiple Models")
```
- **st.title**: Sets the title of the Streamlit web app.

### Sidebar Settings

```python
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter API Key:", type='password')
model = st.sidebar.selectbox("Select Model", options=model_list)
temperature = st.sidebar.slider("Select Temperature", min_value=0.00, max_value=1.00, step=0.01)
```
- **st.sidebar**: Creates a sidebar for user input.
  - **text_input**: Field for entering the API key.
  - **selectbox**: Dropdown for selecting the language model.
  - **slider**: Slider for adjusting the temperature setting.

### Main Content

```python
st.write("Ask your question")
user_input = st.text_input("Enter Text")
```
- **st.write**: Displays text in the main content area.
- **st.text_input**: Field for entering the user's question.

### Displaying Response

```python
if user_input and api_key:
    response = generate_response(user_input, api_key, model, temperature)
    st.write(response)
elif user_input:
    st.warning('Please enter API key')
else:
    st.warning("Please enter your question")
```
- **if user_input and api_key**: Checks if both the question and API key are provided.
  - **generate_response**: Calls the function to get the response.
  - **st.write**: Displays the response.
- **st.warning**: Displays a warning if the API key or question is missing.

## Project Structure

- `app.py`: The main application file containing the Streamlit code and chatbot logic.
- `requirements.txt`: The list of required Python packages.
- `.streamlit/secrets.toml`: File to store sensitive information like API keys.

## Example

Here’s an example of how the chatbot interface looks:

![Chatbot Interface](screenshot.png)

## Troubleshooting

- **API Key Issues**: Ensure your API key is correctly placed in the `secrets.toml` file.
- **Model Errors**: Verify that the selected model is available and correctly referenced.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact the repository owner.

---

This README file explains each section of your code and provides a comprehensive guide for setting up and using your project. If there's anything more you'd like to add or adjust, let me know!
