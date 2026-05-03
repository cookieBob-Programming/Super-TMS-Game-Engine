import pygame

from STMSGE_OOP import Engine, Player, NPC, load_sprite, Music



def main():
    engine = Engine(800, 600, "Test Game")

    # Load Sprites
    player_sprite = load_sprite("../Sprites/Costumes/MUDKIP.png")
    npc_sprite = load_sprite("../Sprites/Costumes/MORPEKO.png")
    npc2_sprite = load_sprite("../Sprites/Costumes/CHIKORITA.png")
    player2_sprite = load_sprite("../Sprites/Costumes/ABSOL.png")
    player2_controls = {    "left": pygame.K_a,
    "right": pygame.K_d,
    "up": pygame.K_w,
    "down": pygame.K_s}


#macht object
    player = Player(100, 100, player_sprite, 100)
    npc = NPC(400, 300, npc_sprite)
    npc2 = NPC(500, 400, npc2_sprite)
    player2 = Player(200, 200, player2_sprite, 100, player2_controls)

    engine.add_object(player)
    engine.add_object(npc)
    engine.add_object(npc2)
    engine.add_object(player2)

    music = Music()
    music.load("../sounds/title_origin.ogg")
    music.play()



    engine.run()





if __name__ == "__main__":
    main()