from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": [
            {
                "image": "deps/images/goods/battlefield.jpg",
                "name": "Battlefield 2042",
                "description": "Battlefield, Action, Adventure, Co-op, First Person",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/darksouls.jpg",
                "name": "Dark Souls 3",
                "description": "Game for No-Lifes, Very Hard Game, Action",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/creedvalhala.jpg",
                "name": "Assassin's Creed Valhalla",
                "description": "Assasin's Creed, Plot Heavy Game, Action",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/fc24.jpg",
                "name": "EA SPORTS FC 24 Ultimate Edition",
                "description": "EA, EA SPORTS FC, EA Sports, EA app, PC Games",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/gothamknights.jpg",
                "name": "Gotham Knights",
                "description": "Action, Adventure, Multiplayer, RPG",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/gta5.jpg",
                "name": "Grand Theft Auto V",
                "description": "Grand Theft Auto, Silly Game, Action, Adventure",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/payday.jpg",
                "name": "Payday 2",
                "description": "Action, Co-op, First Person, Multiplayer, RPG",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/hogwarts.jpg",
                "name": "Hogwarts Legacy",
                "description": "Action, Adventure, RPG, Single Player",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/injustice.jpg",
                "name": "Injustice 2 Legendary Edition",
                "description": "Action, Fighting, Multiplayer, Single Player",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/madden24.jpg",
                "name": "Madden NFL 24",
                "description": "EA, EA Sports, EA app, Co-op, Local Co-op",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/monsterhunter.jpg",
                "name": "Monster Hunter",
                "description": "PC Games, Steam Games, Action, Multiplayer",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/mortalcombat.jpg",
                "name": "Mortal Kombat 11",
                "description": "Mortal Kombat, Action, Fighting, Multiplayer",
                "price": 25.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")