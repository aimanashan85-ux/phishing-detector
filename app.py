import streamlit as st 
import pandas as pd 
from sklearn.pipeline import Pipeline 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes import MultinomialNB 
# Page settings 
st.set_page_config( 
page_title="AI Phishing Detector", 
page_icon=" " 
) 
st.title("AI Phishing Email Detector")
st.write("Check a message for potential spam or phishing.") 
# Sample training data for demonstration 
messages = [ 
"Hello, how are you today", 
"Your university class starts at 9 AM", 
"Meeting scheduled for tomorrow", 
"Please find the attached assignment", 
"Your payment receipt is ready", 
"Congratulations you won a free prize click now", 
"Claim your free reward immediately", 
"Win cash now limited offer", 
"You have won a lottery send your details", 
"Get free gifts by clicking this link", 
"Your bank account is blocked verify your password", 
"Urgent click here to verify your bank account", 
"Confirm your password to avoid account suspension", 
"Your account is suspended click this link", 
"Update your banking details immediately" 
] 
labels = [ 
"Safe", 
"Safe", 
"Safe", 
"Safe", 
"Safe", 
"Spam", 
"Spam", 
"Spam", 
"Spam", 
"Spam", 
"Phishing", 
"Phishing", 
"Phishing", 
"Phishing", 
"Phishing" 
] 
 
# Build the AI pipeline 
model = Pipeline([ 
    ("tfidf", TfidfVectorizer()), 
    ("classifier", MultinomialNB()) 
]) 
 
# Train the model 
model.fit(messages, labels) 
 
# User input 
email_text = st.text_area( 
    "Paste your email or message here:" 
) 
 
# Analyze button 
if st.button("Analyze Message"): 
 
    if email_text.strip(): 
 
        prediction = model.predict([email_text])[0] 
 
        st.subheader("Analysis Result") 
 
        if prediction == "Phishing": 
            st.error("    Phishing-like message detected!") 
 
        elif prediction == "Spam": 
            st.warning("🚫 Potential spam detected!") 
 
        else: 
            st.success("✅ Classified as Safe") 
 
        st.info( 
            "This is an educational prototype. " 
            "Predictions may be incorrect." 
        ) 
 
    else: 
        st.warning("Please enter a message first.") 