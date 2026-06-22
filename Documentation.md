# STMSGE_OOP Engine Documentation

Eine einfache 2D Python Game Engine basierend auf Pygame.

---

# 🚀 ENGINE

## Erstellung

```python
Engine(width, height, title)

Beispiel:

engine = Engine(800, 600, "Mein Spiel")
Methoden
add_object

Fügt ein Objekt zur Engine hinzu:

engine.add_object(obj)
remove_object

Entfernt ein Objekt:

engine.remove_object(obj)
run

Startet die Game Loop:

engine.run()
Eigenschaften
screen → Zeichenfläche
clock → FPS Steuerung
objects → alle GameObjects
debug → Hitbox Debug (F9)
osd → HUD System
buttons → UI Buttons
🎮 GAMEOBJECT

Basis für alle Objekte.

Pflichtmethoden
update(dt)
draw(screen)
Kollision
obj.touch(other)

Beispiel:

if player.touch(point):
    print("Collision!")
Hitbox Update
obj.update_hitbox()
👤 PLAYER
Player(x, y, sprite, speed, controls)
Beispiel
player = Player(100, 100, sprite, 250, {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "up": pygame.K_w,
    "down": pygame.K_s
})
🧱 NPC

Statisches Objekt ohne Bewegung.

NPC(x, y, sprite)
🖼 SPRITE
Sprite(path)
🔊 AUDIO
SOUND
Sound(path).play()
MUSIC
Music.load(path)
Music.play()
🎞 ANIMATION
SimpleAnimation(frame_w, frame_h, max_frames)
Methoden
anim.update(dt)
anim.set_row(row)
anim.get_rect()
🖱 BUTTON SYSTEM
Erstellung
Button((x, y, width, height))
engine.add_button(button)
Nutzung
if button.pressed():
    print("Button gedrückt")
📢 OSD SYSTEM
engine.osd.add("Text", duration, color)
Beispiele
engine.osd.add("Spiel gestartet!", 3)
engine.osd.add("+1 Punkt", 1.5, (0,255,0))
engine.osd.add("Warnung!", 2, (255,0,0))
🔧 DEBUG MODE

F9 → Hitboxen an/aus

🎮 GAME LOOP
Input Events
Update Objects
Collision Check
Draw Objects
Draw OSD + UI
Display Flip
⚡ BEISPIEL
if player.touch(point):
    engine.osd.add("Collected!", 2)
