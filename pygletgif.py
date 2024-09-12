# Pacote "Leitão" para display de janelas e multimídia
import pyglet as pg

file = "gifs/Miss-ezgif.com-crop.gif"

animation = pg.resource.animation(file)
sprite = pg.sprite.Sprite(animation)

win = pg.window.Window(fullscreen=True)
sprite.x = win.width // 2 - sprite.width // 2
sprite.y = win.height // 2 - sprite.height // 2
color = 1,1,1,1
pg.gl.glClearColor(*color)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pg.app.run()