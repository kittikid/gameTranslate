label ivent_club_occult_npc:
     python:
         name_npc213123 = str(name_npc)+' '+str(fam_npc)
         npc = DynamicCharacter("name_npc213123", color="#CD5C5C", who_outlines=[ (5, "#282828") ], who_font= 'gui/fonts/prototype.ttf', who_drop_shadow=[ (2, 1) ] )
     if gender_npc == 1:
         show image "character/npc/npc_m/[v_npc].png"
     elif gender_npc == 2:
         show image "character/npc/npc_f/[v_npc].png"
     if hour <= 7:
         scene club_occult_v
     elif hour <= 16:
         scene club_occult_ut
     elif hour <= 20:
         scene club_occult_v
     else:
         scene club_occult_v
     if gender_npc == 1:
         npc "Привет... Я хотел бы вступить в ваш клуб. Вы все еще принимаете людей?"
     elif gender_npc == 2:
         npc "Привет... Я хотела бы вступить в ваш клуб. Вы все еще принимаете людей?"
     menu:
         "{color=#000000}Конечно!\n{size=21}{i}0 энергии{/i}{/size}{/color}":
             if gender_npc == 1:
                 npc "Тогда прямо сейчас и приступлю к работе!"
             elif gender_npc == 2:
                 npc "Хе-хе... Спасибо!"
         "{color=#000000}Нет, извини, но клуб полон.\n{size=21}{i}0 энергии{/i}{/size}{/color}":
             if gender_npc == 1:
                 npc "..."
             elif gender_npc == 2:
                 npc "Эээ... Правда? Извини тогда за беспокойство..."
             $ club_npc = 7
             $ eval(npc_id)["club_npc"] = club_npc
     jump club_occult
