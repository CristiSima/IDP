from mongoengine import Document, EmbeddedDocument, connect as _connect
from mongoengine.fields import StringField, IntField, ReferenceField, DecimalField, EmbeddedDocumentListField, ListField
from typing import List
from os import environ

__all__ = [
    "connect",
    "Item", "Recipe", "CraftingStation",
    "ItemStack", "ResultsSet",
]

def connect():
    _connect(
        "IDP",
        username=environ.get("MONGO_USER", None),
        password=environ.get("MONGO_PASSWORD", None),
        host=environ.get("MONGO_HOST"),
    )

class CraftingStation(Document):
    name = StringField(requiered = True)
    use_tax = IntField(0, requered = True)

    def __repr__(self):
        return f"CraftingStation<{self.name} @{self.use_tax}>"

class Item(Document):
    name = StringField(requiered = True)
    description = StringField()
    
    tier = IntField(requiered=True)
    enchant = IntField(requiered=True)
    quality = IntField(requiered=True)
    
    average_price = IntField(requiered=True)

    def recipes_using(self) -> List["Recipe"]:
        return Recipe.objects(ingredients__item=self.id)

    def recipes_for(self) -> List["Recipe"]:
        return Recipe.objects(result_sets__items__item=self.id)

    def __repr__(self):
        return f"Item<{self.name} T{self.tier}.{self.enchant} Q{self.quality} @{self.average_price}>"

class ItemStack(EmbeddedDocument):
    item = ReferenceField(Item, required=True)
    count = IntField(1, required=True)

    @property
    def name(self):
        return self.item.name
    @property
    def description(self):
        return self.item.description
    @property
    def tier(self):
        return self.item.tier
    @property
    def enchant(self):
        return self.item.enchant
    @property
    def quality(self):
        return self.item.quality
    @property
    def average_price(self):
        return self.item.average_price
    @property
    def stack_average_price(self):
        return self.item.average_price * self.count
    
    def __repr__(self):
        return f"{self.count}x {repr(self.item)}"

class ResultsSet(EmbeddedDocument):
    probability = DecimalField(0, 100, required=True)
    items = EmbeddedDocumentListField(ItemStack, required=True, default=list)

    def __repr__(self):
        return f"ResultsSet<{(self.probability*100)//1}% [{', '.join(map(repr, self.items))}]"

class Recipe(Document):
    name = StringField(requiered = True)
    description = StringField()
    station = ReferenceField(CraftingStation, requiered=True)
    result_sets = EmbeddedDocumentListField(ResultsSet, required=True, default=list)
    ingredients = EmbeddedDocumentListField(ItemStack, required=True, default=list)

    def single_result(*, name, station, results, ingredients) -> "Recipe":
        return Recipe(
            name=name,
            station=station,
            result_sets=[
                ResultsSet(
                    probability=1,
                    items=results
                )
            ],
            ingredients=ingredients,
        )

    def __repr__(self):
        result_text: str
        if len(self.result_sets) == 1:
            result_text = repr(self.result_sets[0])
        else:
            new_line="\n"
            indent="\t"
            result_text = f"{{\n{new_line.join(map(lambda x:indent+repr(x), self.result_sets))}\n}}"

        # ingredients_text: str
        # if len(self.ingredients) == 1:
        #     ingredients_text = repr(ingredients.result_sets[0])
        # else:
        #     new_line="\n"
        #     indent="\t"
        #     ingredients_text = f"{{\n{new_line.join(map(lambda x:indent+repr(x), self.ingredients))}\n}}"

        return f"Recipe<\"{self.name}\" @{repr(self.station)} "\
                f"[{', '.join(map(repr, self.ingredients))}] => {result_text}"
            # f"[{', '.join(map(repr, self.ingredients))}] => [{', '.join(list(map(repr, self.result_sets)))}]"