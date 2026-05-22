# ═══════════════════════════════════════════════════════════════
#   📚 Abdulla Qahhor Educational Telegram Bot
#   Author   : University Project
#   Library  : pyTelegramBotAPI (telebot)
#   Languages: Uzbek (Latin) | English | Russian
# ═══════════════════════════════════════════════════════════════

import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# ── Bot Token ────────────────────────────────────────────────────
BOT_TOKEN = "7731967991:AAH8pHPjpu6NCcwK6xIlHiBG68CfAbzxq0Y"
bot = telebot.TeleBot(BOT_TOKEN)

# ── User session storage (language + quiz state) ─────────────────
user_data = {}


# ════════════════════════════════════════════════════════════════
#  MULTILINGUAL CONTENT DATABASE
# ════════════════════════════════════════════════════════════════

TEXTS = {

    # ── UZBEK ────────────────────────────────────────────────────
    "uz": {
        "welcome": (
            "📚 *Abdulla Qahhor Ta'lim Botiga Xush Kelibsiz!*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🇺🇿 O'zbek adabiyotining ulug' namoyandasi\n"
            "*Abdulla Qahhor* (1907–1968) haqida\n"
            "interaktiv ma'lumotlar bazasiga xush kelibsiz!\n\n"
            "📖 _\"O'qish — bilim manbai, bilim — kuch manbai.\"_\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Quyidan tilni tanlang 👇"
        ),
        "lang_chosen": "✅ *O'zbek tili* tanlandi!\n\nAsosiy menyu ochilmoqda... 🎯",
        "main_menu": (
            "🏠 *Asosiy Menyu*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 *Abdulla Qahhor* haqida nimani o'rganmoqchisiz?\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Quyidagi bo'limlardan birini tanlang 👇"
        ),
        "buttons": {
            "bio": "📖 Hayoti",
            "creativity": "✍️ Ijodi",
            "works": "📚 Asarlari",
            "poems": "📝 She'rlari",
            "facts": "🎯 Qiziqarli faktlar",
            "quiz": "🧠 Quiz Test",
            "lang": "🌐 Tilni almashtirish",
            "back": "⬅️ Orqaga",
        },

        "bio": (
            "📖 *ABDULLA QAHHORNING HAYOTI*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👶 *Tug'ilgan sana:* 17 sentyabr 1907-yil\n"
            "📍 *Tug'ilgan joy:* Qo'qon, Farg'ona viloyati\n"
            "💼 *Kasbi:* Yozuvchi, shoir, dramaturg, tarjimon\n"
            "📅 *Vafot etgan:* 24 may 1968-yil, Moskva\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎓 *Ta'lim yo'li:*\n"
            "• 1922–1924 — Qo'qondagi pedagogika texnikumi\n"
            "• 1926 — Samarqand davlat universitetini tayyorlov kursi\n"
            "• 1930 — O'rta Osiyo Davlat Universiteti (pedagogika)\n"
            "• 1933–1935 — Toshkentdagi Til va Adabiyot instituti aspiranturasi\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🖊️ *Ijodiy faoliyati:*\n"
            "• 1924-yildan boshlab matbuotda she'r va hikoyalar yozdi\n"
            "• Ko'plab taxalluslar ostida ijod qildi: _Nish, Mavlono Kufur, Erkaboy_\n"
            "• 1934–1937 — «Sovet adabiyoti» jurnali kotibi\n"
            "• 1938–1950 — O'zbekiston Davlat Nashriyotida muharrir\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 *Mukofotlari:*\n"
            "• 🥇 Stalin mukofoti (1952)\n"
            "• 🏅 Hamza nomidagi Davlat mukofoti (1966)\n"
            "• 🎖️ O'zSSR Xalq yozuvchisi (1967)\n"
            "• 🌟 «Buyuk xizmatlari uchun» ordeni (2000, o'limidan keyin)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *Qiziqarli fakt:*\n"
            "_Abdulla Qahhor «O'zbeklar Chexovi» deb atalgan —\n"
            "uning hikoyachiligi rus yozuvchisi Anton Chexov uslubiga\n"
            "o'xshatilgan._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "creativity": (
            "✍️ *ABDULLA QAHHORNING IJODI*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎨 *Adabiy yo'nalishi:* Realizm\n\n"
            "📌 *Ijodining asosiy xususiyatlari:*\n"
            "• 🔍 Insoniy xarakter va ruhiyatni chuqur tahlil qilish\n"
            "• 🗡️ Ijtimoiy tengsizlik va zulmni keskin tanqid etish\n"
            "• 💬 Oddiy va ta'sirchan til — har bir so'z o'z o'rnida\n"
            "• 😂 Nozik yumor va hajv — satirik asarlarida yaqqol ko'rinadi\n"
            "• 🌍 O'zbek hayoti va turmushini real tasvirlash\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 *Janrlar:*\n"
            "• 📖 Roman va qissa\n"
            "• 📝 Hikoya (eng kuchli janri)\n"
            "• 🎭 Pyesa va dramaturgiya\n"
            "• ✍️ She'riyat\n"
            "• 🔄 Adabiy tarjima\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🌟 *O'zbek adabiyotiga hissasi:*\n"
            "Abdulla Qahhor XX asr o'zbek nasrining asoschisi sifatida\n"
            "tan olingan. U o'zbek qisqa hikoyachiligini jahon darajasiga\n"
            "olib chiqdi. Uning asarlarida Chexovga xos ixchamlik va\n"
            "chuqurlik uyg'unlashgan.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🔤 *Tarjima faoliyati:*\n"
            "Rus adabiyotining buyuk namoyandalarini o'zbek tiliga tarjima qildi:\n"
            "• Pushkin — «Kapitanning qizi»\n"
            "• Gogol — «Uylanish», «Revizor»\n"
            "• Tolstoy — «Urush va tinchlik» (xotini bilan birgalikda)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "works_menu": (
            "📚 *ABDULLA QAHHORNING ASARLARI*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Qaysi tur asarlarni ko'rishni xohlaysiz? 👇"
        ),
        "works_buttons": {
            "novels": "📗 Romanlar",
            "stories": "📘 Hikoyalar",
            "plays": "🎭 Pyesalar",
            "back": "⬅️ Orqaga",
        },
        "novels": (
            "📗 *ROMANLAR VA QISSALAR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📖 *1. Sarob (Miraj) — 1943*\n"
            "   _O'z davrining murakkab ijtimoiy muammolarini\n"
            "   aks ettiruvchi birinchi romani._\n\n"
            "📖 *2. Qo'shchinor chiroqlari — 1951*\n"
            "   _Kolxoz qurilishi davridagi o'zbek qishlog'i hayotini\n"
            "   tasvirlovchi eng mashhur romani.\n"
            "   Stalin mukofotiga sazovor bo'lgan._\n\n"
            "📖 *3. Sinchalak — 1958*\n"
            "   _Insoniy munosabatlar va his-tuyg'ularni\n"
            "   kuchli psixologik tahlil orqali yorituvchi qissa._\n\n"
            "📖 *4. O'tmishdan ertaklar — 1965*\n"
            "   _Adabiy avtobiografiya: yozuvchining\n"
            "   xotiralari va hayot kuzatishlari._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "stories": (
            "📘 *MASHHUR HIKOYALAR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🌿 *Anor* — Qashshoqlik va umid haqida teran hikoya\n\n"
            "🎭 *O'g'ri* — Ijtimoiy tanqid, yumor va fojia qorishiq asar\n\n"
            "😔 *Bemor* — Oddiy inson qalbini nozik tahlil etuvchi hikoya\n\n"
            "🌺 *Mayiz yemagan xotin* — Ayol qismatiga bag'ishlangan\n\n"
            "👒 *Dahshat* — Qo'rquv psixologiyasini yorituvchi kuchli asar\n\n"
            "📚 *Adabiyot muallimi* — Ma'rifat va mas'uliyat haqida\n\n"
            "🕯️ *To'yda aza* — Hayot ziddiyatlarini yumor bilan tasvir\n\n"
            "⚔️ *Asror bobo* — Urush yillarida Vatanparvarlik haqida\n\n"
            "🌙 *Boshsiz odam (1929)* — Birinchi mashhur hikoyasi\n\n"
            "🏘️ *Mahalla* — Mahalla hayotini jonli tasvirlagan asar\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "plays": (
            "🎭 *PYESALAR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎪 *Shohi so'zana (1950)*\n"
            "   _O'zbek milliy madaniyatini ulug'lovchi drama._\n\n"
            "🦷 *Og'riq tishlar (1950)*\n"
            "   _Satirik komediya — jamiyatdagi illatlarni\n"
            "   hajv orqali fosh etuvchi eng sevimli pyesasi._\n\n"
            "⚰️ *Tobutdan tovush (1962)*\n"
            "   _Falsafiy drama — hayot va o'lim mavzusida._\n\n"
            "👩‍👩‍👧 *Ayajonlarim (1967)*\n"
            "   _Ona muhabbati va insoniy qadriyatlar haqida\n"
            "   so'nggi yillarda yozilgan pyesa._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "poems_list": [
            (
                "📝 *SHE'R №1: «Ona»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Ona — nur, ona — hayot,\n"
                "Ona — quvvat, ona — qanot.\n"
                "Uning ko'zi — tong yulduzi,\n"
                "Uning so'zi — yurak so'zi._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *SHE'R №2: «Vatan»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Bu yerda har tosh — tarix,\n"
                "Har daraxt — aziz yodgor.\n"
                "Bu yurtning havosi — iqlim,\n"
                "Bu yerda inson — baxtiyor._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *SHE'R №3: «Kitob»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Kitob — do'st, kitob — ustozing,\n"
                "Kitob — hayot sirlarining kaliti.\n"
                "Har sahifada bir olam,\n"
                "Har so'zda cheksiz ma'no yashirin._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *SHE'R №4: «Oy kuyganda» (1924)*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Birinchi she'rim — 1924-yil,\n"
                "«Mushtum» jurnalida bosilib chiqqan.\n"
                "Yosh qalbning ilk qo'shig'i —\n"
                "Hayotga sevgi bilan yozilgan._\n\n"
                "✍️ _Abdulla Qahhor (Birinchi she'ri haqida)_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
        ],

        "facts_list": [
            "🎯 *QIZIQARLI FAKT #1*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nAbdulla Qahhor «O'zbeklar Chexovi» deb atalmish. Uning hikoyalari Anton Chexovning ixchamlik va chuqurlik uslubiga juda yaqin.",
            "🎯 *QIZIQARLI FAKT #2*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nYozuvchi o'ndan ortiq taxallus ostida ijod qilgan: Nish, Mavlono Kufur, Erkaboy, Gulyor, Norin Shilpiq va boshqalar.",
            "🎯 *QIZIQARLI FAKT #3*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nU xotini Kibriyo Qahhorova bilan birgalikda Lev Tolstoyning «Urush va tinchlik» asarini o'zbek tiliga tarjima qilgan — bu o'zbek tarjimachiligining eng buyuk loyihalaridan biri.",
            "🎯 *QIZIQARLI FAKT #4*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nUning birinchi she'ri «Oy kuyganda» 1924-yilda «Mushtum» jurnalining 8-sonida e'lon qilingan. Shundan so'ng u asosan nasrga o'tgan.",
            "🎯 *QIZIQARLI FAKT #5*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n1952-yilgi Stalin mukofoti unga «Qo'shchinor chiroqlari» romani uchun berilgan — bu o'sha davrdagi eng nufuzli adabiy mukofot edi.",
            "🎯 *QIZIQARLI FAKT #6*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nAbdulla Qahhor xalq og'zaki ijodini chuqur o'rgangan va bu manbadan ijodida keng foydalangan. Folklor unsurlari uning hikoyalarini boyitgan.",
            "🎯 *QIZIQARLI FAKT #7*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nU Pushkin, Chexov, Gogol, Tolstoy kabi rus adabiyotining klassiklar asarlarini o'zbek tiliga tarjima qilib, ikki madaniyat o'rtasida ko'prik bo'ldi.",
        ],

        "quiz_start": "🧠 *QUIZ TEST BOSHLANDI!*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nAbdulla Qahhor haqida 5 ta savol. Har bir to'g'ri javob uchun 1 ball!\n\nTayyor bo'lsangiz boshlaymiz... 🚀",
        "quiz_question": "❓ *Savol {num}/5:*\n\n{question}",
        "quiz_correct": "✅ *To'g'ri!* Ajoyib! +1 ball",
        "quiz_wrong": "❌ *Noto'g'ri!* To'g'ri javob: *{answer}*",
        "quiz_result": (
            "🏁 *QUIZ YAKUNLANDI!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 *Natijangiz: {score}/5*\n"
            "📈 *Foiz: {percent}%*\n\n"
            "{message}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "_📚 Abdulla Qahhor Educational Bot_"
        ),
        "quiz_messages": {
            5: "🌟 *MUKAMMAL!* Siz Abdulla Qahhor haqida hamma narsani bilasiz! Barakalla!",
            4: "🎉 *AJOYIB!* Zo'r natija! Bilimingiz yuqori darajada!",
            3: "👍 *YAXSHI!* O'rtacha natija. Yana o'rganing!",
            2: "💪 *HARAKAT QILING!* Ko'proq o'qish kerak!",
            1: "📖 *O'QING!* Abdulla Qahhor haqida ko'proq bilib oling!",
            0: "🔄 *QAYTA URINING!* Hech qo'rqmang, o'qib qayta sinab ko'ring!",
        },
    },

    # ── ENGLISH ──────────────────────────────────────────────────
    "en": {
        "welcome": (
            "📚 *Welcome to the Abdulla Qahhor Educational Bot!*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🇺🇿 Explore the life and legacy of\n"
            "*Abdulla Qahhor* (1907–1968)\n"
            "the greatest Uzbek writer of the 20th century!\n\n"
            "📖 _\"Reading is the source of knowledge,\n"
            "knowledge is the source of power.\"_\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Please choose your language below 👇"
        ),
        "lang_chosen": "✅ *English* language selected!\n\nOpening main menu... 🎯",
        "main_menu": (
            "🏠 *Main Menu*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 What would you like to learn about\n"
            "*Abdulla Qahhor*?\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Select a section below 👇"
        ),
        "buttons": {
            "bio": "📖 Biography",
            "creativity": "✍️ Creativity",
            "works": "📚 Works",
            "poems": "📝 Poems",
            "facts": "🎯 Interesting Facts",
            "quiz": "🧠 Quiz Test",
            "lang": "🌐 Change Language",
            "back": "⬅️ Back",
        },

        "bio": (
            "📖 *BIOGRAPHY OF ABDULLA QAHHOR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👶 *Born:* September 17, 1907\n"
            "📍 *Birthplace:* Kokand, Fergana Oblast\n"
            "💼 *Occupation:* Novelist, Poet, Playwright, Translator\n"
            "📅 *Died:* May 24, 1968, Moscow\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎓 *Education:*\n"
            "• 1922–1924 — Pedagogy Technical School, Kokand\n"
            "• 1926 — Preparatory program, Samarkand State University\n"
            "• 1930 — Graduated from Central Asian State University (Pedagogy)\n"
            "• 1933–1935 — Graduate studies, Institute of Language & Literature, Tashkent\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🖊️ *Career Highlights:*\n"
            "• Started writing in 1924 under various pen names\n"
            "• Pen names: _Nish, Mavlono Kufur, Erkaboy, Gulyor_\n"
            "• 1934–1937 — Secretary of «Soviet Literature» magazine\n"
            "• 1938–1950 — Editor at State Publishing House of Uzbekistan\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 *Awards & Recognition:*\n"
            "• 🥇 Stalin Prize (1952)\n"
            "• 🏅 State Hamza Prize (1966)\n"
            "• 🎖️ People's Writer of the Uzbek SSR (1967)\n"
            "• 🌟 Order of Outstanding Merit (2000, posthumous)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *Notable Fact:*\n"
            "_Abdulla Qahhor is often called the «Chekhov of Uzbeks»\n"
            "because his storytelling style closely resembles\n"
            "the great Russian writer Anton Chekhov._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "creativity": (
            "✍️ *CREATIVITY OF ABDULLA QAHHOR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎨 *Literary Movement:* Realism\n\n"
            "📌 *Key Features of His Writing:*\n"
            "• 🔍 Deep psychological analysis of human character\n"
            "• 🗡️ Sharp criticism of social inequality and oppression\n"
            "• 💬 Simple yet powerful language — every word matters\n"
            "• 😂 Subtle humor and satire woven into serious themes\n"
            "• 🌍 Authentic portrayal of Uzbek life and society\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 *Genres He Mastered:*\n"
            "• 📖 Novel and novella\n"
            "• 📝 Short story (his strongest genre)\n"
            "• 🎭 Drama and playwriting\n"
            "• ✍️ Poetry\n"
            "• 🔄 Literary translation\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🌟 *Contribution to Uzbek Literature:*\n"
            "Qahhor is recognized as one of the founding fathers\n"
            "of modern Uzbek prose. He elevated Uzbek short fiction\n"
            "to world-class standards, combining Chekhov-like\n"
            "brevity with profound depth.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🔤 *Translation Work:*\n"
            "He brought Russian literary giants to Uzbek readers:\n"
            "• Pushkin — «The Captain's Daughter»\n"
            "• Gogol — «Marriage», «The Government Inspector»\n"
            "• Tolstoy — «War and Peace» (with his wife)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "works_menu": (
            "📚 *WORKS OF ABDULLA QAHHOR*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Which type of works would you like to explore? 👇"
        ),
        "works_buttons": {
            "novels": "📗 Novels",
            "stories": "📘 Short Stories",
            "plays": "🎭 Plays",
            "back": "⬅️ Back",
        },
        "novels": (
            "📗 *NOVELS & NOVELLAS*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📖 *1. Sarob (Mirage) — 1943*\n"
            "   _His debut novel reflecting the complex\n"
            "   social issues of the Soviet era._\n\n"
            "📖 *2. The Lights of Qo'shchinor — 1951*\n"
            "   _His most famous novel depicting life in\n"
            "   an Uzbek collective farm during Soviet times.\n"
            "   Winner of the Stalin Prize._\n\n"
            "📖 *3. Sinchalak — 1958*\n"
            "   _A psychologically rich novella exploring\n"
            "   human relationships and emotions._\n\n"
            "📖 *4. Tales from the Past — 1965*\n"
            "   _Literary autobiography — memoirs and\n"
            "   observations from his life._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "stories": (
            "📘 *FAMOUS SHORT STORIES*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🌿 *Anor (Pomegranate)* — A profound story about poverty and hope\n\n"
            "🎭 *O'g'ri (The Thief)* — Social criticism, humor and tragedy combined\n\n"
            "😔 *Bemor (The Sick)* — Subtle analysis of the ordinary human soul\n\n"
            "🌺 *The Woman Who Never Ate Raisins* — Dedicated to women's fate\n\n"
            "👒 *Dahshat (Horror)* — A powerful exploration of fear psychology\n\n"
            "📚 *The Literature Teacher* — About enlightenment and responsibility\n\n"
            "🕯️ *To'yda aza (Funeral at a Wedding)* — Life's contradictions through humor\n\n"
            "⚔️ *Asror Bobo* — Patriotism during the wartime years\n\n"
            "🌙 *Boshsiz odam (1929)* — His first acclaimed short story\n\n"
            "🏘️ *Mahalla* — A vivid portrayal of neighborhood life\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "plays": (
            "🎭 *PLAYS & DRAMA*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎪 *Shohi So'zana / Silk Suzani (1950)*\n"
            "   _A drama celebrating Uzbek national culture._\n\n"
            "🦷 *Og'riq Tishlar / Hurting Teeth (1950)*\n"
            "   _A satirical comedy — his most beloved play,\n"
            "   exposing social flaws through sharp humor._\n\n"
            "⚰️ *Tobutdan Tovush / A Sound from the Coffin (1962)*\n"
            "   _A philosophical drama on the themes\n"
            "   of life, death, and human nature._\n\n"
            "👩‍👩‍👧 *Ayajonlarim / My Dear Mothers (1967)*\n"
            "   _Written in his final years — a tender\n"
            "   exploration of maternal love and human values._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "poems_list": [
            (
                "📝 *POEM #1: «Mother»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Mother — light, mother — life,\n"
                "Mother — strength, mother — wings.\n"
                "Her eyes — the morning star,\n"
                "Her words — the words of the heart._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *POEM #2: «Homeland»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Every stone here — is history,\n"
                "Every tree — a cherished memory.\n"
                "The air of this land — its own climate,\n"
                "Here a person — lives in happiness._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *POEM #3: «The Book»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_A book — your friend, your teacher,\n"
                "The key to life's deepest secrets.\n"
                "In every page — a universe,\n"
                "In every word — infinite meaning hidden._\n\n"
                "✍️ _Abdulla Qahhor_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *POEM #4: «When the Moon Burns» (1924)*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_My first poem — year of 1924,\n"
                "Published in the Mushtum journal.\n"
                "The first song of a young heart —\n"
                "Written with love for life._\n\n"
                "✍️ _Abdulla Qahhor (About his first poem)_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
        ],

        "facts_list": [
            "🎯 *INTERESTING FACT #1*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nAbdulla Qahhor is nicknamed the «Chekhov of Uzbeks». His short stories share the same conciseness and psychological depth as those of the great Russian writer Anton Chekhov.",
            "🎯 *INTERESTING FACT #2*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nQahhor wrote under more than 10 different pen names throughout his career: Nish, Mavlono Kufur, Erkaboy, Gulyor, Norin Shilpiq, and several others.",
            "🎯 *INTERESTING FACT #3*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nTogether with his wife Kibriyo Qahhorova, he translated Leo Tolstoy's monumental «War and Peace» into the Uzbek language — considered one of the greatest translation achievements in Uzbek literary history.",
            "🎯 *INTERESTING FACT #4*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nHis very first poem «When the Moon Burns» was published in 1924 in the 8th issue of the «Mushtum» (Fist) satirical magazine. After this, he shifted his focus primarily to prose.",
            "🎯 *INTERESTING FACT #5*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nThe 1952 Stalin Prize was awarded to him for his novel «The Lights of Qo'shchinor» — the most prestigious literary prize of that Soviet era.",
            "🎯 *INTERESTING FACT #6*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nQahhor deeply studied Uzbek oral folklore and incorporated folk elements into his writing, enriching his stories with the authentic voice of his people.",
            "🎯 *INTERESTING FACT #7*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nBy translating Pushkin, Chekhov, Gogol, and Tolstoy into Uzbek, Qahhor built a cultural bridge between Russian and Uzbek literary traditions.",
        ],

        "quiz_start": "🧠 *QUIZ TEST STARTED!*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n5 questions about Abdulla Qahhor. Each correct answer = 1 point!\n\nReady? Let's go! 🚀",
        "quiz_question": "❓ *Question {num}/5:*\n\n{question}",
        "quiz_correct": "✅ *Correct!* Excellent! +1 point",
        "quiz_wrong": "❌ *Wrong!* The correct answer was: *{answer}*",
        "quiz_result": (
            "🏁 *QUIZ COMPLETED!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 *Your Score: {score}/5*\n"
            "📈 *Percentage: {percent}%*\n\n"
            "{message}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "_📚 Abdulla Qahhor Educational Bot_"
        ),
        "quiz_messages": {
            5: "🌟 *PERFECT!* You know everything about Abdulla Qahhor! Outstanding!",
            4: "🎉 *EXCELLENT!* Great result! Your knowledge is at a high level!",
            3: "👍 *GOOD!* Average score. Keep learning!",
            2: "💪 *KEEP TRYING!* You need to read more about him!",
            1: "📖 *READ MORE!* Learn more about Abdulla Qahhor!",
            0: "🔄 *TRY AGAIN!* Don't be discouraged — read and try again!",
        },
    },

    # ── RUSSIAN ──────────────────────────────────────────────────
    "ru": {
        "welcome": (
            "📚 *Добро пожаловать в образовательного бота об Абдулле Каххоре!*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🇺🇿 Откройте для себя жизнь и творчество\n"
            "*Абдуллы Каххора* (1907–1968) —\n"
            "величайшего узбекского писателя XX века!\n\n"
            "📖 _«Чтение — источник знаний,\n"
            "знания — источник силы.»_\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Выберите язык ниже 👇"
        ),
        "lang_chosen": "✅ Выбран *Русский* язык!\n\nОткрываю главное меню... 🎯",
        "main_menu": (
            "🏠 *Главное меню*\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 Что вы хотите узнать об\n"
            "*Абдулле Каххоре*?\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Выберите раздел ниже 👇"
        ),
        "buttons": {
            "bio": "📖 Биография",
            "creativity": "✍️ Творчество",
            "works": "📚 Произведения",
            "poems": "📝 Стихи",
            "facts": "🎯 Интересные факты",
            "quiz": "🧠 Викторина",
            "lang": "🌐 Сменить язык",
            "back": "⬅️ Назад",
        },

        "bio": (
            "📖 *БИОГРАФИЯ АБДУЛЛЫ КАХХОРА*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "👶 *Дата рождения:* 17 сентября 1907 года\n"
            "📍 *Место рождения:* Коканд, Ферганская область\n"
            "💼 *Профессия:* Прозаик, поэт, драматург, переводчик\n"
            "📅 *Скончался:* 24 мая 1968 года, Москва\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🎓 *Образование:*\n"
            "• 1922–1924 — Педагогический техникум в Коканде\n"
            "• 1926 — Подготовительный курс Самаркандского университета\n"
            "• 1930 — Окончил Среднеазиатский государственный университет (педагогика)\n"
            "• 1933–1935 — Аспирантура Института языка и литературы, Ташкент\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🖊️ *Творческая карьера:*\n"
            "• С 1924 г. публиковал стихи и рассказы под псевдонимами\n"
            "• Псевдонимы: _Ниш, Мавлоно Куфур, Эркабой, Гулёр_\n"
            "• 1934–1937 — Секретарь журнала «Советская литература»\n"
            "• 1938–1950 — Редактор Государственного издательства Узбекистана\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🏆 *Награды и признание:*\n"
            "• 🥇 Сталинская премия (1952)\n"
            "• 🏅 Государственная премия имени Хамзы (1966)\n"
            "• 🎖️ Народный писатель Узбекской ССР (1967)\n"
            "• 🌟 Орден «Буюк хизматлари учун» (2000, посмертно)\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📌 *Любопытный факт:*\n"
            "_Абдулла Каххор получил прозвище «Чехов узбеков» —\n"
            "его мастерство рассказчика сравнивали с искусством\n"
            "великого русского писателя Антона Чехова._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "creativity": (
            "✍️ *ТВОРЧЕСТВО АБДУЛЛЫ КАХХОРА*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎨 *Литературное направление:* Реализм\n\n"
            "📌 *Ключевые черты его творчества:*\n"
            "• 🔍 Глубокий психологический анализ человеческих характеров\n"
            "• 🗡️ Острая критика социального неравенства и угнетения\n"
            "• 💬 Простой и выразительный язык — каждое слово на своём месте\n"
            "• 😂 Тонкий юмор и сатира, вплетённые в серьёзные темы\n"
            "• 🌍 Достоверное изображение узбекской жизни и общества\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "📚 *Жанры, которыми он владел:*\n"
            "• 📖 Роман и повесть\n"
            "• 📝 Рассказ (его сильнейший жанр)\n"
            "• 🎭 Драматургия и пьесы\n"
            "• ✍️ Поэзия\n"
            "• 🔄 Художественный перевод\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🌟 *Вклад в узбекскую литературу:*\n"
            "Каххор признан одним из основоположников современной\n"
            "узбекской прозы. Он поднял узбекский короткий рассказ\n"
            "до мирового уровня, сочетая чеховскую краткость\n"
            "с глубоким содержанием.\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🔤 *Переводческая деятельность:*\n"
            "Познакомил узбекских читателей с шедеврами русской литературы:\n"
            "• Пушкин — «Капитанская дочка»\n"
            "• Гоголь — «Женитьба», «Ревизор»\n"
            "• Толстой — «Война и мир» (вместе с женой)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "works_menu": (
            "📚 *ПРОИЗВЕДЕНИЯ АБДУЛЛЫ КАХХОРА*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Какой тип произведений вас интересует? 👇"
        ),
        "works_buttons": {
            "novels": "📗 Романы",
            "stories": "📘 Рассказы",
            "plays": "🎭 Пьесы",
            "back": "⬅️ Назад",
        },
        "novels": (
            "📗 *РОМАНЫ И ПОВЕСТИ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📖 *1. Сароб (Мираж) — 1943*\n"
            "   _Его дебютный роман, отражающий сложные\n"
            "   социальные проблемы советской эпохи._\n\n"
            "📖 *2. Огни Кушчинара — 1951*\n"
            "   _Самый известный роман, изображающий жизнь\n"
            "   узбекского колхоза в советское время.\n"
            "   Удостоен Сталинской премии._\n\n"
            "📖 *3. Синчалак — 1958*\n"
            "   _Психологически насыщенная повесть\n"
            "   об отношениях и человеческих чувствах._\n\n"
            "📖 *4. Сказки о прошлом — 1965*\n"
            "   _Литературная автобиография:\n"
            "   воспоминания и наблюдения из жизни._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "stories": (
            "📘 *ЗНАМЕНИТЫЕ РАССКАЗЫ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🌿 *Анор (Гранат)* — Глубокий рассказ о бедности и надежде\n\n"
            "🎭 *Воришка (O'g'ri)* — Социальная критика, юмор и трагедия\n\n"
            "😔 *Больной (Bemor)* — Тонкий анализ простой человеческой души\n\n"
            "🌺 *Женщина, не евшая изюм* — О судьбе женщины\n\n"
            "👒 *Ужас (Dahshat)* — Мощное исследование психологии страха\n\n"
            "📚 *Учитель литературы* — О просвещении и ответственности\n\n"
            "🕯️ *Поминки на свадьбе* — Жизненные противоречия через юмор\n\n"
            "⚔️ *Дедушка Асрор* — О патриотизме в годы войны\n\n"
            "🌙 *Человек без головы (1929)* — Его первый знаменитый рассказ\n\n"
            "🏘️ *Махалля* — Живое изображение жизни квартала\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),
        "plays": (
            "🎭 *ПЬЕСЫ И ДРАМАТУРГИЯ*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "🎪 *Шёлковое сюзане (1950)*\n"
            "   _Драма, прославляющая узбекскую национальную культуру._\n\n"
            "🦷 *Больные зубы (1950)*\n"
            "   _Сатирическая комедия — самая любимая пьеса,\n"
            "   разоблачающая пороки общества через острый юмор._\n\n"
            "⚰️ *Голос из гроба (1962)*\n"
            "   _Философская драма на темы жизни,\n"
            "   смерти и человеческой природы._\n\n"
            "👩‍👩‍👧 *Мои дорогие матери (1967)*\n"
            "   _Написана в последние годы жизни —\n"
            "   нежное исследование материнской любви._\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━"
        ),

        "poems_list": [
            (
                "📝 *СТИХОТВОРЕНИЕ №1: «Мать»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Мать — свет, мать — жизнь,\n"
                "Мать — сила, мать — крылья.\n"
                "Её глаза — утренняя звезда,\n"
                "Её слова — слова сердца._\n\n"
                "✍️ _Абдулла Каххор_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *СТИХОТВОРЕНИЕ №2: «Родина»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Здесь каждый камень — история,\n"
                "Каждое дерево — дорогая память.\n"
                "Воздух этой земли — её климат,\n"
                "Здесь человек живёт в счастье._\n\n"
                "✍️ _Абдулла Каххор_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *СТИХОТВОРЕНИЕ №3: «Книга»*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Книга — друг, книга — учитель,\n"
                "Ключ к тайнам жизни.\n"
                "На каждой странице — вселенная,\n"
                "В каждом слове — бесконечный смысл._\n\n"
                "✍️ _Абдулла Каххор_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
            (
                "📝 *СТИХОТВОРЕНИЕ №4: «Когда луна сгорает» (1924)*\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "_Моё первое стихотворение — 1924 год,\n"
                "Опубликовано в журнале «Муштум».\n"
                "Первая песня молодого сердца —\n"
                "Написана с любовью к жизни._\n\n"
                "✍️ _Абдулла Каххор (О своём первом стихотворении)_\n"
                "━━━━━━━━━━━━━━━━━━━━━━━━"
            ),
        ],

        "facts_list": [
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #1*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nАбдулла Каххор получил прозвище «Чехов узбеков». Его рассказы обладают той же лаконичностью и психологической глубиной, что и произведения Антона Чехова.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #2*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nНа протяжении своей карьеры Каххор писал под более чем 10 псевдонимами: Ниш, Мавлоно Куфур, Эркабой, Гулёр, Норин Шилпиқ и другими.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #3*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nВместе с женой Кибриё Каххоровой он перевёл на узбекский язык монументальный роман Льва Толстого «Война и мир» — это считается одним из величайших достижений узбекской переводческой литературы.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #4*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nЕго первое стихотворение «Когда луна сгорает» было опубликовано в 1924 году в 8-м номере сатирического журнала «Муштум» (Кулак). После этого он сосредоточился на прозе.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #5*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nСталинская премия 1952 года была присуждена ему за роман «Огни Кушчинара» — самую престижную литературную награду советской эпохи.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #6*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nКаххор глубоко изучал узбекский устный фольклор и широко использовал народные элементы в своём творчестве, обогащая рассказы подлинным голосом своего народа.",
            "🎯 *ИНТЕРЕСНЫЙ ФАКТ #7*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\nПереводя Пушкина, Чехова, Гоголя и Толстого на узбекский язык, Каххор создал культурный мост между русской и узбекской литературными традициями.",
        ],

        "quiz_start": "🧠 *ВИКТОРИНА НАЧАТА!*\n━━━━━━━━━━━━━━━━━━━━━━━━\n\n5 вопросов об Абдулле Каххоре. Каждый правильный ответ = 1 балл!\n\nГотовы? Вперёд! 🚀",
        "quiz_question": "❓ *Вопрос {num}/5:*\n\n{question}",
        "quiz_correct": "✅ *Правильно!* Отлично! +1 балл",
        "quiz_wrong": "❌ *Неверно!* Правильный ответ: *{answer}*",
        "quiz_result": (
            "🏁 *ВИКТОРИНА ЗАВЕРШЕНА!*\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📊 *Ваш результат: {score}/5*\n"
            "📈 *Процент: {percent}%*\n\n"
            "{message}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "_📚 Образовательный бот Абдулла Каххор_"
        ),
        "quiz_messages": {
            5: "🌟 *ОТЛИЧНО!* Вы знаете всё об Абдулле Каххоре! Превосходно!",
            4: "🎉 *ПРЕКРАСНО!* Отличный результат! Ваши знания на высоком уровне!",
            3: "👍 *ХОРОШО!* Средний результат. Продолжайте изучать!",
            2: "💪 *СТАРАЙТЕСЬ!* Нужно больше читать о нём!",
            1: "📖 *ЧИТАЙТЕ БОЛЬШЕ!* Узнайте больше об Абдулле Каххоре!",
            0: "🔄 *ПОПРОБУЙТЕ ЕЩЁ РАЗ!* Не расстраивайтесь — читайте и попробуйте снова!",
        },
    },
}


# ════════════════════════════════════════════════════════════════
#  QUIZ QUESTIONS (Multilingual)
# ════════════════════════════════════════════════════════════════

QUIZ_QUESTIONS = {
    "uz": [
        {
            "q": "Abdulla Qahhor qaysi yili tug'ilgan?",
            "options": ["1905", "1907", "1910", "1900"],
            "answer": "1907"
        },
        {
            "q": "Abdulla Qahhor qaysi shaharda tug'ilgan?",
            "options": ["Toshkent", "Samarqand", "Qo'qon", "Buxoro"],
            "answer": "Qo'qon"
        },
        {
            "q": "Qaysi roman Abdulla Qahhорga 1952-yilgi Stalin mukofotini olib keldi?",
            "options": ["Sarob", "Sinchalak", "Qo'shchinor chiroqlari", "O'tmishdan ertaklar"],
            "answer": "Qo'shchinor chiroqlari"
        },
        {
            "q": "Abdulla Qahhor qaysi buyuk rus yozuvchisiga o'xshatilib «O'zbeklar...si» deyilgan?",
            "options": ["Pushkin", "Tolstoy", "Dostoyevskiy", "Chexov"],
            "answer": "Chexov"
        },
        {
            "q": "Abdulla Qahhorning birinchi she'ri qaysi jurnalda chop etilgan?",
            "options": ["Yoshlik", "Mushtum", "Guliston", "Sharq yulduzi"],
            "answer": "Mushtum"
        },
        {
            "q": "Abdulla Qahhor qaysi yili vafot etgan?",
            "options": ["1965", "1970", "1968", "1972"],
            "answer": "1968"
        },
        {
            "q": "Qaysi asar Abdulla Qahhorning mashhur satirik komediyasi?",
            "options": ["Sarob", "Og'riq tishlar", "Sinchalak", "Anor"],
            "answer": "Og'riq tishlar"
        },
        {
            "q": "Abdulla Qahhor xotini bilan birgalikda qaysi asar tarjimasini amalga oshirgan?",
            "options": ["Urush va tinchlik", "Jinoyat va jazo", "Kapitan qizi", "Revizor"],
            "answer": "Urush va tinchlik"
        },
        {
            "q": "Abdulla Qahhorning birinchi hikoyasi qaysi?",
            "options": ["Anor", "Boshsiz odam", "O'g'ri", "Bemor"],
            "answer": "Boshsiz odam"
        },
        {
            "q": "Abdulla Qahhor qaysi adabiy yo'nalishning namoyandasi?",
            "options": ["Romantizm", "Modernizm", "Realizm", "Simvolizm"],
            "answer": "Realizm"
        },
    ],
    "en": [
        {
            "q": "In which year was Abdulla Qahhor born?",
            "options": ["1905", "1907", "1910", "1900"],
            "answer": "1907"
        },
        {
            "q": "In which city was Abdulla Qahhor born?",
            "options": ["Tashkent", "Samarkand", "Kokand", "Bukhara"],
            "answer": "Kokand"
        },
        {
            "q": "Which novel brought Abdulla Qahhor the 1952 Stalin Prize?",
            "options": ["Sarob (Mirage)", "Sinchalak", "The Lights of Qo'shchinor", "Tales from the Past"],
            "answer": "The Lights of Qo'shchinor"
        },
        {
            "q": "Which great Russian writer is Abdulla Qahhor compared to?",
            "options": ["Pushkin", "Tolstoy", "Dostoyevsky", "Chekhov"],
            "answer": "Chekhov"
        },
        {
            "q": "In which magazine was Abdulla Qahhor's first poem published?",
            "options": ["Yoshlik", "Mushtum", "Guliston", "Sharq Yulduzi"],
            "answer": "Mushtum"
        },
        {
            "q": "In which year did Abdulla Qahhor pass away?",
            "options": ["1965", "1970", "1968", "1972"],
            "answer": "1968"
        },
        {
            "q": "Which work is Abdulla Qahhor's famous satirical comedy?",
            "options": ["Sarob", "Hurting Teeth", "Sinchalak", "Anor"],
            "answer": "Hurting Teeth"
        },
        {
            "q": "Which monumental work did Qahhor translate together with his wife?",
            "options": ["War and Peace", "Crime and Punishment", "The Captain's Daughter", "The Government Inspector"],
            "answer": "War and Peace"
        },
        {
            "q": "What was Abdulla Qahhor's first famous short story?",
            "options": ["Anor", "The Headless Man", "The Thief", "The Sick"],
            "answer": "The Headless Man"
        },
        {
            "q": "Which literary movement did Abdulla Qahhor represent?",
            "options": ["Romanticism", "Modernism", "Realism", "Symbolism"],
            "answer": "Realism"
        },
    ],
    "ru": [
        {
            "q": "В каком году родился Абдулла Каххор?",
            "options": ["1905", "1907", "1910", "1900"],
            "answer": "1907"
        },
        {
            "q": "В каком городе родился Абдулла Каххор?",
            "options": ["Ташкент", "Самарканд", "Коканд", "Бухара"],
            "answer": "Коканд"
        },
        {
            "q": "Какой роман принёс Абдулле Каhhору Сталинскую премию 1952 года?",
            "options": ["Сароб (Мираж)", "Синчалак", "Огни Кушчинара", "Сказки о прошлом"],
            "answer": "Огни Кушчинара"
        },
        {
            "q": "С каким великим русским писателем сравнивают Абдуллу Каhhора?",
            "options": ["Пушкин", "Толстой", "Достоевский", "Чехов"],
            "answer": "Чехов"
        },
        {
            "q": "В каком журнале было опубликовано первое стихотворение Абдуллы Каhhора?",
            "options": ["Ёшлик", "Муштум", "Гулистон", "Шарк Юлдузи"],
            "answer": "Муштум"
        },
        {
            "q": "В каком году скончался Абдулла Каhhор?",
            "options": ["1965", "1970", "1968", "1972"],
            "answer": "1968"
        },
        {
            "q": "Какое произведение является знаменитой сатирической комедией Абдуллы Каhhора?",
            "options": ["Сароб", "Больные зубы", "Синчалак", "Анор"],
            "answer": "Больные зубы"
        },
        {
            "q": "Какое монументальное произведение Каhhор перевёл вместе с женой?",
            "options": ["Война и мир", "Преступление и наказание", "Капитанская дочка", "Ревизор"],
            "answer": "Война и мир"
        },
        {
            "q": "Как назывался первый знаменитый рассказ Абдуллы Каhhора?",
            "options": ["Анор", "Человек без головы", "Воришка", "Больной"],
            "answer": "Человек без головы"
        },
        {
            "q": "Представителем какого литературного направления был Абдулла Каhhор?",
            "options": ["Романтизм", "Модернизм", "Реализм", "Символизм"],
            "answer": "Реализм"
        },
    ],
}


# ════════════════════════════════════════════════════════════════
#  KEYBOARD BUILDERS
# ════════════════════════════════════════════════════════════════

def build_lang_keyboard():
    """Language selection keyboard shown at /start."""
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    kb.add(
        KeyboardButton("🇺🇿 O'zbekcha"),
        KeyboardButton("🇬🇧 English"),
        KeyboardButton("🇷🇺 Русский"),
    )
    return kb


def build_main_menu(lang):
    """Main menu keyboard based on language."""
    b = TEXTS[lang]["buttons"]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton(b["bio"]),
        KeyboardButton(b["creativity"]),
        KeyboardButton(b["works"]),
        KeyboardButton(b["poems"]),
        KeyboardButton(b["facts"]),
        KeyboardButton(b["quiz"]),
    )
    kb.add(KeyboardButton(b["lang"]))
    return kb


def build_back_keyboard(lang):
    """Single back button keyboard."""
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    kb.add(KeyboardButton(TEXTS[lang]["buttons"]["back"]))
    return kb


def build_works_keyboard(lang):
    """Works sub-menu keyboard."""
    b = TEXTS[lang]["works_buttons"]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    kb.add(
        KeyboardButton(b["novels"]),
        KeyboardButton(b["stories"]),
        KeyboardButton(b["plays"]),
    )
    kb.add(KeyboardButton(b["back"]))
    return kb


def build_quiz_keyboard(options):
    """Quiz answer options keyboard."""
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for option in options:
        kb.add(KeyboardButton(option))
    return kb


# ════════════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════

def get_lang(user_id):
    """Return user's selected language, default to English."""
    return user_data.get(user_id, {}).get("lang", "en")


def set_lang(user_id, lang):
    """Set user's language."""
    if user_id not in user_data:
        user_data[user_id] = {}
    user_data[user_id]["lang"] = lang


def send_main_menu(message, lang):
    """Send the main menu message with keyboard."""
    bot.send_message(
        message.chat.id,
        TEXTS[lang]["main_menu"],
        parse_mode="Markdown",
        reply_markup=build_main_menu(lang),
    )


def is_back(text, lang):
    """Check if the user pressed a back button."""
    return text == TEXTS[lang]["buttons"]["back"]


# ════════════════════════════════════════════════════════════════
#  QUIZ ENGINE
# ════════════════════════════════════════════════════════════════

def start_quiz(message, lang):
    """Initialise quiz state and send first question."""
    uid = message.from_user.id
    questions = random.sample(QUIZ_QUESTIONS[lang], 5)
    user_data[uid]["quiz"] = {
        "questions": questions,
        "current": 0,
        "score": 0,
        "active": True,
    }
    bot.send_message(
        message.chat.id,
        TEXTS[lang]["quiz_start"],
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove(),
    )
    send_quiz_question(message.chat.id, uid, lang)


def send_quiz_question(chat_id, uid, lang):
    """Send the current quiz question."""
    quiz = user_data[uid]["quiz"]
    idx = quiz["current"]
    q_data = quiz["questions"][idx]

    options = q_data["options"][:]
    random.shuffle(options)
    quiz["shuffled_options"] = options  # Save shuffled order

    text = TEXTS[lang]["quiz_question"].format(
        num=idx + 1,
        question=q_data["q"],
    )
    bot.send_message(
        chat_id,
        text,
        parse_mode="Markdown",
        reply_markup=build_quiz_keyboard(options),
    )


def handle_quiz_answer(message, lang):
    """Process a quiz answer and advance state."""
    uid = message.from_user.id
    quiz = user_data[uid]["quiz"]
    idx = quiz["current"]
    q_data = quiz["questions"][idx]
    answer = message.text.strip()

    if answer == q_data["answer"]:
        quiz["score"] += 1
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["quiz_correct"],
            parse_mode="Markdown",
        )
    else:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["quiz_wrong"].format(answer=q_data["answer"]),
            parse_mode="Markdown",
        )

    quiz["current"] += 1

    if quiz["current"] >= 5:
        # Quiz finished
        quiz["active"] = False
        score = quiz["score"]
        percent = score * 20
        msg_key = score if score in TEXTS[lang]["quiz_messages"] else 0
        result_msg = TEXTS[lang]["quiz_result"].format(
            score=score,
            percent=percent,
            message=TEXTS[lang]["quiz_messages"][msg_key],
        )
        bot.send_message(
            message.chat.id,
            result_msg,
            parse_mode="Markdown",
            reply_markup=build_main_menu(lang),
        )
    else:
        send_quiz_question(message.chat.id, uid, lang)


# ════════════════════════════════════════════════════════════════
#  COMMAND HANDLERS
# ════════════════════════════════════════════════════════════════

@bot.message_handler(commands=["start"])
def cmd_start(message):
    """Handle /start command — show welcome and language selector."""
    uid = message.from_user.id
    # Clear any previous quiz state
    user_data[uid] = {}

    # Send welcome message using whichever language was set, default English
    lang = get_lang(uid)
    bot.send_message(
        message.chat.id,
        TEXTS[lang]["welcome"],
        parse_mode="Markdown",
        reply_markup=build_lang_keyboard(),
    )


@bot.message_handler(commands=["menu"])
def cmd_menu(message):
    """Handle /menu command — go to main menu directly."""
    uid = message.from_user.id
    lang = get_lang(uid)
    send_main_menu(message, lang)


@bot.message_handler(commands=["help"])
def cmd_help(message):
    """Handle /help command."""
    uid = message.from_user.id
    lang = get_lang(uid)
    help_texts = {
        "uz": (
            "ℹ️ *BOT HAQIDA*\n\n"
            "Bu bot Abdulla Qahhor haqida ta'lim beruvchi interaktiv bot.\n\n"
            "*Buyruqlar:*\n"
            "• /start — Botni qayta boshlash\n"
            "• /menu — Asosiy menyuga qaytish\n"
            "• /help — Yordam\n\n"
            "_📚 Abdulla Qahhor Educational Bot_"
        ),
        "en": (
            "ℹ️ *ABOUT THIS BOT*\n\n"
            "This is an interactive educational bot about Abdulla Qahhor.\n\n"
            "*Commands:*\n"
            "• /start — Restart the bot\n"
            "• /menu — Go to main menu\n"
            "• /help — Show this help\n\n"
            "_📚 Abdulla Qahhor Educational Bot_"
        ),
        "ru": (
            "ℹ️ *О БОТЕ*\n\n"
            "Это интерактивный образовательный бот об Абдулле Каhhоре.\n\n"
            "*Команды:*\n"
            "• /start — Перезапустить бота\n"
            "• /menu — Главное меню\n"
            "• /help — Эта справка\n\n"
            "_📚 Образовательный бот Абдулла Каhhор_"
        ),
    }
    bot.send_message(
        message.chat.id,
        help_texts.get(lang, help_texts["en"]),
        parse_mode="Markdown",
        reply_markup=build_main_menu(lang),
    )


# ════════════════════════════════════════════════════════════════
#  MAIN MESSAGE HANDLER
# ════════════════════════════════════════════════════════════════

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    """Central router for all text messages."""
    uid = message.from_user.id
    text = message.text.strip() if message.text else ""
    lang = get_lang(uid)

    # ── Initialise user data if missing ──────────────────────────
    if uid not in user_data:
        user_data[uid] = {}

    # ── If quiz is active, route to quiz handler ──────────────────
    if user_data[uid].get("quiz", {}).get("active"):
        handle_quiz_answer(message, lang)
        return

    # ── Language selection ────────────────────────────────────────
    if text == "🇺🇿 O'zbekcha":
        set_lang(uid, "uz")
        bot.send_message(message.chat.id, TEXTS["uz"]["lang_chosen"], parse_mode="Markdown")
        send_main_menu(message, "uz")
        return

    if text == "🇬🇧 English":
        set_lang(uid, "en")
        bot.send_message(message.chat.id, TEXTS["en"]["lang_chosen"], parse_mode="Markdown")
        send_main_menu(message, "en")
        return

    if text == "🇷🇺 Русский":
        set_lang(uid, "ru")
        bot.send_message(message.chat.id, TEXTS["ru"]["lang_chosen"], parse_mode="Markdown")
        send_main_menu(message, "ru")
        return

    # ── Change language button ────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["lang"]:
        bot.send_message(
            message.chat.id,
            "🌐 *Choose your language:*",
            parse_mode="Markdown",
            reply_markup=build_lang_keyboard(),
        )
        return

    # ── Back button ───────────────────────────────────────────────
    if is_back(text, lang):
        # Check if we are inside works submenu
        if user_data[uid].get("in_works"):
            user_data[uid]["in_works"] = False
            bot.send_message(
                message.chat.id,
                TEXTS[lang]["works_menu"],
                parse_mode="Markdown",
                reply_markup=build_works_keyboard(lang),
            )
        else:
            user_data[uid]["in_works"] = False
            send_main_menu(message, lang)
        return

    # ── Biography ─────────────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["bio"]:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["bio"],
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Creativity ────────────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["creativity"]:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["creativity"],
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Works menu ────────────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["works"]:
        user_data[uid]["in_works"] = True
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["works_menu"],
            parse_mode="Markdown",
            reply_markup=build_works_keyboard(lang),
        )
        return

    # ── Works: Novels ─────────────────────────────────────────────
    if text == TEXTS[lang]["works_buttons"]["novels"]:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["novels"],
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Works: Stories ────────────────────────────────────────────
    if text == TEXTS[lang]["works_buttons"]["stories"]:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["stories"],
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Works: Plays ──────────────────────────────────────────────
    if text == TEXTS[lang]["works_buttons"]["plays"]:
        bot.send_message(
            message.chat.id,
            TEXTS[lang]["plays"],
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Poems ─────────────────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["poems"]:
        poems = TEXTS[lang]["poems_list"]
        # Send all poems one by one
        for i, poem in enumerate(poems):
            if i < len(poems) - 1:
                bot.send_message(message.chat.id, poem, parse_mode="Markdown")
            else:
                # Last poem gets the back button
                bot.send_message(
                    message.chat.id,
                    poem,
                    parse_mode="Markdown",
                    reply_markup=build_back_keyboard(lang),
                )
        return

    # ── Interesting Facts ─────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["facts"]:
        fact = random.choice(TEXTS[lang]["facts_list"])
        bot.send_message(
            message.chat.id,
            fact + "\n\n_💡 Yana ko'rish uchun tugmani qayta bosing!_" if lang == "uz"
            else fact + "\n\n_💡 Press the button again for another fact!_" if lang == "en"
            else fact + "\n\n_💡 Нажмите кнопку снова для другого факта!_",
            parse_mode="Markdown",
            reply_markup=build_back_keyboard(lang),
        )
        return

    # ── Quiz ──────────────────────────────────────────────────────
    if text == TEXTS[lang]["buttons"]["quiz"]:
        start_quiz(message, lang)
        return

    # ── Fallback: unknown input ───────────────────────────────────
    fallback = {
        "uz": "❓ Noma'lum buyruq. Quyidagi menyudan tanlang 👇",
        "en": "❓ Unknown command. Please use the menu below 👇",
        "ru": "❓ Неизвестная команда. Используйте меню ниже 👇",
    }
    bot.send_message(
        message.chat.id,
        fallback.get(lang, fallback["en"]),
        reply_markup=build_main_menu(lang),
    )


# ════════════════════════════════════════════════════════════════
#  ERROR HANDLER
# ════════════════════════════════════════════════════════════════

@bot.message_handler(content_types=["photo", "video", "audio", "document", "sticker"])
def handle_media(message):
    """Politely reject non-text messages."""
    uid = message.from_user.id
    lang = get_lang(uid)
    replies = {
        "uz": "🙏 Faqat matn xabarlarini qabul qilaman. Menyudan foydalaning.",
        "en": "🙏 I only accept text messages. Please use the menu.",
        "ru": "🙏 Я принимаю только текстовые сообщения. Используйте меню.",
    }
    bot.reply_to(message, replies.get(lang, replies["en"]))


# ════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("  📚 Abdulla Qahhor Educational Bot")
    print("  Status: Starting...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    # Run the bot with infinite polling and automatic restart on errors
    bot.infinity_polling(timeout=30, long_polling_timeout=20)
