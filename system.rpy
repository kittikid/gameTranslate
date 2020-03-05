init python:
     fist_punch = True
     kick_punch = False
label start3:
if help_fight == 1:
     jump guide1
stop music fadeout 1
$ renpy.pause(1.0, hard=True)
queue music [ "music/3.mp3", "music/4.mp3" ]
scene bf
if language_game == 1:
     if points_hp_gg <= 20:
         "У вас нет сил, чтобы драться. Вы уверены, что хотите этого?"
         menu:
             "Да":
                 $ dadadada = 1312
             "Нет":
                 jump check_location
else:
     if points_hp_gg <= 20:
         "You have no strength to fight. Are you sure you want this?"
         menu:
             "Yes":
                 $ dadadada = 1312
             "No":
                 jump check_location
if npc == 1:
     $ npc_stats = eval(npc_id)['npc_stats']
     $ stats_forces = npc_stats['forces']
     $ stats_agility = npc_stats['agility']
     $ stats_stamina = npc_stats['stamina']
     $ stats_lucky = npc_stats['lucky']
if xuligan_class == 1:
     if language_game == 1:
         "Разразилась битва! Удары градом сыпались по Вам и от Вас! Гневные крики хулиганов огласили место сражения!"
     elif language_game == 2:
         "The battle broke out! Habits rained down on you and from you! The angry screams of the hooligans announced the scene of the battle!"
     $ stats_forces = 35
     $ stats_agility = 20
     $ stats_stamina = 25
     $ stats_lucky = 10
elif xuligan_class == 2:
     $ stats_forces = 35
     $ stats_agility = 20
     $ stats_stamina = 25
     $ stats_lucky = 10
$ points_hp = 100
$ DopHP = stats_stamina / 2
$ points_hp += DopHP
$ mod_speed_attack = 100
$ speed_attack = mod_speed_attack / 4 / float(stats_agility)
$ standart_mod_attack = 20
$ damage = stats_forces / 2 + standart_mod_attack
$ block_damage = 100 / (stats_stamina / 2)
$ miss_chance = 100 / (stats_agility / 2)
$ accuracy = 100 / (stats_agility / 4)
$ punch = float(2.5) / speed_attack
$ knockdown = stats_forces / 6
$ critical_damage = 100 / (stats_lucky/ 2)
call screen punch
screen punch:
     if fist_punch == True:
         imagebutton xalign 0.01 yalign 0.02:
             idle "icons/icons_fist_fight_hover.png"
             action SetVariable('fist_punch', False), SetVariable('kick_punch', True)
     elif fist_punch == False:
         imagebutton xalign 0.01 yalign 0.02:
             idle "icons/icons_fist_fight.png"
             action SetVariable('fist_punch', True), SetVariable('kick_punch', False)
     if kick_punch == True:
         imagebutton xalign 0.1 yalign 0.02:
             idle "icons/icons_leg_hover.png"
             action SetVariable('fist_punch', True), SetVariable('kick_punch', False)
     elif kick_punch == False:
         imagebutton xalign 0.1 yalign 0.02:
             idle "icons/icons_leg.png"
             action SetVariable('fist_punch', False), SetVariable('kick_punch', True)
     if language_game == 1:
         text "{color=#000000}Ударить голову:{/color}" xalign 0.45 yalign 0.4
         text "{color=#000000}Ударить тело:{/color}" xalign 0.45 yalign 0.5
         text "{color=#000000}Ударить ноги:{/color}" xalign 0.45 yalign 0.6
         text "{color=#000000}Здоровье противника: [points_hp]/200{/color}" xalign 0.99 yalign 0.92
         text "{color=#000000}Ваше здоровье: [points_hp_gg]/200{/color}" xalign 0.99 yalign 0.97
     else:
         text "{color=#000000}Hit the head:{/color}" xalign 0.45 yalign 0.4
         text "{color=#000000}Hit the body:{/color}" xalign 0.45 yalign 0.5
         text "{color=#000000}Kick Feet:{/color}" xalign 0.45 yalign 0.6
         text "{color=#000000}Enemy Health: [points_hp]/200{/color}" xalign 0.99 yalign 0.92
         text "{color=#000000}Your Health: [points_hp_gg]/200{/color}" xalign 0.99 yalign 0.97
     if fist_punch == True:
         imagebutton xalign 0.55 yalign 0.4:
             idle im.Rotozoom("icons/icons_fist_fight.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_fist_fight_hover.png", 0, 0.6)
             action Jump('fist_punch')
         imagebutton xalign 0.55 yalign 0.5:
             idle im.Rotozoom("icons/icons_fist_fight.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_fist_fight_hover.png", 0, 0.6)
             action Jump('fist_punch')
         imagebutton xalign 0.55 yalign 0.6:
             idle im.Rotozoom("icons/icons_fist_fight.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_fist_fight_hover.png", 0, 0.6)
             action Jump('fist_punch')
     elif kick_punch == True:
         imagebutton xalign 0.55 yalign 0.4:
             idle im.Rotozoom("icons/icons_kicking.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_kicking_hover.png", 0, 0.6)
             action Jump('fist_punch')
         imagebutton xalign 0.55 yalign 0.5:
             idle im.Rotozoom("icons/icons_kicking.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_kicking_hover.png", 0, 0.6)
             action Jump('fist_punch')
         imagebutton xalign 0.55 yalign 0.6:
             idle im.Rotozoom("icons/icons_kicking.png", 0, 0.6)
             hover im.Rotozoom("icons/icons_kicking_hover.png", 0, 0.6)
             action Jump('fist_punch')
label fist_punch:
     $ minute += 2
     if fist_punch == True:
         $ knockdown_plus = 0
     if kick_punch == True:
         $ knockdown_plus = 10
     $ rand_kick = renpy.random.randint(1, 2)
     $ knockdown_gg1 = renpy.random.randint(1, 100)
     $ knockdown_npc1 = renpy.random.randint(1, 100)
     $ miss_chance_gg1 = renpy.random.randint(1, int(miss_chance_gg))
     $ miss_chance_npc = renpy.random.randint(1, int(miss_chance))
     $ critical_damage_chance = renpy.random.randint(1, int(critical_damage_gg))
     $ critical_damage_chance_npc = renpy.random.randint(1, int(critical_damage))
     if knockdown_gg1 <= knockdown_info+knockdown_plus and miss_chance_npc >= 3:
         "Вы нокаутировали своего противника!"
         $ combat_win += 1
         $ combat_experience += 1
         if xuligan_class == 1:
             if language_game == 1:
                 "Хулиганы корчились у ваших ног. Наступив на грудь их главарю, вы подняли голову и протяжно завыли. Это была славная битва."
                 "“А теперь сделайте так, чтобы я вас долго искал!” - сказали вы, грозно глянув на проигравших, отчего забияки проворно поползли к выходу, оставив вас наедине с избитым школьником."
                 $ stats_authority_gg_info += 1
                 menu:
                     "Пнуть слабака":
                         $ stats_authority_gg_info += 1
                         "Проходя мимо избитого, Вы услышали слабое cпасибо, но тут же пнули его в живот. Жертва, не ожидавшая такой подлости, потеряла дыхание.\nВсех, кто младше и слабей - не задумываясь бей! - произнесли вы, еще раз пнув грушу для битья, после выйдя с класса."
                     "Помочь подняться.":
                         "Вы подняли с пола избитую жертву и помогли дойти до умывальника, выслушивая горячие слова благодарности. Как только жертва отмыла кровавые сопли с лица, вы совместными усилиями привели её костюм в пристойный вид, после попрощавшись друг с другом."
                     "Уйти":
                         "Вы молча посмотрели на избитую жертву и вышли из класса. Тут каждый сам за себя. Он должен это понять."
                     "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
                 $ xuligan_class = 0
                 $ ivents_hooligans = 1
             elif language_game == 2:
                 "You were able to knock down your opponent, thereby winning the fight went to you"
                 "The hooligans writhed at your feet. Stepping on the chest of their leader, you raised your head and howled lingeringly. It was a glorious battle."
                 "“Now, make sure I look for you for a long time!” - You said, looking fiercely at the bunch of losers, after which the bullies crawled cunningly to the exit, leaving you alone with the battered schoolboy."
                 $ stats_authority_gg_info += 1
                 menu:
                     "Kick the wimp":
                         $ stats_authority_gg_info += 1
                         "Passing the beaten one, you heard a weak thank you, but then kicked him in the stomach. The victim, who did not expect such meanness, lost her breath.\nEveryone who is younger and weaker - do not hesitate to beat! - You said, once again kicking the punching bag, after leaving the classroom."
                     "Help rise":
                         "You picked up the battered victim from the floor and helped you get to the washstand, listening to the warm words of gratitude. As soon as the victim washed the bloody snot from the face, together you brought her suit in decent shape, after saying goodbye to each other."
                     "To leave":
                         "You silently looked at the battered victim and left the classroom. Here, everyone is for himself. He must understand this."
                     "{color=#32CD32}Your authority level has increased!{/color}"
                 $ xuligan_class = 0
                 $ ivents_hooligans = 1
             jump check_location
         elif xuligan_class == 2:
             scene toilet
             $ stats_authority_gg_info += 1
             $ xuligan_class = 0
             $ ivent_extortion = 1
             if language_game == 1:
                 "Спустя долгие минуты вы все же выиграли в бойне, вырубив одного хулигана. Как ни странно, другие не решились продолжать схватку и ушли, оставив вас наедине с вашим кипящим адреналином."
                 "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
             elif language_game == 2:
                 "After the long minutes of the battle, you still won the slaughter, knocking out one bully. Strangely enough, the others did not dare to continue the fight and left, leaving you alone with your seething adrenaline."
                 "{color=#32CD32}Your authority level has increased!{/color}"
             jump check_location
         $ contact_npc -= 100
         $ love_npc -= 20
         $ fear_npc += 20
         $ eval(npc_id)["love_npc"] = love_npc
         $ eval(npc_id)["contact_npc"] = contact_npc
         $ eval(npc_id)["fear_npc"] = fear_npc
         stop music fadeout 1
         $ renpy.pause(1.0, hard=True)
         queue music [ "music/5.mp3", "music/2.mp3" ]
         jump check_location
     else:
         if fist_punch == True:
                 if miss_chance_npc <= 2:
                     "Противник увернулся"
                 else:
                     if critical_damage_chance == 1:
                         $ points_hp -= int((damage_gg_info / 2) - block_damage * damage_gg_info / 100) * 2
                         "Вы ударили критическим ударом!"
                     else:
                         $ points_hp -= int((damage_gg_info / 2) - block_damage * damage_gg_info / 100)
                         "Вы ударили с руки"
                 if miss_chance_gg1 == 1:
                     "Вы увернулись от удара"
         if kick_punch == True:
             if kick_punch == True:
                 if miss_chance_npc <= 4:
                     "Противник увернулся"
                 else:
                     if critical_damage_chance_npc == 1:
                         $ points_hp -= int((damage_gg_info / 2)+(stats_agility_gg * damage_gg_info / 100)-(block_damage * damage_gg_info / 100)) * 2
                         "Вы ударили критическим ударом!"
                     else:
                         $ points_hp -= int(damage_gg_info / 2)+(stats_agility_gg * damage_gg_info / 100)-(block_damage * damage_gg_info / 100)
                         "Вы ударили с ноги"
         if miss_chance_gg1 <= 2:
             "Вы увернулись от удара противника"
         else:
             if knockdown_npc1 <= knockdown:
                 "Вас нокаутировали. Вы проиграли."
                 $ combat_experience += 1
                 if xuligan_class == 1:
                     if language_game == 1:
                         $ stats_authority_gg_info -= 1
                         "Едва упав на пол, вы почувствовали град ударов ногами. Вас били долго и сладострастно, после заставив просить прощения и унижаться."
                         x2 "Понял, сука, кто тут главный?!"
                         x3 "Мы эту школу держим!"
                         "Наконец хулиганы оплевали вас и ушли."
                         "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
                     elif language_game == 2:
                         $ stats_authority_gg_info -= 1
                         "As soon as you fell to the floor, you felt a hail of kicks. You were beaten for a long time and voluptuous, after being forced to apologize and humiliate yourself"
                         x2 "Got it, bitch, who's in charge here?!"
                         x3 "We keep this school!"
                         "Finally, the bullies spat on you and left."
                         "{color=#FF0000}Your authority level has declined!{/color}"
                     $ ivents_hooligans = 1
                     jump check_location
                 elif xuligan_class == 2:
                     scene toilet
                     $ stats_authority_gg_info -= 1
                     $ money = 0
                     $ ivent_extortion = 1
                     if language_game == 1:
                         "Спустя долгие минуты битвы вы все же проиграли, упав на холодный пол туалета, а пинки кучи хулиганов заставляли вас лежать и не рыпаться."
                         x2 "Надеюсь, что ты понял этот урок!"
                         "После его слов из вашего кармана забрали кошелек со всеми сбережениями. Пересчитав все ваши деньги, считавший пожал плечами и покинул туалет, пока другие вас продолжали избивать."
                         "Все же спустя некоторое время вас все же отпустили, и вы вышли избитым из злополучного туалета."
                         "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
                     elif language_game == 2:
                         "After long minutes of the battle, you still lost, falling to the cold floor of the toilet, and the kicks of a pile of hooligans forced you to lie down and not rock the boat."
                         x2 "Hope you understood this lesson!"
                         "After his words, a wallet with all the savings was taken from your pocket. Having counted all your money, he considered shrugging his shoulders and left the toilet, while others continued to beat you."
                         "Nevertheless, after some time, you were nevertheless released, and you came out beaten from the ill-fated toilet."
                         "{color=#FF0000}Your authority level has declined!{/color}"
                     jump check_location
                 $ xuligan_class = 0
                 $ contact_npc -= 100
                 $ love_npc -= 20
                 $ fear_npc -= 20
                 $ eval(npc_id)["love_npc"] = love_npc
                 $ eval(npc_id)["contact_npc"] = contact_npc
                 $ eval(npc_id)["fear_npc"] = fear_npc
                 stop music fadeout 1
                 $ renpy.pause(1.0, hard=True)
                 queue music [ "music/5.mp3", "music/2.mp3" ]
                 jump check_location
             else:
                 if rand_kick == 1:
                     $ points_hp_gg -= int(damage / 2)+(stats_agility * damage / 100)-(block_damage_gg * damage / 100)
                 else:
                     $ points_hp_gg -= int(damage / 2)-(block_damage_gg * damage / 100)
                 "Противник ударил вас"
     if points_hp_gg <= 0:
         "Вы проиграли."
         $ combat_experience += 1
         if xuligan_class == 1:
             if language_game == 1:
                 $ stats_authority_gg_info -= 1
                 "Едва упав на пол, вы почувствовали град ударов ногами. Вас били долго и сладострастно, после заставив просить прощения и унижаться."
                 x2 "Понял, сука, кто тут главный?!"
                 x3 "Мы эту школу держим!"
                 "Наконец хулиганы оплевали вас и ушли."
                 "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
             elif language_game == 2:
                 $ stats_authority_gg_info -= 1
                 "As soon as you fell to the floor, you felt a hail of kicks. You were beaten for a long time and voluptuous, after being forced to apologize and humiliate yourself"
                 x2 "Got it, bitch, who's in charge here?!"
                 x3 "We keep this school!"
                 "Finally, the bullies spat on you and left."
                 "{color=#FF0000}Your authority level has declined!{/color}"
             $ xuligan_class = 0
             $ ivents_hooligans = 1
             jump check_location
         elif xuligan_class == 2:
             scene toilet
             $ stats_authority_gg_info -= 1
             $ money = 0
             $ ivent_extortion = 1
             if language_game == 1:
                 "Спустя долгие минуты битвы вы все же проиграли, упав на холодный пол туалета, а пинки кучи хулиганов заставляли вас лежать и не рыпаться."
                 x2 "Надеюсь, что ты понял этот урок!"
                 "После его слов из вашего кармана забрали кошелек со всеми сбережениями. Пересчитав все ваши деньги, считавший пожал плечами и покинул туалет, пока другие вас продолжали избивать."
                 "Все же спустя некоторое время вас все же отпустили, и вы вышли избитым из злополучного туалета."
                 "{color=#FF0000}Ваш уровень авторитета снизился!{/color}"
             elif language_game == 2:
                 "After long minutes of the battle, you still lost, falling to the cold floor of the toilet, and the kicks of a pile of hooligans forced you to lie down and not rock the boat."
                 x2 "Hope you understood this lesson!"
                 "After his words, a wallet with all the savings was taken from your pocket. Having counted all your money, he considered shrugging his shoulders and left the toilet, while others continued to beat you."
                 "Nevertheless, after some time, you were nevertheless released, and you came out beaten from the ill-fated toilet."
                 "{color=#FF0000}Your authority level has declined!{/color}"
                 $ xuligan_class = 0
             jump check_location
         $ contact_npc -= 100
         $ love_npc -= 20
         $ fear_npc -= 20
         $ eval(npc_id)["love_npc"] = love_npc
         $ eval(npc_id)["contact_npc"] = contact_npc
         $ eval(npc_id)["fear_npc"] = fear_npc
         $ points_hp_gg = 1
         stop music fadeout 1
         $ renpy.pause(1.0, hard=True)
         queue music [ "music/5.mp3", "music/2.mp3" ]
         jump check_location
     if points_hp <= 0:
         "Вы выиграли."
         $ combat_win += 1
         $ combat_experience += 1
         if xuligan_class == 1:
             if language_game == 1:
                 "Вы смогли кинуть в нокдаун своего противника, тем самым победа в драке досталась вам"
                 "Хулиганы корчились у ваших ног. Наступив на грудь их главарю, вы подняли голову и протяжно завыли. Это была славная битва."
                 "“А теперь сделайте так, чтобы я вас долго искал!” - сказали вы, грозно глянув на проигравших, отчего забияки проворно поползли к выходу, оставив вас наедине с избитым школьником."
                 $ stats_authority_gg_info += 1
                 menu:
                     "Пнуть слабака":
                         $ stats_authority_gg_info += 1
                         "Проходя мимо избитого, Вы услышали слабое cпасибо, но тут же пнули его в живот. Жертва, не ожидавшая такой подлости, потеряла дыхание.\nВсех, кто младше и слабей - не задумываясь бей! - произнесли вы, еще раз пнув грушу для битья, после выйдя с класса."
                     "Помочь подняться.":
                         "Вы подняли с пола избитую жертву и помогли дойти до умывальника, выслушивая горячие слова благодарности. Как только жертва отмыла кровавые сопли с лица, вы совместными усилиями привели её костюм в пристойный вид, после попрощавшись друг с другом."
                     "Уйти":
                         "Вы молча посмотрели на избитую жертву и вышли из класса. Тут каждый сам за себя. Он должен это понять."
                     "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
                 $ xuligan_class = 0
                 $ ivents_hooligans = 1
             elif language_game == 2:
                 "You were able to knock down your opponent, thereby winning the fight went to you"
                 "The hooligans writhed at your feet. Stepping on the chest of their leader, you raised your head and howled lingeringly. It was a glorious battle."
                 "“Now, make sure I look for you for a long time!” - You said, looking fiercely at the bunch of losers, after which the bullies crawled cunningly to the exit, leaving you alone with the battered schoolboy."
                 $ stats_authority_gg_info += 1
                 menu:
                     "Kick the wimp":
                         $ stats_authority_gg_info += 1
                         "Passing the beaten one, you heard a weak thank you, but then kicked him in the stomach. The victim, who did not expect such meanness, lost her breath.\nEveryone who is younger and weaker - do not hesitate to beat! - You said, once again kicking the punching bag, after leaving the classroom."
                     "Help rise":
                         "You picked up the battered victim from the floor and helped you get to the washstand, listening to the warm words of gratitude. As soon as the victim washed the bloody snot from the face, together you brought her suit in decent shape, after saying goodbye to each other."
                     "To leave":
                         "You silently looked at the battered victim and left the classroom. Here, everyone is for himself. He must understand this."
                     "{color=#32CD32}Your authority level has increased!{/color}"
                 $ xuligan_class = 0
                 $ ivents_hooligans = 1
             jump check_location
         elif xuligan_class == 2:
             scene toilet
             $ stats_authority_gg_info += 1
             $ xuligan_class = 0
             $ ivent_extortion = 1
             if language_game == 1:
                 "Спустя долгие минуты вы все же выиграли в бойне, вырубив одного хулигана. Как ни странно, другие не решились продолжать схватку и ушли, оставив вас наедине с вашим кипящим адреналином."
                 "{color=#32CD32}Ваш уровень авторитета повысился!{/color}"
             elif language_game == 2:
                 "After the long minutes of the battle, you still won the slaughter, knocking out one bully. Strangely enough, the others did not dare to continue the fight and left, leaving you alone with your seething adrenaline."
                 "{color=#32CD32}Your authority level has increased!{/color}"
             jump check_location
         $ xuligan_class = 0
         $ contact_npc -= 100
         $ love_npc -= 20
         $ fear_npc += 20
         $ eval(npc_id)["love_npc"] = love_npc
         $ eval(npc_id)["contact_npc"] = contact_npc
         $ eval(npc_id)["fear_npc"] = fear_npc
         $ points_hp = 1
         stop music fadeout 1
         $ renpy.pause(1.0, hard=True)
         queue music [ "music/5.mp3", "music/2.mp3" ]
         jump check_location
     call screen punch
init python:
     import string

     # переменные (вручную не трогать)
     qte_word = ""
     next_k = ""
     qteTime = .0
     qteMaxTime = 5.0
     abc = list(string.ascii_lowercase)

    # инициализация игры при запуске экрана
    # параметры передаются при вызове экрана игры
    # если слово пустое, то генерируется рандомное длиной length
    # time - время, отведенное на игру в секундах
     def qte_init(word="", time=5.0, length=5):
         global qte_word, next_k, qteMaxTime, qteTime
         qteMaxTime = time
         qteTime = time
         qte_word = word.lower()
         if word:
             next_k = qte_word[0]
         else:
             for i in range(0, length):
                 qte_word = qte_word + renpy.random.choice(abc)
                 next_k = qte_word[0]
         renpy.restart_interaction()
    # нажатие очередной нужной кнопки, переходим к следующей
     def next_key():
         global qte_word, next_k
         qte_word = qte_word[1:]
         next_k = ""
         if qte_word:
             next_k = qte_word[0]
         renpy.restart_interaction()
     NextKey = renpy.curry(next_key)
     qteInit = renpy.curry(qte_init)

# сам экран игры
screen scr_qte(word="", time=5.0, length=5):
     # инициализация
     on 'show' action qteInit(word, time, length)
     modal True
     if qte_word:
         # уменьшаем время, отведенное на игру, и проверяем, не вышло ли оно - проигрыш
         timer 0.01 repeat True action [SetVariable("qteTime", qteTime - .01), If(qteTime <= .0, true=Jump('lossqte'))]
         # отображаем, какую кнопку нужно нажать
         text next_k.upper() align(.5, .5) size 96
         # если что-то нужно нажать, то опрашивает клавиатуру
         if len(next_k) == 1:
             key next_k action NextKey()
     else:
         # все кнопки нажаты - победа
         timer .1 action Jump('winqte'),
     # шкала времени
     bar value StaticValue(qteTime, qteMaxTime) align(.5, .1) xmaximum 600
label winqte:
     if language_game == 1:
         "Вы успешно сбежали!"
         jump check_location
     elif language_game == 2:
         "You have successfully escaped!"
     if gg_npc == 1:
         $ contact_npc1 -= 30
         $ love_npc1 -= 100
         $ fear_npc1 -= 20
     elif gg_npc == 2:
         $ contact_npc2 -= 30
         $ love_npc2 -= 100
         $ fear_npc2 -= 20
     elif gg_npc == 3:
         $ contact_npc3 -= 30
         $ love_npc3 -= 100
         $ fear_npc3 -= 20
     elif gg_npc == 4:
         $ contact_npc4 -= 30
         $ love_npc4 -= 100
         $ fear_npc4 -= 20
     elif gg_npc == 5:
         $ contact_npc5 -= 30
         $ love_npc5 -= 100
         $ fear_npc5 -= 20
     elif gg_npc == 6:
         $ contact_npc6 -= 30
         $ love_npc6 -= 100
         $ fear_npc6 -= 20
     elif gg_npc == 7:
         $ contact_npc7 -= 30
         $ love_npc7 -= 100
         $ fear_npc7 -= 20
     elif gg_npc == 8:
         $ contact_npc8 -= 30
         $ love_npc8 -= 100
         $ fear_npc8 -= 20
     elif gg_npc == 9:
         $ contact_npc9 -= 30
         $ love_npc9 -= 100
         $ fear_npc9 -= 20
     elif gg_npc == 10:
         $ contact_npc10 -= 30
         $ love_npc10 -= 100
         $ fear_npc10 -= 20
     jump check_location
label lossqte:
     if language_game == 1:
         "Вы не смогли сбежать от своего противника."
         jump check_location
     elif language_game == 2:
         "You were unable to escape from your opponent."
     if gg_npc == 1:
         $ fear_npc1 -= 20
     elif gg_npc == 2:
         $ fear_npc2 -= 20
     elif gg_npc == 3:
         $ fear_npc3 -= 20
     elif gg_npc == 4:
         $ fear_npc4 -= 20
     elif gg_npc == 5:
         $ fear_npc5 -= 20
     elif gg_npc == 6:
         $ fear_npc6 -= 20
     elif gg_npc == 7:
         $ fear_npc7 -= 20
     elif gg_npc == 8:
         $ fear_npc8 -= 20
     elif gg_npc == 9:
         $ fear_npc9 -= 20
     elif gg_npc == 10:
         $ fear_npc10 -= 20
     jump punch
label Patreon_Code123123:
     #пiшев нахуй отсюда, мамкин программист!
     #кто прочитал, тот гей
     scene main_menu123
     $ Patreon_Code_M = str(Patreon_Code_M)
     if Patreon_Code_M == 'eggto':
         $ Patreon_Code = 1
         "Вы ввели Comrade патреон-код!"
         call screen main_menu
     elif Patreon_Code_M == 'qsgte':
         $ Patreon_Code = 1
         "Вы ввели Comrade патреон-код!"
         call screen main_menu
     elif Patreon_Code_M == 'yeten':
         $ Patreon_Code = 2
         "Вы ввели Friend патреон-код!"
         call screen main_menu
     elif Patreon_Code_M == 'baryt':
         $ Patreon_Code = 2
         "Вы ввели Friend патреон-код!"
         call screen main_menu
     elif Patreon_Code_M == 'qrcode':
         $ Patreon_Code = 3
         "Вы ввели hentai patch ключ."
         call screen main_menu
     else:
         "Вы ввели неправильный патреон код!"
         call screen main_menu
label check_location:
     $ page = 0
     if dialoge == 0 and dialoge >= 4:
         $ dialoge = 1
     if gg == 1:
         jump school
     elif gg == 2:
         jump corridor
     elif gg == 3:
         jump class
     elif gg == 4:
         jump roof
     elif gg == 5:
         jump home
     elif gg == 6:
         jump beach
     elif gg == 7:
         jump park1
     elif gg == 8:
         jump stroll
     elif gg == 9:
         jump magazine
     elif gg == 10:
         jump magazine1
     elif gg == 11:
         jump computer
     elif gg == 12:
         jump stair_school
     elif gg == 13:
         jump corridor1
     elif gg == 19:
         jump product_magazine
     elif gg == 20:
         jump shopping_center
     elif gg == 21:
         jump student_soviet
     elif gg == 22:
         jump canteen
     elif gg == 23:
         jump pool
     elif gg == 24:
         jump club_occult
     elif gg == 25:
         jump storeroom
     else:
         jump school
label phone:
     $ v_pos = 0
     $ y_pos = 0.1
     $ menu_loc = 0
     scene bf with dissolve
     if language_game == 1:
         "Достав древний телефон из кармана и покрутив его в руках, вы сразу поняли, что это обычная звонилка, с которой ни поиграешь, ни посидишь в интернете, как в этих новомодных смартфонах, но зато его корпусом можно пробить череп неугодному."
     elif language_game == 2:
         "Pulling the ancient phone out of your pocket and twisting it in your hands, you immediately realized that it was an ordinary dialer, with which you could neither play nor sit on the Internet, as in these new-fangled smartphones, but you could pierce a skull that was objectionable with its body."
     call screen phone
screen call_phone_:
     modal True
     add "gui/telephone/telephone.png" xpos -35 ypos 10
     vpgrid:
         cols 1
         rows 20
         spacing -459
         xpos 57 ypos 471 xysize (300, 415)
         child_size (300, 500)
         draggable True
         mousewheel True
         arrowkeys True
         scrollbars 'vertical'
         if suzuki_number == 1:
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 if telephone_number == -10:
                     add "gui/telephone/contact_hover.png"
                 else:
                     add "gui/telephone/contact_idle.png"
                 hover_background "gui/telephone/contact_hover.png"
                 textbutton '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Сузуки Мацуи{/font}{/size}{/color}' ypos 0 xpos 10
                 action Hide("sms_phone1"), SetVariable('telephone_number', -10), SetVariable('messange_npc', 0)
         for number_npc in range(1, number_npc_max):
             $ npc_id = 'npc'+str(number_npc)
             $ number_phone = eval(npc_id)["number_phone"]
             if number_phone == 1:
                 $ contact_npc = eval(npc_id)["contact_npc"]
                 $ npc_name = eval(npc_id)["npc_name"]
                 $ npc_fam = eval(npc_id)["npc_fam"]
                 $ name_npc = npc_name + ' ' + npc_fam
                 $ location_npc = eval(npc_id)["location_npc"]
                 button:
                     xpadding 0
                     ypadding 0
                     xmargin 5
                     ymargin 5
                     if telephone_number == number_npc-2:
                         add "gui/telephone/contact_hover.png"
                     else:
                         add "gui/telephone/contact_idle.png"
                     hover_background "gui/telephone/contact_hover.png"
                     textbutton '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}[name_npc]{/font}{/size}{/color}' ypos 0 xpos 10
                     action Hide("sms_phone1"), SetVariable('telephone_number', number_npc-2), SetVariable('page_phone', 1), SetVariable('messange_npc', 0), SetVariable('npc_id', npc_id)
     imagebutton xpos 100 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/phone_idle.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/phone.png", 0, 1.2))
         if not telephone_number == -10:
             if page_phone == 1:
                 action Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_"), Jump('call_hover')
         else:
             action Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_"), Jump('call_hover_suzuki')
     imagebutton xpos 180 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/messages_idle.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/messages.png", 0, 1.2))
         if not telephone_number == -10:
             if page_phone == 1:
                 action SetVariable('messange_npc', 0), Show('sms_phone1')
     imagebutton xpos 260 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/information.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/messages.png", 0, 1.2))
     imagebutton xalign 0.002 ypos 920 focus_mask True:
         idle (im.Rotozoom("gui/system/icons/phone.png", 0, 1.4))
         hover (im.Rotozoom("gui/system/icons/phone_hover.png", 0, 1.4))
         action SetVariable('page_phone', 0), Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_")
screen sms_phone_:
     modal True
     add "gui/telephone/telephone.png" xpos -35 ypos 10
     vpgrid:
         cols 1
         rows 20
         spacing -459
         xpos 57 ypos 471 xysize (300, 415)
         child_size (300, 500)
         draggable True
         mousewheel True
         arrowkeys True
         scrollbars 'vertical'
         if suzuki_number == 1:
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 if telephone_number == -10:
                     add "gui/telephone/contact_hover.png"
                 else:
                     add "gui/telephone/contact_idle.png"
                 hover_background "gui/telephone/contact_hover.png"
                 textbutton '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Сузуки Мацуи{/font}{/size}{/color}' ypos 0 xpos 10
                 action Hide("sms_phone1"), SetVariable('telephone_number', -10), SetVariable('messange_npc', 0)
         for number_npc in range(1, number_npc_max):
             $ npc_id = 'npc'+str(number_npc)
             $ number_phone = eval(npc_id)["number_phone"]
             if number_phone == 1:
                 $ contact_npc = eval(npc_id)["contact_npc"]
                 $ npc_name = eval(npc_id)["npc_name"]
                 $ npc_fam = eval(npc_id)["npc_fam"]
                 $ name_npc = npc_name + ' ' + npc_fam
                 $ location_npc = eval(npc_id)["location_npc"]
                 button:
                     xpadding 0
                     ypadding 0
                     xmargin 5
                     ymargin 5
                     if telephone_number == number_npc-2:
                         add "gui/telephone/contact_hover.png"
                     else:
                         add "gui/telephone/contact_idle.png"
                     hover_background "gui/telephone/contact_hover.png"
                     textbutton '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}[name_npc]{/font}{/size}{/color}' ypos 0 xpos 10
                     action Hide("sms_phone1"), SetVariable('telephone_number', number_npc-2), SetVariable('page_phone', 1), SetVariable('messange_npc', 0), SetVariable('npc_id', npc_id)
     imagebutton xpos 100 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/phone_idle.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/phone.png", 0, 1.2))
         if not telephone_number == -10:
             if page_phone == 1:
                 action Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_"), Jump('call_hover')
         else:
             action Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_"), Jump('call_hover_suzuki')
     imagebutton xpos 180 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/messages_idle.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/messages.png", 0, 1.2))
         if not telephone_number == -10:
             if page_phone == 1:
                 action SetVariable('messange_npc', 0), Show('sms_phone1')
     imagebutton xpos 260 ypos 870 focus_mask True:
         idle (im.Rotozoom("gui/telephone/information.png", 0, 1.2))
         hover (im.Rotozoom("gui/telephone/messages.png", 0, 1.2))
     imagebutton xalign 0.002 ypos 920 focus_mask True:
         idle (im.Rotozoom("gui/system/icons/phone.png", 0, 1.4))
         hover (im.Rotozoom("gui/system/icons/phone_hover.png", 0, 1.4))
         action SetVariable('page_phone', 0), Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_")
screen sms_phone1:
     $ npc_id = npc_id
     add 'gui/telephone/sms_osn.png'
     if messange_npc == 1 or messange_npc == 3:
         $ gender_npc = eval(npc_id)["gender_npc"]
         $ location_npc = eval(npc_id)["location_npc"]
         button xpos 450 ypos 170:
             add 'gui/telephone/podlozhka.png':
                 size(400, 50)
             text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Ты где сейчас находишься?{/font}{/size}{/color}' xpos 20 ypos 5
         if location_npc == 'school_class':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в классе, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'join_school':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас у входа школы, но,\возможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'corridor_school':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в школьном коридоре,\nно, возможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'roof':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас на крыше школы, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'canteen':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в столовой, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'pool':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в бассейне, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'park':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в парке, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'shopping_center':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в ТЦ, но,\nвозможно скоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'occult_club':
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 130)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в комнате клуба\nоккультизма, но, возможно\nскоро уйду оттуда.{/font}{/size}{/color}' xpos 20 ypos 5
         elif location_npc == 'apartament':
             $ messange_npc = 3
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 50)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас у себя дома.{/font}{/size}{/color}' xpos 20 ypos 5
         else:
             $ messange_npc = 3
             button xpos 500 ypos 230:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 if gender_npc == 1:
                     text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас немного занят.\nДавай позже?{/font}{/size}{/color}' xpos 20 ypos 5
                 else:
                     text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас немного занята.\nДавай позже?{/font}{/size}{/color}' xpos 20 ypos 5
     elif messange_npc == 2:
         $ gender_npc = eval(npc_id)["gender_npc"]
         if gg == 1:
             $ location_npc1 = 'join_school'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас у школьного двора.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 2:
             $ location_npc1 = 'corridor_school'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в школьном коридоре.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 3:
             $ location_npc1 = 'school_class'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в классе.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 4:
             $ location_npc1 = 'roof'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас на крыше школы.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 7:
             $ location_npc1 = 'park'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в парке.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 19:
             $ location_npc1 = 'shopping_center'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в продуктовом.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 20:
             $ location_npc1 = 'shopping_center'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в ТЦ.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 21:
             $ location_npc1 = 'student_soviet'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в комнате студенческого совета.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 22:
             $ location_npc1 = 'canteen'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в столовой.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 23:
             $ location_npc1 = 'pool'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас рядом с бассейной.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         elif gg == 24:
             $ location_npc1 = 'occult_club'
             button xpos 450 ypos 170:
                 add 'gui/telephone/podlozhka.png':
                     size(400, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Я сейчас в комнате клуба оккультизма.\nМожет, давай встретимся?{/font}{/size}{/color}' xpos 20 ypos 5
         if contact_npc >= random:
             button xpos 500 ypos 270:
                 add 'gui/telephone/podlozhka.png':
                     size(420, 100)
                 text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Без проблем! Сейчас приду к тебе.{/font}{/size}{/color}' xpos 20 ypos 5
             $ npc_name = eval(npc_id)["npc_name"]
             $ npc_fam = eval(npc_id)["npc_fam"]
             $ name_npc = npc_name + ' ' + npc_fam
             button xpos 440 ypos 950:
                 focus_mask True
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 hover_background "gui/telephone/sms_hover.png"
                 idle_background "gui/telephone/sms_idle.png"
                 unhovered SetVariable('telephone_number1', 1)
                 hovered SetVariable('telephone_number1', 4)
                 if telephone_number1 <= 3 or telephone_number1 >= 5:
                     textbutton '{color=505050}{size=30}{font=gui/fonts/alegreya.ttf}Дождаться [name_npc]{/font}{/size}{/color}' xpos 20 ypos 0
                 else:
                     textbutton '{color=ffffff}{size=30}{font=gui/fonts/alegreya.ttf}Дождаться [name_npc]{/font}{/size}{/color}' xpos 20 ypos 0
                 action Hide("sms_phone1"), Hide("sms_phone_"), Hide("call_phone_"), SetVariable('page', npc_id), SetVariable('location_npc1', location_npc1), Jump('ads')
         else:
             if gender_npc == 1:
                 button xpos 500 ypos 270:
                     add 'gui/telephone/podlozhka.png':
                         size(420, 100)
                     text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Извини, но я сейчас немного\nзанят... Давай потом?{/font}{/size}{/color}' xpos 40 ypos 5
             else:
                 button xpos 500 ypos 270:
                     add 'gui/telephone/podlozhka.png':
                         size(420, 100)
                     text '{color=#282828}{size=25}{font=gui/fonts/alegreya.ttf}Извини, но я сейчас немного\nзанята... Давай потом?{/font}{/size}{/color}' xpos 40 ypos 5
     button xpos 440 ypos 850:
         focus_mask True
         xpadding 0
         ypadding 0
         xmargin 5
         ymargin 5
         hover_background "gui/telephone/sms_hover.png"
         idle_background "gui/telephone/sms_idle.png"
         unhovered SetVariable('telephone_number1', 1)
         hovered SetVariable('telephone_number1', 2)
         if telephone_number1 == 1 or telephone_number1 >= 3:
             textbutton '{color=505050}{size=30}{font=gui/fonts/alegreya.ttf}Спросить местоположение{/font}{/size}{/color}' xpos 40 ypos 0
         else:
             textbutton '{color=ffffff}{size=30}{font=gui/fonts/alegreya.ttf}Спросить местоположение{/font}{/size}{/color}' xpos 40 ypos 0
         action SetVariable('location_npc', location_npc), SetVariable('minute', minute+3), SetVariable('messange_npc', 1)
     if not hour <= 7:
         if not hour >= 22:
             if not messange_npc == 3:
                 button xpos 440 ypos 900:
                     focus_mask True
                     xpadding 0
                     ypadding 0
                     xmargin 5
                     ymargin 5
                     hover_background "gui/telephone/sms_hover.png"
                     idle_background "gui/telephone/sms_idle.png"
                     unhovered SetVariable('telephone_number1', 1)
                     hovered SetVariable('telephone_number1', 3)
                     if not gg == 5:
                         if telephone_number1 <= 2 or telephone_number1 >= 4:
                             textbutton '{color=505050}{size=30}{font=gui/fonts/alegreya.ttf}Назвать свое местоположение{/font}{/size}{/color}' xpos 20 ypos 0
                         else:
                             textbutton '{color=ffffff}{size=30}{font=gui/fonts/alegreya.ttf}Назвать свое местоположение{/font}{/size}{/color}' xpos 20 ypos 0
                     if not gg == 5:
                         action SetVariable('messange_npc', 2), SetVariable('minute', minute+3), SetVariable('random', renpy.random.randint(1, 100))
label ads:
     $ minute += 10
     $ location_npc = location_npc1
     $ eval(page)["location_npc"] = location_npc
     $ page = 1
     jump check_location
label call_hover:
     if gg == 1:
         if hour <= 16:
             scene image "gui/overlay/mm/main_menu1.png"
         elif hour <= 19:
             scene image "gui/overlay/mm/main_menu2.png"
         elif hour >= 20:
             scene image "gui/overlay/mm/main_menu3.png"
     elif gg == 2:
         if hour <= 16:
             scene image "backgrounds/school/corridor.png"
         elif hour <= 19:
             scene image "backgrounds/school/corridor1.png"
         elif hour >= 20:
             scene image "backgrounds/school/corridor2.png"
     elif gg == 3:
         scene image "backgrounds/school/class.jpg"
     elif gg == 4:
         if hour <= 3:
             scene image "backgrounds/school/roof_night.jpg":
                 size(1920, 1080)
         elif hour <= 7:
             scene image "backgrounds/school/roof_v.jpg":
                 size(1920, 1080)
         elif hour <= 18:
             scene image "backgrounds/school/roof_ut.jpg":
                 size(1920, 1080)
         elif hour <= 22:
             scene image "backgrounds/school/roof_v.jpg":
                 size(1920, 1080)
         else:
             scene image "backgrounds/school/roof_night.jpg":
                 size(1920, 1080)
     elif gg == 5:
         if hour <= 3:
             scene image "backgrounds/location/ph/room_night.png"
         elif hour <= 7:
              scene image "backgrounds/location/ph/room_v.png"
         elif hour <= 16:
              scene image "backgrounds/location/ph/room_ut.png"
         elif hour <= 19:
              scene image "backgrounds/location/ph/room_v.png"
         elif hour <= 24:
              scene image "backgrounds/location/ph/room_night.png"
     elif gg == 7:
         if hour <= 3:
             scene image "backgrounds/location/park/2.png":
                 size(1920, 1080)
         elif hour <= 16:
             scene image "backgrounds/location/park/1.png":
                 size(1920, 1080)
         elif hour <= 19:
             scene image "backgrounds/location/park/2.png":
                 size(1920, 1080)
         elif hour <= 25:
             scene image "backgrounds/location/park/3.png":
                 size(1920, 1080)
     elif gg == 12:
         if hour <= 16:
             scene image "backgrounds/school/stairs2.png"
         else:
             scene image "backgrounds/school/stairs.png"
         if hour == 8 or hour == 10 or hour == 12 or hour == 14:
             scene image "backgrounds/school/stairs1.png"
     elif gg == 13:
         if hour <= 16:
             scene image "backgrounds/school/corridor21.png"
         elif hour <= 19:
             scene image "backgrounds/school/corridor22.png"
         else:
             scene image "backgrounds/school/corridor23.png"
     elif gg == 20:
         if hour <= 3:
             scene image "backgrounds/location/shopping_center/shopping_center_ut.png"
         elif hour <= 16:
             scene image "backgrounds/location/shopping_center/shopping_center_v.png"
         elif hour <= 20:
             scene image "backgrounds/location/shopping_center/shopping_center_ut.png"
         elif hour >= 21:
             scene image "backgrounds/location/shopping_center/shopping_center_v.png"
     elif gg == 22:
         if hour <= 3:
             scene image "backgrounds/school/canteen/canteen_n.jpg":
                 size(1920, 1080)
         elif hour <= 6:
             scene image "backgrounds/school/canteen/canteen_v.jpg":
                 size(1920, 1080)
         elif hour <= 16:
             scene image "backgrounds/school/canteen/canteen_ut.jpg":
                 size(1920, 1080)
         elif hour >= 22:
             scene image "backgrounds/school/canteen/canteen_n.jpg":
                 size(1920, 1080)
         elif hour >= 17:
             scene image "backgrounds/school/canteen/canteen_v.jpg":
                 size(1920, 1080)
     elif gg == 23:
         if hour <= 3:
             scene image "backgrounds/school/pool/pool_n.jpg":
                 size(1920, 1080)
         elif hour <= 7:
             scene image "backgrounds/school/pool/pool_v.jpg":
                 size(1920, 1080)
         elif hour <= 16:
             scene image "backgrounds/school/pool/pool_ut.jpg":
                 size(1920, 1080)
         elif hour <= 19:
             scene image "backgrounds/school/pool/pool_v.jpg":
                 size(1920, 1080)
         else:
             scene image "backgrounds/school/pool/pool_n.jpg":
                 size(1920, 1080)
     python:
         name_npc = eval(npc_id)["npc_name"]
         fam_npc = eval(npc_id)["npc_fam"]
         contact_npc = eval(npc_id)["contact_npc"]
         love_npc = eval(npc_id)["love_npc"]
         v_npc = eval(npc_id)["pich_npc"]
         gender_npc = eval(npc_id)["gender_npc"]
     image side npc = "character/npc/npc_m/[v_npc].png"
     if contact_npc >= 100:
         $ contact_npc = 100
     if days <= 5 and hour <= 16:
         $ npc_otvet = renpy.random.randint(1, contact_npc/4)
     elif days <= 5 and hour >= 17:
         $ npc_otvet = renpy.random.randint(1, contact_npc)
     elif days >= 6 and hour <= 8:
         $ npc_otvet = renpy.random.randint(1, contact_npc/4)
     elif days >= 6 and hour >= 9:
         $ npc_otvet = renpy.random.randint(1, contact_npc)
     if npc_otvet <= 35:
         "Слушая долгий монотонный гудок нудную минуту, вскоре вы поняли, что отвечать вам не собираются то ли от занятости, то ли от отсутствия желания вступать в какой бы то ни было контакт. Забросив всю эту затею, вы нажали кнопку сброса и положили телефон обратно в карман."
         jump check_location
     else:
         "Казалось, что в течении целой вечности вы слушали монотонный, бесконечно тянущийся телефонный гудок. Спустя минуту ваших бесконечно-вечных ожиданий, вам ответили и поинтересовались целью звонка."
         menu:
             "{color=#000000}Просто поговорить{/color}":
                 $ energy -= 5
                 "Разговаривая целый час со своей целью, вы перебирали многие темы, которые бы обсуждали при встрече: повседневные, личные, а также обычные сплетни, присутствующие в вашем диалоге, казалось, везде и всюду."
                 "Но всему, даже самым интересным вещам, суждено когда-либо закончиться. Спустя час рутинного, но достаточно увлекательного диалога, ваш собеседник попрощался с вами, ссылаясь на то, что у него дела."
                 $ contact_npc += contact_gg_npc * 2
                 $ love_npc += love_gg_npc * 2
                 jump check_location
             "{color=#000000}Пригласить к себе домой{/color}":
                 if gg == 5:
                     python:
                         energy -= 10
                         name_npc = name_npc + " " + fam_npc
                         name_npc = str(name_npc)
                         npc = Character("name_npc", who_suffix = ':', dynamic=True, image='npc')
                     if gender_npc == 1:
                         glgg "Не хотел бы провести время у меня дома?"
                         $ npc_otvet = renpy.random.randint(1, contact_npc * 2)
                         if npc_otvet >= 35:
                             npc "С радостью, дружище! Когда подъезжать?"
                         else:
                             npc "Не, извини. Сегодня я занят. Перезвони мне позже."
                             jump phone
                         if gg == 5:
                             "Решив встретиться через час у вас дома, вы почесали свой живот, лежа на кровати, и попросту забили на уборку. В конце концов не девушка же в гостях!"
                         else:
                             "Решив встретиться через час у вас дома, вы быстрым шагом направились в ваше жилище, в которое зашли уже спустя пару десятков минут."
                         $ hour += 1
                         "Спустя некоторое время ваш названный гость все же перешел порог вашей квартиры, где вы встретили его крепким рукопожатием и провели в свою единственную, но достаточно просторную комнату."
                         "Разговаривая целый час о разных вещах, вперемешку обсуждая тела девушек и изредка поигрывая в компьютер, вы отлично провели время со своим собеседником, которому, видно, тоже понравилось ваше времяпрепровождение."
                         "Устало потянувшись и зевнув, ваш гость посмотрел на время и сказал, что ему уже пора. Проводив его к порогу, вы попрощались вновь крепким рукопожатием и отправили в путь-дорогу [name_npc], который истребил половину вашего холодильника!"
                         $ contact_npc += contact_gg_npc * 4
                     else:
                         "Пригласив к себе вашу новоиспеченную подругу в гости, вы быстрым темпом начали убираться в комнате, кидая носки под кровать, пустые бутылки закидывая за шкаф, а также изредка протирая тряпочкой пыльную мебель."
                         "Завершив все за достаточный промежуток времени, вы устало потянулись, после чего глянули на часы, показывающие, что ваш гость уже опаздывает на десяток минут. Тяжело вздохнув, вы упали на кровать уже и не надеясь, что девушка порадует вас своим присутствием, но ваши раздумья прервал громкий звонок в дверь, сразу же отбросивший ваши опасения."
                         scene image "actions/phone/game_female.png":
                             size (1920, 1080)
                         "За секунды преодолев такое недалекое расстояние, вы открыли входную дверь, где вас встретила улыбчивая девушка, [name_npc]. Выругивая себя за странную и нелепую паранойю, ваш взор и не заметил беспардонное движение вашей гостьи в сторону комнаты. Расположившись на вашей кровати, девушка схватила геймпад, сразу же начав играть, оставляя вас со своим самобичеванием наедине. Почесав затылок, только спустя минуту до вас дошло, что вас бросили у порога."
                         "Снова выругавшись на себя, но уже за рассеянность, вы закрыли входную дверь на несколько оборотов и направились по следу гостьи, которая благополучно заняла всю вашу кровать и не обращала на вас никакого внимания некоторое время."
                         scene image "actions/phone/game_female1.png":
                             size (1920, 1080)
                         "Присев на пол, близ девушки, вы даже и не заметили, как она вскоре подвинулась поближе к вам, чуть ли не садясь на колени. Увлеченно играя в игру, гостья постоянно ерзала пятой точкой по полу до тех пор, пока и вовсе не ретировалась на ваши ноги, используя те как стулья. Картина маслом: вместо удобной кровати особь женского пола выбирает место, которое попросту не предназначено для сидения на нем..."
                         "Еще некоторое время удивляясь такому странному решению, вы смиренно приняли судьбу кресла, пялясь на то, как [name_npc] играется в игры, портя статистики ваших аккаунтов."
                         scene image "actions/phone/game_female2.png":
                             size (1920, 1080)
                         "Вскоре, видно, пожалев вас, [name_npc] присела возле вас, предложив вместе сыграть в игру. Будучи не против подобных раскладов, вы потерли больное насиженное место от костлявой задницы девушки и взяли джойстик, начав играть с ней в шутеры, в которых явным победителем были вы. Убивая вашего противника с соотношением пять к одному, он сдался, обиженно надув щечки и назвав читером."
                         "Будучи довольным собой, вы и не заметили, как девушка взяла с вашего холодильника последние остатки чего-то съедобного и жадно поедала, приговаривая, что это все месть!"
                         scene image "actions/phone/game_female3.png":
                             size (1920, 1080)
                         "Проводя подобным образом время еще под час, девушка устало глянула на время, высказав, что ей уже пора домой! Проводив до порога гостью, вас прижали к стене и поблагодарили за весело проведенное время, упоминая, что она подобное не забудет и чмокая вас в щечку. Мило улыбнувшись под конец, [name_npc] попрощалась с вами и покинула пределы вашего дома."
                         $ contact_npc += contact_gg_npc * 4
                         $ love_npc += love_gg_npc * 4
                 else:
                     "Нужно находиться дома, чтобы приглашать кого-либо."
     $ eval(npc_id)["love_npc"] = love_npc
     $ eval(npc_id)["contact_npc"] = contact_npc
     jump check_location
label call_hover_ayano:
     "Данная функция недоступна"
     jump check_location
label call_hover_suzuki:
     scene bf
     if hour >= 14 and hour <= 20:
         "Глянув на экран разблокировки своего старенького телефона, вас охватило внезапное желание позвонить Сузуки, услышать ее голос и, возможно, даже встретиться."
         "Исполняя свое хотение, вы поднесли к уху свой мобильник, из которого звучал привычный и монотонный гудок, длившийся несоизмеримо долго по вашим меркам: целую минуту!"
         "В конце концов дождавшись ответа от Сузуки, вы сразу же услышали одну фразу, которая поставила крест на вашем дальнейшем разговоре: я на работе, перезвони позже."
         "Удрученно вздохнув, вы пожелали удачи девушке в ее нелегком деле, после сбросив звонок."
         jump check_location
     elif hour >= 2 and hour <= 8:
         "Глянув на экран разблокировки своего старенького телефона, вас охватило внезапное желание позвонить Сузуки, услышать ее голос и, возможно, даже встретиться."
         "Исполняя свое хотение, вы поднесли к уху свой мобильник, из которого звучал привычный и монотонный гудок, который, как вы поняли, и не собирался прекращаться."
         "Возможно, стоит позвонить чуть позже. В конце концов-то время позднее."
         jump check_location
     else:
         jump suzuki_call_number
