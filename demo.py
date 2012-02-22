import darc
import pygame
import time

if __name__ == "__main__":
	darc.set_key("TEST")
	darc.set_data_dir("demo/")
	darc.create_darc()
	imagefile = darc.get_file("demo/test", "test.gif")
	image = pygame.image.load(imagefile, "test.gif")
	screen = pygame.display.set_mode((100, 100))
	screen.blit(image, (0,0))
	pygame.display.flip()
	time.sleep(2)