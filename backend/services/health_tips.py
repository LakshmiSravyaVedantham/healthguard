"""60+ bilingual health tips for 50+ Indians."""

import random

HEALTH_TIPS = [
    # --- Blood Pressure ---
    {
        "telugu": "Uppu takkuva tinandi. Rojuku 5 grams kanna takkuva uppu manchidi. BP control lo untundi.",
        "english": "Reduce salt intake. Less than 5g per day helps control blood pressure.",
    },
    {
        "telugu": "Banana, sweet potato, palakura lo potassium ekkuva. BP takkuva chestundi.",
        "english": "Bananas, sweet potatoes, and spinach are rich in potassium - great for lowering BP.",
    },
    {
        "telugu": "Rojuu BP check cheyandi. 120/80 normal. 140/90 paina doctor ki chupinchandi.",
        "english": "Check BP daily. 120/80 is normal. Above 140/90, consult your doctor.",
    },
    {
        "telugu": "Stress takkuva chesukundi. Deep breathing cheyandi. BP ki manchidi.",
        "english": "Manage stress with deep breathing. It helps lower blood pressure.",
    },
    {
        "telugu": "Vellullipaaya (garlic) rojuu okati tinandi. BP ki chaalaa manchidi.",
        "english": "Eat a clove of garlic daily. It's excellent for blood pressure.",
    },

    # --- Diabetes ---
    {
        "telugu": "White rice badulu brown rice leda ragi mudda tinandi. Sugar control lo untundi.",
        "english": "Replace white rice with brown rice or ragi. It helps control blood sugar.",
    },
    {
        "telugu": "Tinina tarvatha 15 nimishaalu nadavandi. Sugar level takkuva avutundi.",
        "english": "Walk for 15 minutes after meals. It helps lower blood sugar levels.",
    },
    {
        "telugu": "Methi ginjallu raatri neellu lo nana pettandi. Poddu taagandi. Sugar ki manchidi.",
        "english": "Soak fenugreek (methi) seeds overnight. Drink the water in morning for diabetes control.",
    },
    {
        "telugu": "Sugar level empty stomach lo 100 kanna takkuva undaali. Regular ga check cheyandi.",
        "english": "Fasting blood sugar should be below 100. Check regularly.",
    },
    {
        "telugu": "Sweet fruits takkuva tinandi. Guava, apple, papaya manchivi. Mango, grapes takkuva.",
        "english": "Choose low-sugar fruits: guava, apple, papaya. Limit mango, grapes.",
    },
    {
        "telugu": "Kaaram takkuva, fibre ekkuva tinandi. Vegetables ekkuva tinandi.",
        "english": "Eat less spice, more fiber. Load up on vegetables.",
    },

    # --- Joint Pain / Arthritis ---
    {
        "telugu": "Rojuu 20 nimishaalu mellaga nadavandi. Joints ki manchidi.",
        "english": "Walk slowly for 20 minutes daily. It keeps joints healthy.",
    },
    {
        "telugu": "Venniti neellu (warm water) lo Epsom salt vesi kaallaki pedthey noppi takkuva avutundi.",
        "english": "Soak feet in warm water with Epsom salt to reduce joint pain.",
    },
    {
        "telugu": "Pasupu paalu raatri taagandi. Turmeric lo anti-inflammatory properties unnayi.",
        "english": "Drink turmeric milk at night. Turmeric has anti-inflammatory properties.",
    },
    {
        "telugu": "Calcium kosam paalu, perugu, raagi tinandi. Bones strong avutaayi.",
        "english": "Eat dairy, curd, and ragi for calcium. Strong bones mean healthier joints.",
    },
    {
        "telugu": "Heavy weights eththakandi. Joints ki damage avutundi.",
        "english": "Avoid lifting heavy weights. It can damage your joints.",
    },

    # --- Eye Health ---
    {
        "telugu": "20-20-20 rule follow cheyandi: 20 nimishaalaki okasaari 20 feet door choodandi 20 seconds.",
        "english": "Follow 20-20-20 rule: Every 20 min, look 20 feet away for 20 seconds.",
    },
    {
        "telugu": "Carrot, papaya, green leafy vegetables kallu ki manchivi.",
        "english": "Carrots, papaya, and green leafy vegetables are great for eye health.",
    },
    {
        "telugu": "Sunlight lo bayata vellethappudu sunglasses pedthey kallu ki protection untundi.",
        "english": "Wear sunglasses outdoors to protect your eyes from UV rays.",
    },
    {
        "telugu": "Phone/TV screen eppudu kallu level lo undaali. Kinda choodakandi.",
        "english": "Keep screens at eye level. Don't look down at phones for long periods.",
    },
    {
        "telugu": "Year ki okasaari eye checkup cheyinchukundi. Cataract, glaucoma early lo pattukovachu.",
        "english": "Get an eye checkup yearly. Catch cataracts and glaucoma early.",
    },

    # --- Diet & Nutrition ---
    {
        "telugu": "Rojuu 5 variety vegetables tinandi. Different colors lo different nutrients untaayi.",
        "english": "Eat 5 different colored vegetables daily for varied nutrients.",
    },
    {
        "telugu": "Paala kosam cow milk, curd, paneer manchivi. Calcium ki avasaram.",
        "english": "Milk, curd, and paneer are great sources of calcium. Essential after 50.",
    },
    {
        "telugu": "Baadaam, walnut, pista rojuu kotta mukka tinandi. Heart ki manchivi.",
        "english": "Eat a handful of almonds, walnuts, or pistachios daily. Great for heart.",
    },
    {
        "telugu": "Oil lo deep fry chesina items takkuva tinandi. Steam, boil manchidi.",
        "english": "Avoid deep-fried foods. Prefer steamed or boiled preparations.",
    },
    {
        "telugu": "Rojuu oka pandu (fruit) tinandi. Seasonal fruits best.",
        "english": "Eat one seasonal fruit every day.",
    },
    {
        "telugu": "Dinner 7-8 PM ki tinandi. Late ga tintey digestion problem vasthundi.",
        "english": "Eat dinner by 7-8 PM. Late eating causes digestive problems.",
    },
    {
        "telugu": "Kobbarinune (coconut oil) leda nuvvula nune (sesame oil) cooking ki manchidi.",
        "english": "Use coconut oil or sesame oil for cooking - healthier than refined oils.",
    },

    # --- Hydration ---
    {
        "telugu": "Rojuku 8-10 glasses neellu taagandi. Dehydration common after 50.",
        "english": "Drink 8-10 glasses of water daily. Dehydration is common after 50.",
    },
    {
        "telugu": "Poddu leechaka okka glass venniti neellu taagandi. Digestion ki manchidi.",
        "english": "Drink a glass of warm water first thing in the morning for digestion.",
    },
    {
        "telugu": "Buttermilk (majjiga) summer lo best. Hydration + probiotics.",
        "english": "Buttermilk is perfect for summer - hydrating and probiotic-rich.",
    },
    {
        "telugu": "Neellu taagadam marchipothey phone daaggara bottle pettandi.",
        "english": "Keep a water bottle nearby so you don't forget to drink.",
    },
    {
        "telugu": "Coffee, tea 2-3 cups ki limit cheyandi. Ekkuva taagithey dehydration avutundi.",
        "english": "Limit tea/coffee to 2-3 cups. Excess caffeine causes dehydration.",
    },

    # --- Sleep ---
    {
        "telugu": "Rojuu 7-8 hours nidra poyyandi. Nidra rakapothe doctor ni adagandi.",
        "english": "Sleep 7-8 hours daily. Consult doctor if you have trouble sleeping.",
    },
    {
        "telugu": "Nidra poye mundhu phone choodakandi. Blue light nidra ki aatankam.",
        "english": "Avoid phones before bed. Blue light disrupts sleep.",
    },
    {
        "telugu": "Rojuu same time ki padukundi, same time ki leychandi. Body clock set avutundi.",
        "english": "Sleep and wake at the same time daily. It sets your body clock.",
    },
    {
        "telugu": "Raatri paalu lo pasupu vesi taagandi. Nidra baagaa vastundi.",
        "english": "Drink turmeric milk before bed. It promotes better sleep.",
    },

    # --- Mental Health ---
    {
        "telugu": "Rojuku 10 nimishaalu meditation cheyandi. Manassuku shaanthi vasthundi.",
        "english": "Meditate 10 minutes daily. It brings peace of mind.",
    },
    {
        "telugu": "Friends tho maatlaadandi, bayata vellandi. Okkara ga undakandi.",
        "english": "Talk to friends, go outside. Don't stay isolated.",
    },
    {
        "telugu": "Hobby chesukundi - gardening, reading, music. Active ga undandi.",
        "english": "Keep a hobby - gardening, reading, music. Stay mentally active.",
    },
    {
        "telugu": "Baadha ga unte family tho cheppandi. Mental health kuda important.",
        "english": "If feeling sad, talk to family. Mental health matters too.",
    },
    {
        "telugu": "Rojuu oka manchi pani cheyandi - evariko help cheyandi. Happiness vastundi.",
        "english": "Do one good deed daily - help someone. It brings happiness.",
    },

    # --- Heart Health ---
    {
        "telugu": "Rojuu 30 nimishaalu exercise cheyandi. Heart strong avutundi.",
        "english": "Exercise 30 minutes daily to keep your heart strong.",
    },
    {
        "telugu": "Ghee moderation lo tinandi. Ekkuva tintey cholesterol perugutundi.",
        "english": "Use ghee in moderation. Excess increases cholesterol.",
    },
    {
        "telugu": "Omega-3 kosam fish, flaxseeds, walnuts tinandi. Heart ki manchidi.",
        "english": "Eat fish, flaxseeds, walnuts for Omega-3 - great for heart health.",
    },
    {
        "telugu": "Smoking, alcohol avoid cheyandi. Heart ki chaalaa harmful.",
        "english": "Avoid smoking and alcohol. Very harmful for the heart.",
    },

    # --- Bone Health ---
    {
        "telugu": "Poddu 15-20 nimishaalu sunlight lo undandi. Vitamin D vastundi.",
        "english": "Spend 15-20 minutes in morning sunlight for Vitamin D.",
    },
    {
        "telugu": "Calcium tablets doctor cheppinatte teesukundi. Bones weak avakunda.",
        "english": "Take calcium supplements as prescribed by your doctor.",
    },
    {
        "telugu": "Steps ekkethappudu jagrathaga undandi. Falls ki risk ekkuva 50 tarvatha.",
        "english": "Be careful on stairs. Fall risk increases after 50.",
    },

    # --- Digestive Health ---
    {
        "telugu": "Fibre food ekkuva tinandi - fruits, vegetables, whole grains. Constipation raadu.",
        "english": "Eat high-fiber foods - fruits, vegetables, whole grains - to prevent constipation.",
    },
    {
        "telugu": "Tinedappudu mellaga navaandi (chew). 20 saarlu navaandi tarvatha mingandi.",
        "english": "Chew food slowly - at least 20 chews before swallowing.",
    },
    {
        "telugu": "Perugu rojuu tinandi. Gut health ki probiotics avasaram.",
        "english": "Eat curd daily. Probiotics are essential for gut health.",
    },

    # --- General Wellness ---
    {
        "telugu": "Year ki 2 saarlu full body checkup cheyinchukundi.",
        "english": "Get a full body checkup twice a year.",
    },
    {
        "telugu": "Mandulu time ki teesukundi. Miss cheyakandi. Doctor cheppinatte follow avandi.",
        "english": "Take medicines on time. Never skip. Follow doctor's instructions.",
    },
    {
        "telugu": "Dengue, malaria raakunda mosquito nets vadandi. Neellu nilva pettakandi.",
        "english": "Use mosquito nets. Don't let water stagnate - prevents dengue and malaria.",
    },
    {
        "telugu": "Rojuku oka saari navvandi - laughing ki health benefits ekkuva!",
        "english": "Laugh every day - laughter has many health benefits!",
    },
    {
        "telugu": "Positive ga alochinchandi. Happy ga undandi. Aarogyam automatic ga vasthundi.",
        "english": "Think positive, stay happy. Good health follows a happy mind.",
    },
    {
        "telugu": "Temple ki, park ki, walking ki vellandi. Bayata gaali pilavandi.",
        "english": "Visit temples, parks, go for walks. Breathe fresh air.",
    },
    {
        "telugu": "Flu vaccination year ki okasaari teesukundi. Elders ki important.",
        "english": "Get a flu vaccination yearly. Very important for elders.",
    },
    {
        "telugu": "Shoes comfortable ga undaali. Tight shoes valla kaalu noppulu vasthaayi.",
        "english": "Wear comfortable shoes. Tight shoes cause foot pain.",
    },
    {
        "telugu": "AC room lo ekkuva sepu undakandi. Natural gaali manchidi.",
        "english": "Don't stay in AC for too long. Natural air is healthier.",
    },
    {
        "telugu": "Teeth ki kuda care cheyandi. 6 months ki okasaari dentist ki vellandi.",
        "english": "Take care of your teeth too. Visit dentist every 6 months.",
    },
]


def get_random_tip(language: str = "both") -> str:
    """Get a random health tip in the specified language."""
    tip = random.choice(HEALTH_TIPS)
    lang = language if language in ("telugu", "english") else "both"

    if lang == "both":
        return f"{tip['telugu']}\n\n{tip['english']}"
    return tip.get(lang, tip["english"])


def get_tip_by_index(index: int, language: str = "both") -> str:
    """Get a specific health tip by index."""
    tip = HEALTH_TIPS[index % len(HEALTH_TIPS)]
    lang = language if language in ("telugu", "english") else "both"

    if lang == "both":
        return f"{tip['telugu']}\n\n{tip['english']}"
    return tip.get(lang, tip["english"])
