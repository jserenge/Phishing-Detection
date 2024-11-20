# Phishing-Detection
PHI
# Website Phishing Detection System Documentation

## 1. Initial Data Analysis and Preprocessing

### Dataset Overview
The original dataset contained 88 features related to website characteristics including:
- URL-based features (length, special characters, etc.)
- Domain-based features (age, registration, etc.)
- HTML and JavaScript features
- Network-based features

### Data Preprocessing Steps
1. Data Cleaning
   - Checked for missing values
   - Removed duplicates
   - Standardized data types

2. Feature Scaling
   - Applied StandardScaler to normalize numerical features
   - Transformed features to have mean=0 and variance=1
   ```python
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

## 2. Model Selection Process

### Models Evaluated
1. Logistic Regression
   - Basic baseline model
   - Good for binary classification
   - Provides probability scores

2. Support Vector Machine (SVM)
   - Effective for high-dimensional data
   - Can handle non-linear relationships
   - More computationally intensive

3. Random Forest
   - Ensemble method combining multiple decision trees
   - Good at handling different types of features
   - Provides feature importance scores

4. Multi-Layer Perceptron (MLP)
   - Neural network approach
   - Can capture complex patterns
   - Requires more tuning

5. Decision Tree
   - Simple and interpretable
   - Can handle both numerical and categorical data
   - Provides clear decision rules
   - Selected as final model due to:
     * Good balance of accuracy and interpretability
     * Fast prediction time
     * Easy to understand decision process

## 3. Feature Selection

### Important Features Identified
The model identified these key features as most important:
1. Google Index (website indexed by Google)
2. Page Rank (Google's ranking)
3. Web Traffic (site popularity)
4. Number of Hyperlinks
5. URL Length

### Feature Selection Process
1. Used Decision Tree's feature importance scores
2. Selected top 5 features based on importance weights
3. Retrained model using only selected features
4. Validated performance maintained with reduced feature set

## 4. Final Model Implementation

### Model Architecture
- Decision Tree Classifier
- Trained on reduced feature set
- Optimized hyperparameters
- Serialized using pickle for deployment

### Model Performance Metrics
- Achieved good balance between precision and recall
- Effective at identifying both legitimate and phishing websites
- Fast prediction time suitable for real-time analysis

## 5. Web Application Architecture

### Components

#### URL Analysis Module
```python
def extract_url_features(url):
    # Extracts features directly from URL:
    # - Length
    # - Special characters
    # - Domain structure
    # - Security indicators (HTTPS)
```

#### Model Prediction Module
```python
def make_prediction(features):
    # Loads pickled model
    # Processes input features
    # Returns prediction
```

#### User Interface
- Built with Streamlit
- Two main sections:
  1. URL Analysis
     * Direct URL input
     * Automatic feature extraction
     * Real-time analysis display
  
  2. Manual Feature Input
     * Google Index status
     * Page Rank input
     * Web Traffic metrics
     * Hyperlink count
     * URL characteristics

### Data Flow
1. User inputs URL or manual features
2. System extracts URL features automatically
3. Features are preprocessed and scaled
4. Model makes prediction
5. Results displayed with explanations

## 6. Deployment Instructions

### Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt
```

### Required Files
- `main.py`: Main application code
- `phishing_model.pkl`: Serialized model
- `requirements.txt`: Dependencies

### Running the Application
```bash
streamlit run main.py
```

## 7. Security Considerations

### Model Limitations
- Based on static features
- Requires regular updates
- Should be used as part of larger security strategy

### Best Practices
1. Regular model retraining
2. Monitoring of false positives/negatives
3. Integration with other security tools
4. User education about phishing risks

## 8. Future Improvements

### Potential Enhancements
1. Real-time webpage content analysis
2. Integration with URL reputation databases
3. Machine learning model updates
4. Additional feature extraction
5. Enhanced visualization of results
