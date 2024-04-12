# Movie Survey Bot with Streamlit and Langchain

## Overview
The Movie Survey Bot is a conversational chatbot designed to conduct surveys related to movies based on plot provied.
It asks users a series of follo-up questions about movie based on plot and gathers their responses ,based on response generate new suvery question.

## Features
- Asks users a series of movie-related questions from Movie plot.
- Collects user responses and displays them generate new question on user Response.
- Provides a conversational experience for users.

## Usage
1. Clone the repository:
   ``` bash
   git clone https://github.com/chaitanyasisodiya/Movie-survey-bot.git
   cd Movie-survey-bot
   
## Install the required dependencies:   
pip install -r requirements.txt

## Run the application:
- `streamlit run surveybot_dynamicQandA.py` : Run the converstional chabot without passing static movies survey question into chatbot.
- `streamlit run surveybot_staticQandA.py ` : Run the converstional chabot with passing static movies survey question into chatbot.

## Directory Structure
- `surveybot_dynamicQandA.py`: Main Streamlit application file ,genration of dynamic survey question based on plot.
- `surveybot_staticQandA.py`: Main Streamlit application file for genrating static survey question.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation file (you're reading it!).
- `.env`: which contents openai credentials like - apikey.
- `Data folder`: consist of pickel file and csv file for storing history data.
- `snapshot folder`: consist of snapshot for working chabtot

## Dependencies
- Streamlit: [Streamlit documentation](https://docs.streamlit.io/)
- Langchain: [Langchain documentation](https://github.com/langchain/langchain)
- Openai:[langchain_openai]

## LLM model from Openai using openai apikey:
- `chatgpt-turbo-3.5`: from Openai

## local hosted open source LLM models using Ollama platfrom.
- `gemma-7b`: from google
- `llama2-7b` from meta
- `mistral-7b`:from mistral
- `phi-2-7b`: from microsoft


## Contributors
- [chaitanya girase](https://github.com/your-username)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.