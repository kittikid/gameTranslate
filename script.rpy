init:
     if port == 1:
          image ayso g1 = im.Rotozoom("character/guide/1.png", 0, 1.5)
          image ayso g2 = im.Rotozoom("character/guide/2.png", 0, 1.5)
          image ayso g3 = im.Rotozoom("character/guide/3.png", 0, 1.5)
          image ayso g4 = im.Rotozoom("character/guide/4.png", 0, 1.5)
          image ayso g5 = im.Rotozoom("character/guide/5.png", 0, 1.5)
          image ayso g6 = im.Rotozoom("character/guide/6.png", 0, 1.5)
          image ayso g7 = im.Rotozoom("character/guide/7.png", 0, 1.5)
          image ayso g8 = im.Rotozoom("character/guide/8.png", 0, 1.5)
          image ayso g9 = im.Rotozoom("character/guide/9.png", 0, 1.5)
          image ayso g10 = im.Rotozoom("character/guide/10.png", 0, 1.5)
          image ayso g11 = im.Rotozoom("character/guide/11.png", 0, 1.5)
          image ayso g12 = im.Rotozoom("character/guide/12.png", 0, 1.5)
          image ayso g13 = im.Rotozoom("character/guide/13.png", 0, 1.5)
     elif port == 0:
          image side g1 = "character/guide/1.png"
          image side g2 = "character/guide/2.png"
          image side g3 = "character/guide/3.png"
          image side g4 = "character/guide/4.png"
          image side g5 = "character/guide/5.png"
          image side g6 = "character/guide/6.png"
          image side g7 = "character/guide/7.png"
          image side g8 = "character/guide/8.png"
          image side g9 = "character/guide/9.png"
          image side g10 = "character/guide/10.png"
          image side g11 = "character/guide/11.png"
          image side g12 = "character/guide/12.png"
          image side g13 = "character/guide/13.png"
define ayanogg = Character("Неизвестная девушка", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define glgg = DynamicCharacter("player_name", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define beg_p = Character("Убегающий парень", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define b = Character("Продавщица", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define s = Character("Неизвестный парень", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define y = Character("Юми", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define n = Character("Начальник заводского комплекса", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define f = Character("Работник заводского комплекса", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define npc = DynamicCharacter("npc_name2", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define x1 = Character("Первый хулиган", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="x1", who_drop_shadow=[ (2, 1) ] )
define x2 = Character("   Второй хулиган", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="x2", who_drop_shadow=[ (2, 1) ] )
define x3 = Character("Третий хулиган", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="x3", who_drop_shadow=[ (2, 1) ] )
define guide1 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g1", who_drop_shadow=[ (2, 1) ] )
define guide2 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g2", who_drop_shadow=[ (2, 1) ] )
define guide3 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g3", who_drop_shadow=[ (2, 1) ] )
define guide4 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g4", who_drop_shadow=[ (2, 1) ] )
define guide5 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g5", who_drop_shadow=[ (2, 1) ] )
define guide6 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g6", who_drop_shadow=[ (2, 1) ] )
define guide7 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g7", who_drop_shadow=[ (2, 1) ] )
define guide8 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g8", who_drop_shadow=[ (2, 1) ] )
define guide9 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g9", who_drop_shadow=[ (2, 1) ] )
define guide10 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g10", who_drop_shadow=[ (2, 1) ] )
define guide11 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g11", who_drop_shadow=[ (2, 1) ] )
define guide12 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g12", who_drop_shadow=[ (2, 1) ] )
define guide13 = Character("Гид", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', image="g13", who_drop_shadow=[ (2, 1) ] )
define ayanogg1 = Character("Аяно {size=24}глава оккультного клуба{/size}", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define adm_magazine = Character("Администратор магазина", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define suzuku = Character("Сузуки", color="#FFFF00", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
define of = Character("Официантка", color="#BAF300", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
label npc_list:
     call screen npc_list
screen npc_list:
     add 'bf'
     text "{b}Отношения/Доверие/Страх{/b}" xalign 0.4 yalign 0
     viewport:
         xalign 0.1 ypos 10 xysize (1900, 1800)
         child_size (1920, 2000)
         scrollbars "vertical"
         spacing 1 ###расстояние от порта до края изображе
         draggable True
         mousewheel True
         arrowkeys True
         for number_npc in range(1, number_npc_max):
             python:
                 npc_id = 'npc'+str(number_npc)
                 name_npc = eval(npc_id)["npc_name"]
                 fam_npc = eval(npc_id)["npc_fam"]
                 v_npc = eval(npc_id)["pich_npc"]
                 gender_npc = eval(npc_id)["gender_npc"]
                 contact_npc = eval(npc_id)["contact_npc"]
                 love_npc = eval(npc_id)["love_npc"]
                 fear_npc = eval(npc_id)["fear_npc"]
                 npc_stats = eval(npc_id)['npc_stats']
                 stats_forces = npc_stats['forces']
                 stats_agility = npc_stats['agility']
                 stats_stamina = npc_stats['stamina']
                 stats_lucky = npc_stats['lucky']
                 stats_science = npc_stats['science']
                 stats_cunning = npc_stats['cunning']
                 stats_authority = npc_stats['authority']
                 stats_erudition = npc_stats['erudition']
                 npc_nature = eval(npc_id)['npc_nature']
             textbutton "{color=#000000}id_[number_npc] / [name_npc] [fam_npc]: [contact_npc]/[love_npc]/[fear_npc] / Характер: [npc_nature]{/color}" xalign pol_text_v yalign pol_text_z
             if pol_text_z >= 0.95:
                 $ pol_text_z = -0.0075
                 $ pol_text_v = 0.8
             $ pol_text_z += 0.0175
     textbutton "{b}Далее{/b}" action Jump('stats12') xalign 0.97 yalign 0.99
screen list_npc:
     add 'bf'
     viewport:
         xalign 0.1 ypos 10 xysize (1900, 1800)
         child_size (1920, 2000)
         scrollbars "vertical"
         spacing 1 ###расстояние от порта до края изображе
         draggable True
         mousewheel True
         arrowkeys True
         for number_npc in range(1, number_npc_max):
             python:
                 npc_id = 'npc'+str(number_npc)
                 name_npc = eval(npc_id)["npc_name"]
                 fam_npc = eval(npc_id)["npc_fam"]
                 v_npc = eval(npc_id)["pich_npc"]
                 gender_npc = eval(npc_id)["gender_npc"]
                 contact_npc = eval(npc_id)["contact_npc"]
                 love_npc = eval(npc_id)["love_npc"]
                 fear_npc = eval(npc_id)["fear_npc"]
                 npc_stats = eval(npc_id)['npc_stats']
                 stats_forces = npc_stats['forces']
                 stats_agility = npc_stats['agility']
                 stats_stamina = npc_stats['stamina']
                 stats_lucky = npc_stats['lucky']
                 stats_science = npc_stats['science']
                 stats_cunning = npc_stats['cunning']
                 stats_authority = npc_stats['authority']
                 stats_erudition = npc_stats['erudition']
             textbutton "{color=#000000}[name_npc] [fam_npc]: id_[number_npc]_[stats_forces][stats_agility][stats_stamina][stats_lucky][stats_science][stats_cunning][stats_authority][stats_erudition]{/color}" xalign pol_text_v yalign pol_text_z
             if pol_text_z >= 0.95:
                 $ pol_text_z = -0.0075
                 $ pol_text_v = 0.7
             $ pol_text_z += 0.0175
     textbutton "{b}Далее{/b}" action Jump('guide') xalign 0.97 yalign 0.99
label rr_npc:
     $ dialoge = 0
     $ id_npc = 0
     $ app = (stats_erudition_gg + stats_science_gg) / 5 + dop_app
     $ mod_horror = abs(stats_forces_gg + stats_agility_gg) / 5 - app + dop_mod_horror
     $ smoking_npc = 0
     $ smok_npc = 0
     if language_game == 1:
         menu:
             "{color=#000000}Создать персонажей самостоятельно{/color}":
                 "Данная функция все еще разрабатывается."
                 jump rr_npc
             "{color=#000000}Рандомизировать всех персонажей{/color}":
                 $ randomize_npc = 1
                 label _random_npc:
                 python:
                     for number_npc in range(randomize_npc, number_npc_max):
                         npc_number = "npc"+str(number_npc)
                         if atribute_npc_123 == 0:
                             stats_forces_npc = renpy.random.randint(10, 40)
                             stats_agility_npc = renpy.random.randint(10, 40)
                             stats_stamina_npc = renpy.random.randint(10, 40)
                             stats_science_npc = renpy.random.randint(10, 40)
                             stats_cunning_npc = renpy.random.randint(10, 40)
                             stats_authority_npc = renpy.random.randint(10, 40)
                             stats_erudition_npc = renpy.random.randint(10, 40)
                             stats_lucky_npc = renpy.random.randint(10, 40)
                         else:
                             if atribute_npc_123 <= 30:
                                 atribute_npc_123 = 10
                                 atribute_npc_1234 = 40
                             elif atribute_npc_123 >= 80:
                                 atribute_npc_123 = 50
                                 atribute_npc_1234 = 100
                             else:
                                 atribute_npc_123 = atribute_npc_123
                                 atribute_npc_1234 = atribute_npc_123 + 20
                             stats_forces_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_agility_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_stamina_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_science_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_cunning_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_authority_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_erudition_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                             stats_lucky_npc = renpy.random.randint(atribute_npc_123, atribute_npc_1234)
                         club_npc = renpy.random.randint(1, 5)
                         if gender_npc_123 == 1:
                             pol_npc = renpy.random.randint(1, 75)
                         elif gender_npc_123 == 2:
                             pol_npc = renpy.random.randint(25, 100)
                         else:
                             pol_npc = renpy.random.randint(1, 100)
                         if pol_npc <= 50:
                             pol_npc = 1
                         else:
                             pol_npc = 2
                         if smoke_npc_123 == True:
                             smoking_npc = renpy.random.randint(6, 10)
                         elif smoke_npc_123 == False:
                             smoking_npc = renpy.random.randint(1, 10)
                         stats_npc = renpy.random.randint(1, 10)
                         if active_npc_p == 0:
                             active_npc = renpy.random.randint(1, 5)
                         else:
                             active_npc = active_npc_p
                         if stats_npc == 1:
                             stats_forces_npc += 20
                         elif stats_npc == 2:
                             stats_agility_npc += 20
                         elif stats_npc == 3:
                             stats_stamina_npc += 20
                         elif stats_npc == 4:
                             stats_science_npc += 20
                         elif stats_npc == 5:
                             stats_cunning_npc += 20
                         elif stats_npc == 6:
                             stats_authority_npc += 20
                         elif stats_npc == 7:
                             stats_erudition_npc += 20
                         elif stats_npc == 8:
                             stats_lucky_npc += 20
                         elif stats_npc == 9:
                             stats_forces_npc += 10
                             stats_agility_npc += 10
                         elif stats_npc == 10:
                             stats_stamina_npc += 10
                             stats_agility_npc += 10
                         if smoking_npc <= 8:
                             smok_npc = 1
                         else:
                             smok_npc = 2
                         random_otn = renpy.random.randint(0, 10)
                         contact_npc = 0 - mod_horror * 3 + app + app_contact_npc + random_otn
                         love_npc = 0 - mod_horror * 2 + app_love_npc + random_otn
                         fear_npc = 0 + mod_horror * 3 + app_fear_npc
                         perk = ['Верный', 'Фонтан идей', 'Старательный', 'Быстро печатает', 'Вялый', 'Одиночка', 'Командный', 'Самостоятельный', 'Ленивый', 'Заядлый игрок', 'Школьная знаменитость', 'Омежка', 'Чистюля', 'Неряха', 'Бережливый']
                         if pol_npc == 2:
                             npc_nature1 = ["Романтичный", "Адекватность", "Надменный"]
                             v_npc = renpy.random.randint(1, 19)
                             if ladies_man == True:
                                 contact_npc += 20
                                 love_npc += 20
                             if boost_otn == True:
                                 contact_npc += boost_otn_zn
                                 love_npc += boost_otn_zn
                         elif pol_npc == 1:
                             npc_nature1 = ['Агрессивный', "Адекватность", "Надменный"]
                             v_npc = renpy.random.randint(1, 19)
                         if name_npc == 'Japan':
                             if pol_npc == 1:
                                 name_list = ["Джуничи", "Даичи", "Изаму", "Йошики", "Кайоши", "Кен", "Кенджи", "Мамору", "Наоки", "Акайо", "Дэйчи", "Дэйки", "Кеничи", "Джэро", "Кента", "Риота", "Ясуши"]
                             elif pol_npc == 2:
                                 name_list = ["Аки", "Аяно", "Акеми", "Акира", "Азуми", "Аземи", "Асука", "Аяка", "Аямо", "Изуми", "Киоко", "Кохеку", "Ай", "Ая", "Мива", "Мегуми", "Киоко", "Мика", "Мики", "Мичики", "Мияко", "Мэй", "Наоки", "Мэйко", "Рика", "Сора", "Фумико", "Хоши", "Юка", "Ясуко"]
                             l_name_list = ["Сузуки", "Такахаши", "Танака", "Ватанабе", "Ямамото", "Накамура", "Кобаяши", "Ёшида", "Ямада", "Сасаки", "Ито", "Танака", "Такахаси", "Хасимото", "Хасэгава", "Фудзивара", "Оота", "Сибата", "Миямото"]
                         elif name_npc == 'Russian':
                             if pol_npc == 1:
                                 name_list = ["Вадим", "Михаил", "Александр", "Ярослав", "Юрий", "Станислав", "Павел", "Петр", "Захар", "Моисей", "Давид", "Даниил", "Виктор", "Евгений", "Владислав", "Евдоким", "Ероха", "Сыч", "Богдан"]
                                 l_name_list = ["Сталин", "Иванов", "Горбачев", "Бандера", "Астапов", "Высоцкий", "Ковалев", "Власов", "Молчанов", "Анисимов", "Шутов", "Ленин", "Смирнов", "Кузнецов", "Попов", "Васильев", "Павлов"]
                             elif pol_npc == 2:
                                 name_list = ["Александра", "Маргарита", "Алина", "Алиса", "Алла", "Алсу", "Алена", "Евгений", "Зенаида", "Олеся", "Оксана", "Любовь", "Наташка", "Надежда", "Снежана", "Анастасия", "Екатерина", "Елизавета"]
                                 l_name_list = ["Сталина", "Иванова", "Горбачева", "Бандера", "Астапова", "Высоцкая", "Ковалева", "Власова", "Молчанова", "Анисимова", "Шутова", "Ленина", "Смирнова", "Кузнецова", "Попова", "Васильева", "Павлова"]
                         else:
                             if pol_npc == 1:
                                 name_list = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles", "Joseph", "Thomas", "Christopher", "Daniel", "Paul", "Mark", "Donald", "George", "Steven", "Edward", "Brian"]
                             elif pol_npc == 2:
                                 name_list = ["Mary", "Patrica", "Linda", "Barbara", "Elizabeth", "Jennifer", "Maria", "Susan", "Margaret", "Lisa", "Nansy", "Karen", "Betty", "Hellen", "Sandra", "Donna", "Carol", "Sharon"]
                             l_name_list = ["Smith", "Johnson", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Moore", "Thompson", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Collins"]
                         random_name = renpy.random.choice(name_list)
                         random_fam = renpy.random.choice(l_name_list)
                         squeeze = 1
                         npc_nature = renpy.random.choice(npc_nature1)
                         perk = renpy.random.choice(perk)
                         if npc_nature == "Агрессивный":
                             if trap == True:
                                 fear_npc -= 30
                                 love_npc -= 50
                                 contact_npc -= 50
                             if otn_agressive == True:
                                 love_npc += otn_agressive_zn - 20
                                 contact_npc += otn_agressive_zn
                         student_soviet_g_npc = renpy.random.randint(1, 5)
                         id_npc += 1
                         number_phone = 0
                         location_school = ['school_class', 'join_school', 'corridor_school', 'roof', 'canteen', 'pool']
                         location_npc = renpy.random.choice(location_school)
                         npc_stats = {"agility":stats_agility_npc, "forces":stats_forces_npc, "stamina":stats_stamina_npc, "science":stats_science_npc, "cunning":stats_cunning_npc, "authority":stats_authority_npc, "erudition":stats_erudition_npc, "lucky":stats_lucky_npc}
                         npc_character = {'perk':perk, "gender_npc":pol_npc, "smoking_npc":smok_npc, "npc_stats":npc_stats, "pich_npc":v_npc, "npc_name":random_name, "npc_fam":random_fam, "contact_npc":contact_npc, "love_npc":love_npc, "fear_npc":fear_npc, "squeeze":squeeze, "npc_nature":npc_nature, "id_npc":id_npc, "number_phone":number_phone, "location_npc":location_npc, "active_npc":active_npc, "student_soviet_g_npc":student_soviet_g_npc, "club_npc":club_npc}
                         setattr(store, npc_number, npc_character)
         if randomize_npc >= 2:
             jump check_location
         $ name_npc = ['Пусто']
         $ fam_npc = ['Пусто']
         $ v_npc = ['Пусто']
         $ gender_npc = ['Пусто']
         $ contact_npc = ['Пусто']
         $ love_npc = ['Пусто']
         $ fear_npc = ['Пусто']
         $ npc_id = ['Пусто']
         if language_game == 1:
             "Рандомизация завершена."
             $ contact_club = 0
             $ suzuki_number = 0
             $ suzuki = 0
             $ manga2_1 = 0
             $ colvo_npc = 0
             $ pol_text_v = 0.03
             $ pol_text_z = 0.01
             $ npc = 0
             $ dialoge_mode = 1
             $ multiplier_dialoge = 1
             $ ayano_contact = 0
             $ depravity_ayano = 0
             $ ayano_trust = 0
             $ heal = 0
             $ candy = 0
             $ zhiha = 0
             $ wear_zhiga = 0
             $ cupboard_cigarette = 0
             $ cupboard_cola = 0
             $ cupboard_rolton = 0
             $ cupboard_heal = 0
             $ cupboard_candy = 0
             $ cupboard_zhiga = 0
             $ joob_complete = 0
             $ ayano_number = 0
             $ ayano_TC = 0
             $ gotov_st = 0
             $ club_rang = 0
             $ old_dialoge = 1
             $ number_occult_club = 2
             $ authority_club_occult = 0
             $ popularity_club_occult = 0
             $ purity_club_occult = 0
             $ budget_club_occult_plus = 0
             $ budget_club_occult = 1000
             $ pool_ivent = 0
             $ videocamera = 0
             $ meiko_compulsion = 0
             $ meiko_compulsion_max = 135
             $ meiko_compulsion_lvl = 0
             $ pool_club_r = 1
             $ body_meiko = 0
             $ nude_meiko = 0
             python:
                 for number_npc in range(1, number_npc_max):
                     npc_id = 'npc'+str(number_npc)
                     gender_npc = eval(npc_id)['gender_npc']
                     name_npc = eval(npc_id)["npc_name"]
                     fam_npc = eval(npc_id)["npc_fam"]
                     if gender_npc == 1:
                         name_meiko = name_npc + ' ' + fam_npc
             define meiko_p = Character("[name_meiko]", color="#3a2a3a", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
             python:
                 global_project = 0
                 festivale = 0
                 club_complete = 0
                 authority_minus = 0
                 new_participant_club_occult = 0
                 random = 0
                 microwave = 0
                 playstation = 0
                 poster = 0
                 refrigerator = 0
                 furniture = 0
                 tablet = 0
                 tablet_painting = 0
                 camera = 0
                 vacuum = 0
                 authority_club_occult += (stats_authority_gg_info / 4)
             call screen list_npc
         elif language_game == 2:
             "Randomization completed."
         jump guide
     elif language_game == 2:
         menu:
             "{color=#000000}Create a character yourself{/color}":
                 "This function is not yet ready."
             "{color=#000000}Randomize characters{/color}":
                 $ random_npc = 0
                 jump _random_npc
     image npc = "character/npc/npc_f/1.png"
     image npc1 = im.Rotozoom("character/npc/npc_f/2.png", 0, 0.9)
     image npc2 = im.Rotozoom("character/npc/npc_f/3.png", 0, 0.6)
     image npc3 = im.Rotozoom("character/npc/npc_f/4.png", 0, 0.6)
     image npc4 = im.Rotozoom("character/npc/npc_f/5.png", 0, 0.6)
     image npc5 = im.Rotozoom("character/npc/npc_f/6.png", 0, 0.6)
     image npc6 =  im.Rotozoom("character/npc/npc_f/7.png", 0, 0.6)
     image npc7 = im.Rotozoom("character/npc/npc_f/8.png", 0, 0.6)
     image npc8 = im.Rotozoom("character/npc/npc_f/9.png", 0, 0.6)
     image npc9 = im.Rotozoom("character/npc/npc_f/10.png", 0, 0.4)
     image npc10 = im.Rotozoom("character/npc/npc_m/1.png", 0, 0.5)
     image npc11 = "character/npc/npc_m/2.png"
     image npc12 = im.Rotozoom("character/npc/npc_m/3.png", 0, 0.8)
     image npc13 = im.Rotozoom("character/npc/npc_m/4.png", 0, 0.6)
     image npc14 = im.Rotozoom("character/npc/npc_m/5.png", 0, 0.6)
     image npc15 = im.Rotozoom("character/npc/npc_m/6.png", 0, 0.5)
     image npc16 = im.Rotozoom("character/npc/npc_m/7.png", 0, 0.8)
     image park = "backgrounds/location/park.jpg"
     image school = "backgrounds/school.jpg"
     image school1 = "backgrounds/school1.jpg"
     image school2 = "backgrounds/school2.jpg"
     image select_character = "character/fuck.png"
     image sprite = "character/select_appearance.jpg"
     image corridor = "backgrounds/school/corridor2.png"
     image class = "backgrounds/school/class.jpg"
     image roof = "backgrounds/school/roof.jpg"
     image room = "backgrounds/location/ph/room_v.png"
     image beach = "backgrounds/location/beach.jpg"
     image stroll = "backgrounds/location/stroll.jpg"
     image magazine = "backgrounds/location/mag.jpg"
     image bf = "backgrounds/location/bf.jpg"
     image gf = "backgrounds/location/gf.jpg"
     image p1 = "character/npc/p1.png"
     image p2 = "character/npc/p2.png"
     image smoking = "character/npc/s.png"
     image smoking1 = "character/npc/s1.png"
     image cab = "backgrounds/location/cab.png"
     image cab = "backgrounds/location/cab1.png"
     image nac = im.Rotozoom("character/npc/nac/2.png", 0, 1.5)
     image nac1 = im.Rotozoom("character/npc/nac/1.png", 0, 1.5)
     image nac2 = im.Rotozoom("character/npc/nac/3.png", 0, 1.5)
     image nac3 = im.Rotozoom("character/npc/nac/4.png", 0, 1.5)
     image menu_gg = "menu_gg.png"
     image side x1 = "character/npc/xuligan/1.png"
     image side x2 = "character/npc/xuligan/2.png"
     image side x3 = "character/npc/xuligan/3.png"
     image xuligan_class = "backgrounds/school/class_xuligan1.jpg"
     image toilet = "backgrounds/school/toilet.png"
     image screenshotroom = "character/guide/screenshot/room.png"
     image screenshotmenu = "character/guide/screenshot/menu.png"
     image screenshotschool = "character/guide/screenshot/school.png"
     image screenshotcomputer = "character/guide/screenshot/computer.png"
label guide:
     $ ayano_ivent = 0
     if port == 1:
         scene bf with dissolve
         show ayso g1 with dissolve
         guide1 "Привет тебе, игрок! Я тот самый NPC, который будет рушить четвертую стену в самом начале игры! Почему же так?"
         guide1 "Постоянные вопросы, которые жаждут однотипных ответов, начали немного раздражать разработчиков, поэтому меня и наняли тебя проконсультировать! Все просто, так ведь?"
         show ayso g2
         guide2 "Как бы там ни было, все вышесказанное скорее ненужная для тебя демагогия, нежели нужная информация. Скажи мне, нужна ли тебе консультация?"
         $ guide_club = 0
         menu:
             "{color=#000000}Нужна{/color}":
                 show ayso g4
                 guide4 "Значит я все же тебе действительно понадобилась? Не ожидала такого. Обычно все игроки пропускают меня, а после жалуются, что они ничего не понимали на протяжении всей игры!"
                 show ayso g1
                 guide1 "Ой, опять я начала говорить не по теме, но я же в этом не виновата! Наверное. Но все же..."
                 show ayso g5
                 guide5 "Как жаль, что тебе придется терпеть трёп низкоквалицированного сотрудника, которого наняли из-за бюджета, равному однозначному и округлому числу."
                 show ayso g6
                 guide6 "Ну-с, для начала давай разберемся с начальным интерфейсом. Чтобы перейти на карту города/школы тебе всего-то нужно нажать на иконку телефона, а после вот на это - {image=phone/gps_idle.png}"
                 show ayso g2
                 guide2 "Что делает каждая из видных тебе иконок можно понять по их виду. К примеру, иконка компьютера переносит игрока в режим пользования компьютером, а иконка телефона, соответственно, в телефон, через который можно звонить и писать СМС."
                 show ayso g1
                 guide1 "Но самое интересное откроется, если нажать ПКМ: меню действий! С помощью него ты сможешь делать дополнительные действия, которые в дальнейшем и с идеями в голове разработчиков будут дополняться! Не загораживать же все доступное место иконками!"
                 show ayso g3
                 guide3 "Бр... Даже страшно думать об этом..."
                 show ayso g1
                 guide1 "Все просто, так ведь?"
                 show ayso g3
                 guide3 "Ох... Осталось рассказать о мелочи, но по словам разработчиков эту мелочь игроки гиперболизировали до такой степени, что она воплотилась в глобальные жалобы со стороны игроков: в чем цель игры?"
                 show ayso g5
                 guide5 "Если говорить по правде, то я и сама не знаю!"
                 show ayso g1
                 guide1 "Шучу! Цель игры проста и понятна: окончить школу и обеспечить приемлимым будущим своего персонажа: будешь ли ты хулиганьем, которое перерастет свой спермотоксикоз и станет достойной ячейкой общества"
                 guide1 "А может и не перерастет, став мафиози и без того в захудалом криминальном городишке. Возможно ты решишь стать примерным учеником, который в будущем станет офисным планктоном..."
                 show ayso g3
                 guide3 "Не лучшее будущее, но все же..."
                 show ayso g4
                 guide4 "Если подытожить все вышесказанное, то ты можешь стать кем угодно. Твои выборы - будущее твоего персонажа, а уже эти выборы напрямую завязаны на РПГ системе, которая может ограничивать твои рвения, но также может и помочь!"
                 show ayso g1
                 guide1 "Все очень и очень просто, так ведь? Главное не помереть раньше времени."
                 show ayso g3
                 guide3 "Упс, я на тебя потратила уже достаточно много времени! Мне нужно помочь и другим людям в консультации!"
                 show ayso g4
                 guide4 "Еще увидимся, игрок!"
                 $ help = 1
                 $ help_club = 1
                 $ help_computer = 1
                 $ help_school = 1
                 $ help_fight = 1
                 $ help_class = 1
                 $ help_occult = 1
                 jump titre
             "{color=#000000}Да кому вообще нужны эти обучения?{/color}":
                 show ayso g3
                 guide3 "Ну, как хочешь. Мое дело предложить, а твое дело отказаться."
                 $ help_computer = 0
                 $ help_club = 0
                 $ help_school = 0
                 $ help_fight = 0
                 $ help_class = 0
                 $ help_occult = 0
                 jump titre
     elif port == 0:
         scene screenshotroom with dissolve
         guide4 "Так… А теперь скажи мне, нуждаешься ли ты в разъяснении механик и систем игры?"
         $ guide_club = 0
         menu:
             "{color=#000000}Нуждаюсь.{/color}":
                 guide4 "Значит я все же тебе действительно понадобилась? Не ожидала такого. Обычно все игроки пропускают меня, а после жалуются, что они ничего не понимали на протяжении всей игры!"
                 guide1 "Ой, опять я начала говорить не по теме, но я же в этом не виновата! Наверное. Но все же..."
                 guide5 "Как жаль, что тебе придется терпеть трёп низкоквалицированного сотрудника, которого наняли из-за бюджета, равному однозначному и округлому числу."
                 guide6 "Ну-с, для начала давай разберемся с начальным интерфейсом. Чтобы перейти на карту города/школы тебе всего-то нужно нажать на иконку телефона, а после вот на эту иконочку: {image=phone/gps_idle.png}"
                 guide2 "Другие же элементы телефона это звонки, СМС, а также простейшие настройки игры!"
                 scene image "character/guide/screenshot/map.png"
                 guide1 "Открыв карту города/школы ты можешь видеть разные локации, на которые можно перейти!"
                 guide1 "К примеру, придя в торговый центр, ты можешь зайти в магазин манги, продуктовый, в котором, кстати, можно устроиться на работу, а если ты пойдешь в парк, то можешь устроить пробежку своему игровому персонажу!"
                 guide1 "Каждое твое действие дает персонажу что-то: деньги, атрибуты, перки. К примеру, учась в школе, ты будешь получать интеллект. Бегая по парку, выносливость и ловкость. Также, если заниматься дома с собственным весом, ты будешь качать силу."
                 guide4 "Все эти действия ты можешь найти в правом баре, под иконкой действие, конечно, кроме обучения. Чтобы начался урок, ты должен быть в классе в 8 часов, 10 часов, 12 часов, а также в 14 часов!"
                 guide1 "Любое твое действие прокачивает единый параметр - скорость обучение, который влияет уже на то, как быстро ты будешь получать прибавку к тому или иному атрибуту."
                 guide1 "Все просто, так ведь?"
                 guide9 "И... Чуть не забыла!"
                 scene image "character/guide/screenshot/locationp.png"
                 guide4 "Чтобы перемещаться межлокационно, тебе нужно нажать в правом баре на перемещение, находящееся в близости с НПС на локации и действиями."
                 guide3 "Ох... Осталось рассказать о мелочи, но по словам разработчиков эту мелочь игроки гиперболизировали до такой степени, что она воплотилась в глобальные жалобы с их стороны: в чем цель игры?"
                 guide5 "Если говорить по правде, то я и сама не знаю!"
                 guide1 "Шучу! Цель игры проста и понятна: окончить школу и обеспечить приемлимым будущим своего персонажа: будешь ли ты хулиганьем, которое перерастет свой спермотоксикоз и станет достойной ячейкой общества"
                 guide1 "А может и не перерастет, став мафиози и без того в захудалом криминальном городишке. Возможно ты решишь стать примерным учеником, который в будущем станет офисным планктоном..."
                 guide3 "Не лучшее будущее, но все же..."
                 guide4 "Если подытожить все вышесказанное, то ты можешь стать кем угодно. Твои выборы - будущее твоего персонажа, а уже эти выборы напрямую завязаны на РПГ системе, которая может ограничивать твои рвения, но также может и помочь!"
                 guide1 "Все очень и очень просто, так ведь? Главное не помереть раньше времени!"
                 guide3 "Упс, я на тебя потратила уже достаточно много времени! Мне нужно помочь и другим людям в консультации!"
                 guide4 "Еще увидимся, игрок!"
                 $ help = 1
                 $ help_club = 1
                 $ help_computer = 1
                 $ help_school = 1
                 $ help_fight = 1
                 $ help_class = 1
                 $ help_occult = 1
                 $ help_joob_magazine = 1
                 $ help_suzuki = 1
                 scene bf
                 jump titre
             "{color=#000000}Да кому вообще нужны эти обучения?{/color}":
                 guide3 "Ну, как хочешь. Мое дело предложить, а твое дело отказаться."
                 $ help_computer = 0
                 $ help_club = 0
                 $ help_school = 0
                 $ help_fight = 0
                 $ help_class = 0
                 $ help_occult = 0
                 $ help_joob_magazine = 0
                 $ help_suzuki = 0
                 scene bf
                 jump titre
label titre:
     $ ivent_product_1 = 1
     $ warn_joob = 0
     $ reputation_joob = 0
     $ page = 1
     $ price = 0
     $ manga1_1 = 0
     $ manga1_2 = 0
     $ manga1_3 = 0
     $ manga1_info = 1
     if port == 1:
         scene bf
         $ renpy.pause(1.0, hard=True)
         show text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}Sloths Command представляет...{/b}{/font}{/size}{/color}" with dissolve
         $ renpy.pause(3.0, hard=True)
         hide text with dissolve
         $ renpy.pause(1.0, hard=True)
         show text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}School G...{/b}" with dissolve
         show ayso g8
         $ renpy.pause(1.0, hard=True)
         guide8 "Кайто, ты придурок? На кой здесь эти надписи в стиле голливудских боевиков?!" with vpunch
         "Извини..."
         show ayso g7
         guide7 "Когда-нибудь ты точно всех доконаешь... Женатый парень за тридцать, а все еще занимается непонятно чем!"
         hide text with dissolve
         $ renpy.pause(1.0, hard=True)
         jump home1
     elif port == 0:
         scene bf
         $ renpy.pause(1.0, hard=True)
         show text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}Sloths Command представляет...{/b}{/font}{/size}{/color}" with dissolve
         $ renpy.pause(3.0, hard=True)
         hide text with dissolve
         $ renpy.pause(1.0, hard=True)
         show text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}School G...{/b}{/font}{/size}{/color}" with dissolve
         $ renpy.pause(1.0, hard=True)
         guide8 "Кайто, ты придурок? На кой здесь эти надписи в стиле голливудских боевиков?!" with vpunch
         "Извини..."
         guide7 "Когда-нибудь ты точно всех доконаешь... Женатый парень за тридцать, а все еще занимается непонятно чем!"
         hide text with dissolve
         $ renpy.pause(1.0, hard=True)
         jump home1
label guide1:
     if port == 0:
         if help_computer == 1 and gg == 11:
             scene screenshotcomputer
             guide5 "Привет тебе вновь, друг мой! Не ожидал меня увидеть, да?"
             guide1 "Ну ничего, ты привыкнешь к моим внезапным появлениям! В конце концов тебе терпеть мой трёп придется на протяжении всей игры!"
             guide4 "Ты же рад, верно?"
             guide1 "Ну да ладно, давай разбираться с возможностями компьютера вместе! Как можно было понять по иконкам, у компьютера в данной игре куча возможностей!"
             guide1 "Через него можно искать работу, программировать, зарабатывая деньги и прокачивая тем самым интеллект, а еще здесь посмотреть статистику и заниматься другими интересными вещичками!"
             guide1 "Эта приблуда хороша всем, а еще ее можно делать более мощной, чтобы открывать новые функции!"
             guide1 "Упс, похоже мое время вновь закончилось! Удачи тебе просматривать все его возможности вручную, а я пошла заниматься своими делами!"
             $ help_computer = 0
             $ help += 1
             jump computer
         if help_school == 1 and gg == 1:
             scene screenshotschool
             guide5 "Не ожидал, да? А я появилась!"
             guide1 "На самом деле я даже не совсем понимаю зачем, но, похоже, так надо. Погоди секунду, мне нужно вспомнить, зачем я здесь..."
             guide11 "..."
             guide11 ".."
             guide11 "."
             guide10 "Я забыла и не могу вспомнить! Он меня убьет, если узнает!"
             "Что узнаю?"
             guide10 "Не важно! Нет, это не важно! НЕТ, НЕТ, НЕТ!"
             "Ты опять забыла, что нужно говорить?"
             guide9 "Да..."
             "В школу можно зайти..."
             guide12 "Точно! В школу можно зайти, если помнишь, через меню передвижение!"
             guide13 "Я справилась, так что теперь мне можно идти отсюда..."
             guide5 "Встретимся потом, игрок!"
             $ help_school = 0
             $ help += 1
             jump school
         if help_fight == 1 and gg == 16:
             guide9 "Ой-ёй! Как ты попал в такую передрягу?! Это же плохо!"
             guide5 "Ха-ха, похоже вместе с тобой побьют и меня, если я не объясню, что тут надо делать!"
             guide12 "Бей с ноги в лицо! Нет... Нужен прямой хук в челюсть, выруби противника! НЕТ, НЕТ, НЕТ, лучше сделай ему подсечку! Пусть знает наших!"
             "В общем и в целом она права. Удар в разные части тела и вид удара - все это зависит на шанс нокдауна, урон, уклонение и другие статы, которые вы могли видеть в таблице."
             "Чем выше ловкость - тем выше шанс нокдауна и урон с ноги, а чем выше сила - тем выше урон общий. От ловкости идет умножитель урона при ударе с ноги. Лучший вид боевых статов - комбинирование, хотя все и зависит от стиля боя человека."
             guide5 "Дай я договорю! Я тоже хочу поумничать!"
             "Валяй"
             guide1 "Если вы не хотите получать оплеухи, то ловкость ваше все, а если вы хотите бить, чтобы ребра ломались - сила ваш выбор. Но не забывайте, что при ударе с ноги повышается и шанс нокдауна."
             guide1 "Вы должны учитывать множество факторов, чтобы добиться идеального для вас решения. Заканчивать ли все бои нокдаунами или сломанными костями со стороны противника... А может вы хотите быть чуть ли не бессмертным!"
             guide1 "Все на ваш вкус и цвет!"
             guide12 "Я хорошо справилась со своей задачей консультанта?"
             menu:
                 "{color=#000000}Да{/color}":
                     guide5 "Спасибо, я старалась!"
                 "{color=#000000}Нет{/color}":
                     guide9 "Бука!"
             $ help_fight = 0
             jump start3
         if occult_club == 2 and help_occult == 1:
             guide1 "Странная девушка, да?"
             guide1 "Не волнуйся, ты всегда ее можешь как отшить, так и заромансить. Такова политика игры: делай то, что ты хочешь!"
             guide13 "И эта политика мне не нравится..."
             guide7 "Полигамисты... Бр..."
             guide8 "Даже страшно думать о них"
             guide5 "Но в любом случае все зависит от твоих выборов, как и было сказано ранее!"
             "Может ты начнешь говорить уже по теме?"
             guide9 "Извини!"
             guide1 "В общем, открой анкету, когда решишься вступить в клуб! Она находится в рюкзаке. После нажми на нее, будучи у ворот в школу и все. Ты числишься в клубе!"
             guide5 "Опять время... Пока, игрок! Увидимся еще!"
             $ help_occult = 0
             jump school1
         if help_club == 1 and guide_club == 1:
             guide1 "Привет-привет, новенький клубный деятель. Как дела? Всех привидений поймал?"
             guide3 "Ну или что там делают в клубе оккультизма..."
             guide1 "Ну да не важно. В любом случае я здесь, чтобы объяснить тебе, что это за клубы такие и с чем их едят!"
             guide1 "А это, наверное, самая интересная для меня часть игры! В конце концов именно в них можно поймать неплохие ивенты с долей юмора, а может даже и романтики с атмосферой трагедии..."
             guide1 "Развивай клуб и достигни высот с людьми, что тебя окружают! Возможно это и будет обычным убиванием времени со стороны твоего персонажа, но это же круто! В конце концов ты сможешь окончить школу,"
             guide1 "а у других останутся приятные воспоминания о твоем похождении! Кто ж знает, что произойдет в будущем: походы на пляжи, романтика, а может... Вражда, перемешанная с постоянными междусобицами!"
             guide12 "А может ты и вовсе забьешь на все эти клубы, став президентом студ.совета и изменив школу навсегда в лучшую или же худшую сторону!"
             "Может хватит уже говорить не по теме? Какой уже раз!"
             guide9 "Извини!"
             guide11 "Чтобы попасть в клубную комнату, тебе нужно нажать на ПКМ и на кнопочку, которую ты сразу увидишь, но делать это нужно именно в школе! Дальше ты попадешь в клубную комнату и..."
             guide4 "И да, когда увидишь систему микроменеджмента - не пугайся! Главное запомни, что пользоваться всем этим делом ты сможешь, но пройдя ветку событий со студенческим советом и достигнув 80 очков отношений с Аяно!"
             guide3 "А... Мне снова пора... Извини!"
             $ guide_club = 0
             $ help_club = 0
             jump check_location
     if port == 1:
         if help_computer == 1 and gg == 11:
             scene screenshotcomputer
             show ayso g5
             guide5 "Привет тебе вновь, друг мой! Не ожидал меня увидеть, да?"
             show ayso g1
             guide1 "Ну ничего, ты привыкнешь к моим внезапным появлениям! В конце концов тебе терпеть мой трёп придется на протяжении всей игры!"
             show ayso g4
             guide4 "Ты же рад, верно?"
             show ayso g1
             guide1 "Ну да ладно, давай разбираться с возможностями компьютера вместе! Как можно было понять по иконкам, у компьютера в данной игре куча возможностей!"
             guide1 "Через него можно искать работу, программировать, зарабатывая деньги и прокачивая тем самым интеллект, а еще здесь можно купить смартфон, посмотреть статистику и заниматься другими интересными вещичками!"
             show ayso g5
             guide5 "Тут даже есть чат! Ты сможешь переписываться со своими новыми друзьями со школы, а может и девушкой, если она у тебя появилась!"
             show ayso g1
             guide1 "Эта приблуда хороша всем, а еще ее можно делать более мощной, чтобы открывать новые функции!"
             guide1 "Упс, похоже мое время вновь закончилось! Удачи тебе просматривать все его возможности вручную, а я пошла заниматься своими делами!"
             $ help_computer = 0
             $ help += 1
             jump computer
         if help_school == 1 and gg == 1:
             scene screenshotschool
             show ayso g5
             guide5 "Не ожидал, да? А я появилась!"
             show ayso g1
             guide1 "На самом деле я даже не совсем понимаю зачем, но, похоже, так надо. Погоди секунду, мне нужно вспомнить, зачем я здесь..."
             show ayso g11
             guide11 "..."
             guide11 ".."
             guide11 "."
             show ayso g10
             guide10 "Я забыла и не могу вспомнить! Он меня убьет, если узнает!"
             "Что узнаю?"
             guide10 "Не важно! Нет, это не важно! НЕТ, НЕТ, НЕТ!"
             "Ты опять забыла, что нужно говорить?"
             show ayso g9
             guide9 "Да..."
             "В школу можно зайти..."
             show ayso g12
             guide12 "Точно! В школу можно зайти, если нажать на дорожку, которая ведет к этой самой школе!"
             show ayso g13
             guide13 "Я справилась, так что теперь мне можно идти отсюда..."
             show ayso g5
             guide5 "Встретимся потом, игрок!"
             $ help_school = 0
             $ help += 1
             jump school
         if help_fight == 1 and gg == 16:
             show ayso g9
             guide9 "Ой-ёй! Как ты попал в такую передрягу?! Это же плохо!"
             show ayso g5
             guide5 "Ха-ха, похоже вместе с тобой побьют и меня, если я не объясню, что тут надо делать!"
             show ayso g12
             guide12 "Бей с ноги в лицо! Нет... Нужен прямой хук в челюсть, выруби противника! НЕТ, НЕТ, НЕТ, лучше сделай ему подсечку! Пусть знает наших!"
             "В общем и в целом она права. Удар в разные части тела и вид удара - все это зависит на шанс нокдауна, урон, уклонение и другие статы, которые вы могли видеть в таблице."
             "Чем выше ловкость - тем выше шанс нокдауна и урон с ноги, а чем выше сила - тем выше урон общий. От ловкости идет умножитель урона при ударе с ноги. Лучший вид боевых статов - комбинирование, хотя все и зависит от стиля боя человека."
             show ayso g5
             guide5 "Дай я договорю! Я тоже хочу поумничать!"
             "Валяй"
             show ayso g1
             guide1 "Если вы не хотите получать оплеухи, то ловкость ваше все, а если вы хотите бить, чтобы ребра ломались - сила ваш выбор. Но не забывайте, что при ударе с ноги повышается и шанс нокдауна."
             guide1 "Вы должны учитывать множество факторов, чтобы добиться идеального для вас решения. Заканчивать ли все бои нокдаунами или сломанными костями со стороны противника... А может вы хотите быть чуть ли не бессмертным!"
             guide1 "Все на ваш вкус и цвет!"
             show ayso g12
             guide12 "Я хорошо справилась со своей задачей консультанта?"
             menu:
                 "{color=#000000}Да{/color}":
                     show ayso g5
                     guide5 "Спасибо, я старалась!"
                 "{color=#000000}Нет{/color}":
                     show ayso g9
                     guide9 "Бака!"
             $ help_fight = 0
             jump start3
         if occult_club == 2 and help_occult == 1:
             show ayso g1
             guide1 "Странная девушка, да?"
             guide1 "Не волнуйся, ты всегда ее можешь как отшить, так и заромансить. Такова политика игры: делай то, что ты хочешь!"
             show ayso g13
             guide13 "И эта политика мне не нравится..."
             show ayso g7
             guide7 "Полигамисты... Бр..."
             show ayso g8
             guide8 "Даже страшно думать о них."
             show ayso g5
             guide5 "Но в любом случае все зависит от твоих выборов, как и было сказано ранее!"
             "Может ты начнешь говорить уже по теме?"
             show ayso g9
             guide9 "Извини!"
             show ayso g1
             guide1 "В общем, открой анкету, когда решишься вступить в клуб! Она находится в рюкзаке. После нажми на нее, будучи у ворот школы и все. Ты числишься в клубе!"
             "Иди отдыхай"
             show ayso g5
             guide5 "Опять время... Пока, игрок! Увидимся еще!"
             $ help_occult = 0
             jump school1
         if help_club == 1 and guide_club == 1:
             show ayso g1
             guide1 "Привет-привет, новенький клубный деятель. Как дела? Всех привидений поймал?"
             show ayso g3
             guide3 "Ну или что там делают в клубе оккультизма..."
             show ayso g1
             guide1 "Ну да не важно. В любом случае я здесь, чтобы объяснить тебе, что это за клубы такие и с чем их едят!"
             guide1 "А это, наверное, самая интересная для меня часть игры! В конце концов именно в них можно поймать неплохие ивенты с долей юмора, а может даже и романтики с атмосферой трагедии..."
             guide1 "Развивай клуб и достигни высот с людьми, что тебя окружают! Возможно это и будет обычным убиванием времени со стороны твоего персонажа, но это же круто! В конце концов ты сможешь окончить школу,"
             guide1 "а у других останутся приятные воспоминания о твоем похождении! Кто ж знает, что произойдет в будущем: походы на пляжи, романтика, а может... Вражда, перемешанная с постоянными междусобицами!"
             show ayso g12
             guide12 "А может ты и вовсе забьешь на все эти клубы, став президентом студ.совета и изменив школу навсегда в лучшую или же худшую сторону!"
             "Может хватит уже говорить не по теме? Какой уже раз!"
             show ayso g9
             guide9 "Извини!"
             show ayso g11
             guide11 "Чтобы попасть в клубную комнату, тебе нужно нажать на иконку и на кнопочку, которую ты сразу увидишь, но делать это нужно именно в школе! Дальше ты попадешь в клубную комнату и..."
             show ayso g12
             guide12 "Будешь заниматься клубной повседневностью! Главное запомни: Н/О/О - нужные очки отношений, а Н/О/Д - нужные очки доверия."
             show ayso g3
             guide3 "А... Мне снова пора... Извини!"
             $ guide_club = 0
             $ help_club = 0
             jump check_location
