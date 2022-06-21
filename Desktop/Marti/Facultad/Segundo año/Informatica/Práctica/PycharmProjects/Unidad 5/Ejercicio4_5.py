recipes = [
    {'recipe': 'Arroz con Verduras', 'ingredients': ['arroz', 'cebolla', 'morron', 'zanahoria', 'castañas', 'zuchini']},
    {'recipe': 'Ensalada de Quinoa',
     'ingredients': ['quinoa', 'huevo', 'cebolla morada', 'tomate', 'morron', 'almendras']},
    {'recipe': 'Carne al Horno', 'ingredients': ['colita', 'papa', 'zanahoria', 'batata', 'cebolla', 'ajo']},
    {'recipe': 'Fideos al Pesto', 'ingredients': ['fideos', 'queso', 'nueces', 'albahaca', 'ajo', 'aceite de oliva']},
    {'recipe': 'Guiso de Lentejas',
     'ingredients': ['lentejas', 'cebolla', 'zanahoria', 'papa', 'carne', 'puerro', 'morron']},
]

ingredients = []


def recipe_recommender():
    recommend_recipes = []

    for input_ingredient in ingredients:
        for recipe_dict in recipes:
            for recipe_ingredients in recipe_dict['ingredients']:
                if recipe_ingredients == input_ingredient:
                    if not(recipe_dict in recommend_recipes):
                        recommend_recipes.append(recipe_dic