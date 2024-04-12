# Movie Survey Bot with Streamlit and Langchain

## Overview
The Movie Survey Bot is a conversational chatbot designed to conduct surveys related to movies. It asks users a series of questions about their movie preferences and gathers their responses.

## Features
- Asks users a series of movie-related questions.
- Collects user responses and displays them.
- Provides a conversational experience for users.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-survey-bot.git
   cd MOVIE-SURVEY-BOT

   
## Install the required dependencies:   
pip install -r requirements.txt

## Run the application:

# Run the converstional chabot with for without passing static movies survey question.
streamlit run surveybot_dynamicQandA.py 

# Run the converstional chabot with for with passing static movies survey question.
streamlit run surveybot_staticQandA.py 

# File and folder

1. Data folder consist of pickel file and csv file for storing history data.

2. snapshot folder consist of snapshot for chabtot

## Directory Structure
- `surveybot_dynamicQandA.py`: Main Streamlit application file ,genration of dynamic survey question based on previous .
- `surveybot_staticQandA.py`: Main Streamlit application file for static survey question.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation file (you're reading it!).

## Dependencies
- Streamlit: [Streamlit documentation](https://docs.streamlit.io/)
- Langchain: [Langchain documentation](https://github.com/langchain/langchain)

## Contributors
- [chaitanya girase](https://github.com/your-username)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.