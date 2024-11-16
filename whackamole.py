import pygame

#added my first comm
def main():
    x_val = 0
    y_val = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
            screen.fill("light green")
            for x_val in range(0, 640, 16):
                pygame.draw.line(screen, "dark blue", (x_val, 0), (x_val, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            for y_val in range(0, 512, 16):
                pygame.draw.line(screen, "dark blue", (0, y_val), (640, y_val) )
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
