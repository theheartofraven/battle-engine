default name = "Player"
default currentplayer = "[name]"
default eventrunning = False
default _game_menu_screen = "preferences"

label load_setup:
    if not name:
        $ name = "Player"
    $ a.name = name
    call load_skills
    call load_monsters
    call load_items
    $ party_list = [a,y,c,f,r] # initial party list, including main character
    $ wild_monsters = [mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11]
    $ restorehp()
    $ restoremp()
    return
