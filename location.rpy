label home1:
     if Lite_Mode == 1:
         $ stats_forces_gg += 40
         $ stats_agility_gg += 40
         $ stats_stamina_gg += 40
         $ stats_science_gg += 40
         $ stats_cunning_gg += 40
         $ stats_authority_gg += 40
         $ stats_erudition_gg += 40
         $ stats_lucky_gg += 40
         $ money += 10000
     $ progress_science_need = 0
     $ v_mat = 0
     $ mat = 0
     $ run = 0
     $ stats_authority_gg += dop_stats_authority_gg
     $ progress_agility = 0
     $ progress_stamina = 0
     $ stats_authority_gg_info = stats_authority_gg + dop_stats_authority_gg
     $ stats_forces_gg_info = stats_forces_gg + dop_stats_forces_gg
     $ stats_lucky_gg_info = stats_lucky_gg + dop_stats_lucky_gg
     $ stats_stamina_gg_info = stats_stamina_gg + dop_stats_stamina_gg
     $ standart_mod_attack_gg = 20
     $ damage_gg = stats_forces_gg / 2 + standart_mod_attack_gg
     $ damage_gg_info = dop_damage_gg + damage_gg
     $ points_hp_gg = 100 + (stats_stamina_gg / 2)
     $ poins_hp_max_gg = points_hp_gg
     $ mod_speed_attack_gg = 100
     $ speed_attack_gg = float(mod_speed_attack_gg) / 4 / stats_agility_gg
     $ speed_attack_info = round(speed_attack_gg, 2)
     $ standart_mod_attack_gg = 20
     $ damage_gg = stats_forces_gg / 2 + standart_mod_attack_gg
     $ block_damage_gg = 100 / (stats_stamina_gg / 2)
     $ block_damage_info = 100 / int(block_damage_gg)
     $ miss_chance_gg = 100 / (stats_agility_gg / 2)
     $ miss_chance_info = 100/miss_chance_gg
     $ accuracy_gg = 100 / float(stats_agility_gg / 4)
     $ accuracy_info = 100 / int(accuracy_gg)
     $ punch_gg = float(2.5) / speed_attack_gg
     $ knockdown_gg = 100 / float(stats_forces_gg / 6)
     $ knockdown_info = 100 / int(knockdown_gg)
     $ critical_damage_gg = 100 / float(stats_lucky_gg / 4)
     $ critical_damage_info = 100 / int(critical_damage_gg)
     $ speed_education = 9 + stats_science_gg / 3
     $ larceny = 9 + (stats_cunning_gg + stats_agility_gg + stats_lucky_gg) / 10
     $ movement_speed = 7 + (stats_stamina_gg + stats_agility_gg) / 5
     $ app = (stats_erudition_gg + stats_science_gg) / 5
     $ app_info = app + dop_app
     $ mod_horror = abs(stats_forces_gg + stats_agility_gg) / 5 - app
     $ games_chance = 7 + (stats_lucky_gg + stats_cunning_gg) / 5
     $ charisma = (stats_science_gg / 10) + (stats_erudition_gg / 2) + (stats_cunning_gg / 2) + (app / 4) - 9
     $ occult_club = 1
     $ lessons_per_day = 0
     $ absenteeism = 0
     $ absenteeism_joob = 0
     $ open_number = 1
     $ name_days = {"1":"Пн", "2":"Вт", "3":"Ср", "4":"Чт", "5":"Пт", "6":"Сб", "7":"Вс"}
     $ energy = 80 + int(stats_stamina_gg_info / 1.5)
     $ pich_number = 0
     stop music fadeout 1
     $ renpy.pause(1.0, hard=True)
     queue music [ "music/8.mp3", "music/2.mp3", "music/5.mp3" ]
     $ config.overlay_functions.append(time1)
     $ time_start = 1
     $ old_dialoge = 0
     python:
         location_school = ['school_class', 'join_school', 'corridor_school', 'roof', 'canteen', 'pool']
         location_city = ['park', 'shopping_center']
         for number_npc in range(1, number_npc_max):
             npc_id = 'npc'+str(number_npc)
             club_npc = eval(npc_id)['club_npc']
             npc_nature = eval(npc_id)["npc_nature"]
             if days <= 5:
                 if hour <= 16:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         if hour <= 7:
                             location_npc = 'apartament'
                         elif hour == 8 or hour == 10 or hour == 12 or hour == 14:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= 60:
                                 location_npc = 'school_class'
                             elif location_npc <= 85:
                                 location_npc = 'pool'
                             else:
                                 location_npc = renpy.random.randint(1, 100)
                                 if location_npc <= active_npc * 15:
                                     location_npc = renpy.random.choice(location_school)
                                 else:
                                     location_npc = location_npc
                         elif hour == 9 or hour == 11 or hour == 13 or hour == 15:
                             if location_npc <= 42:
                                 location_npc = 'canteen'
                             elif location_npc <= 62:
                                 location_npc = 'school_class'
                             else:
                                 location_npc = renpy.random.randint(1, 100)
                                 if location_npc <= active_npc * 15:
                                     location_npc = renpy.random.choice(location_school)
                                 else:
                                     location_npc = location_npc
                             if club_npc == 7:
                                 location_npc = 'occult_club'
                         else:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                     else:
                         if hour == 8 or hour == 10 or hour == 12 or hour == 14:
                             location_npc = renpy.random.choice(location_school)
                             if location_npc >= 70:
                                 location_npc = 'school_class'
                             elif location_npc >= 60:
                                 location_npc = 'pool'
                             else:
                                 location_npc = renpy.random.randint(1, 100)
                                 if location_npc <= active_npc * 15:
                                     location_npc = renpy.random.choice(location_school)
                                 else:
                                     location_npc = location_npc
                                 if club_npc == 7:
                                     location_npc = 'occult_club'
                         elif hour == 9 or hour == 11 or hour == 13 or hour == 15:
                             if location_npc <= 12:
                                 location_npc = 'canteen'
                             elif location_npc <= 32:
                                 location_npc = 'school_class'
                             elif location_npc <= 72:
                                 location_npc = 'roof'
                             else:
                                 location_npc = renpy.random.randint(1, 100)
                                 if location_npc <= active_npc * 15:
                                     location_npc = renpy.random.choice(location_school)
                                 else:
                                     location_npc = location_npc
                             if club_npc == 7:
                                 location_npc = 'occult_club'
                         else:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                 elif hour <= 18:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         if hour == 8 or hour == 10 or hour == 12 or hour == 14:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                         else:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                     else:
                         if hour == 8 or hour == 10 or hour == 12 or hour == 14:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                         else:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 5:
                                 location_npc = renpy.random.choice(location_city)
                             elif location_npc >= 100 - active_npc * 5:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                     if club_npc == 7:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc <= 90:
                             location_npc = 'occult_club'
                 elif hour <= 20:
                     location_npc = renpy.random.randint(1, 100)
                     if location_npc <= active_npc * 10:
                         location_npc = renpy.random.choice(location_city)
                     else:
                         location_npc = location_npc
                     if club_npc == 7:
                         if location_npc <= 70:
                             location_npc = 'occult_club'
                 else:
                     location_npc = renpy.random.randint(1, 100)
                     if location_npc <= active_npc * 10:
                         location_npc = renpy.random.choice(location_city)
                     else:
                         location_npc = location_npc
                 eval(npc_id)["location_npc"] = location_npc
             else:
                 if hour <= 6:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 95:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     else:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 70:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     eval(npc_id)["location_npc"] = location_npc
                 elif hour <= 10:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 75:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     else:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 60:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     eval(npc_id)["location_npc"] = location_npc
                 elif hour <= 18:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 30:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     else:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 30:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     eval(npc_id)["location_npc"] = location_npc
                 elif hour <= 20:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 50:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     else:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 40:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     eval(npc_id)["location_npc"] = location_npc
                 elif hour >= 21:
                     if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 85:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     else:
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 70:
                             location_npc = renpy.random.choice(location_city)
                         else:
                             location_npc = 'apartament'
                     eval(npc_id)["location_npc"] = location_npc
             eval(npc_id)["location_npc"] = location_npc
     $ gg = 5
     jump check_location
label search_npc:
     $ number_npc = renpy.input("Введите ID персонажа, которого хотите найти.", default =_("1"), allow="1234567890", length=3)
     $ number_npc = number_npc.strip()
     python:
         number_npc = int(number_npc)
     if number_npc <= 0 or number_npc >= number_npc_max:
         "ID персонажа не найден."
         jump search_npc
     python:
         npc_id = 'npc'+str(number_npc)
         club_npc = eval(npc_id)['club_npc']
         name_npc = eval(npc_id)["npc_name"]
         fam_npc = eval(npc_id)["npc_fam"]
         v_npc = eval(npc_id)["pich_npc"]
         gender_npc = eval(npc_id)["gender_npc"]
         contact_npc = eval(npc_id)["contact_npc"]
         love_npc = eval(npc_id)["love_npc"]
         fear_npc = eval(npc_id)["fear_npc"]
         number_phone = eval(npc_id)['number_phone']
         squeeze = eval(npc_id)["squeeze"]
         npc_nature = eval(npc_id)["npc_nature"]
         id_npc = eval(npc_id)["id_npc"]
         club_npc = eval(npc_id)['club_npc']
         student_soviet_g_npc = eval(npc_id)["student_soviet_g_npc"]
     jump npc
label tz:
     scene black
     "Данная локация в разработке"
     jump map_city
screen inventory_p:
     $ heft_cigarette = (2.5 + cigarette * 1) / 1000
     $ heft_cola = 0.5 * cola
     $ heft_rolton = 0.2 * rolton
     $ heft_heal = 1 * heal
     $ heft_candy = 0.3 * candy
     $ heft_zhiga = (11.5 * zhiga) / 1000
     $ heft_character = heft_cigarette + heft_cola + heft_rolton + heft_heal + heft_candy + heft_zhiga
     $ heft_character_max = (stats_stamina_gg + stats_forces_gg) / 10
     if heft_character > heft_character_max:
         text "Вы ходите с максимально доступным весом, отчего на данный момент передвижение по карте будет заблокировано ровно до тех пор, пока вы не освободите место в инвентаре."
screen map_city:
     modal True
     if gg <= 4:
         if hour <= 6 or hour >= 21:
             timer 0.01 repeat True action Jump('map_city')
     imagemap:
         alpha False
         if hour <= 3:
             ground "map/map_city/map_city_night.jpg"
         elif hour <= 7:
             ground "map/map_city/map_city_v.jpg"
         elif hour <= 16:
             ground "map/map_city/map_city_ut.jpg"
         elif hour <= 19:
             ground "map/map_city/map_city_v.jpg"
         elif hour <= 24:
             ground "map/map_city/map_city_night.jpg"
         hover "map/map_city/map_city_ut_hover.png"
         hotspot (1129, 371, 788, 356):
             hovered SetVariable("menu_loc", 2)
             unhovered SetVariable("menu_loc", 0)
             action Jump('home')
         hotspot (452, 586, 303, 370):
             hovered SetVariable("menu_loc", 3)
             unhovered SetVariable("menu_loc", 0)
             action Jump('shopping_center')
         hotspot (889, 725, 269, 293):
             hovered SetVariable("menu_loc", 4)
             unhovered SetVariable("menu_loc", 0)
             action Jump('park1')
         hotspot (0, 163, 1113, 328):
             hovered SetVariable("menu_loc", 5)
             unhovered SetVariable("menu_loc", 0)
             action Jump('map_city')
     frame xalign 0.28 yalign 0.55:
         textbutton "Торговый центр":
             hovered SetVariable("menu_loc", 3)
             unhovered SetVariable("menu_loc", 0)
             action Jump('shopping_center')
     frame xalign 0.87 yalign 0.37:
         textbutton "Место проживания":
             hovered SetVariable("menu_loc", 2)
             unhovered SetVariable("menu_loc", 0)
             action Jump('home')
     frame xalign 0.5 yalign 0.65:
         textbutton "Парк":
             hovered SetVariable("menu_loc", 4)
             unhovered SetVariable("menu_loc", 0)
             action Jump('park1')
     frame xalign 0.34 yalign 0.15:
         textbutton "Другая часть города":
             hovered SetVariable("menu_loc", 5)
             unhovered SetVariable("menu_loc", 0)
             action Jump('map_city')
     frame xalign 0.999 yalign 0:
         textbutton "Поиск персонажей" action Jump("search_npc")
     if menu_loc == 1:
         frame xalign 0.985 yalign 0.93:
             text "{size=30}{color=#000000}   Часы работы 07.00-20.00\nс понедельника по пятницу.{/color}{/size}"
     elif menu_loc == 2:
         frame xalign 0.97 yalign 0.29:
             text "{size=30}{color=#000000}Вы живете в квартире, которая находится\nсреди всех этих высоток.{/color}{/size}"
     elif menu_loc == 3:
         frame xalign 0.2 yalign 0.475:
             text "{size=30}{color=#000000}Огромное здание, имеющее кучу магазинов, потных людей,\nа также отсутствие комфорта для потенциального социофоба.{/color}{/size}"
     elif menu_loc == 4:
         frame xalign 0.5 yalign 0.59:
             text "{size=30}{color=#000000}Ночью лучше не гулять...{/color}{/size}"
     elif menu_loc == 5:
         frame xalign 0.34 yalign 0.1:
             text "{size=30}{color=#000000}На данный момент недоступно для посещения.{/color}{/size}"
     frame xalign 0.97 yalign 0.99:
         if days <= 5:
             if hour <= 6:
                 textbutton "План школы" xalign 0.97 yalign 0.99:
                     hovered SetVariable("menu_loc", 1)
                     unhovered SetVariable("menu_loc", 0)
                     action SetVariable("menu_loc", 1)
             elif hour <= 19:
                 textbutton "План школы" xalign 0.97 yalign 0.99:
                     hovered SetVariable("menu_loc", 1)
                     unhovered SetVariable("menu_loc", 0)
                     action Jump('map_school')
             elif hour >= 20:
                 textbutton "План школы" xalign 0.97 yalign 0.99:
                     hovered SetVariable("menu_loc", 1)
                     unhovered SetVariable("menu_loc", 0)
                     action SetVariable("menu_loc", 1)
         else:
             textbutton "План школы" xalign 0.97 yalign 0.99:
                 hovered SetVariable("menu_loc", 1)
                 unhovered SetVariable("menu_loc", 0)
                 action SetVariable("menu_loc", 1)
     frame xpos 75 yalign 0.07:
         text "{color=#000000}[money] кредитов{/color}"
     add im.Rotozoom("gui/frame4.png", 0, 1.3) xalign 0.02 yalign 0.01
     $ days_name = name_days[str(days)]
     if hour <= 9 and minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] 0[hour]:0[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     elif hour <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] 0[hour]:[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     elif minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] [hour]:0[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     else:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] [hour]:[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     frame xpos 10 yalign 0.12:
         text "{color=#000000}Уровень энергии: [energy]{/color}"
label map_school:
     if hour <= 6 or hour >= 21:
         jump map_city
     if hour <= 16:
         scene image "map/map_school/map_school_ut.jpg"
     else:
         scene image "map/map_school/map_school_v.jpg"
     if dialoge == 0 and dialoge >= 4:
         $ dialoge = 1
     $ heft_cigarette = (2.5 + cigarette * 1) / 1000
     $ heft_cola = 0.5 * cola
     $ heft_rolton = 0.2 * rolton
     $ heft_heal = 1 * heal
     $ heft_candy = 0.3 * candy
     $ heft_zhiga = (11.5 * zhiga) / 1000
     $ heft_character = heft_cigarette + heft_cola + heft_rolton + heft_heal + heft_candy + heft_zhiga
     $ heft_character_max = (stats_stamina_gg + stats_forces_gg) / 10
     if heft_character > heft_character_max:
         "Вы ходите с максимально доступным весом, отчего на данный момент передвижение по карте будет заблокировано ровно до тех пор, пока вы не освободите место в инвентаре."
         jump check_location
     if Lite_Mode == 0:
         if energy <= -30:
             "Будучи уже не в силах что-либо делать, вы вернулись обратно домой."
             jump home
         elif energy <= 10:
             "У вас мало энергии. Восстановите ее предметами или же другими способами."
     $ config.overlay_functions.append(time1)
     call screen map_school
screen map_school:
     if hour <= 16:
         imagemap:
             ground "map/map_school/map_school_ut.jpg"
             hover "map/map_school/map_school_ut_hover.jpg"
             hotspot (331, 290, 343, 159) action Jump('club')
             hotspot (678, 288, 307, 96) action SetVariable('menu_loc', 0), Jump('school')
             hotspot (1183, 509, 514, 109) action Jump('tz')
     elif hour <= 20:
         imagemap:
             ground "map/map_school/map_school_v.jpg"
             hover "map/map_school/map_school_v-hover.jpg"
             hotspot (331, 290, 343, 159) action Jump('club')
             hotspot (678, 288, 307, 96) action SetVariable('menu_loc', 0), Jump('school')
             hotspot (1183, 509, 514, 109) action Jump('tz')
     add im.Rotozoom("gui/frame.png", 0, 0.14) xalign 0.43 yalign 0.22
     textbutton "Школа" xalign 0.43 yalign 0.22 action SetVariable('menu_loc', 0), Jump('school')
     add im.Rotozoom("gui/frame2.png", 0, 0.16) xalign 0.195 yalign 0.25
     textbutton "Школьный клуб" xalign 0.2 yalign 0.25 action Jump('club')
     add im.Rotozoom("gui/frame2.png", 0, 0.16) xalign 0.99 yalign 0.99
     add im.Rotozoom("gui/frame2.png", 0, 0.16) xalign 0.99 yalign 0.99
     textbutton "План города" xalign 0.97 yalign 0.99 action Jump('map_city')
     add im.Rotozoom("gui/frame2.png", 0, 0.18) xalign 0.81 yalign 0.43
     textbutton "Теннисный корт {image=icons/icons_construct.png}" xalign 0.81 yalign 0.43 action Jump('tz')
     frame xpos 75 yalign 0.07:
         text "{color=#000000}[money] кредитов{/color}"
     add im.Rotozoom("gui/frame4.png", 0, 1.3) xalign 0.02 yalign 0.01
     $ days_name = name_days[str(days)]
     if hour <= 9 and minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] 0[hour]:0[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     elif hour <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] 0[hour]:[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     elif minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] [hour]:0[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     else:
         text "{font=gui/fonts/ubuntu.ttf}{color=#000000}[days_name] [hour]:[minute]{/color}{/font}" xalign 0.035 yalign 0.011 size 48
     frame xpos 10 yalign 0.12:
         text "{color=#000000}Уровень энергии: [energy]{/color}"
label stair_school:
     $ gg = 12
     $ pol_text_v = 0.01
     $ pol_text_z = 0.05
     if hour <= 16:
         scene stairs2
     else:
         scene stairs
     if hour == 8 or hour == 10 or hour == 12 or hour == 14:
         scene stairs1
     $ events_loc = renpy.random.randint(1, 10)
     if events_loc <= 2:
         if ivents_hooligans == 0:
             if language_game == 1:
                 "Спокойно прогуливаясь по школьным закоулкам, вы услышали странные звуки, исходящии из, как могло показаться, пустого класса. Никто и не обращал на них внимания, кроме вас. Возможно было слишком шумно, возможно они просто были равнодушны к подобным ситуациям."
                 "Так что мне нужно сделать?"
                 menu:
                     "{color=#000000}Зайти в класс{/color}":
                         stop music fadeout 1
                         $ renpy.pause(1.0, hard=True)
                         play music "music/3.mp3" fadeout 1 loop
                         scene xuligan_class
                         "Только зайдя в класс, вы увидели картину маслом: очередное проявление насилия со стороны школьных хулиганов. Теперь было понятно, почему никто не обращал внимания на звуки. И почему нынче люди так жестоки?"
                         "От мыслей вас отвлекло то, что школьник отлетел в стену и осел, размазывая cлёзы и жалобно хныкая. Было похоже, что он просто пушинка. Ну или хулиганы настолько сильны, что могли запросто отбросить человеческую тушу."
                         x2 "Мерзкий слизняк! Я говорил, что тебе будет только хуже!"
                         x3 "Дай ему!"
                         x1 "Надеюсь, что после этого урока ты поймёшь, что мы тут главные."
                         if larceny <= 20:
                             "Наконец заметив вас, хулиганы обернулись в вашу сторону, после чего один из них произнес."
                         else:
                             "Хулиганы не заметили, как вы вошли в класс, и продолжали азартно пинать свою жертву."
                         if stats_authority_gg_info <= 25:
                             x2 "Ага! Ещё один лошок на колотушки подбежал! Хватай его!"
                             $ xuligan_class = 1
                             jump start3
                         else:
                             x2 "Приветствую!"
                             menu:
                                 "{color=#000000}Поговорить с хулиганами{/color}":
                                     menu:
                                         "{color=#000000}Поддержать хулиганов{/color}":
                                             "Продолжайте, что ж вы стоите? - сказали вы, смотря на шпану, которая совершенно недавно развлекалась, избивая школьника."
                                             if stats_authority_gg_info <= 25:
                                                 x2 "Это точно... Хватайте этого недоноска!"
                                                 "Сказал один из хулиганов, указав пальцем на вас"
                                                 jump start3
                                             else:
                                                 "Хулиганы приветливо кивнули"
                                                 x2 "Поздорову, уважаемый. Пнёшь недоноска?"
                                                 menu:
                                                     "Да":
                                                         $ stats_authority_gg_info += 1
                                                         "Вы подошли к жертве и с удовольствием пнули её в живот, после чего хулиганы похлопали вас по спине и плечам."
                                                         x2 "Наш человек! Ну, мы с ним сами закончим. Не отвлекайся на нас."
                                                         "Дослушав слова одного из хулиганов, вы направились к выходу из класса"
                                                         "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
                                                     "Нет":
                                                         "Нет, вы тут уж без меня справляетесь, - сказали вы, смотря на одного из хулиганов, который, похоже, был их главарем."
                                                         x2 "Ну, дело твоё."
                                                         "Посмотрев еще немного на избиение, вы вышли из класса."
                                                 stop music fadeout 1
                                                 $ renpy.pause(1.0, hard=True)
                                                 queue music [ "music/5.mp3", "music/2.mp3" ]
                                         "{color=#000000}Поддержать жертву{/color}":
                                             if stats_erudition_gg <= 25:
                                                 "Немного осмыслив ситуацию, вы решили спасти свою жертву простой, но такой понятной фразой..."
                                                 "Я слышал, что директор по этажу ходит. Вы бы немного потише, - сказали вы, глядя на избитого школьника."
                                                 x2 "От души, уважаемый! Линяем!"
                                                 "Шпана дружно выскочила из кабинета, оставив вас наедине с жертвой."
                                                 menu:
                                                     "Пнуть слабака":
                                                         $ stats_authority_gg_info += 1
                                                         "Проходя мимо избитого, Вы услышали слабое cпасибо, но тут же пнули его в живот. Жертва, не ожидавшая такой подлости, потеряла дыхание.\nВсех, кто младше и слабей - не задумываясь бей! - произнесли вы, еще раз пнув грушу для битья, после выйдя с класса."
                                                         "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
                                                     "Помочь подняться":
                                                         "Вы подняли с пола избитую жертву и помогли дойти до умывальника, выслушивая горячие слова благодарности. Как только жертва отмыла кровавые сопли с лица, вы совместными усилиями привели её костюм в пристойный вид, после попрощавшись друг с другом."
                                                     "Уйти":
                                                         "Вы молча посмотрели на избитую жертву и вышли из класса. Тут каждый сам за себя. Он должен это понять."
                                                 stop music fadeout 1
                                                 $ renpy.pause(1.0, hard=True)
                                                 queue music [ "music/5.mp3", "music/2.mp3" ]
                                             else:
                                                 "Это... Ну... Не убейте его... - промямлили вы, так ничего и не придумав."
                                                 x2 "Не ссы! Не впервой! И не мешайся тут, если не помогаешь!"
                                                 "Пожав плечами, вы про себя подумали, что сделали все, что могли, после выйдя из злополучного класса."
                                                 stop music fadeout 1
                                                 $ renpy.pause(1.0, hard=True)
                                                 queue music [ "music/5.mp3", "music/2.mp3" ]
                                 "{color=#000000}Спокойно выйти из класса, не обращая внимания на избиение{/color}":
                                     if stats_authority_gg_info <= 30:
                                         x2 "Опа! А кто это тут такой борзый?! Хватай его!"
                                         jump start3
                                     else:
                                         "Озадаченно пожав плечами, хулиганы перебросили свое внимание на жертву, продолжая избивать ее. В это время вы спокойненько вышли из класса живыми и здоровыми."
                                         stop music fadeout 1
                                         $ renpy.pause(1.0, hard=True)
                                         queue music [ "music/5.mp3", "music/2.mp3" ]
                                 "{color=#000000}Кинуться в драку{/color}":
                                     $ xuligan_class = 1
                                     jump start3
                     "{color=#000000}А мне это надо?{/color}":
                         $ ivents_hooligans = 1
                         "Подумав, что оно вам и не надо, вы спокойно отдалились от класса и продолжили заниматься своими делами."
             elif language_game == 2:
                 "Walking quietly through the back streets of the school, you heard strange noises coming from what seemed to be an empty classroom. Nobody paid any attention to them except you. Maybe it was too noisy, maybe they were just indifferent to such situations."
                 "So what do I need to do?"
                 menu:
                     "Go to class":
                         scene xuligan_class
                         "Just when you entered class, you saw an oil painting: another manifestation of violence from school bullies. Now it was clear why no one paid attention to the sounds. And why are people so cruel now?"
                         "What distracted you from your thoughts was that the schoolboy flew into the wall and the donkey, smearing tears and whining miserably. It looked like he was just a fluff. Well, or the hooligans are so strong that they could easily throw away a human carcass."
                         x2 "Vile slug! I said that you will only get worse!"
                         x3 "Give him!"
                         x1 "I hope that after this lesson you will understand that we are in charge here."
                         if larceny <= 20:
                             "Finally spotting you, the hooligans turned in your direction, after which one of them spoke."
                         else:
                             "The hooligans did not notice how you entered the class, and continued to recklessly kick their victim."
                         if stats_authority_gg_info <= 25:
                             x2 "Yeah! Another loshka on the beater ran up! Grab it!"
                             $ xuligan_class = 1
                             jump start3
                         else:
                             x2 "Greetings!"
                             menu:
                                 "Talk to the Hooligans":
                                     menu:
                                         "Support the bullies":
                                             "Go on, why are you standing? - you said, looking at the bullies, who just recently had fun, beating a schoolboy."
                                             if stats_authority_gg_info <= 25:
                                                 x2 "That's for sure ... grab this jerk!"
                                                 "One of the hooligans said, pointing a finger at you."
                                                 jump start3
                                             else:
                                                 "Hooligans nodded affably"
                                                 x2 "Dear Pozdorov. Do you kick the little bastard?"
                                                 menu:
                                                     "Yes":
                                                         $ stats_authority_gg_info += 1
                                                         "You went to your stomach and went to your stomach with pleasure, after which the hooligans patted your back and shoulder."
                                                         x2 "Our man! Well, we will finish it ourselves. Do not be distracted by us."
                                                         "After hearing the words of one of the hooligans, you headed for the exit from the class"
                                                         "{color=#32CD32}Your authority level has increased!{/color}"
                                                     "No":
                                                         "No, you can do without me here, - you said, looking at one of the hooligans, who seemed to be their leader."
                                                         x2 "Well, your business."
                                                         "After looking a little more for the beating, you left the classroom."
                                         "Support the victim":
                                             if stats_erudition_gg <= 25:
                                                 "Having a little understanding of the situation, you decided to save your victim with a simple, but understandable phrase..."
                                                 "I heard the director of the floor is walking. You would be a little quieter, ”you said, looking at the battered schoolboy."
                                                 x2 "With all my heart, dear! Shedding!"
                                                 "Shpana amicably jumped out of the office, leaving you alone with the victim."
                                                 menu:
                                                     "Kick the wimp":
                                                         $ stats_authority_gg_info += 1
                                                         "Walking past a battered man, you heard a weak thank you, but then kicked him in the stomach. The victim, who did not expect such meanness, lost her breath.\nAll who are younger and weaker - do not hesitate to beat! - You said, once again kicking a punching bag after leaving class."
                                                         "{color=#32CD32}Your authority level has increased!{/color}"
                                                     "Help rise":
                                                         "You lifted a battered victim from the floor and helped get to the washbasin, hearing warm words of gratitude. As soon as the victim washed the bloody snot from her face, you brought her suit in decent shape, after saying goodbye to each other."
                                                     "Leave":
                                                         "You silently looked at the battered victim and left the classroom. Everyone here is for himself. He must understand this."
                                             else:
                                                 "This is ... Well ... Don’t kill him ... - you mumbled, without inventing anything. "
                                                 x2 "Do not piss! Not the first time! And do not interfere here if you do not help!"
                                                 "With a shrug, you thought to yourself that you did everything you could, after leaving the ill-fated class."
                                 "Quietly leave the classroom, ignoring the beating":
                                     if stats_authority_gg_info <= 30:
                                         x2 "Oops! Who the hell is this ?! Grab it!"
                                         jump start3
                                     else:
                                         "With a puzzled shrug, the hooligans turned their attention to the victim, continuing to beat her. At that time, you calmly left the classroom alive and well."
                                 "Rush into the fray":
                                     $ xuligan_class = 1
                                     jump start3
                     "Do I need this?":
                         $ ivents_hooligans = 1
                         "Thinking that you didn’t need it, you calmly moved away from the class and continued to do your own thing."
     if events_loc <= 4:
         if ivent_extortion == 0:
             if language_game == 1:
                 "Спокойно прогуливаясь по коридорам школы, вас остановила группа хулиганов, смотрящая на вас с ярко выраженным экономическим интересом. Не ожидая подобного, вы остановились возле них и зыркали, ожидая объяснений."
                 if stats_authority_gg_info >= 30:
                     x1 "А... Всё норм, проходи. Не тебя ждём."
                     $ ivent_extortion = 1
                 else:
                     x1 "Ну что?! Видишь, у меня дети голодные! А ну-ка проспонсируй им обед быстренько!"
                     menu:
                         "{color=#000000}Согласиться с его словами, отдав все свои деньги{/color}":
                             "Вы быстро выгребаете все свои деньги и отдаёте хулигану."
                             x1 "Вот! Сегодня детишки не умрут голодной смертью! И не забывай, они каждый день жрать хотят! Вали отсюда."
                             "После этих слов один из этой группы хулиганов оттолкнул вас в сторону, чтобы ваша тушка не мешалась их великому превосходительству."
                             $ ivent_extortion = 1
                             $ money = 0
                             $ stats_authority_gg_info -= 2
                             "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
                         "{color=#000000}Отказаться отдавать свои деньги{/color}":
                             if stats_erudition_gg >= 25:
                                 "Придётся вам голодать сегодня. Сюда директор направляется, ему на пайку скудную сейчас пожалуетесь, - сказали вы, спокойно обойдя группу хулиганов и идя дальше по своим делам."
                                 x1 "Мы с тобой потом разберемся! Хоть попробуй попасться на глаза!"
                                 $ ivent_extortion = 1
                                 $ stats_authority_gg_info += 1
                                 "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
                             else:
                                 "Ну... У меня нет денег, - сказали вы, так и не придумав ничего лучше."
                                 x1 "Позволь нам проверить твою честность!"
                                 menu:
                                     "{color=#000000}Позволить себя обыскать{/color}":
                                         "Хулиганы быстро вывернули ваши карманы."
                                         if money <= 0:
                                             x1 "Мда... Похоже у тебя действительно нет денег."
                                         elif money >= 1:
                                             x1 "Ну вот! А говорил, что пустой! Не ври дяденькам в следующий раз!"
                                         "После этих слов один из этой группы хулиганов оттолкнул вас в сторону, чтобы ваша тушка не мешалась их великому превосходительству."
                                         $ money = 0
                                         $ stats_authority_gg_info -= 2
                                         $ ivent_extortion = 1
                                         "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
                                     "{color=#000000}Отказаться{/color}":
                                         "После вашего отказа один из хулиганов схватил вас за шкирку и повел в школьный туалет. Дойдя до назначенного место, вас отпустили."
                                         scene toilet
                                         x1 "Молись, чтобы твои слова оказались правдой!"
                                         $ xuligan_class = 2
                                         jump start3
             elif language_game == 1:
                 "Walking calmly along the corridors of the school, a group of hooligans stopped you, looking at you with a pronounced economic interest. Not expecting this, you stopped near them and gawked, waiting for an explanation."
                 if stats_authority_gg_info >= 30:
                     x1 "Ah ... All right, come on in. We are not waiting for you."
                     $ ivent_extortion = 1
                 else:
                     x1 "Well?! You see, my children are hungry! Well, sponsor them lunch quickly!"
                     menu:
                         "Agree with his words, giving all your money":
                             "You quickly rake out all your money and give it to the bully."
                             x1 "Here! Today, kids will not die of starvation! And do not forget, they want to eat every day! Get out from here."
                             "After these words, one of this group of hooligans pushed you aside so that your carcass does not interfere with their great excellency."
                             $ ivent_extortion = 1
                             $ money = 0
                             $ stats_authority_gg_info -= 2
                             "{color=#FF0000}Your authority level has declined!{/color}"
                         "Refuse to give your money":
                             if stats_erudition_gg >= 25:
                                 "You have to starve today. The director goes here, you’ll complain about the poor ration, ”you said, calmly going around a group of hooligans and going further on your business."
                                 x1 "We will deal with you later! At least try to catch the eye!"
                                 $ ivent_extortion = 1
                                 $ stats_authority_gg_info += 1
                                 "{color=#32CD32}Your authority level has increased!{/color}"
                             else:
                                 "Well ... I don’t have money, you said, without having come up with anything better."
                                 x1 "Let us test your honesty!"
                                 menu:
                                     "Let yourself be searched":
                                         "Bullies quickly twisted your pockets."
                                         if money <= 0:
                                             x1 "Hmm ... Looks like you really have no money."
                                         elif money >= 1:
                                             x1 "Here you go! And he said that it was empty! Do not lie to uncles next time!"
                                         "After these words, one of this group of hooligans pushed you aside so that your carcass does not interfere with their great excellency."
                                         $ money = 0
                                         $ stats_authority_gg_info -= 2
                                         $ ivent_extortion = 1
                                         "{color=#FF0000}Your authority level has declined!{/color}"
                                     "Refuse":
                                         "After your refusal, one of the hooligans grabbed you by the collar and led you to the school toilet. Having reached the appointed place, you were released."
                                         scene toilet
                                         x1 "Pray for your words to be true!"
                                         $ xuligan_class = 2
                                         jump start3
     $ minute += 3
     call screen stair_school
screen stair_school:
     imagebutton xalign 0.99 yalign 0.24:
         idle ("icons/icons_backpack.png")
         hover ("icons/icons_backpack_hover.png")
         action Jump("backpack")
     imagebutton xalign 0.99 yalign 0.35:
         idle ("icons/icons_phone.png")
         hover ("icons/icons_phone_hover.png")
         action Jump("phone")
     imagebutton xalign 0.99 yalign 0.15:
         idle ("icons/icons_return_idle.png")
         hover ("icons/icons_return_hover.png")
         action Jump("school")
     imagebutton xalign 0.75 yalign 0.4:
         idle ("icons/icons_arrow.png")
         hover ("icons/icons_arrow_hover.png")
         action Jump("corridor")
     frame xpos 75 yalign 0.21:
         text "[money] кредитов"
     add im.Rotozoom("gui/frame4.png", 0, 1.3) xalign 0.02 yalign 0.15
     if hour <= 9 and minute <= 9:
         text "0[hour]:0[minute]" xalign 0.05 yalign 0.152 size 48
     elif hour <= 9:
         text "0[hour]:[minute]" xalign 0.05 yalign 0.152 size 48
     elif minute <= 9:
         text "[hour]:0[minute]" xalign 0.05 yalign 0.152 size 48
     else:
         text "[hour]:[minute]" xalign 0.05 yalign 0.152 size 48
     frame xpos 10 yalign 0.26:
         text "Уровень энергии: [energy]"
     add im.Rotozoom("gui/frame1.png", 0, 1):
         size (1920, 150)
     text "{size=26}{b}Школьная лестница: кто в локации?{/b}{/size}" xalign 0.5 yalign 0.01
     vpgrid:
         cols 5
         rows 10
         xalign 0.1 ypos 50 xysize (1920, 98)
         child_size (1920, 100)
         scrollbars "vertical"
         spacing 20 ###расстояние от порта до края изображе
         draggable True
         mousewheel True
         arrowkeys True
         for number_npc in range(1, number_npc_max):
             $ npc_id = 'npc'+str(number_npc)
             $ location_npc = eval(npc_id)["location_npc"]
             if location_npc == 'stair_school':
                 python:
                     npc_id = 'npc'+str(number_npc)
                     name_npc = eval(npc_id)["npc_name"]
                     fam_npc = eval(npc_id)["npc_fam"]
                     v_npc = eval(npc_id)["pich_npc"]
                     gender_npc = eval(npc_id)["gender_npc"]
                     contact_npc = eval(npc_id)["contact_npc"]
                     love_npc = eval(npc_id)["love_npc"]
                     fear_npc = eval(npc_id)["fear_npc"]
                 textbutton "{b}[number_npc].{/b} [name_npc] [fam_npc]":
                     action SetVariable('npc_id', npc_id), SetVariable('name_npc', name_npc), SetVariable('fam_npc', fam_npc), SetVariable('v_npc', v_npc), SetVariable('gender_npc', gender_npc), SetVariable('contact_npc', contact_npc), SetVariable('love_npc', love_npc), SetVariable('fear_npc', fear_npc), Jump('npc')
             python:
                 if hour == 8 or hour == 10 or hour == 12 or hour == 14:
                     location_npc = renpy.random.randint(1, 100)
                     if location_npc <= 50:
                         location_npc = 'school_class'
                         eval(npc_id)["location_npc"] = location_npc
label time2:
     if language_game == 1:
         if days == 1:
             "Сейчас [hour]:[minute], понедельник."
         if days == 2:
             "Сейчас [hour]:[minute], вторник"
         if days == 3:
             "Сейчас [hour]:[minute], среда."
         if days == 4:
             "Сейчас [hour]:[minute], четверг."
         if days == 5:
             "Сейчас [hour]:[minute], пятница"
         if days == 6:
             "Сейчас [hour]:[minute], суббота."
         if days == 7:
             "Сейчас [hour]:[minute], воскресенье."
     elif language_game == 2:
         if days == 1:
             "Now [hour]: [minute], Monday."
         if days == 2:
             "Now [hour]: [minute], Tuesday"
         if days == 3:
             "Now [hour]: [minute], Wednesday."
         if days == 4:
             "Now [hour]: [minute], Thursday."
         if days == 5:
             "Now [hour]: [minute], Friday"
         if days == 6:
             "Now [hour]: [minute], Saturday."
         if days == 7:
             "Now [hour]: [minute], Sunday."
     jump check_location
label mini_ivent_corridor_school:
     scene image "actions/school/corridor/corridor_ivent.jpg":
         size(1920, 1080)
     "Вашему взору предстала компания мило общающихся между собой девушек. Неспешно прогуливаясь по коридору и направляясь к лестнице, они успевали обсудить практически всё: кто-то рассказывал, как у неё прошёл день, что произошло нового, а кто-то попросту сплетничал, обсуждая со своими собеседниками новоиспеченную влюбленную парочку. Через пару минут они удалились на такое расстояние, с которого их речь уже была неразборчивой."
     jump ivent_no_corridor
label corridor:
     $ page = 0
     if dialoge == 0 or dialoge >= 4:
         $ dialoge = 1
     $ random_ivent = renpy.random.randint(1, 100)
     if hour >= 17:
         if random_ivent >= 80:
             python:
                 for number_npc in range(1, number_npc_max):
                     npc_id = 'npc'+str(number_npc)
                     npc_nature = eval(npc_id)["npc_nature"]
                     if npc_nature == 'Агрессивный':
                         location_npc = renpy.random.randint(1, 100)
                         if location_npc >= 50:
                             name_npc = eval(npc_id)["npc_name"]
                             fam_npc = eval(npc_id)["npc_fam"]
                             name_npc = str(name_npc)+' '+str(fam_npc)
                             renpy.jump('mini_ivent_corridor_school')
     label ivent_no_corridor:
     $ page = 0
     $ pol_text_v = 0.01
     $ pol_text_z = 0.05
     $ minute += 2
     $ gg = 2
     call screen corridor
screen corridor:
     if dialoge >= 4:
         $ dialoge = 1
     if hour <= 16:
         add "backgrounds/school/corridor.png"
     elif hour <= 19:
         add "backgrounds/school/corridor1.png"
     elif hour >= 20:
         add "backgrounds/school/corridor2.png"
     add "gui/system/podlozhka.png"
     if dialoge == 1:
         vpgrid:
             cols 1
             rows number_npc_max
             spacing -267
             xpos 1565 ypos 755 xysize (350, 310)
             child_size (350, 310)
             draggable True
             mousewheel True
             arrowkeys True
             scrollbars "vertical"
             for number_npc in range(1, number_npc_max):
                 $ npc_id = 'npc'+str(number_npc)
                 $ location_npc = eval(npc_id)["location_npc"]
                 if location_npc == 'corridor_school':
                     python:
                         npc_id = 'npc'+str(number_npc)
                         name_npc = eval(npc_id)["npc_name"]
                         fam_npc = eval(npc_id)["npc_fam"]
                         v_npc = eval(npc_id)["pich_npc"]
                         gender_npc = eval(npc_id)["gender_npc"]
                         contact_npc = eval(npc_id)["contact_npc"]
                         love_npc = eval(npc_id)["love_npc"]
                         fear_npc = eval(npc_id)["fear_npc"]
                     button:
                         if fear_npc >= 40:
                             add "gui/system/npc/enemy1_idle.png"
                             hover_background "gui/system/npc/enemy1_hover.png"
                         elif fear_npc >= 100:
                             add "gui/system/npc/enemy_idle.png"
                             hover_background "gui/system/npc/enemy_hover.png"
                         elif love_npc >= 50:
                             add "gui/system/npc/love_idle.png"
                             hover_background "gui/system/npc/love_hover.png"
                         elif love_npc >= 500:
                             add "gui/system/npc/love1_idle.png"
                             hover_background "gui/system/npc/love1_hover.png"
                         elif contact_npc <= 50:
                             add "gui/system/npc/stranger_idle.png"
                             hover_background "gui/system/npc/stranger_hover.png"
                         elif contact_npc <= 120:
                             add "gui/system/npc/buddy_idle.png"
                             hover_background "gui/system/npc/buddy_hover.png"
                         elif contact_npc >= 121:
                             add "gui/system/npc/friend_idle.png"
                             hover_background "gui/system/npc/friend_hover.png"
                         xpadding 0
                         ypadding 0
                         xmargin 5
                         ymargin 5
                         text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}[name_npc] [fam_npc]{/font}{/size}{/color}"
                         action SetVariable('npc_id', npc_id), SetVariable('name_npc', name_npc), SetVariable('fam_npc', fam_npc), SetVariable('v_npc', v_npc), SetVariable('gender_npc', gender_npc), SetVariable('contact_npc', contact_npc), SetVariable('love_npc', love_npc), SetVariable('fear_npc', fear_npc), Jump('npc')
     elif dialoge == 2:
         vpgrid:
             cols 1
             rows number_npc_max
             spacing -267
             xpos 1565 ypos 755 xysize (350, 310)
             child_size (350, 310)
             draggable True
             mousewheel True
             arrowkeys True
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/enemy1_idle.png"
                 hover_background "gui/system/npc/enemy1_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Промотать время{/font}{/size}{/color}"
                 action Jump('oz')
     elif dialoge == 3:
         vpgrid:
             cols 1
             rows number_npc_max
             spacing -267
             xpos 1565 ypos 755 xysize (350, 310)
             child_size (350, 310)
             scrollbars "vertical"
             draggable True
             mousewheel True
             arrowkeys True
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Школьный клуб{/font}{/size}{/color}"
                 action Jump('club')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Столовая{/font}{/size}{/color}"
                 action Jump('canteen')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Бассейн{/font}{/size}{/color}"
                 action Jump('pool')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Крыша{/font}{/size}{/color}"
                 action Jump('roof')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Студенческий совет{/font}{/size}{/color}"
                 action Jump('student_soviet')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Вход школы{/font}{/size}{/color}"
                 action Jump('school')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Школьный класс{/font}{/size}{/color}"
                 action Jump('class')
     imagemap:
         if dialoge == 1:
             ground "gui/system/v_npc_2.png" xpos 1585 yalign 0.67
             hotspot (0, 11, 52, 40):
                 action SetVariable('dialoge', 2)
             hotspot (264, 8, 73, 46):
                 action SetVariable('dialoge', 3)
         elif dialoge == 2:
             ground "gui/system/v_npc_1.png" xpos 1585 yalign 0.67
             hotspot (217, 5, 56, 50):
                 action SetVariable('dialoge', 1)
             hotspot (272, 4, 65, 55):
                 action SetVariable('dialoge', 3)
         elif dialoge == 3:
             ground "gui/system/v_npc_3.png" xpos 1585 yalign 0.67
             hotspot (0, 7, 51, 46):
                 action SetVariable('dialoge', 2)
             hotspot (50, 5, 49, 51):
                 action SetVariable('dialoge', 1)
     add "gui/system/menu.png"
     if page == 1:
         add "phone/phone.png" yalign 0.99
         imagebutton xalign 0.04 yalign 0.45 focus_mask True:
             idle (im.Rotozoom("phone/call_idle.png", 0, 1)) at button_phone
             action Show('call_phone_')
         imagebutton xalign 0.092 yalign 0.45 focus_mask True:
             idle (im.Rotozoom("phone/sms_idle.png", 0, 1)) at button_phone
             action Show('sms_phone_')
         imagebutton xalign 0.14 yalign 0.45 focus_mask True:
             idle (im.Rotozoom("phone/setting_idle.png", 0, 1)) at button_phone
             action ShowMenu("preferences")
         imagebutton xalign 0.092 yalign 0.55 focus_mask True:
             idle (im.Rotozoom("phone/gps_idle.png", 0, 1)) at button_phone
             action Show("maps")
         imagebutton xalign 0.002 ypos 920 focus_mask True:
             idle (im.Rotozoom("gui/system/icons/phone.png", 0, 1.4))
             hover (im.Rotozoom("gui/system/icons/phone_hover.png", 0, 1.4))
             action SetVariable ("page", 0)
     else:
         imagebutton xalign 0.002 ypos 920 focus_mask True:
             idle (im.Rotozoom("gui/system/icons/phone.png", 0, 1.4))
             hover (im.Rotozoom("gui/system/icons/phone_hover.png", 0, 1.4))
             action SetVariable ("page", 1)
     imagebutton xalign 0.065 ypos 920 focus_mask True:
         idle (im.Rotozoom("gui/system/icons/backpack.png", 0, 1.4))
         hover (im.Rotozoom("gui/system/icons/backpack_hover.png", 0, 1.4))
         action Show('backpack')
     $ days_name = name_days[str(days)]
     if hour <= 9 and minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=24}[days_name] 0[hour]:0[minute]{/size}{/font}" xalign 0.9645 yalign 0.9805 size 32
     elif hour <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=24}[days_name] 0[hour]:[minute]{/size}{/font}" xalign 0.9645 yalign 0.9805 size 32
     elif minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=24}[days_name] [hour]:0[minute]{/size}{/font}" xalign 0.9645 yalign 0.9805 size 32
     else:
         text "{font=gui/fonts/ubuntu.ttf}{size=24}[days_name] [hour]:[minute]{/size}{/font}" xalign 0.9645 yalign 0.9805 size 32
     text "{font=gui/fonts/ubuntu.ttf}[energy]{/font}" xalign 0.885 yalign 0.9805 size 24
     text "{font=gui/fonts/ubuntu.ttf}[money]{/font}" xalign 0.8 yalign 0.9805 size 24
label corridor1:
     $ pol_text_v = 0.01
     $ pol_text_z = 0.05
     if hour <= 16:
         scene corridor21
     elif hour == 17 and 18 and 19:
         scene corridor22
     else:
         scene corridor23
     $ gg = 13
     $ minute += 3
     call screen corridor1
screen corridor1:
     imagebutton xalign 0.99 yalign 0.24:
         idle ("icons/icons_backpack.png")
         hover ("icons/icons_backpack_hover.png")
         action Jump("backpack")
     imagebutton xalign 0.99 yalign 0.35:
         idle ("icons/icons_phone.png")
         hover ("icons/icons_phone_hover.png")
         action Jump("phone")
     imagebutton xalign 0.99 yalign 0.15:
         idle ("icons/icons_return_idle.png")
         hover ("icons/icons_return_hover.png")
         action Jump("corridor")
     frame xpos 75 yalign 0.21:
         text "[money] кредитов"
     add im.Rotozoom("gui/frame4.png", 0, 1.3) xalign 0.02 yalign 0.15
     if hour <= 9 and minute <= 9:
         text "0[hour]:0[minute]" xalign 0.05 yalign 0.152 size 48
     elif hour <= 9:
         text "0[hour]:[minute]" xalign 0.05 yalign 0.152 size 48
     elif minute <= 9:
         text "[hour]:0[minute]" xalign 0.05 yalign 0.152 size 48
     else:
         text "[hour]:[minute]" xalign 0.05 yalign 0.152 size 48
     frame xpos 10 yalign 0.26:
         text "Уровень энергии: [energy]"
     add im.Rotozoom("gui/frame1.png", 0, 1):
         size (1920, 150)
     text "{size=26}{b}Коридор школы: кто в локации?{/b}{/size}" xalign 0.5 yalign 0.01
     vpgrid:
         cols 5
         rows 10
         xalign 0.1 ypos 50 xysize (1920, 98)
         child_size (1920, 100)
         scrollbars "vertical"
         spacing 20 ###расстояние от порта до края изображе
         draggable True
         mousewheel True
         arrowkeys True
         for number_npc in range(1, number_npc_max):
             python:
                 location_npc = renpy.random.randint(1, 100)
             if hour <= 6:
                 $ u_loc_npc = 0
             if hour <= 7:
                 $ u_loc_npc = 20
             elif hour <= 8:
                 $ u_loc_npc = 1
             elif hour <= 9:
                 $ u_loc_npc = 10
             elif hour <= 10:
                 $ u_loc_npc = 1
             elif hour <= 11:
                 $ u_loc_npc = 10
             elif hour <= 12:
                 $ u_loc_npc = 1
             elif hour <= 13:
                 $ u_loc_npc = 10
             elif hour <= 14:
                 $ u_loc_npc = 1
             elif hour <= 16:
                 $ u_loc_npc = 15
             elif hour <= 18:
                 $ u_loc_npc = 7
             elif hour <= 22:
                 $ u_loc_npc = 10
             elif hour >= 23:
                 $ u_loc_npc = 0
             if location_npc <= u_loc_npc:
                 python:
                     npc_id = 'npc'+str(number_npc)
                     name_npc = eval(npc_id)["npc_name"]
                     fam_npc = eval(npc_id)["npc_fam"]
                     v_npc = eval(npc_id)["pich_npc"]
                     gender_npc = eval(npc_id)["gender_npc"]
                     contact_npc = eval(npc_id)["contact_npc"]
                     love_npc = eval(npc_id)["love_npc"]
                     fear_npc = eval(npc_id)["fear_npc"]
                 textbutton "{b}[number_npc].{/b} [name_npc] [fam_npc]":
                     action SetVariable('npc_id', npc_id), SetVariable('name_npc', name_npc), SetVariable('fam_npc', fam_npc), SetVariable('v_npc', v_npc), SetVariable('gender_npc', gender_npc), SetVariable('contact_npc', contact_npc), SetVariable('love_npc', love_npc), SetVariable('fear_npc', fear_npc), Jump('npc')
label map:
     scene bf with dissolve
     if language_game == 1:
         menu:
             "{color=#000000}Пляж{/color}":
                 if gg == 6:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_beach = True
                 call screen transport
             "{color=#000000}Школа{/color}":
                 if gg == 1:
                     "Ты уже находишься на этой локации"
                     jump map
                 if hour <= 18:
                     $ transport_school = True
                     call screen transport
                 elif hour <= 24:
                     "Сейчас школа закрыта."
                 jump map
             "{color=#000000}Парк{/color}":
                 if gg == 7:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_park = True
                 call screen transport
             "{color=#000000}Магазин{/color}":
                 if gg == 9:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_magazine = True
                 call screen transport
             "{color=#000000}Работа{/color}":
                 jump check_work
             "{color=#000000}Назад{/color}":
                 jump check_location
     elif language_game == 2:
         menu:
             "{color=#000000}Beach{/color}":
                 if gg == 6:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_beach = True
                 call screen transport
             "{color=#000000}School{/color}":
                 if gg == 1:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_school = True
                 call screen transport
             "{color=#000000}Park{/color}":
                 if gg == 7:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_park = True
                 call screen transport
             "{color=#000000}Store{/color}":
                 if gg == 9:
                     "Ты уже находишься на этой локации"
                     jump map
                 $ transport_magazine = True
                 call screen transport
             "{color=#000000}Joob{/color}":
                 jump check_work
             "{color=#000000}Back{/color}":
                 jump check_location
label check_work:
     if joob == False:
         if language_game == 1:
             "У вас нет работы."
         elif language_game == 2:
             "You have no job."
     if zavod == True:
         if hour == 16 and hour == 17 and hour == 18:
             jump zavod
         elif hour <= 15:
             if language_game == 2:
                 "It's not time to go to the factory yet. The shift begins at 16:00."
             elif language_game == 1:
                 "Смена начинается в 16:00."
             jump check_location
         else:
             "You have already missed the shift at the factory."
             jump check_location
label beach:
     $ gg = 6
     call screen beach
screen beach:
     imagebutton xalign 0.94 yalign 0.005:
         idle ("icons/icons_map_idle.png")
         hover ("icons/icons_map_hover.png")
         action Jump("map")
     imagebutton xalign 0.99 yalign 0:
         idle ("icons/icons_home_idle.png")
         hover ("icons/icons_home_hover.png")
         action Jump("home")
     imagebutton xalign 0.89 yalign 0.005:
         idle ("icons/icons_backpack.png")
         hover ("icons/icons_backpack_hover.png")
         action Jump("backpack")
     imagebutton xalign 0.85 yalign 0.005:
         idle ("icons/icons_phone.png")
         hover ("icons/icons_phone_hover.png")
         action Jump("phone")
     imagebutton xalign 0 yalign 0:
         idle ("icons/icons_time_idle.png")
         hover ("icons/icons_time_hover.png")
         action Jump('time2')
     imagebutton xalign 0 yalign 0.1:
         idle ("icons/icons_money.png")
     text "[money]" xalign 0.1 yalign 0.12 size 48
     if hour <= 9 and minute <= 9:
         text "0[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     elif hour <= 9:
         text "0[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
     elif minute <= 9:
         text "[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     else:
         text "[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
label bench:
     if language_game == 2:
         "Sitting on the bench, you began to observe the movement of passers-by, which seemed quite amusing to you."
         menu:
             "Light a cigarette":
                 if cigarette >= 1 and zhiga == 1:
                     "Having taken out a cigarette from a pack and a lighter from your pockets, you lit a cigarette right in the park. Two hours later, you already smoked the first cigarette and went to the second round."
                     "Having already smoked a fifth cigarette, you realized that this was a disastrous business and got up off the bench."
                     $ cigarette -= 5
                     $ energy += 3
                     "But apart from losing 5 cigarettes from a pack, you had a pretty good rest and had a lot of energy."
                     jump park1
                 if cigarette == 0:
                     "You do not have cigarettes."
                     jump park1
                 if zhiga == 0:
                     "You do not have a lighter."
                     jump park1
             "Just sit and watch":
                 $ energy += 2
                 $ minute += 30
                 "After sitting like this on the bench for half an hour, there was a feeling that you had little, but added energy."
                 jump park1
     elif language_game == 1:
             "Присев на лавочку, вы начали наблюдать за передвижением прохожих, что казалось вам вполне себе занятным."
             menu:
                 "Закурить":
                     if cigarette >= 1 and zhiga == 1:
                         "Достав сигарету из пачки и зажигалку из карманы, вы закурили прямо в парке. Через два часа вы уже выкурили первую сигарету и пошли на второй круг."
                         "Выкурив уже пятую сигарету, вы поняли, что это гиблое дело и встали со скамейки."
                         $ cigarette -= 5
                         $ energy += 3
                         "Но не считая потери 5 сигарет из пачки, вы довольно отлично отдохнули и имели достаточно много энергии."
                         jump park1
                     if cigarette == 0:
                         "Вы не имеете сигарет."
                         jump park1
                     if zhiga == 0:
                         "Вы не имеете зажигалки."
                         jump park1
                 "Просто сидеть и смотреть":
                     $ energy += 2
                     $ minute += 30
                     "Посидев так на лавочке полчаса, было ощущение, что вам немного, но добавилось энергии."
                     jump park1
label stroll:
     $ gg = 8
     scene stroll
     call screen stroll
screen stroll:
     imagebutton xalign 0.99 yalign 0:
         idle ("icons/icons_return_idle.png")
         hover ("icons/icons_return_hover.png")
         action Jump("park1")
     imagebutton xalign 0.85 yalign 0.005:
         idle ("icons/icons_phone.png")
         hover ("icons/icons_phone_hover.png")
         action Jump("phone")
     imagebutton xalign 0 yalign 0:
         idle ("icons/icons_time_idle.png")
         hover ("icons/icons_time_hover.png")
         action Jump('time2')
     if hour <= 9 and minute <= 9:
         text "0[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     elif hour <= 9:
         text "0[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
     elif minute <= 9:
         text "[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     else:
         text "[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
label park1:
     $ gg = 7
     if dialoge == 0 and dialoge >= 4:
         $ dialoge = 1
     call screen park
screen transport:
     if language_game == 1:
         text "{b}Выберите один из способов передвижения:{/b}"xalign 0.45 yalign 0.4 size 36
     elif language_game == 2:
         text "{b}Choose one of the transportation methods:{/b}"xalign 0.45 yalign 0.4 size 36
     imagebutton xalign 0.5 yalign 0.5:
         idle ("icons/icons_idle.png")
         hover ("icons/icons_hover.png")
         action Jump('afoot')
     imagebutton xalign 0.4 yalign 0.5:
         idle ("icons/icons_metro_idle.png")
         hover ("icons/icons_metro_hover.png")
         action Jump('metro')
     imagebutton xalign 0.3 yalign 0.5:
         idle ("icons/icons_autobus_idle.png")
         hover ("icons/icons_autobus_hover.png")
         action Jump('autobus')
     imagebutton xalign 0.6 yalign 0.5:
         idle ("icons/icons_taxi_idle.png")
         hover ("icons/icons_taxi_hover.png")
         action Jump('taxi')
label afoot:
     $ energy -= 10
     $ speed_transport = 0
label metro:
     $ energy -= 2
     $ speed_transport = 500
label autobus:
     $ energy -= 3
     $ speed_transport = 150
label taxi:
     $ energy -= 1
     $ speed_transport = 300
jump transport1
label transport1:
     if transport_magazine == True:
         $ distance_afoot = 100
         $ distance_transport = 0
         $ transport = 4
         $ transport_magazine = False
     if transport_beach == True:
         $ distance_afoot = 150
         $ distance_transport = 500
         $ transport = 1
         $ transport_beach = False
     if transport_school == True:
         $ distance_afoot = 100
         $ distance_transport = 150
         $ transport = 2
         $ transport_school = False
     if transport_park == True:
         $ distance_afoot = 200
         $ distance_transport = 1000
         $ transport = 3
         $ transport_park = False
     if transport_zavod == True:
         $ distance_afoot = 100
         $ distance_transport = 1000
         $ transport = 5
         $ transport_zavod = False
     $ distance_transport /= speed_transport
     $ minute += distance_transport
     $ distance_afoot /= movement_speed
     $ minute += distance_afoot
     if transport == 1:
         scene beach
         jump beach
     elif transport == 2:
         jump school
     elif transport == 3:
         jump park1
     elif transport == 4:
         jump magazine
     elif transport == 5:
         jump zavod
label magazine:
     $ energy -= 1
     $ gg = 9
     call screen magazine
screen magazine:
     imagemap:
         ground "backgrounds/location/magazine.jpg"
         hover "backgrounds/location/magazine_hover.png"
         hotspot (1142, 592, 233, 270) action Jump("magazine1")
     imagebutton xalign 0 yalign 0:
         idle ("icons/icons_time_idle.png")
         hover ("icons/icons_time_hover.png")
         action Jump('time2')
     imagebutton xalign 0.99 yalign 0:
         idle ("icons/icons_home_idle.png")
         hover ("icons/icons_home_hover.png")
         action Jump("home")
     imagebutton xalign 0.94 yalign 0.005:
         idle ("icons/icons_map_idle.png")
         hover ("icons/icons_map_hover.png")
         action Jump("map")
     imagebutton xalign 0.89 yalign 0.005:
         idle ("icons/icons_backpack.png")
         hover ("icons/icons_backpack_hover.png")
         action Jump("backpack")
     imagebutton xalign 0 yalign 0.1:
         idle ("icons/icons_money.png")
     text "[money]" xalign 0.1 yalign 0.12 size 48
     if hour <= 9 and minute <= 9:
         text "0[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     elif hour <= 9:
         text "0[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
     elif minute <= 9:
         text "[hour]:0[minute]" xalign 0.1 yalign 0.025 size 48
     else:
         text "[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
label magazine1:
     $ energy -= 1
     $ gg = 10
     scene magazine
     call screen buy
screen buy:
     imagebutton xalign 0.99 yalign 0:
         idle ("icons/icons_return_idle.png")
         hover ("icons/icons_return_hover.png")
         action Jump("magazine")
     imagebutton xalign 0.99 yalign 0.1:
         idle ("icons/icons_buy_idle.png")
         hover ("icons/icons_buy_hover.png")
         action Jump('buy_item')
     imagebutton xalign 0.85 yalign 0.005:
         idle ("icons/icons_phone.png")
         hover ("icons/icons_phone_hover.png")
         action Jump("phone")
     imagebutton xalign 0 yalign 0:
         idle ("icons/icons_time_idle.png")
         hover ("icons/icons_time_hover.png")
         action Jump('time2')
     imagebutton xalign 0 yalign 0.1:
         idle ("icons/icons_money.png")
     text "[money]" xalign 0.1 yalign 0.12 size 48
     text "[hour]:[minute]" xalign 0.1 yalign 0.025 size 48
label buy_item:
     show p1 at center with dissolve
     $ cigarette_buy = renpy.random.randint(1, 4)
     if language_game == 1:
         menu:
             "Купить пачку сигарет":
                 if cigarette_buy <= 2:
                     "Хоть вы и не выглядели совершеннолетним, но вам без проблем продали вашу заветную пачку."
                     $ cigarette += 20
                 else:
                     "Оглянув вас с головы до пят, продавщица попросила вас показать паспорт, поняв, что вы несовершеннолетний."
                     menu:
                         "Сказать, что паспорта у вас с собой нет, но вы все же намерены получить свою пачку.":
                             show p2 at center
                             b "Молодой человек, либо вы сейчас уходите, либо я вызываю полицию."
                             "Глянув на грозное лицо продавщицы, вы решили не усугублять конфликт и вышли из магазина, так и не купив заветную пачку сигарет."
                             jump magazine
                         "Уйти, не создавая ни себе, ни продавщице лишних проблем.":
                             "Вы решили уйти подальше от этого стервозного вида девушки, так и не получив то, чего вы так хотели."
                             jump magazine
             "Купить газировку":
                 "Быстро схватив с полки бутылку газировки, вы положили ее на кассу и, оплатив товар, ушли."
                 $ cola += 1
             "Купить лапшу быстрого приготовления":
                 "Взяв лапшу быстрого приготовления с полки, вы понесли ее на кассу, после чего оплатили."
                 $ rolton += 1
             "Купить зажигалку":
                 $ zhiga = 1
             "Назад":
                 jump magazine1
         jump magazine1
     elif language_game == 2:
         menu:
             "Buy a pack of cigarettes":
                 if cigarette_buy <= 2:
                     "Although you didn’t look of age, they sold your treasured bundle without any problems."
                     $ cigarette += 20
                 else:
                     "Looking around from head to toe, the saleswoman asked you to show your passport, realizing that you are a minor."
                     menu:
                         "Say that you do not have a passport with you, but you still intend to get your pack.":
                             show p2 at center
                             b "The young man, either you leave now, or I call the police."
                             "Looking at the terrible face of the saleswoman, you decided not to aggravate the conflict and left the store without having bought a treasured pack of cigarettes."
                             jump magazine
                         "To leave without creating any problems for herself or the saleswoman.":
                             "You decided to get away from this bitchy kind of girl without ever getting what you wanted."
                             jump magazine
             "Buy soda":
                 "Quickly grabbing a bottle of soda from the shelf, you put it on the cash register and, having waited your turn, paid for the goods and left."
                 $ cola += 1
             "Buy instant noodles":
                 "Taking instant noodles from the shelf, you carried it to the cashier, and then paid."
                 $ rolton += 1
             "Buy lighter":
                 $ zhiga = 1
             "Back":
                 jump magazine1
         jump magazine1
