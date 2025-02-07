import codesters
from codesters import StageClass
stage = StageClass()


player = codesters.Sprite("gulp")
object = codesters.Sprite("hotdawg")
stage.set_background("1000s")

object.size(2)
player.event_key("a", "left")
player.event_key("d", "right")
#starting speed
object_speed = 50
#use += or -= on the line below