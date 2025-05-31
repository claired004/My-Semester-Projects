#Recipe Organizer
#CREATE Task

# Credits to Caroline Stanko's "Our 98 Highest Rated Recipes, Ever" on Taste of Home (https://www.tasteofhome.com/collection/our-100-highest-rated-recipes-ever/?srsltid=AfmBOooOvPHq0SXaEl-i3_5iPsCPfbcD7tvuQnpbB8iTuHJJXo5_wRZM) for all the recipes used in this project

recipes_list = ["CreamyWhiteChili","BananaBread","CheeseburgerSoup","AmishBreakfastCasserole","PumpkinCupcakes","ChickenPotpie","ChickenFajitas","ApplePie","EnchiladaCasserole","ZucchiniPizzaCasserole","Lasagna","CauliflowerSoup","HomemadeBread","ZucchiniCupcakes","CheesyMeatLoaf","TortelliniSoup","FluffyKeyLimePie","StuffedPepperSoup","ChocolateCakeWithVanillaFrosting","MeatLoaf","PigPickinCake","BakedSpaghetti","Cornbread","BakedMushroomChicken","HotMilkCake","MacaroniColeslaw","HamChowder","AppleCrisp","Jambalaya","BananaMuffins","SeafoodLasagna","GrapeSalad","PeanutButterLasagna","PotRoast","PumpkinBread","TacoLasagna","BananaBars","ShrimpScampi","RhubarbCustardBars","PecanCheesecakePie","BeefEnchiladas","ChunkyAppleCake","CornPudding","PumpkinChili","AuGratinPotatoes","BruschettaChicken","PotatoSoup","HuliHuliChicken","Pancakes","AsianChickenThighs","ReesesPeanutButterCheesecake","SmotheredChickenBreasts","LemonBlueberryBread","VegetarianLinguine","PorkChopsAndScallopedPotatoes","ChickenAndDumplings","GingerCookies","ChickenWildRiceSoup","ClamChowder","PineapplePuddingCake","BakedTilapia","CherryPieBars","CreamyChickenNoodleSoup","ChickenPastaCasserole","FirstPlaceCoconutMacaroons","PorcupineMeatballs","HamAndCheeseSliders","TeriyakiChickenThighs","BaconMacaroniSalad"]
ingredients = ["ChickenBreasts,Onion,GarlicPowder,CanolaOil,GreatNorthernBeans,ChickenBroth,CannedGreenChiles,Seasoning,SourCream,HeavyWhippingCream","AllPurposeFlour,Eggs,Bananas,CanolaOil,Buttermilk,Walnuts","GroundBeef,Flour,Butter,Vegetables,Potatoes,ChickenBroth,ChickenMilk,Velveeta,SourCream","Bacon,Onion,Eggs,HashBrownPotatoes,Cheeses","Butter,Sugar,Eggs,CannedPumpkin,AllPurposeFlour,Spieces,BakingPower,BakingSoda,Buttermilk,CreamCheese,Butter,VanillaExtract","PieCrust,Chicken,Vegetables,CreamSauce","Chicken,Peppers,Onions,Spieces,FlourTortillas","PieDough,Apples,BrownSugar,GranulatedSugar,Spices,LemonJuice","LeanGroundBeef,Onion,Salsa,BlackBeans,SaladDressing,Seasoning,GroundCumin,FlourTortillas,SourCream,Lettuce,Tomato,Cilantro,ShreddedCheese","Zucchini,Salt,Eggs,Cheese,GroundBeef,Onion,Tomato,BellPepper","LasagnaNoodles,SausageBeef,GroundBeef,Tomatoes,Sugar,Cheese,Egg","Cauliflower,ChickenBouillon,VegetableBouillon,Butter,Flour,Milk,CheddarCheese,HotSauce","DryYeast,Water,Sugar,Salt,CanolaOil,BreadFlour","Eggs,Sugar,CanolaOil,OrangeJuice,AlmondExtract,AllPurposeFlour,GroundCinnamon,BakingPowder,BakingSoda,Salt,GroundCloves,Zucchini,BrownSugar,Butter,Milk,VanillaExtract","GroundBeef,Milk,Eggs,Oats,Cheese,Onion,Ketchup","Tortellini,Sausage,ChickenBroth,Tomatoes,Spinach,Basil","Water,LimeGelatin,KeyLimeYogurt,WhippedCream,GrahamCrackerCrust","GroundBeef,ChoppedGreenPeppers,Tomatoes,BrownSugar,BeefBouillonGranules,Rice","AllPurposeFlour,Sugar,BakingSoda,BakingCocoa,Salt,BakingPowder,CanolaOil,BrewedCoffee,Milk,Eggs,VanillaExtract","GroundBeef,Milk,Eggs,Saltines,Onion,Ketchup","CakeMix,Eggs,Oranges,VegetableOil,WhippedCream,Pineapple,VanillaPudding","Onion,GreenPepper,DicedTomatoes,Mushroom,Olives,GroundBeef,Cheese,MushroomSoup","Butter,Eggs,Milk,AllPurposeFlour,Cornmeal","ChickenBreasts,AllPurposeFlour,Butter,Mushrooms,ChickenBroth,Salt,Pepper,Cheese,Onions","Eggs,Sugar,Vanilla,AllPurposeFlour,BakingPowder,Milk,Butter","Macaroni,ColeslawMix,Onions,CeleryRibs,Cucumber,Pepper,Chestnuts","Ham,Bacon,Roux,Veggies,Cheese","CinnamonStreusel,Apples,VanillaSyrup,VanillaIceCream","Tomatoes,Aromatics,Broth,Herbs,Spices,Chicken,AndouilleSausage,Shrimp,Rice","AllPurposeFlour,Bananas,Eggs,VegetableOil,VanillaExtract","Shrimp,Scallops,Crabmeat,ChickenBroth,ClamJuice,Dairy,Cheese","Grapes,CreamCheese,SourCream,Pecans,Sugar","SandwichCookies,Butter,CreamCheese,PeanutButter,Sugar,PeanutButterCups,Milk,Fudge","BeefChuckRoasts,Ranch,ItalianSalad,GravyMix,Water,Parsley","Flour,BakingPowder,BakingSoda,Oil,Pumpkin,Spices","FlourTortillas,Meat,Beans,MexicanCheeseBlend","Butter,Sugar,Eggs,RipedBananas,VanillaExtract,AllPurposeFlour,BakingSoda,CreamCheese,Sugar","Linguine,Spices,Butter,OliveOil,Shrimp,WhiteWine,Lemon,Parmesan,Parsley","Flour,Sugar,Butter,Cream,Eggs,Rhubarb,CreamCheese,VanillaExtract","PieDough,CreamCheese,Sugar,Eggs,VanillaExtract,Pecans,CaramelSauce","GroundBeef,EnchiladaSauce,FlourTortillas,Cheese,Tomatoes,Cilantro,Pepper,Onion,Avacado","Butter,Sugar,VanillaExtract,Eggs,AllPurposeFlour,GroundCinnamon,Nutmeg,Salt,BakingSoda,Apples","Butter,Sugar,Eggs,SourCream,CornbreadMix,Milk,CornKernels","Onions,Pepper,Garlic,BlackBeans,Pumpkin,Tomatoes,ChickenBroth,Turkey,Seasoning","Potatoes,Flour,Butter,Cheese,Milk,Onion","AllPurposeFlour,Eggs,ChickenBreasts,Cheese,BreadCrumbs,Butter,Tomatoes,FreshBasil,OliveOil,Garlic,Salt,Pepper","Bacon,Potatoes,Aromatics,Herbs,Spices,ChickenBroth,Flour,Milk,Velveeta,GreenOnions","ChickenThighs,HuliHuliSauce","AllPurposeFlour,BakingPowder,Milk,Butter","ChickenThighs,SoySauce,BrownSugar,OrangeJuice,ChineseFiveSpicePowder,WhiteVinegar,Cornstarch","GrahamCrackerCrumbs,Sugar,Oreo,Butter,PeanutButter,CreamCheese,SourCream,VanillaExtract,Eggs,HotFudge,PeanutButterCups","ChickenBreasts,Salt,Seasoning,CanolaOil,Bacon,Onion,BrownSugar,Cheese","Butter,Sugar,LemonJuice,Eggs,Flour,Milk,Blueberries,Nuts","Linguine,Butter,OliveOil,Zucchini,Mushrooms,Tomato,GreenOnions,GarlicClove,Salt,Pepper,Cheese,Basil","PorkRibChops,Potatoes,Onion,Oli,ChickenBroth,Butter,Flour,Seasonings","CeleryRibs,Carrots,ChickenBroth,ChickenBreasts,Seasoning,Pepper,Milk,BakingMix","Sugar,Molasses,AllPurposeFlour,Ginger,Spieces","ChickenBroth,Mushrooms,WildRice,Aromatics,Herbs,MushroomSoupCream,Chicken","ChoppedClams,Bacon,Onion,Celery,Garlic,Potatoes,ClamJuice,HalfAndHalf","YellowCakeMix,VanillaPuddingMix,Cheese,Pineapple,WhippedTopping,Walnuts,Cherries","TilapiaFillets,Butter,LemonJuice,Capers,Seasoning","Eggs,AlmondExtract,AllPurposeFlour,CherryPieFilling","ChickenBouillon,EggNoodles,ChickenCream,Chicken,SourCream,Parsley","PennePasta,ChickenThighs,Vegetables,Seasoning,TomatoSauce,Cheese","Coconut,Sugar,AllPurposeFlour,Salt,Eggs,VanillaExtract","GroundBeef,LongGrainRice,Water,Onion,TomatoSauce","HawaiianSweetRolls,Ham,SwishCheese,Butter,HorseradishSauce,ChoppedOnion","ChickenThighs,Sugar,SoySauce,CiderVinegar,Garlic,GroundGinger,Pepper,Cornstarch","ElbowMacaroni,Tomato,Ribs,Onions,Mayonnaise,Vinegar,Salt,Pepper,BaconStrips"]
cooking_time = [40,75,55,50,45,75,30,80,55,60,110,30,50,40,40,40,20,60,40,75,40,60,40,40,50,25,60,80,290,30,70,20,20,430,80,45,35,20,75,50,70,60,65,260,110,40,30,30,15,65,75,30,75,30,115,30,30,60,55,40,20,55,25,80,30,80,55,255,20]

# This creates a dictionary for the user to add new recipes; output stores the new recipe in recipes_list, ingredients, and cooking_time, respectively
def add_recipe(recipes_list_add,ingredients_add,cooking_time_add):
    recipes_list.append(recipes_list_add)
    ingredients.append(ingredients_add)
    cooking_time.append(cooking_time_add)
    print("Recipe " + str(recipes_list_add) + " successfully added!")

# This allows the user to search a recipe up by name; output is the recipe, its ingredients, and its cooking time
def search_recipe_by_name(recipe):
    if recipe in recipes_list:
        recipeIndex = recipes_list.index(recipe)
        timeIndex = cooking_time[recipeIndex]
        ingredientsIndex = ingredients[recipeIndex]
        print(recipe)
        print("Ingredients: " + str(ingredientsIndex))
        print("Cooking Time (in minutes): " + str(timeIndex))
    else:
        print("Sorry, I'm unable to find the recipe you're looking for, but feel free to add your own!")

# This allows the user to search a recipe up based on the ingredient(s) they have available; output is the recipes that the user can make with the ingredients they input
def search_recipe_by_ingredient(ingredient):
    filtered_recipes = []
    for i in range(0,len(ingredients)):
        for ingredients_available in ingredient:
            if ingredients_available in ingredients[i]:
                if recipes_list[i] not in filtered_recipes:
                    filtered_recipes.append(recipes_list[i])
                    print("You can make: " + recipes_list[i])
                else:
                    print("Sorry, I'm unable to find any recipes with those ingredients, but feel free to add your own!")

# This allows the user to input how much cooking time they have available; output is a list of recipes they can make within that time frame
def search_recipe_by_time(time):
    filtered_recipes = []
    for i in range(0,len(cooking_time)):
        if cooking_time[i] == time:
            filtered_recipes.append(recipes_list[i])
    print("Here are some recipes you can make in " + str(time) + " minutes: ")
    print(filtered_recipes)

# This is the main menu
def main():
    while True:
        print("Welcome to Recipe Organizer!\n1. Display all recipes\n2. Search recipe by name\n3. Search recipe by ingredients\n4. Search recipe by cooking time\n5. Add a new recipe\n6. Exit")
        choice = input("Choose an option 1-6: ")
        if choice == "1":
            print(recipes_list)
        elif choice == "2":
            recipe = input("What is the name of the recipe you are looking for? Please type in uppercase for every new word and with no spaces. For example: BananaBread.")
            search_recipe_by_name(recipe)
        elif choice == "3":
            ingredient = input("Enter the ingredients you have available (use a comma to separate). Please type in uppercase for every new word and with no spaces. For example: VanillaExtract,BakingPowder.").split(",")
            search_recipe_by_ingredient(ingredient)
        elif choice == "4":
            time = int(input("Enter available cooking time (in minutes): "))
            search_recipe_by_time(time)
        elif choice == "5":
            recipes_list_add = input("Enter the recipe name: ")
            ingredients_add = input("Enter the ingredients (use a comma to separate): ").split(",")
            cooking_time_add = int(input("Enter the cooking time (in minutes): "))
            add_recipe(recipes_list_add,ingredients_add,cooking_time_add)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

#main()
main()


