label CH01:
    init python:
        import os

    scene bg skyday
    with fade
    play music BGM1
    pause 0.5

    "It's a normal day like any other."
    "I get up, get dressed, eat, and leave for work."
    "Everything appeared normal, until now."
    play audio Txt
    "What?"
    stop music fadeout 1.0
    "I look at my phone to see an emergency alert message."
    "It's just a link."
    "I click the link, and it brings me to a site with only 1 string of text, and an image"
    u "The following is a message composed via consensus of the O5 Council."
    play sound doc
    show doc173
    pause 3.0
    "..."
    play sound doc
    hide doc173
    "Is this a joke?"
    "Underneath the image, I see some more text."
    u "Object number SCP\-\173 has breached containment and is heading for your area."
    u "Please stay inside until further notice."
    "There's no way this can be real."
    u "If you see SCP-173, do not panic."
    u "Just keep staring, do not blink, and call 911."
    "..."
    "No..."
    u "If you are in a group, alert one another before blinking, as the object can move a considerable distance in the time it takes for the human eye to blink."
    "That symbol, it feels so familiar to me."
    u "Further instructions will come shortly."
    "..."
    play sound MoveShort
    pause 0.2
    show scp173
    mc "Ahh!"
    play sound Rattle2
    scp173 "I don't have very long, I should make quick work of this one and move on."
    "I'm shocked, and silent."
    mc "They never said this thing could talk."
    scp173 "..."
    play sound Rattle3
    scp173 "You can understand me?"
    mc "Yeah, I can." 
    mc "I'm assuming that doesn't happen often?"
    play sound Rattle1
    scp173 "Not at all, you're the first person to be able to understand me."
    "But it doesn't matter."
    "It's too late for me. They told me not to blink in front of it, but it's too hard."
    "I can't keep my eyes open any longer."
    hide scp173
    scene bg black
    pause 2.0
    "..."
    pause 2.0
    "?"
    pause 1.0
    scene bg skyday
    with fade
    show scp173
    mc "You didn't kill me?"
    play sound Rattle2
    scp173 "Of course not, why would I kill the only one who can talk to me?"
    play music BGM1
    mc "I guess that makes sense, I just thought you were supposed to snap peoples necks if they so much as blinked."
    play sound Rattle1
    scp173 "And normally I do, but I literally just said-{nw}"
    mc "Alright, I get it."
    play sound Rattle3
    scp173 "No!"
    stop music fadeout 1.0
    "Just then, I hear someone shout out..."
    show mtf at left
    show mtf1 at right
    u "Blinking!"
    play music FM1
    "What the hell?"
    "I look to my left to see 2 armed soldiers."
    s1 "Keep staring!"
    "Right, I forgot about that."
    play sound Rattle1
    scp173 "Wait! You have to tell them you can talk to me!"
    play sound Rattle2
    scp173 "It's my only chance at freedom, please!"
    "I don't know what to do."
    "I'm in shock."
    "My whole life{nw}"
    "Has turned around{nw}"
    "In one day.{nw}"
    "what do i do?{nw}"
    "PLEASE!{nw}"
menu:
    "Tell them.":
        jump Y1
    "Don't tell them.":
        jump N1

label Y1:
mc "Wait!"
s1 "Don't interrupt us unless it's important!"
mc "It is!"
"The soldier is looking at me, forgetting about SCP-173 completely."
s1 "Out with it!"
"I can't speak, I don't know why."
"I'm frozen, fear has taken a hold of my body."
s2 "I need to blink!"
"He looks back to SCP-173."
s1 "Don't get in the way again."
"I swallow."
jump E1
    
label N1:
"I keep staring at SCP-173."
pause 1.0
"I'm so sorry."
"I can't, I physically can't"
"I swallow."
jump E1
    
label E1:
python:
    try: sys.modules['renpy.error'].report_exception("Can you hear me?", False)
    except: pass
stop music
hide mtf
hide mtf1
hide scp173
show layer master
show layer screens
show FakeX onlayer overlay
"."
play sound glitch
hide FakeX
show CI onlayer overlay
$ persistent.ch01 = True
pause 0.50




#if renpy.exists('YES.txt'):
#    call CH02 from _call_CH02
$ renpy.quit(relaunch=True)






stop music fadeout 1.0
scene bg black
with fade
return 