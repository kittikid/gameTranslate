init python:
     random_ivent = 0
     page = 1
     main_menu_pon = 1
     reaction_gid = 1
     Patreon_Code = 0
     Patreon_Code_M = 'no'
     Lite_Mode = 0
     minute = 100
     hour = 10
     second = 1
     days = 6
     number_npc_max = 0
     weeks = 1
     month = 1
     years = 0
     contact_gg_npc = 0
     progress = 0
     love_gg_npc = 0
     int_science_plus = 0
     progress_body = 0
     int_forces_plus = 0
     speed_education_progress = 0
     language_game = 1
     combat_win = 0
     combat_experience = 0
     ivents_hooligans = 0
     ivent_extortion = 0
     ivents_hooligans1 = 0
     random_gg = 0
     gg_npc = 0
     v_npc = 0
     port = 0
     charisma = 0
     stats_erudition_gg = 0
     love_gg_npc = 0
     contact_npc1 = 0
     energy = 100
     location_school = 0
     days_name = 0
     gg = 0
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
     tablet_painting = 0
     camera = 0
     vacuum = 0
     purity_club_occult = 0
     popularity_club_occult = 0
     npc_nature = 0
     tablet = 0
     minet_ayano = 0
     global_project_poc = 0
     global_project_poc3 = 0
     festivale_poc = 0
     purity_club_occult_poc = 0
     popularity_club_occult_poc = 0
     authority_club_occult_poc = 0
     festivale_poc = 0
     telephone_number = 0
     telephone_number1 = 1
     messange_npc = 0
     random = 0
     location_npc1 = 0
     old_popularity_club_occult = 0
     popularity_club_occult_poc2 = 0
     festivale_poc = 0
     festivale_poc3 = 0
     festivale_poc4 = 0
     book_guide_occult_club = 0
     page_book = 1
     find_human_club_occult = 0
     find_human = 0
     find_human_club_occult_poc = 0
     page_phone = 0
     randomize_npc = 0
     name_days = {"1":"Пн", "2":"Вт", "3":"Ср", "4":"Чт", "5":"Пт", "6":"Сб", "7":"Вс"}
     def time1():
         global minute, hour, second, days, weeks, month, years, contact_gg_npc, charisma, stats_erudition_gg, love_gg_npc, days, contact_npc1, energy, menu_loc, location_school, location_npc, location_school, npc_nature, joob_complete, free_soda, lessons_per_day, absenteeism, absenteeism_joob
         global days_name, name_days, gg, name_days, purity_club_occult, popularity_club_occult, club, location_npc1
         name_days = {"1":"Пн", "2":"Вт", "3":"Ср", "4":"Чт", "5":"Пт", "6":"Сб", "7":"Вс"}
         if days == 0:
             days = 1
         if minute <= -1:
             minute = 0
         if minute >= 60:
             if purity_club_occult >= 100:
                 purity_club_occult = 100
             hour1 = minute/ 60
             hour += hour1
             minute -= hour1 * 60
             location_school = ['school_class', 'join_school', 'corridor_school', 'roof', 'canteen', 'pool']
             location_city = ['park', 'shopping_center']
             for number_npc in range(1, number_npc_max):
                 npc_id = 'npc'+str(number_npc)
                 club_npc = eval(npc_id)['club_npc']
                 npc_nature = eval(npc_id)["npc_nature"]
                 if days <= 5:
                     if hour <= 6:
                         location_npc = 'apartament'
                     elif hour == 7:
                         if location_npc <= 40:
                             location_npc = 'school_class'
                         elif location_npc <= 55:
                             location_npc = 'pool'
                         else:
                             location_npc = renpy.random.randint(1, 100)
                             if location_npc <= active_npc * 15:
                                 location_npc = renpy.random.choice(location_school)
                             else:
                                 location_npc = location_npc
                             eval(npc_id)["location_npc"] = location_npc
                     elif hour == 8:
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
                         eval(npc_id)["location_npc"] = location_npc
                     elif hour == 9:
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
                         eval(npc_id)["location_npc"] = location_npc
                     elif hour <= 16:
                         if npc_nature == 'Адекватность' or npc_nature == 'Романтичный' or npc_nature == 'Надменный':
                             if hour <= 6:
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
                             eval(npc_id)["location_npc"] = location_npc
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
                         eval(npc_id)["location_npc"] = location_npc
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
         if hour >= 24:
             global authority_club_occult, club_joob, npc_id, number_npc, number_occult_club, budget_club_occult, festivale, popularity_club_occult, global_project, new_participant_club_occult, random, popularity_club_occult
             global budget_club_occult, budget_club_occult_plus, popularity_club_occult, budget_club_occult, festivale, microwave, poster, refrigerator, playstation, furniture, authority_club_occult, vacuum, camera, tablet, tablet_painting
             global find_human_club_occult, find_human, microwave, poster, refrigerator, playstation, furniture, authority_club_occult_poc, popularity_club_occult_poc, pool_ivent
             if pool_ivent == 2:
                 pool_ivent = 3
             authority_club_occult_poc = 0
             popularity_club_occult_poc = 0
             if days == 0:
                 days = 1
             if joob >= 1:
                 absenteeism_joob -= joob_complete - 1
             if days <= 5:
                 absenteeism += 4 - lessons_per_day
             lessons_per_day = 0
             joob_complete = 0
             free_soda = 1
             days1 = hour/24
             days += days1
             hour -= days1 * 24
             idleness_human = 0
             global_project_human = 0
             purity_human = 0
             festivale_human = 0
             articles_human = 0
             if number_occult_club >= 3:
                 for number_npc in range(3, number_occult_club+1):
                     npc_id = 'name_club_npc_occult'+str(number_npc)
                     perk = eval(npc_id)["perk"]
                     club_joob = eval(npc_id)["club_joob"]
                     if club_joob == 5:
                         idleness_human += 1
                     elif club_joob == 4:
                         global_project_human += 1
                     elif club_joob == 2:
                         purity_human += 1
                     elif club_joob == 3:
                         festivale_human += 1
                     elif club_joob == 1:
                         articles_human += 1
             if days <= 6:
                 if number_occult_club >= 3:
                     popularity_club_occult += purity_club_occult / 10
                     if vacuum == 1:
                         purity_club_occult += 25
                     if microwave == 1:
                         popularity_club_occult_poc += 0.2
                     if poster == 1:
                         authority_club_occult_poc += 0.2
                     if refrigerator == 1:
                         popularity_club_occult_poc += 0.3
                         authority_club_occult_poc += 0.2
                     if playstation == 1:
                         popularity_club_occult_poc += 0.8
                         authority_club_occult_poc -= 0.2
                     if furniture == 1:
                         authority_club_occult_poc += 0.8
                     authority_club_occult_poc += round((stats_authority_gg_info / 4) / 7, 1)
                     for number_npc in range(3, number_occult_club+1):
                         npc_id = 'name_club_npc_occult'+str(number_npc)
                         perk = eval(npc_id)["perk"]
                         club_joob = eval(npc_id)["club_joob"]
                         if club_joob == 5:
                             if perk == 'Ленивый':
                                 authority_club_occult_poc += 0.2
                             authority_club_occult_poc += 0.3
                         elif club_joob == 4:
                             if perk == 'Одиночка':
                                 if global_project_human <= 2:
                                     global_project += 2
                                 else:
                                     global_project -= 1
                             elif perk == 'Командный':
                                 if global_project_human >= 3:
                                     global_project += 2
                                 else:
                                     global_project -= 1
                             if camera == 1:
                                 global_project += 1
                             if perk == 'Старательный':
                                 global_project += 2
                             if perk == 'Вялый':
                                 global_project -= 2
                             global_project += 3
                             if perk == 'Фонтан идей':
                                 authority_club_occult_poc += 1.5
                             elif perk == 'Верный':
                                 authority_club_occult_poc += 0.6
                             authority_club_occult_poc -= 1.5
                             if global_project >= 100:
                                 global global_project_poc3
                                 if perk == 'Бережливый':
                                     global_project += renpy.random.randint(1, 10)
                                 global_project_poc3 = 0
                                 global_project_poc3 += int((popularity_club_occult / 100) * 15)
                                 popularity_club_occult += int((popularity_club_occult / 100) * 15)
                                 global_project = 0
                         elif club_joob == 2:
                             if perk == 'Одиночка':
                                 if purity_human <= 2:
                                     purity_club_occult += 10
                                 else:
                                     purity_club_occult += 2
                             elif perk == 'Командный':
                                 if purity_human <= 2:
                                     purity_club_occult += 10
                                 else:
                                     purity_club_occult += 2
                             if perk == 'Вялый':
                                 purity_club_occult -= 6
                             if perk == 'Чистюля':
                                 purity_club_occult += 10
                             purity_club_occult += 10
                             if perk == 'Фонтан идей':
                                 authority_club_occult_poc += 0.3
                             elif perk == 'Верный':
                                 authority_club_occult_poc += 0.1
                             authority_club_occult_poc -= 0.3
                         elif club_joob == 3:
                             if perk == 'Одиночка':
                                 if festivale_human <= 2:
                                     festivale += 2
                                 else:
                                     festivale -= 1
                             elif perk == 'Командный':
                                 if festivale_human >= 3:
                                     festivale += 2
                                 else:
                                     festivale -= 1
                             if perk == 'Старательный':
                                 festivale += 1
                             if perk == 'Вялый':
                                 festivale -= 2
                             festivale += 4
                             if perk == 'Фонтан идей':
                                 authority_club_occult_poc += 0.5
                             elif perk == 'Верный':
                                 authority_club_occult_poc += 0.1
                             authority_club_occult_poc -= 0.5
                         elif club_joob == 1:
                             if perk == 'Одиночка':
                                 if articles_human <= 2:
                                     popularity_club_occult_poc += 3
                                 else:
                                     popularity_club_occult_poc -= 1
                             elif perk == 'Командный':
                                 if articles_human >= 3:
                                     popularity_club_occult_poc += 2
                                 else:
                                     popularity_club_occult_poc -= 1
                             if tablet == 1:
                                 popularity_club_occult_poc += 1
                             if tablet_painting == 1:
                                 popularity_club_occult_poc += 2
                             if perk == 'Быстро печатает':
                                 popularity_club_occult_poc += 1
                             if perk == 'Вялый':
                                 popularity_club_occult_poc -= 1
                             popularity_club_occult_poc += 2
                             if perk == 'Фонтан идей':
                                 authority_club_occult_poc += 0.4
                             elif perk == 'Верный':
                                 authority_club_occult_poc += 0.1
                             authority_club_occult_poc -= 0.4
                         elif club_joob == 6:
                             if perk == 'Одиночка':
                                 if articles_human <= 2:
                                     find_human_club_occult += 2
                                 else:
                                     find_human_club_occult -= 1
                             elif perk == 'Командный':
                                 if articles_human >= 3:
                                     find_human_club_occult += 1
                                 else:
                                     find_human_club_occult -= 1
                             if perk == 'Вялый':
                                 find_human_club_occult -= 1
                             find_human_club_occult += 2
                             if perk == 'Фонтан идей':
                                 authority_club_occult_poc += 0.4
                             elif perk == 'Верный':
                                 authority_club_occult_poc += 0.1
                             authority_club_occult_poc -= 0.4
                         if authority_club_occult <= 0:
                             club_joob = 5
                             eval(npc_id)["club_joob"] = club_joob
                         if perk == 'Самостоятельный':
                             if club_joob == 5:
                                 club_joob = renpy.random.randint(1, 4)
                         if perk == 'Ленивый':
                             club_joob = 5
                         if perk == 'Заядлый игрок':
                             if playstation == 1:
                                 club_joob = 5
                         if perk == 'Чистюля':
                             if purity_club_occult <= 0:
                                 club_joob = 2
                         if perk == 'Неряха':
                             purity_club_occult -= 10
                         eval(npc_id)["club_joob"] = club_joob
             if club == 1:
                 random = renpy.random.randint(1, 100)
                 if new_participant_club_occult == 0:
                     global find_human, find_human_club_occult
                     find_human = popularity_club_occult / 100 + find_human_club_occult
                     if random <= find_human:
                         new_participant_club_occult = 1
                 if days <= 5:
                     purity_club_occult -= 10
                 if purity_club_occult >= 101:
                     purity_club_occult = 100
                 elif purity_club_occult <= -101:
                     purity_club_occult = -100
                 if festivale >= 100:
                     festivale = 100
                 if number_occult_club >= 3:
                     authority_club_occult += authority_club_occult_poc
                     popularity_club_occult += popularity_club_occult_poc
         if days >= 8:
             global number_npc_max, randomize_npc
             conditions_school_extensions = number_npc_max * 100
             true_conditions_school_extensions = popularity_basketball + popularity_pool + popularity_athletics + popularity_art + popularity_science + popularity_literature + popularity_drama + popularity_detective + popularity_journalism + popularity_journalism + popularity_club_occult
             if days == 0:
                 days = 1
             global popularity_detective_poc, popularity_journalism_poc, popularity_drama_poc, popularity_club_occult_poc2, old_popularity_club_occult, old_popularity_club_occult, popularity_pool_poc, popularity_athletics_poc, popularity_basketball_poc, popularity_art_poc, popularity_science_poc, popularity_literature_poc
             global popularity_basketball, popularity_pool, popularity_athletics, popularity_art, popularity_science, popularity_literature, popularity_drama, popularity_detective, popularity_journalism

             popularity_basketball_poc = renpy.random.randint(-5, 7) * 10

             popularity_club_occult_poc2 = popularity_club_occult - old_popularity_club_occult
             old_popularity_club_occult = popularity_club_occult
             if pool_club_r == 1:
                 popularity_pool_poc = renpy.random.randint(-5, 29) * 10
             else:
                 popularity_pool_poc = renpy.random.randint(-30, 1) * 10
             popularity_athletics_poc = renpy.random.randint(-5, 25) * 10
             popularity_basketball_poc = renpy.random.randint(-5, 25) * 10
             popularity_art_poc = renpy.random.randint(-5, 20) * 10
             popularity_science_poc = renpy.random.randint(-3, 19) * 10
             popularity_literature_poc = renpy.random.randint(-2, 19) * 10
             popularity_drama_poc = renpy.random.randint(-1, 8) * 10
             popularity_detective_poc = renpy.random.randint(0, 10) * 10
             popularity_journalism_poc = renpy.random.randint(-20, 40) * 10
             popularity_basketball += popularity_basketball_poc
             popularity_pool += popularity_pool_poc
             popularity_athletics += popularity_athletics_poc
             popularity_art += popularity_art_poc
             popularity_science += popularity_science_poc
             popularity_literature += popularity_literature_poc
             popularity_drama += popularity_drama_poc
             popularity_detective += popularity_detective_poc
             popularity_journalism += popularity_journalism_poc
             global authority_club_occult, budget_club_occult, budget_club_occult_plus, popularity_club_occult, budget_club_occult, festivale, microwave, poster, refrigerator, playstation, furniture, authority_club_occult, ayano_contact
             global festivale_poc3, festivale_poc4

             popularity_club_occult += int(festivale / 4)
             budget_club_occult += int(festivale / 4 * 400)
             festivale_poc3 = int(festivale / 4)
             festivale_poc4 = int(festivale / 4) * 400
             festivale = 0

             ayano_contact += int(authority_club_occult / 2)
             for number_npc in range(1, number_npc_max):
                 npc_id = 'npc'+str(number_npc)
                 contact_npc = eval(npc_id)['contact_npc']
                 love_npc = eval(npc_id)["love_npc"]
                 gender_npc = eval(npc_id)["gender_npc"]
                 if gender_npc == 2:
                     location_npc = renpy.random.randint(1, 100)
                     if location_npc <= popularity_club_occult / 2:
                         contact_npc += int(popularity_club_occult / 80)
                         love_npc += int(popularity_club_occult / 120)
                         eval(npc_id)["love_npc"] = love_npc
                         eval(npc_id)["contact_npc"] = contact_npc
             budget_club_occult_plus += int(popularity_club_occult)
             budget_club_occult += int(budget_club_occult_plus)
             if number_occult_club >= 3:
                 for number_npc in range(3, number_occult_club+1):
                     npc_id = 'name_club_npc_occult'+str(number_npc)
                     club_joob = eval(npc_id)["club_joob"]
                     perk = eval(npc_id)["perk"]
                     if club_joob == 3:
                         if perk == 'Бережливый':
                             festivale += renpy.random.randint(1, 10)
             weeks1 = days/8
             weeks += weeks1
             days -= weeks1 * 8
             if true_conditions_school_extensions >= conditions_school_extensions:
                 randomize_npc = number_npc_max
                 number_npc_max += int(true_conditions_school_extensions / 10000)
                 if not number_npc_max >= 301:
                     renpy.show_screen('up_school')
         if weeks >= 4:
             month1 = weeks/4
             month += month1
             weeks -= month1 * 4
         if month >= 12:
             years1 = month/12
             month += years1
             month -= years1 * 12
         contact_gg_npc = ((charisma/2) + (stats_erudition_gg/4)) / 10
         love_gg_npc = ((charisma/3) + (stats_erudition_gg/4)) / 10
         if gg <= 4 or gg >= 21:
             if hour <= 6 or hour >= 21:
                 renpy.show_screen('poshel_von_blyat')
         if energy <= -40:
             energy = -40
     def education_r(where):
         global progress, int_science_plus, stats_science_gg, speed_education
         progress += 1
         progress_science_need = int(stats_agility_gg) / 5
         if progress >= progress_science_need:
             speed_education += 1
             stats_science_gg += 1
             progress = 0
         renpy.jump(where)
     def play_music(where):
         renpy.music.set_volume(0.1, delay=0, channel='music')
         renpy.play("music/1.mp3", channel=None)
     def npc_location(argument):
         number_npc = 0
         while number_npc <= 60:
             number_npc += 1
             npc_number = "npc"+str(number_npc)
             location_npc = renpy.random.randint(1, 10)
             npc_character["npc_location"] = location_npc
             setattr(store, npc_number, npc_character)
         renpy.jump(argument)
     def cursor(name = None):
         if name:
             config.mouse = {'default' : [('images/' + name + '.png', 0, 0)]}
         else:
             config.mouse = None
         Cursor = renpy.curry(cursor)
     def change_joob_club( ):
         eval(npc_id)["club_joob"] = club_complete
         club_complete = 0
init:
     image main_menu123:
         "gui/overlay/mm/main_menu1.png" with Dissolve(.9)
         pause 20.0
         "gui/overlay/mm/main_menu2.png" with Dissolve(.9)
         pause 20.0
         "gui/overlay/mm/main_menu3.png" with Dissolve(.9)
         pause 20.0
         repeat
init:
     if port == 0:
         define gui.dialogue_xpos = 470
         define gui.dialogue_ypos = 15
         define gui.dialogue_width = 1000
         define gui.name_xpos = 700
         define gui.name_ypos = -50
transform show_hide_dissolve:
     on show:
         alpha .0
         linear .5 alpha 1.0
     on hide:
         alpha 1.0
         linear .5 alpha .0
transform button_m:
     on hover:
         zoom 1
         linear .25 zoom 1.25
     on idle:
         zoom 1.25
         linear .25 zoom 1
screen cheat:
     frame xalign 0.5 yalign 0.5:
         has vbox
         text "{color=#000000}Введите патреон код, выданный после покупки подписки\n     на патреоне или полученный в дискорд канале игры.{/color}\n"
         input xalign 0.5 yalign 0.9:
             default ""
             value VariableInputValue('Patreon_Code_M')
             length 8
             font "gui/fonts/ubuntu.ttf"
             size 35
         textbutton "\nПодтвердить" action Hide('cheat'), Jump('Patreon_Code123123') xalign 0.5
screen main_menu():
     imagemap:
         ground "main_menu123" at show_hide_dissolve
     imagemap:
         ground "gui/overlay/main_menu.png"
         hover "gui/overlay/main_menu_hover.png"
         hotspot (1765, 109, 122, 96):
             action OpenURL('https://www.patreon.com/school123')
         hotspot (1819, 207, 92, 65):
             action OpenURL('https://discord.gg/rfdGhda')
         hotspot(1777, 278, 142, 31):
             action Show('cheat')
     python:
         renpy.music.queue("music/1.mp3", channel = "music", fadein = 1)
     imagebutton auto "gui/overlay/button/start_%s.png" focus_mask True action Start()
     imagebutton auto "gui/overlay/button/load_%s.png" focus_mask True action ShowMenu('load')
     imagebutton auto "gui/overlay/button/setting_%s.png" focus_mask True action ShowMenu('preferences')
     imagebutton auto "gui/overlay/button/mod_%s.png" focus_mask True action Jump('mods')
     imagebutton auto "gui/overlay/button/exit_%s.png" focus_mask True action Quit(confirm=True)
     add "gui/system/credits.png"
     tag menu
     imagemap:
         if page == 1:
             ground "gui/overlay/news/update.png"
             hotspot (1574, 1031, 193, 32):
                 action OpenURL('https://www.patreon.com/posts/version-0-903-34239884')
         else:
             ground "gui/overlay/news/info.png"
         hotspot(1700, 563, 79, 86):
             action SetVariable('page', 2)
         hotspot(1777, 565, 69, 95):
             action SetVariable('page', 1)
     vbox yalign 0.3:
         if Patreon_Code == 1 or Patreon_Code == 2:
             if Lite_Mode == 0:
                 textbutton "{color=#FFFFFF}{b}Lite Mode = Off{/b}{/color}" action SetVariable('Lite_Mode', 1)
             elif Lite_Mode == 1:
                 textbutton "{color=#FFFFFF}{b}Lite Mode = On{/b}{/color}" action SetVariable('Lite_Mode', 0)
             if hentai_patch_inicial == True:
                 textbutton "{color=#FFFFFF}{b}Hentai Patch = On{/b}{/color}" action SetVariable('hentai_patch_inicial', False)
             elif hentai_patch_inicial == False:
                 textbutton "{color=#FFFFFF}{b}Hentai Patch = Off{/b}{/color}" action SetVariable('hentai_patch_inicial', True)
         elif Patreon_Code == 3:
             if hentai_patch_inicial == True:
                 textbutton "{color=#FFFFFF}{b}Hentai Patch = On{/b}{/color}" action SetVariable('hentai_patch_inicial', False)
             elif hentai_patch_inicial == False:
                 textbutton "{color=#FFFFFF}{b}Hentai Patch = Off{/b}{/color}" action SetVariable('hentai_patch_inicial', True)
label mods:
     scene bf
     if h_patch == False:
         if language_game == 1:
             "В директории игры отсутствуют моды"
         elif language_game == 2:
             "There are no mods in the game directory"
     else:
         if language_game == 1:
             menu:
                 "Инициализировать хентай патч?"
                 "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Да{/color}{/size}{/font}":
                     $ hentai_patch_inicial = True
                 "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Нет{/color}{/size}{/font}":
                     $ hentai_patch_inicial = False
         elif language_game == 2:
             menu:
                 "Initialize hentai patch?"
                 "Yes":
                     $ hentai_patch_inicial = True
                 "No":
                     $ hentai_patch_inicial = False
     call screen main_menu
label start:
     stop music fadeout 1
     $ renpy.pause(1.0, hard=True)
     play music "music/5.mp3" fadeout 1 loop
     scene bf with dissolve
     if language_game == 2:
         show text "{b}This game is a non-profit product. All files used in it are the property of their creators, and the developers who create the game do not try to appropriate their creativity. If you are opposed to using your art / background / music, etc. in this game, then contact the developers for further discussion of this problem. \ NIf you want to support the developers to finally hire artists, you can click the icon above the language selection in the main menu. You will be transferred to our patreon.{/b}" with dissolve
         with Pause(20)
         hide text with dissolve
         with Pause(1)
     elif language_game == 1:
         show text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Данная игра является некоммерческим продуктом. Все файлы, используемые в оной, являются собственностью их создателей, а разработчики, создающие игру, не пытаются присвоить себе их творчество. Если вы против того, чтобы в данной игре использовался ваш арт/фон/музыка и т.д., то обратитесь к разработчикам для дальнейшего обсуждения этой проблемы.\nЕсли вы хотите поддержать разработчиков, чтобы те наконец-то наняли художников и переводчиков на английский язык, вы можете нажать на иконку патреона в главном меню и поддержать нас там.{/color}{/size}{/font}" with dissolve
         with Pause(20)
         hide text with dissolve
         with Pause(1)
label start1:
     $ open_number = 0
     $ club = 0
     $ gg_npc = 0
     $ xuligan_class = 0
     $ ancete = 0
     $ smartphone = 0
     $ standart_stats = 1
     $ npc_sms = False
     $ push_up_today = False
     $ push_ups = 0
     $ cheat_menu = 0
     $ menu_loc = 0
     $ energy = 100
     $ gg = 1
     $ check_time = 0
     $ app = 0
     $ dop_app = 0
     $ speed_transport = 0
     $ npc_sms = False
     $ info_progress = False
     $ cigarette = 0
     $ cola = 0
     $ money = 0
     $ joob = False
     $ informal_view = False
     $ check_time = 0
     $ yumi_gg_smoking = True
     $ rolton = 0
     $ smartphone = False
     $ skills_programm = 0
     $ level_skills_programm = 0
     $ level_zakaz_up = 10
     $ zakaz = 0
     $ bts = False
     $ hate_yumi = False
     $ sms_start = True
     $ zavod = False
     $ zhiga = 0
     $ check_yumi = True
     $ progress = 0
     $ gg = 1
     $ dop_mod_horror = 0
     $ slots_o = 0
     $ smoker = True
     $ love_yumi = 0
     $ transport_magazine = False
     $ transport_beach = False
     $ transport_school = False
     $ transport_park = False
     $ transport_zavod = False
     $ zavod_first = True
     $ transport = map
     $ stats_forces_gg = 20
     $ stats_agility_gg = 20
     $ stats_stamina_gg = 20
     $ stats_science_gg = 20
     $ stats_cunning_gg = 20
     $ stats_authority_gg = 20
     $ stats_erudition_gg = 20
     $ stats_lucky_gg = 20
     $ dop_stats_authority_gg = 0
     $ dop_stats_forces_gg = 0
     $ dop_stats_agility_gg = 0
     $ dop_stats_lucky_gg = 0
     $ dop_stats_science_gg = 0
     $ dop_stats_stamina_gg = 0
     $ dop_stats_cunning_gg = 0
     $ dop_stats_erudition_gg = 0
     $ vn_gg = 1
     $ miniature = False
     $ help = 0
     $ loner = False
     $ huckster = False
     $ points_perk = 2
     $ stomach = False
     $ stocky = False
     $ heavy_arm = False
     $ zombie = False
     $ politic = False
     $ stomach = False
     $ dop_damage_gg = 0
     $ high_growth = False
     $ points_stats = 20
     $ points_hp_gg = 100
     $ scars_face = False
     $ athletic_body = False
     $ ladies_man = False
     $ botanic = False
     $ damage_gg = 0
     $ mod_horror = 0
     $ boost_otn = False
     $ boost_otn_zn = 0
     $ trap = False
     $ app_contact_npc = 0
     $ app_love_npc = 0
     $ app_fear_npc = 0
     $ otn_agressive = False
     $ otn_agressive_zn = 0
     $ pretty_face = False
     $ pumped_up_body = False
     $ remarkable_strength = False
     $ stocky1 = False
     $ fat = False
     $ dry_body = False
     $ student_soviet_g = 0
     $ student_soviet_progress = 0
     $ randomize_npc = 1
     define config.hard_rollback_limit = 0
     jump menu_character
screen icons_preset:
     add "icons/icons_fist_fight.png" xalign 0.3 yalign 0.2
label menu_character:
     python:
          days_calendar = 0
          for days_calendar in range(1, 12):
              calendar_month12 = 31
              calendar_month = "calendar_month"+str(days_calendar)
              calendar_days = renpy.random.randint(28, 31)
              setattr(store, calendar_month, calendar_days)
     if Patreon_Code_M == 'eggto' or Patreon_Code_M == 'baryt':
         $ renpy.movie_cutscene("backgrounds/location/cafe/andrey.webm")
         guide7 "И не стыдно тебе использовать слитый патреон-код?!"
         guide8 "Ненавижу таких игроков! Удачи тебе."
         $ renpy.quit()
     show main_menu123 with dissolve
     guide1 "Привет-привет тебе, новоиспеченный игрок! Как дела, есть какие-нибудь новости?"
     guide3 "Ах… Мы же отнюдь не знакомы…"
     guide4 "Но не волнуйся! Сейчас мы и исправим это упущение!"
     guide1 "Я – гид. Именно я буду преследовать тебя всю игру, объясняя механики, системы и суть игры!"
     guide3 "Ух… Страшно прозвучало. Будто я сталкер какой-то, но…"
     guide5 "В некоторой степени это действительно так. Я же тот самый НПС, ломающий четвертую стену!"
     guide1 "Ну, я рассказала о себе. Теперь твоя очередь! Как тебя звать?"
     $ player_name = renpy.input("Введите имя вашего персонажа", default =_("Безымянный"), allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZйцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ", length=10)
     $ player_name = player_name.strip()
     if len(player_name) < 2:
         "Вы должны использовать минимум 2 буквы"
     if player_name == 'andrey' or player_name == 'Andrey' or player_name == 'Андрей' or player_name == 'андрей':
         $ renpy.movie_cutscene("backgrounds/location/cafe/andrey.webm")
     guide12 "А неплохое имя! Щепотка фантазии, горстка увлечений и… Смысла?"
     guide1 "Ладно-ладно, я уже захожу немного не в ту степь, так что давай не терять время друг дружки. Имя у тебя уже есть, [player_name], поэтому давай разбираться в РПГ системе данной игры!"
     guide1 "В общем, смотри, в School Game присутствует несколько элементов: атрибуты, особенности внешности, соответственно, перки и скрытые значения параметров, влияющие на геймплей: тот же модификатор жуткости или привлекательности."
     guide1 "Каждый из вышеназванных имеет свое назначение, но если говорить очень кратко, то атрибуты – основополагающая геймплея, а другие элементы вспомогательные значения, задающие ответы в диалоговой системе, дающие плюсы или минусы к привязанности, отношениям с каким-либо НПС и"
     guide1 "собственно, много других вещей, которые перечислять займет достаточно долгое время, так что…"
     guide4 "Давай не будем лезть в эти дебри механик!"
     guide1 "Но... Одно сказать все же нужно обязательно: в игре есть пресеты характеров, влияющие на ответы ИПа, его действия при ивентах, событиях, а также на начальный набор атрибутов, особенностей внешности и перков, которые можно посмотреть после в компьютере при начале геймплея. "
     guide1 "Так… Раз уж мы кратко разобрались с пресетами, давай ты мне расскажешь причины твоего перевода в данную школу?"
     menu:
         guide1 "Так… Раз уж мы кратко разобрались с пресетами, давай ты мне расскажешь причины твоего перевода в данную школу?"
         "{color=#000000}У меня было множество проблем из-за хулиганства\nв прошлой школе…{/color}":
             guide3 "О как! Любитель подраться, вымогать деньги, а также издеваться над слабыми?"
             guide11 "Тут уж не мое дело, осуждать я тебя не могу, но на всякий предупрежу – будь осторожнее."
             guide7 "И еще… Если решишься устроить сильный мордобой, то будь готов к отчислению!"
             guide8 "Тут даже я не спасу тебя, какой бы я могущественной в рамках игрового процесса не была…"
             $ otn_agressive = True
             $ otn_agressive_zn = 20
             $ dop_stats_authority_gg += 10
             $ dop_stats_forces_gg += 10
             $ dop_stats_stamina_gg += 10
             $ heavy_arm = True
             $ gg_character = 'Хулиган'
         "{color=#000000}Думаю, что эта школа может дать мне знания, которые бы я не получил в своем прошлом учебном заведении.{/color}":
             guide4 "О как! Похвально!"
             guide5 "Книжный червь, стремящийся к знаниям – нынче достаточно необычное явление!"
             guide1 "В любом случае желаю тебе удачи с женским полом. Она тебе точно пригодится, учитывая, что тебя будут считать за задрота и изначально плохо к тебе относиться…"
             $ otn_agressive = True
             $ otn_agressive_zn -= 20
             $ dop_stats_science_gg += 20
             $ dop_stats_cunning_gg += 5
             $ dop_stats_erudition_gg += 5
             $ botanic = True
             $ gg_character = 'Заучка'
         "{color=#000000}У вас много красивых девушек. Я бы хотел пообщаться со многими, а может и со всеми из них.{/color}":
             guide7 "Казанова на борту..."
             guide8 "Спрятать всех девушек!"
             guide11 "Шучу."
             guide3 "Но тебе лучше быть осторожнее, ведь если все узнают о твоих предпочтениях…"
             guide1 "Хотя, думаю, ты сам знаешь!"
             $ ladies_man = True
             $ dop_stats_cunning_gg += 10
             $ dop_stats_erudition_gg += 20
             $ gg_character = 'Дамский угодник'
         "{color=#000000}Ну… У меня были плохие отношения со своими прошлыми одноклассниками… Может, у меня будет все хорошо с нынешними… Я надеюсь…{/color}":
             guide6 "…"
             guide6 "Ну… Понимаю?"
             guide4 "В любом случае удачи тебе что ли… Она тебе пригодится, как никому другому…"
             $ app_love_npc -= 40
             $ app_contact_npc -= 40
             $ app_fear_npc -= 40
             $ gg_character = 'Забитый'
         "{color=#000000}На то и нет особых причин. Перешел и перешел – вполне обычное дело. Возможно…{/color}":
             guide4 "Адекватный игрок! Наконец-то!"
             guide8 "А то хулиганы, книжные черви, задроты, казановы…"
             guide12 "Мне уже казалось, что в этом мире более не осталось сбалансированных персонажей, которые пройдут весь достаточно тяжелый и огромный путь с улыбкой на лице!"
             $ dop_stats_authority_gg += 10
             $ dop_stats_forces_gg += 10
             $ dop_stats_agility_gg += 10
             $ dop_stats_lucky_gg += 10
             $ dop_stats_science_gg += 10
             $ dop_stats_stamina_gg += 10
             $ dop_stats_cunning_gg += 10
             $ dop_stats_erudition_gg += 10
             $ informal_view = True
             $ gg_character = 'Обычный'
     guide5 "А теперь..."
     guide5 "Можешь описать свою внешность?"
     label _label_h:
     menu:
         guide5 "Можешь описать свою внешность?"
         "{color=#000000}Я высокого роста.{/color}":
             menu:
                 guide5 "Можешь описать свою внешность?"
                 "{color=#000000}И имею парочку-другую достаточно приметных шрамов, рубцов как на теле, так и на лице.{/color}":
                     $ scars_face = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 10
                     $ dop_stats_authority_gg += 7
                     $ app_fear_npc += 15
                 "{color=#000000}И имею достаточно миловидное лицо, отчего популярен среди женского пола.{/color}":
                     $ pretty_face = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 10
                     $ boost_otn = True
                     $ boost_otn_zn = 20
                 "{color=#000000}И имею достаточно подкаченное тело.{/color}":
                     $ pumped_up_body = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 14
                     $ boost_otn = True
                     $ boost_otn_zn = 13
                 "{color=#000000}И имею недюжинную силу, которая обусловлена крепким телосложением.{/color}":
                     $ remarkable_strength = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 20
                     $ boost_otn = True
                     $ boost_otn_zn = 10
                 "{color=#000000}И имею большой процент подкожного жира{/color}":
                     $ fat = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 17
                     $ dop_stats_stamina_gg -= 10
                     $ dop_stats_agility_gg -= 10
                     $ app_fear_npc += 10
                 "{color=#000000}И имею неплохое сухое тело из-за того,\nчто раньше занимался бегом.{/color}":
                     $ dry_body = True
                     $ high_growth = True
                     $ dop_stats_forces_gg += 10
                     $ dop_stats_stamina_gg += 20
                 "{color=#000000}Назад{/color}":
                     jump _label_h
         "{color=#000000}Я достаточно миниатюрен…{/color}":
             menu:
                 guide5 "Можешь описать свою внешность?"
                 "{color=#000000}И имею парочку-другую достаточно приметных шрамов, рубцов как на теле, так и на лице.{/color}":
                     $ miniature = True
                     $ scars_face = True
                     $ dop_stats_agility_gg += 10
                     $ dop_stats_authority_gg += 7
                     $ app_fear_npc += 15
                 "{color=#000000}И имею достаточно миловидное лицо, отчего популярен среди женского пола.{/color}":
                     $ pretty_face = True
                     $ miniature = True
                     $ dop_stats_forces_gg += 10
                     $ dop_stats_agility_gg += 10
                     $ boost_otn = True
                     $ boost_otn_zn = 20
                 "{color=#000000}И имею неплохое сухое тело из-за того,\nчто раньше занимался бегом.{/color}":
                     $ dry_body = True
                     $ miniature = True
                     $ dop_stats_stamina_gg += 20
                     $ dop_stats_agility_gg += 10
                 "{color=#000000}И имею большой процент подкожного жира{/color}":
                     $ fat = True
                     $ miniature = True
                     $ dop_stats_forces_gg += 5
                     $ dop_stats_stamina_gg -= 10
                     $ boost_otn = True
                     $ boost_otn_zn = 10
                 "{color=#000000}И я… Я немного смахиваю на девчонку…{/color}":
                     if gg_character == 'Хулиган':
                         guide11 "Хулиган-трап?"
                         guide12 "А это вообще законно?"
                         "Нет..."
                         guide4 "Извини, но главный разработчик запрещает делать таких персонажей... Перевыбери все еще раз!"
                         jump _label_h
                     $ miniature = True
                     $ app_contact_npc += 30
                     $ app_contact_npc += 30
                     $ dop_stats_agility_gg += 10
                     $ app_fear_npc -= 10
                     $ trap = True
                 "{color=#000000}Назад{/color}":
                     jump _label_h
         "{color=#000000}Я низкого роста, но при этом коренастый.{/color}":
             menu:
                 guide5 "Можешь описать свою внешность?"
                 "{color=#000000}И имею парочку-другую достаточно приметных шрамов, рубцов как на теле, так и на лице.{/color}":
                     $ stocky = True
                     $ scars_face = True
                     $ dop_stats_stamina_gg += 10
                     $ dop_stats_authority_gg += 7
                     $ app_fear_npc += 15
                 "{color=#000000}И имею достаточно миловидное лицо, отчего популярен среди женского пола.{/color}":
                     $ stocky = True
                     $ pretty_face = True
                     $ dop_stats_stamina_gg += 10
                     $ boost_otn = True
                     $ boost_otn_zn = 20
                 "{color=#000000}И имею большой процент подкожного жира{/color}":
                     $ stocky = True
                     $ fat = True
                     $ dop_stats_forces_gg += 5
                     $ boost_otn = True
                     $ boost_otn_zn = 3
                 "{color=#000000}И имею недюжинную силу, которая обусловлена крепким телосложением.{/color}":
                     $ stocky = True
                     $ remarkable_strength = True
                     $ dop_stats_forces_gg += 10
                     $ dop_stats_stamina_gg += 10
                     $ boost_otn = True
                     $ boost_otn_zn = 10
                 "{color=#000000}И имею достаточно подкаченное тело.{/color}":
                     $ pumped_up_body = True
                     $ stocky = True
                     $ dop_stats_forces_gg += 4
                     $ dop_stats_stamina_gg += 10
                     $ boost_otn = True
                     $ boost_otn_zn = 3
                 "{color=#000000}И имею неплохое сухое тело из-за того,\nчто раньше занимался бегом.{/color}":
                     $ dry_body = True
                     $ stocky = True
                     $ dop_stats_stamina_gg += 30
                     $ dop_stats_agility_gg += 10
                 "{color=#000000}Назад{/color}":
                     jump _label_h
     $ stats_authority_gg_info = stats_authority_gg + dop_stats_authority_gg
     $ stats_forces_gg_info = stats_forces_gg + dop_stats_forces_gg
     $ stats_agility_gg_info = stats_agility_gg + dop_stats_agility_gg
     $ stats_lucky_gg_info = stats_lucky_gg + dop_stats_lucky_gg
     $ stats_stamina_gg_info = stats_stamina_gg + dop_stats_stamina_gg
     $ stats_science_gg_info = stats_science_gg + dop_stats_science_gg
     $ stats_cunning_gg_info = stats_cunning_gg + dop_stats_cunning_gg
     $ stats_erudition_gg_info = stats_erudition_gg + dop_stats_erudition_gg
     guide4 "О как! Интересно..."
     guide3 "Но в любом случае, раз уж мы с этим разобрались, это не так уж и важно на данный момент, так что…"
     guide1 "Скажи мне, какие имена ты хочешь видеть у своих одноклассников?"
     menu:
         guide1 "Скажи мне, какие имена ты хочешь у них видеть?"
         "{color=#000000}Славянского происхождения{/color}":
             guide2 "Эээ… Ладно. Дело твое, мне не жалко."
             $ name_npc = 'Russian'
         "{color=#000000}Японского происхождения{/color}":
             guide4 "А у тебя хороший вкус!"
             $ name_npc = 'Japan'
         "{color=#000000}Американского происхождения{/color}":
             guide5 "Даже так!"
             $ name_npc = 'America'
     guide1 "А сейчас… Скажи мне, хочешь приступить к более глубокой настройке школы?"
     menu:
         guide1 "А сейчас… Скажи мне, хочешь приступить к более глубокой настройке школы?"
         "{color=#000000}Да, конечно.{/color}":
             label _npc_col:
             $ number_npc_max = renpy.input("Какое максимальное количество людей от 10 до 100 ты хочешь видеть в школе?", default =_("60"), allow="1234567890", length=3)
             $ number_npc_max = number_npc_max.strip()
             python:
                 number_npc_max = int(number_npc_max)
                 number_npc_max += 1
             if number_npc_max <= 10:
                 "Это должно быть, как минимум, двузначное число"
                 jump _npc_col
             if Patreon_Code <= 1:
                 if number_npc_max >= 102:
                     "Возможность создания больше сотни персонажей все еще тестируется и доступна только Friend подписчикам патреона."
                     jump _npc_col
             label _npc_col1:
             $ active_npc_p = renpy.input("А какую активность перехода по локациям хочешь им задать от 1 до 5?", default =_("1"), allow="12345", length=1)
             $ active_npc_p = active_npc_p.strip()
             python:
                 active_npc_p = int(active_npc_p)
             if active_npc_p == 0:
                 guide5 "Пожалуйста, введи число от 1 до 5."
                 jump _npc_col1
             guide1 "Твои одноклассники… Они много курят?"
             menu:
                 guide1 "Твои одноклассники… Они много курят?"
                 "{color=#000000}Да":
                     $ smoke_npc_123 = True
                 "{color=#000000}Нет":
                     $ smoke_npc_123 = False
             guide4 "Хм… А что насчет соотношения женского пола к мужскому? Кто преобладает?"
             menu:
                 guide4 "Хм… А что насчет соотношения женского пола к мужскому? Кто преобладает?"
                 "{color=#000000}Мужской{/color}":
                     $ gender_npc_123 = 1
                 "{color=#000000}Женский{/color}":
                     $ gender_npc_123 = 2
                 "{color=#000000}Один к одному{/color}":
                     $ gender_npc_123 = 0
             label _npc_col2:
             $ atribute_npc_123 = renpy.input("А какое у них среднее значение атрибутов от 10 до 100?", default =_("20"), allow="1234567890", length=3)
             $ atribute_npc_123 = atribute_npc_123.strip()
             python:
                 atribute_npc_123 = int(atribute_npc_123)
             if atribute_npc_123 <= 9 or atribute_npc_123 >= 101:
                 guide5 "Пожалуйста, введи число от 10 до 100."
                 jump _npc_col2
             guide3 "И…"
             guide5 "Сделано!"
             $ dialoge = 0
             $ id_npc = 0
             $ smoking_npc = 0
             $ smok_npc = 0
             jump _random_npc
         "{color=#000000}Рассчитай все по среднестатистическому значению. Не хочу лезть в дебри этого генератора...{/color}":
             $ atribute_npc_123 = 0
             $ gender_npc_123 = 0
             $ active_npc_p = 0
             $ smoke_npc_123 = False
             guide3 "И…"
             guide5 "Сделано!"
             $ number_npc_max = 100
             $ dialoge = 0
             $ id_npc = 0
             $ smoking_npc = 0
             $ smok_npc = 0
             jump _random_npc
     call screen create_character
screen create_character:
     frame:
         $ stats_authority_gg_info = stats_authority_gg + dop_stats_authority_gg
         $ stats_forces_gg_info = stats_forces_gg + dop_stats_forces_gg
         $ stats_agility_gg_info = stats_agility_gg + dop_stats_agility_gg
         $ stats_lucky_gg_info = stats_lucky_gg + dop_stats_lucky_gg
         $ stats_stamina_gg_info = stats_stamina_gg + dop_stats_stamina_gg
         if stats_forces_gg_info <= 10:
             $ stats_forces_gg_info = 10
         if stats_agility_gg_info <= 10:
             $ stats_agility_gg_info = 10
         $ standart_mod_attack_gg = 20
         $ damage_gg = stats_forces_gg_info / 2 + standart_mod_attack_gg
         $ damage_gg_info = dop_damage_gg + damage_gg
         $ points_hp_gg = 100 + (stats_stamina_gg_info / 2)
         $ poins_hp_max_gg = points_hp_gg
         $ mod_speed_attack_gg = 100
         $ speed_attack_gg = float(mod_speed_attack_gg) / 4 / stats_agility_gg_info
         $ speed_attack_info = round(speed_attack_gg, 2)
         $ standart_mod_attack_gg = 20
         $ damage_gg = stats_forces_gg_info / 2 + standart_mod_attack_gg
         $ block_damage_gg = 100 / (stats_stamina_gg_info / 2)
         $ block_damage_info = 100 / int(block_damage_gg)
         $ miss_chance_gg = 100 / (stats_agility_gg_info / 2)
         $ miss_chance_info = 100/miss_chance_gg
         $ accuracy_gg = 100 / float(stats_agility_gg_info / 4)
         $ accuracy_info = 100 / int(accuracy_gg)
         $ punch_gg = float(2.5) / speed_attack_gg
         $ knockdown_gg = 100 / float(stats_forces_gg_info / 6)
         $ knockdown_info = 100 / int(knockdown_gg)
         $ critical_damage_gg = 100 / float(stats_lucky_gg_info / 4)
         $ critical_damage_info = 100 / int(critical_damage_gg)
         $ speed_education = 9 + stats_science_gg / 3
         $ larceny = 9 + (stats_cunning_gg + stats_agility_gg_info + stats_lucky_gg_info) / 10
         $ movement_speed = 7 + (stats_stamina_gg_info + stats_agility_gg_info) / 5
         $ app = (stats_erudition_gg + stats_science_gg) / 5
         $ app_info = app + dop_app
         $ mod_horror = abs(stats_forces_gg + stats_agility_gg) / 5 - app + dop_mod_horror
         $ games_chance = 7 + (stats_lucky_gg_info + stats_cunning_gg) / 5
         $ charisma = (stats_science_gg / 10) + (stats_erudition_gg / 2) + (stats_cunning_gg / 2) + (app / 4) - 9
         pass
     add "gui/frame.png" xalign 0 yalign 0:
         size(500, 690)
     add "gui/frame.png" xpos 1350 ypos 419:
         size(570, 690)
     add "gui/frame.png" xalign 0.34 yalign 0:
         size(540, 690)
     add "gui/frame.png" xpos 1007 yalign 0:
         size(600, 425)
     add "gui/frame.png" xpos 1500 yalign 0:
         size(500, 425)
     add "gui/frame.png" xpos 1007 ypos 421:
         size(343, 670)
     if language_game == 1:
         vbox xalign 0.01 yalign 0.02:
             spacing -1
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}                    {b}Атрибуты:{/b}\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Сила: [stats_forces_gg]\n{/color}{/size}{/font}                     "
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Ловкость: [stats_agility_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Выносливость: [stats_stamina_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Интеллект: [stats_science_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Хитроумие: [stats_cunning_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Авторитет: [stats_authority_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Красноречие: [stats_erudition_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Удача: [stats_lucky_gg]\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000} Нераспределенных очков: {b}[points_stats]{/b}{/color}{/size}{/font}     "
         vbox xalign 0.34 yalign 0.02:
             spacing -1
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}         {b} Доп. особенности:{/b}\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Барыга\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Волк-одиночка\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Крепкий желудок\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Политик\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Зомби\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Тяжелая рука\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}   Дамский угодник\n\n\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Нераспределенных очков перков: {b}[points_perk]{/b}{/color}{/size}{/font}" xalign 0.99 yalign 0.99 size 30
         vbox xalign 0.69 yalign 0.015:
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}Особенности внешности:{/b}\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Высокий рост\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Шрамы на лице\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Миниатюрное тело\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Ординарность\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}Коренастость\n{/color}{/size}{/font}"
         vbox xalign 0.64 yalign 0.6:
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}        Выбранное\nперки/особенности\n        внешности.{/b}\n{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}{b}           Перки:{b}{/color}{/size}{/font}"
             if huckster == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}                 Барыга{/color}{/size}{/font}"
             if loner == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}        Волк-одиночка{/color}{/size}{/font}"
             if stomach == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}      Крепкий желудок{/color}{/size}{/font}"
             if politic == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}               Политик{/color}{/size}{/font}"
             if zombie == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}                 Зомби{/color}{/size}{/font}"
             if heavy_arm == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}          Тяжелая рука{/color}{/size}{/font}"
             if ladies_man == True:
                 text "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}      Дамский угодник{/color}{/size}{/font}"
             text "{font=gui/fonts/ubuntu.ttf}{size=26}{color=#000000}\n{b}{size=29}     Особенности\n       внешности:{/size}{/b}{/color}{/size}{/font}"
             if high_growth == True:
                 text  "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}          Высокий рост{/color}{/size}{/font}"
             if scars_face == True:
                 text  "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}        Шрамы на лице{/color}{/size}{/font}"
             if miniature == True:
                 text  "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}    Миниатюрное тело{/color}{/size}{/font}"
             if informal_view == True:
                 text  "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}         Ординарность{/color}{/size}{/font}"
             if stocky == True:
                 text  "{font=gui/fonts/ubuntu.ttf}{size=27}{color=#000000}          Коренастость{/color}{/size}{/font}"
     elif language_game == 2:
         vbox xalign 0.01 yalign 0.02:
             text "                    {b}Attribute{/b}\n"
             text "   Strength: [stats_forces_gg]\n                     "
             text "   Dexterity: [stats_agility_gg]\n"
             text "   Stamina: [stats_stamina_gg]\n"
             text "   Intelligence: [stats_science_gg]\n"
             text "   Cunning: [stats_cunning_gg]\n"
             text "   Authority: [stats_authority_gg]\n"
             text "   Eloquence: [stats_erudition_gg]\n"
             text "   Lucky: [stats_lucky_gg]\n"
             text " Нераспределенных очков: {b}[points_stats]{/b}     "
         vbox xalign 0.34 yalign 0.02:
             text "         {b} Доп. особенности:{/b}\n"
             text "   Huckster\n"
             text "   a lone Wolf\n"
             text "   a Strong stomach\n"
             text "   Policy\n"
             text "   Zombie\n"
             text "   Heavy hand\n"
             text "   Ladies' man\n\n\n"
             text "Unallocated points perks: {b}[points_perk]{/b}" xalign 0.99 yalign 0.99 size 30
         vbox xalign 0.69 yalign 0.015:
             text "{b}Appearance Features:{/b}\n"
             text "Tall\n"
             text "Scars on the face\n"
             text "Miniature body\n"
             text "Ordinary\n"
             text "Chunky\n"
         vbox xalign 0.64 yalign 0.6:
             text "{b}        Выбранное\nперки/особенности\n        внешности.{/b}\n"
             text "{b}           Перки:{b}"
             if huckster == True:
                 text "                 Huckster"
             if loner == True:
                 text "        a lone Wolf"
             if stomach == True:
                 text "      a Strong stomach"
             if politic == True:
                 text "               Policy"
             if zombie == True:
                 text "                 Zombie"
             if heavy_arm == True:
                 text "          Heavy hand"
             if ladies_man == True:
                 text "      Ladies' man"
             text "\n{b}{size=29}       Особенности\n         внешности:{/size}{/b}"
             if high_growth == True:
                 text  "          Высокий рост"
             if scars_face == True:
                 text  "         Шрамы на лице"
             if miniature == True:
                 text  "    Миниатюрное тело"
             if informal_view == True:
                 text  "          Ординарность"
             if stocky == True:
                 text  "          Коренастость"
     imagebutton xalign 0.99 yalign 0.3:
         idle ("icons/icons_next.png")
         hover ("icons/icons_next_hover.png")
         action SensitiveIf(points_perk <= 0 and vn_gg <= 0 and points_stats <= 0), Jump('rr_npc')
     if points_perk >= 1:
         text "{color=#000000}Определитесь с\nособенностями\nвнешности{/color}" xalign 0.99 yalign 0.17 size 24
     if vn_gg >= 1:
         text "{color=#000000}Распределите очки\nатрибутов{/color}" xalign 0.96 yalign 0.25 size 24
     if points_stats >= 1:
         text "{color=#000000}Распределите\nочки перков{/color}" xalign 0.91 yalign 0.32 size 24
     viewport:
         xalign 0.01 yalign 0.99 xysize (990, 325)
         child_size (950, 325)
         scrollbars "vertical"
         spacing 20
         draggable True
         mousewheel True
         arrowkeys True
         if help == 1:
             text "{color=#000000}Сила характерна персонажам, что решают свои проблемы насильственными методами. Хочешь ударить - бей.\nСила влияет на шанс нокдауна, урон, а также на модификатор жуткости.{/color}"
         elif help == 2:
             text "{color=#000000}Ловкость является неотъемлемым атрибутом для персонажей, что не привыкли получать постоянно от других оплеухи.\n Влияет на шанс точность, шанс уворота и скорость атаки.{/color}"
         elif help == 10:
             text "{color=#000000}Во многих странах ценится высокий рост, что вполне хорошо может сказаться на отношения между противоположным полом. Кроме того высокие люди имеют длинные мышечные волокна, делающие их сильнее при совершенно том же весе, что и их братьев меньших.\nДобавляет силу и привлекательность, но убавляет ловкость.{/color}"
         elif help == 11:
             text "{color=#000000}Навряд ли шрамы можно назвать чем-то эстетичным, но это может добавить авторитет, да и выглядеть более угрожающе при присутствие на лице пару тройки шрамов - дело обычное.{/color}"
         elif help == 12:
             text "{color=#000000}Миниатюрность для мужского пола многие могут назвать чем-то непривлекательным, но есть так же и люди, которым нравятся маленькие люди.\nДобавляет ловкости, но сила уменьшается.{/color}"
         elif help == 13:
             text "{color=#000000}Многие люди с непримечательной внешностью - счастливчики. В конце-то концов кому нужно это лишнее внимание от других людей за счет каких-то особенностей внешности?{/color}"
         elif help == 14:
             text "{color=#000000}Быть мелким и крепким - достаточно удобно, ведь ты не только очень вынослив, но и в некотором роде силен физически. Одна проблема: девушки все так же нечасто обращают на вас внимание...{/color}"
         elif help == 15:
             text "{color=#000000}Быть жадным, считать каждую копейку, но при этом всегда иметь при себе деньги - прерогатива барыг, которой они пользуются постоянно.\nПоявляется возможность переторговывать вещички подороже на барахолках.{/color}"
         elif help == 16:
             text "{color=#000000}Социализация - бред, навязанный обществом. По крайней мере так считаете вы.\nБлокирует прокачку красноречия, но дает постоянную прибавку к другим атрибутам, так еще и в начале дает дополнительных 20 поинтов на распределение.{/color}"
         elif help == 17:
             text "{color=#000000}Жрать все подряд и при этом не бояться изжоги/язвы и других неприятностей - вот что хотел бы каждый небогатый студент в свои годы. В конце-то концов переносимость фастфуда есть не у всех.{/color}"
         elif help == 18:
             text "{color=#000000}Бывает, что скупость и жадность достигает пред... Кхм... Будучи политиком, вы получаете постоянный бонус к авторитету, а также имеете дополнительные выходы из некоторых сложных ситуаций.{/color}"
         elif help == 19:
             text "{color=#000000}Правда ли выстрел в голову вас убьет?\nДает огромные бонусы к выносливости, но при этом блокирует прокачку силы.{/color}"
         elif help == 20:
             text "{color=#000000}Кому хочется вырубать людей направо и налево? Так вот, тяжелый кулак - ваш выбор, но будьте осторожны и случайно не сломайте кому-то челюсть!{/color}"
         elif help == 21:
             text "{color=#000000}Повышает уровень отношений с персонажами женского пола на 40 очков.{/color}"
     viewport:
         xalign 0.99 yalign 0.99 xysize (550, 640)
         child_size (500, 260)
         scrollbars "vertical"
         spacing 20
         draggable True
         mousewheel True
         arrowkeys True
         vbox xalign 0.06 yalign 0.85:
             text "{color=#000000}{b}Статистика боевых навыков:{/b}\n{/color}"
             text "{color=#000000}Очки здоровья: [points_hp_gg]{/color}"
             text "{color=#000000}Скорость атаки: [speed_attack_info]{/color}"
             text "{color=#000000}Урон: [damage_gg_info]{/color}"
             text "{color=#000000}Блокировка входящего урона: [block_damage_info]%{/color}"
             text "{color=#000000}Шанс уворота: [miss_chance_info]%{/color}"
             text "{color=#000000}Точность: [accuracy_info]%{/color}"
             text "{color=#000000}Нокдаун: [knockdown_info]%{/color}"
             text "{color=#000000}Критический удар: [critical_damage_info]%\n{/color}"
             text "{color=#000000}{b}Статистика нейтральных навыков:{/b}\n{/color}"
             text "{color=#000000}Скорость обучения: [speed_education]%{/color}"
             text "{color=#000000}Кража: [larceny]%{/color}"
             text "{color=#000000}Скорость передвижения: [movement_speed]%{/color}"
             text "{color=#000000}Азартные игры: [games_chance]%{/color}"
             text "{color=#000000}Харизматичность: [charisma]%{/color}"
             text "{color=#000000}Модификатор привлекательности [app_info]%{/color}"
             text "{color=#000000}Модификатор жуткости [mod_horror]%{/color}"
     text "{color=#000000}{size=36}{b}Описание:{/b}{/size}{/color}" xalign 0.23 yalign 0.675
     hbox xalign 0.17 yalign 0.065:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_forces_gg >= 21), SetVariable("stats_forces_gg", stats_forces_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1 and zombie == False), SetVariable("stats_forces_gg", stats_forces_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 1)
     hbox xalign 0.17 yalign 0.13:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_agility_gg >= 21), SetVariable("stats_agility_gg", stats_agility_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_agility_gg", stats_agility_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 2)
     hbox xalign 0.17 yalign 0.197:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_stamina_gg >= 21), SetVariable("stats_stamina_gg", stats_stamina_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_stamina_gg", stats_stamina_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 3)
     hbox xalign 0.17 yalign 0.262:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_science_gg >= 21), SetVariable("stats_science_gg", stats_science_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_science_gg", stats_science_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 4)
     hbox xalign 0.17 yalign 0.328:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_cunning_gg >= 21), SetVariable("stats_cunning_gg", stats_cunning_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_cunning_gg", stats_cunning_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 5)
     hbox xalign 0.17 yalign 0.394:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_authority_gg >= 21), SetVariable("stats_authority_gg", stats_authority_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_authority_gg", stats_authority_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 6)
     hbox xalign 0.17 yalign 0.46:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_erudition_gg >= 21), SetVariable("stats_erudition_gg", stats_erudition_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf(points_stats >= 1 and loner == False), SetVariable("stats_erudition_gg", stats_erudition_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 7)
     hbox xalign 0.17 yalign 0.525:
             imagebutton:
                 idle ("icons/icons_minus.png")
                 hover ("icons/icons_minus_hover.png")
                 action SensitiveIf(stats_lucky_gg >= 21), SetVariable("stats_lucky_gg", stats_lucky_gg-1), SetVariable('points_stats', points_stats+1)
             imagebutton:
                 idle ("icons/icons_plus.png")
                 hover ("icons/icons_plus_hover.png")
                 action SensitiveIf( points_stats >= 1), SetVariable("stats_lucky_gg", stats_lucky_gg+1), SetVariable('points_stats', points_stats-1)
             imagebutton:
                 idle ("icons/icons_menu_question.png")
                 hover ("icons/icons_menu_question_hover.png")
                 action SetVariable("help", 8)
     hbox xalign 0.45 yalign 0.065:
         imagebutton:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(huckster == True), SetVariable("points_perk", points_perk+1), SetVariable("huckster", False)
         imagebutton:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and huckster == False), SetVariable("points_perk", points_perk-1), SetVariable("huckster", True)
         imagebutton:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 15)
     hbox xalign 0.45 yalign 0.13:
         imagebutton xalign 0.8 yalign 0.675:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(loner == True), SetVariable("points_perk", points_perk+1), SetVariable("loner", False), SetVariable("points_stats", 20), SetVariable("stats_lucky_gg", 20), SetVariable("stats_erudition_gg", 20), SetVariable("stats_authority_gg", 20), SetVariable("stats_cunning_gg", 20), SetVariable("stats_forces_gg", 20), SetVariable("stats_agility_gg", 20), SetVariable("stats_stamina_gg", 20), SetVariable("stats_science_gg ", 20)
         imagebutton xalign 0.77 yalign 0.675:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and loner == False), SetVariable("points_perk", points_perk-1), SetVariable("loner", True), SetVariable("points_stats", stats_erudition_gg - 20 + points_stats + 20), SetVariable("stats_erudition_gg", 10)
         imagebutton xalign 0.74 yalign 0.675:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 16)
     hbox xalign 0.45 yalign 0.194:
         imagebutton xalign 0.8 yalign 0.725:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(stomach == True), SetVariable("points_perk", points_perk+1), SetVariable("stomach", False)
         imagebutton xalign 0.77 yalign 0.725:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and stomach == False), SetVariable("points_perk", points_perk-1), SetVariable("stomach", True)
         imagebutton xalign 0.74 yalign 0.725:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 17)
     hbox xalign 0.45 yalign 0.259:
         imagebutton xalign 0.8 yalign 0.775:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(politic == True), SetVariable("points_perk", points_perk+1), SetVariable("politic", False), SetVariable("stats_authority_gg", stats_authority_gg - 20)
         imagebutton xalign 0.77 yalign 0.775:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and politic == False), SetVariable("points_perk", points_perk-1), SetVariable("politic", True), SetVariable("stats_authority_gg", stats_authority_gg + 20)
         imagebutton xalign 0.74 yalign 0.775:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 18)
     hbox xalign 0.45 yalign 0.326:
         imagebutton xalign 0.8 yalign 0.825:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(zombie == True), SetVariable("points_perk", points_perk+1), SetVariable("zombie", False), SetVariable("stats_forces_gg", 20), SetVariable("stats_stamina_gg", stats_stamina_gg-60)
         imagebutton xalign 0.77 yalign 0.825:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and zombie == False), SetVariable("points_perk", points_perk-1), SetVariable("zombie", True), SetVariable("points_stats", stats_forces_gg - 20 + points_stats), SetVariable("stats_forces_gg", 10), SetVariable("stats_stamina_gg", stats_stamina_gg+60)
         imagebutton xalign 0.74 yalign 0.825:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 19)
     hbox xalign 0.45 yalign 0.392:
         imagebutton:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(heavy_arm == True), SetVariable("points_perk", points_perk+1), SetVariable("heavy_arm", False), SetVariable("dop_damage_gg", damage_gg-5)
         imagebutton:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and heavy_arm == False), SetVariable("points_perk", points_perk-1), SetVariable("heavy_arm", True), SetVariable("dop_damage_gg", damage_gg+5)
         imagebutton:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 20)
     hbox xalign 0.45 yalign 0.46:
         imagebutton:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(ladies_man == True), SetVariable("points_perk", points_perk+1), SetVariable("ladies_man", False)
         imagebutton:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(points_perk >= 1 and ladies_man == False), SetVariable("points_perk", points_perk-1), SetVariable("ladies_man", True)
         imagebutton:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 21)
     hbox xalign 0.76 yalign 0.135:
         imagebutton xalign 0.2 yalign 0.675:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(scars_face == True), SetVariable("vn_gg", vn_gg+1), SetVariable("scars_face", False), SetVariable("mod_horror", mod_horror-5), SetVariable("stats_authority_gg", stats_authority_gg-10)
         imagebutton xalign 0.23 yalign 0.675:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(vn_gg >= 1 and scars_face == False), SetVariable("vn_gg", vn_gg-1), SetVariable("scars_face", True), SetVariable("mod_horror", mod_horror+5), SetVariable("stats_authority_gg", stats_authority_gg+10)
         imagebutton xalign 0.26 yalign 0.675:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 11)
     hbox xalign 0.76 yalign 0.07:
         imagebutton xalign 0.2 yalign 0.625:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action [SensitiveIf(high_growth == True), SetVariable("vn_gg", vn_gg+1), SetVariable("dop_app", dop_app-5), SetVariable("high_growth", False), SetVariable("stats_forces_gg", stats_forces_gg-7), SetVariable("stats_agility_gg", stats_agility_gg+7)]
         imagebutton xalign 0.23 yalign 0.625:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action [SensitiveIf(vn_gg >= 1 and miniature == False and high_growth == False), SetVariable("dop_app", dop_app+5), SetVariable("vn_gg", vn_gg-1), SetVariable("high_growth", True), SetVariable("stats_forces_gg", stats_forces_gg+7), SetVariable("stats_agility_gg", stats_agility_gg-7)]
         imagebutton xalign 0.26 yalign 0.625:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 10)
     hbox xalign 0.76 yalign 0.202:
         imagebutton xalign 0.2 yalign 0.725:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(miniature == True), SetVariable("vn_gg", vn_gg+1), SetVariable("miniature", False), SetVariable("stats_agility_gg", stats_agility_gg-7), SetVariable("stats_forces_gg", stats_forces_gg+7)
         imagebutton xalign 0.23 yalign 0.725:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(vn_gg >= 1 and high_growth == False and miniature == False), SetVariable("vn_gg", vn_gg-1), SetVariable("miniature", True), SetVariable("stats_agility_gg", stats_agility_gg+7), SetVariable("stats_forces_gg", stats_forces_gg-7)
         imagebutton xalign 0.26 yalign 0.725:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 12)
     hbox xalign 0.76 yalign 0.267:
         imagebutton xalign 0.2 yalign 0.775:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(informal_view == True), SetVariable("vn_gg", vn_gg+1), SetVariable("informal_view", False), SetVariable("stats_lucky_gg", stats_lucky_gg-8)
         imagebutton xalign 0.23 yalign 0.775:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(vn_gg >= 1 and informal_view == False), SetVariable("vn_gg", vn_gg-1), SetVariable("informal_view", True), SetVariable("stats_lucky_gg", stats_lucky_gg+8)
         imagebutton xalign 0.26 yalign 0.775:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 13)
     hbox xalign 0.76 yalign 0.334:
         imagebutton xalign 0.2 yalign 0.825:
             idle ("icons/icons_minus.png")
             hover ("icons/icons_minus_hover.png")
             action SensitiveIf(stocky == True), SetVariable("vn_gg", vn_gg+1), SetVariable("stocky", False), SetVariable("stats_stamina_gg", stats_stamina_gg-8)
         imagebutton xalign 0.23 yalign 0.825:
             idle ("icons/icons_plus.png")
             hover ("icons/icons_plus_hover.png")
             action SensitiveIf(vn_gg >= 1 and stocky == False), SetVariable("vn_gg", vn_gg-1), SetVariable("stocky", True), SetVariable("stats_stamina_gg", stats_stamina_gg+8)
         imagebutton xalign 0.26 yalign 0.825:
             idle ("icons/icons_menu_question.png")
             hover ("icons/icons_menu_question_hover.png")
             action SetVariable("help", 14)
     key 'shift_alt_K_F12' action Jump("rr_npc")
screen menu_character:
     key 'shift_alt_K_F12' action Jump("rr_npc")
     $ stats_authority_gg_info = stats_authority_gg + dop_stats_authority_gg
     $ stats_forces_gg_info = stats_forces_gg + dop_stats_forces_gg
     $ stats_agility_gg_info = stats_agility_gg + dop_stats_agility_gg
     $ stats_lucky_gg_info = stats_lucky_gg + dop_stats_lucky_gg
     $ stats_stamina_gg_info = stats_stamina_gg + dop_stats_stamina_gg
     if stats_forces_gg_info <= 10:
         $ stats_forces_gg_info = 10
     if stats_agility_gg_info <= 10:
         $ stats_agility_gg_info = 10
     $ standart_mod_attack_gg = 20
     $ damage_gg = stats_forces_gg_info / 2 + standart_mod_attack_gg
     $ damage_gg_info = dop_damage_gg + damage_gg
     $ points_hp_gg = 100 + (stats_stamina_gg_info / 2)
     $ poins_hp_max_gg = points_hp_gg
     $ mod_speed_attack_gg = 100
     $ speed_attack_gg = float(mod_speed_attack_gg) / 4 / stats_agility_gg_info
     $ speed_attack_info = round(speed_attack_gg, 2)
     $ standart_mod_attack_gg = 20
     $ damage_gg = stats_forces_gg_info / 2 + standart_mod_attack_gg
     $ block_damage_gg = 100 / (stats_stamina_gg_info / 2)
     $ block_damage_info = 100 / int(block_damage_gg)
     $ miss_chance_gg = 100 / (stats_agility_gg_info / 2)
     $ miss_chance_info = 100/miss_chance_gg
     $ accuracy_gg = 100 / float(stats_agility_gg_info / 4)
     $ accuracy_info = 100 / int(accuracy_gg)
     $ punch_gg = float(2.5) / speed_attack_gg
     $ knockdown_gg = 100 / float(stats_forces_gg_info / 6)
     $ knockdown_info = 100 / int(knockdown_gg)
     $ critical_damage_gg = 100 / float(stats_lucky_gg_info / 4)
     $ critical_damage_info = 100 / int(critical_damage_gg)
     $ speed_education = 9 + stats_science_gg / 3
     $ larceny = 9 + (stats_cunning_gg + stats_agility_gg_info + stats_lucky_gg_info) / 10
     $ movement_speed = 7 + (stats_stamina_gg_info + stats_agility_gg_info) / 5
     $ app = (stats_erudition_gg + stats_science_gg) / 5
     $ app_info = app + dop_app
     $ mod_horror = abs(stats_forces_gg + stats_agility_gg) / 5 - app + dop_mod_horror
     $ games_chance = 7 + (stats_lucky_gg_info + stats_cunning_gg) / 5
     $ charisma = (stats_science_gg / 10) + (stats_erudition_gg / 2) + (stats_cunning_gg / 2) + (app / 4) - 9
     #атрибуты
     if language_game == 2:
         text "{b}Attributes:{/b}" xalign 0.1 yalign 0.02 size 32
         text "Strength: [stats_forces_gg_info]" xalign 0.01 yalign 0.07 size 32
         text "Agility: [stats_agility_gg_info]" xalign 0.01 yalign 0.12 size 32
         text "Stamina: [stats_stamina_gg_info]" xalign 0.01 yalign 0.17 size 32
         text "Intellect: [stats_science_gg]" xalign 0.01 yalign 0.22 size 32
         text "Cunning: [stats_cunning_gg]" xalign 0.01 yalign 0.27 size 32
         text "Authority: [stats_authority_gg_info]" xalign 0.01 yalign 0.32 size 32
         text "Oratory: [stats_erudition_gg]" xalign 0.01 yalign 0.37 size 32
         text "Lucky: [stats_lucky_gg_info]" xalign 0.01 yalign 0.42 size 32
         text "Unallocated points: {b}[points_stats]{/b}" xalign 0.01 yalign 0.48 size 32
     elif language_game == 1:
         text "{b}Атрибуты:{/b}" xalign 0.1 yalign 0.02 size 32
         text "Сила: [stats_forces_gg_info]" xalign 0.01 yalign 0.07 size 32
         text "Ловкость: [stats_agility_gg_info]" xalign 0.01 yalign 0.12 size 32
         text "Выносливость: [stats_stamina_gg_info]" xalign 0.01 yalign 0.17 size 32
         text "Интеллект: [stats_science_gg]" xalign 0.01 yalign 0.22 size 32
         text "Хитроумие: [stats_cunning_gg]" xalign 0.01 yalign 0.27 size 32
         text "Авторитет: [stats_authority_gg_info]" xalign 0.01 yalign 0.32 size 32
         text "Красноречие: [stats_erudition_gg]" xalign 0.01 yalign 0.37 size 32
         text "Удача: [stats_lucky_gg_info]" xalign 0.01 yalign 0.42 size 32
         text "Нераспределенных очков: {b}[points_stats]{/b}" xalign 0.01 yalign 0.48 size 32
     imagebutton xalign 0.2 yalign 0.065:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_forces_gg >= 21), SetVariable("stats_forces_gg", stats_forces_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.065:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1 and zombie == False), SetVariable("stats_forces_gg", stats_forces_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.065:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 1)
     imagebutton xalign 0.2 yalign 0.115:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_agility_gg >= 21), SetVariable("stats_agility_gg", stats_agility_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.115:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_agility_gg", stats_agility_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.115:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 2)
     imagebutton xalign 0.2 yalign 0.165:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_stamina_gg >= 21), SetVariable("stats_stamina_gg", stats_stamina_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.165:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_stamina_gg", stats_stamina_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.165:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 3)
     imagebutton xalign 0.2 yalign 0.215:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_science_gg >= 21), SetVariable("stats_science_gg", stats_science_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.215:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_science_gg", stats_science_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.215:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 4)
     imagebutton xalign 0.2 yalign 0.265:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_cunning_gg >= 21), SetVariable("stats_cunning_gg", stats_cunning_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.265:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_cunning_gg", stats_cunning_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.265:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 5)
     imagebutton xalign 0.2 yalign 0.315:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_authority_gg >= 21), SetVariable("stats_authority_gg", stats_authority_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.315:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_authority_gg", stats_authority_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.315:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 6)
     imagebutton xalign 0.2 yalign 0.365:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_erudition_gg >= 21), SetVariable("stats_erudition_gg", stats_erudition_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.365:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_stats >= 1 and loner == False), SetVariable("stats_erudition_gg", stats_erudition_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.365:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 7)
     imagebutton xalign 0.2 yalign 0.415:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stats_lucky_gg >= 21), SetVariable("stats_lucky_gg", stats_lucky_gg-1), SetVariable('points_stats', points_stats+1)
     imagebutton xalign 0.23 yalign 0.415:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf( points_stats >= 1), SetVariable("stats_lucky_gg", stats_lucky_gg+1), SetVariable('points_stats', points_stats-1)
     imagebutton xalign 0.26 yalign 0.415:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 8)
     #подсчет боевых навыков
     if language_game == 1:
         text "{b}Статистика боевых навыков:{/b}" xalign 0.45 yalign 0.02 size 32
         text "Очки здоровья: [points_hp_gg]" xalign 0.45 yalign 0.07 size 32
         text "Скорость атаки: [speed_attack_info]" xalign 0.45 yalign 0.17 size 32
         text "Урон: [damage_gg_info]" xalign 0.45 yalign 0.12 size 32
         text "Блокировка входящего урона: [block_damage_info]%" xalign 0.45 yalign 0.22 size 32
         text "Шанс уворота: [miss_chance_info]%" xalign 0.45 yalign 0.27 size 32
         text "Точность: [accuracy_info]%" xalign 0.45 yalign 0.32 size 32
         text "Нокдаун: [knockdown_info]%" xalign 0.45 yalign 0.37 size 32
         text "Критический удар: [critical_damage_info]%" xalign 0.45 yalign 0.42 size 32
     elif language_game == 2:
         text "{b}Statistics of combat skills:{/b}" xalign 0.45 yalign 0.02 size 32
         text "Points HP: [points_hp_gg]" xalign 0.45 yalign 0.07 size 32
         text "Speed attack: [speed_attack_info]" xalign 0.45 yalign 0.17 size 32
         text "Damage: [damage_gg_info]" xalign 0.45 yalign 0.12 size 32
         text "Block incoming damage: [block_damage_info]%" xalign 0.45 yalign 0.22 size 32
         text "Miss chance: [miss_chance_info]%" xalign 0.45 yalign 0.27 size 32
         text "Accuracy: [accuracy_info]%" xalign 0.45 yalign 0.32 size 32
         text "Knockdown: [knockdown_info]%" xalign 0.45 yalign 0.37 size 32
         text "Critical damage: [critical_damage_info]%" xalign 0.45 yalign 0.42 size 32
     #подсчет нейтральных навыков
     if language_game == 1:
         text "{b}Статистика нейтральных навыков:{/b}" xalign 0.48 yalign 0.57 size 32
         text "Скорость обучения: [speed_education]%" xalign 0.48 yalign 0.62 size 32
         text "Кража: [larceny]%" xalign 0.48 yalign 0.72 size 32
         text "Скорость передвижения: [movement_speed]%" xalign 0.48 yalign 0.67 size 32
         text "Азартные игры: [games_chance]%" xalign 0.48 yalign 0.77 size 32
         text "Харизматичность: [charisma]%" xalign 0.48 yalign 0.82 size 32
         text "Модификатор привлекательности [app_info]%" xalign 0.48 yalign 0.87 size 32
         text "Модификатор жуткости [mod_horror]%" xalign 0.48 yalign 0.92 size 32
     elif language_game == 2:
         text "{b}Neutral Skills Statistics:{/b}" xalign 0.48 yalign 0.57 size 32
         text "Speed education: [speed_education]%" xalign 0.48 yalign 0.62 size 32
         text "Larceny: [larceny]%" xalign 0.48 yalign 0.72 size 32
         text "Movement speed: [movement_speed]%" xalign 0.48 yalign 0.67 size 32
         text "Games of chance: [games_chance]%" xalign 0.48 yalign 0.77 size 32
         text "Charisma: [charisma]%" xalign 0.48 yalign 0.82 size 32
         text "Attractiveness modifier [app_info]%" xalign 0.48 yalign 0.87 size 32
         text "Eerie modifier [mod_horror]%" xalign 0.48 yalign 0.92 size 32
     #перки внешности
     if language_game == 1:
         text "{b}Особенности внешности:{/b}" xalign 0.01 yalign 0.57 size 32
         text "Высокий рост" xalign 0.01 yalign 0.62 size 32
     elif language_game == 2:
         text "{b}Appearance features:{/b}" xalign 0.01 yalign 0.57 size 32
         text "High growth" xalign 0.01 yalign 0.62 size 32
     imagebutton xalign 0.2 yalign 0.625:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action [SensitiveIf(high_growth == True), SetVariable("vn_gg", vn_gg+1), SetVariable("dop_app", dop_app-5), SetVariable("high_growth", False), SetVariable("dop_stats_forces_gg", dop_stats_forces_gg-7), SetVariable("dop_stats_agility_gg", dop_stats_agility_gg+7)]
     imagebutton xalign 0.23 yalign 0.625:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action [SensitiveIf(vn_gg >= 1 and miniature == False and high_growth == False), SetVariable("dop_app", dop_app+5), SetVariable("vn_gg", vn_gg-1), SetVariable("high_growth", True), SetVariable("dop_stats_forces_gg", dop_stats_forces_gg+7), SetVariable("dop_stats_agility_gg", dop_stats_agility_gg-7)]
     imagebutton xalign 0.26 yalign 0.625:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 10)
     if language_game == 1:
         text "Шрамы на лице" xalign 0.01 yalign 0.67 size 32
     elif language_game == 2:
         text "Facial scars" xalign 0.01 yalign 0.67 size 32
     imagebutton xalign 0.2 yalign 0.675:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(scars_face == True), SetVariable("vn_gg", vn_gg+1), SetVariable("scars_face", False), SetVariable("dop_mod_horror", dop_mod_horror-5), SetVariable("dop_stats_authority_gg", dop_stats_authority_gg-10)
     imagebutton xalign 0.23 yalign 0.675:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(vn_gg >= 1 and scars_face == False), SetVariable("vn_gg", vn_gg-1), SetVariable("scars_face", True), SetVariable("dop_mod_horror", dop_mod_horror+5), SetVariable("dop_stats_authority_gg", dop_stats_authority_gg+10)
     imagebutton xalign 0.26 yalign 0.675:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 11)
     if language_game == 1:
         text "Миниатюрное тело" xalign 0.01 yalign 0.72 size 32
     elif language_game == 2:
         text "Miniature body" xalign 0.01 yalign 0.72 size 32
     imagebutton xalign 0.2 yalign 0.725:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(miniature == True), SetVariable("vn_gg", vn_gg+1), SetVariable("miniature", False), SetVariable("dop_stats_agility_gg", dop_stats_agility_gg-7), SetVariable("dop_stats_forces_gg", dop_stats_forces_gg+7)
     imagebutton xalign 0.23 yalign 0.725:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(vn_gg >= 1 and high_growth == False and miniature == False), SetVariable("vn_gg", vn_gg-1), SetVariable("miniature", True), SetVariable("dop_stats_agility_gg", dop_stats_agility_gg+7), SetVariable("dop_stats_forces_gg", dop_stats_forces_gg-7)
     imagebutton xalign 0.26 yalign 0.725:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 12)
     if language_game == 1:
         text "Ординарность" xalign 0.01 yalign 0.77 size 32
     elif language_game == 2:
         text "Ordinary" xalign 0.01 yalign 0.77 size 32
     imagebutton xalign 0.2 yalign 0.775:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(informal_view == True), SetVariable("vn_gg", vn_gg+1), SetVariable("informal_view", False), SetVariable("dop_stats_lucky_gg", dop_stats_lucky_gg-8)
     imagebutton xalign 0.23 yalign 0.775:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(vn_gg >= 1 and informal_view == False), SetVariable("vn_gg", vn_gg-1), SetVariable("informal_view", True), SetVariable("dop_stats_lucky_gg", dop_stats_lucky_gg+8)
     imagebutton xalign 0.26 yalign 0.775:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 13)
     if language_game == 1:
         text "Коренастость" xalign 0.01 yalign 0.82 size 32
     elif language_game == 2:
         text "Stocky" xalign 0.01 yalign 0.82 size 32
     imagebutton xalign 0.2 yalign 0.825:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stocky == True), SetVariable("vn_gg", vn_gg+1), SetVariable("stocky", False), SetVariable("dop_stats_stamina_gg", dop_stats_stamina_gg-8)
     imagebutton xalign 0.23 yalign 0.825:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(vn_gg >= 1 and stocky == False), SetVariable("vn_gg", vn_gg-1), SetVariable("stocky", True), SetVariable("dop_stats_stamina_gg", dop_stats_stamina_gg+8)
     imagebutton xalign 0.26 yalign 0.825:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 14)
     if language_game == 1:
         text "{b}Описание:{/b}" xalign 0.85 yalign 0.02 size 32
     elif language_game == 2:
         text "{b}Description:{/b}" xalign 0.85 yalign 0.02 size 32
     if language_game == 1:
         if help == 1:
             text "Сила характерна персонажам, что решают свои проблемы\nнасильственными методами. Хочешь ударить - бей.\nСила влияет на шанс нокдауна, урон, а также на модификатор жуткости." xalign 0.99 yalign 0.07 size 20
         elif help == 2:
             text " Ловкость является неотъемлемым атрибутом для\n персонажей, что не привыкли получать постоянно получать\n от других оплеухи" xalign 0.99 yalign 0.07 size 20
         elif help == 10:
             text "Во многих странах ценится высокий рост, что\nвполне хорошо может сказаться на отношения между\nпротивоположным полом. Кроме того высокие люди имеют\nдлинные мышечные волокна, делающие их сильнее при\nсовершенно том же весе, что и их братьев меньших.\nДобавляет силу и привлекательность, но убавляет ловкость." xalign 0.99 yalign 0.07 size 20
         elif help == 11:
             text "Навряд ли шрамы можно назвать чем-то эстетичным,\nно это может добавить авторитет, да и выглядеть более\nугрожающе при присутствие на лице пару тройки\nшрамов - дело обычное." xalign 0.99 yalign 0.07 size 20
         elif help == 12:
             text "Миниатюрность для мужского пола многие могут\nназвать чем-то непривлекательным, но есть так же и люди,\nкоторым нравятся маленькие люди. Добавляет ловкости,\nно сила уменьшается." xalign 0.99 yalign 0.07 size 20
         elif help == 13:
             text "Многие люди с непримечательной внешностью - счастливчики.\nВ конце-то концов кому нужно это лишнее внимание\nот других людей за счет каких-то особенностей внешности?" xalign 0.99 yalign 0.07 size 20
         elif help == 14:
             text "Быть мелким и крепким - достаточно удобно, ведь\nты не только очень вынослив, но и в некотором роде\nсилен физически. Одна проблема: девушки все так же нечасто\nобращают на вас внимание..." xalign 0.99 yalign 0.07 size 20
         elif help == 15:
             text "Быть жадным, считать каждую копейку, но при этом\nвсегда иметь при себе деньги - прерогатива барыг,\nкоторой они пользуются постоянно. Появляется возможность\nпереторговывать вещички подороже на барахолках." xalign 0.99 yalign 0.07 size 20
         elif help == 16:
             text "Социализация - бред, навязанный обществом. По\nкрайней мере так считаете вы. Блокирует прокачку\nкрасноречия, но дает постоянную прибавку к другим\nатрибутам, так еще и в начале дает дополнительных 20\nпоинтов на распределение." xalign 0.99 yalign 0.07 size 20
         elif help == 17:
             text "Жрать все подряд и при этом не бояться изжоги/язвы\nи других неприятностей - вот что хотел бы каждый\nнебогатый студент в свои годы. В конце-то концов\nпереносимость фастфуда есть не у всех." xalign 0.99 yalign 0.07 size 20
         elif help == 18:
             text "Бывает, что скупость и жадность достигает пред...\nКхм... Будучи политиком, вы получаете постоянный бонус\nк авторитету, а также имеете дополнительные выходы\nиз некоторых сложных ситуаций." xalign 0.99 yalign 0.07 size 20
         elif help == 19:
             text "Правда ли выстрел в голову вас убьет?\nДает огромные бонусы к выносливости, но при\nэтом блокирует прокачку силы." xalign 0.99 yalign 0.07 size 20
         elif help == 20:
             text "Кому хочется вырубать людей направо и налево? Так вот,\nтяжелый кулак - ваш выбор, но будьте осторожны и случайно\nне сломайте кому-то челюсть!" xalign 0.99 yalign 0.07 size 20
     if language_game == 2:
         if help == 10:
             text "In many countries, high growth is valued,\nwhich may well affect relations between the opposite\nsex. In addition, tall people have longer muscle\nfibers, making them stronger with exactly\nthe same weight as their smaller brothers.\nAdds strength and attractiveness, but\nreduces dexterity." xalign 0.99 yalign 0.07 size 20
         elif help == 11:
             text "It is unlikely that the scars can be called\nsomething aesthetic, but this can add authority,\nand look more threatening when there are a couple\nof three scars on the face - this is common." xalign 0.99 yalign 0.07 size 20
         elif help == 12:
             text "A miniature for a male may not be as attractive\nas people who like small people. Adds dexterity,\nbut a drop power." xalign 0.99 yalign 0.07 size 20
         elif help == 13:
             text "Many people with unusual looks are lucky.\nAfter all, who needs this extra attention?" xalign 0.99 yalign 0.07 size 20
         elif help == 14:
             text "To be small and strong is quite convenient,\nbecause you are not only very hardy, but also physically\nstrong in some way. One problem: girls are\nstill infrequent pay attention to you ..." xalign 0.99 yalign 0.07 size 20
         elif help == 15:
             text "Being greedy, counting every penny, but always\nhave money with you is the prerogative of the huckster,\nwhich they use all the time. There is an\nopportunity to re-trade things more expensive\nat flea markets." xalign 0.99 yalign 0.07 size 20
         elif help == 16:
             text "Socialization is nonsense imposed by society.\nAt least you think so. It blocks the pumping of eloquence,\nbut gives a constant increase to other\nattributes, and also at the beginning gives an additional\n20 points to publish." xalign 0.99 yalign 0.07 size 20
         elif help == 17:
             text "Eat everything and not be afraid of\nheartburn/ulcers and other troubles - that’s what every\npoor student would like in his age. In the end,\nnot everyone has fast food tolerance." xalign 0.99 yalign 0.07 size 20
         elif help == 18:
             text "It happens that stinginess and greed reaches\nup to... Khm... As a politician, you get a\nconstant bonus to authority, and also have\nadditional ways out of some difficult situations." xalign 0.99 yalign 0.07 size 20
         elif help == 19:
             text "Is it true that a headshot will kill you? It\ngives huge endurance bonuses, but when this\nblock the pumping of strength." xalign 0.99 yalign 0.07 size 20
         elif help == 20:
             text "Who wants to cut people right and left?\nSo, a heavy fist is your choice, but be careful\nand accidentally do not break someone’s jaw!" xalign 0.99 yalign 0.07 size 20
     #Перки
     if language_game == 1:
         text "{b}Доп. особенности:{/b}" xalign 0.9 yalign 0.57 size 32
         text "Барыга" xalign 0.99 yalign 0.62 size 32
     if language_game == 2:
         text "{b}Dop.features:{/b}" xalign 0.9 yalign 0.57 size 32
         text "Huckster" xalign 0.99 yalign 0.62 size 32
     imagebutton xalign 0.8 yalign 0.625:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(huckster == True), SetVariable("points_perk", points_perk+1), SetVariable("huckster", False)
     imagebutton xalign 0.77 yalign 0.625:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and huckster == False), SetVariable("points_perk", points_perk-1), SetVariable("huckster", True)
     imagebutton xalign 0.74 yalign 0.625:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 15)
     if language_game == 1:
         text "Волк-одиночка" xalign 0.99 yalign 0.67 size 32
     elif language_game == 2:
         text "Lone wolf" xalign 0.99 yalign 0.67 size 32
     imagebutton xalign 0.8 yalign 0.675:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(loner == True), SetVariable("points_perk", points_perk+1), SetVariable("loner", False), SetVariable("points_stats", 20), SetVariable("stats_lucky_gg", 20), SetVariable("stats_erudition_gg", 20), SetVariable("stats_authority_gg", 20), SetVariable("stats_cunning_gg", 20), SetVariable("stats_forces_gg", 20), SetVariable("stats_agility_gg", 20), SetVariable("stats_stamina_gg", 20), SetVariable("stats_science_gg ", 20)
     imagebutton xalign 0.77 yalign 0.675:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and loner == False), SetVariable("points_perk", points_perk-1), SetVariable("loner", True), SetVariable("points_stats", stats_erudition_gg - 20 + points_stats + 20), SetVariable("stats_erudition_gg", 10)
     imagebutton xalign 0.74 yalign 0.675:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 16)
     if language_game == 1:
         text "Крепкий желудок" xalign 0.99 yalign 0.72 size 32
     elif language_game == 2:
         text "Strong stomach" xalign 0.99 yalign 0.72 size 32
     imagebutton xalign 0.8 yalign 0.725:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(stomach == True), SetVariable("points_perk", points_perk+1), SetVariable("stomach", False)
     imagebutton xalign 0.77 yalign 0.725:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and stomach == False), SetVariable("points_perk", points_perk-1), SetVariable("stomach", True)
     imagebutton xalign 0.74 yalign 0.725:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 17)
     if language_game == 1:
         text "Политик" xalign 0.99 yalign 0.77 size 32
     elif language_game == 2:
         text "Politician" xalign 0.99 yalign 0.77 size 32
     imagebutton xalign 0.8 yalign 0.775:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(politic == True), SetVariable("points_perk", points_perk+1), SetVariable("politic", False), SetVariable("dop_stats_authority_gg", dop_stats_authority_gg - 20)
     imagebutton xalign 0.77 yalign 0.775:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and politic == False), SetVariable("points_perk", points_perk-1), SetVariable("politic", True), SetVariable("dop_stats_authority_gg", dop_stats_authority_gg + 20)
     imagebutton xalign 0.74 yalign 0.775:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 18)
     if language_game == 1:
         text "Зомби" xalign 0.99 yalign 0.82 size 32
     elif language_game == 2:
         text "Zombie" xalign 0.99 yalign 0.82 size 32
     imagebutton xalign 0.8 yalign 0.825:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(zombie == True), SetVariable("points_perk", points_perk+1), SetVariable("zombie", False), SetVariable("stats_forces_gg", 20), SetVariable("dop_stats_stamina_gg", dop_stats_stamina_gg-60)
     imagebutton xalign 0.77 yalign 0.825:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and zombie == False), SetVariable("points_perk", points_perk-1), SetVariable("zombie", True), SetVariable("points_stats", stats_forces_gg - 20 + points_stats), SetVariable("stats_forces_gg", 10), SetVariable("dop_stats_stamina_gg", dop_stats_stamina_gg+60)
     imagebutton xalign 0.74 yalign 0.825:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 19)
     if language_game == 1:
         text "Тяжелая рука" xalign 0.99 yalign 0.87 size 32
     elif language_game == 2:
         text "Heavy arm" xalign 0.99 yalign 0.87 size 32
     imagebutton xalign 0.8 yalign 0.875:
         idle ("icons/icons_minus.png")
         hover ("icons/icons_minus_hover.png")
         action SensitiveIf(heavy_arm == True), SetVariable("points_perk", points_perk+1), SetVariable("heavy_arm", False), SetVariable("dop_damage_gg", dop_damage_gg-15)
     imagebutton xalign 0.77 yalign 0.875:
         idle ("icons/icons_plus.png")
         hover ("icons/icons_plus_hover.png")
         action SensitiveIf(points_perk >= 1 and heavy_arm == False), SetVariable("points_perk", points_perk-1), SetVariable("heavy_arm", True), SetVariable("dop_damage_gg", dop_damage_gg+15)
     imagebutton xalign 0.74 yalign 0.875:
         idle ("icons/icons_menu_question.png")
         hover ("icons/icons_menu_question_hover.png")
         action SetVariable("help", 20)
     if language_game == 1:
         text "Нераспределенных очков перков: {b}[points_perk]{/b}" xalign 0.99 yalign 0.99 size 30
     elif language_game == 2:
         text "Unallocated perk points: {b}[points_perk]{/b}" xalign 0.99 yalign 0.99 size 30
     imagebutton xalign 0.99 yalign 0.5:
         idle ("icons/icons_next.png")
         hover ("icons/icons_next_hover.png")
         action SensitiveIf(points_perk <= 0 and vn_gg <= 0 and points_stats <= 0), Jump('rr_npc')
     if language_game == 1:
         if points_perk >= 1:
             text "Распределите очки перков" xalign 0.9 yalign 0.5 size 24
         if vn_gg >= 1:
             text "Определитесь с особенностями внешности" xalign 0.9 yalign 0.47 size 24
         if points_stats >= 1:
             text "Распределите очки атрибутов" xalign 0.9 yalign 0.53 size 24
     if language_game == 2:
         if points_perk >= 1:
             text "Distribute perk points" xalign 0.9 yalign 0.5 size 24
         if vn_gg >= 1:
             text "Decide on the features of appearance" xalign 0.9 yalign 0.47 size 24
         if points_stats >= 1:
             text "Distribute attribute points" xalign 0.9 yalign 0.53 size 24
