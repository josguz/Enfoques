
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 2.5, 3.5, 3.0, 4.5])

# Crear un árbol de regresión
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# Hacer predicciones
predictions = regressor.predict(np.array([[1.5], [2.5], [3.5]]))
print("Predicciones:", predictions)
