import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_openai import OpenAI

#llm = OpenAI(api_key='sk-proj-ovAgDbPD13b3DErnBIxOT3BlbkFJoUZz7pbArcEmDPdUNl87', model='gpt-4o')
llm = ChatGroq(api_key='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', model='Llama3-70b-8192')

#streamlit view components
with st.form("my_form"):
    st.title('Douyin Comment Analysis')
    text_review = st.text_area('Write me the key value pair') 

    submitted = st.form_submit_button("Submit")
    if submitted:
        
        #1 prompt template
        template = """
        <<s>>
            [INST]
            You are acting as a data analyzer at tiktok company. You are well versed with the concepts of data science, data anlytics, machine
            learning and deep learning. You are expert in analyzing anything given to you. You will be provided with a dictionary of a key value
            pair. The key will be the word and value will be the count of the word. For example ('word':'what': 'count':'20', 'word':'you','count':'87'). Your task is to analyze
            this key value pair. Based on the content, give me the overall percentage of positive, negative, and neutral words. Also, 
            as this is based on the comments of the reviews, try to analyze the key concern word in the key value pair. Also, try to make 
            what does this key value pair mean overall.

            Example:

            You:1, bad:1, good:1, car:1, and:1, breath:1

            positive words = good: 1 , total positive =1
            negative words = bad: 1, total negative =1
            Neutral words = You:1, car:1, and:1, breath:1, total neutral =4  

            percentage positive = no of Positive words/ Total words = 1/6=0.166
            percentage negative = no of negative words/ Total words = 1/6= 0.166
            percentage of neutral words = 1- percentage positive-percentage negative

            key concern:- car, breath,

            comment make up = What can you make from the key value pair. Here it means The car is good but the breath is bad

            Do everything else likewise. You will be provided with much bigger key value pairs. Ana;yze everything and dont miss out on anything.

            Here is the output format


            field 1 named :
            **text_review with value:** {text_review}
            field 2 named :
            **Word Segregated:** positive words, negative words, neutral words
            field 2 named :
            **Percentage of words:** percent positive, percent negative, percent neutral
            Field 3 named : 
            **Key concern words:** key concern
            Review text: '''{text_review}'''
            Field 4 named :
            **Recommendation:** comment make up

            [/INST]
        <</s>>

    

        """

        prompt = PromptTemplate(template=template, input_variables=["text_review","option"])

        llm_chain = LLMChain(prompt=prompt, llm=llm)

        if prompt:
            response = llm_chain.run({"text_review": text_review})
            #json printed
            print(response)
            st.text(response) 

# make an app which takes word and count, and generate negative and positive percentages. Based on this, what the llm can understand