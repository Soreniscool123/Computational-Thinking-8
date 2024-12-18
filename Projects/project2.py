# Beginning

ski_points = 0
snowboard_points = 0

# Middle

answer = input("Would you rather A) Learn quickly, or B) learn slowly?\n")
if answer == "A":
    ski_points += 1
elif answer == "B":
    snowboard_points += 1
answer = input("Would you rather A) Master a sport faster, or B) have more skills to progress?\n")
if answer == "A":
    snowboard_points += 1
elif answer == "B":
    ski_points += 1
answer = input("Do you prefer A) hockey, or B) skateboarding?\n")
if answer == "A":
    ski_points += 1
elif answer == "B":
    snowboard_points += 1
answer = input("which sounds better A) going very fast, or B) going slowly and playfully ?\n")
if answer == "A":
    ski_points += 1
elif answer == "B":
    snowboard_points += 1
answer = input("Do you want friends A) no, or B) yes?\n")
if answer == "A":
    snowboard_points += 1
elif answer == "B":
    ski_points += 1
answer = input("Are you interested in backcountry A) yes, or B) no?\n")
if answer == "A":
    ski_points += 1
elif answer == "B":
    snowboard_points += 1
answer = input("Would you rather A) drive a motorcycle, or B) drive a sports car?\n")
if answer == "A":
    snowboard_points += 1
elif answer == "B":
    ski_points += 1

# End

if ski_points > snowboard_points:
    print("you should try skiing")
elif snowboard_points > ski_points:
    print("you should try snowboarding")
elif ski_points == snowboard_points:
    print("you should try skiing")