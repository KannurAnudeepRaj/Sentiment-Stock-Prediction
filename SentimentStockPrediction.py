# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from textblob import TextBlob  # For sentiment analysis

# Load and preprocess data (Dummy data used here for illustration)
stock_data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'ClosePrice': [100, 105, 110, 95, 102, 98, 115, 120, 105, 110],
})

news_data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'News': ["Positive news today.", "Stocks are falling.", "Great earnings report.", "Market is uncertain.", "Investors optimistic.", "Company expands operations.", "Economic downturn.", "New product launch.", "Mixed market sentiments.", "Positive outlook for the future."]
})

# Sentiment Analysis
news_data['Sentiment'] = news_data['News'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Merge stock and sentiment data
merged_data = pd.merge(stock_data, news_data, on='Date', how='left')

# Feature Engineering
# Here, we are using sentiment as an additional feature. You can add more features.
features = merged_data[['ClosePrice', 'Sentiment']]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(features.drop('ClosePrice', axis=1), features['ClosePrice'], test_size=0.2, random_state=42)

# Model Selection and Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Model Deployment (Optional)
from joblib import dump  # Assuming you want to use joblib to save the trained model

# Save the trained model for future use
model_filename = 'stock_price_prediction_model.joblib'
dump(model, model_filename)
print(f'Model saved as {model_filename}')

# Load the model in another script or application
# loaded_model = load(model_filename)

# Perform real-time predictions with new data
# new_data = pd.DataFrame({'Sentiment': [0.1, -0.2]})
# new_prediction = loaded_model.predict(new_data)
# print(f'Real-time prediction: {new_prediction[0]}')
