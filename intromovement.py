# Setup
import codesters
from codesters import StageClass
Stage = StageClass()

Stage.set_background("moon")
s1 = codesters.Sprite("person2", 0, -200)
s1.set_size(0.5)

# Define controls
def move_up(sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_left(sprite):
    sprite.move_left(10)

def move_right(sprite):
    sprite.move_right(10)

def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 1)

def turn_right(sprite):
    heading = sprite.heading
    sprite.set_heading(heading - 1)

def forward(sprite):
    sprite.forward(1)


# Im not typing all that
def hide(sprite):
    sprite.hide()

def show(sprite):
    sprite.show()


# Bind controls to keys
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s1.event_key("h", hide)
s1.event_key("g", show)

s2 = codesters.Sprite("chillguy", 0, 200)
s2.set_size(0.25)
s2.event_key("up", move_up)
s2.event_key("down", move_down)
s2.event_key("left", move_left)
s2.event_key("right", move_right)
s2.event_key("k", hide)
s2.event_key("j", show)

s3 = codesters.Sprite("character2", 0, 100)
s3.set_size(0.5)
s3.event_key("spacebar", move_up)