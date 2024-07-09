import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("7127599495:AAEssQLs9OvwezCWra_b-NivGjS7UnfqrTc", parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    historique = InlineKeyboardButton('Historique', callback_data='historique')
    campus = InlineKeyboardButton('Nos Campus', callback_data='campus')
    localisation = InlineKeyboardButton('Localisation', callback_data='localisation')
    candidature = InlineKeyboardButton('Postuler', callback_data='candidature')
    partenaire = InlineKeyboardButton('Partenaire', callback_data='partenaire')
    markup.row(historique, campus)
    markup.row(localisation, candidature)
    markup.row(partenaire)
    ISTDI = InlineKeyboardButton('ISTDI', callback_data='ISTDI')
    ICIA = InlineKeyboardButton('ICIA', callback_data='ICIA')
    IAC = InlineKeyboardButton('3IAC', callback_data='3IAC')
    PISTI = InlineKeyboardButton('PISTI', callback_data='PISTI')
    SEAS = InlineKeyboardButton('SEAS', callback_data='SEAS')
    markup.row(ISTDI)
    markup.row(ICIA)
    markup.row(SEAS)
    markup.row(IAC)
    markup.row(PISTI)

    texte = (
        "Bonjour et bienvenue sur le chatbot de renseignement de IUC\n cette institue a été fondé en 2002 par le president Fondateur PAUL GUIMEZAP\n"
        "elle comprend de nombreuses ecoles certaines parmis elles en partenariat avec "
        "l'etranger et presentant les meilleur formation et debouché dans le milieu du travail\n veullez consulter le menu ci dessous⬇️ pour plus d'information")
    photo = open('iucc.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption=texte, parse_mode='HTML', reply_markup=markup)
    user = message.from_user
    print(user.username)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    p_istdi = open('istdi.jpeg', 'rb')
    p_icia = open('icia.png', 'rb')
    p_iac = open('iac.jpeg', 'rb')
    p_seas = open('seas.png', 'rb')
    p_pisti = open('pisti.jpeg', 'rb')
    p_loc = open('location.jpeg', 'rb')
    p_hist = open('historique.jpeg', 'rb')
    p_campus= open('campus.jpeg','rb')
    p_partenaire = open('partenaire.jpeg', 'rb')
    p_candidature = open('candidature.jpeg','rb')
    markup = InlineKeyboardMarkup()
    # istdi = InlineKeyboardButton('Terminer', callback_data='supprimer')
    # markup.row(istdi)
    try:
        if call.data == "ISTDI":
            text = ("ISTDI pour <b>Institut Supérieur des Technologies et du Design Industriel</b>\n\n"
                    "est le premier établissement de l’IUC. Cette école constitue la plaque tournante "
                    "de l’univers technologique et industriel. Elle offre aux candidats titulaires "
                    "d’un baccalauréat (C, D, E, F, ou BT) ou tout autre diplôme reconnu équivalent, "
                    "la possibilité de préparer :\n\n"
                    "* Le BTS Industriel et Technologique\n"
                    "* La Licence Professionnelle\n"
                    "* Le Master Professionnel\n\n"
                    "Depuis sa création en 2002, l’ISTDI a su insérer une nouvelle élite d’agents "
                    "de maîtrise et cadres dans de nombreuses entreprises relevant du secteur industriel "
                    "de notre économie, et dont les résultats aujourd’hui sont encourageants.")
            formation = InlineKeyboardButton('FORMATION', callback_data='form_istdi')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_istdi, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "ICIA":
            text = (
                "ICIA pour<b> Institut de Commerce et d'Ingénierie d'Affaires</b>\n\n constitue le pôle de commerce et Gestion de l’IUC. Sa mission est de former les commerciaux, les communicateurs, et les gestionnaires hautement performants et répondant aux attentes des milieux socioprofessionnels. ICIA offre aux candidats titulaires d’un Baccalauréat (A, C, D, E, F, ou BT) ou tout autre diplôme reconnu équivalent.")
            formation = InlineKeyboardButton('FORMATION', callback_data='form_icia')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_icia, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "3IAC":
            text = "3IAC pour<b> Institut d'Ingénierie Informatique d'Afrique Centrale</b>\n\n Ici les formations, les diplomes et autres menu selon l'analyse L’Institut d’Ingénierie Informatique d’Afrique Centrale (3IAC) est une école dont la vocation est de préparer les étudiants à la fois aux métiers de l’ingénieur et au master suivant le profil de base du candidat titulaire d’un baccalauréat toutes spécialités confondues. Le choix de la filière devant varier selon la nature du baccalauréat, les candidats ont la possibilité soit d’obtenir le diplôme d’Ingénieur ou de Master en Informatique ou de préparer après 02 années de formation, une licence Professionnelle industrielle dans les domaines des technologies de l’information et de la communication (TIC)."
            # formation = InlineKeyboardButton('FORMATION', callback_data='form_iac')
            # markup.row(formation)
            bot.send_photo(call.message.chat.id, p_iac, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "PISTI":
            text = "PISTI pour <b>Programmes Internationaux des Sciences et Technologies de l'Innovation</b>\n\nIl s'occupe de l'intégration des jeunes dans les formations délocalisées en Sciences et Technologies de l'Innovation, avec l'obtention du diplôme d'Ingénieur. Les titulaires d'un Baccalauréat scientifique ont la possibilité de préparer, après 02 années de formation, une Licence en Sciences et Techniques dans les domaines de la chimie, de la physique et des mathématiques appliquées, leur donnant accès aux cycles Master Professionnel ou aux écoles d'Ingénieurs.\n\nCe Pôle englobe plusieurs formations :\n\n- Les classes prépa qui permettent aux étudiants d'intégrer les Ecoles d'Ingénieurs\n- BTS Santé\n- Le Cycle d'Ingénieur en Architecture (ADI), avec des possibilités d'obtenir des bourses pour l'Italie\n- Le cycle d'Ingénieur du réseau Polytech de France\n- Le Cycle d'Ingénierie Biomédicale (IBM)\n- Le Cycle d'Ingénierie en Agronomie"
            formation = InlineKeyboardButton('FORMATION', callback_data='form_pisti')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_pisti, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "SEAS":
            text = (
                "SEAS pour <b>School of Engineering & Applied Sciences</b>\n\n"
                "Dans le pôle d'excellence existe l'École d'Ingénierie et des Sciences Appliquées (SEAS), qui offre "
                "une formation anglo-saxonne concise et complète dans le domaine de l'ingénierie, de la santé et de la gestion des affaires. "
                "L'inscription aux programmes de carrière de cette école est ouverte aux titulaires du GCE Advanced Level / BAC, HND / BTS / "
                "Équivalence, et Bachelor / BAC+3 ou Équivalence. Dans l'École d'Ingénierie et des Sciences Appliquées (SEAS), il existe les cycles de formation suivants :\n\n"
                "* Executive Programs/MBA\n"
                "* Bachelor of Engineering\n"
                "* Bachelor in Business & Management Sciences\n"
                "* Bachelor of Health Science\n"
                "* Bachelor of Technology / Licence Technologique\n"
                "* HND Cycle Commercial and Industrial Fields"
            )
            # formation = InlineKeyboardButton('FORMATION', callback_data='form_seas')
            # markup.row(formation)
            bot.send_photo(call.message.chat.id, p_seas, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "localisation":
            text = "L'Institut Universitaire de la Côte (IUC) est situé dans la région du littoral, au Cameroun, plus précisément dans le département du Wouri, arrondissement de Douala 5ème, au quartier Logbessou."
            formation = InlineKeyboardButton('DETAILS', callback_data='form_loc')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_loc, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "historique":
            text = "L'Institut Universitaire de la Côte a été fondé en 2002 sous le nom d'Institut Supérieur de Technologie et du Design Industriel (ISTDI) par Monsieur Paul GUIMEZAP. "
            formation = InlineKeyboardButton('PLUS D\'INFO', callback_data='form_hist')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_hist, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "campus":
                text = "L’Institut Universitaire de la Côte situé dans la ville de Douala, possède trois sièges dont le Campus principal, situé à LOGBESSOU loin du vacarme de la ville est repartis en trois campus A, B, C. le second quant à lui est situé en plein centre des affaires à AKWA à proximité des étudiants et travailleurs de la zone. Enfin le troisième récemment créé dans la ville de l'ouest Dschang."
                formation = InlineKeyboardButton('DETAILS', callback_data='form_campus')
                markup.row(formation)
                bot.send_photo(call.message.chat.id, p_campus, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "candidature":
            text = "Les candidatures à l'Institut Universitaire de la Côte (IUC) suivent un processus structuré qui comprend plusieurs étapes importantes. Voici une description détaillée de ce processus:"
            formation = InlineKeyboardButton('PLUS DE DETAILS', callback_data='form_cand')
            markup.row(formation)
            bot.send_photo(call.message.chat.id, p_candidature, caption=text, parse_mode='HTML', reply_markup=markup)


        if call.data == "partenaire":
            text = (" L’IUC est en partenariat avec de prestigieuses écoles nationales étrangères pour faciliter la mobilité des étudiants et enseignants à l’international.Grâce à ces partenariats, "
                    "l'IUC peut offrir des opportunités d'échange d'étudiants et de professeurs, favorisant ainsi la diversité culturelle et le partage d'expertise. Ces collaborations internationales permettent également à "
                    "l'IUC d'inscrire ses programmes dans une perspective globale, en abordant les défis sociétaux à l'échelle internationale et en favorisant une approche interdisciplinaire.")
            bot.send_photo(call.message.chat.id, p_partenaire, caption=text, parse_mode='HTML', reply_markup=markup)

        if call.data == "form_istdi":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "------> BTS INDUSTRIELS ET TECHNOLOGIQUES <------:\n\n***"
                                                   "-Chaudronnerie et Souderie\n"
                                                   "-Fabrication Mécanique\n"
                                                   "-Construction métallique\n"
                                                   "-Mécatronique\n"
                                                   "-Maintenance Industrielle et Productique\n"
                                                   "-Informatique industrielle et automatique\n"
                                                   "-Génie logiciel\n"
                                                   "- Réseaux et sécurité informatique\n"
                                                   "- Gestion des systèmes d'information\n"
                                                   "- Télécommunication\n"
                                                   "- Maintenance des systèmes informatiques\n"
                                                   "- Infographie et web design\n"
                                                   "- E-commerce et marketing numérique\n\n\n"
                                                   "------> LICENCE PRO. INDUSTRIELLES ET TECHNOLOGIQUES <------\n\n"
                                                   "- Génie télécommunication et Réseaux\n"
                                                   "- Génie mécanique et productique\n"
                                                   "- Maintenance et expertise industrielle\n"
                                                   "- Génie civil\n"
                                                   "- Génie énergétique et industriel\n"
                                                   "- Management des services de l'automobile\n"
                                                   "- Génie logiciel\n"
                                                   "- Génie bois\n"
                                                   "- Electrotechnique/Electronique\n"
                                                   "- Hygiène sécurité industrielle\n"
                                                   "- Instrumentation et Maintenance Biométrique\n"
                                                   "- Mecanique/Constructions industrielles\n"

                                                   "------> MASTERS POLYTECH Yaoundé <------\n\n"
                                                   "- Génie civil (GC)\n"
                                                   "- Génie Industriel et maintenance (GIM)\n"
                                                   "- Génie énergétique et environnement\n"

                                                   "------> MASTERS PRO. INDUSTRIELLES ET TECHNOLOGIQUES <------\n\n"
                                                   "- Génie électrique et informatique industrielle (GE2I)\n"
                                                   "- Génie des réseaux et télécommunications (GRT)\n"
                                                   "- Système d'information et Génie logiciel\n"
                                                   "- Qualité Hygiène sécurité industrielle\n"
                                                   "- Système d'information et réseaux (SIR)\n"
                                                   "- Système d'information audit et conseil (SIAC)\n")

        if call.data == "form_pisti":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "------> BTS ETUDES MEDICO-SANITAIRES <------:\n\n***"
                                                   "-Sciences infirmières\n"
                                                   "-Kinésithérapie\n"
                                                   "-Sage-femme\n"

                                                   "------> BTS SCIENCES ET TECHNIQUES BIOMEDICALES <------\n\n"
                                                   "- Techniques de laboratoires et d'analyses médicales\n"
                                                   "- Radiologie et imagerie médicale\n"

                                                   "------> CLASSES PREPARATOIRES AUX GRANDES ECOLES D'INGENIEURS <------\n\n"
                                                   "02 ans de préparations aux sciences de l'ingénieur, poursuite des études en 3ème "
                                                   "année dans une école d'ingénieurs étrangère dans les parcours suivants:\n"
                                                   "- Génie du bois\n"
                                                   "- Génie mécanique\n"
                                                   "- Architecture Navale\n"
                                                   "- Génie des matériaux\n"
                                                   "- Génie info & Numérique\n"
                                                   "- Robotique/Mécanique\n"
                                                   "- Sciences Actuaires, Assurance\n"
                                                   "- Génie électrique/énergétique\n")

        if call.data == "form_icia":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, "------>BTS Commerce et de Gestion<------\n"
                                                   "- Assurance\n"
                                                   "- Banque et Finance\n"
                                                   "- Commerce International\n"
                                                   "- Communications des Organisations\n"
                                                   "- Comptabilité et Gestion des Entreprises\n"
                                                   "- Gestion de la Qualité\n"
                                                   "- Journalisme\n"
                                                   "- Logistique et Transport\n"
                                                   "- Marketing Commerce et Vente\n"
                                                   "- Ressources Humaines\n\n"
                                                   "------> BTS CARRIERES JURIDIQUES <------\n\n"
                                                   "- Droit Domanial\n"
                                                   "- Gestion Fiscale\n"
                                                   "- Douane et Travail\n"
                                                   "- Droit des Affaires et de l'entreprise\n\n"
                                                   "------> LICENCE Pro.COMMERCE ET DE GESTION <------"
                                                   "- Assurance\n"
                                                   "- Gestion de la Qualité\n"
                                                   "- Communications des Organisations\n"
                                                   "- Publicité\n"
                                                   "- Banque et Finance\n"
                                                   "- Comptabilité Controle et Audit\n"
                                                   "- Gestions des Ressources Humaines\n"
                                                   "- Sciences et techniques Administratives\n"
                                                   "- Management des Opérations du Commerce International\n\n"
                                                   " ---> ISUGA (Tout BAC)<--- \n\n"
                                                   " - BAC+3 (IUC)\n"
                                                   "-> BACHELOR\n"
                                                   " - Europe - Asie (Internationnal Business)\n"
                                                   "-> MASTER\n"
                                                   "- Diplome de Manager du Développement d'affaires à l'interationnal\n"
                                                   "- MBA Europe - Asie International Business\n"
                                                   "---> VATEL France délocalise ses formations à l'IUC <---\n\n"
                                                   "- Industrie Touristique\n"
                                                   "- Manager des services hoteliers à l'international\n")
            if call.data == "form_seas":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id,
                                 "------> HND INDUSTRIAL FIELDS <------:\n\n***"
                                 "- Chemical Engineering\n"
                                 "- Telecommunication\n"
                                 "- Civil Engineering\n"
                                 "- Mechanical Fabrication\n"
                                 "- Software Engineering and Computing\n"
                                 "- Topography\n"
                                 "- Electrical and Electronices Engineering\n"
                                 "- Network and Security\n"
                                 "- Industrial Computing and Automation\n\n"
                                 "------> HND COMMERCIAL FIELDS <------\n\n"
                                 "- Accounting\n"
                                 "- Banking and Finance\n"
                                 "- Maketing\n"
                                 "- Management\n"
                                 "- Project Management\n"
                                 "- Logistics and Transport Management\n"
                                 "- Human Resource Management\n"
                                 "- International Trade\n"
                                 "- Custom and Transit\n\n"
                                 "------> BACHELOR OF TECHNOLOGY <------\n\n"
                                 "- Chemical Engineering\n"
                                 "- Geometics and Surveying\n"
                                 "- Civil Engineering\n"
                                 "- Mechatronics\n"
                                 "- Software Engineering and Computing\n"
                                 "- Automation and Control\n"
                                 "- Electrical and Electronices Engineering\n"
                                 "- Welding and Fabrication Technology\n"
                                 "- Thermal Engineering\n"
                                 "- Information Technology\n"
                                 "- Communication and Computer Networks\n\n"
                                 "------> BTS SCIENCES ET TECHNIQUES BIOMEDICALES <------\n\n"
                                 "- Techniques de laboratoires et d'analyses médicales\n"
                                 "- Radiologie et imagerie médicale\n\n"
                                 "------> CLASSES PREPARATOIRES AUX GRANDES ECOLES D'INGENIEURS <------\n\n"
                                 "02 ans de préparations aux sciences de l'ingénieur, poursuite des études en 3ème "
                                 "année dans une école d'ingénieurs étrangère dans les parcours suivants:\n"
                                 "- Génie du bois\n"
                                 "- Génie mécanique\n"
                                 "- Architecture Navale\n"
                                 "- Génie des matériaux\n"
                                 "- Génie info & Numérique\n"
                                 "- Robotique/Mécanique\n"
                                 "- Sciences Actuaires, Assurance\n"
                                 "- Génie électrique/énergétique\n"
                                 )

                if call.data == "form_iac":
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    bot.send_message(call.message.chat.id,
                                     "------>TECHNOLOGIE DE L'INFORMATIQUE<------\n\n" "- Génie des matériaux\n"
                                     "- *** DIPLOME CANADIEN ***\n\n"
                                     "- Réseautique et Sécurité informatique (Tout BAC)\n"
                                     "- Programmation et applications mobiles\n"
                                     "- *** DIPLOME FRANCAIS ***\n\n"
                                     "- Classes preparatoires Informatiques (3IL) BAC C,D,E\n"
                                     "- Programmation et applications mobiles\n"
                                     "- Ingénieurie Informatique\n\n"

                                     " *** CYCLE BACHELOR EN INFORMATIQUE ***\n"
                                     "- Concepteur des systèmes d'informations informatisés (CS2I/3IL-France)\n\n"

                                     " *** CYCLE MASTER EUROPEEN EN INFORMATIQUE ***\n\n"
                                     "-Manager des systèmes d'informations infrastrutures (MS2I/3IL-France) \n\n"
                                     " *** CYCLE D'INGENIEURIE INFORMATIQUE (3IL) ***\n"
                                     "- Informatique (3IL - Afrique Centrale)\n\n")

        if call.data == "form_hist":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,
                             "Le monde évolue à une vitesse vertigineuse et l’on observe une montée considérable du nombre d’entreprises. Malgré la disponibilité permanente des emplois et des postes à pourvoir en entreprises, les patrons ont de plus en plus de mal à trouver la main d’œuvre compétente, susceptible de satisfaire les besoins de leurs structures.\n\n"
                             "Face à ce constat, Monsieur Paul GUIMEZAP, décide de contribuer à la résolution de ce problème,  en  mettant sur pied, dans la région du littoral, département du Wouri, arrondissement de Douala 5ème, au quartier Logbessou, un INSTITUT SUPERIEUR dont les qualités répondent aux exigences des entreprises.\n\n"
                             "C’est ainsi qu’est créé l’ISTDI (Institut Supérieur de Technologie et du Design Industriel) par arrêté N° 02/0094/MINESUP/DDES/ESUP du 13 Septembre 2002 et autorisation d’ouverture N° 0102/MINESUP/DDES/ESUP du 18 septembre 2002.\n\n"
                             "Soucieux de la croissance et de l’autonomie universitaire, L’ISTDI est ensuite devenu l’Institut Universitaire de la Côte (IUC) en 2011 par arrêté N°5/05156/N/MINESUP/DDES/ESUP/SAC/ebm. L’école comporte à ce jour Cinq (5) établissements notamment :\n"
                             "* ISTDI (Institut Supérieur de Technologies & du Design Industriel) : l’école  qui  forme les étudiants dans les cycles BTS, Licence, Masters dans les filières Technologiques et Industriels.\n"
                             "* ICIA (Institut de Commerce et d’Ingénierie d’Affaires), forme les étudiants en commerce et gestion dans les cycles BTS, Licence et Masters executive programs.\n"
                             "* 3IAC (Institut d’Ingénierie Informatique d’Afrique Centrale) offre des cycles d’Ingénieur et de master dans les domaines de l’informatique et des Technologies de l’Information et de la Communication (TIC) avec des partenariats étrangers.\n"
                             "* PISTI (Programmes Internationaux des Sciences et Technologies de l’Innovation), forme dans les filières des Classes Préparatoires aux Grandes Ecoles d’Ingénieurs (CP) en partenariat avec de grandes Universités internationales  (France, Portugal, en Italie et en Indeentre  autres)\n"
                             "* SEAS : School of Engineering and Applied Sciences qui offre des formations purement anglophones dans les filières Techniques industrielles, de même que les filières de commerce et de gestion.\n"
                             "* Au fil du temps le pôle d’excellence en Afrique s’est doté d’un autre campus situé au quartier Akwa en plein centre de la ville de Douala."
                             )
        if call.data == "form_campus":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id,
                             "1. Campus de Logbessou, Douala\n"
                             "Ce campus est le siège principal de l'IUC. Initialement fondé en 2002 sous le nom d'Institut Supérieur de Technologie et du Design Industriel (ISTDI), il a été créé pour répondre à la demande croissante de main-d'œuvre qualifiée dans la région du littoral. En 2011, l'ISTDI a évolué pour devenir l'Institut Universitaire de la Côte (IUC).\n"
                             "- Spécialisations : Le campus offre des programmes variés dans les domaines technologiques, industriels, commerciaux et informatiques.\n\n"
                             "2. Campus d'Akwa, Douala\n"
                             "Situé en plein centre de Douala, le campus d'Akwa a été créé pour faciliter l'accès à une éducation de qualité en plein cœur de la ville. Il s'inscrit dans la vision d'expansion de l'IUC pour mieux desservir les étudiants et les entreprises locales.\n"
                             "- Spécialisations : Ce campus propose des formations dans les domaines techniques industriels, commerciaux, et de gestion, souvent en collaboration avec des partenaires internationaux.\n\n"
                             "3. Campus de Dschang\n"
                             "Il est l'un des plus récents ajouts à l'IUC. Dschang est une ville universitaire réputée, et l'ouverture de ce campus vise à capitaliser sur cet environnement académique stimulant.\n"
                             "- Spécialisations : Le campus de Dschang propose des programmes similaires à ceux des autres campus, mais peut également inclure des partenariats locaux pour des programmes spécifiques en fonction des besoins régionaux."
                             )
        if call.data == "form_cand":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            text = (
                "<b>1. Choix du Programme</b>\n"
                "Les candidats doivent d'abord choisir le programme de formation qui correspond à leurs aspirations académiques et professionnelles parmi les diverses filières proposées par l'IUC, telles que les sciences sociales, les sciences humaines, l'ingénierie, la gestion, etc.\n\n"

                "<b>2. Préparation des Documents</b>\n"
                "Les candidats doivent préparer un dossier de candidature complet, comprenant généralement :\n"
                "- Une copie certifiée conforme du diplôme de fin d'études secondaires (Baccalauréat ou équivalent).\n"
                "- Les relevés de notes des années scolaires précédentes.\n"
                "- Un curriculum vitae (CV).\n"
                "- Une lettre de motivation expliquant les raisons du choix de l'IUC et du programme spécifique.\n"
                "- Des lettres de recommandation (souvent demandées pour les programmes de niveau supérieur).\n"
                "- Une copie de la carte nationale d'identité ou du passeport.\n\n"

                "<b>3. Soumission de la Candidature</b>\n"
                "Les dossiers de candidature peuvent être soumis de deux manières :\n"
                "- <b>En ligne</b> : Via le portail de candidature en ligne de l'IUC, où les candidats peuvent télécharger les documents requis et remplir le formulaire de candidature.\n"
                "- <b>En personne</b> : En déposant le dossier physique au bureau des admissions de l'IUC.\n\n"

                "<b>4. Frais de Candidature</b>\n"
                "Le paiement des frais de candidature est souvent requis. Les détails sur le montant et les modalités de paiement sont disponibles sur le site de l'IUC ou au bureau des admissions."
            )
            bot.send_message(call.message.chat.id, text, parse_mode='HTML')



        if call.data == 'supprimer':
            bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass


bot.polling()
