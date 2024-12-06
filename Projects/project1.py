###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("winter")
q1 = codesters.Square (100, 100, 200, 'blue')
q2 = codesters.Triangle (-100, 60, 200, 'orange')
q3 = codesters.Square (-100, -100, 200, 'red')
q4 = codesters.Circle (100, -100, 200, 'black')
s1 = codesters.Sprite ("drake", 100, 100)
s2 = codesters.Sprite ("ski", -80, -100)
s1.set_size(0.5)
s2.set_size(0.5)
s4 = codesters.Sprite ("food", 100, -100)
s4.set_size(0.15)
s3 = codesters.Sprite ("chillguy", -100, 65)
s3.set_size(0.1)
message1 = codesters.Text("Soren",0,220, "black")
message2 = codesters.Text("cool coat of arms",0,-220, "black")
s5 = codesters.Sprite ("hotdawg", 0, 0)
s5.set_size(0.1)