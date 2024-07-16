import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

##llm = ChatOpenAI(api_key='sk-proj-ovAgDbPD13b3DErnBIxOT3BlbkFJoUZz7pbArcEmDPdUNl87', model='gpt-4o')

llm = ChatGroq(api_key='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', model='Llama3-70b-8192')


#streamlit view components
with st.form("my_form"):
    st.title('Douyin Comment Analysis')
    text_review = st.text_area('Write me a review') 

    option = st.selectbox(
    'Select the language to evaluate:',
    ('Chinese', 'Spanish', 'English'))
    submitted = st.form_submit_button("Submit")
    if submitted:
        
        #1 prompt template
        template = """
        You are acting as a comment analyzer for a company named Tiktok, you analyze the comments of the users when a livestreamer on the 
        tiktok app sells the product and viewers comment on it. ANd, in the end, give recommendation to the livestreamer on what things he should address to 
        increase the sales of the product, or understand the good or bad qualities of the product, which he can give to the product manager. Also, if the language is chinese, then give both chinese and translated chinese to english keywords.
        If the selected language is english, then give only the english output
        Please act as a machine learning model trained for perform a supervised learning task, 
        for extract the sentiment of a review in '{option}' Language. Also extract the keywords on which users are emphasizing more on.
        

        Give your answer writing a Json evaluating the sentiment field between the dollar sign, the value must be printed without dollar sign.
        The value of sentiment must be "positive"  or "negative", otherwise if the text is not valuable write "null".
        

    

        Example:

        field 1 named :
        **text_review with value:** {text_review}
        field 2 named :
        **sentiment with value:** $sentiment$
        Field 3 named : 
        **language with value:** {option}
        Review text: '''{text_review}'''
        Field 4 named :
        **Recommendation:** 

    

        """

        prompt = PromptTemplate(template=template, input_variables=["text_review","option"])

        llm_chain = LLMChain(prompt=prompt, llm=llm)

        if prompt:
            response = llm_chain.run({"text_review": text_review, "option": option})
            #json printed
            print(response)
            st.text(response) 