#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import googletrans as gt

import pytesseract as pst


# In[2]:


recogniser=sr.Recognizer()
man=pyttsx3.init()
trans=gt.Translator()


# In[3]:


pst.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[4]:


def voice_text():
    with sr.Microphone() as source:
        print("wait for connection")
        recogniser.adjust_for_ambient_noise(source,duration=2)
        print("you can speak now")
        voice=recogniser.listen(source)
        print("we reach your voice")
        text=recogniser.recognize_google(voice)
        text=text.lower()
        return text


# In[5]:


def translate(text):
    print("TRANSLATION")
    print("\n",gt.LANGCODES)
    lan=input("\n enter the translation language code = ")
    output=trans.translate(text=text,dest=lan)
    print(output.text,output.pronunciation)
    


# In[6]:


def speak(text):
    man.setProperty("rate",100)
    man.say(text)
    man.runAndWait()
    


# In[7]:


def image():
    img=input(r"enter your image directory")
    text=pst.image_to_string(img)
    return text


# In[13]:



    print(""" enter the input option
             1.text
             2.audio
             3.image""")
    opt=int(input("enter your options ="))
    if opt==1:
        text=input("enter your text")
    elif opt==2:
        text=voice_text()
    elif opt==3:
        text=image()
        
    else:
        pass
    print(""" enter you output option
               1.Translate the text
               2.tranlate into audio
               3.speak the text
               4.text 
               """)
    opt=int(input("enter the option"))
    if opt==1:
        translate(text)
    elif opt==2:
        text=translate(text)
        print(text)
        text=text.pronunciation
        speak(text)
    elif opt==3:
        speak(text)
    elif opt==4:
        print("output=",text)
    else:
        pass
        

    


# In[ ]:




