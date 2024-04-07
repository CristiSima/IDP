from documents import *

tier_prefix_dic = {
    2: "Novice",
    3: "Journeyman",
    4: "Adept",
}

def init_db():
    recipes = []
    items = []

    stations = [
        CraftingStation(name='Farm Field', use_tax=0),
        CraftingStation(name='Herbal Garden', use_tax=0),
        CraftingStation(name='Cook', use_tax=300),
        CraftingStation(name='Toolmaker', use_tax=100),
        CraftingStation(name='Warrior''s Forge', use_tax=1000),
        CraftingStation(name='Lumber Mill', use_tax=100),
        CraftingStation(name='Smelter', use_tax=100),
    ]
    farm_field, herbal_garden, cook, toolmaker, forge, lumber_mill, smelter = stations

    farm_items = [
        Item(name='Wheat Sheaft', tier=3, enchant=0, quality=0, average_price=300),
        Item(name='Wheat Seed', tier=3, enchant=0, quality=0, average_price=5000),
        Item(name='Bread', tier=3, enchant=0, quality=0, average_price=8000)
    ]
    items += farm_items

    recipes.append(Recipe(
        name="Grow Wheat",
        station=farm_field,
        result_sets=[
            ResultsSet(
                probability=0.5,
                items=[
                    ItemStack(item=farm_items[0], count=5),
                    ItemStack(item=farm_items[1], count=1)
                ]
            ),
            ResultsSet(
                probability=0.5,
                items=[ItemStack(item=farm_items[0], count=5)]
            )
        ],
        ingredients=[
            ItemStack(item=farm_items[1], count=1)
        ]
    ))

    logs = [
        Item(name='Birch Logs', tier=2, enchant=0, quality=0, average_price=80),
        Item(name='Chestnut Logs', tier=3, enchant=0, quality=0, average_price=300),
        Item(name='Pine Logs', tier=4, enchant=0, quality=0, average_price=700),
        Item(name='Pine Logs', tier=4, enchant=1, quality=0, average_price=1150),
        Item(name='Pine Logs', tier=4, enchant=2, quality=0, average_price=1800),
        Item(name='Pine Logs', tier=4, enchant=3, quality=0, average_price=3000),
    ]
    treehearth = Item(name='Treehearth', tier=1, enchant=0, quality=0, average_price=5000)
    items += logs
    items.append(treehearth)
    # + [treehearth, ]

    planks = [
        Item(name='Birch Planks', tier=2, enchant=0, quality=0, average_price=100),
        Item(name='Chestnut Planks', tier=3, enchant=0, quality=0, average_price=350),
        Item(name='Pine Planks', tier=4, enchant=0, quality=0, average_price=1000),
        Item(name='Pine Planks', tier=4, enchant=1, quality=0, average_price=2000),
        Item(name='Pine Planks', tier=4, enchant=2, quality=0, average_price=3000),
        Item(name='Pine Planks', tier=4, enchant=3, quality=0, average_price=10000),
    ]
    items += planks


    ores = [
        Item(name='Copper Ore', tier=2, enchant=0, quality=0, average_price=80),
        Item(name='Tin Ore', tier=3, enchant=0, quality=0, average_price=300),
        Item(name='Iron Ore', tier=4, enchant=0, quality=0, average_price=700),
        Item(name='Iron Ore', tier=4, enchant=1, quality=0, average_price=1150),
        Item(name='Iron Ore', tier=4, enchant=2, quality=0, average_price=1800),
        Item(name='Iron Ore', tier=4, enchant=3, quality=0, average_price=3000),
    ]
    mountainhearth = Item(name='Mountainhearth', tier=1, enchant=0, quality=0, average_price=5000)
    items += ores
    items.append(mountainhearth)

    bars = [
        Item(name='Copper Bar', tier=2, enchant=0, quality=0, average_price=100),
        Item(name='Bronze Bar', tier=3, enchant=0, quality=0, average_price=350),
        Item(name='Iron Bar', tier=4, enchant=0, quality=0, average_price=1000),
        Item(name='Iron Bar', tier=4, enchant=1, quality=0, average_price=2000),
        Item(name='Iron Bar', tier=4, enchant=2, quality=0, average_price=3000),
        Item(name='Iron Bar', tier=4, enchant=3, quality=0, average_price=10000),
    ]
    items += bars

    for recipe_name, station, raws, refineds in zip(
            ["Cut Planks", "Smelt Ore"],
            [lumber_mill, smelter],
            [logs, ores],
            [planks, bars]
            ):
        recipes.append(Recipe.single_result(
            name=recipe_name,
            station=station,
            results=[ ItemStack(
                item=refineds[0],
                count=1,
            )],
            ingredients=[ ItemStack(
                item=raws[0],
                count=1,
            )]
        ))

        recipes.append(Recipe.single_result(
            name=recipe_name,
            station=station,
            results=[ ItemStack(
                item=refineds[1],
                count=1,
            )],
            ingredients=[
                ItemStack(
                    item=raws[1],
                    count=1,
                ),
                ItemStack(
                    item=refineds[0],
                    count=1
                )
            ]
        ))

        for raw, refined in zip(raws[2:], refineds[2:]):
            recipes.append(Recipe.single_result(
                name=recipe_name,
                station=station,
                results=[ ItemStack(
                    item=refined,
                    count=1,
                )],
                ingredients=[
                    ItemStack(
                        item=raw,
                        count=1,
                    ),
                    ItemStack(
                        item=refineds[1],
                        count=1
                    )
                ]
            ))

    for plank, bar in zip(planks, bars):
        tier = plank.tier
        enchant = plank.enchant
        swords = [
            Item(name=tier_prefix_dic[tier]+' Broadsword', tier=tier, enchant=enchant, quality=0, average_price=100),
            Item(name=tier_prefix_dic[tier]+' Broadsword', tier=tier, enchant=enchant, quality=1, average_price=100),
            Item(name=tier_prefix_dic[tier]+' Broadsword', tier=tier, enchant=enchant, quality=2, average_price=100),
            Item(name=tier_prefix_dic[tier]+' Broadsword', tier=tier, enchant=enchant, quality=3, average_price=100),
            Item(name=tier_prefix_dic[tier]+' Broadsword', tier=tier, enchant=enchant, quality=4, average_price=100),
        ]
        items += swords
        recipes.append(Recipe(
            name="Smith Sword",
            station=forge,
            ingredients=[
                ItemStack(item=plank, count=21),
                ItemStack(item=bar, count=41)
            ],
            result_sets=[
                ResultsSet(probability=probability, items=[
                    ItemStack(item=sword, count=1)
                ]) for sword, probability in zip(swords, [0.5, .3, .1, .08, .02])
            ]
        ))

    # print(repr(recipes[1]))
    if __name__ == "__main__":
        for recipe in recipes:
            print(repr(recipe))
        exit()

    # print(items, flush=True)
    
    for item in items:
        item.save()
    for station in stations:
        station.save()
    for recipe in recipes:
        recipe.save()

if __name__ == "__main__":
    init_db()