from fastapi import APIRouter, HTTPException
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

router = APIRouter(prefix="/data-analysis", tags=["Data Analysis"])

@router.post("/linear-regression")
async def linear_regression(data: pd.DataFrame):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop("target", axis=1), data["target"], test_size=0.2, random_state=42)
    
    # Create and train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the testing set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return {"mse": mse}

@router.post("/clustering")
async def clustering(data: pd.DataFrame):
    # Perform k-means clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(data)
    
    # Get the cluster labels
    labels = kmeans.labels_
    
    return {"labels": labels}
