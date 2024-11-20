import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import re
from urllib.parse import urlparse
import tld
from tld import get_tld

def extract_url_features(url):
    """Extract features from the URL for analysis"""
    try:
        # Basic URL features
        length_url = len(url)
        
        # Parse URL
        parsed = urlparse(url)
        hostname = parsed.netloc
        path = parsed.path
        
        # Count various URL characteristics
        nb_dots = url.count('.')
        nb_hyphens = url.count('-')
        nb_at = url.count('@')
        nb_qm = url.count('?')
        nb_and = url.count('&')
        nb_or = url.count('|')
        nb_eq = url.count('=')
        nb_underscore = url.count('_')
        nb_tilde = url.count('~')
        nb_percent = url.count('%')
        nb_slash = url.count('/')
        nb_star = url.count('*')
        nb_colon = url.count(':')
        nb_comma = url.count(',')
        nb_semicolumn = url.count(';')
        nb_dollar = url.count('$')
        nb_space = url.count(' ')
        
        # Check for common suspicious patterns
        has_https = 1 if url.startswith('https://') else 0
        has_http = 1 if url.startswith('http://') else 0
        
        # Check for IP address in URL
        has_ip = 1 if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', hostname) else 0
        
        # Calculate ratio of digits
        nb_digits = sum(c.isdigit() for c in url)
        ratio_digits = nb_digits / len(url) if len(url) > 0 else 0
        
        # Check for suspicious TLD
        try:
            tld_info = get_tld(url, as_object=True)
            tld = tld_info.tld
            suspicious_tld = 1 if tld not in ['com', 'org', 'net', 'edu', 'gov'] else 0
        except:
            suspicious_tld = 1
        
        return {
            'length_url': length_url,
            'nb_dots': nb_dots,
            'nb_hyphens': nb_hyphens,
            'has_https': has_https,
            'has_ip': has_ip,
            'ratio_digits': ratio_digits,
            'suspicious_tld': suspicious_tld,
            'total_special_chars': sum([nb_at, nb_qm, nb_and, nb_or, nb_eq, nb_underscore,
                                      nb_tilde, nb_percent, nb_slash, nb_star, nb_colon,
                                      nb_comma, nb_semicolumn, nb_dollar, nb_space])
        }
    except Exception as e:
        st.error(f"Error analyzing URL: {str(e)}")
        return None

def load_model():
    with open('decision1_tree_model (1).pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def make_prediction(features):
    model = load_model()
    
    expected_features = [
        'google_index',
        'page_rank',
        'web_traffic',
        'nb_hyperlinks',
        'length_url'
    ]
    
    features_df = pd.DataFrame([features], columns=expected_features)
    prediction = model.predict(features_df)[0]
    return prediction

def main():
    st.title("Enhanced Website Phishing Detection System")
    
    # URL Analysis Section
    st.header("URL Analysis")
    url_input = st.text_input("Enter Website URL", "https://example.com")
    
    if url_input:
        url_features = extract_url_features(url_input)
        if url_features:
            st.subheader("URL Analysis Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("URL Length", url_features['length_url'])
                st.metric("Number of Dots", url_features['nb_dots'])
                st.metric("Number of Hyphens", url_features['nb_hyphens'])
                st.metric("HTTPS Present", "Yes" if url_features['has_https'] else "No")
            
            with col2:
                st.metric("Contains IP Address", "Yes" if url_features['has_ip'] else "No")
                st.metric("Ratio of Digits", f"{url_features['ratio_digits']:.2%}")
                st.metric("Suspicious TLD", "Yes" if url_features['suspicious_tld'] else "No")
                st.metric("Special Characters", url_features['total_special_chars'])
            
            # Warning indicators
            if url_features['has_ip']:
                st.warning("⚠️ URL contains an IP address instead of a domain name")
            if url_features['suspicious_tld']:
                st.warning("⚠️ Unusual top-level domain detected")
            if url_features['total_special_chars'] > 10:
                st.warning("⚠️ High number of special characters detected")
            if not url_features['has_https']:
                st.warning("⚠️ Website does not use HTTPS")
    
    # Manual Feature Input Section
    st.header("Additional Website Characteristics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        google_index = st.selectbox("Google Index", [0, 1], help="Is the site indexed by Google? (1=Yes, 0=No)")
        page_rank = st.slider("Page Rank", 0, 10, 5, help="Google Page Rank (0-10)")
        web_traffic = st.slider("Web Traffic Score", 0, 100, 50, help="Website popularity score (0-100)")
    
    with col2:
        hyperlinks = st.number_input("Number of Hyperlinks", min_value=0, help="Total number of links on the webpage")
        # Use URL length from analysis if available
        url_length = url_features['length_url'] if url_features else st.number_input("URL Length", min_value=0)
    
    if st.button("Analyze Website"):
        features = {
            'google_index': google_index,
            'page_rank': page_rank,
            'web_traffic': web_traffic,
            'nb_hyperlinks': hyperlinks,
            'length_url': url_length
        }
        
        try:
            prediction = make_prediction(features)
            
            st.header("Final Analysis Result")
            if prediction == 0:
                st.success("✅ This website appears to be legitimate!")
            else:
                st.error("⚠️ Warning: This website shows characteristics of a phishing site!")
            
            # Display confidence information
            st.info("""
            Factors considered in this analysis:
            - URL structure and characteristics
            - Web presence (Google Index and Page Rank)
            - Traffic patterns
            - Link structure
            
            Always verify website security through multiple means:
            - Check for HTTPS
            - Verify the domain name carefully
            - Look for security certificates
            - Be cautious with personal information
            """)
            
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")

if __name__ == "__main__":
    main()