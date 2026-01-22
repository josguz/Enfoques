
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador de árbol de decisión (K-DT)
classifier = DecisionTreeClassifier()

# Entrenar el modelo
classifier.fit(X_train, y_train)

# Evaluar el modelo
accuracy = classifier.score(X_test, y_test)
print(f"Precisión del clasificador de árbol de decisión: {accuracy:.2f}")
