from book import Book
from recipe import Recipe

tourte = Recipe("Tourte", 2, 30, ['beurre', 'champignons', 'poulet'], "miam", "lunch")

cheesecake = Recipe("Cheesecake", 1, 45, ['CheeseCream', 'Cream', 'Speculoos', 'Vanille', 'Beurre'], "Émiettez les biscuits spéculoos ou bastogne à l'aide d'un robot mixeur ou d'un rouleau à pâtisserie. Le but est d'obtenir des miettes assez fines mais pas de la poudre", "dessert")

tiramisu = Recipe("Tiramisu", 3, 25, ['Cafe', 'Biscuits Cuilleres', 'mascarpone', 'creme fraiche épaisse'], "penser à bien fouetter la creme et le mascarponne de manière à obtenir une consistance chantilly", "dessert"
)


print(tourte , cheesecake , tiramisu)
necroMiBon = Book()

print(necroMiBon)
necroMiBon.add_recipe(tourte)
print(necroMiBon)
necroMiBon.add_recipe(tiramisu)
print(necroMiBon)
necroMiBon.add_recipe(cheesecake)
print(necroMiBon)

necroMiBon.get_recipes_by_types("lunch")
necroMiBon.get_recipes_by_types("dessert")
necroMiBon.get_recipes_by_types("starter")

necroMiBon.get_recipe_by_name("cheesecake")
necroMiBon.get_recipe_by_name("Cheesecake")
