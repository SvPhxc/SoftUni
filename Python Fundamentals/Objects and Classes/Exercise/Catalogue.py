class Catalogue:
    def __init__(self, name):
        self.catalogue = name
        self.products = []
    def add_product(self, poduct_name):
        self.products.append(poduct_name)
    def get_by_letter(self, letter):
        filtered = []
        for i in self.products:
            if i[0] == letter:
                filtered.append(i)
        return filtered
    def __repr__(self):

        result = f"Items in the {''.join(self.catalogue)} catalogue:\n"
        for x in sorted(self.products):
            result += f"{''.join(x)}\n"
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)