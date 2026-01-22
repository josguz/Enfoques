
class DecisionTree:
    def __init__(self):
        self.tree = {}

    def fit(self, data, target):
        # Suponiendo que data es un diccionario donde las claves son características
        # y target es la etiqueta correspondiente
        features = list(data.keys())
        self.tree = self._build_tree(data, target, features)

    def _build_tree(self, data, target, features):
        if len(set(target)) == 1:
            return target[0]  # Retornar la etiqueta si es pura

        if not features:
            return max(set(target), key=target.count)  # Retornar la más común

        # Elegir la mejor característica (simplificado)
        best_feature = features[0]
        tree = {best_feature: {}}

        for value in set(data[best_feature]):
            subset = {k: v for k, v in data.items() if v[best_feature] == value}
            subset_target = [target[i] for i in range(len(target)) if data[best_feature][i] == value]
            subtree = self._build_tree(subset, subset_target, features[1:])
            tree[best_feature][value] = subtree

        return tree

    def predict(self, instance):
        current_node = self.tree
        while isinstance(current_node, dict):
            feature = list(current_node.keys())[0]
            value = instance[feature]
            current_node = current_node[feature].get(value, None)
            if current_node is None:
                return None  # No se puede hacer una predicción
        return current_node

# Crear un árbol de decisión
data = {
    'Temperatura': ['Frío', 'Frío', 'Cálido', 'Cálido'],
    'Humedad': ['Alta', 'Baja', 'Alta', 'Baja'],
}

target = ['No', 'No', 'Sí', 'Sí']

tree = DecisionTree()
tree.fit(data, target)

# Hacer predicciones
prediction = tree.predict({'Temperatura': 'Cálido', 'Humedad': 'Baja'})
print("Predicción:", prediction)
