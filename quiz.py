print("Welcome to Playstation's fan Quiz!!!")
answer_user = input("Shall we Start? (Y/N)")

if answer_user != "Y":
    exit(0)

print("Starting...")

points = 0 

print("Initial Points ", points)

print("Who developed GTA V?")
print("\t(A) EA Sports")
print("\t(B) Bethesda")
print("\t(C) Rockstar Games")
print("\t(D) EA Sports")

option = input(" ")

if option == "C":
    points += 1

    print("Which of these games was developed by Naughty Dog and released exclusively for PlayStation?")
print("\t(A) Halo: Combat Evolved")
print("\t(B) The Last of Us")
print("\t(C) Gears of War")
print("\t(D) Forza Horizon")
option = input(" ")
if option.upper() == "B":
    points += 1

print("\nWhat was the first PlayStation console to include a built-in Blu-ray player?")
print("\t(A) PlayStation 1")
print("\t(B) PlayStation 2")
print("\t(C) PlayStation 3")
print("\t(D) PlayStation Portable (PSP)")
option = input(" ")
if option.upper() == "C":
    points += 1

print("\nWhich of these iconic PlayStation characters is known for wielding a giant key as a weapon?")
print("\t(A) Kratos (God of War)")
print("\t(B) Sora (Kingdom Hearts)")
print("\t(C) Nathan Drake (Uncharted)")
print("\t(D) Aloy (Horizon Zero Dawn)")
option = input(" ")
if option.upper() == "B":
    points += 1

print("\nWhat is the name of the virtual reality (VR) headset released by Sony for PlayStation?")
print("\t(A) PlayStation VR")
print("\t(B) PlayStation AR")
print("\t(C) PlayStation Holo")
print("\t(D) PlayStation Vision")
option = input(" ")
if option.upper() == "A":
    points += 1

print("\nIn God of War (2018), who is Kratos’ son?")
print("\t(A) Atreus")
print("\t(B) Deimos")
print("\t(C) Zeus")
print("\t(D) Baldur")
option = input(" ")
if option.upper() == "A":
    points += 1

print("\nWhich of these franchises was NOT originally a PlayStation exclusive?")
print("\t(A) Uncharted")
print("\t(B) Bloodborne")
print("\t(C) Final Fantasy VII (Original 1997 release)")
print("\t(D) Gears of War")
option = input(" ")
if option.upper() == "D":
    points += 1

print("\nWhat was the codename for the PlayStation 5 before its official reveal?")
print("\t(A) Project Morpheus")
print("\t(B) Next-Gen PlayStation")
print("\t(C) PlayStation X")
print("\t(D) PlayStation Neo")
option = input(" ")
if option.upper() == "B":
    points += 1

print("\nWhich PlayStation game features a protagonist named Jin Sakai fighting against Mongol invaders?")
print("\t(A) Ghost of Tsushima")
print("\t(B) Sekiro: Shadows Die Twice")
print("\t(C) Nioh")
print("\t(D) Tenchu: Stealth Assassins")
option = input(" ")
if option.upper() == "A":
    points += 1

print("\nWhat is the name of the subscription service that gives players access to a library of classic PlayStation games?")
print("\t(A) PlayStation Now")
print("\t(B) PlayStation Plus Premium")
print("\t(C) PlayStation Classics")
print("\t(D) PlayStation Retro")
option = input(" ")
if option.upper() == "B":
    points += 1

print("\nWhich of these villains is NOT from a PlayStation-exclusive game?")
print("\t(A) Sephiroth (Final Fantasy VII)")
print("\t(B) Rafe Adler (Uncharted 4)")
print("\t(C) Baldur (God of War)")
print("\t(D) Bowser (Super Mario)")
option = input(" ")
if option.upper() == "D":
    points += 1

print("Total Points: ", points)