from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - Catalog",
        "goods": [
            {
                "image": "deps/img/goods/rimworld-anomaly-pc-mac-game-steam-cover.jpg",
                "name": "RimWorld - Anomaly",
                "description": "Darkness stirs on the rim. Survive flesh infestations, cultist attacks, shambling undead, blood rains, invisible hunters, and other sanity-shredding perils. Capture and study entities to harness the power of the void. Conduct psychic rituals and awaken an evil machine god.",
                "price": 21.89,
            },
            {
                "image": "deps/img/goods/balatro-pc-game-steam-cover.jpg",
                "name": "Balatro",
                "description": "Balatro is a poker-inspired roguelike deck builder all about creating powerful synergies and winning big.",
                "price": 9.99,
            },
            {
                "image": "deps/img/goods/assetto-corsa-competizione-the-nurburgring-24h-pack-pc-game-steam-cover.jpg",
                "name": "Assetto Corsa Competizione - The Nürburgring 24h Pack",
                "description": "The most anticipated moment for Assetto Corsa Competizione has finally come. Nürburgring 24 hours is in. Nordschleife is probably the most iconic circuit worldwide. Constantly attracting thousands of professional and weekend racers from across the globe, this is the place where driver aim to drive in their career. Surely being the most challenging road course to ever have existed, it consists of 25.3 km of tarmac with over 70 bends that challenge even the most experienced racers.",
                "price": 8.99,
            },
            {
                "image": "deps/img/goods/gigantic-rampage-edition-rampage-edition-pc-game-steam-cover.jpg",
                "name": "Gigantic: Rampage Edition",
                "description": "GO GIGANTIC! THE UNIQUE MOBA HERO SHOOTER RETURNS!  GIGANTIC: RAMPAGE EDITION is a premium and definitive release of the original 5v5 MOBA Hero Shooter, GIGANTIC, that provides a dynamic and exciting team-based multiplayer experience for fans of both genres.",
                "price": 12.40,
            },
            {
                "image": "deps/img/goods/dying-light-2-stay-human-reloaded-edition-reloaded-edition-pc-game-steam-cover.jpg",
                "name": "Dying Light 2 Stay Human Reloaded Edition",
                "description": "It’s been 20 years since the events of the original game. The virus won, and humanity is slowly dying. You play as Aiden Caldwell, a wandering Pilgrim who delivers goods, brings news, and connects the few remaining survivor settlements in barren lands devastated by the zombie virus. However, your true goal is to find your little sister Mia, who you left behind as a kid to escape Dr. Waltz's torturous experiments. Haunted by the past, you eventually make the decision to confront it when you learn that Mia may still be alive in Villedor — the last city standing on Earth.",
                "price": 19.99,
            },
            {
                "image": "deps/img/goods/buckshot-roulette-pc-game-steam-cover.jpg",
                "name": "Buckshot Roulette",
                "description": "12-Gauge Action Play Russian roulette with a 12-gauge. Cause shotguns just feel better. Literally Mindblowing Gameplay 15 to 20-minute intense playtime. Enter the arena, go three rounds against The Dealer, and walk away with the prize. Or don't. Immersive Atmosphere Welcome to the underground nightclub, where metal railings pulse to the beats of forgotten drum machines.",
                "price": 2.19,
            },
            {
                "image": "deps/img/goods/children-of-the-sun-pc-game-steam-cover.jpg",
                "name": "Children of the Sun",
                "description": "Burning with anger, THE GIRL wages a one-woman war against THE CULT, taking them down cultist by cultist, bullet by bullet, until she reaches her true target: THE LEADER. Along the way she will unravel the dark truth about this mysterious order and the atrocities committed by them in the name of their master.",
                "price": 10.99,
            },
            {
                "image": "deps/img/goods/the-outlast-trials-pc-game-steam-cover.jpg",
                "name": "The Outlast Trials",
                "description": "Red Barrels invites you to experience mind-numbing terror, this time with friends. Whether you go through the trials alone or in teams, if you survive long enough and complete the therapy, Murkoff will happily let you leave… but will you be the same?",
                "price": 24.53,
            },
            {
                "image": "deps/img/goods/assetto-corsa-competizione-gt2-pack-pc-game-steam-cover.jpg",
                "name": "Assetto Corsa Competizione GT2 Pack",
                "description": "Assetto Corsa Competizione GT2 Pack is finally bringing the higher power of GT2 vehicles to sim racers, together with the perfect playground of the Red Bull Ring Circuit. GT2 cars are a new grand tourer racing class maintained from SRO Motorsports Group, the class inserts between GT4 and GT3 in terms of on track performance. They are well known for their high power, which is extremely demanding and fun to control thanks to the less invasive aerodynamic package they come with, when compared to GT3.",
                "price": 11.90,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")