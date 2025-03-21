from core.split import split_in_two, split_in_three


class BrawlersConstants:
    alternative_brawlers = {
        "Dyna": "Dynamike",
        "Mike": "Dynamike",
        "8Bit": "8-Bit",
        "Primo": "El Primo",
        "Barely": "Barley",
        "Daryl": "Darryl",
        "Daryll": "Darryl",
        "Mrp": "Mr P",
        "Mr. P": "Mr P",
        "Colete": "Colette",
        "Collete": "Colette",
        "Collette": "Colette",
        "Colonel": "Colonel Ruffs",
        "Ruffs": "Colonel Ruffs",
        "Col": "Colonel Ruffs",
        "Col Ruffs": "Colonel Ruffs",
        "Squaek": "Squeak",
    }

    brawlers = {
        # Starting Brawler
        "Shelly": {
            "rarity": "Starting Brawler",
            "emoji": "<:S:776007475156484146>",
            "gadgets": ["Fast Forward", "Clay Pigeons"],
            "starpowers": ["Shell Shock", "Band-Aid"],
        },
        # Rare
        "Nita": {
            "rarity": "Rare",
            "emoji": "<:N:776007475156746261>",
            "gadgets": ["Bear Paws", "Faux Fur"],
            "starpowers": ["Bear With Me", "Hyper Bear"],
        },
        "Colt": {
            "rarity": "Rare",
            "emoji": "<:C:776006754051162113>",
            "gadgets": ["Speedloader", "Silver Bullet"],
            "starpowers": ["Slick Boots", "Magnum Special"],
        },
        "Bull": {
            "rarity": "Rare",
            "emoji": "<:B:776006754265333780>",
            "gadgets": ["T-Bone Injector", "Stomper"],
            "starpowers": ["Berserker", "Tough Guy"],
        },
        "Brock": {
            "rarity": "Rare",
            "emoji": "<:B:776006754433105931>",
            "gadgets": ["Rocket Laces", "Rocket Fuel"],
            "starpowers": ["Incendiary", "Rocket No. Four"],
        },
        "El Primo": {
            "rarity": "Rare",
            "emoji": "<:E:776006754139111434>",
            "gadgets": ["Suplex Supplement", "Asteroid Belt"],
            "starpowers": ["El Fuego", "Meteor Rush"],
        },
        "Barley": {
            "rarity": "Rare",
            "emoji": "<:B:776006754488025118>",
            "gadgets": ["Sticky Syrup Mixer", "Herbal Tonic"],
            "starpowers": ["Medical Use", "Extra Noxious"],
        },
        "Poco": {
            "rarity": "Rare",
            "emoji": "<:P:776007474792235038>",
            "gadgets": ["Tuning Fork", "Protective Tunes"],
            "starpowers": ["Da Capo!", "Screeching Solo"],
        },
        "Rosa": {
            "rarity": "Rare",
            "emoji": "<:R:776007475052150805>",
            "gadgets": ["Grow Light", "Unfriendly Bushes"],
            "starpowers": ["Plant Life", "Thorny Gloves"],
        },
        # Super Rare
        "Jessie": {
            "rarity": "Super Rare",
            "emoji": "<:J:776006754034122763>",
            "gadgets": ["Spark Plug", "Recoil Spring"],
            "starpowers": ["Energize", "Shocky"],
        },
        "Dynamike": {
            "rarity": "Super Rare",
            "emoji": "<:D:776006754495627314>",
            "gadgets": ["Fidget Spinner", "Satchel Charge"],
            "starpowers": ["Dyna-Jump", "Demolition"],
        },
        "Tick": {
            "rarity": "Super Rare",
            "emoji": "<:T:776007475433963521>",
            "gadgets": ["Backup Mine", "Last Hurrah"],
            "starpowers": ["Well Oiled", "Automa-Tick Reload"],
        },
        "8-Bit": {
            "rarity": "Super Rare",
            "emoji": "<:8:776006752885145610>",
            "gadgets": ["Cheat Cartridge", "Extra Credits"],
            "starpowers": ["Boosted Booster", "Extra Life"],
        },
        "Rico": {
            "rarity": "Super Rare",
            "emoji": "<:R:776007475072860180>",
            "gadgets": ["Multiball Launcher", "Bouncy Castle"],
            "starpowers": ["Super Bouncy", "Robo Retreat"],
        },
        "Darryl": {
            "rarity": "Super Rare",
            "emoji": "<:D:776006754114732052>",
            "gadgets": ["Recoiling Rotator", "Tar Barrel"],
            "starpowers": ["Steel Hoops", "Rolling Reload"],
        },
        "Penny": {
            "rarity": "Super Rare",
            "emoji": "<:P:994235836004569088>",
            "gadgets": ["Pocket Detonator", "Captain's Compass"],
            "starpowers": ["Last Blast", "Balls of Fire"],
        },
        "Carl": {
            "rarity": "Super Rare",
            "emoji": "<:C:776006754428256267>",
            "gadgets": ["Heat Ejector", "Flying Hook"],
            "starpowers": ["Power Throw", "Protective Pirouette"],
        },
        "Jacky": {
            "rarity": "Super Rare",
            "emoji": "<:J:776007474867339296>",
            "gadgets": ["Pneumatic Booster", "Rebuild"],
            "starpowers": ["Counter Crush", "Hardy Hard Hat"],
        },
        "Gus": {
            "rarity": "Super Rare",
            "emoji": "<:G:1023246681975832667>",
            "gadgets": ["Kooky Popper", "Soul Switcher"],
            "starpowers": ["Health Bonanza", "Spirit Animal"],
        },
        # Epic
        "Bo": {
            "rarity": "Epic",
            "emoji": "<:B:776006754488156220>",
            "gadgets": ["Super Totem", "Tripwire"],
            "starpowers": ["Circling Eagle", "Snare a Bear"],
        },
        "Emz": {
            "rarity": "Epic",
            "emoji": "<:E:776006754479374367>",
            "gadgets": ["Friendzoner", "Acid Spray"],
            "starpowers": ["Bad Karma", "Hype"],
        },
        "Stu": {
            "rarity": "Epic",
            "emoji": "<:S:821042120222572625>",
            "gadgets": ["Speed Zone", "Breakthrough"],
            "starpowers": ["Zero Drag", "Gaso-Heal"],
        },
        "Piper": {
            "rarity": "Epic",
            "emoji": "<:P:776007475102220329>",
            "gadgets": ["Auto Aimer", "Homemade Recipe"],
            "starpowers": ["Ambush", "Snappy Sniping"],
        },
        "Pam": {
            "rarity": "Epic",
            "emoji": "<:P:776007475329499147>",
            "gadgets": ["Pulse Modulator", "Scrapsucker"],
            "starpowers": ["Mama's Hug", "Mama's Squeeze"],
        },
        "Frank": {
            "rarity": "Epic",
            "emoji": "<:F:776006753753628682>",
            "gadgets": ["Active Noise Cancelling", "Irresistible Attraction"],
            "starpowers": ["Power Grab", "Sponge"],
        },
        "Bibi": {
            "rarity": "Epic",
            "emoji": "<:B:776006754139504691>",
            "gadgets": ["Vitamin Booster", "Extra Sticky"],
            "starpowers": ["Home Run", "Batting Stance"],
        },
        "Bea": {
            "rarity": "Epic",
            "emoji": "<:B:776006754571649024>",
            "gadgets": ["Honey Molasses", "Rattled Hive"],
            "starpowers": ["Insta Beeload", "Honey Coat"],
        },
        "Nani": {
            "rarity": "Epic",
            "emoji": "<:N:776007475006275605>",
            "gadgets": ["Warp Blast", "Return To Sender"],
            "starpowers": ["Autofocus", "Tempered Steel"],
        },
        "Edgar": {
            "rarity": "Epic",
            "emoji": "<:E:788333161725034516>",
            "gadgets": ["Let's Fly", "Hardcore"],
            "starpowers": ["Hard Landing", "Fisticuffs"],
        },
        "Griff": {
            "rarity": "Epic",
            "emoji": "<:G:854635938582626314>",
            "gadgets": ["Piggy Bank", "Coin Shower"],
            "starpowers": ["Keep The Change", "Business Resilience"],
        },
        "Grom": {
            "rarity": "Epic",
            "emoji": "<:G:923487323847540736>",
            "gadgets": ["Watchtower", "Radio Check"],
            "starpowers": ["Foot Patrol", "X-Factor"],
        },
        "Bonnie": {
            "rarity": "Epic",
            "emoji": "<:B:983273470278373417>",
            "gadgets": ["Sugar Rush", "Crash Test"],
            "starpowers": ["Black Powder", "Wisdom Tooth"],
        },
        "Gale": {
            "rarity": "Epic",
            "emoji": "<:G:776006754646884352>",
            "gadgets": ["Spring Ejector", "Twister"],
            "starpowers": ["Blustery Blow", "Freezing Snow"],
        },
        "Colette": {
            "rarity": "Epic",
            "emoji": "<:C:776006754663399489>",
            "gadgets": ["Na-ah!", "Gotcha!"],
            "starpowers": ["Push It", "Mass Tax"],
        },
        "Belle": {
            "rarity": "Epic",
            "emoji": "<:B:830402914941927425>",
            "gadgets": ["Nest Egg", "Reverse Polarity"],
            "starpowers": ["Positive Feedback", "Grounded"],
        },
        "Ash": {
            "rarity": "Epic",
            "emoji": "<:A:881457139837710357>",
            "gadgets": ["Chill Pill", "Rotten Banana"],
            "starpowers": ["First Bash", "Mad As Heck"],
        },
        "Lola": {
            "rarity": "Epic",
            "emoji": "<:L:902944553575804971>",
            "gadgets": ["Freeze Frame", "Stunt Double"],
            "starpowers": ["Improvise", "Sealed With A Kiss"],
        },
        "Sam": {
            "rarity": "Epic",
            "emoji": "<:S:1016081621117575190>",
            "gadgets": ["Magnetic Field", "Pulse Repellent"],
            "starpowers": ["Hearty Recovery", "Remote Recharge"],
        },
        "Mandy": {
            "rarity": "Epic",
            "emoji": "<:M:1059551287080914985>",
            "gadgets": ["Caramelize", "Cookie Crumbs"],
            "starpowers": ["In My Sights", "Hard Candy"],
        },
        "Maisie": {
            "rarity": "Epic",
            "emoji": "<:M:1108815643345690744>",
            "gadgets": ["Disengage!", "Finish Them!"],
            "starpowers": ["Pinpoint Precision", "Tremors"],
        },
        "Hank": {
            "rarity": "Epic",
            "emoji": "<:H:1108819447675883650>",
            "gadgets": ["Water Balloons", "Barricade"],
            "starpowers": ["It's Gonna Blow", "Take Cover!"],
        },
        "Pearl": {
            "rarity": "Epic",
            "emoji": "<:P:1201538436104990803>",
            "gadgets": ["Overcooked", "Made With Love"],
            "starpowers": ["Heat Retention", "Heat Shield"],
        },
        "Larry & Lawrie": {
            "rarity": "Epic",
            "emoji": "<:L:1201538438395068446>",
            "gadgets": ["Order: Swap", "Order: Fall Back"],
            "starpowers": ["Protocol: Protect", "Protocol: Assist"],
        },
        "Angelo": {
            "rarity": "Epic",
            "emoji": "<:A:1215744344863281152>",
            "gadgets": ["Stinging Flight", "Master Fletcher"],
            "starpowers": ["Empower", "Flow"],
        },
        "Berry": {
            "rarity": "Epic",
            "emoji": "<:B:1262408060069085257>",
            "gadgets": ["Friendship Is Great", "Healthy Additives"],
            "starpowers": ["Floor Is Fine", "Making A Mess"],
        },
        "Shade": {
            "rarity": "Epic",
            "emoji": "<:S:1320843531434332210>",
            "gadgets": ["Longarms", "Jump Scare"],
            "starpowers": ["Spooky Speedster", "Hardened Hoodie"],
        },
        "Meeple": {
            "rarity": "Epic",
            "emoji": "<:M:1352278664208846868>",
            "gadgets": ["Mansions of Meeple", "Ragequit"],
            "starpowers": ["Do Not Pass Go", "Rule Bending"],
        },
        # Mythic
        "Mortis": {
            "rarity": "Mythic",
            "emoji": "<:M:776006754424979456>",
            "gadgets": ["Combo Spinner", "Survival Shovel"],
            "starpowers": ["Creepy Harvest", "Coiled Snake"],
        },
        "Tara": {
            "rarity": "Mythic",
            "emoji": "<:T:776007475328581642>",
            "gadgets": ["Psychic Enhancer", "Support From Beyond"],
            "starpowers": ["Black Portal", "Healing Shade"],
        },
        "Gene": {
            "rarity": "Mythic",
            "emoji": "<:G:776006754810068992>",
            "gadgets": ["Lamp Blowout", "Vengeful Spirits"],
            "starpowers": ["Magic Puffs", "Spirit Slap"],
        },
        "Max": {
            "rarity": "Mythic",
            "emoji": "<:M:776007475228704788>",
            "gadgets": ["Phase Shifter", "Sneaky Sneakers"],
            "starpowers": ["Super Charged", "Run n' Gun"],
        },
        "Mr P": {
            "rarity": "Mythic",
            "emoji": "<:M:776007475257278504>",
            "gadgets": ["Service Bell", "Porter Reinforcements"],
            "starpowers": ["Handle With Care", "Tin Can"],
        },
        "Sprout": {
            "rarity": "Mythic",
            "emoji": "<:S:776007475068796928>",
            "gadgets": ["Garden Mulcher", "Transplant"],
            "starpowers": ["Overgrowth", "Photosynthesis"],
        },
        "Byron": {
            "rarity": "Mythic",
            "emoji": "<:B:788333161791750144>",
            "gadgets": ["Shot In The Arm", "Booster Shots"],
            "starpowers": ["Malaise", "Injection"],
        },
        "Squeak": {
            "rarity": "Mythic",
            "emoji": "<:S:830402901696446464>",
            "gadgets": ["Windup", "Residue"],
            "starpowers": ["Chain Reaction", "Super Sticky"],
        },
        "Lou": {
            "rarity": "Mythic",
            "emoji": "<:L:776353795030122507>",
            "gadgets": ["Ice Block", "Cryo Syrup"],
            "starpowers": ["Supercool", "Hypothermia"],
        },
        "Colonel Ruffs": {
            "rarity": "Mythic",
            "emoji": "<:C:804311859090948096>",
            "gadgets": ["Take Cover", "Air Support"],
            "starpowers": ["Air Superiority", "Field Promotion"],
        },
        "Buzz": {
            "rarity": "Mythic",
            "emoji": "<:B:854635938360721408>",
            "gadgets": ["Reserve Buoy", "X-Ray-Shades"],
            "starpowers": ["Tougher Torpedo", "Eyes Sharp"],
        },
        "Fang": {
            "rarity": "Mythic",
            "emoji": "<:F:923487339597148160>",
            "gadgets": ["Corn-Fu", "Roundhouse Kick"],
            "starpowers": ["Fresh Kicks", "Divine Soles"],
        },
        "Eve": {
            "rarity": "Mythic",
            "emoji": "<:E:950762267522269224>",
            "gadgets": ["Gotta Go!", "Motherly Love"],
            "starpowers": ["Unnatural Order", "Happy Surprise"],
        },
        "Janet": {
            "rarity": "Mythic",
            "emoji": "<:J:970789140922769438>",
            "gadgets": ["Drop The Bass", "Backstage Pass"],
            "starpowers": ["Stage View", "Vocal Warm Up"],
        },
        "Otis": {
            "rarity": "Mythic",
            "emoji": "<:O:992111448274763778>",
            "gadgets": ["Dormant Star", "Phat Splatter"],
            "starpowers": ["Stencil Glue", "Ink Refills"],
        },
        "Buster": {
            "rarity": "Mythic",
            "emoji": "<:B:1039257726250930256>",
            "gadgets": ["Utility Belt", "Slo-Mo Replay"],
            "starpowers": ["Blockbuster", "Kevlar Vest"],
        },
        "Gray": {
            "rarity": "Mythic",
            "emoji": "<:G:1059551285294141511>",
            "gadgets": ["Walking Cane", "Grand Piano"],
            "starpowers": ["Fake Injury", "New Perspective"],
        },
        "R-T": {
            "rarity": "Mythic",
            "emoji": "<:R:1081866518725406782>",
            "gadgets": ["In Line", "Hacks!"],
            "starpowers": ["Quick Maths", "Recording"],
        },
        "Willow": {
            "rarity": "Mythic",
            "emoji": "<:W:1081866517471305728>",
            "gadgets": ["Spellbound", "Dive"],
            "starpowers": ["Love Is Blind", "Obsession"],
        },
        "Doug": {
            "rarity": "Mythic",
            "emoji": "<:D:1125365773729271829>",
            "gadgets": ["Double Sausage", "Extra Mustard"],
            "starpowers": ["Fast Food", "Self Service"],
        },
        "Chuck": {
            "rarity": "Mythic",
            "emoji": "<:C:1171178357627568168>",
            "gadgets": ["Rerouting", "Ghost Train"],
            "starpowers": ["Pit Stop", "Tickets Please!"],
        },
        "Charlie": {
            "rarity": "Mythic",
            "emoji": "<:C:1171178359523389511>",
            "gadgets": ["Spiders", "Personal Space"],
            "starpowers": ["Digestive", "Slimy"],
        },
        "Mico": {
            "rarity": "Mythic",
            "emoji": "<:M:1201538443780567170>",
            "gadgets": ["Clipping Scream", "Presto"],
            "starpowers": ["Monkey Business", "Record Smash"],
        },
        "Melodie": {
            "rarity": "Mythic",
            "emoji": "<:M:1254748190008414349>",
            "gadgets": ["Perfect Pitch", "Interlude"],
            "starpowers": ["Fast Beats", "Extended Mix"],
        },
        "Lily": {
            "rarity": "Mythic",
            "emoji": "<:L:1254748188775026708>",
            "gadgets": ["Vanish", "Repot"],
            "starpowers": ["Spiky", "Vigilance"],
        },
        "Clancy": {
            "rarity": "Mythic",
            "emoji": "<:C:1262408062153789501>",
            "gadgets": ["Snappy Shooting", "Tactical Retreat"],
            "starpowers": ["Recon", "Pumping Up"],
        },
        "Moe": {
            "rarity": "Mythic",
            "emoji": "<:M:1281346463519084646>",
            "gadgets": ["Dodgy Digging", "Rat Race"],
            "starpowers": ["Skipping Stones", "Speeding Ticket"],
        },
        "Juju": {
            "rarity": "Mythic",
            "emoji": "<:J:1320843530045751478>",
            "gadgets": ["Voodoo Chile", "Elementalist"],
            "starpowers": ["Guarded Gris-Gris", "Numbing Needles"],
        },
        "Ollie": {
            "rarity": "Mythic",
            "emoji": "<:O:1352278670097518653>",
            "gadgets": ["Regulate", "All Eyez On Me"],
            "starpowers": ["Kick, Push", "Renegade"],
        },
        "Finx": {
            "rarity": "Mythic",
            "emoji": "<:F:1352278666498932770>",
            "gadgets": ["Back To The Finxture", "No Escape"],
            "starpowers": ["Hieroglyph Halt", "Primer"],
        },
        # Legendary
        "Spike": {
            "rarity": "Legendary",
            "emoji": "<:S:776007474016288778>",
            "gadgets": ["Popping Pincushion", "Life Plant"],
            "starpowers": ["Fertilize", "Curveball"],
        },
        "Crow": {
            "rarity": "Legendary",
            "emoji": "<:C:776006753501708329>",
            "gadgets": ["Defense Booster", "Slowing Toxin"],
            "starpowers": ["Extra Toxic", "Carrion Crow"],
        },
        "Leon": {
            "rarity": "Legendary",
            "emoji": "<:L:776007475077578752>",
            "gadgets": ["Clone Projector", "Lollipop Drop"],
            "starpowers": ["Smoke Trails", "Invisiheal"],
        },
        "Sandy": {
            "rarity": "Legendary",
            "emoji": "<:S:776007475093569546>",
            "gadgets": ["Sleep Simulator", "Sweet Dreams"],
            "starpowers": ["Rude Sands", "Healing Winds"],
        },
        "Amber": {
            "rarity": "Legendary",
            "emoji": "<:A:776006753745502208>",
            "gadgets": ["Fire Starters", "Dancing Flames"],
            "starpowers": ["Wild Flames", "Scorchin' Siphon"],
        },
        "Meg": {
            "rarity": "Legendary",
            "emoji": "<:M:892446763103973398>",
            "gadgets": ["Jolting Volts", "Toolbox"],
            "starpowers": ["Force Field", "Self Destruction"],
        },
        "Surge": {
            "rarity": "Legendary",
            "emoji": "<:S:776007475261603841>",
            "gadgets": ["Power Surge", "Power Shield"],
            "starpowers": ["To The Max!", "Serve Ice Cold"],
        },
        "Chester": {
            "rarity": "Legendary",
            "emoji": "<:C:1052972358073335877>",
            "gadgets": ["Spicy Dice", "Candy Beans"],
            "starpowers": ["Bell'O'Mania", "Sneak Peek"],
        },
        "Cordelius": {
            "rarity": "Legendary",
            "emoji": "<:C:1125365776006774784>",
            "gadgets": ["Replanting", "Poison Mushroom"],
            "starpowers": ["Comboshrooms", "Mushroom Kingdom"],
        },
        "Kit": {
            "rarity": "Legendary",
            "emoji": "<:K:1201538441201078323>",
            "gadgets": ["Cardboard Box", "Cheeseburger"],
            "starpowers": ["Power Hungry", "Overly Attached"],
        },
        "Draco": {
            "rarity": "Legendary",
            "emoji": "<:D:1254748186799640646>",
            "gadgets": ["Upper Cut", "Last Stand"],
            "starpowers": ["Expose", "Shredding"],
        },
        "Kenji": {
            "rarity": "Legendary",
            "emoji": "<:K:1281346462562648157>",
            "gadgets": ["Dashi Dash", "Hosomaki Healing"],
            "starpowers": ["Studied The Blade", "Nigiri Nemesis"],
        },
    }

    gadgets_overwrite = {
        "Active Noise Cancelling": "Active Noise Canceling",  # Frank
        "Pocket Detonator": "Salty Barrel",  # Penny
        "Captain's Compass": "Trusty Spyglass",  # Penny
        "Sleep Simulator": "Sleep Stimulator",  # Sandy
        "Backup Mine": "Mine Mania",  # Tick
        "In Line": "Out Of Line",  # R-T
        "Warp Blast": "Warpin' Time",  # Nani
    }

    starpowers_overwrite = {
        "Extra Life": "Plugged In",  # 8-Bit
        "Insta Beeload": "Insta Beaload",  # Bea
        "Honey Coat": "Honeycomb",  # Bea
        "Snare a Bear": "Snare A Bear",  # Bo
        "Rocket No. Four": "Rocket No. 4",  # Brock
        "Incendiary": "More Rockets!",  # Brock
        "Bell'O'Mania": "Single Bell'O'Mania",  # Chester
        "Run n' Gun": "Run N Gun",  # Max
        "Self Destruction": "Heavy Metal",  # Meg
        "Tin Can": "Revolving Door",  # Mr P
        "Last Blast": "Heavy Coffers",  # Penny
        "Balls of Fire": "Master Blaster",  # Penny
    }

    emoji = {k: v["emoji"] for k, v in brawlers.items()}

    shop_gem_skins = {
        "Bandita Shelly": ("Shelly", "<:bs:597723269923078156>", 29),
        "Rockstar Colt": ("Colt", "<:rockc:597722687074467863>", 29),
        "Panda Nita": ("Nita", "<:pn:597723031577690153>", 29),
        "Pyro Spike": ("Spike", "<:P:1013874049702707321>", 49),
        "Ghost Squeak": ("Squeak", "<:G:1013874036092174366>", 49),
        "White Crow": ("Crow", "<:whc:597722720301613056>", 79),
        "Sakura Spike": ("Spike", "<:ss:597723306845667328>", 79),
        "El Rudo Primo": ("El Primo", "<:rup:597722827172347924>", 79),
        "Viking Bull": ("Bull", "<:vb:597722616148656128>", 79),
        "Road Rage Carl": ("Carl", "<:roc:597722660129996800>", 79),
        "Hog Rider Carl": ("Carl", "<:hrc:609102124009259049>", 79),
        "Maple Barley": ("Barley", "<:mb:597722509894221845>", 79),
        "Sally Leon": ("Leon", "<:sl:647789849666912286>", 79),
        "Leonard Carl": ("Carl", "<:le:647789849612648469>", 79),
        "Ivy Belle": ("Belle", "<:I:983298278194028594>", 79),
        "Ruby Prince Sprout": ("Sprout", "<:R:983298272493989898>", 79),
        "Neko Bea": ("Bea", "<:N:1013874044032012298>", 79),
        "Swamp Gene": ("Gene", "<:S:1013874051535610018>", 79),
        "Count Pengula": ("Mr P", "<:C:1013874025619013772>", 79),
        "Mr Fly": ("Mr P", "<:M:1013874041754505328>", 79),
        "Calavera Piper": ("Piper", "<:C:1013874022246797362>", 79),
        "Octo Fang": ("Fang", "<:O:1013874045831348355>", 79),
        "Galaxy Storm Lola": ("Lola", "<:G:1013874034305413150>", 79),
        "Krampus Ash": ("Ash", "<:K:1052981178975662190>", 79),
        "High Score Griff": ("Griff", "<:H:1052981182142357625>", 79),
        "Detective Gray": ("Gray", "<:D:1081879527665434626>", 79),
        "Spicy Mike": ("Dynamike", "<:spd:597722785862647850>", 149),
        "Popcorn Rico": ("Rico", "<:pr:597723232983973899>", 149),
        "Shiba Nita": ("Nita", "<:sn:597723031305060387>", 149),
        "Bakesale Barley": ("Barley", "<:bb:597722509747683339>", 149),
        "Robo Spike": ("Spike", "<:rs:597723306786947104>", 149),
        "El Brown": ("El Primo", "<:el:647789850191331338>", 149),
        "Tempest Tara": ("Tara", "<:T:983298276319170580>", 149),
        "Mantis Rosa": ("Rosa", "<:M:983298273924227084>", 149),
        "Monster Truck Meg": ("Meg", "<:M:983298270145150976>", 149),
        "Doctor Edgar": ("Edgar", "<:D:1013874030329204876>", 149),
        "Headless Rider Stu": ("Stu", "<:H:1013874039925772379>", 149),
        "Werewolf Leon": ("Leon", "<:W:1013874053561462834>", 149),
        "Witch Shelly": ("Shelly", "<:W:1013874055675396116>", 149),
        "Coral Belle": ("Belle", "<:C:1013874023945474170>", 149),
        "Gold Neko Bea": ("Bea", "<:G:1013874037715382425>", 149),
        "Empress Bonnie": ("Bonnie", "<:E:1013874032598335558>", 149),
        "Overlord Byron": ("Byron", "<:O:1013874047882366976>", 149),
        "World Champion Gus": ("Gus", "<:W:1052981180590473236>", 149),
        "Frost Queen Amber": ("Amber", "<:F:1052981175234342943>", 149),
        "Yeti Sam": ("Sam", "<:Y:1052981177469915196>", 149),
        "Amber De La Vega": ("Amber", "<:A:1081879860647055360>", 149),
        "Nutcracker Gale": ("Gale", "<:N:1081879652450173049>", 149),
        "Oni Otis": ("Otis", "<:O:1081879535907250256>", 149),
        "Tengu Mike": ("Dynamike", "<:T:1081879533717823518>", 149),
        "Kitsune Lola": ("Lola", "<:K:1081879531901702174>", 149),
        "Jungle Queen Maisie": ("Maisie", "<:J:1108819493372833884>", 149),
        "Bananas Colt": ("Colt", "<:B:1108819495113457724>", 149),
        "Jaguar Spirit Meg": ("Meg", "<:J:1108819497902682223>", 149),
        "Crocodile Buster": ("Buster", "<:C:1108819500557684859>", 149),
        "Robo Dynamike": ("Dynamike", "<:rd:597722785782956032>", 299),
        "Mecha Bo": ("Bo", "<:mbo:597722541951549441>", 299),
        "Mecha Crow": ("Crow", "<:mc:597722720209207296>", 299),
        "Mecha Mortis": ("Mortis", "<:M:1081879657462370314>", 299),
    }

    new_shop_gem_skins = {
        "Wood Spirit Chester": ("Chester", "<:W:1125365765105799259>", 79),
        "Stone Troll Lou": ("Lou", "<:S:1125365769258151998>", 149),
        "Dark Fairy Janet": ("Janet", "<:D:1125365767102267443>", 149),
        "Megalodon": ("Meg", "<:M:1125365770810052608>", 199),
    }

    new_shop_star_skins = {}

    shop_star_skins = {
        "Outlaw Colt": ("Colt", "<:oc:597722687087050753>", 500),
        "Linebacker Bull": ("Bull", "<:lb:597722616362696725>", 2500),
        "Light Mecha Bo": ("Bo", "<:lmb:597722542379237377>", 10000),
        "Night Mecha Crow": ("Crow", "<:nmc:597722720289030146>", 10000),
        "Postal Brock": ("Brock", "<:P:1081879654018842704>", 25000),
        "Inspector Colette": ("Colette", "<:I:1081879656120205352>", 25000),
        "Mariposa Piper": ("Piper", "<:M:1081879529431244910>", 25000),
        "Gold Mecha Bo": ("Bo", "<:gmb:597722542844674048>", 50000),
        "Gold Mecha Crow": ("Crow", "<:gmc:597722720524042250>", 50000),
    }

    special_skins = {
        "Star Shelly": "<:sts:597723270153764864>",  # Discord server
        #
        "Boom Box Brock": "<:bob:597722576936108062>",  # comeback
        "Wizard Barley": "<:wb:597722510028439573>",  # 100 servers
        "Bunny Penny": "<:bp:597723137521745930>",  # 1k servers
        "Brawl-O-Ween Rosa": "<:br:771763988593508353>",  # 50k & B-O-W 2020
        "Logmas Spike": "<:L:923487356777037884>",  # 100k & Brawlidays 2021
        "Summer Jessie": "<:sj:597722931338149898>",  # 1k members
        "Tanuki Jessie": "<:T:826771874196357142>",  # 10k members
        #
        "Red Nose Nita": "<:rn:597723031430758402>",  # Brawlidays 2019
        "Lil Helper Penny": "<:hp:597723137010040842>",  # Brawlidays 2019
        "Santamike": "<:sd:597722785485291558>",  # Brawlidays 2019
        #
        "Pirate Poco": "<:pi:791327646608261160>",  # Brawlidays 2020
        "Corsair Colt": "<:co:791328379990573057>",  # Brawlidays 2020
        #
        "Dragon Knight Jessie": "<:dj:597722931535020042>",  # prestige tier 4
        "Night Witch Mortis": "<:nm:597722977068646413>",  # prestige tier 8
        #
        "Phoenix Crow": "<:pc:597722720054018049>",  # VIP
        "Serenade Poco": "<:sp:597723181813465088>",  # VIP+
        "Royal Agent Colt": "<:rc:597722687124537344>",  # VIP++
    }

    for skin, properties in shop_gem_skins.items():
        emoji[skin] = properties[1]

    for skin, properties in new_shop_gem_skins.items():
        emoji[skin] = properties[1]

    for skin, properties in new_shop_star_skins.items():
        emoji[skin] = properties[1]

    for skin, properties in shop_star_skins.items():
        emoji[skin] = properties[1]

    emoji.update(special_skins)

    starting_brawler = [
        k for k, v in brawlers.items() if v["rarity"] == "Starting Brawler"
    ]
    rare_brawlers = [k for k, v in brawlers.items() if v["rarity"] == "Rare"]
    super_rare_brawlers = [
        k for k, v in brawlers.items() if v["rarity"] == "Super Rare"
    ]
    epic_brawlers = [k for k, v in brawlers.items() if v["rarity"] == "Epic"]
    mythic_brawlers = [
        k for k, v in brawlers.items() if v["rarity"] == "Mythic"
    ]
    legendary_brawlers = [
        k for k, v in brawlers.items() if v["rarity"] == "Legendary"
    ]

    droprates = {
        "pp": 92.1,
        "trophy": 0.0,
        "rare": 3.7,
        "sr": 2.3,
        "epic": 1.1,
        "mythic": 0.5,
        "legen": 0.3,
    }

    rarities = {
        "trophy": starting_brawler,
        "rare": rare_brawlers,
        "sr": super_rare_brawlers,
        "epic": epic_brawlers,
        "mythic": mythic_brawlers,
        "legen": legendary_brawlers,
    }

    brawler_categories = {
        "⚪ Starting Brawler": starting_brawler,
        "🟢 Rare": split_in_two(rare_brawlers)[0],
        "‎": split_in_two(rare_brawlers)[1],
        "🔵 Super Rare": split_in_three(super_rare_brawlers)[0],
        "‎" * 2: split_in_three(super_rare_brawlers)[1],
        "‎" * 3: split_in_three(super_rare_brawlers)[2],
        "🟣 Epic": split_in_three(epic_brawlers)[0],
        "‎" * 4: split_in_three(epic_brawlers)[1],
        "‎" * 5: split_in_three(epic_brawlers)[2],
        "🔴 Mythic": split_in_three(mythic_brawlers)[0],
        "‎" * 6: split_in_three(mythic_brawlers)[1],
        "‎" * 7: split_in_three(mythic_brawlers)[2],
        "🟡 Legendary": split_in_two(legendary_brawlers)[0],
        "‎" * 8: split_in_two(legendary_brawlers)[1],
    }

    rarity_emoji = {
        "Trophy Road": "🤍",
        "Rare": "💚",
        "Super Rare": "💙",
        "Epic": "💜",
        "Mythic": "❤",
        "Legendary": "💛",
    }

    icon_url = "https://papier.dis.tf/static/brawlbox/pins/{}.png"
    skin_icon_url = (
        "https://papier.dis.tf/static/brawlbox/pins/skins/{}/{}.png"
    )

    powerpoint_costs = [0, 20, 30, 50, 80, 130, 210, 340, 550, 890, 1440, 0]
