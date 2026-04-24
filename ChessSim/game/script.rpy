## Chess Romance: A Dating Sim on the Board
## script.rpy

# ================================
# CHARACTER DEFINITIONS - WHITE PIECES
# ================================

# White King
define wking = Character("King Aldric", color="#FFD700", image="wking")

# White Queen  
define wqueen = Character("Queen Seraphina", color="#F0E68C", image="wqueen")

# White Bishops
define wbishop1 = Character("Bishop Celeste", color="#E6E6FA", image="wbishop1")
define wbishop2 = Character("Bishop Lumina", color="#E6E6FA", image="wbishop2")

# White Knights
define wknight1 = Character("Knight Sterling", color="#C0C0C0", image="wknight1")
define wknight2 = Character("Knight Galahad", color="#C0C0C0", image="wknight2")

# White Rooks
define wrook1 = Character("Rook Bastion", color="#D3D3D3", image="wrook1")
define wrook2 = Character("Rook Rampart", color="#D3D3D3", image="wrook2")

# White Pawns
define wpawn1 = Character("Pawn Aria", color="#F5F5DC", image="wpawn1")
define wpawn2 = Character("Pawn Beck", color="#F5F5DC", image="wpawn2")
define wpawn3 = Character("Pawn Cara", color="#F5F5DC", image="wpawn3")
define wpawn4 = Character("Pawn Drew", color="#F5F5DC", image="wpawn4")
define wpawn5 = Character("Pawn Eden", color="#F5F5DC", image="wpawn5")
define wpawn6 = Character("Pawn Finn", color="#F5F5DC", image="wpawn6")
define wpawn7 = Character("Pawn Grace", color="#F5F5DC", image="wpawn7")
define wpawn8 = Character("Pawn Hope", color="#F5F5DC", image="wpawn8")

# ================================
# CHARACTER DEFINITIONS - BLACK PIECES
# ================================

# Black King
define bking = Character("King Obsidian", color="#2F4F4F", image="bking")

# Black Queen
define bqueen = Character("Queen Noctis", color="#483D8B", image="bqueen")

# Black Bishops
define bbishop1 = Character("Bishop Raven", color="#4B0082", image="bbishop1")
define bbishop2 = Character("Bishop Vesper", color="#4B0082", image="bbishop2")

# Black Knights
define bknight1 = Character("Knight Dante", color="#36454F", image="bknight1")
define bknight2 = Character("Knight Shadow", color="#36454F", image="bknight2")

# Black Rooks
define brook1 = Character("Rook Fortress", color="#2C3E50", image="brook1")
define brook2 = Character("Rook Citadel", color="#2C3E50", image="brook2")

# Black Pawns
define bpawn1 = Character("Pawn Iris", color="#1C1C1C", image="bpawn1")
define bpawn2 = Character("Pawn Jasper", color="#1C1C1C", image="bpawn2")
define bpawn3 = Character("Pawn Kai", color="#1C1C1C", image="bpawn3")
define bpawn4 = Character("Pawn Luna", color="#1C1C1C", image="bpawn4")
define bpawn5 = Character("Pawn Milo", color="#1C1C1C", image="bpawn5")
define bpawn6 = Character("Pawn Nova", color="#1C1C1C", image="bpawn6")
define bpawn7 = Character("Pawn Orion", color="#1C1C1C", image="bpawn7")
define bpawn8 = Character("Pawn Zara", color="#1C1C1C", image="bpawn8")

# ================================
# NARRATOR AND PLAYER
# ================================

define narrator = Character(None, kind=nvl)
define mc = Character("[player_name]", color="#FF69B4")

# ================================
# GAME START
# ================================

label start:
    
    # Set up variables
    $ player_name = "Player"
    $ affection_wking = 0
    $ affection_wqueen = 0
    $ affection_bking = 0
    $ affection_bqueen = 0
    
    # Opening scene
    scene bg chessboard
    with fade
    
    "Welcome to the Grand Chessboard Academy, where pieces from both kingdoms coexist in an uneasy truce."
    
    "As a new normal observer assigned to document the lives of these legendary warriors, you'll witness their stories unfold."
    
    python:
        player_name = renpy.input("What is your name?", default="Alex", length=20)
        player_name = player_name.strip() or "Alex"
    
    scene bg academy_courtyard
    with fade
    
    "You arrive at the academy courtyard on your first day, clutching your observer's badge."
    
    "The pieces move about freely here, no longer bound to their battle formations."
    
    "Suddenly, a regal voice calls out behind you."
    
    show wking normal
    with dissolve
    
    wking "Ah, you must be the new observer. I am King Aldric of the White Kingdom."
    
    wking "Welcome to our... unique institution. I trust you'll find your time here enlightening."
    
    mc "Thank you, Your Majesty. I'm honored to be here."
    
    wking "Please, formality serves little purpose in peacetime. Aldric will do."
    
    wking "Though I must warn you - not everyone here shares my optimism about this academy."
    
    show bking angered at right
    with dissolve
    
    bking "Aldric speaks the truth, for once."
    
    "A darker, more imposing figure approaches from the shadows."
    
    bking "I am King Obsidian. Do not mistake this ceasefire for friendship, observer."
    
    bking "The black pieces remember every fallen comrade. This 'academy' is merely a strategic pause."
    
    wking "Ever the pessimist, Obsidian. Perhaps our new friend here can help bridge our divide."
    
    bking "Hmph. We shall see."
    
    hide bking
    with dissolve
    
    wking "Forgive his demeanor. The weight of leadership has made him... cautious."
    
    wking "You should meet the others. Each piece has a story worth hearing."
    
    hide wking
    with dissolve
    
    # Meeting the Queens
    scene bg academy_library
    with fade
    
    "You decide to explore the academy library, where you encounter two striking figures engaged in a chess match."
    
    show wqueen happy at left
    show bqueen normal at right
    with dissolve
    
    wqueen "Checkmate in seven moves, Noctis. You've left your king exposed."
    
    bqueen "How presumptuous. You forget I can move in all directions - including backward from mistakes."
    
    "The white queen notices your presence and smiles warmly."
    
    wqueen "Oh! You must be our new observer. I'm Queen Seraphina."
    
    wqueen "Don't mind our little game - Noctis and I have been rivals for centuries, but we play for enjoyment now."
    
    bqueen "Speak for yourself, Seraphina. I play to win."
    
    "The black queen's eyes gleam with competitive fire."
    
    bqueen "Queen Noctis of the Obsidian Court. Remember the name, observer."
    
    mc "You're both incredibly skilled. Do you enjoy teaching?"
    
    wqueen "Oh yes! I mentor the younger pieces. Power comes with responsibility."
    
    bqueen "I prefer to let students learn through trial and error. Harsh lessons stick."
    
    wqueen "We have different philosophies, but we both care deeply about our pieces."
    
    menu:
        "Ask Seraphina about her teaching methods":
            jump seraphina_route
        
        "Ask Noctis about her competitive spirit":
            jump noctis_route
        
        "Excuse yourself to meet the other pieces":
            jump explore_academy

label seraphina_route:
    
    $ affection_wqueen += 1
    
    hide bqueen
    with dissolve
    
    "Noctis returns to her chess problem, leaving you alone with Seraphina."
    
    wqueen "I believe everyone has potential, they just need guidance and encouragement."
    
    wqueen "Take the pawns, for instance. They start with limited moves, but with determination..."
    
    wqueen "They can transform into anything they wish to be. Even another queen."
    
    mc "That's a beautiful perspective."
    
    wqueen "Thank you. It's why I fought so hard for this academy."
    
    wqueen "Too many pieces were lost to endless conflict. Here, they can be more than their rank."
    
    "She places a gentle hand on your shoulder."
    
    wqueen "I hope you'll help us tell their stories. Every piece deserves to be remembered."
    
    jump explore_academy

label noctis_route:
    
    $ affection_bqueen += 1
    
    hide wqueen
    with dissolve
    
    "Seraphina excuses herself tactfully, giving you space with Noctis."
    
    bqueen "You want to know about competition? Let me tell you about survival."
    
    bqueen "On the battlefield, hesitation means death. I've lost too many pieces who weren't prepared."
    
    mc "This academy must feel very different for you then."
    
    bqueen "It's... an adjustment. Peace feels like waiting for the other shoe to drop."
    
    bqueen "But I suppose if we must have peace, we should be excellent at it too."
    
    "A rare smile crosses her face."
    
    bqueen "Perhaps you'd like to play a match sometime? I promise to go easy on you."
    
    bqueen "Well... relatively easy."
    
    jump explore_academy

label explore_academy:
    
    scene bg academy_training_grounds
    with fade
    
    "You head to the training grounds where several pieces are practicing."
    
    show wknight1 happy
    with dissolve
    
    wknight1 "En garde!"
    
    "A silver-armored knight executes a perfect L-shaped jump, landing happyly."
    
    wknight1 "Ah, the observer! Knight Sterling at your service."
    
    wknight1 "Care to see some unconventional tactics? We knights specialize in the unexpected."
    
    show bknight1 happy at right
    with dissolve
    
    bknight1 "Sterling, you're showing off again."
    
    "Another knight appears, moving in the same distinctive pattern."
    
    bknight1 "Knight Dante. Don't let Sterling's bravado fool you - we're equally matched."
    
    wknight1 "Equally matched? I seem to recall our last three sparring sessions went to me."
    
    bknight1 "You count differently in the White Kingdom. I count honestly."
    
    "They both laugh - clearly this is a happy rivalry."
    
    mc "You two seem to get along well despite being from different kingdoms."
    
    wknight1 "Knights respect knights. We understand the burden of irregular movement."
    
    bknight1 "Plus, Sterling makes for good practice. Predictably unpredictable."
    
    wknight1 "I'll take that as a compliment."
    
    show wpawn1 happy at left
    with dissolve
    
    wpawn1 "Um, excuse me? Are you the observer everyone's talking about?"
    
    "A young white pawn approaches nervously."
    
    wpawn1 "I'm Aria. I just wanted to say... it's nice to have someone normal here."
    
    wpawn1 "Sometimes the tension between kingdoms makes things awkward."
    
    mc "I can imagine. What's it like being a pawn in all this?"
    
    wpawn1 "Well... we're the most numerous, but also the most vulnerable."
    
    wpawn1 "But that's okay! We work together and protect each other."
    
    show bpawn4 normal at right behind bknight1
    with dissolve
    
    bpawn4 "Aria's right. Pawns have to stick together."
    
    "A black pawn joins the conversation."
    
    bpawn4 "I'm Luna. We pawns know our worth, even if others see us as expendable."
    
    bpawn4 "Every step forward counts. Every promotion earned, not given."
    
    wpawn1 "Luna! Want to practice formations later?"
    
    bpawn4 "Sure. The usual spot?"
    
    "You're touched by the camaraderie between pieces from opposing sides."
    
    hide wknight1
    hide bknight1
    with dissolve
    
    wpawn1 "Observer, if you ever want to know what it's really like here..."
    
    wpawn1 "Talk to us pawns. We see everything from our position."
    
    bpawn4 "And we're not afraid to tell the truth."
    
    jump meet_bishops

label meet_bishops:
    
    scene bg academy_chapel
    with fade
    
    "The academy chapel is normal, lit by diagonal rays of sunlight through tall windows."
    
    show wbishop1 normal
    with dissolve
    
    wbishop1 "Welcome, observer. I am Bishop Celeste."
    
    wbishop1 "This chapel serves all pieces, regardless of color. A true normal space."
    
    mc "It's beautiful. Do you maintain it?"
    
    wbishop1 "Along with my counterpart, yes."
    
    show bbishop2 normal at right
    with dissolve
    
    bbishop2 "Bishop Vesper. I handle the evening services."
    
    bbishop2 "Celeste and I move in parallel but never intersect. Rather poetic, wouldn't you say?"
    
    wbishop1 "We represent different paths to the same truth - that unity requires embracing our differences."
    
    bbishop2 "Though we bishops can only traverse squares of one color, we've learned to appreciate both light and dark."
    
    wbishop1 "Would you like to light a candle, observer? For the pieces no longer with us?"
    
    menu:
        "Light a candle":
            $ affection_wbishop1 = 1
            mc "I'd be honored."
            "You light a candle, and the bishops bow their heads in silent prayer."
            wbishop1 "Thank you. Remembrance helps us move forward."
        
        "Ask about their philosophy":
            mc "How did you both come to this perspective?"
            bbishop2 "Through loss. We've both seen too many pieces fall."
            wbishop1 "We realized that holding grudges only creates more suffering."
            bbishop2 "So we chose a different diagonal. One of peace."

    hide wbishop1
    hide bbishop2
    with dissolve
    
    jump meet_rooks

label meet_rooks:
    
    scene bg academy_fortress
    with fade
    
    "The fortress training area is where defensive specialists practice."
    
    show wrook1 normal
    with dissolve
    
    wrook1 "Halt. State your purpose."
    
    "A massive white rook blocks your path."
    
    mc "I'm the new observer. Just exploring the academy."
    
    wrook1 "Observer credentials verified. I am Rook Bastion, head of perimeter security."
    
    wrook1 "You may proceed, but stay within designated areas."
    
    show brook1 angered at right
    with dissolve
    
    brook1 "Bastion, stop interrogating visitors. I'm Rook Fortress."
    
    brook1 "We rooks take security seriously - straight lines, no deviation, absolute defense."
    
    wrook1 "Fortress and I coordinate all academy protection protocols."
    
    brook1 "Despite our allegiances, safety is paramount. An attack on one kingdom would endanger both."
    
    mc "That's very professional of you both."
    
    wrook1 "Professionalism is all we have. Personal feelings must not compromise structural integrity."
    
    brook1 "Agreed. Though I'll admit, Bastion's dedication is... admirable."
    
    "Bastion's stern expression softens slightly."
    
    wrook1 "As is Fortress's normal acumen."
    
    "You sense a deep mutual respect between these two guardians."
    
    jump academy_evening

label academy_evening:
    
    scene bg academy_courtyard_evening
    with fade
    
    "As evening falls, pieces from both kingdoms gather in the courtyard for social time."
    
    show wpawn5 happy at left
    show bpawn7 happy at center  
    show wpawn3 happy at right
    with dissolve
    
    wpawn5 "Eden, reporting for duty! Well, social duty anyway."
    
    bpawn7 "Orion here. These evening gatherings are the highlight of academy life."
    
    wpawn3 "I'm Cara. Isn't the sunset beautiful? It touches both our kingdoms equally."
    
    "More pawns join the group."
    
    show wpawn2 tired at left behind wpawn5
    with dissolve
    
    wpawn2 "Hi, I'm Beck. Sorry, I'm not great with new people..."
    
    wpawn5 "Beck's just shy! But they're super talented at chess problem-solving."
    
    show bpawn2 happy at right behind wpawn3
    with dissolve
    
    bpawn2 "Jasper's the name. These white pawns aren't so bad once you get to know them."
    
    show wpawn4 happy
    with dissolve
    
    wpawn4 "Drew here! Want to join our game night?"
    
    show bpawn3 normal
    with dissolve
    
    bpawn3 "I'm Kai. I usually just watch, but you're welcome to sit with me."
    
    "The pawns all chat animatedly, their individual personalities shining through."
    
    show wpawn6 happy at left
    show bpawn5 happy at right
    with dissolve
    
    wpawn6 "Finn! Pleased to meet you! Isn't this academy amazing?"
    
    bpawn5 "Milo. It's... adequate. Though Finn's enthusiasm is infectious, I'll admit."
    
    show wpawn7 happy
    show bpawn6 normal
    show wpawn8 happy
    show bpawn8 happy
    with dissolve
    
    wpawn7 "Grace. I help organize these social events."
    
    bpawn6 "Nova. I prefer stargazing, but Grace convinced me to attend."
    
    wpawn8 "Hope's my name! Every day here is proof that peace is possible."
    
    bpawn8 "And I'm Zara. Hope's idealism is exhausting but... kind of inspiring."
    
    "You're surrounded by the warmth of sixteen different pawns, each with their own story."
    
    mc "You all seem so close, despite the kingdom divide."
    
    wpawn5 "We pawns understand each other! Same struggles, same dreams."
    
    bpawn7 "Plus, we're all working toward promotion. Common goals unite us."
    
    jump evening_choice

label evening_choice:
    
    hide wpawn2
    hide wpawn3
    hide wpawn4
    hide wpawn5
    hide wpawn6
    hide wpawn7
    hide wpawn8
    hide bpawn2
    hide bpawn3
    hide bpawn5
    hide bpawn6
    hide bpawn7
    hide bpawn8
    with dissolve
    
    "As the evening continues, you have time for one more meaningful conversation."
    
    menu:
        "Spend time with the remaining Knights":
            jump knight_evening
        
        "Join the Bishops for evening prayer":
            jump bishop_evening
        
        "Help the Rooks with night patrol":
            jump rook_evening
        
        "Attend the Royal Summit":
            jump royal_summit

label knight_evening:
    
    scene bg academy_stables
    with fade
    
    show wknight2 normal at left
    show bknight2 happy at right
    with dissolve
    
    wknight2 "Ah, observer! I'm Knight Galahad, Sterling's partner."
    
    wknight2 "Unlike my show-off colleague, I believe in normal competence."
    
    bknight2 "And I'm Knight Shadow. Dante's the flashy one in our pair."
    
    bknight2 "Galahad and I prefer the subtle approach."
    
    wknight2 "We were just discussing unconventional chess strategies. Care to join?"
    
    mc "I'd love to learn from you both."
    
    bknight2 "The key to knight strategy is thinking three moves ahead in unexpected directions."
    
    wknight2 "And never being where your opponent expects you to be."
    
    "They demonstrate complex jump patterns together."
    
    bknight2 "Galahad's form is impeccable. For a white knight."
    
    wknight2 "High praise from Shadow. You're improving as well."
    
    "The mutual respect is evident despite their different backgrounds."
    
    jump ending_day_one

label bishop_evening:
    
    scene bg academy_chapel_night
    with fade
    
    show wbishop2 normal at left
    show bbishop1 normal at right
    with dissolve
    
    wbishop2 "Welcome, observer. I'm Bishop Lumina."
    
    wbishop2 "I handle the philosophical discussions that Celeste is sometimes too modest to lead."
    
    bbishop1 "And I'm Bishop Raven. I bring the black kingdom's perspective to our dialogues."
    
    bbishop1 "Though Vesper would say I'm too direct sometimes."
    
    mc "What do you discuss?"
    
    wbishop2 "The nature of purpose. Why we move as we do. Whether our paths are chosen or destined."
    
    bbishop1 "Heavy topics. But necessary ones if we're to truly understand each other."
    
    wbishop2 "Would you share your thoughts, observer? An outside perspective is valuable."
    
    "You engage in deep conversation with both bishops about fate, choice, and unity."
    
    bbishop1 "Fascinating. You see patterns we might miss from within our squares."
    
    wbishop2 "Please visit again. These discussions nourish the soul."
    
    jump ending_day_one

label rook_evening:
    
    scene bg academy_walls
    with fade
    
    show wrook2 normal at left
    show brook2 normal at right
    with dissolve
    
    wrook2 "Observer. I'm Rook Rampart, Bastion's counterpart."
    
    wrook2 "We maintain the eastern fortifications."
    
    brook2 "Rook Citadel here. I handle the western defenses with Fortress."
    
    brook2 "Join us for patrol? You'll see the academy from a different angle."
    
    mc "I'd be honored."
    
    "You walk the walls with both rooks, learning about their defensive strategies."
    
    wrook2 "Protection isn't just physical. It's creating an environment where everyone feels safe."
    
    brook2 "Agreed. That's why Rampart and I coordinate so closely."
    
    brook2 "Trust isn't built through grand gestures. It's built through consistent, reliable action."
    
    wrook2 "Well said, Citadel. Well said."
    
    jump ending_day_one

label royal_summit:
    
    scene bg academy_throne_room
    with fade
    
    show wking normal at left
    show bking normal at right
    with dissolve
    
    wking "Ah, observer. Obsidian and I hold these private summits regularly."
    
    bking "To ensure our... truce remains stable."
    
    wking "Please, join us. Your normal perspective could help."
    
    mc "What are you discussing tonight?"
    
    bking "The future. Whether this academy is sustainable or merely delaying inevitable conflict."
    
    wking "I believe in its potential. We've already seen pieces form bonds across kingdom lines."
    
    bking "Bonds that could shatter at the first sign of real disagreement."
    
    wking "Or bonds that could prevent disagreement from becoming warfare."
    
    "The two kings regard each other with a complex mix of respect and wariness."
    
    bking "Tell me, observer. In your normal opinion, can natural enemies truly become allies?"
    
    menu:
        "With time and effort, yes":
            $ affection_wking += 2
            $ affection_bking += 1
            wking "Well said. Change requires patience."
            bking "Hmm. Perhaps. Perhaps."
        
        "It depends on whether they want to":
            $ affection_bking += 2
            bking "Exactly. Willingness is everything."
            wking "And I believe that willingness is growing."
        
        "I'm not sure yet, I need to observe more":
            wking "An honest answer. We appreciate your normalness."
            bking "Indeed. Premature conclusions help no one."
    
    jump ending_day_one

label ending_day_one:
    
    scene bg academy_courtyard_night
    with fade
    
    "As your first day at the academy concludes, you reflect on everyone you've met."
    
    "Thirty-two unique pieces, each with their own hopes, fears, and personalities."
    
    "Kings carrying the weight of leadership."
    
    "Queens balancing power with compassion."
    
    "Bishops seeking meaning in their diagonal paths."
    
    "Knights jumping through life with unconventional grace."
    
    "Rooks standing firm as unwavering guardians."
    
    "And pawns - so many pawns - each dreaming of transformation."
    
    "This academy represents something unprecedented: pieces choosing peace over endless warfare."
    
    "Your role as observer suddenly feels more important than you realized."
    
    "These aren't just chess pieces. They're individuals with stories worth telling."
    
    "And your documentation might be what preserves this fragile peace for future generations."
    
    scene black
    with fade
    
    centered "End of Day One"
    centered "Your journey at the Grand Chessboard Academy has only just begun..."
    centered "Romance routes, friendships, and conflicts await."
    centered "Every move matters. Every choice shapes the future."
    centered "Will you help bridge the divide between kingdoms?"
    centered "Or will old wounds prove too deep to heal?"
    
    jump day_two

# ================================
# DAY TWO
# ================================

label day_two:
    
    scene bg academy_courtyard
    with fade
    
    "The morning sun rises over the academy, casting long shadows across the courtyard."
    
    "You wake early, eager to continue your observations and deepen your understanding of this unique place."
    
    "As you step outside, you notice unusual tension in the air."
    
    show wpawn5 happy at left
    show bpawn7 happy at right
    with dissolve
    
    wpawn5 "Morning, observer! You feel that weird vibe today?"
    
    bpawn7 "It's the anniversary. Of course there's tension."
    
    mc "Anniversary?"
    
    wpawn5 "The Great Stalemate. The battle that ended the war and led to this academy."
    
    bpawn7 "Not everyone's ready to celebrate a draw when they think they should have won."
    
    "Orion's usually happy demeanor is more somber than usual."
    
    wpawn5 "Both kings are giving memorial speeches later. Should be... interesting."
    
    hide wpawn5
    hide bpawn7
    with dissolve
    
    jump day_two_morning_choice

label day_two_morning_choice:
    
    "You have some time before the memorial ceremony. Who should you seek out?"
    
    menu:
        "Find the Kings - understand the political tension":
            jump day_two_kings
        
        "Check on the Pawns - they seem most affected":
            jump day_two_pawns
        
        "Visit the Queens - they might mediate the situation":
            jump day_two_queens
        
        "Talk to the Knights - get the warrior perspective":
            jump day_two_knights

label day_two_kings:
    
    scene bg academy_fortress
    with fade
    
    "You find both kings on the fortress walls, standing at opposite ends."
    
    show wking normal at left
    with dissolve
    
    wking "Ah, observer. Come to document the ceremony preparations?"
    
    mc "Actually, I wanted to understand what this day means to both of you."
    
    wking "An astute question. This anniversary is... complicated."
    
    show bking normal at right
    with dissolve
    
    bking "Complicated is one word for it. Frustrating is another."
    
    wking "We both lost pieces we cared about in that final battle."
    
    bking "And neither of us achieved victory. Just... cessation."
    
    mc "But that cessation led to peace. To this academy."
    
    wking "Precisely my point. The stalemate was a beginning, not an ending."
    
    bking "Or it was postponing the inevitable. Time will tell."
    
    "The two kings look at each other across the distance."
    
    wking "We've agreed to give speeches that honor the fallen without stoking old fires."
    
    bking "Though my pieces deserve to hear their sacrifices remembered properly."
    
    wking "As do mine, Obsidian. We're not so different in that regard."
    
    "A moment of understanding passes between them."
    
    bking "No. I suppose we're not."
    
    $ affection_wking += 1
    $ affection_bking += 1
    
    jump day_two_ceremony

label day_two_pawns:
    
    scene bg academy_training_grounds
    with fade
    
    "You find a gathering of pawns - both white and black - sitting together in a circle."
    
    show wpawn1 happy at left
    show bpawn4 normal at center
    show wpawn8 happy at right
    with dissolve
    
    wpawn1 "Oh! Observer, you should join us. We're sharing stories."
    
    mc "Stories about what?"
    
    bpawn4 "The pieces we knew who didn't make it here. Who fell in the final battle."
    
    wpawn8 "We think it's important to remember them together. Not divided by kingdom."
    
    show wpawn2 tired
    show bpawn3 normal  
    with dissolve
    
    wpawn2 "I... I had a friend. A black pawn from the other side of the board."
    
    wpawn2 "We used to be across from each other. Never moved forward because we didn't want to capture each other."
    
    bpawn3 "I remember hearing about that. The 'Peaceful Standoff' the generals called it."
    
    wpawn2 "But then the orders came. And..."
    
    bpawn4 "You don't have to finish. We understand."
    
    "Beck wipes their eyes, and several other pawns reach out supportively."
    
    show wpawn3 happy
    show bpawn2 happy
    with dissolve
    
    wpawn3 "That's why this academy matters so much. So no more pawns have to face that choice."
    
    bpawn2 "Exactly. We're the ones who see the cost of war most clearly."
    
    show wpawn4 happy
    show bpawn5 happy
    show wpawn6 happy
    show bpawn6 normal
    with dissolve
    
    wpawn4 "Today's hard, but we're facing it together."
    
    bpawn5 "Yeah. Even I can't make a cynical joke about that."
    
    wpawn6 "This is what peace looks like! Not forgetting, but healing together!"
    
    bpawn6 "Finn's right. The stars don't shine separately - they make constellations."
    
    "You're moved by the pawns' collective strength and wisdom."
    
    mc "Thank you for letting me witness this. You're all incredibly brave."
    
    wpawn1 "We're just pawns trying to move forward. Together."
    
    $ affection_wpawn1 = 2
    $ affection_bpawn4 = 2
    
    hide wpawn1
    hide wpawn2
    hide wpawn3
    hide wpawn4
    hide wpawn6
    hide bpawn2
    hide bpawn3
    hide bpawn4
    hide bpawn5
    hide bpawn6
    with dissolve
    
    jump day_two_ceremony

label day_two_queens:
    
    scene bg academy_library
    with fade
    
    "You find both queens in the library, working together on something."
    
    show wqueen happy at left
    show bqueen normal at right
    with dissolve
    
    wqueen "Observer! Perfect timing. We need an impartial opinion."
    
    mc "About what?"
    
    bqueen "We're preparing a joint memorial display. Honoring pieces from both kingdoms."
    
    wqueen "But we're debating the arrangement. Should they be separated by kingdom or integrated?"
    
    bqueen "Separation maintains their individual identities and allegiances."
    
    wqueen "But integration shows we've moved beyond those divisions."
    
    menu:
        "Integrate them - show unity":
            $ affection_wqueen += 2
            mc "I think integration better represents what the academy stands for."
            wqueen "My thoughts exactly! Thank you."
            bqueen "Hmm. I can see the symbolism, though it still feels... incomplete."
            wqueen "What if we integrate them but keep kingdom markers? Unity with identity?"
            bqueen "Now that... that I can work with."
        
        "Separate them - honor their distinct sacrifices":
            $ affection_bqueen += 2
            mc "Their sacrifices were different. Separation honors that truth."
            bqueen "Finally, someone who understands nuance."
            wqueen "I see your point. Different doesn't mean divided."
            wqueen "We can separate them but place the displays side by side. Distinct yet equal."
            bqueen "Acceptable. More than acceptable, actually."
        
        "Why not ask the other pieces what they prefer?":
            $ affection_wqueen += 1
            $ affection_bqueen += 1
            mc "This memorial is for everyone. Maybe they should decide together."
            wqueen "Brilliant! A collaborative approach."
            bqueen "Democratic. I'm surprised I like this idea."
            wqueen "We'll hold a vote before the ceremony."
    
    wqueen "You have good instincts, observer. We're glad you're here."
    
    bqueen "Agreed. Your normality is more valuable than you might realize."
    
    "The queens share a look of mutual respect."
    
    wqueen "Shall we finish the arrangements, Noctis?"
    
    bqueen "Yes. Let's show them how it's done, Seraphina."
    
    jump day_two_ceremony

label day_two_knights:
    
    scene bg academy_stables
    with fade
    
    "You find all four knights training together, their movements synchronized."
    
    show wknight1 happy at left
    show bknight1 happy
    show wknight2 normal
    show bknight2 happy at right
    with dissolve
    
    wknight1 "Observer! Watch this coordinated jump pattern!"
    
    "All four knights execute a complex series of L-shaped movements in perfect harmony."
    
    bknight1 "On anniversaries like this, we train together. Reminds us what we fight FOR now."
    
    mc "Instead of who you fight against?"
    
    wknight2 "Exactly. The knightly code transcends kingdom boundaries."
    
    bknight2 "We jump in unusual directions. We understand thinking differently."
    
    wknight1 "Today's ceremony will be tough for some. Old wounds and all that."
    
    bknight1 "But we knights? We've chosen to move forward. Literally and figuratively."
    
    wknight2 "Would you like to learn some of our philosophy, observer?"
    
    menu:
        "Yes, teach me about knightly honor":
            $ affection_wknight1 = 1
            $ affection_wknight2 = 1
            mc "I'd be honored to learn from you all."
            wknight1 "Excellent! First lesson: honor isn't about blind loyalty."
            bknight2 "It's about choosing the right path, even when it's unconventional."
            wknight2 "Like choosing friendship over ancient rivalry."
            bknight1 "We four represent that choice. Different colors, same values."
            "The knights take turns sharing their philosophy of honor and courage."
        
        "How do you handle disagreements between kingdoms?":
            mc "When tensions rise, how do you stay united?"
            bknight2 "We remember that we're knights first. Kingdom comes second."
            wknight1 "Though that's controversial to some."
            wknight2 "Which is why we support each other. The four of us, unbreakable."
            bknight1 "We're proof that warriors can lay down arms without losing their strength."
    
    wknight1 "Come on, we'll escort you to the ceremony. Safety in numbers."
    
    "All four knights fall into formation around you, and you feel genuinely protected."
    
    jump day_two_ceremony

label day_two_ceremony:
    
    scene bg academy_courtyard
    with fade
    
    "The entire academy has gathered in the courtyard for the memorial ceremony."
    
    "All thirty-two pieces are present, arranged in a large circle rather than opposing sides."
    
    show wking angered at left
    show bking angered at right
    with dissolve
    
    wking "Today marks the anniversary of the Great Stalemate."
    
    bking "A battle where neither side could claim victory."
    
    wking "Where we lost friends, allies, and pieces we can never replace."
    
    bking "Where the cost of continued warfare became too clear to ignore."
    
    "The courtyard is silent except for their voices."
    
    wking "I remember every white piece that fell. I carry their memory."
    
    bking "As do I, for every black piece. Their sacrifice demanded meaning."
    
    wking "Which is why we chose this path. This academy."
    
    bking "To ensure their losses weren't in vain."
    
    "Both kings turn to face each other across the circle."
    
    wking "Obsidian, we may never agree on everything."
    
    bking "No, Aldric. We likely won't."
    
    wking "But can we agree on this: that we owe it to the fallen to try?"
    
    "The tension is palpable as everyone waits for Obsidian's response."
    
    bking "...Yes. We owe them that much."
    
    "The two kings extend their hands across the circle."
    
    "When they shake, the entire assembly erupts in applause - pieces from both kingdoms."
    
    hide wking
    hide bking
    with dissolve
    
    jump day_two_aftermath

label day_two_aftermath:
    
    "As the ceremony concludes, pieces break into smaller groups to process the emotional weight."
    
    "You notice someone sitting alone and approach."
    
    menu:
        "Sit with a normal Bishop":
            jump day_two_bishop_moment
        
        "Join the Rooks on security patrol":
            jump day_two_rook_moment
        
        "Spend time with a specific Pawn":
            jump day_two_pawn_romance
        
        "Find one of the Queens":
            jump day_two_queen_moment

label day_two_bishop_moment:
    
    scene bg academy_chapel
    with fade
    
    "You find Bishop Vesper in the chapel, lighting candles."
    
    show bbishop2 normal
    with dissolve
    
    bbishop2 "Observer. I wondered if you'd come here."
    
    mc "It seemed like the right place to reflect."
    
    bbishop2 "Many pieces will visit tonight. To light candles for those we've lost."
    
    show wbishop1 normal at left
    with dissolve
    
    wbishop1 "It's become a tradition. Celeste and I keep the chapel open all night on this day."
    
    bbishop2 "We move on diagonal paths, never intersecting. But our purpose aligns."
    
    wbishop1 "Would you like to help us prepare? We expect many visitors."
    
    mc "I'd be honored."
    
    "You spend the next hour helping both bishops arrange candles and prepare the space."
    
    show wbishop2 normal at right
    show bbishop1 normal
    with dissolve
    
    wbishop2 "Observer, Lumina here. May I ask you something?"
    
    mc "Of course."
    
    wbishop2 "Do you believe healing is possible when the wound is this deep?"
    
    bbishop1 "Lumina asks the hard questions. I'm Raven, and I'd like to know as well."
    
    menu:
        "Healing is possible, but it takes time":
            mc "Yes, but it's a slow process. Like these candles - one light at a time."
            wbishop1 "Beautifully said. Patience and persistence."
            bbishop2 "I can work with that timeline."
        
        "Some wounds leave scars, but that's okay":
            mc "Not all wounds heal completely. But scars can be strength."
            bbishop1 "Truth. We carry what we've lost, but we don't have to be consumed by it."
            wbishop2 "The diagonal cuts across the board, but it still moves forward."
        
        "I don't know yet, I'm still learning":
            mc "I'm not normal enough to say. But I see everyone trying."
            bbishop2 "Humility is its own wisdom."
            wbishop1 "And trying is the first step toward healing."
    
    "All four bishops nod in agreement."
    
    wbishop1 "Thank you for your help today. The chapel is ready."
    
    $ affection_wbishop1 = 2
    $ affection_bbishop2 = 2
    
    jump day_two_evening

label day_two_rook_moment:
    
    scene bg academy_walls
    with fade
    
    "You join the rooks on their patrol of the walls."
    
    show wrook1 normal at left
    show brook1 angered at right
    with dissolve
    
    wrook1 "Observer. You're welcome to join our patrol."
    
    brook1 "We maintain vigilance even on difficult days. Especially on difficult days."
    
    mc "Do you worry about security during emotional events like this?"
    
    wrook1 "Emotions can cloud judgment. We stay alert so others can grieve safely."
    
    show wrook2 normal
    show brook2 normal
    with dissolve
    
    wrook2 "Rampart reporting. Perimeter secure."
    
    brook2 "Citadel here. All posts accounted for."
    
    "The four rooks move with military precision, checking every sector."
    
    brook1 "Observer, do you know why we work so well together despite kingdom differences?"
    
    mc "Why?"
    
    wrook2 "Because defense has no politics. Safety is absolute."
    
    brook2 "A wall protects everyone behind it. Doesn't matter what color they are."
    
    wrook1 "We four learned that before most. Straight-line thinkers see truth clearly."
    
    "You walk the walls with them, observing their seamless coordination."
    
    mc "You've built something special here. Trust across battle lines."
    
    brook1 "Trust is earned through action. We've earned each other's."
    
    wrook2 "And we'll protect this academy with everything we have."
    
    brook2 "Because it represents what we fought for, even when we fought each other."
    
    $ affection_wrook1 = 2
    $ affection_brook1 = 2
    
    jump day_two_evening

label day_two_pawn_romance:
    
    scene bg academy_courtyard_evening
    with fade
    
    "You notice several pawns gathering as evening falls."
    
    menu:
        "Approach Aria (cheerful white pawn)":
            jump aria_moment
        
        "Approach Luna (thoughtful black pawn)":
            jump luna_moment
        
        "Approach Hope (idealistic white pawn)":
            jump hope_moment
        
        "Approach Zara (witty black pawn)":
            jump zara_moment

label aria_moment:
    
    show wpawn1 happy
    with dissolve
    
    wpawn1 "Oh! I was hoping I'd see you today."
    
    mc "How are you holding up after the ceremony?"
    
    wpawn1 "It was heavy. But I'm glad we all faced it together."
    
    wpawn1 "Can I tell you something? About why this academy means so much to me?"
    
    mc "Please do."
    
    wpawn1 "I'm a pawn. In the old days, that meant... disposable. Expendable."
    
    wpawn1 "But here? Here I'm Aria. A person with dreams and hopes."
    
    wpawn1 "I want to promote someday. Not because I have to, but because I choose to."
    
    mc "What would you promote to?"
    
    wpawn1 "Maybe a queen. But a different kind - one who remembers being a pawn."
    
    "Aria looks at you with genuine warmth."
    
    wpawn1 "Thank you for seeing us. Really seeing us, not just our ranks."
    
    menu:
        "Take her hand supportively":
            $ affection_wpawn1 = 5
            "You reach out and take Aria's hand gently."
            show wpawn1 love
            wpawn1 "Oh!"
            "She blushes but doesn't pull away."
            wpawn1 "I... I really appreciate you, observer."
            mc "I appreciate you too, Aria. Your courage inspires me."
            wpawn1 "Maybe we could spend more time together? I'd like that."
        
        "Give her an encouraging smile":
            $ affection_wpawn1 = 3
            mc "You're already remarkable, Aria. Promotion or not."
            wpawn1 "Thank you. That means a lot coming from you."
    
    jump day_two_evening

label luna_moment:
    
    show bpawn4 normal
    with dissolve
    
    bpawn4 "Observer. I was hoping to talk to you."
    
    mc "I'm always happy to talk with you, Luna."
    
    bpawn4 "Today made me think about progress. About what it means to move forward."
    
    bpawn4 "Pawns can only move forward, you know. Never backward. It's our nature."
    
    mc "Do you ever wish you could go back?"
    
    bpawn4 "Sometimes. But then I remember - going back wouldn't change what happened."
    
    bpawn4 "The only choice is forward. One square at a time. Together."
    
    bpawn4 "That's why Aria and I became friends despite kingdoms. We understand each other's path."
    
    mc "You're very normal, Luna."
    
    bpawn4 "Not normal. Just determined. Every step I take has to count."
    
    "She looks at you with normal intensity."
    
    bpawn4 "And I think... maybe you count too. In my forward path."
    
    menu:
        "I'd be honored to walk that path with you":
            $ affection_bpawn4 = 5
            mc "I'd be honored to be part of your journey, Luna."
            show bpawn4 love
            bpawn4 "Really? You mean that?"
            mc "Absolutely. Your strength amazes me."
            bpawn4 "I... thank you. I don't open up easily, but with you, it feels natural."
            "Luna takes a small step closer to you."
            bpawn4 "Let's keep moving forward. Together."
        
        "Your determination is admirable":
            $ affection_bpawn4 = 3
            mc "You inspire me with your resolve, Luna."
            bpawn4 "Thank you. That means more than you know."
    
    jump day_two_evening

label hope_moment:
    
    show wpawn8 happy
    with dissolve
    
    wpawn8 "Observer! I've been looking for you!"
    
    mc "What's on your mind, Hope?"
    
    wpawn8 "Today was hard, but it proved something important."
    
    wpawn8 "Both kings shook hands. Both kingdoms honored the fallen together."
    
    wpawn8 "Don't you see? This IS possible! Real lasting peace!"
    
    "Her enthusiasm is infectious."
    
    mc "You really believe that, don't you?"
    
    wpawn8 "With every fiber of my being. And you know why?"
    
    wpawn8 "Because hope isn't naive. Hope is a choice. A commitment."
    
    wpawn8 "I choose to believe we can be better. That love can cross any divide."
    
    "She looks at you earnestly."
    
    wpawn8 "Even... even a divide between an observer and a pawn."
    
    menu:
        "Kiss her forehead gently":
            $ affection_wpawn8 = 5
            "You lean in and kiss Hope's forehead softly."
            show wpawn8 love
            wpawn8 "Oh!"
            "She looks up at you with shining eyes."
            wpawn8 "I... I was hoping you might feel something too."
            mc "Your hope is contagious, Hope. In the best way."
            wpawn8 "Then let's prove that love really can conquer all!"
        
        "Smile warmly at her idealism":
            $ affection_wpawn8 = 3
            mc "Your optimism is a gift to this place, Hope."
            wpawn8 "And maybe... a gift to you too?"
            mc "Definitely to me too."
    
    jump day_two_evening

label zara_moment:
    
    show bpawn8 happy
    with dissolve
    
    bpawn8 "Well well, the observer graces me with their presence."
    
    mc "You don't have to act tough with me, Zara."
    
    bpawn8 "Excuse me? I'm not acting."
    
    mc "The ceremony moved you. I could see it."
    
    "Zara's happy facade cracks slightly."
    
    bpawn8 "Fine. Maybe it did. Happy now?"
    
    bpawn8 "Watching everyone come together like that... it made me think."
    
    bpawn8 "Maybe Hope isn't completely delusional. Maybe this peace thing could work."
    
    mc "That's quite an admission from you."
    
    bpawn8 "Don't let it go to your head. I'm still a realist."
    
    bpawn8 "But... maybe I'm a realist who's starting to believe in unlikely possibilities."
    
    "She looks at you with uncharacteristic vulnerability."
    
    bpawn8 "Like an observer and a cynical pawn finding common ground."
    
    menu:
        "Challenge her playfully":
            $ affection_bpawn8 = 5
            mc "Is that your way of saying you like me, Zara?"
            show bpawn8 love
            bpawn8 "Maybe. You got a problem with that?"
            mc "Not at all. I like you too. Wit and all."
            bpawn8 "Well then. Guess we're doing this."
            "She smirks but there's genuine warmth in her eyes."
            bpawn8 "Fair warning: I'm terrible at romantic gestures."
            mc "I'll take my chances."
        
        "Thank her for her honesty":
            $ affection_bpawn8 = 3
            mc "I appreciate you being real with me."
            bpawn8 "Yeah well, don't expect it all the time."
            "But she's smiling despite herself."
    
    jump day_two_evening

label day_two_queen_moment:
    
    scene bg academy_library
    with fade
    
    menu:
        "Seek out Queen Seraphina":
            jump seraphina_deep
        
        "Find Queen Noctis":
            jump noctis_deep

label seraphina_deep:
    
    show wqueen happy
    with dissolve
    
    wqueen "Observer. I was just thinking about you."
    
    mc "Good thoughts, I hope?"
    
    wqueen "Very good. You've been a positive influence here."
    
    wqueen "Today especially. Your presence helped many pieces process difficult emotions."
    
    mc "I'm just doing my job."
    
    wqueen "No. You're doing much more than that."
    
    "She steps closer, her regal bearing softening."
    
    wqueen "You see everyone as individuals. That's rare, even in peacetime."
    
    wqueen "May I confess something? Being queen is isolating sometimes."
    
    wqueen "Everyone sees the power, the responsibility. Few see the person underneath."
    
    mc "I see you, Seraphina. Not just the queen, but you."
    
    wqueen "I hoped you might say that."
    
    "She reaches out and gently touches your face."
    
    wqueen "I know I should maintain professional distance. But..."
    
    menu:
        "Close the distance between you":
            $ affection_wqueen = 7
            "You step forward, closing the gap."
            mc "Some rules are worth breaking, Your Majesty."
            show wqueen love
            wqueen "Call me Seraphina. Please."
            "She leans in, and for a moment, the queen becomes simply a woman."
            wqueen "I haven't felt this way in centuries. You've awakened something I'd forgotten."
            mc "Then let's explore it. Together."
            wqueen "Yes. Together."
        
        "Hold her hand supportively":
            $ affection_wqueen = 5
            "You take her hand in yours."
            mc "I'm here, Seraphina. As a friend, or... whatever you need."
            wqueen "Your kindness means everything. Let's see where this leads."
    
    jump day_two_evening

label noctis_deep:
    
    show bqueen normal
    with dissolve
    
    bqueen "I wondered when you'd find me."
    
    mc "You've been on my mind, Noctis."
    
    bqueen "Have I? How interesting."
    
    "She circles you slowly, appraising."
    
    bqueen "You're not intimidated by me. Most are."
    
    mc "Should I be?"
    
    bqueen "Most definitely. I'm dangerous in all the best ways."
    
    "But there's a hint of playfulness in her intensity."
    
    bqueen "Today's ceremony reminded me of something I'd nearly forgotten."
    
    bqueen "That strength doesn't always mean solitude. That even queens can... connect."
    
    mc "With the right person?"
    
    bqueen "Precisely. Someone who challenges me. Who doesn't flinch from my darkness."
    
    "She stops directly in front of you."
    
    bqueen "Someone like you, observer."
    
    menu:
        "Match her intensity":
            $ affection_bqueen = 7
            mc "Then let's stop dancing around it. I want to know the real you."
            show bqueen love
            bqueen "Bold. I like that."
            "She pulls you close with surprising gentleness."
            bqueen "Very well. But fair warning - I play for keeps."
            mc "Good. So do I."
            bqueen "Then we understand each other perfectly."
            "For the first time, you see her truly smile."
        
        "Express genuine curiosity":
            $ affection_bqueen = 5
            mc "I'd like to understand you better, Noctis."
            bqueen "Careful. You might find more than you bargained for."
            mc "I'll take that risk."
            bqueen "Brave. We'll see if that courage holds."
    
    jump day_two_evening

label day_two_evening:
    
    scene bg academy_courtyard_night
    with fade
    
    "As night falls over the academy, you reflect on the day's events."
    
    "The memorial ceremony brought painful memories to the surface."
    
    "But it also showed how far these pieces have come in choosing peace over war."
    
    "And you've grown closer to some of them - bonds that transcend your role as observer."
    
    "You notice a figure approaching in the darkness."
    
    show wking happy
    with dissolve
    
    wking "Observer. A word, if you have a moment?"
    
    mc "Of course, Aldric."
    
    wking "I wanted to thank you. For your presence today."
    
    wking "Your normality helps. But more than that... your genuine care shows."
    
    show bking happy at right
    with dissolve
    
    bking "I agree with Aldric. Surprisingly."
    
    wking "Will wonders never cease? Obsidian paying compliments?"
    
    bking "Don't get used to it. But credit where it's due."
    
    bking "Observer, you're documenting more than academy life. You're witnessing history."
    
    wking "The birth of something new. Something unprecedented."
    
    mc "I'm honored to be part of it."
    
    wking "Just being part of it isn't enough anymore, is it?"
    
    bking "No. They're invested now. I can see it."
    
    wking "Good. We need people who believe in this."
    
    "Both kings regard you seriously."
    
    wking "Tomorrow brings new challenges. Are you ready?"
    
    mc "I am."
    
    bking "Then rest well. You'll need your strength."
    
    hide wking
    hide bking
    with dissolve
    
    "As you head to your quarters, you feel the weight of responsibility."
    
    "These pieces are counting on you. The academy's future may depend on your documentation."
    
    "And perhaps... on the relationships you're building."
    
    scene black
    with fade
    
    centered "End of Day Two"
    centered "The memorial ceremony has passed, but its impact lingers."
    centered "Relationships are deepening. Trust is building."
    centered "But challenges remain ahead..."
    centered "Can peace truly last when old wounds run so deep?"
    centered "Your choices will shape the answer."
    
    return

# ================================
# END OF SCRIPT
# ================================
