#Definitions

#Images
image bitch11 = "images/bitch11.png"
image bg space = "images/space.jpg"
image bg skyday = ("images/skyday.jpg")
image scp173 = ("images/SCP173.png")
image bg black = ("images/bg black.jpg")
image doc173 = ("images/doc173.jpg")
image mtf = ("images/MTF.png")
image mtf1 = ("images/MTF1.png")
image FakeX = ("images/Capture1.png")
image CI = ("images/CI.png")
image Splash = ("images/Load.png")
image bg white = ("images/white.jpg")
image Splash1 = ("images/Splash1.jpg")
image Splash2 = ("images/Splash2.jpg")
image help = ("images/Help.jpg")

#Audio
define NeckSnap1 = ("audio/NeckSnap1.ogg")
define NeckSnap2 = ("audio/NeckSnap2.ogg")
define NeckSnap3 = ("audio/NeckSnap3.ogg")
define Rattle1 = ("audio/Rattle1.ogg")
define Rattle2 = ("audio/Rattle2.ogg")
define Rattle3 = ("audio/Rattle3.ogg")
define PeanutMove = ("audio/173Move.mp3")
define Alarm10 = ("audio/Alarm10.ogg")
define Alarm11 = ("audio/Alarm11.ogg")
define Alarm = ("audio/Alarm.ogg")
define SS1 = ("audio/StartSequence1.ogg")
define Gunshot = ("audio/Gunshot.ogg")
define Refuse = ("audio/Refuse.ogg")
define Txt = ("audio/Vibrate.ogg")
define doc = ("audio/DocPickup.ogg")
define MoveShort = ("audio/173MoveShort.ogg")


#Music
define BGM1 = ("audio/BGM1.ogg")
define Main = ("audio/Main.ogg")
define Main2 = ("audio/Main2.ogg")
define FM1 = ("audio/FM1.ogg")
define sad = ("audio/Sad.ogg")

#Characters
define mc = Character("[Player]")
define scp173 = Character("SCP 173")
define g1 = Character("Gaurd 1")
define g2 = Character("Gaurd 2")
define u = Character("???")
define s1 = Character("Soldier 1")
define s2 = Character("Soldier 2")

#Effects
screen tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150 #Screen tear appears above pretty much everything
    add Tear(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size (1280,720)
    on "show" action Function(hide_windows_enabled, enabled=False) #This makes sure UI is hidden
    on "hide" action Function(hide_windows_enabled, enabled=True)