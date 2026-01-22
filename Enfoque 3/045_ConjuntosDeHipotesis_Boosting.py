
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Generar datos de ejemplo
X, y = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador base
base_classifier = DecisionTreeClassifier(max_depth=1)

# Crear el clasificador AdaBoost
boosting_classifier = AdaBoostClassifier(base_classifier, n_estimators=50)

# Entrenar el modelo
boosting_classifier.fit(X_train, y_train)

# Evaluar el modelo
accuracy = boosting_classifier.score(X_test, y_test)
print(f"Precisión del modelo de boosting: {accuracy:.2f}")
