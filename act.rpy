init -2 python:
     file_path = "mods/h_patch.txt"
     if renpy.exists(file_path) == True:
         h_patch = True
         hentai_patch_inicial = True
     else:
         h_patch = False
         hentai_patch_inicial = False
image oc_c1 = "character/club/occult/loc/oc_c1.jpg"
image ayano g1 = "character/club/occult/npc/1.png"
image ayano g2 = "character/club/occult/npc/2.png"
image ayano g3 = "character/club/occult/npc/3.png"
image ayano g4 = "character/club/occult/npc/4.png"
image ayano g5 = "character/club/occult/npc/5.png"
image ayano g6 = "character/club/occult/npc/6.png"
image ayano g7 = "character/club/occult/npc/7.png"
image ayano g8 = "character/club/occult/npc/8.png"
image ayano g9 = "character/club/occult/npc/9.png"
image ayano g10 = "character/club/occult/npc/10.png"
image ayano g11 = "character/club/occult/npc/11.png"
image ayano g12 = "character/club/occult/npc/12.png"
image ayano g13 = "character/club/occult/npc/13.png"
image ayano g14 = "character/club/occult/npc/14.png"
image ayano g15 = "character/club/occult/npc/15.png"
image ayano g16 = "character/club/occult/npc/16.png"
image ayano g21 = "character/club/occult/npc/ni/1.png"
image ayano g22 = "character/club/occult/npc/ni/2.png"
image ayano g23 = "character/club/occult/npc/ni/3.png"
image ayano g24 = "character/club/occult/npc/ni/4.png"
image ayano g25 = "character/club/occult/npc/ni/5.png"
image ayano g26 = "character/club/occult/npc/ni/6.png"
image ayano g27 = "character/club/occult/npc/ni/7.png"
image ayano g28 = "character/club/occult/npc/ni/8.png"
image ayano g29 = "character/club/occult/npc/ni/9.png"
image ayano g30 = "character/club/occult/npc/ni/10.png"
image ayano g31 = "character/club/occult/npc/ni/11.png"
image ayano g32 = "character/club/occult/npc/ni/12.png"
image ayano g33 = "character/club/occult/npc/ni/13.png"
image ayano g34 = "character/club/occult/npc/ni/14.png"
image ayano g35 = "character/club/occult/npc/ni/15.png"
image ayano g36 = "character/club/occult/npc/ni/16.png"
image ayano g37 = "character/club/occult/npc/ni/17.png"
image ayano g38 = "character/club/occult/npc/ni/18.png"
image ayano g39 = "character/club/occult/npc/ni/19.png"
image ayano g40 = "character/club/occult/npc/ni/20.png"
image ayano g41 = "character/club/occult/npc/ni/21.png"
image ayano g42 = "character/club/occult/npc/ni/22.png"
image ayano g43 = "character/club/occult/npc/ni/23.png"
image ayano g44 = "character/club/occult/npc/ni/24.png"
image ayano g45 = "character/club/occult/npc/ni/25.png"
image ayano g46 = "character/club/occult/npc/ni/26.png"
image ayano g47 = "character/club/occult/npc/ni/27.png"
image ayano g48 = "character/club/occult/npc/ni/28.png"
image ayano g49 = "character/club/occult/npc/ni/29.png"
image ayano g50 = "character/club/occult/npc/ni/30.png"
image ayano_cosplay g1 = "character/ayano_cosplay/1.png"
image ayano_cosplay g2 = "character/ayano_cosplay/2.png"
image ayano_cosplay g3 = "character/ayano_cosplay/3.png"
image ayano_cosplay g4 = "character/ayano_cosplay/4.png"
image ayano_cosplay g5 = "character/ayano_cosplay/5.png"
image ayano_cosplay g6 = "character/ayano_cosplay/6.png"
image ayano_cosplay g7 = "character/ayano_cosplay/7.png"
image ayano_cosplay g8 = "character/ayano_cosplay/8.png"
image ayano_cosplay g9 = "character/ayano_cosplay/9.png"
image ayano_cosplay g10 = "character/ayano_cosplay/10.png"
image ayano_cosplay g11 = "character/ayano_cosplay/11.png"
image ayano_cosplay g12 = "character/ayano_cosplay/12.png"
image ayano_cosplay g13 = "character/ayano_cosplay/13.png"
image ayano_cosplay g14 = "character/ayano_cosplay/14.png"
image ayano_cosplay g15 = "character/ayano_cosplay/15.png"
image ayano_cosplay g16 = "character/ayano_cosplay/16.png"
image ayano_cosplay g17 = "character/ayano_cosplay/17.png"

image school123 = "backgrounds/school1.jpg"
image club_occult_ut = "character/club/occult/loc/club_ut.jpg"
image club_occult_v = "character/club/occult/loc/club_v.jpg"
image black = "#000000"
label occult_book_guide:
    "Once again, looking around the club room for any interesting things, you saw an old enough book lying safely on the table and literally telling you to take it."
    "When you came a little closer, you noticed a note next to it, which said Ayano, make sure you read it! and a hard to distinguish the name of the find: Basic management of the club.
     ayanogg1 "Heh heh. What are we looking at?"
     show ayano g26 with dissolve
     "Looking back at the sound that sounded nearby, you noticed Ayano standing nearby, staring at you and the book."
     ayanogg1 "Well? What are we looking at with such interest?"
     glgg "That's a stupid enough question, considering I've been looking at your book the whole time."
     show ayano g32
     ayanogg1 "Are you interested in her?"
     glgg "Not exactly. You can say that I was just surprised by the presence of something similar within the walls of our club, but after reading the note, I realized that you were given it either by student advice or someone else who does not want the occult club to be closed".
     show ayano g22
     ayanogg1 "It feels like I've been insulted, but... Anyway, you're right: Yuki, the head of the student council, gave it to me."
     glgg "Have you even read it?"
     show ayano g24
     ayanogg1 "No! Why, if I already know everything."
     show ayano g32
     ayanogg1 "Especially what it says is boring, and I don't want to do boring things!"
     glgg "Whatever you say."
     show ayano g24
     ayanogg1 "Well, now that we're talking about it, don't you want it for yourself?"
     show ayano g36
     ayanogg1 "I was gonna take it to the dusty utility room, where it's like a wastepaper pond, so maybe you'll need it. Maybe you'll find it interesting, I don't know."
     glgg "{i}And then she wonders why the club falls apart under her control...{/i}"
     show ayano g41
     ayanogg1 "What?"
     glgg "I say I'll take this book. I think it'll be much better."
     show ayano g24
     ayanogg1 "Here's the deal. Take it!"
     "Continuing to do her undoubtedly important work, Ayano turned her back on your carcass, no longer paying attention."
     $ book_guide_occult_club = 1
     '{color=578426}THERE IS A NEW ITEM IN YOUR INVENTORY{/color}'
screen guide_book_club_occult:
     modal True
     imagebutton:
         idle 'gui/club_control/guide/guide_idle.png'
         hover 'gui/club_control/guide/guide_hover.png'
         focus_mask True
         action Hide('guide_book_club_occult')
     if page_book == 1:
         imagemap:
             ground 'gui/club_control/guide/guide_str1.png'
             hover 'gui/club_control/guide/guide_str1_hover.png'
             hotspot (1262, 106, 221, 871):
                 action SetVariable('page_book', 2)
     elif page_book == 2:
         imagemap:
             ground 'gui/club_control/guide/guide_str2.png'
             hover 'gui/club_control/guide/guide_str2_hover.png'
             hotspot (436, 101, 197, 879):
                 action SetVariable('page_book', 1)
     else:
         $ page = 1
label ayano_storeroom:
     if hour <= 3:
         scene image "character/club/occult/loc/podsobka_night.jpg":
             size(1920, 1080)
     if hour <= 7:
         scene image "character/club/occult/loc/podsobka_ut.jpg":
             size(1920, 1080)
     elif hour <= 16:
         scene image "character/club/occult/loc/podsobka_ut.jpg":
             size(1920, 1080)
     elif hour <= 20:
         scene image "character/club/occult/loc/podsobka_v.jpg":
             size(1920, 1080)
     else:
         scene image "character/club/occult/loc/podsobka_night.jpg":
             size(1920, 1080)
     if minet_ayano == 2:
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/1_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/2_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/3_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/4_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
             missioner = 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/1_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
             missioner = 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/5_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
             missioner = 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/6_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
             missioner = 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/7_minet.png"
             setattr(store, name_size, name_ik)
             open_number += 1
             missioner = 1
         show ayano_cosplay g2 with dissolve
         ayanogg1 "And you're fast enough..."
         glgg "There's no other way. All the more reason I don't want to lose my life because of your impulsiveness."
         show ayano_cosplay g3
         ayanogg1 "I'm not impulsive!"
         glgg "Whatever you say. Anyway, the only question I have left is... Why did you change?"
         show ayano_cosplay g6
         ayanogg1 "Something told me you were going to ask that..."
         show ayano_cosplay g7
         ayanogg1 "It's gonna be a lot easier for me psychologically... I guess I'm just not ready to do something like that yet, you know... In my usual way..."
         glgg "How... Is your image so innocent that it can't do something like the first stranger?"
         show ayano_cosplay g4
         ayanogg1 "Of course!"
         show ayano_cosplay g3
         ayanogg1 "And I am innocent not only in my image, but in others as well!"
         glgg "Only if physically..."
         "After hitting you on the shoulder, Ayano inflated her lips and continued." with vpunch
         show ayano_cosplay g13
         ayanogg1 "You know, the Cosplers value their images... At least those like me... And... Anyway, it doesn't matter! You came here to make me satisfy you, so sit down somewhere!"
         hide ayano_cosplay
         "Without saying anything else, you covered a strong enough microwave box with a cloth next to it and sat down on the made seat."
         "After unbuttoning the fly and delivering the already standing unit from there, a slightly confused Ayano came across your eyes, that she was already sitting next to him on her knees."
         scene image "mods/h_pictures/CG_ayano/1_minet.png" with Dissolve(.9):
             size (1920, 1080)
         "While staring at your reproductive organ, the girl, with some surprise, drove awkwardly up and down, taking her eyes away from him."
         scene image "mods/h_pictures/CG_ayano/2_minet.png" with Dissolve(.9):
             size (1920, 1080)
         "Continuing to do this kind of exextraction, suddenly your dick trembled for her and made her a little frightened..."
         ayanogg1 "What... What is it? Is it okay?"
         glgg "It would be even better if you finally started doing what you were originally talking about."
         ayanogg1 "А?.. Yes... Okay."
         scene image "mods/h_pictures/CG_ayano/3_minet.png" with Dissolve(.9):
             size (1920, 1080)
         "Ayano finally started to do what you originally agreed to do, and although all her exertions looked pathetic enough, it was a great pleasure for you morally."
         "Well... Physically, it's just the pain and suffering caused by your partner's general lack of sexual skills: he'll bite his head off, he'll stick his tongue in the wrong place, or he'll stick his teeth in a rather sensitive bridle."
         scene image "mods/h_pictures/CG_ayano/4_minet.png" with Dissolve(.9):
             size (1920, 1080)
         "It's almost impossible to keep your dick excited, so you soon had it falling, freeing up a girl's mouth from something so unloved."
         if hour <= 3:
             scene image "character/club/occult/loc/podsobka_night.jpg":
                 size(1920, 1080)
         if hour <= 7:
             scene image "character/club/occult/loc/podsobka_ut.jpg":
                 size(1920, 1080)
         elif hour <= 16:
             scene image "character/club/occult/loc/podsobka_ut.jpg":
                 size(1920, 1080)
         elif hour <= 20:
             scene image "character/club/occult/loc/podsobka_v.jpg":
                 size(1920, 1080)
         else:
             scene image "character/club/occult/loc/podsobka_night.jpg":
                 size(1920, 1080)
         show ayano_cosplay g4 with dissolve
         ayanogg1 "Now, I hope you're satisfied?"
         glgg "If you used your lips and tongue, not just your teeth, you wouldn't have a price."
         show ayano_cosplay g3
         ayanogg1 "You're... You've got to be kidding me!"
         glgg "And that's what the girl who almost ate my own cock tells me..."
         show ayano_cosplay g16
         ayanogg1 "I don't know how to do it, and you're as quiet as a partisan! So I thought you liked it, and in general... Enjoy what you have!"
         glgg "I'm already satisfied that I almost got bitten off."
         show ayano_cosplay g12
         ayanogg1 "That's good. Let's say you liked it!"
         glgg "Okay! Then... You're doing a good blow job, Ayano!"
         show ayano_cosplay g9
         ayanogg1 "A terrible compliment..."
         glgg "Like your blow..."
         show ayano_cosplay g3
         ayanogg1 "I got it! You don't have to say that!"
         glgg "If you say so. Anyway, I gotta go."
         show ayano_cosplay g15
         ayanogg1 "{size=20}{i}Handle...{/size}{/i}"
         glgg "What?"
         show ayano_cosplay g4
         ayanogg1 "Nothing! Get out of here!"
         "Having shrugged your shoulders and lost your still sore spot again, you left the back room and went about your business, leaving your acquaintance dressed in already quite ordinary clothes."
         $ minet_ayano = 3
         $ energy -= 2
         $ minute += 20
     elif minet_ayano == 4:
         menu:
             "{color=#000000}Asking to do it in a casual way.\n{size=21}{i}2 energies\n??? popularity{/i}{/size}{/color}":
                 $ energy -= 2
                 show ayano_cosplay g3 with dissolve
                 ayanogg1 "No!"
                 glgg "And why is that?"
                 show ayano_cosplay g4
                 ayanogg1 "I've already answered that question to you! No and again no! I don't want to spoil my innocent image... Well... Like this..."
                 ayanogg1 "So sit down now and let's have less talk!"
                 jump _otsos_ayano
             "{color=#000000}However, I don't care where, how or what suit I wear.\n{size=21}{i}2 energies{/i}{/size}{/color}":
                 $ energy -= 2
                 show ayano_cosplay g2
                 ayanogg1 "Heh-heh... You came fast enough again! Anyway, let's talk less and sit down!"
                 label _otsos_ayano:
                 hide ayano_cosplay
                 "Sitting in the place you've prepared since last time, you pulled your reproductive organ out, freeing it from the tight shackles of clothing."
                 scene image "mods/h_pictures/CG_ayano/1_minet.png" with Dissolve(.9):
                     size (1920, 1080)
                 "At the same time, Ayano knelt down beside him and began to stare with some curiosity, only a minute later taking him in the hand and starting to move it up and down, and then and then squeezing your unit at the very base."
                 scene image "mods/h_pictures/CG_ayano/3_minet.png" with Dissolve(.9):
                     size (1920, 1080)
                 "Shortly working in this way, the girl soon let go of her dick and took it in her mouth, starting the original business, already moving her head in such a familiar tact."
                 scene image "mods/h_pictures/CG_ayano/4_minet.png" with Dissolve(.9):
                     size (1920, 1080)
                 "Which was a real surprise, your partner began to move much better and the whole act began to cause not only moral but also physical satisfaction, which stopped only occasionally, when she accidentally used her teeth."
                 scene image "mods/h_pictures/CG_ayano/5_minet.png" with Dissolve(.9):
                     size (1920, 1080)
                 "In the end, you soon, unable to hold back, ended up in a girl's mouth, which clearly did not expect such a sharp and quick outcome."
                 scene image "mods/h_pictures/CG_ayano/6_minet.png" with Dissolve(.9):
                     size (1920, 1080)
                 "Having swallowed your seed and licked the machine at the end, she stood on her feet and looked you in the eye."
                 if hour <= 3:
                     scene image "character/club/occult/loc/podsobka_night.jpg":
                         size(1920, 1080)
                 if hour <= 7:
                     scene image "character/club/occult/loc/podsobka_ut.jpg":
                         size(1920, 1080)
                 elif hour <= 16:
                     scene image "character/club/occult/loc/podsobka_ut.jpg":
                         size(1920, 1080)
                 elif hour <= 20:
                     scene image "character/club/occult/loc/podsobka_v.jpg":
                         size(1920, 1080)
                 else:
                     scene image "character/club/occult/loc/podsobka_night.jpg":
                         size(1920, 1080)
                 show ayano_cosplay g13 with dissolve
                 ayanogg1 "I hope you enjoyed it... I tried to do the best I could..."
                 hide ayano_cosplay
                 "After a short talk for a while, you left the back room and went on with your work."
                 $ minet_ayano = 3
                 $ minute += 20
     jump club
label club:
     scene black
     if club == 1:
         jump club_occult
     else:
         "You are not a member of any school club."
         jump check_location
label occult_club_act1:
     if hour <= 16:
         scene image "gui/overlay/mm/main_menu1.png"
     elif hour <= 19:
         scene image "gui/overlay/mm/main_menu2.png"
     elif hour >= 20:
         scene image "gui/overlay/mm/main_menu3.png"
     "As you approached the gates of the already quite ordinary school, you noticed a rather strange movement of other schoolchildren: they went behind the school, not towards the entrance, as always."
     glgg "Perhaps an action, or perhaps some student gathering... Anyway, it could be something interesting..."
     menu:
         "{color=#000000}To go and see what's going on.\n{size=21}{i}3 energies{/i}{/size}{/color}":
             $ energy -= 3
             "With a shrug of your shoulders, you followed a group of schoolboys you didn't know, and within minutes, two minutes, you finally got to where you needed to be."
             $ minute += 2
             scene oc_c1 with dissolve
             glgg "Well, now it's clear. Club gatherings happen every year, which means... It's been a year now?"
             "..."
             ".."
             "."
             glgg "And who did I tell that to anyway? Oh, come on, it doesn't really matter."
             "As you passed through the crowd, you pushed the disciples that were in your way to finally get out of this unfortunate trap until you noticed a rather funny situation."
             show ayano g3
             ayanogg "How come you don't want to join our club?! Oh, no way! Wait, maybe you made a mistake!"
             "A girl with obscure toys in her hands tried to catch up with a guy already running away from her, screaming at him..."
             beg_p "Get off me, you ride!"
             ayanogg "No, stop it! This is all a big mistake!"
             "In the end, it couldn't last, and the girl fell over an empty bottle, which someone seemed to have thrown away carelessly before the whole situation." with vpunch
             show ayano g7
             ayanogg "Ouch... Who even throws bottles in places like this?! That's illegal, by the way! You'll get a fine!"
             "It seems that the crowd has understood that standing next to this girl is the most dangerous not only for life, but also for morals, so they left her alone to rub a sick knee."
             show ayano g9
             "Finally on her feet, she took a hard sigh and walked back to her tent where she gave out flyers inviting you to the club, but that was until she noticed your curious person."
             show ayano g8
             stop music fadeout 1
             $ renpy.pause(1.0, hard=True)
             queue music [ "music/6.mp3" ]
             glgg "I don't like it..."
             "As soon as your eyes crossed, she literally started running to you holding her two toys."
             glgg "And now I don't like it any more..."
             menu:
                 "{color=#000000}Escape, following the example of that guy.\n{size=21}{i}2 energies{/i}{/size}\n{size=21}{i}[stats_agility_gg_info]/30 dexterity{/i}{/size}{/color}":
                     $ energy -= 2
                     "As soon as you realised you had to get into a fight, you turned in the opposite direction and accelerated, pushing all the passers-by in your way."
                     show ayano g3
                     ayanogg "WAIT FOR ME! I HAVE SOMETHING TO OFFER YOU! IT'S AN OFFER YOU CAN'T REFUSE!"
                     "By ignoring her words, you accelerated even more. Literally jumping any obstacles, but in the end, everything can come to an end... Failing to calculate your strength, you jumped an obstacle that stood in front of you."
                     scene school123 with dissolve
                     if stats_agility_gg_info >= 30:
                         queue music [ "music/8.mp3", "music/2.mp3", "music/5.mp3" ]
                         "And yet they didn't stumble as you expected, and ran on. Wiping sweat off your face, you breathed heavily and looked behind your back. Making sure the girl had fallen behind you, you sighed lightly and regained your lost breath."
                         menu:
                             "{color=#000000}Could this be a mistake?\n{size=21}{i}2 energies{/i}{/size}{/color}":
                                 $ energy -2
                                 glgg "Even though it's a silly enough thought, it was a bit reckless. I better get back to that girl."
                             "{color=#000000}Get the hell out of this crazy...\n{size=21}{i}0 energy{/i}{/size}{/color}":
                                 "After scolding yourself, you put bad thoughts out of your mind and went about your business."
                                 $ occult_club = 0
                                 jump school
                     else:
                         "And yet luck is not on your side today. When you jumped the obstacle, you twisted your leg and fell, spreading the weight wrongly." with vpunch
                         stop music fadeout 1
                         $ renpy.pause(1.0, hard=True)
                         queue music [ "music/8.mp3", "music/2.mp3", "music/5.mp3" ]
                         glgg "Why am I so unlucky today?!"
                         show ayano g3
                         ayanogg "Hey, are you all right?"
                         "Even though the girl asked the question without any evil intent, it all sounded... Angry and fierce? Perhaps because of her face, or perhaps..."
                         show ayano g2
                         ayanogg "Sorry, stupid, I didn't mean to scare you! Are you all right?"
                         glgg "..."
                         "It's her prerogative to confuse my thoughts when I'm trying to make something clear?!"
                         show ayano g14
                         ayanogg "Don't shut up! Say something!"
                         glgg "So that I can communicate normally with you, tell me, first of all, why do you carry these two toys with you, and secondly, why are you wearing out of uniform?"
                         "Although the second one could be called a common nag, but still the interest takes its toll... On your feet, you kept your eyes on the girl. It's not enough what she'll do."
                         show ayano g10
                         ayanogg "So you're all right..."
                 "{color=#000000}Wait till she gets there and says what she wants.\n{size=21}{i}0 energy{/i}{/size}{/color}":
                     stop music fadeout 1
                     $ renpy.pause(1.0, hard=True)
                     queue music [ "music/5.mp3", "music/2.mp3" ]
                     glgg "Did you want something?"
             show ayano g8
             "I don't like that face..."
             ayanogg "Do you want to join the occult club?" with vpunch
             "Her words are like a blow... Weak, but still a blow."
             glgg "DO WE HAVE AN OCCULT CLUB?" with vpunch
             show ayano g3
             "It seems that for her, my words were as shocking as hers for me. And what's her problem?"
             ayanogg "No, but it will! I only need one person to start the club!"
             glgg "No, don't even ask! I'm not joining your club! I value my health more than all this trouble!"
             show ayano g15
             $ renpy.pause(1.0, hard=True)
             show ayano g14
             "She's about to cry..."
             show ayano g16
             menu:
                 "{color=#000000}Join the club\n{size=21}{i}0 energy{/i}{/size}{/color}":
                     glgg "Okay, I did, but then put those away... Toys?"
                     show ayano g8
                     ayanogg "That's great! Get the questionnaire!"
                     "You already wanted to object and refuse to join the club, but your zeal was interrupted by the continuation of the girl's words and the leaflet in her hand that you took from the machine."
                     show ayano g8
                     ayanogg "It's my own fault for agreeing to join the club. It's too late to take it back!"
                     hide ayano
                     "Without letting you do what you wanted two minutes ago, the girl left you with a flyer in her hand."
                     "{color=#BC8F8F}{b}You have a new item{/b}{/color}"
                     "{color=#BC8F8F}{b}You have the opportunity to join the occult club...{/b}{/color}"
                     $ occult_club = 2
                     $ ancete = 1
                     $ ancete_z = 0
                     glgg "Looks like right now I've been fooled and knocked over... And what am I supposed to do with that?"
                     jump school
                 "{color=#000000}Not today.\n{size=21}{i}0 energy{/i}{/size}{/color}":
                     "Looking at it and weighing the pros and cons, you decided you didn't want it. Leaving the unknown girl alone, you left quickly."
                     $ occult_club = 0
                     jump school
         "{color=#000000}Do I need it?\n{size=21}{i}0 energy{/i}{/size}{/color}":
             "After taking a hard breath, you headed for the entrance to the school. You can always find the adventure of the fifth point, but the time for that..."
             $ occult_club = 0
             jump school
label ayano_TC:
     $ gg == 1000
     scene image "backgrounds/location/shopping_center/shopping_center_v.png"
     "As you walked around the mall, you noticed at the edge of your eye a number of choppers that apparently decided to have their next festival here."
     'Some of them were shouting out obscure phrases that only an avid geek can understand, and were playing with their hands some obscure signs.'
     'Others, based on their female gender, tried to use other signs, putting two fingers to their face every now and then. Oddly enough, people liked it. He must have been guided by the rule, "The more unusual, the more interesting", but...'
     "The real surprise for you was the presence of your friend in this crowd - it's Ayano! Without waiting to see her here in a place like this, you came closer to the performance and began to follow the act with much more attention."
     show ayano_cosplay g3 with dissolve
     ayanogg1 "May the heavens burst before my majesty, may Myrtle descend upon our mortal land!"
     hide ayano_cosplay
     "For a long time, shouting out such phrases, reproducing various absurd movements either from films or from some animation, Ayano greedily examined the crowd, realizing that some views are precisely focused on her, which, apparently, made her do such things."
     'As you watched it for a while longer, you began to notice that the crowd was finally beginning to dissolve, with only a few of the most patient geeks left and a few curious newcomers.
     'Soon, strangely enough, the choppers began to diverge from the understanding that there was no longer an audience or the fatigue of the process - this, you might say, and made your acquaintance turn in your direction.
     "She began to mumble, mumble with surprise, but soon she continued with renewed vigour, abstracting from the embarrassing situation."
     show ayano_cosplay g2 with dissolve
     ayanogg1 "May the grace of heaven come, may the messengers of Myrtle save us..."
     hide ayano_cosplay
     'Having watched such an event for some more time, you began to realize that it can last a very long time, and time is not rubber, and just standing and kneeling is not the best option.'
     "After taking a hard breath, you began to leave the place you were used to underneath the same strange movements of the Cosplers."
     ayanogg1 "[player_name], wait for!"
     "Turned towards the sound of the sound, you saw a cosplayer you knew, who you had recently drilled with your eyes."
     "She quickly enough overcame the distance before you with her far-fetched run and, greedily swallowed air, literally jumped on you with her arms, only a minute later letting go of your skinny little carcass." with vpunch
     show ayano_cosplay g1 with dissolve
     ayanogg1 "I didn't expect to see you here... How often do you walk around the mall like that?"
     glgg "Well, from what I saw here, not as often as you think."
     show ayano_cosplay g10
     ayanogg1 "You knew I wanted to attend such an event a long time ago! Don't pretend! You must have come to support me, even though it was my first time and I never told you about it!"
     glgg "I'll probably disappoint you, but... I was just walking by and I saw a crowd of people and you in it. No more."
     "Clearly disappointed with this fact, the girl exhaled hard, puffed up her lips, but a second later she still calmed down, not letting her emotions go."
     show ayano_cosplay g11
     ayanogg1 "Fine! Anyway, I'm free, and you have to go for a walk with me!"
     glgg "You know, I have things to do..."
     show ayano_cosplay g3
     ayanogg1 "AND YOU MUST WALK WITH ME!"
     glgg "But on the other hand, there aren't many, but... Don't tell me you're gonna go in there..."
     show ayano_cosplay g4
     ayanogg1 "Is there something you don't like?!"
     glgg "You'll be looked at like a fool in that lush dress... Not enough of that, what's on your head? Overlapping hair?"
     show ayano_cosplay g12
     ayanogg1 "And last time you didn't ask me that! Are you finally interested in me as a girl?"
     glgg "Not really... It's just that last time you met Gagarin in person. I didn't really want to distract you from..."
     show ayano_cosplay g3
     ayanogg1 "Don't go on! Your jokes are immoral!"
     glgg "Not really... It wasn't me who finally fell, hitting the back of the head. You're lucky you didn't get hurt at all."
     show ayano_cosplay g4
     ayanogg1 "..."
     glgg "What?"
     show ayano_cosplay g10
     ayanogg1 "Never mind. I'm just thinking about how hard it would be to hit you."
     glgg "I certainly wouldn't mind if you didn't hit me at all."
     show ayano_cosplay g13
     ayanogg1 "Whatever you say."
     show ayano_cosplay g1
     ayanogg1 "We have to go anyway!"
     glgg "I don't even like it here..."
     hide ayano_cosplay
     "Without letting you talk, the girl grabbed your hand, headed for the exit of the shopping center."
     scene black
     pause(1.0)
     scene image "backgrounds/location/park/2.png"
     "And... What you certainly couldn't expect is that you were taken to the park. Half an hour later, with Ayano's quick pace and muttering, you made it to your destination, and both went to the nearest shop."
     show ayano_cosplay g1
     ayanogg1 "Good weather today, huh? Still, the weather on the Internet was wrong. They said it was going to rain, and now there's no hint of it..."
     glgg "Well, whatever they say, you can't draw premature conclusions. It's common practice that anything can happen."
     show ayano_cosplay g14
     ayanogg1 "I agree with you, but I think it's better to always believe in a good way!"
     glgg "To hear from you and to hear this sentence-building... You're not sick?"
     show ayano_cosplay g5
     ayanogg1 "Did you just call me stupid?"
     glgg "Well... More like a girl who can only use such words when she hears them from someone..."
     show ayano_cosplay g4
     ayanogg1 "..."
     show ayano_cosplay g3
     ayanogg1 "You are... You're bad!"
     glgg "And that's why you asked me out on a date to the park. Very much like the average girl."
     show ayano_cosplay g5
     ayanogg1 "Get off! I called you to the park because you're my only friend and I'm just bored! No more!"
     show ayano_cosplay g3
     ayanogg1 "And anyway... You better tell me what you think about what you saw at the mall. Did you like it?"
     menu:
         "{color=#000000}I'm not a special fan of ladies dressed up in all sorts of costumes.\n{size=21}{i}14 energies{/i}{/size}{/color}":
             show ayano_cosplay g15
             ayanogg1 "..."
             glgg "What is it? "
             ayanogg1 "I... I just didn't expect you to say that... Never mind. "
             glgg "Eh? Well, okay..."
             "After sitting in silence for a few more minutes, you began to notice that it began to drizzle, as the recent weather forecast said."
             glgg "Is it me, or is it really drizzling? "
             "Only after hearing your phrase, Ayano looked at the thickening clouds in the sky and caught a few drops of water with her face that made her turn again in your direction. "
             show ayano_cosplay g7
             ayanogg1 "Really... Well, shall we go home?"
             glgg "You're not offended, are you?"
             show ayano_cosplay g15
             ayanogg1 "Don't worry... It's just... Never mind..."
             "Rising from the bench, the girl headed in an unknown direction, leaving you alone to consider her retreating figure on the horizon."
             $ hour += 3
             $ energy -= 14
             $ ayano_TC = 1
             $ ayano_contact -= 25
             $ ayano_trust -= 40
             jump park1
         "{color=#000000}Well, that sounds like a great show to me.\n{size=21}{i}19 energies{/i}{/size}{/color}":
             $ energy -= 19
             show ayano_cosplay g7
             ayanogg1 "Do you... Do you really think so?"
             glgg "Well... There's not much point in lying to me here.."
             show ayano_cosplay g1
             ayanogg1 "Still, you're sweet..."
             glgg "What are you talking about?"
             show ayano_cosplay g7
             ayanogg1 "Well... I thought a lot about what happened between us, and I noticed that you're very good to me... You talk all the time, sometimes you're gentle, but most importantly for me..."
             show ayano_cosplay g15
             ayanogg1 "You support me.
             glgg "Why are you even talking about this?"
             ayanogg1 "You support me even in such trivial things... It would seem that in this cosplay there's such an ordinary costume, but..."
             ayanogg1 "But even here you're on my side... And you know... I really appreciate it and I really hope you keep doing the same... I appreciate it."
             glgg "I'm glad you say that, of course, but why talk like that if I'm just doing what I want?"
             show ayano_cosplay g1
             ayanogg1 "That's why I'm very pleased, I appreciate it: you're not doing everything for me for some reason, but..."
             glgg "Are you saying that my actions have no selfish purposes?"
             show ayano_cosplay g7
             ayanogg1 "Exactly."
             glgg "Perhaps it is..."
             hide ayano_cosplay
             "Silence. The oppressive silence - that's what haunted your dialogue after the soulful sayings of the girl that embarrassedly stared at the dirt track. Having already lost hope of continuing the dialogue, you felt that something dripped on you... Like rain?"
             glgg "Is it me, or is it starting to drizzle?"
             "Only after hearing your phrase, Ayano looked at the thickening clouds in the sky and caught a few drops of water with her face that made her turn again in your direction. "
             show ayano_cosplay g3 with dissolve
             ayanogg1 "It's not true! It seems to you!"
             glgg "You know, you're dripping a little bit of water now, saying otherwise..."
             show ayano_cosplay g4
             ayanogg1 "..."
             glgg "So... Go home?"
             hide ayano_cosplay
             "Disappointedly waving her head at you as a sign of consent, the girl began to look at the floor, apparently very upset by the fact that you say goodbye, but..."
             "Suddenly, she heard a rather strange sentence that literally lifted her mood from the bottom."
             show ayano_cosplay g1 with dissolve
             ayanogg1 "Would you like to come over to my house?"
             glgg "What?"
             show ayano_cosplay g11
             ayanogg1 "Well... Home. To my place. If we can't get a date with you, at least we can, but we'll spend time together."
             menu:
                 "{color=#000000}Why wouldn't I?\n{size=21}{i}20 powers{/i}{/size}{/color}":
                     $ energy -= 20
                     show ayano_cosplay g7
                     ayanogg1 "What's that? Are you serious?"
                     glgg "Well, you invited me... What's the problem?"
                     show ayano_cosplay g1
                     "Waving your head again, but in the exact opposite sense, the girl smiled nicely at you and looked into your eyes."
                     ayanogg1 "No. Nothing. I just... Glad? I don't know how to explain this feeling..."
                     show screen Rain with dissolve
                     "Talking to each other, content with every moment you've spent together, you haven't noticed how the usual little drizzling rain has turned everything into a literal downpour."
                     show ayano_cosplay g12
                     ayanogg1 "Heh-heh... Now we're definitely gonna get sick..."
                     hide ayano_cosplay
                     "Having taken your hand again, but for the good of a completely different purpose, Ayano, with the help of a fast enough run, headed towards her house, dragging your carcass after herself."
                     scene image "backgrounds/location/street.jpg" with dissolve:
                         size(1920, 1080)
                     "Running down a completely empty street, you come across a rather interesting fact: the girl started running slower and slower, you can see, because of sewing her dress, which absorbed all the moisture, but ..."
                     "You're in luck this time. As it turned out, her house was near the park, which is why you got to your destination fast enough."
                     hide screen Rain with dissolve
                     scene image "backgrounds/location/home_ayano.jpg" with dissolve:
                         size(1920, 1080)
                     "At a very fast pace, after opening the front door, your companion ran into the apartment with you and took off her shoes, quickly headed for the bathroom, leaving you at the doorstep."
                     glgg "Hospitable..."
                     "Just by saying that, a towel from Ayano flew in you, that just came out of the bathroom, drilled you with a cruel look and said something like, you'll sort it out now if you don't like it! after coming back in."
                     glgg "Really impulsive... Joyful, sad, angry..."
                     'After taking a hard sigh, you took off your shoes while wiping your face and hair wet from the rain. Falling fifth point on the first empty nightstand at the doorstep, you continued to "dry", paying little attention to anything.'
                     "In the end, realizing that this is the maximum that can be achieved, already a wet towel flew to the floor, and you began to wait until the landlady of the apartment leaves the bath to wash yourself under a hot shower."
                     glgg "Yeah, well... I'd be sick now for my happiness."
                     "Waiting for a few more minutes, the long-awaited sound of the tickling sound of the bath from which Ayano came out in her nightie, which surprised her eyes at you."
                     ayanogg1 "Why aren't you undressed yet? You'll get so sick, you fool!"
                     glgg "Thank you, of course, for the excitement, but you're the one who took the bathroom long enough. So if I get sick, you'll have to nurse me for a long time."
                     ayanogg1 "Boo-boo-boo..."
                     "By stepping away from the bathroom door, the girl gave you the opportunity to go in there, which you did."
                     "Quickly taking off your clothes and hanging them on some source of heat, you turned on a hot shower, almost boiling, and began washing the body, which was quite chilled during the cold and wet street."
                     "Standing so under hot water for another 20-30 minutes, you hoped your clothes were finally dry, so when you turned off the water, you touched the still wet cloth."
                     glgg "Well... Don't walk naked after all."
                     "After wearing wet clothes, you corrected it and left the bathroom, heading towards the bedroom where Ayano was."
                     stop music
                     python:
                         name_size = 'name_size'+str(open_number)
                         name_ik = "character/ayano_cosplay/CG/3.png"
                         setattr(store, name_size, name_ik)
                         open_number += 1
                         renpy.music.queue('mods/rain/sounds/rain_window.mp3', channel='sound', fadein = 5, loop = True)
                         renpy.music.queue('music/7.mp3', channel='music', fadein = 5, loop = True)
                     scene image "character/ayano_cosplay/CG/3.png" with dissolve:
                         size(1920, 1080)
                     "Quite quickly, having calculated the location of it, you opened the door and noticed that she was lying on the bed with some rag on her forehead, and when you came closer, you noticed that her gaze was directed at the window, at the street, where it was dark enough, but the rain was still pouring like a bucket."
                     python:
                         name_size = 'name_size'+str(open_number)
                         name_ik = "character/ayano_cosplay/CG/3.png"
                         setattr(store, name_size, name_ik)
                         open_number += 1
                     scene image "character/ayano_cosplay/CG/3.png" with dissolve:
                         size(1920, 1080)
                     "Translating the look at you, she was a little surprised that you were wearing wet clothes, but afterwards, it seemed to her that there was no friend."
                     glgg "And why did you lie down?"
                     ayanogg1 "..."
                     glgg "Well?"
                     ayanogg1 "Heh heh... I think I'm a little sick and I'm chilly..."
                     "Not knowing how to react, you took the first chair in your hand and placed it next to the bed, sitting on it and crossed your arms at your chest. "
                     glgg "About how... What shall we do?"
                     python:
                         name_size = 'name_size'+str(open_number)
                         name_ik = "character/ayano_cosplay/CG/2.png"
                         setattr(store, name_size, name_ik)
                         open_number += 1
                     python:
                         name_size = 'name_size'+str(open_number)
                         name_ik = "character/ayano_cosplay/CG/2.png"
                         setattr(store, name_size, name_ik)
                         open_number += 1
                     scene image "character/ayano_cosplay/CG/2.png" with dissolve:
                         size(1920, 1080)
                     ayanogg1 "I want to spend time with you, but this is unexpected... In such a short time I got sick... I may have caught a cold before and now... Well... It's manifested... If you want, you can go home. There's an umbrella on the doorstep..."
                     menu:
                         "{color=#000000}I guess I better really go. There's nothing I can do for sure. \n{size=21}{i}0 energy{/i}{/size}{/color}":
                             scene image "character/ayano_cosplay/CG/1.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "I understand... Good luck. Don't get sick like me."
                             scene image "character/ayano_cosplay/CG/3.png" with dissolve:
                                 size(1920, 1080)
                             "Clearly sullen, the girl continued to look out the window without even seeing you through as you left her room."
                             stop music
                             stop sound
                             queue music [ "music/8.mp3", "music/2.mp3", "music/5.mp3" ]
                             $ hour += 5
                             $ ayano_TC = 1
                             $ ayano_contact += 25
                             $ ayano_trust += 30
                             $ gg = -1
                             call screen maps
                         "{color=#000000}I'll sit with you for a while and see. Maybe when it's raining, I'll go back to домой\n{size=21}{i} {i}0 energy{/i}{/size}{/color}":
                             python:
                                 renpy.music.queue('music/8.mp3', channel='music', fadein = 5, loop = True)
                             scene image "character/ayano_cosplay/CG/1.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "I appreciate it, but... Now it's dark enough. How are you going to get home?"
                             glgg "It's not a big deal right now. Let's talk about something else."
                             ayanogg1 "Like what?"
                             glgg "For example, about the Cosplay. Why do you love it so much?"
                             scene image "character/ayano_cosplay/CG/3.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "I don't think I chose this theme on purpose... I don't really love him. It's just that sometimes it feels good to be needed, to be loved, to be somebody else, just for a little while..."
                             glgg "Is it so bad for you if you're trying to... Like this?"
                             ayanogg1 "Well, it's like looking at this situation from the outside, so... I don't know how to answer that... I wasn't much of a complainer in the family, I was the firstborn, and then my brother was born..."
                             ayanogg1 "And in fact, even before I was born, it was bad, and now... Now it's just terrible. My brother started fighting all the time, more and more he started messing with bad companies, and then..."
                             ayanogg1 "Next, my parents were just spilling their anger on me. I don't know why it happened, but... It happened."
                             glgg "I don't know what to say to that... I'm sorry?"
                             ayanogg1 "It's hard enough, you know. "
                             glgg "I know, but you better tell me why you're not telling me the details."
                             scene image "character/ayano_cosplay/CG/1.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "What are you talking about?"
                             glgg "The story of the family has certainly answered many questions, but not the most important at the moment... A person can't get sick in 30 minutes, so the question and the assumption at the same time: if you were sick before all this, why did you go to the mall at all?"
                             scene image "character/ayano_cosplay/CG/3.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "Can't hide anything from you... And who are you so curious about?"
                             ayanogg1 "I didn't want to put it off any longer. I used to... Although before... Even now I keep putting things off, telling myself it's normal."
                             ayanogg1 "It's the same thing once in a while: I want to go to the Cosplay Festival, finally perform, but I'm afraid of the audience, being in some kind of image... Well, what I did was a protest. A protest to my fears."
                             glgg "After that, you call me weird. "A battered little girl with a clear psychological trauma calls me weird."
                             scene image "character/ayano_cosplay/CG/1.png" with dissolve:
                                 size(1920, 1080)
                             ayanogg1 "I'm sorry I'm not really who I am at school... But I think you should know that. Sooner or later."
                             "After talking to the girl for a while, you began to notice that she was gradually falling asleep, speaking more and more abruptly."
                             scene image "character/ayano_cosplay/CG/2.png" with dissolve:
                                 size(1920, 1080)
                             "Waiting for her to fall asleep, you started looking at her sleeping face, digesting the information."
                             "And while you didn't seem to care at all about her story, they did leave a small mark. "A trace of pity, a certain amount of joy for Ayano's success and, of course, misunderstanding."
                             "Looking at the window and watching the drops knocking at it, you fell asleep at the end, barely realizing it."
                             stop sound
                             stop music
                             scene black
                             pause(3.0)
                             queue music [ "music/2.mp3", "music/5.mp3", "music/8.mp3" ]
                             ayanogg1 "Sleepy, get up..."
                             scene image "backgrounds/location/home_ayano1.jpg" with dissolve:
                                 size(1920, 1080)
                             "Feeling a strong push in your carcass, you began to slowly open your eyes. The light was shining in your eyes, and they seemed to be covered in veil, but in the end you opened them completely, taking note of your acquaintance, that recently with a sad look told you stories."
                             show ayano g42 with dissolve
                             ayanogg1 "Woke up at last... How did you sleep in the chair?"
                             glgg "Okay, great. If you hadn't woken me up, I would have remembered this moment for a long time."
                             "Tired of stretching, a loud and pleasant crunch was heard from your back. "
                             show ayano g39
                             ayanogg1 "It can be heard..."
                             show ayano g32
                             ayanogg1 "Listen, did you fall asleep somehow?"
                             glgg "Closed his eyes and fell asleep. I'm more interested in the reason for your cheerfulness. Aren't you sick? "
                             show ayano g24
                             ayanogg1 "I'm sick. But when you sleep so well... It's like no temperature!"
                             "When you looked around the room, you noticed the usual lavish dress lying around... With the wig? "
                             glgg "The question is... How do you put a wig on yourself if you have such long hair? "
                             show ayano g26
                             ayanogg1 "A strange question for just waking up... I wish you a good morning."
                             glgg "I wish you, when you answer the question. "
                             show ayano g24
                             ayanogg1 "Boo-boo-boo, how evil we are."
                             show ayano g32
                             ayanogg1 "Well, the wig is easy enough to put on, it's expensive, but... The top size increases a lot, I admit."
                             glgg "Good morning."
                             show ayano g27
                             ayanogg1 "Finally said... Listen, aren't you going somewhere now?"
                             glgg "Are you chasing me away?"
                             show ayano g24
                             ayanogg1 "No, but if you're so anxious to meet my parents, who'll be here any minute, then go ahead!"
                             glgg "..."
                             show ayano g26
                             ayanogg1 "М?"
                             "If you didn't want to listen to Ayano anymore, you quickly got together and went to the front door under the girl's snide laughter."
                             glgg "It was nice spending time with you, Ayano, but I have to go. Business is called and, as they say, guests are good and houses are better."
                             "When you opened the front door and left the girl's apartment, you took a quick step back home."
                             $ hour = 10
                             $ days += 1
                             $ ayano_TC = 1
                             $ ayano_contact += 35
                             $ ayano_trust += 40
                             $ gg = -1
                             call screen maps
                 "{color=#000000}Sorry, but there's a lot to do today. We had a good time, of course, but that's it. \n{size=21}{i}0 energy{/i}{/size}{/color}":
                     hide ayano_cosplay
                     "By nodding you again, the girl weaved herself into an unknown direction. No arguments, no nothing. She just walked away, and only her distant silhouette, disappearing more and more from minute to minute, was visible to you."
                     $ hour += 3
                     $ ayano_TC = 1
                     $ ayano_contact += 15
                     $ ayano_trust += 20
                     jump park1
label ayano_ivent:
     $ gg == 1000
     $ minute += renpy.random.randint(26, 35)
     if ayano_ivent == 1:
         "When you were doing your job, you were as focused and focused as possible, which is why you didn't pay any attention to what was going on around you, but for nothing."
         "At that time, in the other corner of the room, something was happening that you couldn't have guessed: Ayano was quietly changing her clothes, apparently already accustomed to the fact that you don't look at her particularly."
         "Having completed her transformation, the girl ran up to you and closed your eyes with her hands."
         scene black with dissolve
         ayanogg1 "Do you think I'm cute today?"
         menu:
             "{color=#000000} No idea have\n{size=21}{i}0 energy{/i}{/size}{/color}":
                 glgg "I have no idea."
                 ayanogg1 "Don't be a beech and answer the question!"
                 glgg "I already told you, I have no idea."
                 if hour <= 16:
                     scene club_occult_ut with dissolve
                 elif hour <= 20:
                     scene club_occult_v with dissolve
                 else:
                     scene club_occult_v with dissolve
                 "Clearly disappointed with your answer, the girl took her hands off your eyes and took a step back to give you room for your eyes. When you turned around, you saw Ayano in the botforts and some gothic dress... And, strangely enough, her hair became much longer, so white on top of that."
                 show ayano_cosplay g1
                 glgg "Why did you put this on yourself?"
                 show ayano_cosplay g2
                 ayanogg1 "I love the Cosplay, and now I'm as my favorite character!"
                 glgg "Beautiful. I thought we had an occult club, but it's actually a cosplay club."
                 show ayano_cosplay g3
                 ayanogg1 "Don't be so mean!"
                 "When you took a hard breath, you noticed a tin can at Ayano's feet. When you decided you should warn her, you pointed at her with your finger."
                 glgg "This is good, of course, but you should be careful."
                 hide ayano_cosplay
                 python:
                     name_size = 'name_size'+str(open_number)
                     name_ik = "mods/h_pictures/CG_ayano/1.png"
                     setattr(store, name_size, name_ik)
                     open_number += 1
                 scene image "mods/h_pictures/CG_ayano/1.png":
                     size(1920, 1080)
                 "Not knowing what you were talking about at once, the girl unsuccessfully moved, which is why she fell to her fifth point, hitting her head. You can not, of course, rejoice at the failures of other people, but that's what pleased you at least the view that was open to your eyes: blue panties in a white stripe were quite fit for children's character Ayano.
             "{color=#000000} Quite possibly\n{size=21}{i}0 energy{/i}{/size}{/color}":
                 glgg "She may be cute, but I can't say for sure, because, as you know, my eyes are covered with your palms."
                 ayanogg1 "Right, right, right!"
                 if hour <= 16:
                     scene club_occult_ut with dissolve
                 elif hour <= 20:
                     scene club_occult_v with dissolve
                 "Having clearly rejoiced at your answer, the girl took her palms out of your eyes and moved one step away to give your eyes room for evaluation. When she turned around, you were a little pleased with her outfit: instead of a casual blouse and skirt, she was wearing a gothic dress and botforts."
                 "Apparently, she mapped out some anime character in a medieval setting."
                 show ayano_cosplay g1
                 ayanogg1 "What do you think?"
                 glgg "I think it suits you, Ayano."
                 show ayano_cosplay g2
                 ayanogg1 "Thank you! You're so cute!"
                 python:
                     name_size = 'name_size'+str(open_number)
                     name_ik = "mods/h_pictures/CG_ayano/1.png"
                     setattr(store, name_size, name_ik)
                     open_number += 1
                 scene image "mods/h_pictures/CG_ayano/1.png":
                     size(1920, 1080)
                 $ ayano_contact += 1
                 "As she was about to turn her back on you, the girl didn't notice the tin can lying on the floor, which is why she fell fifth to the floor, hitting her head and opening your eyes a beautiful view of her blue panties in a white stripe." with vpunch

         "Rubbing the back of her head, Ayano didn't even notice you staring at her underwear. Looking vaguely around, the girl seems to have lost touch with reality, which was on one side of your hand and on the other quite exciting..."
         ayanogg1 "Uh... What happened?"
         "Ayano's vague gaze changed into a more comprehensible one as he slowly came to his senses. It seems that soon she will fully recover, and this beautiful painting will be closed to you."
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/2.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/3.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         python:
             name_size = 'name_size'+str(open_number)
             name_ik = "mods/h_pictures/CG_ayano/4.png"
             setattr(store, name_size, name_ik)
             open_number += 1
         scene image "mods/h_pictures/CG_ayano/2.png":
             size(1920, 1080)
         glgg "Houston, we have a ship wreck..."
         "When the girl heard your words, she tried to find you with a look, which was quite unsuccessful in her position. In the end, strong dizziness from impact is no joke. After sitting on her butt for a few more minutes, the girl finally regained consciousness and noticed that her panties were open to you."
         "Quickly stood up and shaken off, she looked at you."
         if hour <= 16:
             scene club_occult_ut with dissolve
         elif hour <= 20:
             scene club_occult_v with dissolve
         else:
             scene club_occult_v with dissolve
         show ayano_cosplay g4
         ayanogg1 "Did you see that, pervert?"
         menu:
             "{color=#000000}Quite\n{size=21}{i}0 energy{/i}{/size}{/color}."
                 glgg "Yeah. I guess I won't be seeing these kinds again soon, so could you please fall down again?"
                 show ayano_cosplay g5
                 ayanogg1 "Idiot! Idiot! Idiot!"
                 "After hearing a few more synonymous words from her mouth, you began to realize that she wasn't going to shut her mouth, so you decided to take some pretty sharp and rough action."
                 glgg "Why are you so mad at me? The view's not bad, I liked the show, and I learned a lot about myself."
                 ayanogg1 "Jackass!"
                 "{color=#BC8F8F}{b} The relationship and trust level has deteriorated!"
                 $ ayano_contact -= 10
                 $ ayano_trust -= 7
                 $ depravity_ayano += 2
             "{color=#000000} Are you all right? \n{size=21}{i}0 energy{/i}{/size}{/color}."
                 glgg "Are you all right?"
                 show ayano_cosplay g8
                 ayanogg1 "I suppose so... But the dizziness hasn't completely gone away."
                 "Apparently forgetting that you've been quietly enjoying the sight of her panties lately, the girl quietly started talking to you."
                 glgg "Maybe you should go to the clinic. In the end, a blow to the back of the head would have given you a concussion."
                 show ayano_cosplay g7
                 ayanogg1 "No... I guess it's okay. Thank you for your concern."
                 "Sitting next to you, the girl rubbed her neck. And how did she not rub it into the holes today?"
                 glgg "Not nauseous? No noise in your ears or diplopia?"
                 show ayano_cosplay g6
                 ayanogg1 "I don't even know these words about the third one, but the first two aren't felt yet..."
                 glgg "I suppose you're all right then. It's just a bruise. Although I'm not a doctor, I don't know for sure."
                 show ayano_cosplay g9
                 ayanogg1 "Thank you for worrying..."
                 menu:
                     "{color=#000000} Not for what\n{size=21}{i}0 energy{/i}{/size}{/color}."
                         glgg "You're welcome. After all, I should be worried about my soccer player, I guess..."
                         show ayano_cosplay g2
                         ayanogg1 "You're cute today..."
                         glgg "Quite possibly, I don't deny it."
                         hide ayano_cosplay
                         "After continuing with your business, you left Ayano alone to rub the sick back of the head."
                         "{color=#BC8F8F}{b} The level of relationship and trust has improved!"
                         $ ayano_contact += 8
                         $ ayano_trust += 2
                         $ depravity_ayano += 1
                     "{color=#000000}I'm not worried. I just don't want you puking on my pants. \n{size=21}{i}0 energy{/i}{/size}{/color}"
                         glgg "I'm not worried, I feel sorry for my pants. I don't want them to vomit."
                         show ayano_cosplay g6
                         ayanogg1 "You're so cute today..."
                         glgg "I suppose you've got all the doors open at the infirmary if you think it's nice. Maybe an ambulance will call and find a couple more diseases."
                         show ayano_cosplay g7
                         ayanogg1 "You'll say, I know you were worried about me."
                         glgg "I was worried about my pants, not you. I think it's a big difference."
                         hide ayano_cosplay
                         "Not listening to you, the girl started doing her own thing, apparently counting the above as a joke."
                         "{color=#BC8F8F}{b} The level of relationship and trust has improved!"
                         $ ayano_contact += 5
                         $ ayano_trust += 1
                         $ depravity_ayano += 2
         hide ayano_cosplay
         $ ayano_ivent += 1
     elif ayano_ivent == 2:
         ayanogg1 "Hey, wait up!"
         "Quite harsh words made you quit your club business and turn to the source of the noise, which turned out to be familiar and, to some extent, pleasant."
         "Stopping by your carcass, the girl stretched out a little leaf with numbers that looked like a phone number."
         show ayano g24
         ayanogg1 "- И... This is my number. Actually, I didn't really want to give it at the beginning, but I finally realized one very depressing thing... It turns out that I'm communicating, let's just say, close enough, that's why I need your number!"
         show ayano g22
         "A little blush on Ayano's cheeks showed that she doesn't do such things often. It was more like a first for her. And how can such an active girl, according to her words, not have many friends or acquaintances?"
         menu:
             "{color=#000000}No problem\n{size=21}{i}0 energy{/i}{/size}{/color}."
                 label _ayano_ivent12:
                 "By nodding your head approvingly, you took a sheet of paper that was stretched out to you, after you entered the number on it into your phone and made a ringing to a girl. The ringtone, strange as it may seem, fully represented Ayano, but was so unusual for other girls..."
                 label _ayano_ivent1:
                 show ayano g24
                 ayanogg1 "And it turns out to be easier than I thought!"
                 show ayano g22
                 "Noticing that you thought her ringtone was interesting, Ayano rejected your call and began to snarl at you in surprise."
                 show ayano g26
                 ayanogg1 "Why, you've never heard heavy metal from the opposite sex on a ringtone?"
                 glgg "And you can read my mind straight."
                 show ayano g32
                 ayanogg1 "And I hear things like this all the time! Only, oddly enough, in the informal..."
                 glgg "Where do you go to see informals in our town? I thought they were long gone before they were even born."
                 show ayano g24
                 ayanogg1 "You might find out if you're close enough to me, and now you're no more my friend!"
                 show ayano g22
                 ayanogg1 "And seems to be the only one..."
                 glgg "Whatever you say."
                 "With a shrug of your shoulders, you left the girl to mind her own business."
                 $ ayano_number = 1
                 $ ayano_ivent += 1
                 "{color=#BC8F8F}{b}You got a new phone number!{/b}{/color}"
             "{color=#000000} In return, I want something... \n{size=21}{i}0 energy."
                 glgg "Then I want something in return."
                 show ayano g31
                 ayanogg1 "What?"
                 "Clearly unaware of what was going on, the girl looked you in the eye, which was a bit of a burden. In the end, to endure a long direct visual contact with a person is always difficult, but despite this, it is always easier to persuade through him. With a little thought, you finally decided what you wanted in return."
                 glgg "I want..."
                 menu:
                     "{color=#000000}How do you hold me\n{size=21}{i}2?"
                         $ energy -= 2
                         hide ayano
                         scene image "character/club/occult/npc/faceless/1.jpg" with dissolve
                         pause 3
                         if hour <= 16:
                             scene club_occult_ut with dissolve
                         elif hour <= 20:
                             scene club_occult_v with dissolve
                         "Surprised by your desire, the girl shrugged her shoulders after giving you a gentle hug. Anyway, it was more of a friendly hug with no hint of romance. In a moment, you were released."
                         show ayano g34
                         ayanogg1 "Now give me your number!"
                         "By nodding your head, you took a sheet of paper with a number and quickly put it on your cell phone and then you rang the girl. The ringtone, strange as it may seem, fully represented Ayano, but was far from the ordinary ringtones of other girls."
                         jump _ayano_ivent1
                     "{color=#000000}To kiss me \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         show ayano g33
                         ayanogg1 "No!"
                         hide ayano
                         "The girl's rude enough answer made it clear that she's not going to kiss you. "At least not directly. After leaving class, Ayano slammed the door loudly, and you began to expect a girl who seemed to resent you, but... It was much simpler."
                         show ayano g38
                         ayanogg1 "Drink."
                         "After giving you an open jar of soda, the preliminator of which she drank some of the liquid in it, the girl looked at you threateningly waiting for you to take her present."
                         show ayano g34
                         ayanogg1 "Since you didn't tell me what kind of kiss you wanted, it would be indirect. Drink it."
                         menu:
                             "{color=#000000} Stand by your\n{size=21}{i}{i}0 energy{/i}{/size}{/color}."
                                 "{color=FF0000} Not enough dominance points and/or girlfriendhood points."
                                 jump _ayano_ivent13
                             "{color=#000000} I got what wanted\n{size=21}{i}0 energy{/i}{/size}{/color}":
                                 label _ayano_ivent13:
                                 "Having decided not to piss off the girl for nothing, you took the can and in just a few seconds you emptied her, after throwing it in the urn."
                                 ayanogg1 "Happy?"
                                 jump _ayano_ivent12
                     "{color=#000000}To give me a can of soda, my throat is dry \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         "Once again, that incomprehensible look... As it seemed to you, you said your request clearly enough, but after a second, the girl's incomprehensible face was replaced with a satisfied one. After running out of the club room, Ayano left you for ten minutes, but then came back with a can of soda, which she gave you immediately."
                         $ cola += 1
                         "{color=#BC8F8F}{b} You have a new item{/b}{/color}."
                         show ayano g34
                         ayanogg1 "Happy?"
                         jump _ayano_ivent12
     elif ayano_ivent == 3:
         show ayano g22
         ayanogg1 "What do you think will happen to the club?"
         "A sudden question from a girl has knocked you out. You certainly didn't expect anything like that from her."
         glgg "Why do you suddenly ask that?"
         ayanogg1 "Well... In fact, our club doesn't do anything... Is this a good future for him?"
         menu:
             "{color=#000000} Since when do you care? \n{size=21}{i}0 energy{/i}{/size}{/color}":
                 glgg "And... Since when do you care about this?"
                 ayanogg1 "You know, when every weekday is monotonous, day after day, and you start thinking about the uselessness of your life... It's... Depressing?"
                 menu:
                     "{color=#000000}I don't think your life will change anyway if you make this club even a little active \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         glgg "I guess your life won't change much if you decide to improve the club somehow. One day to the next... What's the point?"
                         "By asking a rhetorical question, you moved the chair closest to you and fell on it with a fifth dot, after starting to look at the person you were talking to."
                         show ayano g40
                         ayanogg1 "It's possible that you're right... Thank you, anyway."
                         "Not knowing what's going on with the girl, you decided not to push the situation any further. You don't know how this is going to end, and risks don't always have a good start."
                         $ ayano_contact += 2
                         $ ayano_trust += 5
                     "{color=#000000} Maybe you're right... \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         glgg "I suppose you're right this time. Everyday life can actually be quite tense, and in this case a change of scenery may well help."
                         show ayano g32
                         "Who knows..."
                         "It was like a load fell from a girl, and she smiled looking at you. Looks like you helped her with an invisible problem."
                         $ ayano_contact += 1
                         $ ayano_trust += 7
             "{color=#000000} Maybe. \n{size=21}{i}0 energy{/i}{/size}{/color}."
                 glgg "A good future doesn't await him in this case, but that's probably not even the point. Club activity becomes successful only in two cases: if people in it become really close to each other, and if people like what they do".
                 "If you like hammering things with the help of the club, you've got the flag in your hands. Even that's a bit of a success, but a bit in a different direction."
                 "The girl who looked at you with a misunderstood look didn't understand much of your ranting, but still your words had a good effect on her, which is why her frown finally changed into a happy face."
                 show ayano g35
                 ayanogg1 "Thank you!"
                 glgg "You're welcome, I guess..."
                 hide ayano
                 scene image "character/club/occult/npc/faceless/2.jpg" with dissolve
                 pause 3
                 if hour <= 16:
                     scene club_occult_ut with dissolve
                 elif hour <= 20:
                     scene club_occult_v with dissolve
                 "As she ran up and hugged your carcass, the girl rubbed her face gently against your chest. After a minute of such tenderness, you finally let go, and the girl's sadness has evaporated, replacing the usual excessive energy." "with vpunch
                 $ ayano_contact += 3
                 $ ayano_trust += 9
         $ ayano_ivent += 1
         "{color=#BC8F8F}{b}The girl's relationship and trust have improved!{/b}{/color}"
     hide ayano
label club_occult:
     $ gg = 24
     if new_participant_club_occult == 1:
         python:
             for number_npc in range(1, number_npc_max):
                 new_participant_club_occult = 0
                 npc_id = 'npc'+str(number_npc)
                 club_npc = eval(npc_id)["club_npc"]
                 if club_npc == 4:
                     npc_id = 'npc'+str(number_npc)
                     name_npc = eval(npc_id)["npc_name"]
                     fam_npc = eval(npc_id)["npc_fam"]
                     v_npc = eval(npc_id)["pich_npc"]
                     gender_npc = eval(npc_id)["gender_npc"]
                     contact_npc = eval(npc_id)["contact_npc"]
                     love_npc = eval(npc_id)["love_npc"]
                     fear_npc = eval(npc_id)["fear_npc"]
                     perk = eval(npc_id)["perk"]
                     club_npc = 7
                     eval(npc_id)["club_npc"] = club_npc

                     number_occult_club += 1
                     name_npc213123 = str(name_npc)+' '+str(fam_npc)
                     name_club_npc_occult = 'name_club_npc_occult'+str(number_occult_club)
                     club_joob = 5
                     npc_character = {'perk':perk, "gender_npc":gender_npc, "pich_npc":v_npc, "npc_name":name_npc213123, "contact_npc":contact_npc, "love_npc":love_npc, "fear_npc":fear_npc, "npc_nature":npc_nature, "id_npc":id_npc, "club_npc":club_npc, "club_joob":club_joob}
                     setattr(store, name_club_npc_occult, npc_character)
                     renpy.jump('ivent_club_occult_npc')
     if hour <= 3:
         scene club_occult_v
     elif hour <= 16:
         scene club_occult_ut
     elif hour <= 20:
         scene club_occult_v
     else:
         scene club_occult_v
     $ rand_ayano = renpy.random.randint(1, 50)
     if ayano_ivent == 1 and ayano_contact >= 5 and hentai_patch_inicial == True:
         jump ayano_ivent
     elif ayano_ivent == 1 and ayano_contact >= 5 and hentai_patch_inicial == False:
         $ ayano_ivent += 1
     elif ayano_ivent == 2 and ayano_contact >= 20:
         jump ayano_ivent
     elif ayano_ivent == 3 and ayano_contact >= 40:
         jump ayano_ivent
     if ayano_contact >= 40 and rand_ayano == 3:
         $ dialoge = 10
         jump ayano2
     elif ayano_contact >= 40 and rand_ayano == 4:
         $ dialoge = 10
         jump ayano2
     elif ayano_contact >= 50 and rand_ayano == 6:
         $ dialoge = 11
         jump ayano2
     if student_soviet_progress == 100 and ayano_contact >= 80:
         jump ayano100
     elif student_soviet_progress == 101 or student_soviet_progress == 102 and ayano_contact >= 130:
         jump ayano101
     elif student_soviet_progress == 103 and ayano_contact >= 180:
         jump ayano102
     if number_occult_club >= 5 and student_soviet_progress == 104:
         jump ayano103
     $ dialoge = 1
     $ page = 0
     $ club_control = 1
     $ menu_control = 1
     if occult_club == 3:
         $ ayano_dialoge = 0
         $ club_rang = 0
         $ club_human = 2
         $ school_festival = 0
         $ ayano_perception = 1
         $ ayano_trust = 0
         $ dialoge_club = 0
         $ ayano_ivent += 1
         $ ayano_number = False
         if hentai_patch_inicial == True:
             $ depravity_ayano = 0
         "Upon entering the club room, you immediately noticed a figure you knew who didn't even notice you: Ayano in person."
         "Maybe you should ask her something. She's not going to run away from asking now."
         menu:
             "{color=#000000} Ask about the lack of people in the club room \n{size=21}{i}0 energy{/i}{/size}{/color}."
                 "Having noticed that there are actually two members in the club, counting you, you've made it possible to learn about the current state of the club in general."
                 glgg "Can you explain why only a couple of people are in the club?"
                 show ayano g25
                 "The girl who wasn't expecting anyone behind her looked at you scared, but then she exhaled with relief."
                 show ayano g22
                 ayanogg1 "Oh, it's just you... So what were you asking?"
                 hide ayano
                 "When you look at a girl with a terrible gaze, you turn your back on the empty class."
                 label _club_occult:
                 glgg "So can you tell me why it's just you and me at the club?"
                 ayanogg1 "Because there's enough of the two of us in the club!"
                 glgg "And it was because of these words that I had a second question... What is the purpose of the club?"
                 "Turned towards the girl, you asked a leading question, which slightly, but made the situation worse."
                 label _club_occult1:
                 show ayano g30
                 "After the question, the girl thought a little, falling fifth point on a chair next to you and looking at you with an incomprehensible look."
                 "Realizing that you wouldn't leave her alone, even if you were ignored, she took a hard sigh."
                 show ayano g32
                 ayanogg1 "As you know, our school has a rule: student by club. There are no exceptions, but this club is to avoid useless activities in other clubs."
                 ayanogg1 "So to speak, the self-employed club in the wrapper of the occult club."
                 menu:
                     "{color=#000000}Picture \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         glgg "So now this club will be doing something to attract new members."
                         show ayano g26
                         "The girl who was expecting this kind of answer winked at you after getting out of the chair and hitting your shoulder with her palm a couple of times."
                         ayanogg1 "Good luck, cap."
                         hide ayano
                         "Before I could say anything to the girl who left you alone with the dusty club room, the door slammed in front of you."
                         glgg "Looks like I'll have to develop the club myself or get Ayano to help somehow..."
                         $ occult_club += 1
                         $ ayano_contact -= 1
                         "{color=#BC8F8F}{b}Relationships with the girl have deteriorated!{/b}{/color}"
                         jump club_occult
                     "{color=#000000} Shrug and accept girl's version \n{size=21}{i}0 energy{/i}{/size}{/color}."
                         glgg "Well, that's what I expected, though."
                         "When you said that, you fell your fifth point on the chair, following the example of your new friend."
                         show ayano g24
                         ayanogg1 "That's the right decision, buddy."
                         hide ayano
                         $ ayano_contact += 1
                         $ occult_club += 1
                         "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
                         "Relaxed, the girl literally fell asleep in a chair, not paying much attention to you. She doesn't seem very interested in you."
                         jump club_occult
             "{color=#000000} Find out how the girl's doing \n{size=21}{i}{i}0\n{size=21}{i}[stats_erudition_gg_info]/30 eloquence{/i}{/size}{/color}":
                 "When you thought it was the right decision to ask a girl not about the club, but about life, you came up behind her and patted her on the shoulder so she'd pay attention to you."
                 show ayano g25
                 ayanogg1 "DO NOT KILL!" with vpunch
                 show ayano g22
                 "Scared to look at you, the girl was relieved to exhale, but still her voice was a little shaky."
                 show ayano g34
                 ayanogg1 "What was it you wanted to tell me?"
                 "She seems obviously not in the mood... We should say something neutral."
                 if stats_erudition_gg_info >= 30:
                     glgg  "So how's your mood?"
                     show ayano g22
                     glgg "You said it was strange enough in this situation, but such a routine question, which also knocked out your interlocutor, who obviously did not expect this."
                     show ayano g22
                     ayanogg1 "It's okay, but what's with the questions? I thought we were going to start asking questions about the club, not me."
                     glgg "I can't get to know my soccer player better, who I see is a single target in this room?"
                     show ayano g31
                     ayanogg1 "We can, of course, but this... Unusual?"
                     menu:
                         "{color=#000000} Ask how Ayano is on the personal front \n{size=21}{i}{i}0\n{size=21}{i}[stats_erudition_gg_info]/40 eloquence{/i}{/size}{/color}":
                             if stats_erudition_gg_info >= 40:
                                 glgg "So what's on your personal front, Ayano?"
                                 "The girl was a little embarrassed to answer your question, but after a confident tone, it seemed as if there was no trembling voice."
                                 ayanogg1 "It's okay, there's going to be a bunch of kids and a confident husband who'll love m!..."
                                 show ayano g28
                                 "Suddenly the girl completely changed her face and looked at you in surprise."
                                 show ayano g29
                                 ayanogg1 "WHY DID I EVEN START SAYING THAT?" with vpunch
                                 glgg "I have no idea why, but... It turns out you don't have a boyfriend, right?"
                                 show ayano g22
                                 ayanogg1 "Yes!"
                                 show ayano g29
                                 ayanogg1 "You said it again!"
                                 show ayano g30
                                 ayanogg1 "Do you have superpowers?"
                                 $ occult_club += 2
                                 "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
                             else:
                                 glgg "Well... So, what's on your personal front?"
                                 ayanogg1 "It seems like you're going somewhere you're not asked to go."
                                 $ ayano_contact -= 1
                                 "{color=#BC8F8F}{b}Relationships with the girl have deteriorated!{/b}{/color}"
                             "Knowing that further dialogue wouldn't lead anywhere, you changed the subject to school."
                             menu:
                                 "{color=#000000} Ask about the lack of people in the club room.{/color}":
                                     jump _club_occult
                                 "{color=#000000}Ask about the goals of the club{/color}":
                                     jump _occult_club2
                         "{color=#000000} Find out what Ayano does in his spare time \n{size=21}{i}{i}0\n{size=21}{i}[stats_cunning_gg_info]/30 cunning{/i}{/size}{/color}":
                             "Ignoring some of the girl's resentment, you asked yourself the obvious and standard question used in dating."
                             glgg "So what do you do in your spare time?"
                             show ayano g31
                             ayanogg1 "Uh... Well, uh... I don't think it's that important!"
                             if stats_cunning_gg_info <= 29:
                                 "With a shrug of your shoulders, you decided to translate the subject without filling your head with too much detail about a girl's personal life and interests."
                                 jump _school_t
                             else:
                                 "With a shrug of your shoulders, you decided to translate the subject without filling your head with too much detail about a girl's personal life and interests."
                                 show ayano g33
                                 ayanogg1 "What are you looking at? Don't you have anything to do?"
                                 "When you thought it was strange, you looked at the girl irritably, and then moved your gaze back to the club room, ignoring the dissatisfaction of your interlocutor."
                                 show ayano g22
                                 ayanogg1 "Well, yes... I'm out of class here, so there's so many portable consoles and food..."
                                 show ayano g33
                                 ayanogg1 "But I won't give you anything for your excessive curiosity, all right?"
                                 show ayano g34
                                 ayanogg1 "And you found out what I do in my spare time, so no complaints are accepted."
                                 jump _school_t
                         "{color=#000000}Translate this conversation to school discussion \n{size=21}{i}0 energy{/i}{/size}{/color}."
                             label _school_t:
                             menu:
                                 "{color=#000000} Ask about the lack of people in the club room \n{size=21}{i}0 energy{/i}{/size}{/color}."
                                     jump _club_occult
                                 "{color=#000000} Ask about club goals \n{size=21}{i}0 energy{/i}{/size}{/color}."
                                     jump _occult_club2
                 else:
                     "When you couldn't think of anything, you decided to change your plans for further dialogue by asking your interlocutor about the club."
                     menu:
                         "{color=#000000} Ask about the lack of people in the club room \n{size=21}{i}0 energy{/i}{/size}{/color}."
                             jump _club_occult
                         "{color=#000000} Ask about club goals \n{size=21}{i}0 energy{/i}{/size}{/color}."
                             jump _occult_club2
             "{color=#000000} Ask about club goals \n{size=21}{i}0 energy{/i}{/size}{/color}."
                 "Having decided that the best solution in this situation is to ask about the goals of the club, you sit next to the girl and move the chair under your fifth point, falling on it."
                 show ayano g25
                 ayanogg1 "READY FOR WORK AND DEFENSE!" with vpunch
                 show ayano g22
                 "A girl who wasn't expecting anyone else in the club room almost fell out of her chair, making a nice enough squeak and strange words in a trembling voice, but after that she exhaled with a certain calmness when she saw you."
                 glgg "Why are you so scared?"
                 show ayano g34
                 ayanogg1 "Who knew a guy who likes to watch schoolgirls would sneak in from behind me!"
                 "When you took a hard sigh, you ignored Ayano's words, which she clearly said, being not in the best spirits."
                 show ayano g33
                 ayanogg1 "So what was it you wanted to say?"
                 label _occult_club2:
                 glgg "So... What's the club's purpose, Ayano?"
                 jump _club_occult1
     else:
         call screen occult_club_control
label ayano103:
     if hour <= 16:
         scene club_occult_ut with dissolve
     elif hour <= 20:
         scene club_occult_v with dissolve
     show ayano g32 with dissolve
     ayanogg1 "And you did it fast enough... You're still so good, [player_name]! It's so fast to find three people in a club - you have to really know how! "
     glgg "You and Gagarin didn't meet up there again while I was looking? That's weird enough to hear from you, too... "
     show ayano g41
     ayanogg1 "Don't joke about that case! By the way, I had a headache after that for a very long time! It's not funny! "
     glgg "Well... You can see better than me. It wasn't me who punched the floor through the back of my head after all."
     show ayano g22
     ayanogg1 "Boo, you're evil... Anyway, I wanted to compliment you again, but suddenly I changed my mind! Anyway, what do you think about raising the profile of the club within and outside the school? "
     glgg "You know, if we were some kind of science or sports club, your question would be a lot more weight, and now... Now it's just a set of letters from a girl who doesn't know what she's talking about. "
     show ayano g33
     ayanogg1 "Boo-boo-boo, you're mumbling again... Anyway, what do you think about parties like the Cosplay Club? "
     glgg "I have no idea what they're doing there."
     show ayano g32
     ayanogg1 "They go to all kinds of events, they discuss all kinds of things, and they just... Communicate?"
     glgg "Stupid and inappropriate. One thing is the Cosplay, and another thing is... The occult?"
     show ayano g22
     ayanogg1 "All right... What do you suggest, then?"
     glgg "Authority can be raised in many ways, not only through events: more people, some articles on our topic that can attract new participants..."
     glgg "We just have to do our own original planned activities: mysticism, paranormalism and the like... "
     show ayano g32
     ayanogg1 "Yet you not only have your pretty face in you, but you're also smart enough! "
     glgg "It sounded like an insult..."
     show ayano g26
     ayanogg1 "Anyway, what you said can be arranged right now."
     show ayano g32
     ayanogg1 "We can send those three members you found, explore something... To a place where there are ghosts."
     glgg "We may initially have enough of a journalism club... And the people there may be those who are interested in the topic, not amateurs like us."
     glgg "Right now, I think we can ask the other members to do the paranormal, and you can deal with the journalism club. It'll be a lot more effective. "
     show ayano g26
     ayanogg1 "Okay, I'll try to deal with the journalism, and you manage the contestants. Maybe they'll do something that might attract... "
     glgg "Do not repeat my words. Go deal with the assignment I gave you. "
     show ayano g22
     ayanogg1 "Boo-boo-boo"
     $ ayano_contact += 20
     $ ayano_trust += 20
     $ student_soviet_progress = 105
     call screen occult_club_control
label ayano102:
     $ club_rang = 2
     $ gg == 1000
     scene black with dissolve
     "While doing business in the club, the feeling of deja vu suddenly enveloped you, as well as the palms of a girl you already know very well. Closing your eyes, she said a phrase with a rather playful tone, which is familiar to many from childhood."
     ayanogg1 "Guess who."
     glgg "You know, this game would be even more interesting if there weren't two people in our club..."
     ayanogg1 "That's exactly the problem I wanted to talk to you about, [player_name]."
     glgg "Oh, how... Go ahead, I'm all ears."
     ayanogg1 "Boo-boo-boo, you're angry again..."
     glgg "I shouldn't be angry when I haven't seen anything for a long time."
     ayanogg1 "Exactly!"
     if hour <= 16:
         scene club_occult_ut with dissolve
     elif hour <= 20:
         scene club_occult_v with dissolve
     show ayano g32 with dissolve
     ayanogg1 "Is that better?"
     glgg "You bet. Say what you want."
     show ayano g36
     ayanogg1 "How about you become my right hand?"
     glgg "What?"
     show ayano g32
     ayanogg1 "Well, with my right hand at the club.."
     glgg "And now who am I?"
     show ayano g35
     ayanogg1 "You... You were a rookie, but... I decided to promote you for your services!"
     glgg "And the salary will be?"
     show ayano g41
     ayanogg1 "Stop joking already!"
     show ayano g40
     ayanogg1 "Anyway, answer me one question... Can you get the club up from the bottom and make it a decent place within the school?"
     glgg "Perhaps, but... Why do you have to ask these questions anyway? You didn't care about that much before."
     show ayano g22
     ayanogg1 "Well... I've been thinking a lot about what happened then and I realized that you're my best friend, helping out everywhere, always and everywhere. And, you know..."
     show ayano g39
     ayanogg1 "It has come to me, however, that even if there are more people in the club, he won't stop tying us up..."
     glgg "It's like... And then what?"
     show ayano g36
     ayanogg1 "I want our club not to be closed, and this memory of our friendship is left for at least one more year!"
     glgg "So, to put it simply, you just want me to find at least three more people to keep the club open?"
     show ayano g32
     ayanogg1 " Exactly! So, can you handle it? "
     glgg "That's where we'll see. Anyway, since I can invite someone and not get breeches for it, why not do it in my spare time?"
     show ayano g36
     ayanogg1 "You're a cutie..."
     glgg "Why did you even just say that?"
     show ayano g32
     ayanogg1 "Well, what about it! You're trying to show alpha with a lot to do, but in fact, as soon as you get out of the club, you'll run out looking for members!"
     glgg "I changed my mind about helping you..."
     show ayano g26
     ayanogg1 "Heh-heh-heh, I'm kidding, don't worry. And remember: I'll always be grateful for you and your actions. If you need anything and I can do it, don't be shy!"
     glgg "If you say so..."
     $ ayano_contact += 25
     $ ayano_trust += 20
     $ student_soviet_progress = 104
     call screen occult_club_control
label ayano101:
     $ microwave = 1
     $ gg == 1000
     if hour <= 16:
         scene club_occult_ut with dissolve
     elif hour <= 20:
         scene club_occult_v with dissolve
     "Calmly sitting in your familiar comfort zone, you heard the sound of the door opening, which literally fell into, your friend, to some extent, even a friend."
     "Quacking and carrying a huge box, almost falling, the girl soon put it on the table and tired plunged into the nearest chair, breathing heavily in and out of oxygen."
     glgg "What did you bring this time?"
     "Still breathing heavily, Ayano looked at you, but after a second so 10 turned her eyes to the ceiling, still breathing like a 30-year-old smoker who climbed the stairs to the next floor."
     "As you rose from your seat, out of curiosity, you came to the box and, taking a clerical knife, which the girl apparently had prepared in advance, put it on the table, opened it."
     glgg "Did you really buy a microwave?"
     ayanogg1 "Ye... Yes... Your work will not go unnoticed..."
     "After sitting next to the girl, you started waiting for her to breathe, which happened soon. After ten minutes, she turned again to your side, having regained her breath, and said."
     show ayano g21 with dissolve
     ayanogg1 "You didn't expect it, did you?"
     glgg "That's an understatement."
     show ayano g24
     ayanogg1 "Since our club doesn't do much, but gets this kind of funding, I decided to spend the money on something useful!"
     glgg "I don't think the microwave is anything useful for our club."
     show ayano g26
     ayanogg1 "Oh, come on, you nerd! After all, now we can heat up the food we bought at the supermarket."
     glgg "You're acting..."
     hide ayano
     show yuki g4 with dissolve
     yuki "Oh, my God! And you're well settled. With the funding you were given to buy..."
     hide yuki
     show ayano g42 with dissolve
     ayanogg1 "AND HOW DID YOU GET IN HERE, BITCH?"
     hide ayano
     show yuki g2 with dissolve
     yuki "Easy, easy, easy, easy, easy. I just came to see..."
     hide yuki
     show ayano g41 with dissolve
     ayanogg1 "Check it out, huh? DON'T FORGET THAT YOU WANTED TO CLOSE OUR CLUB! YOU'RE THE ENEMY!"
     hide ayano
     show yuki g2 with dissolve
     yuki "I didn't close it, and I also raised the funding, so, Ayanochka, calm down, please."
     hide yuki
     show ayano g41 with dissolve
     ayanogg1 "DON'T CALL ME THAT!"
     hide ayano
     show yuki g6 with dissolve
     yuki "If you say so. Anyway, I came to warn you."
     hide yuki
     show ayano g33 with dissolve
     ayanogg1 "Yeah? Our club is going to close, isn't it?"
     hide ayano
     show yuki g10 with dissolve
     yuki "Partly. As you know, the charter says that the club should develop in any case, as well as the requirements for it during the school year. If it lacks members, it will be closed."
     yuki "If at the beginning of the first trimester the bar is two people, then in the second five. You must understand that it can end badly if you spend this... On this."
     hide yuki
     show ayano g34 with dissolve
     ayanogg1 "YES? THANK YOU FOR THE WARNING! IT HELPED US SO MUCH!"
     hide ayano
     show yuki g2 with dissolve
     yuki "It's no use talking to you about it..."
     show yuki g11 with dissolve
     yuki "[player_name] what do you think about all this?"
     glgg "Honestly? I have no idea. There's plenty of time until the next trimester, so we can always find new entrants without being overly active."
     show yuki g2 with dissolve
     yuki "Something told me you'd say something like that..."
     show yuki g3 with dissolve
     yuki "Okay, that's your business. Mine's just a warning, but... I don't want what you've been working for, you know, to just disappear into the abyss."
     glgg "Whatever you say."
     show yuki g4 with dissolve
     yuki "Anyway, I hope we understand each other. Oh, and yes... If you decide to buy something like that, please close the doors, or if anyone notices, there'll be a lot of noise."
     hide yuki
     "Having looked at the club room again, Yuki quietly stepped out of the club room, literally theatrically closing the door."
     show ayano g41 with dissolve
     ayanogg1 "Bitch..."
     glgg "..."
     show ayano g22
     ayanogg1 "Look, [player_name], what are we going to do about it? Do you have any ideas?"
     glgg "Ideas? We just need to get five people together at the club. It's, you know, not such a problem..."
     ayanogg1 "But then our club... It won't be our... It'll be common... You... You want that?"
     glgg "What are you talking about?"
     show ayano g31
     ayanogg1 "Well... Now this is our private place where we can do whatever we want within the school, and if there's anyone else here, then..."
     glgg "It's likely to be the same nerds and truants as you. Probably hooligans. Those who are considered scum."
     ayanogg1 "I understand, but..."
     glgg "But?"
     ayanogg1 "Understand... Our private little corner..."
     glgg "Strange hints you've got... Originally, a club is a collection of people's interests, not a hiding place for two people. Don't forget that."
     show ayano g22
     ayanogg1 "..."
     glgg "Okay. In the future, the situation will be clearer, and now let it be as it was."
     show ayano g45
     ayanogg1 "Okay... Thank you... I'm glad you agreed..."
     hide ayano
     "Embarrassedly turning away from you, the girl continued to deal with the microwave, leaving you alone with your own."
     $ ayano_contact += 10
     $ ayano_trust += 10
     $ student_soviet_progress = 103
     call screen occult_club_control
label ayano100:
     $ gg == 1000
     if hour <= 16:
         scene club_occult_ut with dissolve
     elif hour <= 20:
         scene club_occult_v with dissolve
     $ minute += 20
     show ayano g31 with dissolve
     ayanogg1 "You... You're serious?"
     glgg "What's serious?"
     show ayano g33
     ayanogg1 "Where are we gonna get this money! It's... It's a whole bunch of credits, and there's only two of us in the club..."
     show ayano g23
     ayanogg1 "Admit it! You did it, didn't you?"
     glgg "And you're guessing..."
     show ayano g30
     ayanogg1 "But... But what do you think of this bitch..."
     show ayano g33
     ayanogg1 "What did you do?"
     glgg "Is it so important now?"
     show ayano g41
     ayanogg1 "Yes! This is very important!"
     show ayano g42
     ayanogg1 "TELL ME WHAT YOU DID!"
     glgg "Just helped her. That's all."
     show ayano g34
     ayanogg1 "Did you... Did you help her with the next vote? As I recall, she has some problems with that..."
     glgg "You could say that."
     show ayano g31
     ayanogg1 "I see... Okay, but..."
     show ayano g34
     ayanogg1 "WHERE DO WE SPEND THIS MONEY?!"
     glgg "Well... You can spend it on a microwave. You kind of wanted to buy it a long time ago to heat up supermarket food."
     show ayano g22
     ayanogg1 "You... Why did you do that? I don't understand..."
     glgg "Did I need a reason to make you feel good?"
     show ayano g41
     ayanogg1 "You... Don't act like an alpha! Say what you want in return for your actions!"
     glgg "I don't want anything, calm down..."
     show ayano g42
     ayanogg1 "Speak up!"
     glgg "Okay, then how about..."
     menu:
         "{color=#000000}Kiss me. \n{size=21}{i}10 energy{/i}{/size}{/color}."
             hide ayano
             "With a smile in return, the girl punched you on the lips clumsily, after retreating two steps in embarrassment." with vpunch
             glgg "No question about it... And where did your sarcasm go?"
             show ayano g41 with dissolve
             ayanogg1 "To the same place as your tactfulness!"
             show ayano g22
             ayanogg1 "Funding our club is now 15,000 credits a month, how can you not fulfill the wish of the one who did this?!"
             glgg "That's how it is... And if I asked for nonsense, would you do it too?"
             show ayano g24
             ayanogg1 "Who knows... Now guess!"
             glgg "You are so cruel..."
             show ayano g32
             ayanogg1 "Brutal, but you know... I really appreciate it. You've done so much for the club..."
             glgg "One single action is a lot?"
             show ayano g44
             ayanogg1 "You look at your actions only from one side, without even thinking about what you [player_name] did for me, and for the club, much more than anyone else..."
             glgg "Here it is..."
             show ayano g30
             ayanogg1 "I'm really grateful to you... You... You think my insignificant words are something... Something much bigger, taking them into account..."
             glgg "Happy to help you."
             show ayano g24
             ayanogg1 "You know, just so you're not so upset, I'll let you come up to me anytime you want, so..."
             glgg "With what?"
             show ayano g26
             ayanogg1 "Who knows... Now guess!"
             glgg "Shall I repeat...?"
             hide ayano
             "Embarrassedly turning away from you, the girl sat down in her already raped habitual place and continued to do her business, occasionally looking at you with a certain caution. When you decided to check her words, you followed Ayano's example by sitting next to her."
             $ energy -= 10
             $ student_soviet_progress = 101
             $ ayano_contact += 25
             $ ayano_trust += 25
             call screen occult_club_control
         "{color=#000000} I've had enough of your happy face \n{size=21}{i}5 energy{/i}{/size}{/color}":
             $ energy -= 5
             show ayano g41
             ayanogg1 "DON'T ACT LIKE AN ALPHA, DAMN IT..."
             glgg "Okay, okay."
             show ayano g42
             ayanogg1 "What do you want?"
             glgg "Your smile."
             show ayano g33
             ayanogg1 "YOU GOTTA BE KIDDING ME. You did something weird just to see me smile?!"
             glgg "Is that so weird?"
             ayanogg1 "Yes! It's very strange to see a man who's recently been indifferent to me! Admit it, you need a cut, right?"
             glgg "I don't really need those pennies..."
             show ayano g41
             ayanogg1 "Pebbles? 15,000 credits a month for a club like this?!"
             glgg "Oh, how... And she really tried to get more funding..."
             show ayano g42
             ayanogg1 "SO YOU DIDN'T EVEN AGREE ON THE AMOUNT?"
             glgg "Yeah, well, it was about the simplest funding..."
             show ayano g38
             ayanogg1 "The easiest financing is 2,000 credits per month, not 15,000! Clubs that have a few dozen members have this kind of funding, and they really need this money! What have you done for that bitch?!"
             glgg "Helped."
             show ayano g34
             ayanogg1 "How did you help her so much that she knocked out 15 grand for our sleazy club that the students' claws used to hone in. Tip, to close?!"
             glgg "Why are you so mad? I helped you, and you had a passionate interrogation..."
             ayanogg1 "You're either a fucking genius or a jerk.."
             glgg "Can we all do this together?"
             show ayano g42
             ayanogg1 "Don't be sarcastic! JUST TELL ME!"
             glgg "I just helped her with the next election, that's all."
             show ayano g41
             ayanogg1 "Anyway, I hear you... She had her eye on you, be careful with that snake, but..."
             show ayano g32
             ayanogg1 "Anyway... Thank you."
             glgg "Payment has been received. Please contact us again."
             hide ayano
             "With a smile in return, the girl punched you on the lips clumsily, after retreating two steps in embarrassment." with vpunch
             show ayano g26 with dissolve
             ayanogg1 "Once again... Thank you..."
             glgg "You change your mind about different situations... Impulsivity is the same."
             show ayano g31
             ayanogg1 "I'm... I'm just worried about you... You helped me, not even me... Us, but I really hope you don't contact her again. She's... She's not a nice person."
             glgg "I'll try not to get in touch."
             show ayano g22
             ayanogg1 "Thank you again..."
             hide ayano
             "After sitting down in her comfort zone, Ayano returned to her business as if nothing had happened."
             glgg "I guess I've had some openings with her after what happened..."
             $ student_soviet_progress = 101
             $ ayano_contact += 25
             $ ayano_trust += 25
             call screen occult_club_control
         "{color=#000000} Give me a soda. \n{size=21}{i}0 energy{/i}{/size}{/color}."
             show ayano g39
             ayanogg1 "And why do you like soda so much..."
             glgg "I don't know. Is she... Refreshing?"
             show ayano g22
             ayanogg1 "You're kidding, right?"
             glgg "Maybe."
             show ayano g27
             ayanogg1 "Do you know what kind of funding the club has at the moment?"
             glgg "Not really, but I really hope that you'll enlighten me with some... Four-digit number."
             show ayano g34
             ayanogg1 "15,000 a month."
             glgg "And I guess I even tried too hard, since I was valued at this price."
             show ayano g32
             ayanogg1 "Yeah. And for some reason, I don't even want to know the details. Anyway... You wanted a soda, right?"
             glgg "That's right."
             show ayano g22
             ayanogg1 "You can ask me for as much soda as you want, and not just..."
             glgg "Oh, yeah. Can I take your chips?"
             ayanogg1 "Not only..."
             glgg "Um... Can I take all your food?"
             ayanogg1 "Not just..."
             glgg "I don't know what else. Can you give me a hint?"
             hide ayano
             "With a smile in return, the girl punched you on the lips clumsily, after retreating two steps in embarrassment."
             show ayano g22 with dissolve
             ayanogg1 "One more time... Thank you..."
             glgg "The hint is clear. I will address you as soon as I want something like that."
             hide ayano
             "Embarrassedly turning away from you, the girl sat down in her already raped habitual place and continued to do her business, occasionally looking at you with a certain caution."
             $ free_soda = 1
             $ student_soviet_progress = 102
             $ ayano_contact += 25
             $ ayano_trust += 25
             call screen occult_club_control
label ayano_d:
     $ dialoge_ayano = 0
     $ chance_dialoge1 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 25
     $ chance_dialoge2 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 5
     $ chance_dialoge3 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 15
     $ chance_dialoge5 = int(stats_erudition_gg_info + ayano_contact) + 35
     $ chance_dialoge6 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 10
     $ chance_dialoge7 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 5
     $ chance_dialoge8 = int(stats_erudition_gg_info + (ayano_contact / 1.5))
     $ flirt_chance = int((stats_erudition_gg_info + ayano_contact) / 1.5) - 10
     $ minet_chance = int(popularity_club_occult / 0.75)
     call screen ayano_d
screen ayano_d:
     $ chance_dialoge1 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 25
     $ chance_dialoge2 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 5
     $ chance_dialoge3 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 15
     $ chance_dialoge5 = int(stats_erudition_gg_info + ayano_contact) + 35
     $ chance_dialoge6 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 10
     $ chance_dialoge7 = int(stats_erudition_gg_info + (ayano_contact / 1.5)) + 5
     $ chance_dialoge8 = int(stats_erudition_gg_info + (ayano_contact / 1.5))
     $ flirt_chance = int((stats_erudition_gg_info + ayano_contact) / 1.5) - 10
     $ minet_chance = int(popularity_club_occult / 0.75)
     key 'shift_alt_K_F12' action SetVariable("ayano_contact", ayano_contact+10)
     key 'shift_alt_K_F11' action SetVariable("ayano_trust", ayano_trust+10)
     if hour <= 7:
         add "club_occult_v"
     elif hour <= 16:
         add "club_occult_ut"
     elif hour <= 20:
         add "club_occult_v"
     else:
         add "club_occult_v"
     if dialoge_ayano == 0 or dialoge_ayano == 2 or dialoge_ayano == 4:
         imagebutton xalign 0.4 ypos 100:
             mouse "images/hands.png"
             idle 'ayano g44'
             if ayano_contact <= 40:
                 hover 'ayano g41'
                 hovered SetVariable('dialoge_ayano', 2)
                 unhovered SetVariable('dialoge_ayano', 5)
                 action SetVariable('energy', energy-4), SetVariable('minute', minute+10), SetVariable('dialoge_ayano', 1), SetVariable('ayano_contact', ayano_contact-4), SetVariable('ayano_trust', ayano_trust-2)
             else:
                 hover 'ayano g36'
                 hovered SetVariable('dialoge_ayano', 4)
                 unhovered SetVariable('dialoge_ayano', 6)
                 action SetVariable('energy', energy-4), SetVariable('minute', minute+10), SetVariable('dialoge_ayano', 3), SetVariable('ayano_contact', ayano_contact+2), SetVariable('ayano_trust', ayano_trust+1)
     elif dialoge_ayano == 1:
         imagebutton xalign 0.4 ypos 100:
             idle 'ayano g42'
     elif dialoge_ayano == 3:
         imagebutton xalign 0.4 ypos 100:
             idle 'ayano g36'
     elif dialoge_ayano == 5:
         imagebutton xalign 0.4 ypos 100:
             focus_mask True
             idle 'ayano g22'
             hover 'ayano g41'
             hovered SetVariable('dialoge_ayano', 2)
             unhovered SetVariable('dialoge_ayano', 5)
             action SetVariable('dialoge_ayano', 1)
     elif dialoge_ayano == 6:
         imagebutton xalign 0.4 ypos 100:
             idle 'ayano g32'
             hover 'ayano g36'
             hovered SetVariable('dialoge_ayano', 4)
             unhovered SetVariable('dialoge_ayano', 6)
             action SetVariable('dialoge_ayano', 3)
     elif dialoge_ayano == 7:
         imagebutton xalign 0.4 ypos 100:
             idle 'ayano g36'
     elif dialoge_ayano == 8:
         imagebutton xalign 0.4 ypos 100:
             idle 'ayano g41'
     add 'gui/system/ayano_dialoge1.png'
     add 'gui/system/ayano_dialoge.png'
     $ days_name = name_days[str(days)]
     if hour <= 9 and minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=30}[days_name] 0[hour]:0[minute]{/size}{/font}" xalign 0.306 yalign 0.9785 size 32
     elif hour <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=30}[days_name] 0[hour]:[minute]{/size}{/font}" xalign 0.306 yalign 0.9785 size 32
     elif minute <= 9:
         text "{font=gui/fonts/ubuntu.ttf}{size=30}[days_name] [hour]:0[minute]{/size}{/font}" xalign 0.306 yalign 0.9785 size 32
     else:
         text "{font=gui/fonts/ubuntu.ttf}{size=30}[days_name] [hour]:[minute]{/size}{/font}" xalign 0.306 yalign 0.9785 size 32
     text "{font=gui/fonts/ubuntu.ttf}[energy]{/font}" xalign 0.41 yalign 0.9785 size 32
     text "{font=gui/fonts/ubuntu.ttf}[money]{/font}"  xalign 0.53 yalign 0.9785 size 32
     if dialoge_ayano == 0:
         text '{size=34}{color=#e6e6e6}There is something you wanted to tell me?{/color}{/size}' xalign 0.3 yalign 0.83
     elif dialoge_ayano == 2:
         text '{size=34}{color=#e6e6e6}Do not look at me with those eyes, you pervert!\nDo not you dare even think about it!{/color}{/size}' xpos 460 yalign 0.87
     elif dialoge_ayano == 1:
         text '{size=34}{color=#e6e6e6}Hey! Do not touch me with your dirty paws,\nIdiot!{/color}{/size}' xpos 460 yalign 0.87
     elif dialoge_ayano == 3:
         text '{size=34}{color=#e6e6e6}Heh heh... If you can, touch me more often... {/color}{/size}' xpos 460 yalign 0.83
     elif dialoge_ayano == 4:
         text '{size=34}{color=#e6e6e6}Hey... Is there something on my face?{/color}{/size}' xpos 460 yalign 0.83
     elif dialoge_ayano == 5:
         text '{size=34}{color=#e6e6e6}Tell me what you wanted, [player_name]...{/color}{/size}' xpos 460 yalign 0.83
     elif dialoge_ayano == 6:
         text '{size=34}{color=#e6e6e6}Heh heh... Well, whatever you say. Anyway, I will find out soon enough!{/color}{/size}' xpos 460 yalign 0.83
     elif dialoge_ayano == 7:
         text '{size=34}{color=#e6e6e6}Heh-heh... Is it me, or are you really cuter than usual today?{/color}{/size}' xpos 460 yalign 0.83
     elif dialoge_ayano == 8:
         text '{size=34}{color=#e6e6e6}What do you want from me, you dirty pervert?!{/color}{/size}' xpos 460 yalign 0.83
     imagebutton xpos 20 ypos 605:
         idle Text('{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Talk{/color}{/size}{/font}')
         hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=32}{color=#282828}Talk{/color}{/size}{/font}{/u}')
         action SetVariable('dialoge', 1)
     imagebutton xpos 20 ypos 655:
         idle Text('{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Romance{/color}{/size}{/font}')
         hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=32}{color=#282828}Romance{/color}{/size}{/font}{/u}')
         action SetVariable('dialoge', 2)
     imagebutton xpos 20 ypos 700:
         idle Text('{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Erotica{/color}{/size}{/font}')
         hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=32}{color=#282828}Erotica{/color}{/size}{/font}{/u}')
         action SetVariable('dialoge', 3)
     imagebutton xpos 20 ypos 745:
         idle Text('{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Back{/color}{/size}{/font}')
         hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=32}{color=#282828}Back{/color}{/size}{/font}{/u}')
         action Hide('ayano_d'), Jump('club')
     vpgrid:
         cols 1
         rows 1
         spacing 1
         xpos 20 ypos 830 xysize (350, 310)
         child_size (350, 310)
         draggable True
         mousewheel True
         arrowkeys True
         if ayano_contact <= 15:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Relationship:{/color}{color=#282828} acquaintance {/color}{color=#282828}([ayano_contact]){/color}{/size}{/font}'
         elif ayano_contact <= 85:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Relationship:{/color}{color=#b0cc62} friend {/color}{color=#282828}([ayano_contact]){/color}{/size}{/font}'
         elif ayano_contact <= 150:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Relationship:{/color}{color=#89ad27} best friend {/color}{color=#282828}([ayano_contact]){/color}{/size}{/font}'
         elif ayano_contact >= 151:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Relationship:{/color}{color=#ff8cb4} You are loved! {/color}{color=#282828}([ayano_contact]){/color}{/size}{/font}'
         if ayano_trust <= 15:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Trust:{/color}{color=#282828} low {/color}{color=#282828}([ayano_trust]){/color}{/size}{/font}'
         elif ayano_trust <= 85:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Trust:{/color}{color=#b0cc62} middle {/color}{color=#282828}([ayano_trust]){/color}{/size}{/font}'
         elif ayano_trust <= 150:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Trust:{/color}{color=#89ad27} high {/color}{color=#282828}([ayano_trust]){/color}{/size}{/font}'
         elif ayano_trust >= 151:
             text '{font=gui/fonts/comicsans.ttf}{size=28}{color=#282828}Trust:{/color}{color=#ff8cb4} lofty {/color}{color=#282828}([ayano_trust]){/color}{/size}{/font}'
     if dialoge == 1:
         imagebutton xpos 1565 ypos 755:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}About urgent{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge1]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}About urgent{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge1]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 1), SetVariable('dialoge', 1), Jump('ayano2')
         imagebutton xpos 1565 ypos 860:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}About romance{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge2]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}About romance{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge2]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 1), SetVariable('dialoge', 4), Jump('ayano2')
         imagebutton xpos 1565 ypos 705:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}About games{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge5]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}About games{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge5]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 1), SetVariable('dialoge', 3), Jump('ayano2')
         imagebutton xpos 1565 ypos 810:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}About study{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge3]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}About study{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge3]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 1), SetVariable('dialoge', 2), Jump('ayano2')
         imagebutton xpos 1565 ypos 910:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}About erotica{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}About erotica{/u}{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 1), SetVariable('dialoge', 5), Jump('ayano2')
         if student_soviet_progress <= 100:
             if dialoge_club == 0:
                 imagebutton xpos 1565 ypos 960:
                     idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Club development?{/color}{/size}{/font}')
                     hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Club development?{/color}{/size}{/font}{/u}')
                     action SetVariable('dialoge', 9), Jump('ayano2')
         elif student_soviet_progress >= 102:
             imagebutton xpos 1565 ypos 960:
                 idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Soda{/color}{/size}{/font}')
                 hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Soda{/color}{/size}{/font}{/u}')
                 action SetVariable('dialoge', 19), Jump('ayano2')
     elif dialoge == 2:
         imagebutton xpos 1565 ypos 705:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Touch{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge6]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Touch{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge6]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 2), SetVariable('dialoge', 6), Jump('ayano2')
         imagebutton xpos 1565 ypos 755:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Hug{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge7]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Hug{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge7]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 2), SetVariable('dialoge', 7), Jump('ayano2')
         imagebutton xpos 1565 ypos 810:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Date{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge8]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Date{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[chance_dialoge8]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 2), SetVariable('dialoge', 8), Jump('ayano2')
         if student_soviet_progress >= 101:
             imagebutton xpos 1565 ypos 860:
                 idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Kiss{/color}{/size}{/font}')
                 hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Kiss{/color}{/size}{/font}{/u}')
                 action SetVariable('old_dialoge', 2), SetVariable('dialoge', 22), Jump('ayano2')
         else:
             imagebutton xpos 1565 ypos 860:
                 idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Kiss {image=icons/icons_block.png}{/color}{/size}{/font}')
                 hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Kiss {image=icons/icons_block.png}{/color}{/size}{/font}{/u}')
                 action SetVariable('old_dialoge', 2), SetVariable('page', 22)
         imagebutton xpos 1565 ypos 915:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=30}{color=#282828}Let is go out! {image=icons/icons_block.png}{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=33}{color=#282828}Let is go out! {image=icons/icons_block.png}{/color}{/size}{/font}{/u}')
             action SetVariable('old_dialoge', 2), SetVariable('page', 22)
     elif dialoge == 3:
         imagebutton xpos 1565 ypos 705:
             idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Flirt {/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=27}[[[flirt_chance]%]{/color}{/size}{/font}')
             hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Flirt{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[flirt_chance]%]{/color}{/size}{/font}')
             action SetVariable('old_dialoge', 3), SetVariable('dialoge', 25), Jump('ayano2')
         if ayano_contact >= 100:
             imagebutton xpos 1565 ypos 755:
                 idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Blow job{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=27} [[[minet_chance]%]{/color}{/size}{/font}')
                 hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Blow job{/u}{/color}{/size}{/font}{color=#808080}{font=gui/fonts/comicsans.ttf}{size=30} [[[minet_chance]%]{/color}{/size}{/font}')
                 action SetVariable('old_dialoge', 3), SetVariable('dialoge', 26), Jump('ayano2')
         else:
             imagebutton xpos 1565 ypos 755:
                 idle Text('{font=gui/fonts/comicsans.ttf}{size=35}{color=#282828}Blow job {image=icons/icons_block.png}{/color}{/size}{/font}')
                 hover Text('{u}{font=gui/fonts/comicsans.ttf}{size=38}{color=#282828}Blow job {image=icons/icons_block.png}{/u}{/color}{/size}{/font}')
                 action SetVariable('old_dialoge', 3)
label storeroom:
     $ gg = 25
     call screen storeroom
screen storeroom:
     if hour <= 3:
         add "character/club/occult/loc/podsobka_night.jpg":
             size(1920, 1080)
     if hour <= 7:
         add "character/club/occult/loc/podsobka_ut.jpg":
             size(1920, 1080)
     elif hour <= 16:
         add "character/club/occult/loc/podsobka_ut.jpg":
             size(1920, 1080)
     elif hour <= 20:
         add "character/club/occult/loc/podsobka_v.jpg":
             size(1920, 1080)
     else:
         add "character/club/occult/loc/podsobka_night.jpg":
             size(1920, 1080)
     if dialoge >= 4:
         $ dialoge = 1
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
             if minet_ayano == 2 or minet_ayano == 4:
                 button:
                     if ayano_contact <= -80:
                         add "gui/system/npc/enemy_idle.png"
                         hover_background "gui/system/npc/enemy_hover.png"
                     elif ayano_contact <= -40:
                         add "gui/system/npc/enemy1_idle.png"
                         hover_background "gui/system/npc/enemy1_hover.png"
                     elif ayano_contact <= 15:
                         add "gui/system/npc/stranger_idle.png"
                         hover_background "gui/system/npc/stranger_hover.png"
                     elif ayano_contact <= 85:
                         add "gui/system/npc/buddy_idle.png"
                         hover_background "gui/system/npc/buddy_hover.png"
                     elif ayano_contact <= 150:
                         add "gui/system/npc/friend_idle.png"
                         hover_background "gui/system/npc/friend_hover.png"
                     elif ayano_contact <= 250:
                         add "gui/system/npc/love_idle.png"
                         hover_background "gui/system/npc/love_hover.png"
                     else:
                         add "gui/system/npc/love1_idle.png"
                         hover_background "gui/system/npc/love1_hover.png"
                     xpadding 0
                     ypadding 0
                     xmargin 5
                     ymargin 5
                     text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Yoshida Ayano{/font}{/size}{/color}"
                     action Jump('ayano_storeroom')
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
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}School club{/font}{/size}{/color}"
                 action Jump('club')
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
screen occult_club_control:
     if hour <= 7:
         add "club_occult_v"
     elif hour <= 16:
         add "club_occult_ut"
     elif hour <= 20:
         add "club_occult_v"
     else:
         add "club_occult_v"
     if dialoge >= 4 or dialoge == 0:
         $ dialoge = 1
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
             if not minet_ayano == 2:
                 if not minet_ayano == 4:
                     button:
                         if ayano_contact <= -80:
                             add "gui/system/npc/enemy_idle.png"
                             hover_background "gui/system/npc/enemy_hover.png"
                         elif ayano_contact <= -40:
                             add "gui/system/npc/enemy1_idle.png"
                             hover_background "gui/system/npc/enemy1_hover.png"
                         elif ayano_contact <= 15:
                             add "gui/system/npc/stranger_idle.png"
                             hover_background "gui/system/npc/stranger_hover.png"
                         elif ayano_contact <= 85:
                             add "gui/system/npc/buddy_idle.png"
                             hover_background "gui/system/npc/buddy_hover.png"
                         elif ayano_contact <= 150:
                             add "gui/system/npc/friend_idle.png"
                             hover_background "gui/system/npc/friend_hover.png"
                         elif ayano_contact <= 250:
                             add "gui/system/npc/love_idle.png"
                             hover_background "gui/system/npc/love_hover.png"
                         else:
                             add "gui/system/npc/love1_idle.png"
                             hover_background "gui/system/npc/love1_hover.png"
                         xpadding 0
                         ypadding 0
                         xmargin 5
                         ymargin 5
                         text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Yoshida Ayano{/font}{/size}{/color}"
                         action Jump('ayano_d')
             for number_npc in range(1, number_npc_max):
                 $ npc_id = 'npc'+str(number_npc)
                 $ location_npc = eval(npc_id)["location_npc"]
                 if location_npc == 'occult_club':
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
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Club Management{/font}{/size}{/color}"
                 action Hide('occult_club_control'), Hide('ayano'), Hide('ayano_cosplay'), SetVariable('page', 1), Show('stats_club_occult')
             if book_guide_occult_club == 0:
                 button:
                     xpadding 0
                     ypadding 0
                     xmargin 5
                     ymargin 5
                     add "gui/system/npc/enemy1_idle.png"
                     hover_background "gui/system/npc/enemy1_hover.png"
                     text "  {color=#000000}{size=22}{font=gui/fonts/alegreya.ttf}Basic management of the club{/font}{/size}{/color}"
                     action Hide('occult_club_control'), Hide('ayano'), Hide('ayano_cosplay'), SetVariable('page', 1), Jump('occult_book_guide')
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
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Backpack of the club{/font}{/size}{/color}"
                 action Jump('storeroom')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Roof{/font}{/size}{/color}"
                 action Jump('roof')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Dining Hall{/font}{/size}{/color}"
                 action Jump('canteen')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Swimming Pool{/font}{/size}{/color}"
                 action Jump('pool')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}School Class{/font}{/size}{/color}"
                 action Jump('class')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}Student Council{/font}{/size}{/color}"
                 action Jump('student_soviet')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}School corridor{/font}{/size}{/color}"
                 action Jump('corridor')
             button:
                 xpadding 0
                 ypadding 0
                 xmargin 5
                 ymargin 5
                 add "gui/system/npc/stranger_idle.png"
                 hover_background "gui/system/npc/stranger_hover.png"
                 text "  {color=#000000}{size=27}{font=gui/fonts/alegreya.ttf}School entrance{/font}{/size}{/color}"
                 action Jump('school')
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
     if rand_ayano == 1 and ayano_contact <= 39:
         $ rand_ayano = renpy.random.randint(3, 8)
     elif rand_ayano == 2 and ayano_contact <= 39:
         $ rand_ayano = renpy.random.randint(3, 8)
     key 'shift_alt_K_F12' action SetVariable("ayano_contact", ayano_contact+10)
     key 'shift_alt_K_F11' action SetVariable("rand_ayano", 1)
label manager_club_occult:
     hide screen afas
     python:
         npc_id = 'name_club_npc_occult'+str(number_npc)
         club_joob = club_complete
         eval(npc_id)["club_joob"] = club_joob
     call screen afas
screen stats_club_occult:
     imagebutton:
         focus_mask True
         idle "gui/club_control/exit_idle.png"
         hover "gui/club_control/exit_hover.png"
         action Hide('stats_club_occult'), Hide('afas'), Jump('club_occult')
     imagebutton xpos -20:
         focus_mask True
         idle "gui/club_control/control_idle.png"
         hover "gui/club_control/control_hover.png"
         action SetVariable('page', 1)
     imagebutton ypos 1:
         focus_mask True
         idle "gui/club_control/stats_idle.png"
         hover "gui/club_control/stats_hover.png"
         action SetVariable('page', 3), Hide('afas')
     imagebutton xpos -22:
         focus_mask True
         idle "gui/club_control/arrangement_idle.png"
         hover "gui/club_control/arrangement_hover.png"
         action SetVariable('page', 2), Hide('afas')
     if page == 3:
         key 'shift_alt_K_F12' action SetVariable("popularity_club_occult", popularity_club_occult+100)
         add "gui/club_control/stats.png"
         text '{font=gui/fonts/alegreya.ttf}{color=#505050}{size=24}Reputation{/size}{/color}{/font}' xpos 620 ypos 835
         text '{font=gui/fonts/alegreya.ttf}{color=#505050}{size=24}Popularity{/size}{/color}{/font}' xpos 620 ypos 860
         text '{font=gui/fonts/alegreya.ttf}{color=#505050}{size=24}New members{/size}{/color}{/font}' xpos 620 ypos 910
         text '{font=gui/fonts/alegreya.ttf}{color=#505050}{size=24}Earned by{/size}{/color}{/font}' xpos 620 ypos 955
         text '{font=gui/fonts/alegreya.ttf}{color=#505050}{size=24}Spent{/size}{/color}{/font}' xpos 620 ypos 980
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}Result{/size}{/color}{/font}' xpos 620 ypos 1030

         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+0 unit.{/size}{/color}{/font}' xpos 1165 ypos 835
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+[global_project_poc3] ед.{/size}{/color}{/font}' xpos 1165 ypos 860
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+0 person{/size}{/color}{/font}' xpos 1135 ypos 910
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}Not available.{/size}{/color}{/font}' xpos 1140 ypos 955
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}Not wasted.{/size}{/color}{/font}' xpos 1130 ypos 980
         if global_project_poc3 == 0:
             text '{font=gui/fonts/alegreya.ttf}{color=#842626}{size=24}FAIL!{/size}{/color}{/font}' xpos 1155 ypos 1030
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#578426}{size=24}SUCCESS!{/size}{/color}{/font}' xpos 1160 ypos 1030


         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+0 unit.{/size}{/color}{/font}' xpos 950 ypos 835
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+[festivale_poc3] ед.{/size}{/color}{/font}' xpos 950 ypos 860
         text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=24}+0 person{/size}{/color}{/font}' xpos 915 ypos 910
         if festivale_poc4 >= 1000:
             text '{font=gui/fonts/alegreya.ttf}{color=#578426}{size=24}+[festivale_poc4] к.{/size}{/color}{/font}' xpos 935 ypos 955
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#578426}{size=24}+[festivale_poc4] к.{/size}{/color}{/font}' xpos 955 ypos 955
         text '{font=gui/fonts/alegreya.ttf}{color=#842626}{size=24}-0 c.{/size}{/color}{/font}' xpos 955 ypos 980
         if festivale_poc3 == 0:
             text '{font=gui/fonts/alegreya.ttf}{color=#842626}{size=24}FAIL!{/size}{/color}{/font}' xpos 935 ypos 1030
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#578426}{size=24}SUCCESS!{/size}{/color}{/font}' xpos 940 ypos 1030
         $ myarr = [popularity_basketball, popularity_pool, popularity_club_occult, popularity_athletics, popularity_art, popularity_science, popularity_literature, popularity_drama, popularity_detective, popularity_journalism]
         $ e = sorted(myarr, reverse=True)
         vbox xpos 620 ypos 230:
             spacing 10
             for number_npc in e:
                 hbox:
                     if number_npc == popularity_basketball:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Basketball Club{/size}{/color}{/font}' ypos 2
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 108 ypos 2
                         if popularity_basketball_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=26}[number_npc] {/color}{color=#282828}({/color}{color=#578426}▲ [popularity_basketball_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 138 ypos 2
                         elif popularity_basketball_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=26}[number_npc] {/color}{color=#282828}({/color}{color=#842626}▼ [popularity_basketball_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 138 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#323232}{size=26}[number_npc] {/color}{color=#282828}([popularity_basketball_poc]) оп{/size}{/color}{/font}' xpos 138 ypos 2
                     elif number_npc == popularity_pool:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Swimming Club{/size}{/color}{/font}' ypos 5
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 175 ypos 5
                         if popularity_pool_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_pool_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 205 ypos 2
                         elif popularity_pool_poc <= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_pool_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 205 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_pool_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 205 ypos 2
                     elif number_npc == popularity_club_occult:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Occultism Club{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 136
                         if popularity_club_occult_poc2 >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_club_occult_poc2]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 166 ypos 2
                         elif popularity_club_occult_poc2 <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_club_occult_poc2]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 166 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_club_occult_poc2]){/size}{size=23} оп{/size}{/color}{/font}' xpos 166 ypos 2
                     elif number_npc == popularity_athletics:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Athletics Club{/size}{/color}{/font}' ypos 3
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 92 ypos 3
                         if popularity_athletics_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_athletics_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 122 ypos 2
                         elif popularity_athletics_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_athletics_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 122 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_athletics_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 122 ypos 2
                     elif number_npc == popularity_art:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Art Club{/size}{/color}{/font}' ypos 1
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 86 ypos 1
                         if popularity_art_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_art_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 116 ypos 2
                         elif popularity_art_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_art_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 116 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_art_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 116 ypos 2
                     elif number_npc == popularity_science:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Natural History Club{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 101
                         if popularity_science_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_science_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 131 ypos 2
                         elif popularity_science_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_science_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 131 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_science_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 131 ypos 2
                     elif number_npc == popularity_literature:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Literary Club{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 121
                         if popularity_literature_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_literature_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 151 ypos 2
                         elif popularity_literature_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_literature_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 151 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_literature_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 151 ypos 2
                     elif number_npc == popularity_drama:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Drama and Comedy Club{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 83
                         if popularity_drama_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_drama_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 113 ypos 2
                         elif popularity_drama_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_drama_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 113 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_drama_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 113 ypos 2
                     elif number_npc == popularity_detective:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Detective Club{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 130
                         if popularity_detective_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_detective_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 160 ypos 2
                         elif popularity_detective_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_detective_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 160 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_detective_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 160 ypos 2
                     elif number_npc == popularity_journalism:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Club of Journalism{/size}{/color}{/font}'
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 114
                         if popularity_journalism_poc >= 1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#578426}▲ [popularity_journalism_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 144 ypos 2
                         elif popularity_journalism_poc <= -1:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ({/color}{color=#842626}▼ [popularity_journalism_poc]{/color}{color=#282828}){/size}{size=23} оп{/size}{/color}{/font}' xpos 144 ypos 2
                         else:
                             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=26}[number_npc] ([popularity_journalism_poc]){/size}{size=23} оп{/size}{/color}{/font}' xpos 144 ypos 2
     elif page == 2:
         add "gui/club_control/arrangement.png"
         add "gui/club_control/budzhet_info.png"
         text '{font=gui/fonts/ubuntu.ttf}{color=#282828}[budget_club_occult] к.{/color}{/font}' xalign 0.725 yalign 0.22
         vpgrid:
             cols 1
             rows 1
             spacing -1665
             child_size (1125, 0)
             xpos 600 ypos 225 xysize (1125, 850)
             draggable True
             mousewheel True
             arrowkeys True
             scrollbars "vertical"
             vbox:
                 add "gui/club_control/icons/microwave_osn.png" ypos 0 xpos 1
                 add "gui/club_control/icons/poster.png" ypos 0 xpos 1
                 add "gui/club_control/icons/refrigerator.png" ypos 0 xpos 1
                 add "gui/club_control/icons/playstation.png" ypos 0 xpos 1
                 add "gui/club_control/icons/furniture.png" ypos 0 xpos 1
                 add "gui/club_control/icons/tablet.png" ypos 0 xpos 1
                 add "gui/club_control/icons/camera.png" ypos 0 xpos 1
                 add "gui/club_control/icons/vacuum.png" ypos 0 xpos 1
                 add "gui/club_control/icons/tablet_painting.png" ypos 0 xpos 1
             button ypos -85 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if microwave == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}10000 к.{/size}{/color}{/font}" ypos 4 xpos 0
                     if budget_club_occult >= 10000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('microwave', 1), SetVariable('budget_club_occult', budget_club_occult-10000)
             button ypos 20 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if poster == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}1500 с.{/size}{/color}{/font}" ypos 4 xpos 5
                     if budget_club_occult >= 1500:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('poster', 1), SetVariable('budget_club_occult', budget_club_occult-1500)
             button ypos 125 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if refrigerator == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}5000 с.{/size}{/color}{/font}" ypos 4 xpos 5
                     if budget_club_occult >= 5000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('refrigerator', 1), SetVariable('budget_club_occult', budget_club_occult-5000)
             button ypos 230 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if playstation == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}7000 с.{/size}{/color}{/font}" ypos 4 xpos 5
                     if budget_club_occult >= 7000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('playstation', 1), SetVariable('budget_club_occult', budget_club_occult-7000)
             button ypos 335 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if furniture == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}8000 с.{/size}{/color}{/font}" ypos 4 xpos 5
                     if budget_club_occult >= 8000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('furniture', 1), SetVariable('budget_club_occult', budget_club_occult-8000)
             button ypos 440 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if tablet == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}9000 с.{/size}{/color}{/font}" ypos 4 xpos 5
                     if budget_club_occult >= 9000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('tablet', 1), SetVariable('budget_club_occult', budget_club_occult-9000)
             button ypos 545 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if camera == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}10000 с.{/size}{/color}{/font}" ypos 4 xpos 0
                     if budget_club_occult >= 10000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('camera', 1), SetVariable('budget_club_occult', budget_club_occult-10000)
             button ypos 650 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if vacuum == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}12000 с.{/size}{/color}{/font}" ypos 4 xpos 0
                     if budget_club_occult >= 12000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('vacuum', 1), SetVariable('budget_club_occult', budget_club_occult-12000)
             button ypos 755 xpos 480:
                 xpadding 0
                 ypadding 0
                 xmargin 0
                 if tablet_painting == 0:
                     hover_background "gui/club_control/icons/buy_hover.png"
                     add "gui/club_control/icons/buy_idle.png"
                     textbutton "{font=gui/fonts/ubuntu.ttf}{color=#282828}{size=18}15000 с.{/size}{/color}{/font}" ypos 4 xpos 0
                     if budget_club_occult >= 15000:
                         idle_background "gui/club_control/icons/buy_idle.png"
                         action SetVariable('tablet_painting', 1), SetVariable('budget_club_occult', budget_club_occult-15000)
         imagebutton:
             focus_mask True
             idle "gui/club_control/exit_idle.png"
             hover "gui/club_control/exit_hover.png"
             action Hide('stats_club_occult'), Hide('afas'), Jump('club_occult')
         imagebutton xpos -20:
             focus_mask True
             idle "gui/club_control/control_idle.png"
             hover "gui/club_control/control_hover.png"
             action SetVariable('page', 1)
         imagebutton ypos 1:
             focus_mask True
             idle "gui/club_control/stats_idle.png"
             hover "gui/club_control/stats_hover.png"
             action SetVariable('page', 3), Hide('afas')
         imagebutton xpos -22:
             focus_mask True
             idle "gui/club_control/arrangement_idle.png"
             hover "gui/club_control/arrangement_hover.png"
             action SetVariable('page', 2), Hide('afas')
     elif page == 1:
         add "gui/club_control/ui_osn.png"
         $ authority_club_occult_poc1 = 0
         $ purity_club_occult_poc1 = 0
         $ global_project_poc1 = 0
         $ festivale_poc1 = 0
         $ popularity_club_occult_poc1 = 0
         default tt = Tooltip ("")
         vpgrid:
             cols 1
             rows number_occult_club
             spacing -1952
             child_size (600, 2000)
             xpos 600 ypos 225 xysize (630, 465)
             draggable True
             mousewheel True
             arrowkeys True
             if number_occult_club >= 9:
                 scrollbars "vertical"
             python:
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
             button:
                 xpadding 30
                 ypadding 9
                 xmargin 0
                 if dialoge == 0:
                     idle_background "gui/club_control/hover_list.png"
                 hover_background "gui/club_control/hover_list.png"
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Ayano Yoshida{/size}{/color}{/font}'
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}'  xpos 260
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Lounging{/size}{/color}{/font}'  xpos 295
                 action SetVariable('dialoge', 0)
             for number_npc in range(3, number_occult_club+1):
                 python:
                     npc_id = 'name_club_npc_occult'+str(number_npc)
                     v_npc = eval(npc_id)["pich_npc"]
                     gender_npc = eval(npc_id)["gender_npc"]
                     contact_npc = eval(npc_id)["contact_npc"]
                     love_npc = eval(npc_id)["love_npc"]
                     fear_npc = eval(npc_id)["fear_npc"]
                     name_npc = eval(npc_id)["npc_name"]
                     club_joob = eval(npc_id)["club_joob"]
                     perk = eval(npc_id)["perk"]
                     club_joob112413412 = 'club_joob'+str(number_npc-2)
                     setattr(store, club_joob112413412, club_joob)
                 button:
                     xpadding 30
                     ypadding 9
                     xmargin 0
                     if dialoge == number_npc-2:
                         idle_background "gui/club_control/hover_list.png"
                     hover_background "gui/club_control/hover_list.png"
                     text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}[name_npc]{/size}{/color}{/font}'
                     text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}:{/size}{/color}{/font}' xpos 260
                     if club_joob == 1:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Writes articles{/size}{/color}{/font}' xpos 295
                     elif club_joob == 2:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Removable{/size}{/color}{/font}' xpos 295
                     elif club_joob == 3:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Getting ready for the festival{/size}{/color}{/font}' xpos 295
                     elif club_joob == 4:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}He is working on a project{/size}{/color}{/font}' xpos 295
                     elif club_joob == 5:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Lounging{/size}{/color}{/font}' xpos 295
                     elif club_joob == 6:
                         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Search for newcomers{/size}{/color}{/font}' xpos 295
                     hovered SetVariable('random', perk), tt.Action ("Hint")
                     action SetVariable('dialoge', number_npc-2), SetVariable('number_npc', number_npc), SetVariable('club_complete', 0), SetVariable('club_joob', club_joob), Show('afas')
                 python:
                     if club_joob == 5:
                         if perk == 'Lazy':
                             authority_club_occult_poc1 += 0.2
                         authority_club_occult_poc1 += 0.3
                     elif club_joob == 4:
                         if perk == 'Single':
                             if global_project_human <= 2:
                                 global_project_poc1 += 2
                             else:
                                 global_project_poc1 -= 1
                         elif perk == 'Team':
                             if global_project_human >= 3:
                                 global_project_poc1 += 2
                             else:
                                 global_project_poc1 -= 1
                         if camera == 1:
                             global_project_poc1 += 1
                         if perk == 'Endeavour':
                             global_project_poc1 += 2
                         if perk == 'Sleepy':
                             global_project_poc1 -= 2
                         if perk == 'Fountain of ideas':
                             authority_club_occult_poc1 += 1.5
                         elif perk == 'Faithful':
                             authority_club_occult_poc1 += 0.6
                         authority_club_occult_poc1 -= 1.5
                         global_project_poc1 += 3
                     elif club_joob == 3:
                         if perk == 'Single':
                             if festivale_human <= 2:
                                 festivale_poc1 += 2
                             else:
                                 festivale_poc1 -= 1
                         elif perk == 'Team ':
                             if festivale_human >= 3:
                                 festivale_poc1 += 2
                             else:
                                 festivale_poc1 -= 1
                         if perk == 'Endeavour':
                             festivale_poc1 += 1
                         if perk == 'Sleepy':
                             festivale_poc1 -= 2
                         if perk == 'Fountain of ideas':
                             authority_club_occult_poc1 += 0.5
                         elif perk == 'Faithful':
                             authority_club_occult_poc1 += 0.1
                         authority_club_occult_poc1 -= 0.5
                         festivale_poc1 += 4
                     elif club_joob == 2:
                         if perk == 'Single':
                             if purity_human <= 2:
                                 purity_club_occult_poc1 += 10
                             else:
                                 purity_club_occult_poc1 += 2
                         elif perk == 'Team':
                             if purity_human <= 2:
                                 purity_club_occult_poc1 += 10
                             else:
                                 purity_club_occult_poc1 += 2
                         if perk == 'Sleepy':
                             purity_club_occult_poc1 -= 6
                         if perk == 'Cleaning':
                             purity_club_occult_poc1 += 10
                         if perk == 'Fountain of ideas':
                             authority_club_occult_poc1 += 0.3
                         elif perk == 'Faithful':
                             authority_club_occult_poc1 += 0.1
                         authority_club_occult_poc1 -= 0.3
                         purity_club_occult_poc1 += 10
                         if perk == 'Nerja':
                             purity_club_occult_poc1 -= 10
                     elif club_joob == 1:
                         if perk == 'Single':
                             if articles_human <= 2:
                                 popularity_club_occult_poc1 += 3
                             else:
                                 popularity_club_occult_poc1 -= 1
                         elif perk == 'Team':
                             if articles_human >= 3:
                                 popularity_club_occult_poc1 += 2
                             else:
                                 popularity_club_occult_poc1 -= 1
                         if tablet == 1:
                             popularity_club_occult_poc1 += 1
                         if tablet_painting == 1:
                             popularity_club_occult_poc1 += 2
                         if perk == 'Quickly prints':
                             popularity_club_occult_poc1 += 1
                         if perk == 'Sleepy':
                             popularity_club_occult_poc1 -= 1
                         popularity_club_occult_poc1 += 2
                         if perk == 'Fountain of ideas':
                             authority_club_occult_poc1 += 0.4
                         elif perk == 'Faithful':
                             authority_club_occult_poc1 += 0.1
                         authority_club_occult_poc1 -= 0.4
                     elif club_joob == 6:
                         if perk == 'Single':
                             if articles_human <= 2:
                                 find_human_club_occult_poc += 2
                             else:
                                 find_human_club_occult_poc -= 1
                         elif perk == 'Team':
                             if articles_human >= 3:
                                 find_human_club_occult_poc += 1
                             else:
                                 find_human_club_occult_poc -= 1
                         if perk == 'Sleepy':
                             find_human_club_occult_poc -= 1
                         find_human_club_occult_poc += 2
                         if perk == 'Fountain of ideas':
                             authority_club_occult_poc1 += 0.4
                         elif perk == 'Loyal':
                             authority_club_occult_poc1 += 0.1
                         authority_club_occult_poc1 -= 0.4
                     if perk == 'Nerja':
                         purity_club_occult_poc1 -= 10
                     authority_club_occult_poc1 = authority_club_occult_poc1
                     popularity_club_occult_poc1 = popularity_club_occult_poc1
                     festivale_poc1 = festivale_poc1
                     find_human_club_occult_poc = find_human_club_occult_poc
                     purity_club_occult_poc1 = purity_club_occult_poc1
             for number_npc in range(1, 50):
                 button:
                     xpadding -100
                     ypadding 0
                     xmargin -100
                     ymargin 5
                     add 'gui/backpack/backpack.png' xpos -500:
                         size(1500, 500)
                     action SetVariable('random', 0)
         python:
             find_human_club_occult_poc1 = find_human_club_occult_poc + popularity_club_occult / 100
             find_human_club_occult_poc = 0
             find_human_club_occult_poc1 = int(find_human_club_occult_poc1)
             festivale_poc = int(festivale_poc1)
             global_project_poc = int(global_project_poc1)
             global_project_poc1 = 0
             festivale_poc1 = 0
             if microwave == 1:
                 popularity_club_occult_poc1 += 0.2
             if poster == 1:
                 authority_club_occult_poc1 += 0.2
             if refrigerator == 1:
                 popularity_club_occult_poc1 += 0.3
                 authority_club_occult_poc1 += 0.2
             if playstation == 1:
                 popularity_club_occult_poc1 += 0.8
                 authority_club_occult_poc1 -= 0.2
             if furniture == 1:
                 authority_club_occult_poc1 += 0.8
             if vacuum == 1:
                 purity_club_occult_poc1 += 25
             purity_club_occult_poc = int(purity_club_occult_poc1 - 10)
             purity_club_occult_poc1 = 0
             authority_club_occult_poc = round((stats_authority_gg_info / 4) / 7 + authority_club_occult_poc1, 3)
             authority_club_occult_poc1 = 0
             popularity_club_occult_poc = round((purity_club_occult / 10) + popularity_club_occult_poc1, 3)
             popularity_club_occult_poc1 = 0
             popularity_club_occult1212 = round(popularity_club_occult, 2)
             authority_club_occult1212 = round(authority_club_occult, 2)
         if authority_club_occult_poc <= 0:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Reputation: [authority_club_occult1212] ([authority_club_occult_poc]{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.86
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Reputation: [authority_club_occult1212] (+[authority_club_occult_poc]{/size}{size=20}per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.86
         if popularity_club_occult_poc <= 0:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Popularity of the club: [popularity_club_occult1212] ([popularity_club_occult_poc]{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.89
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Popularity of the club: [popularity_club_occult1212] (+[popularity_club_occult_poc]{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.89
         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Number of participants: [number_occult_club]{/size}{/color}{/font}' xpos 875 yalign 0.95
         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Ready for the festival: [festivale]% (+[festivale_poc]%{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.76
         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Project Ready: [global_project]% (+[global_project_poc]%{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.79
         if purity_club_occult_poc >= 1:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Cleanliness of the club room: [purity_club_occult]% (+[purity_club_occult_poc]%{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.73
         else:
             text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Cleanliness of the club room: [purity_club_occult]% ([purity_club_occult_poc]%{/size}{size=20} per day{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.73

         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Possible new club member: [find_human_club_occult_poc1]%{/size}{/color}{/font}' xpos 875 yalign 0.7
         text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Budget: [budget_club_occult] (+[budget_club_occult_plus] per week{/size}{size=24}){/size}{/color}{/font}' xpos 875 yalign 0.92
     if tt.value != "":
         $ (x, y) = renpy.get_mouse_pos ()
         if random == 'School celebrity':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.1)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 25 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#448200}{size=24}+40{/size}{/color}{/font}{color=#282828}{size=24}{font=gui/fonts/alegreya.ttf} popularity for{/size}{/color}{/font}' xpos 40 ypos 43
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}club membership{/size}{/color}{/font}' xpos 60 ypos 75
         elif random == 'Lean':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(715, 120)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Lean{/size}{/font}' xpos 250 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#448200}{size=24}+50% {/size}{/font}{/color}{color=#282828}{font=gui/fonts/alegreya.ttf}{size=24}and more from the amount that was invested in the training,{/size}{/color}{/font}' xpos 5 ypos 42
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}comes back after the project/festival.{/size}{/color}{/font}' xpos 40 ypos 75
         elif random == 'Nerja':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.1):
                     size(480, 120)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Неряха{/size}{/font}' xpos 180 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}While this member is at the club,{/size}{/color}{/font}' xpos 10 ypos 45
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}the room gets polluted faster.{/size}{/color}{/font}' xpos 55 ypos 75
         elif random == 'Lazy':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.1)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 115 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}At the end of the day, it is dropped{/size}{/color}{/font}' xpos 20 ypos 42
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}idling activities{/size}{/color}{/font}' xpos 23 ypos 73
         elif random == 'Loyal':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.15)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 130 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Requires 25% less points.{/size}{/color}{/font}' xpos 10 ypos 45
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}authority to work{/size}{/color}{/font}' xpos 50 ypos 77
         elif random == 'Fountain of ideas':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 110 ypos 11
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}To work for this participant{/size}{/color}{/font}' xpos 10 ypos 50
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}no need for points of authority{/size}{/color}{/font}' xpos 40 ypos 87
         elif random == 'Endeavour':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 95 ypos 11
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Project ready:{/color}{color=#448200} +2%{/size}{/color}{/font}' xpos 40 ypos 47
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}In readiness for the festival:{/color}{color=#448200} +1%{/size}{/color}{/font}' xpos 10 ypos 83
         elif random == 'Quickly prints':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(620, 140)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 25 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Increases the popularity points obtained{/size}{/color}{/font}' xpos 10 ypos 50
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}for writing articles on{/color}{color=#448200} +50%{/size}{/color}{/font}' xpos 60 ypos 87
         elif random == 'Sleepy':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 140 ypos 12
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Received points are reduced{/size}{/color}{/font}' xpos 5 ypos 50
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}for any activity on{/color}{color=#9a0000} -60%{/size}{/color}{/font}' xpos 10 ypos 85
         elif random == 'Single':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(550, 140)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Single{/size}{/font}' xpos 200 ypos 12
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}If a club member works alone, the glasses{/size}{/color}{/font}' xpos 10 ypos 50
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}for any activity are increased by{/color}{color=#448200} +75%{/size}{/color}{/font}' xpos 5 ypos 85
         elif random == 'Team':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(720, 140)
                     text '{font=gui/fonts/alegreya.ttf}{size=24}Team{/size}{/font}' xpos 280 ypos 12
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}If a club member works with three or more members,{/size}{/color}{/font}' xpos 10 ypos 53
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}points for any activity are increased by{/color}{color=#448200} +75%{/size}{/color}{/font}' xpos 70 ypos 86
         elif random == 'Stand alone':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(470, 120)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Stand alone{/size}{/font}' xpos 115 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}If the participant is idling, he is{/size}{/color}{/font}' xpos 20 ypos 43
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}call the shots{/size}{/color}{/font}' xpos 5 ypos 74
         elif random == 'Avid player':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.25):
                     size(580, 120)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Avid player{/size}{/font}' xpos 200 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}If there is a game console in the club, then the member{/size}{/color}{/font}' xpos 10 ypos 45
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}will occasionally be idling.{/size}{/color}{/font}' xpos 70 ypos 75
         elif random == 'Symbiosis':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.1)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}Symbiosis{/size}{/font}' xpos 115 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#9a0000}{size=24}-40{/size}{/color}{/font}{color=#282828}{font=gui/fonts/alegreya.ttf}{size=24} popularity for{/size}{/color}{/font}' xpos 40 ypos 45
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}club membership{/size}{/color}{/font}' xpos 60 ypos 75
         elif random == 'Cleaning':
             button xpos x ypos y:
                 add im.Rotozoom('gui/club_control/character_npc.png', 0, 1.1):
                     size(390, 120)
                 text '{font=gui/fonts/alegreya.ttf}{size=24}[random]{/size}{/font}' xpos 130 ypos 10
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}Cleaning the club room:{/color}{color=#448200} +50%{/size}{/color}{/font}' xpos 10 ypos 39
                 text '{font=gui/fonts/alegreya.ttf}{color=#282828}{size=24}and more.{/size}{/color}{/font}' xpos 140 ypos 75
screen character_npc:
     python:
         npc_id = 'name_club_npc_occult'+str(number_npc)
         perk = eval(npc_id)["perk"]
screen afas:
     python:
         npc_id = 'name_club_npc_occult'+str(number_npc)
         club_joob = eval(npc_id)["club_joob"]
     imagebutton xpos 590 ypos 730:
         if club_joob == 1:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Write articles{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Write articles{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Write articles{/u}{/size}{/color}{/font}')
         if authority_club_occult >= 0.1:
             action SetVariable('club_complete', 1), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
     imagebutton xpos 590 ypos 765:
         if club_joob == 2:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Cleaning the room.{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Cleaning the room.{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Cleaning the room.{/u}{/size}{/color}{/font}')
         if authority_club_occult >= 0.1:
             action SetVariable('club_complete', 2), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
     imagebutton xpos 590 ypos 800:
         if club_joob == 3:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Get ready for the festival{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Get ready for the festival{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Get ready for the festival{/u}{/size}{/color}{/font}')
         if authority_club_occult >= 0.1:
             action SetVariable('club_complete', 3), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
     imagebutton xpos 590 ypos 833:
         if club_joob == 4:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Work on a project{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Work on a project{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Work on a project{/u}{/size}{/color}{/font}')
         if authority_club_occult >= 0.1:
             action SetVariable('club_complete', 4), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
     imagebutton xpos 590 ypos 867:
         if club_joob == 6:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Searching for people{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Searching for people{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Searching for people{/u}{/size}{/color}{/font}')
         action SetVariable('club_complete', 6), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
     imagebutton xpos 590 ypos 901:
         if club_joob == 5:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Rest{/u}{/size}{/color}{/font}')
         else:
             idle Text('{font=gui/fonts/alegreya.ttf}{color=505050}{size=22}Rest{/size}{/color}{/font}')
             hover Text('{font=gui/fonts/alegreya.ttf}{color=#373737}{size=22}{u}Rest{/u}{/size}{/color}{/font}')
         action SetVariable('club_complete', 5), SetVariable('number_npc', number_npc), Jump('manager_club_occult')
label ayano1:
     if hour <= 7:
         scene club_occult_v
     elif hour <= 16:
         scene club_occult_ut
     elif hour <= 20:
         scene club_occult_v
     else:
         scene club_occult_v
     "When you thought it was the right decision to see what Ayano was doing, you threw your business away and turned your gaze on your slacker."
     if rand_ayano == 0:
         "But... Since last time, nothing has changed in the girl's actions."
         call screen occult_club_control
     elif rand_ayano == 1:
         show ayano g33
         ayanogg1 "STUPID GAME!" with vpunch
         "It looks like Ayano was defeated in her next toy, which is why she hit her portable console on the table. And how does a poor console only withstand such blows?"
         show ayano g25
         ayanogg1 "Извини! Я случайно!"
         "Apologizing girl in front of the console... The view is stupid enough, but funny. All it takes is popcorn to fully enjoy the spectacle."
         show ayano g29
         "Noticing she was being watched, the girl threw her eyes at you and was clearly surprised at this turn of events."
         show ayano g26
         ayanogg1 "You know, stalkers are not liked in this country, so be careful."
         $ rand_ayano = 0
         hide ayano
         call screen occult_club_control
     elif rand_ayano == 2:
         "The girl just sat there and enthusiastically wrote something down in her notebook while peacefully shaking her legs like a little kid. Apparently, she was doing her homework. At least that's what the open books on the table next to her were talking about."
         $ rand_ayano = 0
         call screen occult_club_control
     elif rand_ayano == 3 or rand_ayano == 4:
         "The girl, lying relaxed in a chair, waved her legs from idleness, which is why her skirt sometimes rose strongly, opening up a view of most of her hip. Not enjoying the view for long, you soon turned your back, hoping for a sudden thing."
         if hentai_patch_inicial == True:
             $ depravity_ayano += 1
             "{color=#BC8F8F}{b}The girl's depravity has increased slightly!{/b}{/color}"
         $ rand_ayano = 0
         call screen occult_club_control
     elif rand_ayano == 5:
         "The peacefully sleeping girl was delighted with her sweet eyes. Soon she seemed to be completely defenseless, again will be abnormal and too energetic in their actions. It's ironic enough..."
         $ rand_ayano = 0
         call screen occult_club_control
     else:
         jump club_occult
label ayano2:
     if hour <= 7:
         scene club_occult_v
     elif hour <= 16:
         scene club_occult_ut
     elif hour <= 20:
         scene club_occult_v
     else:
         scene club_occult_v
     show ayano g35
     $ minute += renpy.random.randint(26, 35)
     $ energy -= 4
     if dialoge == 1:
         "Having decided that your best pastime was to communicate with your new friend, you sat down close to her, falling with your fifth dot on a chair, and began a dialogue about what was important. Soon, thirty minutes later, you ended the conversation, starting to do each of your own things."
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge1 >= 100:
             $ chance_dialoge1 = 100
         if chance_dialoge <= chance_dialoge1:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if chance_dialoge <= chance_dialoge1 / 1.4:
                 "When you talked to the girl, you showed maximum eloquence, which is why the dialogue was just fine. Ayano and you had a great time and got to know each other quite well in those thirty minutes."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 2
             else:
                 show ayano g32
                 $ ayano_dialoge += 1
                 $ ayano_contact += 1
                 "Having found a point of contact, your dialogue went quite well, not to mention some embarrassing moments. In general, even the girl liked such a pastime, so it can be called a kind of success."
                 "But the main thing is that you got your award: a nice smile of a girl, and her improved opinion about you."
             "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
         else:
             show ayano g34
             "The dialogue that was held was successful with a stretch, but it wasn't exactly the limit of a successful pastime. At least that's what the disgruntled face of the girl was talking about."
             $ ayano_dialoge += 1
             $ ayano_contact -= 1
     elif dialoge == 2:
         "Having decided that the best topic to talk to Ayano is the school topic, you started to tell her about different innovations in schools by the Ministry of Defense and other things, which are simply not interesting to many people".
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge3 >= 100:
             $ chance_dialoge3 = 100
         if chance_dialoge <= chance_dialoge3:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if chance_dialoge <= chance_dialoge3 / 1.4:
                 "Although such a topic is obviously not interesting to the girl, but she is interested in your company, literally uplifting. It seemed that no matter how crazy you talk, she'd listen to you and nod rather."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 1
                 "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
             else:
                 show ayano g34
                 "No matter how hard you try to get the girl interested, it didn't work out. "It seemed that she wasn't made for study, but for the fun she was so lacking now..."
                 "In any case, all this dialogue reached its climax, because the girl fell asleep on the floor, and you never got anything but a long monologue from your side, which Ayano was clearly not interested in."
                 $ ayano_dialoge += 1
         else:
             "It seemed like her pretty face wouldn't change anything, but as soon as you opened your mouth about school, a plastic cup flew into you, clearly filled with something before the throw."
             show ayano g36
             "I don't think this kind of pastime can be called a good one, but still you got yours: the happy and illuminating face of a girl, combined with her ringing but pleasant laughter, created a pleasant atmosphere in the club room."
             $ ayano_dialoge += 1
             $ ayano_contact += 1
             "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
     elif dialoge == 3:
         "Realizing that the best topic to talk to Ayano is the game theme, you started discussing novelties, classic games and more."
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge5 >= 100:
             $ chance_dialoge5 = 100
         if chance_dialoge <= chance_dialoge5:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if chance_dialoge <= chance_dialoge5 / 1.4:
                 "Realizing that it is not the topic of dialogue, but your company, that the girl is more pleasant, you immediately began to move on personal topics, the result of which immediately made itself known."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 3
                 $ ayano_trust += 1
                 "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
             else:
                 "From the very beginning of the dialogue, it was doomed to success, which is why you slowly moved on to more personal topics that were accompanied by mutual compliments."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 2
                 "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
         else:
             "In the end, even without knowing the girl, you found a common point of contact and had a rather pleasant dialogue about games, which soon ended on a pleasant note."
             $ ayano_dialoge += 1
             $ ayano_contact += 1
             "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
     elif dialoge == 4:
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge2 >= 100:
             $ chance_dialoge2 = 100
         if chance_dialoge <= chance_dialoge2:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if chance_dialoge <= chance_dialoge2 / 1.4:
                 show ayano g22
                 "The girl's purple cheeks showed she was finally taking your romantic monologue seriously. Well, or she just got sick in a stuffy room..."
                 "Either way, the conversation went well enough and you and Ayano have made good progress in your relationship."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 1
                 $ ayano_trust += 1
                 "{color=#BC8F8F}{b}The girl's relationship and trust have improved!{/b}{/color}"
             else:
                 "I don't think your exertions are any good... All the time Ayano just waved her legs, sitting in a chair like a little child, and shook her head, trying to pretend she was interested in a subject like this."
                 "Even though this is hardly a success, the girl's hips were always open to your eyes, and a beautiful body always pleases your eyes. "You received an award, though not the one you wanted."
                 $ ayano_dialoge += 1
                 $ ayano_contact += 1
                 "{color=#BC8F8F}{b}Relationships with the girl have improved!{/b}{/color}"
         else:
             show ayano g37
             "As much as you try to put the monologue into a dialogue, nothing came out. Everything was in vain, and it seemed that the girl was not only interested in romance, but also in your speech, from which it was becoming boring, as talked about by her constant yawns."
             "After a long monologue on your part, Ayano passed out, putting her head on the desk and closing her eyes. "It seems that the conversation was the most unfortunate."
             $ ayano_dialoge += 1
             $ ayano_sleep = True
             $ rand_ayano = 5
     elif dialoge == 5:
         "This function is being tested."
     elif dialoge == 6:
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge6 >= 100:
             $ chance_dialoge6 = 100
         if chance_dialoge <= chance_dialoge6:
             "Looking at Ayano, a sudden thought came to you: I want to pet her! Having stretched your palm to the top of the head of nothing unsuspecting, you mussed your hair with your sharp movements. Even though it came out rather crudely, you finally satisfied your undying desires, which once upon a time will manifest themselves."
             "As soon as you put your hand on the girl's head, the girl became charmed, but a second later she came to her senses and went on with her business as if nothing had happened. She seems to have started to like your touching, but who knows what can happen if you hurry up?"
             $ ayano_dialoge += 1
             $ ayano_contact += 3
             $ ayano_trust += 2
             "{color=#BC8F8F}{b}The girl's relationship and trust have improved!{/b}{/color}"
         else:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if chance_dialoge <= chance_dialoge6:
                 "Looking at Ayano, a sudden thought came to you: I want to pet her! Having stretched your palm to the top of the head of nothing unsuspecting, you mussed your hair with your sharp movements. Even though it came out roughly enough, you've finally satisfied your undying desires, which once upon a time will manifest themselves."
                 show ayano g33
                 ayanogg1 "Hey, what are you doing?"
                 "With an even sharper move, the girl took your hand off her top, then turned in your direction, disgruntled by the piercing look."
                 ayanogg1 "Why are you touching my top, you pervert?!"
                 "Dissatisfied face of the girl, and her words made it clear that such an act on your part, she does not like, and you need to keep your distance from her. Is it possible that you were too hasty with body contact?"
                 ayanogg1 "Silent? Fine!"
                 $ ayano_perception = 0
                 "And even though the inflated cheeks of your target said she wasn't happy, you were relatively happy with the result. In the end, Ayano seemed to take it as a joke, so there won't be any more problems with it because you're quick."
             else:
                 "Looking at Ayano, a sudden thought came to you: I want to pet her! Having stretched her palm to the top of the head, as it seemed to you, nothing unattractive, you found yourself in a rather unpleasant position: in just a second Ayano turned to you and began to burn with her gaze, looking at you with disgust".
                 show ayano g33
                 "It seems that this time she seriously considered this act of harassment, but still did not say anything, and what is there to say if the face and look all clear?"
                 glgg "Uh... I'm sorry?"
                 "The words squeezed out of you clearly didn't calm the girl down, but this time they let you go in peace. Turned away from your annoying face, Ayano went on with her business."
                 $ ayano_dialoge -= 3
                 $ ayano_contact -= 2
                 "{color=#BC8F8F}{b}Relationships with the girl have deteriorated!{/b}{/color}"
     elif dialoge == 7:
         "Looking at your energetic female comrade, you were seized by a strong desire to hug him, why you came to nothing unsuspecting purpose and, as it never happened, fulfilled your desire by hugging him."
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge7 >= 100:
             $ chance_dialoge7 = 100
         if chance_dialoge <= chance_dialoge7:
             hide ayano
             scene image "character/club/occult/npc/faceless/1.jpg" with dissolve
             "But... The expected slap and threat to life from your goal did not follow. Ayano just turned in your far-fetched hug to the opposite side and hugged you back, which was simply a pleasant surprise for you."
             "The short hug was soon interrupted, after which the girl continued to do her business, thanking you for the recent one, to which you nodded approvingly and followed Ayano's example."
             if hour <= 16:
                 scene club_occult_ut with dissolve
             elif hour <= 20:
                 scene club_occult_v with dissolve
             $ ayano_dialoge += 1
             $ ayano_contact += 5
             $ ayano_trust += 3
             "{color=#BC8F8F}{b}The girl's relationship and trust have improved!{/b}{/color}"
         else:
             show ayano g33
             "But... As you'd expect, you got out of your hug and gave you a wet slap, the red mark of which will remind you that it's better to stay away from girls with body contact too early."
             "Calling you a jerk, Ayano inflated her cheeks and turned her back on you, warning you that if you violate her privacy again, you can order a ticket to the other world."
             $ ayano_dialoge -= 3
             $ ayano_contact -= 2
             "{color=#BC8F8F}{b}The relationship with the girl has deteriorated!{/b}{/color}"
     elif dialoge == 8:
         if hour <= 15:
             "You can only ask out after 4:00 p.m."
             hide ayano
             jump ayano_d
         "Looking at a woman's slut, you have a strong desire to take him out and take a break from the daily routine that has haunted you, if not all your life, most of it."
         glgg "Ayano, can you keep me company in my adventure?"
         $ chance_dialoge = renpy.random.randint(1, 100)
         if chance_dialoge8 >= 100:
             $ chance_dialoge8 = 100
         if chance_dialoge <= chance_dialoge8:
             show ayano g21
             ayanogg1 "Are you asking me out on a date or something?"
             glgg "Who knows."
             show ayano g26
             ayanogg1 "And... I did! Well, I'll keep an exemplary boy like you company."
             glgg "I didn't talk to you like that..."
             "Ignoring your last offer, the girl started packing her school bag, but then she got tired, so she just scored on the case by throwing it somewhere in the corner."
             show ayano g24
             ayanogg1 "I'm ready!"
             glgg "And you don't care much about your stuff..."
             show ayano g35
             ayanogg1 "Why should I care about something I won't be able to use?"
             glgg "It's true... You probably open your textbooks once a year, if not at three."
             show ayano g26
             ayanogg1 "Heh heh, you can see right through me!"
             glgg "I can't see through it, but I do see things that can tell us about your success in school."
             ayanogg1 "Whatever you say."
             "Obviously not very interested in your stories, the girl left the class, unable to kick the door with her tiny foot and literally say that it's time for you to have fun instead of sharpening your balls." with vpunch
             label _menu_sv_ayano:
             menu:
                 "{color=#000000}Ask a girl to take a walk in the park \n{size=21}{i}5."
                     $ energy -= 5
                     scene image "backgrounds/location/park/2.png" with dissolve
                     hide ayano
                     "The energetic jump girl in the park only pleased you with her presence. It's true people say that the mood is airborne, but she seemed to have a lot of fun without you being there."
                     "At least that's what her maximum alienation to your person was about."
                     "Anyway, after a couple of tens of minutes, Ayano was completely exhausted and sat down on the bench, still giving space for your fifth point. You can see that she hasn't completely forgotten about you yet."
                     show ayano g26
                     ayanogg1 "That was fun!"
                     glgg "Have you been playing with your cockroaches in your head?"
                     show ayano g22
                     ayanogg1 "Hey! I just... I'm just glad!"
                     glgg "And why were you so excited to be so alienated to your companion on this walk?"
                     show ayano g33
                     ayanogg1 "Don't be such a beech!"
                     glgg "If you say so."
                     show ayano g38
                     "With a heavy sigh, with the edge of your eye, you noticed a girl's cheeks inflated, who seems to be a little offended by your words. After a minute, it was as if Ayano had forgotten about the insult and started to look at people passing by."
                     show ayano g35
                     glgg "(And why does she look like a dog?)"
                     menu:
                         "{color=#000000}Seeing passers-by like Ayano \n{size=21}{i}0 energy{/i}{/size}{/color}":
                             "Following the example of your interlocutor, you began to observe passers-by, which really aroused a lot of interest."
                             show ayano g36
                             ayanogg1 "Oh, doggie!"
                             show ayano g40
                             "Pointing her finger at a flea-haired brat, the girl almost rolled around the bench for joy, but when her observation target fled beyond the horizon, she immediately became sad."
                             glgg "You're like that dog yourself..."
                             show ayano g26
                             ayanogg1 "Really?"
                             "She seemed to take rudeness as a compliment... What kind of girl?"
                             glgg "Truly. Just as flea-haired, crazy, and biting."
                             show ayano g33
                             ayanogg1 "Hey! Don't insult me!"
                             hide ayano
                             scene image "backgrounds/location/park/3.png"
                             pause 2
                             "After spending a couple of hours discussing dogs and Ayano's resemblance to them, you looked up at the sky and noticed it was already dark."
                             glgg "Don't you think it's time we went home already?"
                             show ayano g26
                             ayanogg1 "Really... Anyway, thank you for talking to me!"
                             glgg "Whatever you say, doggy."
                             show ayano g33
                             ayanogg1 "Hey! Stop calling me names!"
                             glgg "Whatever you say, do..."
                             show ayano g36
                             ayanogg1 "I'm going!"
                             "After a long look, the girl waved at you and headed out of the park, leaving you alone to sit on the bench. \n Anyway, this date can be called quite a success. Both you and the girl had a great time, and you got along pretty well."
                     $ ayano_trust += 6
                     $ ayano_contact += 8
                     $ hour = 20
                     $ minute += renpy.random.randint(26, 35)
                     if dialoge == 0 and dialoge >= 4:
                         $ dialoge = 1
                     jump park1
                 "{color=#000000}Invite a girl to a cafe {image=icons/icons_block.png}\n{size=21}{i}5 energies{/i}{/size}{/color}":
                     "Данная возможность разрабатывается."
                     jump _menu_sv_ayano
                 "{color=#000000}Invite a girl to your house. {image=icons/icons_block.png}\n{size=21}{i}5 energies{/i}{/size}{/color}":
                     "This opportunity is being developed."
                     jump _menu_sv_ayano
         else:
             show ayano g40
             ayanogg1 "Sorry, but I'm busy."
             "Ayano answered you indifferently and went on with her business. She doesn't seem to be interested in you at the moment."
     elif dialoge == 9:
         if ayano_contact >= 10:
             "With your fifth point on the chair, near Ayano, you looked at the girl who, as always, moved her legs up and down, constantly alternating and changing the seemingly established and standardized order, but all this was only at first sight."
             "In fact, her movements were completely chaotic: there was no rhythm, order or anything like that. They were childish movements with absolutely no special meaning. Just a loss of extra energy so... In a peculiar way?"
             glgg "Well, now that you're here, we can talk about the club. How do you even see his future?"
             show ayano g22
             "On hearing your question, the girl immediately stopped being childish by looking at you with another incomprehensible look."
             ayanogg1 "We've talked about this before, I don't see the point in repeating my words a few times so you can finally get it."
             show ayano g34
             "Even though Ayano's words were rude enough, she still smiled at you. Only it's becoming increasingly unclear what nature this smile has..."
             glgg "Maybe my views are archaic enough, but since it's a club, we should develop it somehow, right?"
             show ayano g28
             "Getting up from her already raped place, the girl came as close to you as possible, so that there was only a ten-inch distance between her and your face."
             show ayano g38
             ayanogg1 "You're not sick? This is the first time I've seen a man who wants to work, you might say, as a volunteer!"
             "Having said that, the girl leaned her forehead against yours, but then immediately moved away."
             show ayano g28
             ayanogg1 "So you're not sick..."
             show ayano g22
             "Without letting you say anything, Ayano put her finger to her chin, tapping on it, and started thinking as you thought. All this awkward pause lasted for five minutes, after which Ayano looked at you again with her incomprehensible look."
             ayanogg1 "Uh... What were we talking about?"
             glgg "About the development of the club..."
             show ayano g36
             "The girl's repressed laugh showed that either she tried to avoid answering in such a stupid way, or she just wanted to be a fool. Who knows her?"
             ayanogg1 "That's right! Anyway, let's think about it later, shall we? It's not a good time, because... Hmm..."
             "Ayano thought again, apparently without realizing that her lies were revealed from the moment she started lying, but still two minutes later, she continued her monologue, trying to get away from club activities."
             show ayano g24
             ayanogg1 "That's right! Your leader has had a little trouble with his studies, and I can't give up my duties because... Because I don't trust you enough! Although... I can throw something away, though!"
             "A girl was thrown at you by a can of soda, which you caught with luck, maybe even dexterity."
             ayanogg1 "Relax, buddy, if you're so boring, the girls won't love you!"
             $ cola += 1
             "{color=#BC8F8F}{b}You have a new item{/b}{/color}"
             "When you took a hard sigh, you realized it's too early to talk to Ayano like that. She wasn't really ready for it herself, which is why you shrugged your shoulders bewildered, leaving your former interlocutor to mind your own business. Perhaps you should come to her later?"
             $ dialoge_club += 1
         elif ayano_contact <= 9:
             "Thinking that the best pastime at the moment is to discuss the club with the girl who needs it for truancy lessons, you looked at Ayano, and then immediately put such thoughts out of your mind. It's not only that the embroidery of words for this girl has no authority," he said.
             "to spend your nerves discussing such matters with a man who's always behaving like a child... It's easy to say, the prerogative is not the best."
     elif dialoge == 10:
         ayanogg1 "And... Hopla!" with vpunch
         hide ayano
         scene image "character/club/occult/npc/faceless/2.jpg" with dissolve
         pause 3
         if hour <= 16:
             scene club_occult_ut with dissolve
         elif hour <= 20:
             scene club_occult_v with dissolve
         "Ayano hugged you for a while, which was a bit of a surprise. After a couple of seconds, your body was free from hugs, but not from the curious look of your interlocutor, who snuck up behind you and made you turn in her direction."
         show ayano g24
         ayanogg1 "Hey, buddy!"
         glgg "Have you decided to hug me now every time you need something?"
         show ayano g26
         ayanogg1 "Maybe..."
         glgg "And... What do you want, then?"
         "When you looked at Ayano, you crossed your arms at your chest and started burning it with your eyes. Trying to manipulate through body contact is not the best way to get what you need."
         show ayano g39
         ayanogg1 "Well... "I'm bored... I want to talk!"
         "Having stomped on her feet, the girl stressed the importance of her last sentence, though she understood that it looked childish enough."
         glgg "Don't you have anything better to do?"
         show ayano g31
         ayanogg1 "Yes! I want to talk to you!"
         menu:
             "{color=#000000}Talk to the girl.\n{size=21}{i}2 energies{/i}{/size}{/color}":
                 $ energy -= 2
                 $ club_control = 8
             "{color=#000000}Refer to business\n{size=21}{i}0 energy{/i}{/size}{/color}":
                 glgg "{b}*A blurry sigh*{/b} I'm busy right now. Can we talk about this later?"
                 show ayano g36
                 ayanogg1 "Okay."
                 jump club_occult
     elif dialoge == 11:
         if hour <= 16:
             scene club_occult_ut with dissolve
         elif hour <= 20:
             scene club_occult_v with dissolve
         show ayano g24
         ayanogg1 "Wait!"
         "When you heard a familiar voice, you turned to the side where the words that the girl had specially extended came from. Maybe thinking it was cuter, maybe there were other reasons. Anyway, it's not that important at the moment."
         show ayano g22
         ayanogg1 "I want you to give me a hug! I miss tenderness!"
         glgg "What?"
         ayanogg1 "I want a hug!"
         menu:
             "{color=#000000}Hug a girl\n{size=21}{i}2 energies{/i}{/size}{/color}":
                 $ energy -= 2
                 hide ayano
                 scene image "character/club/occult/npc/faceless/1.jpg" with dissolve
                 "In an effort to hug the girl, you confidently pressed Ayano's face against your chest, enjoying this act and sometimes stroking her silky hair with a rough palm, making them look even more broken."
                 "Anyway, these movements can hardly be called more than a friendly gesture aimed at the usual satisfaction of human needs."
                 "After a couple of minutes, your hug broke. The girl seems to have liked them too, which is why you can say your relationship is improving exponentially."
                 if hour <= 16:
                     scene club_occult_ut with dissolve
                 elif hour <= 20:
                     scene club_occult_v with dissolve
                 $ ayano_dialoge += 3
                 $ ayano_contact += 2
             "{color=#000000}Refer to business\n{size=21}{i}0 energy{/i}{/size}{/color}":
                 glgg "I'm sorry, this isn't exactly the time."
                 show ayano g37
                 ayanogg1 "Okay..."
         jump club_occult
     elif dialoge == 19:
         if free_soda >= 1:
             show ayano g24
             ayanogg1 "What? Soda? Of course, here you go!"
             "After giving you a cold jar of heavy drink, the girl went on with her business without paying the slightest attention to you."
             $ free_soda = 0
             $ cola += 1
         else:
             show ayano g33
             ayanogg1 "Don't get cocky! You've had it today!"
     elif dialoge == 22:
         "Recalling Ayano's recent words about your complete freedom of action, you approached her and told her that you wanted to kiss, to which you were replied with a approving nod. "
         "Quickly peeing on your lips childishly, the girl turned her back on your face and started staring at the ceiling."
         $ ayano_dialoge += 8
         $ ayano_contact += 5
     elif dialoge == 23:
         "When you talked to those present at the club, you had dialogues on different topics, which in the end brought you all together quite well and gave you much more authority!"
         $ contact_club += 2
         python:
             for number_npc in range(1, number_npc_max):
                 npc_id = 'npc'+str(number_npc)
                 club_npc = eval(npc_id)["club_npc"]
                 if club_npc == 7:
                     contact_npc = eval(npc_id)["contact_npc"]
                     love_npc = eval(npc_id)["love_npc"]
                     contact_npc += 6
                     love_npc += 2
                     eval(npc_id)["love_npc"] = love_npc
                     eval(npc_id)["contact_npc"] = contact_npc
     elif dialoge == 24:
         if contact_club <= 9:
             "Having decided that the popularity of the club is now the most important priority, you asked your friends to write an article on the occult theme, but, as expected, you were refused. It seems that your relationship is not yet as well developed as we would like it to be."
         else:
             if gotov_st == 1:
                 if weeks >= oz_weekly:
                     if days >= oz_days or weeks > oz_weekly:
                         "By approaching your club mates, you have received a long-awaited article that will be used to promote the club."
             else:
                 "It's too soon."
             if gotov_st == 0:
                 $ oz_days = days + 6
                 $ oz_weekly = weeks
                 if oz_days >= 7:
                     $ oz_days -= 7
                     $ oz_weekly += 1
                     $ oz_days_name = name_days[str(oz_days)]
                     $ gotov_st = 1
                 "Having decided that the popularity of the club is now the most important priority, you asked your club mates to write an article on an occult theme, to which, as expected, you received a positive response. Having said that in about a week everything would be ready, you decided to go and check the results of their work in [oz_days_name]".
     elif dialoge == 25:
         $ chance_dialoge = renpy.random.randint(1, 100)
         if flirt_chance >= 100:
             $ flirt_chance = 100
         if chance_dialoge <= flirt_chance:
             show ayano g36
             ayanogg1 "Heh heh... Thank you."
             "Successful flirting is a delicate matter, but you did great! During the whole dialogue your interlocutor actively participated in the dialogue, and also showed you signs of attention, constantly touching you and giving you compliments".
             $ ayano_contact += 6
             $ ayano_trust += 4
             $ dialoge_ayano = 7
             $ dialoge = old_dialoge
         else:
             show ayano g22
             ayanogg1 "Eh? Why are you flirting with me?"
             $ dialoge_ayano = 8
             $ ayano_contact -= 5
             $ ayano_trust -= 7
             $ dialoge = old_dialoge
             "When you were trying to flirt with Ayano, you didn't notice that she didn't like this action on your part. As a result, you were sent far away with such hints, so you also received a picture of your victim's disgruntled face."
         hide ayano
         call screen ayano_d
     elif dialoge == 26:
         if minet_ayano == 0:
             show ayano g31 with dissolve
             ayanogg1 "You... What are you talking about?!"
             glgg "I think you're okay with your hearing, but it looks like you're gonna have to repeat it a few times and syllables... I say I want a blowjob. It's from you."
             show ayano g22
             ayanogg1 "…"
             glgg "I thought I made it clear... Okay, I'll do it again..."
             show ayano g41
             ayanogg1 "I understand you..."
             show ayano g39
             ayanogg1 "It's just... Well... Why talk about it so hard? Why do you have to be blunt about something like that?"
             glgg "How else can I say what I want? Mumble for half an hour on the condition that you once said: "ask me anything, and I'll do it"?"
             show ayano g41
             ayanogg1 "Yes! I am, you know, a girl!"
             show ayano g22
             ayanogg1 "So also... Well... An innocent girl..."
             glgg "About how. So you're still a virgin."
             show ayano g39
             ayanogg1 "You... You've got to be kidding me..."
             show ayano g42
             ayanogg1 "Anyway, I'm not going to do that with you! Yes, you are!"
             glgg "I think you've got a perfect chance to try your skills and even practice a little."
             show ayano g41
             ayanogg1 "I said I didn't..."
             glgg "You may consider this a gesture of good faith. I think this is a really good opportunity for you, though."
             show ayano g42
             ayanogg1 "You're terrible... No. Worst cauldron! I said I didn't want to, but..."
             show ayano g22
             ayanogg1 "Given that you won't let go of me, and how much you've done for me... I don't know... I just don't know how to deal with a request like that..."
             "After standing for a few minutes in the same posture and apparently thinking about your sudden offer, Ayano still snapped and said."
             $ chance_dialoge = renpy.random.randint(1, 100)
             if minet_chance >= 100:
                 $ minet_chance = 100
             if chance_dialoge <= minet_chance:
                 ayanogg1 "You know, I've been doing some thinking and I thought: I think you really deserve it... So... Well... Go to the back of the club now and we'll meet there..."
                 glgg "Somehow you quickly changed your mind about this... Did you want to?"
                 show ayano g41
                 ayanogg1 "One more word and my opinion will change dramatically not only about this, but about your life."
                 hide ayano
                 $ minet_ayano = 2
                 "Heading towards the pantry, the girl left you."
             else:
                 ayanogg1 "You know, well... I've been doing some thinking and... Anyway, I need some more time... You... Well... Wait?"
                 glgg "I'll have to, but anyway, I need to know how long to expect."
                 ayanogg1 "Well..."
                 glgg "Well?"
                 ayanogg1 "The club... As soon as it gets a little more popular, I think I'll decide something about that offer..."
                 hide ayano
                 $ minet_ayano = 1
                 "After taking a hard breath, you left Ayano thinking while you were satisfied with the result of your recent conversation: at least you already know what you need to do to get what you want."
         elif minet_ayano == 1:
             $ chance_dialoge = renpy.random.randint(1, 100)
             if minet_chance >= 100:
                 $ minet_chance = 100
             if chance_dialoge <= minet_chance:
                 glgg "So... Did you think?"
                 show ayano g31
                 ayanogg1 "Ah... Well..."
                 show ayano g22
                 ayanogg1 "Actually, yes..."
                 glgg "Well? Decided what?"
                 show ayano g31
                 ayanogg1 "I'll do it, but... Not here, but in the back. That's where I'll meet you."
                 hide ayano
                 $ minet_ayano = 2
                 "Heading towards the pantry, the girl left you."
             else:
                 glgg "So... Did you think?"
                 show ayano g32
                 ayanogg1 "А? About what?"
                 glgg "You're definitely having a memory problem..."
                 show ayano g39
                 ayanogg1 "Ah... Right... Heh-heh, sorry, but not yet."
         elif minet_ayano == 3:
             show ayano g22
             ayanogg1 "Uh... Is this what you want again?"
             glgg "Why ask what's already obvious?"
             ayanogg1 "Okay, then I'll meet you in the back, like I always do."
             "On her way to the back room, the girl left you alone."
             $ minet_ayano = 4
         jump club
     if ayano_ivent == 1 and ayano_contact >= 5 and hentai_patch_inicial == True:
         jump ayano_ivent
     elif ayano_ivent == 1 and ayano_contact >= 5 and hentai_patch_inicial == False:
         $ ayano_ivent += 1
     elif ayano_ivent == 2 and ayano_contact >= 20:
         jump ayano_ivent
     elif ayano_ivent == 3 and ayano_contact >= 40:
         jump ayano_ivent
     $ rand_ayano = renpy.random.randint(1, 60)
     if ayano_contact >= 40 and rand_ayano == 3:
         $ dialoge = 10
         jump ayano2
     elif ayano_contact >= 40 and rand_ayano == 4:
         $ dialoge = 10
         jump ayano2
     elif ayano_contact >= 50 and rand_ayano == 6:
         $ dialoge = 11
     $ dialoge = old_dialoge
     hide ayano
     jump ayano_d
