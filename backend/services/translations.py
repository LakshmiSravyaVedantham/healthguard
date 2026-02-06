"""Telugu + English bilingual message dictionary for HealthGuard."""

MESSAGES = {
    # --- Onboarding ---
    "welcome": {
        "telugu": (
            "🙏 *HealthGuard* ki Swagatam!\n"
            "Mee aarogyam kosam memu ikkadunnaam.\n\n"
            "Dayachesi mee bhaasha eenchukundi:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both (Telugu + English)"
        ),
        "english": (
            "🙏 Welcome to *HealthGuard*!\n"
            "We are here to take care of your health.\n\n"
            "Please choose your language:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both (Telugu + English)"
        ),
        "both": (
            "🙏 *HealthGuard* ki Swagatam! Welcome!\n"
            "Mee aarogyam kosam memu ikkadunnaam.\n"
            "We are here for your health.\n\n"
            "Dayachesi mee bhaasha eenchukundi / Choose language:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both (Telugu + English)"
        ),
    },
    "ask_name": {
        "telugu": "Mee peru cheppandi (Type your name):",
        "english": "Please type your name:",
        "both": "Mee peru cheppandi / Please type your name:",
    },
    "ask_age": {
        "telugu": "Mee vayasu cheppandi (Type your age):",
        "english": "Please type your age:",
        "both": "Mee vayasu cheppandi / Please type your age:",
    },
    "onboarding_complete": {
        "telugu": (
            "🎉 Dhanyavaadaalu, {name} gaaru!\n"
            "Mee HealthGuard siddham ayyindi.\n"
            "Rojuu health tips, medicine reminders vasthaayi.\n\n"
            "Menu kosam 0 press cheyandi."
        ),
        "english": (
            "🎉 Thank you, {name}!\n"
            "Your HealthGuard is ready.\n"
            "You will receive daily health tips and medicine reminders.\n\n"
            "Press 0 for the menu."
        ),
        "both": (
            "🎉 Dhanyavaadaalu, {name} gaaru! Thank you!\n"
            "Mee HealthGuard siddham ayyindi. Your health companion is ready.\n"
            "Rojuu health tips, medicine reminders vasthaayi.\n\n"
            "Menu kosam 0 press cheyandi / Press 0 for menu."
        ),
    },

    # --- Main Menu (Exercise-first design) ---
    "main_menu": {
        "telugu": (
            "🏥 *HealthGuard Menu*\n\n"
            "1 - 🧘 వ్యాయామం (Exercise)\n"
            "2 - 💡 ఆరోగ్య సలహా (Health Tip)\n"
            "3 - 😊 ఎలా ఉన్నారు? (How are you?)\n"
            "4 - 💊 మందులు (Medicines)\n"
            "5 - 🚨 అపత్కాల సమాచారం (Emergency)\n"
            "6 - భాష మార్చండి (Language)\n\n"
            "Number type cheyandi."
        ),
        "english": (
            "🏥 *HealthGuard Menu*\n\n"
            "1 - 🧘 Exercise\n"
            "2 - 💡 Health Tip\n"
            "3 - 😊 How are you?\n"
            "4 - 💊 Medicines\n"
            "5 - 🚨 Emergency Info\n"
            "6 - Change Language\n\n"
            "Type a number."
        ),
        "both": (
            "🏥 *HealthGuard Menu*\n\n"
            "1 - 🧘 వ్యాయామం / Exercise\n"
            "2 - 💡 ఆరోగ్య సలహా / Health Tip\n"
            "3 - 😊 ఎలా ఉన్నారు? / How are you?\n"
            "4 - 💊 మందులు / Medicines\n"
            "5 - 🚨 అపత్కాల సమాచారం / Emergency\n"
            "6 - భాష మార్చండి / Language\n\n"
            "Number type cheyandi / Type a number."
        ),
    },

    # --- Health Tip ---
    "health_tip_prefix": {
        "telugu": "💡 *Neti Aarogya Salaaha:*\n\n",
        "english": "💡 *Today's Health Tip:*\n\n",
        "both": "💡 *Neti Aarogya Salaaha / Today's Health Tip:*\n\n",
    },

    # --- Medicine Check ---
    "medicine_list_header": {
        "telugu": "💊 *Neti Mandulu:*\n\n",
        "english": "💊 *Today's Medicines:*\n\n",
        "both": "💊 *Neti Mandulu / Today's Medicines:*\n\n",
    },
    "medicine_confirm": {
        "telugu": (
            "\n✅ Teesukunnaru ante 1 press cheyandi.\n"
            "1 - Teesukunnanu ✅\n"
            "0 - Menu ki vellandi"
        ),
        "english": (
            "\n✅ Press 1 if you took them.\n"
            "1 - Done ✅\n"
            "0 - Back to menu"
        ),
        "both": (
            "\n✅ Teesukunnaru ante 1 / Press 1 if done.\n"
            "1 - Done ✅\n"
            "0 - Menu"
        ),
    },
    "medicine_all_taken": {
        "telugu": "✅ Baagundi! Mandulu time ki teesukunnaru. 👍",
        "english": "✅ Great! You took all your medicines on time. 👍",
        "both": "✅ Baagundi! Great! Mandulu time ki teesukunnaru. 👍",
    },
    "medicine_missed": {
        "telugu": "⚠️ Okavela miss aithey, doctor ni adagandi. Tondara ga teesukundi.",
        "english": "⚠️ If you missed any, please take them soon or consult your doctor.",
        "both": "⚠️ Miss aithey tondara teesukundi / Take missed medicines soon.",
    },
    "medicine_not_yet": {
        "telugu": "⏰ Marchipokandi! Mandulu teesukundi. Meeku gurthu chestha.",
        "english": "⏰ Don't forget! Please take your medicines. I'll remind you again.",
        "both": "⏰ Marchipokandi! Don't forget your medicines!",
    },
    "no_medicines": {
        "telugu": "📋 Mee mandula list khaali ga undi. Family member ni add cheyamani cheppandi.",
        "english": "📋 No medicines added yet. Ask your family member to add them on the dashboard.",
        "both": "📋 Mandulu add avvaledu / No medicines added yet.",
    },

    # --- Health Check-in ---
    "checkin_feeling": {
        "telugu": (
            "🩺 *Aarogya Check-in*\n\n"
            "Ee roju meeru ela unnaru?\n"
            "1 - Baagunnanu 😊\n"
            "2 - Parvaaledu 😐\n"
            "3 - Baaledu 😟"
        ),
        "english": (
            "🩺 *Health Check-in*\n\n"
            "How are you feeling today?\n"
            "1 - Good 😊\n"
            "2 - Okay 😐\n"
            "3 - Not well 😟"
        ),
        "both": (
            "🩺 *Aarogya Check-in / Health Check-in*\n\n"
            "Ee roju ela unnaru? / How are you today?\n"
            "1 - Baagunnanu / Good 😊\n"
            "2 - Parvaaledu / Okay 😐\n"
            "3 - Baaledu / Not well 😟"
        ),
    },
    "checkin_good": {
        "telugu": "😊 Chaalaa baagundi! Meeru aarogyam ga undatam chaalaa santosham.",
        "english": "😊 Wonderful! Glad to hear you're doing well.",
        "both": "😊 Baagundi! Wonderful! Stay healthy!",
    },
    "checkin_ok": {
        "telugu": "😐 Parvaaledu. Neerlu taagandi, rest teesukundi.",
        "english": "😐 Take care. Stay hydrated and rest well.",
        "both": "😐 Take care! Neerlu taagandi, rest teesukundi.",
    },
    "checkin_bad_symptoms": {
        "telugu": (
            "😟 Enduku baaledu? Emi problem?\n"
            "1 - Tala noppi (Headache)\n"
            "2 - Kallu tirugutunnaayi (Dizziness)\n"
            "3 - Oopiri aadatam ledu (Breathing)\n"
            "4 - Sandhu noppulu (Joint pain)\n"
            "5 - Kallu manchiga kanipinchatam ledu (Vision)\n"
            "6 - Verey (Other)"
        ),
        "english": (
            "😟 Sorry to hear that. What's bothering you?\n"
            "1 - Headache\n"
            "2 - Dizziness\n"
            "3 - Breathing difficulty\n"
            "4 - Joint pain\n"
            "5 - Vision problems\n"
            "6 - Other"
        ),
        "both": (
            "😟 Emi problem? / What's bothering you?\n"
            "1 - Tala noppi / Headache\n"
            "2 - Kallu tirugutunnaayi / Dizziness\n"
            "3 - Oopiri problem / Breathing difficulty\n"
            "4 - Sandhu noppulu / Joint pain\n"
            "5 - Kallu problem / Vision problems\n"
            "6 - Verey / Other"
        ),
    },
    "checkin_symptom_recorded": {
        "telugu": "📝 Record chesaamu. Jagrathaga undandi. Family ki telusu chesaamu.",
        "english": "📝 Recorded. Please take care. We've notified your family.",
        "both": "📝 Recorded. Family ki alert pampamu / Family has been notified.",
    },
    "checkin_severe_alert": {
        "telugu": "🚨 *Jagratha!* Mee paristhiti family ki urgently cheppamu. Doctor ki chupinchandi.",
        "english": "🚨 *Alert!* We've urgently notified your family. Please see a doctor.",
        "both": "🚨 Urgent alert! Family ki telusu chesaamu / Family notified urgently!",
    },

    # --- Exercise ---
    "exercise_menu": {
        "telugu": (
            "🧘 *Vyaayaamam Menu*\n\n"
            "1 - Chair Yoga (Kurchi Yoga)\n"
            "2 - Walking Tips (Nadaka)\n"
            "3 - Pranayama (Breathing)\n"
            "4 - Eye Exercises (Kallu Vyaayaamam)"
        ),
        "english": (
            "🧘 *Exercise Menu*\n\n"
            "1 - Chair Yoga\n"
            "2 - Walking Tips\n"
            "3 - Pranayama (Breathing)\n"
            "4 - Eye Exercises"
        ),
        "both": (
            "🧘 *Vyaayaamam / Exercise Menu*\n\n"
            "1 - Chair Yoga (Kurchi Yoga)\n"
            "2 - Walking Tips (Nadaka)\n"
            "3 - Pranayama (Breathing)\n"
            "4 - Eye Exercises (Kallu Vyaayaamam)"
        ),
    },
    "exercise_chair_yoga": {
        "telugu": (
            "🪑 *Kurchi Yoga (Chair Yoga)*\n\n"
            "1️⃣ Kurchi lo straight ga kurchundi\n"
            "2️⃣ Rendu chethulu paina ettandi - 5 seconds\n"
            "3️⃣ Mellaga right ki tirugandi - 5 seconds\n"
            "4️⃣ Left ki tirugandi - 5 seconds\n"
            "5️⃣ Mundu ki vangandi, kaalu touch cheyandi\n"
            "6️⃣ 5 saarlu repeat cheyandi\n\n"
            "⚠️ Noppi vasthey aapandi. Mellaga cheyandi."
        ),
        "english": (
            "🪑 *Chair Yoga*\n\n"
            "1️⃣ Sit straight in a chair\n"
            "2️⃣ Raise both hands up - hold 5 seconds\n"
            "3️⃣ Slowly twist right - hold 5 seconds\n"
            "4️⃣ Twist left - hold 5 seconds\n"
            "5️⃣ Bend forward, try to touch your toes\n"
            "6️⃣ Repeat 5 times\n\n"
            "⚠️ Stop if you feel pain. Go slowly."
        ),
        "both": (
            "🪑 *Kurchi Yoga / Chair Yoga*\n\n"
            "1️⃣ Kurchi lo straight kurchundi / Sit straight\n"
            "2️⃣ Chethulu paina / Raise hands up - 5 sec\n"
            "3️⃣ Right ki tirugandi / Twist right - 5 sec\n"
            "4️⃣ Left ki tirugandi / Twist left - 5 sec\n"
            "5️⃣ Mundu ki vangandi / Bend forward\n"
            "6️⃣ 5 saarlu repeat / Repeat 5 times\n\n"
            "⚠️ Noppi vasthey aapandi / Stop if pain."
        ),
    },
    "exercise_walking": {
        "telugu": (
            "🚶 *Nadaka Tips (Walking)*\n\n"
            "1️⃣ Rojuu 20-30 nimishaalu nadavandi\n"
            "2️⃣ Poddu leda saayanthram time best\n"
            "3️⃣ Comfortable shoes vesukundi\n"
            "4️⃣ Neellu bottle teesukundi\n"
            "5️⃣ Mellaga start chesi speed perugandi\n\n"
            "💧 Nadaka mundhu, tarvatha neellu taagandi."
        ),
        "english": (
            "🚶 *Walking Tips*\n\n"
            "1️⃣ Walk 20-30 minutes daily\n"
            "2️⃣ Morning or evening is best\n"
            "3️⃣ Wear comfortable shoes\n"
            "4️⃣ Carry a water bottle\n"
            "5️⃣ Start slow, gradually increase speed\n\n"
            "💧 Drink water before and after walking."
        ),
        "both": (
            "🚶 *Nadaka / Walking Tips*\n\n"
            "1️⃣ Rojuu 20-30 min nadavandi / Walk daily\n"
            "2️⃣ Poddu/saayanthram best / Morning/evening\n"
            "3️⃣ Comfortable shoes vesukundi / Wear good shoes\n"
            "4️⃣ Neellu bottle / Carry water\n"
            "5️⃣ Mellaga start / Start slow\n\n"
            "💧 Neellu taagandi / Stay hydrated."
        ),
    },
    "exercise_pranayama": {
        "telugu": (
            "🫁 *Pranayama (Breathing)*\n\n"
            "*Anulom Vilom:*\n"
            "1️⃣ Sukham ga kurchundi\n"
            "2️⃣ Right mukku muyandi, left tho peelaandi\n"
            "3️⃣ Left mukku muyandi, right tho vadalandi\n"
            "4️⃣ 10 saarlu repeat cheyandi\n\n"
            "*Deep Breathing:*\n"
            "1️⃣ Lota ga peelaandi - 4 seconds\n"
            "2️⃣ Aapandi - 4 seconds\n"
            "3️⃣ Mellaga vadalandi - 6 seconds\n"
            "4️⃣ 10 saarlu cheyandi"
        ),
        "english": (
            "🫁 *Pranayama (Breathing)*\n\n"
            "*Anulom Vilom:*\n"
            "1️⃣ Sit comfortably\n"
            "2️⃣ Close right nostril, breathe in through left\n"
            "3️⃣ Close left nostril, breathe out through right\n"
            "4️⃣ Repeat 10 times\n\n"
            "*Deep Breathing:*\n"
            "1️⃣ Breathe in deeply - 4 seconds\n"
            "2️⃣ Hold - 4 seconds\n"
            "3️⃣ Breathe out slowly - 6 seconds\n"
            "4️⃣ Repeat 10 times"
        ),
        "both": (
            "🫁 *Pranayama / Breathing*\n\n"
            "*Anulom Vilom:*\n"
            "1️⃣ Sukham ga kurchundi / Sit comfortably\n"
            "2️⃣ Right mukku muyandi / Close right nostril\n"
            "3️⃣ Left tho breathe in, switch\n"
            "4️⃣ 10 saarlu / 10 times\n\n"
            "*Deep Breathing:*\n"
            "Breathe in 4s → Hold 4s → Out 6s → 10 times"
        ),
    },
    "exercise_eyes": {
        "telugu": (
            "👁️ *Kallu Vyaayaamam (Eye Exercises)*\n\n"
            "1️⃣ Kallu gadiga muyandi - 5 seconds\n"
            "2️⃣ Tharvatha baga theravandi\n"
            "3️⃣ Paina, kinda, left, right choodandi\n"
            "4️⃣ Golaalu tirugandi (clockwise)\n"
            "5️⃣ Doggara finger petti focus cheyandi\n"
            "6️⃣ Kallu meedha venniti neellu challa cheyandi\n\n"
            "📱 Phone/TV takkuva choodandi."
        ),
        "english": (
            "👁️ *Eye Exercises*\n\n"
            "1️⃣ Close eyes tightly - 5 seconds\n"
            "2️⃣ Open wide\n"
            "3️⃣ Look up, down, left, right\n"
            "4️⃣ Roll eyes clockwise\n"
            "5️⃣ Focus on a finger close, then far\n"
            "6️⃣ Splash cool water on eyes\n\n"
            "📱 Reduce screen time."
        ),
        "both": (
            "👁️ *Kallu Vyaayaamam / Eye Exercises*\n\n"
            "1️⃣ Kallu muyandi / Close eyes - 5 sec\n"
            "2️⃣ Baga theravandi / Open wide\n"
            "3️⃣ Paina, kinda, left, right / Look all sides\n"
            "4️⃣ Golaalu / Roll clockwise\n"
            "5️⃣ Focus near then far\n"
            "6️⃣ Cool water on eyes\n\n"
            "📱 Screen time takkuva / Reduce screen time."
        ),
    },

    # --- Emergency ---
    "emergency_info": {
        "telugu": (
            "🚨 *Apathkaala Numbers*\n\n"
            "🚑 108 - Ambulance\n"
            "🏥 104 - Health Helpline\n"
            "👮 100 - Police\n"
            "🔥 101 - Fire\n"
            "{family_contact}\n\n"
            "1 - SOS Alert pampu (Family ki message)\n"
            "0 - Menu ki vellandi"
        ),
        "english": (
            "🚨 *Emergency Numbers*\n\n"
            "🚑 108 - Ambulance\n"
            "🏥 104 - Health Helpline\n"
            "👮 100 - Police\n"
            "🔥 101 - Fire\n"
            "{family_contact}\n\n"
            "1 - Send SOS Alert to family\n"
            "0 - Back to menu"
        ),
        "both": (
            "🚨 *Emergency Numbers / Apathkaala Numbers*\n\n"
            "🚑 108 - Ambulance\n"
            "🏥 104 - Health Helpline\n"
            "👮 100 - Police\n"
            "🔥 101 - Fire\n"
            "{family_contact}\n\n"
            "1 - SOS Alert pampu / Send SOS\n"
            "0 - Menu / Back to menu"
        ),
    },
    "sos_sent": {
        "telugu": "🆘 *SOS Alert pampamu!* Mee family ki message vellindi. Dhairyam ga undandi.",
        "english": "🆘 *SOS Alert sent!* Your family has been notified. Stay calm and safe.",
        "both": "🆘 SOS Alert sent! Family ki message pampamu. Stay safe!",
    },

    # --- Language Change ---
    "language_change": {
        "telugu": (
            "Bhaasha eenchukundi:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both"
        ),
        "english": (
            "Choose your language:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both"
        ),
        "both": (
            "Bhaasha eenchukundi / Choose language:\n"
            "1 - తెలుగు (Telugu)\n"
            "2 - English\n"
            "3 - Both"
        ),
    },
    "language_changed": {
        "telugu": "✅ Bhaasha Telugu ki maarchamu.",
        "english": "✅ Language changed to English.",
        "both": "✅ Language set to Telugu + English.",
    },

    # --- Reminders ---
    "morning_greeting": {
        "telugu": "🌅 Shubhodayam, {name} gaaru! Ee roju kuda aarogyam ga undandi.",
        "english": "🌅 Good morning, {name}! Wishing you a healthy day.",
        "both": "🌅 Shubhodayam, {name} gaaru! Good morning! Have a healthy day.",
    },
    "medicine_reminder": {
        "telugu": "💊 {name} gaaru, {time_slot} mandulu time ayyindi! Mandulu teesukundi.",
        "english": "💊 {name}, it's time for your {time_slot} medicines! Please take them.",
        "both": "💊 {name} gaaru, {time_slot} mandulu time! Take your medicines.",
    },
    "hydration_reminder": {
        "telugu": "💧 {name} gaaru, neellu taagandi! Rojuku 8 glasses taagandi.",
        "english": "💧 {name}, drink water! Aim for 8 glasses a day.",
        "both": "💧 {name} gaaru, neellu taagandi! Drink water!",
    },
    "exercise_reminder": {
        "telugu": "🧘 {name} gaaru, saayanthram vyaayaamam time! Menu lo 4 press cheyandi.",
        "english": "🧘 {name}, it's time for your evening exercise! Press 4 for exercise menu.",
        "both": "🧘 {name} gaaru, exercise time! Press 4 for options.",
    },
    "night_checkin_reminder": {
        "telugu": "🌙 {name} gaaru, ee roju meeru ela unnaru? 3 press chesi cheppandi.",
        "english": "🌙 {name}, how was your day? Press 3 for health check-in.",
        "both": "🌙 {name} gaaru, ee roju ela unnaru? Press 3 for check-in.",
    },

    # --- General ---
    "invalid_input": {
        "telugu": "❓ Ardham kaaledu. Dayachesi number type cheyandi. Menu ki 0 press cheyandi.",
        "english": "❓ I didn't understand. Please type a number. Press 0 for menu.",
        "both": "❓ Ardham kaaledu / Didn't understand. Type a number. Press 0 for menu.",
    },
    "back_to_menu": {
        "telugu": "👆 Menu ki velthunnamu...",
        "english": "👆 Going back to menu...",
        "both": "👆 Menu ki / Back to menu...",
    },
}


def get_message(key: str, language: str = "both", **kwargs) -> str:
    """Get a translated message by key and language."""
    lang = language if language in ("telugu", "english", "both") else "both"
    msg = MESSAGES.get(key, {}).get(lang, MESSAGES.get(key, {}).get("both", ""))
    if kwargs:
        msg = msg.format(**kwargs)
    return msg
