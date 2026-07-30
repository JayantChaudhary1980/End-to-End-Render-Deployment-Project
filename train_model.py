import pickle

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

# Load dataset
housing = fetch_california_housing(as_frame=True)

X = housing.data
y = housing.target

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
with open("model/house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully.")
print("Saved as model/house_price_model.pkl")