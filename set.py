import pygame

# '''setting'''
FPS = 60
fpsClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("My cat")
screen_coord = (1080, 800)
notif_screen_coord = (1080 + 400 - 116, 800)
screen_center = (1080 / 2, 720 / 2)
image_One_rect = (0, 0)
field = 15

# colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode(notif_screen_coord)

# загрузка картинок
background = pygame.image.load("background_main.jpg")
notif_backgroung = pygame.image.load("background_notif.jpg")
Green_Button = pygame.image.load("BUTTON_GREEN.png")
Red_Button = pygame.image.load("BUTTON_RED.png")
notification_1 = pygame.image.load("notifiaction_1.png")
menu_bg = pygame.image.load("menu_bg.jpg")
cat_sprite_2 = pygame.image.load("cat_sprit_3.png")
notification_2 = pygame.image.load("notifiaction_2.png")
notif_you_win = pygame.image.load("notif_you_win.png")
notif_you_lose = pygame.image.load("notif_you_lose.png")

# button menu
BUTTON_RESTART_GAME = pygame.image.load("BUTTON_RESTART.png")
BUTTON_CLOSE_GAME = pygame.image.load("BUTTON_OUT_GAME.png")

# transform
Green_Button = pygame.transform.scale(Green_Button, (64, 56))
Green_Button = pygame.transform.rotate(Green_Button, 90)
Red_Button = pygame.transform.scale(Red_Button, (62, 55))
Red_Button = pygame.transform.rotate(Red_Button, 90)
bg_img = pygame.transform.scale(background, (screen_coord[0] - 116, screen_coord[1]))
notification_1 = pygame.transform.scale(notification_1, (400, 200))
notification_2 = pygame.transform.scale(notification_2, (400, 200))
BUTTON_CLOSE_GAME = pygame.transform.scale(BUTTON_CLOSE_GAME, (120, 50))
BUTTON_RESTART_GAME = pygame.transform.scale(BUTTON_RESTART_GAME, (120, 50))
notif_backgroung = pygame.transform.scale(notif_backgroung, (500, 520))
menu_bg = pygame.transform.scale(menu_bg, (400, 300))
cat_sprite_2 = pygame.transform.scale(cat_sprite_2, (55, 50))
notif_you_win = pygame.transform.scale(notif_you_win, (500, 300))
notif_you_lose = pygame.transform.scale(notif_you_lose, (500, 300))

# coords menu batton
coord_button_out = (1200 - 116, 600)
coord_button_restart = (0, 0)

screen.blit(menu_bg, (1080 - 116, 520))
button_out_rect = pygame.draw.rect(screen, RED, (coord_button_out[0], coord_button_out[1], 120, 50))
screen.blit(BUTTON_CLOSE_GAME, coord_button_out)
# кнопка рестарта
button_restart_rect = pygame.draw.rect(screen, RED, (coord_button_out[0], coord_button_out[1]+100, 120, 50))
screen.blit(BUTTON_RESTART_GAME, (coord_button_out[0], coord_button_out[1] + 100))

# setting for drawing fild
point_2 = 45
circle_list = []
button_list = []

# случайное кол-во закрашенных стен
ready_walls_const_count = 30

# начальное положение кота
defolt_cat_to_pos = 112

# не строить здесь!
not_build_here = [80, 81, 82, 83, 84, 96, 97, 98, 99, 110, 111, 112, 113, 114, 126, 127, 128, 129, 140, 141, 142, 143,
                  144]
                            # '''setting_end'''