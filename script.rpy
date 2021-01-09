label splashscreen:
    scene bg white
    default persistent.ch01 = False
    if not persistent.ch01:
        default persistent.first_run = False
        if not persistent.first_run:
            show Splash1 at truecenter
            with dissolve
            pause 2.0
            hide Splash1 with dissolve
            pause 0.5

            show Splash2 at truecenter
            with dissolve
            pause 2.0
    
            menu:
                "I agree.":
                    $ persistent.first_run = True
                    hide Splash2 with dissolve
                    scene bg black with dissolve
                    pause 0.5
                    hide Splash2 with dissolve
                    scene bg black with dissolve
                    pause 0.5
                    scene bg white
                    pause 1.0
                
                    play music Main
                    show Splash at truecenter
                    with dissolve
                    pause 2.0
                    hide Splash with dissolve
                    scene bg black with dissolve
                    pause 0.5
                    return 
                "I don't agree.":
                    $ renpy.quit(relaunch=False)
        else:
            scene bg white
            pause 1.0
        
            play music Main
            show Splash at truecenter
            with dissolve
            pause 2.0
            hide Splash with dissolve
            scene bg black with dissolve
            pause 0.5
            return 
    else:
        play music Main
        show Splash at truecenter
        with dissolve
        pause 2.0
        hide Splash
        stop music
        show help
        play sound glitch
        pause 0.5
        hide help
        jump CH02

label start:
    stop music fadeout 1.0

    python:
        Player = renpy.input("What is your name?", length=32)
        Player = Player.strip()

        if not Player:
            Player = "D-9341"
    
    jump CH00