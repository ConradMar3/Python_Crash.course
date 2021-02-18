favorite_foods = {
'conrad': ['pizza', 'steak'],
'celeste': ['mac&cheese'],
'phil': ['ribs', "pie's"],
'mariaan': ['chicken', 'briskit'],
}

for name, foods in favorite_foods.items():
	print(f"\n{name.title()}'s favorite foods are:")

	for food in foods:
		print(f"\t{food.title()}")