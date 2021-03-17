"""
Lookup tables for data on Chao

Data taken from: https://chao.tehfusion.co.uk/chao-hacking/
"""

# TODO : Checking function for this data.

DATA_TYPE_LENGTHS = {
    "Byte": 1,
    "Signed byte": 1,
    "Short": 2,
    "Int": 4,
    "Float": 4,
}

CHAO_OFFSETS = [
    {"Attribute": "Name", "Offset": 18, "Data type": "Name", "Lookup": None},
    {"Attribute": "Swim stat bar", "Offset": 32, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Fly stat bar", "Offset": 33, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Run stat bar", "Offset": 34, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Power stat bar", "Offset": 35, "Data type": "Byte", "Lookup": None},
    {
        "Attribute": "Stamina stat bar",
        "Offset": 36,
        "Data type": "Byte",
        "Lookup": None,
    },
    {"Attribute": "Luck stat bar", "Offset": 37, "Data type": "Byte", "Lookup": None},
    {
        "Attribute": "Intelligence stat bar",
        "Offset": 38,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat bar",
        "Offset": 39,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Swim stat grade",
        "Offset": 40,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Fly stat grade",
        "Offset": 41,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Run stat grade",
        "Offset": 42,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Power stat grade",
        "Offset": 43,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Stamina stat grade",
        "Offset": 44,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {"Attribute": "Luck stat grade", "Offset": 45, "Data type": "Byte", "Lookup": None},
    {
        "Attribute": "Intelligence stat grade",
        "Offset": 46,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat grade",
        "Offset": 47,
        "Data type": "Byte",
        "Lookup": None,
    },
    {"Attribute": "Swim stat level", "Offset": 48, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Fly stat level", "Offset": 49, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Run stat level", "Offset": 50, "Data type": "Byte", "Lookup": None},
    {
        "Attribute": "Power stat level",
        "Offset": 51,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Stamina stat level",
        "Offset": 52,
        "Data type": "Byte",
        "Lookup": None,
    },
    {"Attribute": "Luck stat level", "Offset": 53, "Data type": "Byte", "Lookup": None},
    {
        "Attribute": "Intelligence stat level",
        "Offset": 54,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat level",
        "Offset": 55,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Swim stat points",
        "Offset": 56,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Fly stat points",
        "Offset": 58,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Run stat points",
        "Offset": 60,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Power stat points",
        "Offset": 62,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Stamina stat points",
        "Offset": 64,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Luck stat points",
        "Offset": 66,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Intelligence stat points",
        "Offset": 68,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat points",
        "Offset": 70,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Chao type",
        "Offset": 128,
        "Data type": "Byte",
        "Lookup": "ChaoType",
    },
    {
        "Attribute": "Chao garden",
        "Offset": 129,
        "Data type": "Byte",
        "Lookup": "SA2BChaoGarden",
    },
    {
        "Attribute": "Happiness",
        "Offset": 130,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Remaining lifespan 1",
        "Offset": 138,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Remaining lifespan 2",
        "Offset": 140,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Reincarnations",
        "Offset": 142,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Run ↔ Power transformation",
        "Offset": 168,
        "Data type": "Float",
        "Lookup": None,
    },
    {
        "Attribute": "Swim ↔ Fly transformation",
        "Offset": 172,
        "Data type": "Float",
        "Lookup": None,
    },
    {"Attribute": "Alignment", "Offset": 176, "Data type": "Float", "Lookup": None},
    {
        "Attribute": "Transformation magnitude",
        "Offset": 192,
        "Data type": "Float",
        "Lookup": None,
    },
    {"Attribute": "Eyes", "Offset": 209, "Data type": "Byte", "Lookup": "Eyes"},
    {"Attribute": "Mouth", "Offset": 210, "Data type": "Byte", "Lookup": "Mouth"},
    {
        "Attribute": "Emotiball",
        "Offset": 211,
        "Data type": "Byte",
        "Lookup": "Emotiball",
    },
    {"Attribute": "Hat", "Offset": 213, "Data type": "Byte", "Lookup": "SA2BHat"},
    {
        "Attribute": "Hidden feet flag",
        "Offset": 214,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {"Attribute": "Medal", "Offset": 215, "Data type": "Byte", "Lookup": "Medal"},
    {"Attribute": "Colour", "Offset": 216, "Data type": "Byte", "Lookup": "SA2BColour"},
    {
        "Attribute": "Mono-tone flag",
        "Offset": 217,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Texture",
        "Offset": 218,
        "Data type": "Byte",
        "Lookup": "SA2BTexture",
    },
    {"Attribute": "Shiny flag", "Offset": 219, "Data type": "Boolean", "Lookup": None},
    {
        "Attribute": "Egg colour",
        "Offset": 220,
        "Data type": "Byte",
        "Lookup": "SA2BEggColour",
    },
    {
        "Attribute": "Body type",
        "Offset": 221,
        "Data type": "Byte",
        "Lookup": "SA2BBodyType",
    },
    {
        "Attribute": "Body type animal",
        "Offset": 222,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B animal behaviours",
        "Offset": 280,
        "Data type": "Short",
        "Lookup": "SA2BAnimalFlags",
    },
    {
        "Attribute": "SA2B arms part",
        "Offset": 284,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B ears part",
        "Offset": 285,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B forehead part",
        "Offset": 286,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B horns part",
        "Offset": 287,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B legs part",
        "Offset": 288,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B tail part",
        "Offset": 289,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B wings part",
        "Offset": 290,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {
        "Attribute": "SA2B face part",
        "Offset": 291,
        "Data type": "Byte",
        "Lookup": "SA2BAnimal",
    },
    {"Attribute": "Sleepiness", "Offset": 292, "Data type": "Short", "Lookup": None},
    {"Attribute": "Joy", "Offset": 300, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Urge to cry", "Offset": 302, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Fear", "Offset": 303, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Dizziness", "Offset": 305, "Data type": "Byte", "Lookup": None},
    {"Attribute": "Tiredness", "Offset": 310, "Data type": "Short", "Lookup": None},
    {"Attribute": "Hunger", "Offset": 312, "Data type": "Short", "Lookup": None},
    {
        "Attribute": "Desire to mate",
        "Offset": 314,
        "Data type": "Short",
        "Lookup": None,
    },
    {"Attribute": "Boredom", "Offset": 316, "Data type": "Short", "Lookup": None},
    {"Attribute": "Energy", "Offset": 328, "Data type": "Short", "Lookup": None},
    {
        "Attribute": "Normal ↔ Curious personality",
        "Offset": 330,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Cry Baby ↔ Energetic personality",
        "Offset": 332,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Naive ↔ Normal personality",
        "Offset": 333,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Normal ↔ Big Eater personality",
        "Offset": 336,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Normal ↔ Carefree personality",
        "Offset": 341,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Favourite fruit",
        "Offset": 343,
        "Data type": "Byte",
        "Lookup": "FavouriteFruit",
    },
    {
        "Attribute": "Cough level",
        "Offset": 346,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Cold level",
        "Offset": 347,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Rash level",
        "Offset": 348,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Runny nose level",
        "Offset": 349,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Hiccups level",
        "Offset": 350,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Stomach ache level",
        "Offset": 351,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B classroom skills",
        "Offset": 352,
        "Data type": "Int",
        "Lookup": "ClassroomLessonFlags",
    },
    {
        "Attribute": "SA2B toys",
        "Offset": 356,
        "Data type": "Short",
        "Lookup": "ToyFlags",
    },
    {
        "Attribute": "SA2B Sonic bond",
        "Offset": 364,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B Shadow bond",
        "Offset": 370,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B Tails bond",
        "Offset": 376,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B Eggman bond",
        "Offset": 382,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B Knuckles bond",
        "Offset": 388,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SA2B Rouge bond",
        "Offset": 394,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Reset trigger",
        "Offset": 1080,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Swim stat grade 1",
        "Offset": 1172,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Swim stat grade 2",
        "Offset": 1173,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Fly stat grade 1",
        "Offset": 1174,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Fly stat grade 2",
        "Offset": 1175,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Run stat grade 1",
        "Offset": 1176,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Run stat grade 2",
        "Offset": 1177,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Power stat grade 1",
        "Offset": 1178,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Power stat grade 2",
        "Offset": 1179,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Stamina stat grade 1",
        "Offset": 1180,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Stamina stat grade 2",
        "Offset": 1181,
        "Data type": "Byte",
        "Lookup": "Grade",
    },
    {
        "Attribute": "Luck stat grade 1",
        "Offset": 1182,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Luck stat grade 2",
        "Offset": 1183,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Intelligence stat grade 1",
        "Offset": 1184,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Intelligence stat grade 2",
        "Offset": 1185,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat grade 1",
        "Offset": 1186,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Unknown stat grade 2",
        "Offset": 1187,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Favourite fruit 1",
        "Offset": 1222,
        "Data type": "Byte",
        "Lookup": "FavouriteFruit",
    },
    {
        "Attribute": "Favourite fruit 2",
        "Offset": 1223,
        "Data type": "Byte",
        "Lookup": "FavouriteFruit",
    },
    {
        "Attribute": "Colour 1",
        "Offset": 1228,
        "Data type": "Byte",
        "Lookup": "SA2BColour",
    },
    {
        "Attribute": "Colour 2",
        "Offset": 1229,
        "Data type": "Byte",
        "Lookup": "SA2BColour",
    },
    {
        "Attribute": "Mono-tone flag 1",
        "Offset": 1230,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Mono-tone flag 2",
        "Offset": 1231,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Texture 1",
        "Offset": 1232,
        "Data type": "Byte",
        "Lookup": "SA2BTexture",
    },
    {
        "Attribute": "Texture 2",
        "Offset": 1233,
        "Data type": "Byte",
        "Lookup": "SA2BTexture",
    },
    {
        "Attribute": "Shiny flag 1",
        "Offset": 1234,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Shiny flag 2",
        "Offset": 1235,
        "Data type": "Boolean",
        "Lookup": None,
    },
    {
        "Attribute": "Egg colour 1",
        "Offset": 1236,
        "Data type": "Byte",
        "Lookup": "SA2BEggColour",
    },
    {
        "Attribute": "Egg colour 2",
        "Offset": 1237,
        "Data type": "Byte",
        "Lookup": "SA2BEggColour",
    },
    {
        "Attribute": "SADX animal behaviours",
        "Offset": 1248,
        "Data type": "Short",
        "Lookup": "SADXAnimalFlags",
    },
    {
        "Attribute": "SADX arms part",
        "Offset": 1258,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX ears part",
        "Offset": 1253,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX forehead part",
        "Offset": 1254,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX horns part",
        "Offset": 1255,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX legs part",
        "Offset": 1256,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX tail part",
        "Offset": 1257,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX wings part",
        "Offset": 1258,
        "Data type": "Byte",
        "Lookup": "SADXAnimal",
    },
    {
        "Attribute": "SADX Sonic bond",
        "Offset": 1276,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SADX Tails bond",
        "Offset": 1282,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SADX Knuckles bond",
        "Offset": 1288,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SADX Amy bond",
        "Offset": 1294,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SADX E-102 Gamma bond",
        "Offset": 1300,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "SADX Big bond",
        "Offset": 1306,
        "Data type": "Signed byte",
        "Lookup": None,
    },
    {
        "Attribute": "Crab Pool Race Time",
        "Offset": 224,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Stumo Valley Race Time",
        "Offset": 227,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Mushroom Forest Race Time",
        "Offset": 230,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Block Canyon Race Time",
        "Offset": 233,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Aquamarine Race Time",
        "Offset": 236,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Topaz Race Time",
        "Offset": 239,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Peridot Race Time",
        "Offset": 242,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "Garnet Race Time",
        "Offset": 245,
        "Data type": "Time",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_1 (tick-up)",
        "Offset": 164,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_2 (tick-up)",
        "Offset": 294,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_3 (tick-up)",
        "Offset": 296,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_4 (tick-up)",
        "Offset": 298,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_5 (tick-down character proximity?)",
        "Offset": 306,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "UNKNOWN_TIMER_6 (tick-up)",
        "Offset": 360,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_01 (tick-up character proximity?)",
        "Offset": 954,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_02 (tick-up character proximity?)",
        "Offset": 926,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_02 (tick-up character proximity?)",
        "Offset": 898,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_03 (tick-up character proximity?)",
        "Offset": 870,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_04 (tick-up character proximity?)",
        "Offset": 842,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_05 (tick-up character proximity?)",
        "Offset": 814,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_06 (tick-up character proximity?)",
        "Offset": 786,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_07 (tick-up character proximity?)",
        "Offset": 758,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_08 (tick-up character proximity?)",
        "Offset": 730,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_09 (tick-up character proximity?)",
        "Offset": 702,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_10 (tick-up character proximity?)",
        "Offset": 674,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_11 (tick-up character proximity?)",
        "Offset": 646,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_12 (tick-up character proximity?)",
        "Offset": 618,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_13 (tick-up character proximity?)",
        "Offset": 590,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_14 (tick-up character proximity?)",
        "Offset": 534,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_15 (tick-up character proximity?)",
        "Offset": 506,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_17 (tick-up character proximity?)",
        "Offset": 478,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_18 (tick-up character proximity?)",
        "Offset": 450,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_19 (tick-up character proximity?)",
        "Offset": 422,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_20 (tick-up character proximity?)",
        "Offset": 926,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "PARALLEL_TIMER_21 (tick-up character proximity?)",
        "Offset": 562,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Karate Rounds Played",
        "Offset": 270,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Karate Rounds Won",
        "Offset": 272,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Karate Rounds Lost",
        "Offset": 274,
        "Data type": "Short",
        "Lookup": None,
    },
    {
        "Attribute": "Karate Rank (Fights)",
        "Offset": 266,
        "Data type": "Byte",
        "Lookup": None,
    },
    {
        "Attribute": "Karate Rank (Tournaments)",
        "Offset": 267,
        "Data type": "Byte",
        "Lookup": None,
    },
]

CHARACTER_ENCODING = {
    0: "",
    1: "!",
    2: "”",
    3: "#",
    4: "$",
    5: "%",
    6: "&",
    7: "\\",
    8: "(",
    9: ")",
    10: "*",
    11: "+",
    12: ",",
    13: "-",
    14: ".",
    15: "/",
    16: "0",
    17: "1",
    18: "2",
    19: "3",
    20: "4",
    21: "5",
    22: "6",
    23: "7",
    24: "8",
    25: "9",
    26: ":",
    27: ";",
    28: "<",
    29: "=",
    30: ">",
    31: "?",
    32: "@",
    33: "A",
    34: "B",
    35: "C",
    36: "D",
    37: "E",
    38: "F",
    39: "G",
    40: "H",
    41: "I",
    42: "J",
    43: "K",
    44: "L",
    45: "M",
    46: "N",
    47: "O",
    48: "P",
    49: "Q",
    50: "R",
    51: "S",
    52: "T",
    53: "U",
    54: "V",
    55: "W",
    56: "X",
    57: "Y",
    58: "Z",
    59: "[",
    60: "¥",
    61: "]",
    62: "^",
    63: "_",
    64: "‘",
    65: "a",
    66: "b",
    67: "c",
    68: "d",
    69: "e",
    70: "f",
    71: "g",
    72: "h",
    73: "i",
    74: "j",
    75: "k",
    76: "l",
    77: "m",
    78: "n",
    79: "o",
    80: "p",
    81: "q",
    82: "r",
    83: "s",
    84: "t",
    85: "u",
    86: "v",
    87: "w",
    88: "x",
    89: "y",
    90: "z",
    91: "{",
    92: "|",
    93: "}",
    94: "~",
    95: " ",
    96: "À",
    97: "Á",
    98: "Â",
    99: "Ã",
    100: "Ä",
    101: "Å",
    102: "Æ",
    103: "Ç",
    104: "È",
    105: "É",
    106: "Ê",
    107: "Ë",
    108: "Ì",
    109: "Í",
    110: "Î",
    111: "Ï",
    112: "Ð",
    113: "Ñ",
    114: "Ò",
    115: "Ó",
    116: "Ô",
    117: "Õ",
    118: "Ö",
    119: "¿",
    120: "Ø",
    121: "Ù",
    122: "Ú",
    123: "Û",
    124: "Ü",
    125: "Ý",
    126: "Þ",
    127: "ß",
    128: "à",
    129: "á",
    130: "â",
    131: "ã",
    132: "ä",
    133: "å",
    134: "æ",
    135: "ç",
    136: "è",
    137: "é",
    138: "ê",
    139: "ë",
    140: "ì",
    141: "í",
    142: "î",
    143: "ï",
    144: "ð",
    145: "ñ",
    146: "ò",
    147: "ó",
    148: "ô",
    149: "õ",
    150: "ö",
    151: "¡",
    152: "ø",
    153: "ù",
    154: "ú",
    155: "û",
    156: "ü",
    157: "ý",
    158: "þ",
    159: "ÿ",
    160: "ァ",
    161: "ア",
    162: "ィ",
    163: "イ",
    164: "ゥ",
    165: "ウ",
    166: "ェ",
    167: "エ",
    168: "ォ",
    169: "オ",
    170: "カ",
    171: "ガ",
    172: "キ",
    173: "ギ",
    174: "ク",
    175: "グ",
    176: "ケ",
    177: "ゲ",
    178: "コ",
    179: "ゴ",
    180: "サ",
    181: "ザ",
    182: "シ",
    183: "ジ",
    184: "ス",
    185: "ズ",
    186: "セ",
    187: "ゼ",
    188: "ソ",
    189: "ゾ",
    190: "タ",
    191: "ダ",
    192: "チ",
    193: "ヂ",
    194: "ツ",
    195: "ッ",
    196: "ヅ",
    197: "テ",
    198: "デ",
    199: "ト",
    200: "ド",
    201: "ナ",
    202: "ニ",
    203: "ヌ",
    204: "ネ",
    205: "ノ",
    206: "ハ",
    207: "バ",
    208: "パ",
    209: "ヒ",
    210: "ビ",
    211: "ピ",
    212: "フ",
    213: "ブ",
    214: "プ",
    215: "ヘ",
    216: "ベ",
    217: "ペ",
    218: "ホ",
    219: "ボ",
    220: "ポ",
    221: "マ",
    222: "ミ",
    223: "ム",
    224: "メ",
    225: "モ",
    226: "ャ",
    227: "ヤ",
    228: "ュ",
    229: "ユ",
    230: "ョ",
    231: "ヨ",
    232: "ラ",
    233: "リ",
    234: "ル",
    235: "レ",
    236: "ロ",
    237: "ヮ",
    238: "ワ",
    239: "ﾞ",
    240: "ﾟ",
    241: "ヲ",
    242: "ン",
    243: "。",
    244: "、",
    245: "〒",
    246: "・",
    247: "★",
    248: "♀",
    249: "♂",
    250: "♪",
    251: "…",
    252: "「",
    253: "」",
    254: "ヴ",
    255: " ",
}
