import pygame
import random

#added my first comm
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x_pos= 0
        mole_y_pos = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    selected_x, selected_y = event.pos
                    mole_col = mole_x_pos // 32
                    mole_row = mole_y_pos // 32
                    print(selected_x , selected_y)
                    if selected_x // 32 == mole_col and selected_y // 32 == mole_row:
                        mole_x_pos = random.randrange(0,609, 32)
                        mole_y_pos = random.randrange(0, 481, 32)


                    print(mole_x_pos)
                    print(mole_y_pos)

            screen.fill("light green")

            for x_val in range(0, 640, 32):
                pygame.draw.line(screen, "dark blue", (x_val, 0), (x_val, 512))
            for y_val in range(0, 512, 32):
                pygame.draw.line(screen, "dark blue", (0, y_val), (640, y_val))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x_pos, mole_y_pos)))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
