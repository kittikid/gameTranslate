image zavod = "backgrounds/zavod.jpg"
image zavod1 = "backgrounds/zavod1.png"
image f = im.Rotozoom("character/npc/5/1.png", 0, 0.6)
image f1 = im.Rotozoom("character/npc/5/2.png", 0, 0.6)
image f2 = im.Rotozoom("character/npc/5/3.png", 0, 0.6)
label zavod:
     if language_game == 1:
         if zavod_first == True:
             "Только открыв дверь в заводской цех и переступив за порог, вас встретила девушка с собеседования. В руках она держала рабочую форму."
             show nac2 with dissolve
             n "Вот, держи."
             "После этих слов девушка передала вам форму, которую вы сразу же взяли."
             n "Раздевалка прямо по коридору, там будет еще большое скопление людей. Удачной тебе смены!"
             "Почесав затылок в раздумьях ничего ли она не забыла вам сказать, девушка пожала плечами, а после покинула вас."
             scene zavod1
             show f
             "Послушав ее, вы дошли до раздевалки, где было достаточно много людей за тридцать. Пройдя в самый конец, вы переоделись в рабочую форму, как буквально в тот же момент к вам подошел достаточно старый мужчина."
             f "Так значит это ты новый работник, которого я должен обучать?"
             "Произнес он, оголив свой рот, где не хватало если не парочку, то под десяток зубов уж точно. Вы ответили на его вопрос положительно."
             f "Значит так, сейчас у меня много работы, так что скажи мне: тебе действительно нужно обучение?"
             menu:
                 "{color=#000000}Да{/color}":
                     "Тяжело вздохнув, работник начал рассказывать, что нужно делать"
                     "Если быть кратким, то твоя задача состоит в том, чтобы нажимать правильные кнопки в нужный момент. Обычное QTE. Простое и понятное."
                     jump complex_zavod
                 "{color=#000000}Нет{/color}":
                     f "Ну вот и отлично. Значит я пошел."
                     "Развернувшийся к вам спиной мужчина вскоре пропал из виду, уйдя в цех и оставив вас одного. Вскоре вы последовали его примеру."
                     jump complex_zavod
         else:
             "Придя на очередную смену завода, вы быстро переоделись и направились к уже привычному для вас станку."
     elif language_game == 2:
         if zavod_first == True:
             "Just opening the door to the factory floor and stepping over the threshold, did you meet the girl for an interview."
             show nac2 with dissolve
             n "Here you are."
             "After these words, the girl gave you the form that you immediately took."
             n "The dressing room is right down the hall, there will be a still large crowd of people. Have a nice change!"
             "Having scratched her head in thought, didn’t she forget to tell you anything, the girl shrugged, and then left you."
             scene zavod1
             show f
             "After listening to her, you got to the locker room, where there were quite a lot of people over thirty. Having gone to the very end, you changed into a working uniform, as literally at that very moment a fairly old man came up to you."
             f "So, now I have a lot of work, so tell me: do you really need training?"
             menu:
                 "{color=#000000}Yes{/color}":
                     "Taking a deep breath, the employee began to tell what to do."
                     "To be brief, your task is to press the right buttons at the right time. Normal QTE. Simple and straightforward."
                     jump complex_zavod
                 "{color=#000000}No{/color}":
                     f "Well, that's great. So I went."
                     "The man who turned his back on you soon lost sight of him, having left the workshop and left you alone. Soon you followed suit."
                     jump complex_zavod
         else:
             "Arriving at the next shift of the plant, you quickly changed clothes and headed to the machine that was already familiar to you."
label complex_zavod:
     $ zavod_first = False
     if qte_zavod == 3:
         if language_game == 1:
             "Вы закончили на сегодня свою смену."
         elif language_game == 2:
             "You have finished your shift today."
         $ qte_zavod = 0
         $ money += 1000
         jump home
     scene zavod
     if language_game == 1:
         "Подойдя к станку, вы начали делать то, за что вам, собственно, и платят"
     elif language_game == 2:
         "Approaching the machine, you began to do what you, in fact, are paid for"
     scene bf
     call screen qte_zavod
screen qte_zavod(word="", time=5.0, length=5):
     on 'show' action qteInit(word, time, length)
     modal True
     if qte_word:
         timer 0.01 repeat True action [SetVariable("qteTime", qteTime - .01), If(qteTime <= .0, true=Jump('qte_zavod_loss'))]
         text next_k.upper() align(.5, .5) size 96
         if len(next_k) == 1:
             key next_k action NextKey()
     else:
         timer .1 action Jump('qte_zavod_win'),
     bar value StaticValue(qteTime, qteMaxTime) align(.5, .1) xmaximum 600
label qte_zavod_win:
     $ energy -= 30
     $ hour += 1
     $ minute += 30
     $ qte_zavod += 1
     $ money += 100
     jump zavod_relaxation
label qte_zavod_loss:
     $ energy -= 25
     $ hour += 1
     $ minute += 30
     $ qte_zavod += 1
     jump zavod_relaxation
label zavod_relaxation:
     if language_game == 1:
         menu:
             "{color=#000000}Отдохнуть с сигаретой в руках, как другие рабочие{/color}":
                 if cigarette >= 1:
                     $ energy += 7
                     "Как только вы закурили, в вас будто прибавилось энергии, и вы были буквально готовы работать 24/7."
                     "Через 5 минут вы встали и пошли обратно за станок"
                     jump complex_zavod
                 else:
                     "У вас нет сигарет."
                     jump zavod_relaxation
             "{color=#000000}Сесть на лавочку, дабы отдышаться{/color}":
                 $ energy += 5
                 "Упав на лавочку, вы расслабились, дожидаясь, пока хоть немного, но вы восстановите свои силы."
                 "Через 5 минут вы встали и пошли обратно за станок"
                 jump complex_zavod
     elif language_game == 2:
         menu:
             "{color=#000000}Relax with a cigarette in your hands, like other workers{/color}":
                 if cigarette >= 1:
                     $ energy += 7
                     "As soon as you lit a cigarette, you seemed to have increased energy, and you were literally ready to work 24/7."
                     "After 5 minutes you got up and went back behind the machine"
                     jump complex_zavod
                 else:
                     "У вас нет сигарет."
                     jump zavod_relaxation
             "{color=#000000}Sit on a bench in order to catch your breath{/color}":
                 $ energy += 5
                 "Having fallen on a bench, you relaxed, waiting until at least a little, but you will regain your strength."
                 "After 5 minutes you got up and went back behind the machine."
                 jump complex_zavod


















label magazine_game:
     scene image "backgrounds/location/magazine/joob_magazine.png"
     $ random_ivent = renpy.random.randint(1, 100)
     if random_ivent >= 97:
         $ random_ivent = 3
         python:
             renpy.jump('ivent_magazine'+str(random_ivent))
     if reputation_joob >= -250:
         $ time = 4
     elif reputation_joob >= 50:
         $ time = 6
     elif reputation_joob >= 300:
         $ time = 10
     $ MiniGameTime = time
     $ MiniGameMaxTime = time
     $ ProgressGameMax = 50
     $ random_icon = renpy.random.randint(1, 6)
     $ random_icon_v = renpy.random.randint(1, 9)
     $ random_icon_z = renpy.random.randint(3, 9)
     $ random_icon_v = float(random_icon_v) / 10
     $ random_icon_z = float(random_icon_z) / 10
     $ ProgressGameOld = ProgressGame
     call screen magazine_game
screen magazine_game:
     add "backgrounds/location/magazine/joob_magazine.png"
     timer 0.01 repeat True action [SetVariable("MiniGameTime", MiniGameTime - .01), If(MiniGameTime <= .0, true=Jump('magazine_game_over'))]
     bar value StaticValue(MiniGameTime, MiniGameMaxTime) align(.5, .05) xmaximum 1000
     bar value StaticValue(ProgressGame, ProgressGameMax) align(.5, .1) xmaximum 1000
     frame xalign random_icon_v yalign random_icon_z:
         if random_icon == 1:
             imagebutton:
                 idle ("icons/icons_rolton.png")
                 hover ("icons/icons_rolton_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')
         elif random_icon == 2:
             imagebutton:
                 idle ("icons/icons_cola.png")
                 hover ("icons/icons_cola_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')
         elif random_icon == 3:
             imagebutton:
                 idle ("icons/icons_heal.png")
                 hover ("icons/icons_heal_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')
         elif random_icon == 4:
             imagebutton:
                 idle ("icons/icons_candy.png")
                 hover ("icons/icons_candy_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')
         elif random_icon == 5:
             imagebutton:
                 idle ("icons/icons_lighter.png")
                 hover ("icons/icons_lighter_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')
         elif random_icon == 6:
             imagebutton:
                 idle ("icons/icons_smoking.png")
                 hover ("icons/icons_smoking_hover.png")
                 action SetVariable('ProgressGame', ProgressGame+1), SetVariable('MiniGameTime', MiniGameTime+0.1), Jump('magazine_game_info')

label magazine_game_info:
     $ random_ivent = renpy.random.randint(1, 100)
     if random_ivent >= 95:
         $ random_ivent = renpy.random.randint(1, 2)
         python:
             renpy.jump('ivent_magazine'+str(random_ivent))
     $ random_icon = renpy.random.randint(1, 6)
     $ random_icon_v = renpy.random.randint(1, 9)
     $ random_icon_z = renpy.random.randint(3, 9)
     $ random_icon_v = float(random_icon_v) / 10
     $ random_icon_z = float(random_icon_z) / 10
     call screen magazine_game
label magazine_game_over:
     scene image "backgrounds/location/magazine/joob_magazine.png"
     $ ProgressGameNew = ProgressGame
     $ ProgressGameNew -= ProgressGameOld
     if ProgressGameNew <= 5:
         "Закончив с работой, вы ловите на себе строгий взгляд вашего начальника и понимаете, что вам следует стараться лучше!"
     elif ProgressGameNew <= 10:
         "Закончив с работой, вы ловите на себе безразличный взгляд начальника."
     elif ProgressGameNew <= 20:
         "Закончив с работой, вы ловите на себе одобрительный взгляд вашего начальника. Возможно, если вы продолжите работать в том же духе, вас ждёт повышение!"
     $ hour += 4
     $ energy -= 50
     if reputation_joob >= 399:
         $ money_joob = renpy.random.randint(800, 1001)
     elif reputation_joob >= 249:
         $ money_joob = renpy.random.randint(500, 750)
     elif reputation_joob >= 99:
         $ money_joob = renpy.random.randint(370, 490)
     elif reputation_joob >= 0:
         $ money_joob = renpy.random.randint(250, 350)
     elif reputation_joob >= -250:
         $ money_joob = renpy.random.randint(50, 170)
     $ money += money_joob
     $ joob_complete = 1
     if ProgressGame >= 49:
         if reputation_joob >= 399:
             $ money += 2400
         elif reputation_joob >= 249:
             $ money += 1500
         elif reputation_joob >= 99:
             $ money += 800
         elif reputation_joob >= 0:
             $ money += 500
         if reputation_joob >= -250:
             $ money += 300
         $ reputation_joob += 10
         $ ProgressGame = 0
         "Вы получили премию!"
         "{color=66FF00}Вы получили 10 очков репутации!{/color}"
     if suzuki == 0:
         if hentai_patch_inicial == True:
             if hour >= 15 and hour <= 19:
                 jump suzuki0
     "Уходя с работы, вы чувствуете небольшую усталость, но в тоже время вы довольны собой. За ваши старания вы получаете [money_joob] кредитов."
     if warn_joob >= 3:
         "Вы были уволены с работы за получения трех или более выговоров!"
         $ joob = 2
     jump product_magazine
label shopping_joob:
     scene image "backgrounds/location/magazine/joob_magazine.png"
     if joob == 1:
         if joob_complete == 0:
             "Зайдя в кабинет, вы готовитесь к ещё одному увлекательному рабочему дню, мысленно разминая все свои части тела. Подойдя к своему рабочему месту, вы принимаетесь за работу."
             jump magazine_game
         elif joob_complete == 1:
             "Вы уже работали сегодня."
             jump product_magazine
     elif joob == 2:
         "Вы совершенно недавно были уволены!"
     else:
         scene image "character/joob/magazine/cab.png"
         image adm_magazine g1 = "character/joob/magazine/1.png"
         image adm_magazine g2 = "character/joob/magazine/2.png"
         image adm_magazine g3 = "character/joob/magazine/3.png"
         image adm_magazine g4 = "character/joob/magazine/4.png"
         image adm_magazine g5 = "character/joob/magazine/5.png"
         image adm_magazine g6 = "character/joob/magazine/6.png"
         "Без особых проблем войдя в нужное вам помещение, на ваши глаза сразу же попался мужчина средних лет, разбирающийся в бумагах и не поднимающий своего взгляда на вас то ли из-за концентрации на работе, то ли из-за нежелания отрываться от оной."
         glgg "Здравствуйте, я здесь насчет объяв..."
         show adm_magazine g2
         adm_magazine "Подождите."
         "Так и не дав вам договорить, мужчина продолжил увлеченно работать с бумагами, что продолжалось еще под десяток так минут. Аккуратно положив свою ручку и очки на стол, мужчина устало потер глаза и оглянул вас, сидящих на диване в ожидании своей очереди, с головы до пят."
         adm_magazine "Так вы сказали, что пришли по объявлению?"
         glgg "Верно, я пришел по объявлению."
         adm_magazine "{b}*Тяжелый вздох*{/b} Хорошо, я понял. Почему вы выбрали именно эту вакансию?"
         menu:
             "{color=#000000}Я целеустремленный и всегда добиваюсь своего. Думаю, что эта вакансия раскроет весь мой потенциал.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
                 adm_magazine "Креативность точно не ваш конек. Ладно, хорошо, сколько вам лет?"
                 glgg "Я школьн..."
                 adm_magazine "И как же вы собрались устроиться на работу, будучи школьником без резюме, опыта и креативности?"
                 menu:
                     "{color=#000000}Мне просто нужны деньги.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
                         jump _succes
                     "{color=#000000}Я достаточно интересная личность.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
                         "Сказав это, вы буквально поставили крест на данной работе, что и говорил грозный взгляд работодателя."
                         adm_magazine "Я вас понял. Приходите, когда окончите школу."
                         "Решив все же не усугублять ситуацию, вы вышли из кабинета без работы, униженным, так еще и без гроша в кармане."
                         $ joob = 2
                         jump product_magazine
             "{color=#000000}Мне просто нужны деньги.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
                 label _succes:
                 show adm_magazine g1
                 "После вашего ответа вы заметили небольшую искорку любопытства в глазах у мужчины, который встал со своего уже насиженного места, прихватив с собой анкету со стола. Подойдя к вам, он протянул бумажку, которую вы сразу же взяли."
                 adm_magazine "Знаешь, я всегда ценил честность в людях. За всю мою карьеру лишь единицы говорили подобное, когда же другая часть кичилась одними и теми же качествами, которыми, как ни странно, не обладал никто. Мой управленческий опыт говорит, что ты меня уж точно не подведешь!"
                 "Грубо и достаточно сильно похлопав вас по плечу несколько раз, ваш новый работодатель присел на диван напротив и с интересом наблюдал за вашими действиями."
                 glgg "Можно поподробнее узнать о вакансии?"
                 adm_magazine "Конечно! Если говорить коротко и понятно, то нам нужен сортировщик товаров. Работа непыльная и, соответственно, низкооплачиваемая: 350-450 кредитов за один рабочий день в зависимости от выполненной работы."
                 adm_magazine "Есть карьерный рост до менеджера, который получает уже фиксированный процент от продаж, как заработную плату."
                 adm_magazine "График прост до безобразия: работать нужно всю неделю по 4 часа, кроме воскресенья. Как плюс, он еще и полностью свободный, то есть работай хоть ночью, хоть утром, хоть днем."
                 adm_magazine "Главное, чтобы ты отсортировал за эти 4 часа весь товар: просрочку убрал с витрин, новый продукт поставил сзади старого, ну и дальше, думаю, ты понял. Обычные приемчики супермаркетов и гипермаркетов."
                 menu:
                     "{color=#000000}Вполне себе неплохо!\n{size=21}{i}50 энергии{/i}{/size}{/color}":
                         $ ProgressGame = 0
                         show adm_magazine g4
                         adm_magazine "Отлично! Я в тебе и не сомневался! Заполни анкету, я поставлю штамп и считай, что ты уже работник этого магазина."
                         "Глянув на анкету, вы увидели обыденную бюрократическую форму, куда нужно записать свое имя, адрес, телефон. Озадаченно пожав плечами и взяв с рюкзака ручку, быстрыми движениями была подписана вся информация и поставлена роспись в конце."
                         adm_magazine "А ты достаточно быстро все сделал."
                         "Взяв уже заполненную анкету в руки, мужчина перечитал все и довольно улыбнулся."
                         adm_magazine "Ты принят. Твой рабочий день начинается прямо сейчас."
                         scene black with dissolve
                         $ renpy.pause(1.0, hard=True)
                         scene image "backgrounds/location/magazine/joob_magazine.png" with dissolve
                         "Проведя вас в глубь магазина, ваш новый работодатель начал бегло объяснять суть и задачу вашей работы."
                         hide adm_magazine
                         if help_joob_magazine == 1:
                             guide4 "Ух... Достаточно верный шаг: найти работу! С ней ты точно не будешь иметь проблем с деньгами!"
                             guide10 "Ой... Опять я сказала лишнего! Я же здесь для того, чтобы объяснить тебе механику мини-игры!"
                             guide1 "В общем, смотри! В разных частях экрана будут появляться разные иконки доступных товаров, на которые ты будешь тыкать. Одно нажатие даст тебе дополнительное время и очки победы, за которые ты сможешь чуть позже получить премиальные."
                             guide5 "Все просто, так ведь?"
                             guide2 "Ох... Я забыла упомянуть про навыки! За каждый полностью отработанный день ты будешь получать прибавку к навыку!"
                             guide1 "За каждый уровень навыка ты будешь получать не только прибавку к премиальным, но и небольшие постоянные бусты к атрибутам!"
                             guide1 "Неплохо, да?"
                             guide5 "Хоп, мне пора помогать другим игрокам! Удачи тебе, новоиспеченный работничек!"
                         $ joob = 1
                         jump magazine_game
                     "{color=#000000}Я подумаю насчет вакансии, спасибо.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
                         jump product_magazine
