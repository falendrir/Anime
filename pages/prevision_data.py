# Calcul du score en fonction des episodes, de la durée et de la popularité

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "anime_seasonal_20251122.csv"
df_anime = pd.read_csv(CSV_PATH)

y = df_anime['score']
X = df_anime[['duration', 'popularity', 'episodes']]

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# instantiation
scaler = StandardScaler()

# fit du transformateur : le scaler apprend la moyenne etl'écart-type de chacune des features
scaler.fit(X_train)

# on transforme train et test de la même manière en utilisant le scaler fitté sur le train
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Imports and model training

# instantiate model
lin_reg_scaled = LinearRegression()

lin_reg_scaled.fit(X_train_scaled, y_train)
r2_scaled = lin_reg_scaled.score(X_test_scaled, y_test)
print(r2_scaled)