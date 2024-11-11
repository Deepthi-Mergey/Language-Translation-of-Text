import streamlit as st
from googletrans import Translator, LANGUAGES
import pyttsx3
from IPython.display import Audio
import os
from pathlib import Path
from gtts import gTTS


#set page title and configuration
st.set_page_config(page_title = "Text Language Translation")

#Apply custom CSS using st.markdown()
st.markdown(
    """
    <style>
    /* Add custom CSS here */
    .title {
        font-size: 2em;
        color: darkblue;
        text-align: center;
        padding: 28px;
        background-color: plum;
        border-radius: 18px;
        box-shadow: 2px 2px 5px 8px rgba(0,0,0,0.1);
    }
    
    .text {
        font-size: 1.2em;
        color: #333333;
    }
    
    .stbutton>button {
        background-color: #1f77b4;
        color: white;
        padding: 18px 28 px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    
    </style>
    """,
    unsafe_allow_html = True
    
)

#render styled elements
st.markdown('<h1 class = "title">Text Language Translation</h1>', unsafe_allow_html=True)
st.markdown('<p class = "text">This is a Text Language Translation UI. You can change it to your preferred language ! </p>', 
            unsafe_allow_html=True)

#initialize the translator
translator = Translator()

#Text input for the text to be translated
text_to_translate = st.text_area("Hi, Please enter the text here to translate")


if st.button("Convert and save Audio"):
    if text_to_translate:
       
        #Define save path
        save_directory = "generated_audio"
        Path(save_directory).mkdir(exist_ok=True) #create directory if it doesn't exist
        save_path = os.path.join(save_directory, "Lang_Trans_Input.mp3")
        
        #Convert text to speech
        tts = gTTS(text=text_to_translate, lang='en')
        
        # Save the audio file
        tts.save(save_path)
        
        # Display success message and file path
        st.success("Text-to-Speech audio file saved successfully!")
        st.write("Saved file path:", save_path)
        
        # Play the saved audio file
        st.audio(save_path, format="audio/mp3", start_time=0)
    else:
        st.error("Please enter some text to convert.")
        
#Add some additional instructions or information
st.write("Enter text in the text area above, select source and target languages and click 'Translate' to see the translation.")

#Dropdowns for selecting source and target languages
source_language = st.selectbox("Select your source language", list(LANGUAGES.values()), 
                               index = list(LANGUAGES.keys()).index('en'))
target_language = st.selectbox("Select the target language you want", list(LANGUAGES.values()), 
                               index = list(LANGUAGES.keys()).index('es'))

#language codes
source_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_language)]
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]


#Translate button
if st.button("Translate"):
    #tts = gTTS(text=text_to_translate, lang='en')
    if text_to_translate:
        try:
            #Translate the text
            translation = translator.translate(text_to_translate, src = source_language_code, dest = target_language_code)
            #Display the translated text
            st.write("Translated Successfully !")
            st.write(f"**Your Translated Text:**-----{translation.text}")
            #Define save path
            save_directory = "generated_audio"
            Path(save_directory).mkdir(exist_ok=True) #create directory if it doesn't exist
            save_path = os.path.join(save_directory, "Lang_Trans_Ouput.mp3")
        
            #Convert text to speech
            tts1 = gTTS(text=translation.text, lang='en')
        
            # Save the audio file
            tts1.save(save_path)
        
            # Display success message and file path
            st.success("Translated-Text-to-Speech audio file saved successfully!")
            st.write("Saved file path:", save_path)
        
            # Play the saved audio file
            st.audio(save_path, format="audio/mp3", start_time=0)
            
        except Exception as e:
                st.error("An error occured during Translation")
                st.write(f"Error details: {e}")
    else:
        st.error("Please enter some text to translate")
        

        

        
        
    
        
       

