from django.shortcuts import render

recipes = [
    {
        "id": 1,
        "nazwa": "Spaghetti Carbonara",
        "opis": "Włoski klasyk z boczkiem i parmezanem.",
        "skladniki": ["spaghetti", "jajka", "boczek", "parmezan", "sól", "pieprz"],
        "instrukcja": "Ugotuj makaron, podsmaż boczek, wymieszaj z jajkami i serem.",
        "obraz": "carbonara.jpg"
    },
    {
        "id": 2,
        "nazwa": "Zupa Dyniowa",
        "opis": "Kremowa i rozgrzewająca zupa na jesień.",
        "skladniki": ["dynia", "cebula", "czosnek", "bulion", "śmietana"],
        "instrukcja": "Podsmaż składniki, gotuj z bulionem, zblenduj i dodaj śmietanę.",
        "obraz": "zupa_dyniowa.jpg"
    },
    {
        "id": 3,
        "nazwa": "Kurczak Curry",
        "opis": "Aromatyczny kurczak w sosie curry.",
        "skladniki": ["kurczak", "cebula", "czosnek", "przyprawa curry", "mleko kokosowe"],
        "instrukcja": "Podsmaż składniki, dodaj przyprawy i mleko kokosowe, gotuj do miękkości.",
        "obraz": "kurczak_curry.jpg"
    },
    {
        "id": 4,
        "nazwa": "Naleśniki z serem",
        "opis": "Klasyczne naleśniki z nadzieniem twarogowym.",
        "skladniki": ["jajka", "mleko", "mąka", "twaróg", "cukier wanilinowy"],
        "instrukcja": "Zrób ciasto, usmaż naleśniki, nadziej twarogiem.",
        "obraz": "nalesniki.jpg"
    },
    {
        "id": 5,
        "nazwa": "Sałatka Cezar",
        "opis": "Lekka sałatka z kurczakiem i sosem czosnkowym.",
        "skladniki": ["sałata rzymska", "kurczak", "grzanki", "parmezan", "sos cezar"],
        "instrukcja": "Ułóż składniki na talerzu i polej sosem.",
        "obraz": "cezar.jpg"
    },
    {
        "id": 6,
        "nazwa": "Placki ziemniaczane",
        "opis": "Chrupiące placki z tartych ziemniaków.",
        "skladniki": ["ziemniaki", "cebula", "jajko", "mąka", "sól", "pieprz"],
        "instrukcja": "Zetrzyj składniki, wymieszaj, usmaż na złoto.",
        "obraz": "placki.jpg"
    },
    {
        "id": 7,
        "nazwa": "Lasagne",
        "opis": "Włoska zapiekanka z mięsem i beszamelem.",
        "skladniki": ["płaty lasagne", "mięso mielone", "sos pomidorowy", "beszamel", "ser"],
        "instrukcja": "Układaj warstwami i zapiekaj 40 minut.",
        "obraz": "lasagne.jpg"
    },
    {
        "id": 8,
        "nazwa": "Risotto z grzybami",
        "opis": "Kremowy ryż z grzybami i parmezanem.",
        "skladniki": ["ryż arborio", "grzyby", "bulion", "cebula", "parmezan"],
        "instrukcja": "Podsmaż, podlewaj bulionem, gotuj i mieszaj.",
        "obraz": "risotto.jpg"
    },
    {
        "id": 9,
        "nazwa": "Omlet z warzywami",
        "opis": "Szybki i zdrowy omlet na śniadanie.",
        "skladniki": ["jajka", "papryka", "cebula", "szpinak", "ser"],
        "instrukcja": "Roztrzep jajka, dodaj warzywa, usmaż.",
        "obraz": "omlet.jpg"
    },
    {
        "id": 10,
        "nazwa": "Szarlotka",
        "opis": "Tradycyjne ciasto z jabłkami i cynamonem.",
        "skladniki": ["jabłka", "mąka", "masło", "cukier", "cynamon"],
        "instrukcja": "Zrób kruche ciasto, dodaj jabłka, zapiecz.",
        "obraz": "szarlotka.jpg"
    },
]

# Create your views here.


def starting_page(request):
    return render(request, 'recipes/index.html')


def recipes_list_page(request):
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes
    })


def recipe_details_page(request, recipe_id):
    recipe_details = next(
        (recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    return render(request, 'recipes/recipe_details.html', {
        'recipe_details': recipe_details
    })
