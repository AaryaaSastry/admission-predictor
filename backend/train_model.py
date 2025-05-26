import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load your dataset
data = pd.read_csv(r'C:/Users/91748/OneDrive/Desktop/admission-predictor/admission_data.csv')

# Feature columns and target column
features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'GPA', 'Research', '12th Score', 'CGPA']
target = 'Admission_Chance'  # Assuming this is the column to predict

X = data[features]
y = data[target]

# Binary Classification Option (uncomment to use binary classification)
# threshold = 0.7  # Define a threshold for admission chance
# y = (y >= threshold).astype(int)  # Convert to 1 if admission chance >= 0.7, else 0

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Choose Model
# Uncomment below for Logistic Regression (classification) or Linear Regression (continuous prediction)
# model = LogisticRegression()  # For binary classification
model = LinearRegression()       # For continuous prediction

# Train the model
model.fit(X_train_scaled, y_train)

# Save the trained model and scaler
joblib.dump(model, 'backend/model/admission_model.pkl')
joblib.dump(scaler, 'backend/model/scaler.pkl')

print("Model and scaler have been saved in the 'backend/model/' directory.")
