import langchain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain_community.llms import HuggingFaceHub
import pickle
import pandas as pd
import streamlit as st
import os


os.environ["OPENAI_API_KEY"] = os.getenv('OpenAI_API_Key')

uri_plot = '''The first chapter opens up with an ambush in June 2015 on the convoy of the Indian Army troops in Chandel, Manipur by NSCN(K) militants.
In retaliation, Major Vihaan Singh Shergill, a Para SF officer and his unit, including his brother-in-law, Major Karan Kashyap, infiltrate and attack the Northeastern militants and also kill the key leader responsible for the ambush.
After a successful strike, the Prime Minister of India congratulates him and the whole unit at a formal dinner. Vihaan requests an early retirement as he wants to be close with his mother, who is suffering from Stage VI Alzheimer's, on which
the Prime Minister offers him a desk job at New Delhi near his mother instead of retirement, to which he agrees.An Unsettling Peace (New Delhi, India)The second chapter shows Vihaan taking a desk job at the Integrated Defence Staff HQ in New Delhi and him spending time with his family.
This segment also briefly describes the Pathankot attack. A nurse named Jasmine D'Almeida is assigned to take care of Vihaan's mother. Vihaan meets an Indian Air Force pilot named Flight Lieutenant Seerat Kaur, who is trying to prove her patriotism to her martyred husband, who was an army officer who died in an ambush.
One day, Vihaan's mother goes missing. He searches for her, and blames Jasmine for her ignorance, stating that there is no need for her security. Vihaan's mother is found under a bridge, and Jasmine reveals herself as an intelligence agent. The film reveals why the families of the special forces soldiers were given security due to the threat from the North-eastern terrorists.
An Unsettling Peace (New Delhi, India)The second chapter shows Vihaan taking a desk job at the Integrated Defence Staff HQ in New Delhi and him spending time with his family. This segment also briefly describes the Pathankot attack. A nurse named Jasmine D'Almeida is assigned to take care of Vihaan's mother. Vihaan meets an Indian Air Force pilot named Flight Lieutenant Seerat Kaur,
who is trying to prove her patriotism to her martyred husband, who was an army officer who died in an ambush. One day, Vihaan's mother goes missing. He searches for her, and blames Jasmine for her ignorance, stating that there is no need for her security. Vihaan's mother is found under a bridge, and Jasmine reveals herself as an intelligence agent.
The film reveals why the families of the special forces soldiers were given security due to the threat from the North-eastern terrorists.
Bleed India with Thousand Cuts (Uri, Jammu Kashmir, India) On 18 September 2016, four heavily armed militants attack the brigade headquarters at Uri, Jammu and Kashmir at dawn, killing 19 soldiers in their sleep. The terrorists are killed, but Karan dies in a grenade explosion due to accidentally pulling the pin attached to the terrorist's rifle, which he picked up to examine.
The whole family becomes devastated, including Vihaan. The Ministry decides to take strict action against the perpetrators of the attack. National Security Advisor Govind Bharadwaj suggests the idea of a surgical strike. The Prime Minister gives it a go and gives ten days for the strike. Vihaan leaves his desk job and leaves for Northern Command base in Udhampur.
He requests Chief of the Army Staff General Arjun Singh Rajawat to count him in the operation to which he agrees. Vihaan chooses the elite Ghatak Force commandos from the Bihar Regiment, and the Dogra Regiment along with the special forces as most of the soldiers killed in the attack were from these regiments.
Vihaan informs them that they can no longer use their phones and disguises the mission as regular training exercises. The commandos begin their training'''

animal_plot = '''Ranvijay "Vijay" Singh is the son of Balbir Singh, a powerful Delhi-based industrialist. Despite Balbir being a strict father, Vijay's love for his father is deep and abiding. Balbir doesn't know about his son's devotion for him due to his busy schedule, which also keeps him from spending time with his family.
One day, Balbir expels Vijay to a boarding school in the USA when Vijay threatens the bullies of his elder sister Reet with an AK-47. Vijay finishes his education and returns home after several years. During Balbir's birthday party, Vijay gets into an argument with his brother-in-law Varun, prompting Balbir to expel him from the house again. Vijay marries his childhood girlfriend Geetanjali and the couple cuts ties with their families and moves to the USA.
Eight years later, Vijay, Geetanjali and their two kids return to India upon learning that Balbir had an assassination attempt. Vijay reconciles with his family and takes it upon himself to uncover the assassin's identity. He rounds up his cousins from the village for backup and recruits a body double for his father, who is eventually killed by a gangster named Asrar Haque. Vijay discovers Varun's role in the assassination attempt and kills him publicly at a conference, where Asrar is also present.
Asrar and his assailants launch an attack on Vijay and his cousins at a hotel, when Vijay was at a meeting between him and arms dealer Freddy. Vijay takes them all down and kills Asrar, but gets severely wounded and became bedridden. He wakes up after two weeks and undergoes a heart transplant for his failing heart. Vijay recuperates after several months and is approached by Zoya, the fiancée of his heart donor. Vijay starts an extramartial affair with Zoya, who eventually reveals that she was sent by Asrar's brother Abrar Haque to honey trap him, but Vijay had already knew this and played along to learn the mastermind's identity.
Vijay learns from his grandfather Rajdheer Singh that Abrar and his brothers are Vijay's second cousins. They are the grandchildren of Shamsher Singh, Rajdheer's younger brother. Rajdheer had renounced Shamsher for his immoral antics. Shamsher's son Azim, who had converted to Islam, was denied any share in Balbir's assets, which prompted Shamsher to commit suicide by setting himself on fire. Abrar, who had witnessed his grandfather's suicide, became mute from the trauma. Abrar has relocated to Scotland and has been plotting to seek vengeance against Balbir.'''

golmaal_plot = '''Laxman is a brilliant student who is diverted from his studies by his mischievous band of friends, Gopal, Madhav, and Lucky. Gopal is the muscle of the group, Madhav is the brain, and Lucky is the right one but a mute. The foursome are indebted to a criminal/garage owner named Vasooli, who is constantly pursuing them. They use Laxman's hostel room for their mischievous activities.
Laxman is peer-pressured into running a series of scams to earn himself and his friends some money and they are punished by being thrown out of college. During a short halt in the woods during the night, each one of them reveals their past. Laxman's mother used to work as a maid for a government officer. Madhav had a rough childhood, having been a witness to the constant fights between his parents. Lucky's father had abandoned him and his mother and remarried. Lucky's father's stepchildren used to ridicule Lucky's mutism. Gopal reveals that he is an orphan who was raised in the Jamnadas Orphanage. Vasooli and his gang track down the group in the woods and chase them. The naughty foursome then finds refuge in the bungalow of a blind couple, Somnath and Mangala, who are waiting for their grandson, Sameer, inheriting their paternal grandparents' treasure chest hidden in the old couple's house. Gopal pretends to be Sameer returning from America, and enters the house, while the other three friends sneak in hidden. A cat-and-mouse game unfolds as Laxman's body and Gopal's voice make up Sameer. Each time the blind couple comes amidst them, hilarious situations arise. Enter Nirali, the saucy girl-next-door, and the group now have time, place and 'resources' to fall in love. Their efforts at winning the lady's heart fail. Meanwhile, a gangster named Babli wants to steal the chest from the couple's bungalow, but all of his men's attempts are thwarted by the foursome, sometimes unintentionally and unknowingly.
After the foursome finds the chest hidden behind an old painting in the house, despite Laxman pleading not to open it. Somnath then opens a chest consisting of four items : a compass box, a toy gun, a toy car and an urn which contains ashes. It is revealed that these are Sameer's ashes. Somnath then reveals Sameer's death to Gopal, Laxman, Madhav, and Lucky. The real Sameer, along with his parents, was killed in a car crash on their way to India to meet his grandparents, after Somnath's son learned that Somnath and Mangala were permanently blinded in an accident. Somnath, with help from his friend, a police commissioner, went to America and lit the pyres of his son, daughter-in-law and grandson, the ashes of whom he later kept in an urn, as per the Hindu tradition, which he kept in the chest. Mangala overhears the entire story and is shocked; she breaks into tears and condemns her husband for lying to her all those years and not allowing her to cradle her grandson or light the pyres, while also criticizing the foursome for tricking them and hurting her feelings. Babli then arrives with his gang and later reveals that he hid diamonds in the urn Somnath was carrying as he returned to India. Pandurang, an assassin previously sent by Babli as an undercover servant, later joins Gopal's side on hearing about Sameer's truth and fights the gangsters off, with Vasooli getting caught in the commotion after finally tracking the foursome to the blind couple's house. The fight finally ends with Gopal being accidentally stabbed by Babli in his butt with a knife, and falling unconscious soon after, but not before warning Madhav, Lucky and Laxman to not touch the knife, leaving the three friends in laughter. Babli also falls unconscious after seeing blood flowing from Gopal's butt.
After being admitted to a hospital, Gopal finally has the knife removed from his butt, and Babli is arrested for his crimes. Laxman, Gopal, Madhav and Lucky are then rewarded with ten per cent of the original value of the diamonds for arresting Babli. Nirali then chooses Lucky as her husband-to-be, saying that she wants a partner who only listens to her, and she found true love and loyalty in him and him alone, leaving the remaining three disappointed and waiting for a long time as Nirali has a sister being only 7 years old.
'''

def get_response(llm,plot,question,prompt):
    
    template = f'''you are the movie survey assistant,ask this question to user like {question}'''
    
    prompt = PromptTemplate(input_variables=["plot","prompt",'question'],template=template)
    
    response=llm(prompt.format(plot = plot,prompt= prompt,question = question,messages=st.session_state.messages))
    
    return response

def store_pickel_data(state):
    with open('data/session_state.pkl', 'wb') as f:
        pickle.dump(state, f)
        return
        
def load_pickle_data(filename):
            with open(filename, "rb") as f:
                data = pickle.load(f)
            return data   
         
def save_pickle_data_to_csv(data, filename):
    df = pd.DataFrame(data['messages'])
    df.to_csv(filename,index=True)

def load_llama_2_7b_llm():
    llm = Ollama(model="llama2:latest")
    return llm

def load_mistral_7b_llm():
    llm = Ollama(model="mistral:latest")
    return llm

def load_openai_llm(openai_api_key):
    llm = OpenAI(api_key=openai_api_key,temperature=0.1,max_tokens=100)   
    return llm

def load_gemma_llm():
    llm = Ollama(model='gemma:latest')
    return llm

def load_phi_2_llm():
    llm = Ollama(model ='phi:2.7b')
    return llm

def next_question(questions, current_index):
    """
    Retrieves the next question from a list of questions.

    Args:
    - questions (list): List of questions.
    - current_index (int): Index of the current question.

    Returns:
    - next_question (str): The next question from the list.
    - next_index (int): Index of the next question.
    """
    next_index = current_index + 1
    if next_index < len(questions):
        return questions[next_index], next_index
    else:
        return None, None



# Example usage
movie_survey_questions = [
        'What kinds of genres do you enjoy watching in movies?',
        'Who is your favorite actor/actress?',
        'What is your favorite movie of all time?',
        'How often do you watch movies?',
        'Do you prefer watching movies at home or in the cinema?',
        'What factors influence your decision to watch a movie (e.g., reviews, trailers, recommendations)?',
        'Have you ever walked out of a movie theater during a movie? If yes, why?',
        'Do you prefer watching movies alone or with friends/family?',
        'Are you a fan of sequels and franchises, or do you prefer standalone movies?',
        'What is the most recent movie you watched, and what did you think of it?',
        'What kinds of genres do you like in a movie?',
        'Whose acting did you like the most in the movie?',
        'How do you feel about the storyline of the movie?',
        'Would you recommend this movie to others?',
        'Which part of the movie did you enjoy the most?'
]


def count_user_messages(message_list):
    """
    Counts the number of messages where the role is 'user' from a list of dictionaries.

    Args:
    - message_list (list): List of dictionaries containing messages.

    Returns:
    - count (int): Number of messages where the role is 'user'.
    """
    count = 0
    for message in message_list:
        if message.get('role') == 'user':
            count += 1
    return count


with st.sidebar:
    st.title("💬 Survey Chatbot")
    st.caption("🚀 A Survey chatbot powered by Langchain")
    openai_api_key_pass = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    openai_api_key = os.environ["OPENAI_API_KEY"]
    Start = st.text_input("Password",type='password')
    Submit = st.button("Submit")
    if Submit:
        if Start == 'start':
           st.info('login successfully')
        else:
           st.info('Wrong password')
         
    model = st.sidebar.radio("Choose a LLM model:", ('chatgpt-turbo-3.5','gemma-7b','llama2-7b','mistral-7b','phi-2.7b'))
    clear = st.button("Clear Chat")
    if clear:
        st.session_state.messages = [{"role": "AI", "content": "Hey Hi I'am Yours Movie Survey Assistant !"}]
        
st.title("💬 Survey Chatbot")                
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "AI", "content": "Hey Hi I'am Yours Movie Survey Assistant !"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

st.markdown("""
        <style>
               .block-container {
                    padding-top: 32px;
                    padding-bottom: 32px;
                    padding-left: 5;
                    padding-right: 5;
                }
                .element-container img {
                    background-color: #500000;
                }
                .main-header {
                    font-size: 50px;
                }
                .st-emotion-cache-4oy321 {
                    flex-direction: row-reverse;
                    text-align: right;
                }
        </style>
        """, unsafe_allow_html=True)    

        
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    if Start != 'start':
        st.info("Type password to continue.")

    if Start == 'start': 
        if model == 'chatgpt-turbo-3.5':
            llm = load_openai_llm(openai_api_key)
        if model =='llama2-7b':   
            llm = load_llama_2_7b_llm()
        if model == 'mistral-7b':    
            llm = load_mistral_7b_llm()
        if model == 'gemma-7b':
            llm = load_gemma_llm()  
        if model =='phi-2.7b':
            llm  = load_phi_2_llm() 
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    current_index = 0
    user_message_count = count_user_messages(st.session_state['messages'])
    current_index = user_message_count - 1
    question, current_index = next_question(movie_survey_questions, current_index)
    
    with st.spinner('Processing...'):
        msg = get_response(llm,golmaal_plot,question,prompt)
    st.session_state.messages.append({"role": "AI", "content": msg})
    st.chat_message("assistant").write(msg)

store_pickel_data(st.session_state)    
pickle_data = load_pickle_data("data/session_state.pkl")
save_pickle_data_to_csv(pickle_data,"data/data.csv")