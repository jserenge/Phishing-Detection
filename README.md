# 🛡️ Website Phishing Detection System

## 🚀 Overview
The **Website Phishing Detection System** is a machine learning-powered application built with **Streamlit** that analyzes URLs and website characteristics to identify potential phishing threats. It utilizes a **Decision Tree model** trained on key website features for real-time threat assessment.

## 1️⃣ Initial Data Analysis and Preprocessing

### 📊 Dataset Overview
The original dataset contained **88 features** related to website characteristics, including:
- 🌐 **URL-based features** (length, special characters, etc.)
- 🔐 **Domain-based features** (age, registration, etc.)
- 🖥️ **HTML and JavaScript features**
- 📡 **Network-based features**

### 🔄 Data Preprocessing Steps
1. **Data Cleaning**
   - ✅ Checked for missing values
   - 🗑️ Removed duplicates
   - 🔄 Standardized data types

2. **Feature Scaling**
   - Applied **StandardScaler** to normalize numerical features
   - Transformed features to have `mean=0` and `variance=1`
   ```python
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

## 2️⃣ Model Selection Process

### 🏆 Models Evaluated
1. **Logistic Regression** – Basic baseline model, provides probability scores.
2. **Support Vector Machine (SVM)** – Handles non-linear relationships but is computationally intensive.
3. **Random Forest** – Ensemble model with feature importance scores.
4. **Multi-Layer Perceptron (MLP)** – Neural network capturing complex patterns.
5. **Decision Tree** – **Final model** due to:
   - ✅ Good balance of **accuracy & interpretability**
   - 🚀 Fast **prediction time**
   - 📜 Clear **decision rules**

## 3️⃣ Feature Selection

### 🔑 Important Features Identified
1. 🔍 **Google Index** (Is the site indexed by Google?)
2. ⭐ **Page Rank** (Google's ranking)
3. 📈 **Web Traffic** (Site popularity)
4. 🔗 **Number of Hyperlinks**
5. 🔢 **URL Length**

### 🔬 Feature Selection Process
- Used **Decision Tree's feature importance scores**
- Selected **top 5 features** based on importance weights
- Retrained model using selected features
- Maintained performance with a **simplified feature set**

## 4️⃣ Final Model Implementation

### 🏗️ Model Architecture
- **Decision Tree Classifier**
- Trained on **optimized feature set**
- Serialized using **pickle** for deployment

### 📊 Model Performance
- **Balanced precision & recall**
- 🚀 **Fast prediction time**
- 🛡️ **Effective phishing site detection**

## 5️⃣ Web Application Architecture

### ⚙️ Components

#### 🔍 URL Analysis Module
```python
def extract_url_features(url):
    # Extracts features directly from URL:
    # - Length
    # - Special characters
    # - Domain structure
    # - Security indicators (HTTPS)
```

#### 🧠 Model Prediction Module
```python
def make_prediction(features):
    # Loads pickled model
    # Processes input features
    # Returns prediction
```

#### 🖥️ User Interface
- **Built with Streamlit**
- Two main sections:
  1. **URL Analysis**
     - 🔗 **Direct URL input**
     - ⚡ **Automatic feature extraction**
     - 📊 **Real-time analysis display**
  2. **Manual Feature Input**
     - 📌 **Google Index status**
     - ⭐ **Page Rank input**
     - 📈 **Web Traffic metrics**
     - 🔗 **Hyperlink count**
     - 🔢 **URL characteristics**

### 🔄 Data Flow
1. User **inputs a URL** or **manual features**
2. System **extracts URL features** automatically
3. Features are **preprocessed & scaled**
4. **Model makes prediction**
5. Results **displayed with explanations**

## 6️⃣ Deployment Instructions

### 🛠️ Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### 📂 Required Files
- `main.py` → **Main application code**
- `phishing_model.pkl` → **Serialized model**
- `requirements.txt` → **Dependencies**

### ▶ Running the Application
```bash
streamlit run main.py
```

## 7️⃣ Security Considerations

### ⚠️ Model Limitations
- Based on **static website features**
- Requires **regular updates** to adapt to new phishing tactics
- Should be used as part of a **larger security strategy**

### 🔒 Best Practices
1. 🔄 **Regular model retraining**
2. 📊 **Monitor false positives & negatives**
3. 🔗 **Integrate with other security tools**
4. 🎓 **User education on phishing risks**

## 8️⃣ Future Improvements

### 🚀 Potential Enhancements
1. 🌐 **Real-time webpage content analysis**
2. 🔎 **Integration with URL reputation databases**
3. 📈 **Continuous model updates**
4. 🛠️ **Additional feature extraction**
5. 📊 **Enhanced visualization of results**

🛡️ Stay safe online and verify every link! 🚀

