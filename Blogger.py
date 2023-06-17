import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config
#import requests


import streamlit.components.v1 as components
from streamlit_javascript import st_javascript
import time


openai.api_key=config.api_key

def main():
    st.title("Evaluate Answers")
    st.subheader('This app has been developed and serviced by InstaDataHelp Analytics Services')
    #st.write('This app has been developed for evauating the answers')
   
    question = st.text_area("Enter the questions")
    answer = st.text_area("Enter your answer here")
    
    content = 'Evaluate the answer of a question out of 10. The question is '+question + '. The answer is ' + answer
        
    
       
    if st.button("Check My Answer"):
        with st.spinner("Generating Result ..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{'role':'user','content':f'{content}\n\nDescription:'}]
                
            )
            
            


            description = response['choices'][0]['message']['content'] 
            st.subheader("Generated Blog Content")
            st.write(description)
        #st.subheader("Modified Content with WordAI to avoid AI Tool Detection")
        #st.write(x.json()['text'])        

            
    else:
        st.write("Payment failed")

        

if __name__ == '__main__':
   main()
