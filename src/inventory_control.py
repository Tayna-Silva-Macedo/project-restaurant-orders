class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.shopping_list = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        available_dishes = self.get_available_dishes()

        if order not in available_dishes:
            return False

        for ingredient in self.INGREDIENTS[order]:
            self.shopping_list[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.shopping_list

    def get_available_dishes(self):
        missing_ingredients = {
            ingredient
            for ingredient in self.shopping_list
            if self.shopping_list[ingredient]
            == self.MINIMUM_INVENTORY[ingredient]
        }

        available_dishes = {
            dish
            for dish, ingredients in self.INGREDIENTS.items()
            if len(set(ingredients).intersection(missing_ingredients)) == 0
        }

        return available_dishes
