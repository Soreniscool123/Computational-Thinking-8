# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()
stage.set_background("1000s")
player = codesters.Sprite("gulper", 0, -215)
player.set_size(0.25)
hunger = 5
object_speed = -2


# Section 2 - objects


def falling_object():
    global object_speed, hunger

    hunger += 0.5
    if hunger > 0 and hunger < 10:
        x = random.randint(-250, 250)
        y = 300
        object = codesters.Sprite("sfss", x, y)
        object.set_y_speed(object_speed)
    else:
        player.say("you starved")
stage.event_interval(falling_object, 4)

    
#section 3 - Collision
def collision(player, object):
    global hunger

    if object.get_image_name() == "sfss":
        stage.remove_sprite(object)
        hunger -= 1
        if hunger == 0:
            player.say(f"your full, you lose",5)
        else:
            player.say(f"{hunger} hunger",0.5)
player.event_collision(collision)
    
  # Section 4 - movement  
def go_right():
    player.move_right(10)

player.event_key("right", go_right)
def go_left():
    player.move_left(10)

player.event_key("left", go_left)

    
    
    
    
    