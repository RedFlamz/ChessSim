## Chess Romance: A Dating Sim on the Board
## script.rpy

# ================================
# CHARACTER DEFINITIONS - WHITE PIECES
# ================================

# White King
define wking = Character("King Aldric", color="#FFD700", image="wking")

# White Queen  
define wqueen = Character("Queen Solis", color="#F0E68C", image="wqueen")

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
    
    "As a new neutral observer assigned to document the lives of these legendary warriors, you'll witness their stories unfold."
    
    python:
        player_name = renpy.input("What is your name?", default="Alex", length=20)
        player_name = player_name.strip() or "Alex"
    
    scene bg academy_courtyard
    with fade
    
    "You arrive at the academy courtyard on your first day, clutching your observer's badge."
    
    "The pieces move about freely here, no longer bound to their battle formations."
    
    "Suddenly, a regal voice calls out behind you."
    
    show wking neutral
    with dissolve
    
    wking "Ah, you must be the new observer. I am King Aldric of the White Kingdom."
    
    wking "Welcome to our... unique institution. I trust you'll find your time here enlightening."
    
    mc "Thank you, Your Majesty. I'm honored to be here."
    
    wking "Please, formality serves little purpose in peacetime. Aldric will do."
    
    wking "Though I must warn you - not everyone here shares my optimism about this academy."
    
    show bking serious at right
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
    
    show wqueen elegant at left
    show bqueen mysterious at right
    with dissolve
    
    wqueen "Checkmate in seven moves, Noctis. You've left your king exposed."
    
    bqueen "How presumptuous. You forget I can move in all directions - including backward from mistakes."
    
    "The white queen notices your presence and smiles warmly."
    
    wqueen "Oh! You must be our new observer. I'm Queen Solis."
    
    wqueen "Don't mind our little game - Noctis and I have been rivals for centuries, but we play for enjoyment now."
    
    bqueen "Speak for yourself, Solis. I play to win."
    
    "The black queen's eyes gleam with competitive fire."
    
    bqueen "Queen Noctis of the Obsidian Court. Remember the name, observer."
    
    mc "You're both incredibly skilled. Do you enjoy teaching?"
    
    wqueen "Oh yes! I mentor the younger pieces. Power comes with responsibility."
    
    bqueen "I prefer to let students learn through trial and error. Harsh lessons stick."
    
    wqueen "We have different philosophies, but we both care deeply about our pieces."
    
    menu:
        "Ask Solis about her teaching methods":
            jump solis_route
        
        "Ask Noctis about her competitive spirit":
            jump noctis_route
        
        "Excuse yourself to meet the other pieces":
            jump explore_academy

label solis_route:
    
    $ affection_wqueen += 1
    
    hide bqueen
    with dissolve
    
    "Noctis returns to her chess problem, leaving you alone with Solis."
    
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
    
    "Solis excuses herself tactfully, giving you space with Noctis."
    
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
    
    show wknight1 confident
    with dissolve
    
    wknight1 "En garde!"
    
    "A silver-armored knight executes a perfect L-shaped jump, landing gracefully."
    
    wknight1 "Ah, the observer! Knight Sterling at your service."
    
    wknight1 "Care to see some unconventional tactics? We knights specialize in the unexpected."
    
    show bknight1 cool at right
    with dissolve
    
    bknight1 "Sterling, you're showing off again."
    
    "Another knight appears, moving in the same distinctive pattern."
    
    bknight1 "Knight Dante. Don't let Sterling's bravado fool you - we're equally matched."
    
    wknight1 "Equally matched? I seem to recall our last three sparring sessions went to me."
    
    bknight1 "You count differently in the White Kingdom. I count honestly."
    
    "They both laugh - clearly this is a friendly rivalry."
    
    mc "You two seem to get along well despite being from different kingdoms."
    
    wknight1 "Knights respect knights. We understand the burden of irregular movement."
    
    bknight1 "Plus, Sterling makes for good practice. Predictably unpredictable."
    
    wknight1 "I'll take that as a compliment."
    
    show wpawn1 cheerful at left
    with dissolve
    
    wpawn1 "Um, excuse me? Are you the observer everyone's talking about?"
    
    "A young white pawn approaches nervously."
    
    wpawn1 "I'm Aria. I just wanted to say... it's nice to have someone neutral here."
    
    wpawn1 "Sometimes the tension between kingdoms makes things awkward."
    
    mc "I can imagine. What's it like being a pawn in all this?"
    
    wpawn1 "Well... we're the most numerous, but also the most vulnerable."
    
    wpawn1 "But that's okay! We work together and protect each other."
    
    show bpawn4 thoughtful at right behind bknight1
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
    
    "The academy chapel is quiet, lit by diagonal rays of sunlight through tall windows."
    
    show wbishop1 serene
    with dissolve
    
    wbishop1 "Welcome, observer. I am Bishop Celeste."
    
    wbishop1 "This chapel serves all pieces, regardless of color. A true neutral space."
    
    mc "It's beautiful. Do you maintain it?"
    
    wbishop1 "Along with my counterpart, yes."
    
    show bbishop2 calm at right
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
    
    show wrook1 stoic
    with dissolve
    
    wrook1 "Halt. State your purpose."
    
    "A massive white rook blocks your path."
    
    mc "I'm the new observer. Just exploring the academy."
    
    wrook1 "Observer credentials verified. I am Rook Bastion, head of perimeter security."
    
    wrook1 "You may proceed, but stay within designated areas."
    
    show brook1 stern at right
    with dissolve
    
    brook1 "Bastion, stop interrogating visitors. I'm Rook Fortress."
    
    brook1 "We rooks take security seriously - straight lines, no deviation, absolute defense."
    
    wrook1 "Fortress and I coordinate all academy protection protocols."
    
    brook1 "Despite our allegiances, safety is paramount. An attack on one kingdom would endanger both."
    
    mc "That's very professional of you both."
    
    wrook1 "Professionalism is all we have. Personal feelings must not compromise structural integrity."
    
    brook1 "Agreed. Though I'll admit, Bastion's dedication is... admirable."
    
    "Bastion's stern expression softens slightly."
    
    wrook1 "As is Fortress's tactical acumen."
    
    "You sense a deep mutual respect between these two guardians."
    
    jump academy_evening

label academy_evening:
    
    scene bg academy_courtyard_evening
    with fade
    
    "As evening falls, pieces from both kingdoms gather in the courtyard for social time."
    
    show wpawn5 energetic at left
    show bpawn7 dramatic at center  
    show wpawn3 sweet at right
    with dissolve
    
    wpawn5 "Eden, reporting for duty! Well, social duty anyway."
    
    bpawn7 "Orion here. These evening gatherings are the highlight of academy life."
    
    wpawn3 "I'm Cara. Isn't the sunset beautiful? It touches both our kingdoms equally."
    
    "More pawns join the group."
    
    show wpawn2 nervous at left behind wpawn5
    with dissolve
    
    wpawn2 "Hi, I'm Beck. Sorry, I'm not great with new people..."
    
    wpawn5 "Beck's just shy! But they're super talented at chess problem-solving."
    
    show bpawn2 confident at right behind wpawn3
    with dissolve
    
    bpawn2 "Jasper's the name. These white pawns aren't so bad once you get to know them."
    
    show wpawn4 friendly
    with dissolve
    
    wpawn4 "Drew here! Want to join our game night?"
    
    show bpawn3 quiet
    with dissolve
    
    bpawn3 "I'm Kai. I usually just watch, but you're welcome to sit with me."
    
    "The pawns all chat animatedly, their individual personalities shining through."
    
    show wpawn6 optimistic at left
    show bpawn5 sarcastic at right
    with dissolve
    
    wpawn6 "Finn! Pleased to meet you! Isn't this academy amazing?"
    
    bpawn5 "Milo. It's... adequate. Though Finn's enthusiasm is infectious, I'll admit."
    
    show wpawn7 graceful
    show bpawn6 mysterious
    show wpawn8 hopeful
    show bpawn8 witty
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
    
    show wknight2 noble at left
    show bknight2 edgy at right
    with dissolve
    
    wknight2 "Ah, observer! I'm Knight Galahad, Sterling's partner."
    
    wknight2 "Unlike my show-off colleague, I believe in quiet competence."
    
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
    
    show wbishop2 wise at left
    show bbishop1 mysterious at right
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
    
    show wrook2 disciplined at left
    show brook2 tactical at right
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
    
    show wking thoughtful at left
    show bking contemplative at right
    with dissolve
    
    wking "Ah, observer. Obsidian and I hold these private summits regularly."
    
    bking "To ensure our... truce remains stable."
    
    wking "Please, join us. Your neutral perspective could help."
    
    mc "What are you discussing tonight?"
    
    bking "The future. Whether this academy is sustainable or merely delaying inevitable conflict."
    
    wking "I believe in its potential. We've already seen pieces form bonds across kingdom lines."
    
    bking "Bonds that could shatter at the first sign of real disagreement."
    
    wking "Or bonds that could prevent disagreement from becoming warfare."
    
    "The two kings regard each other with a complex mix of respect and wariness."
    
    bking "Tell me, observer. In your neutral opinion, can natural enemies truly become allies?"
    
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
            wking "An honest answer. We appreciate your thoughtfulness."
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
    
    return

# ================================
# END OF SCRIPT
# ================================
