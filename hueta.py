import random
import pygame
import sys

# import cats_mind

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

# bg
screen.blit(bg_img, image_One_rect)

# coords menu batton
coord_button_out = (1200 - 116, 600)
coord_button_restart = (0, 0)

screen.blit(menu_bg, (1080 - 116, 520))
button_out_rect = pygame.draw.rect(screen, RED, (coord_button_out[0], coord_button_out[1], 120, 50))
screen.blit(BUTTON_CLOSE_GAME, coord_button_out)

button_restart_rect = pygame.draw.rect(screen, RED, (coord_button_out[0], coord_button_out[1]+100, 120, 50))
screen.blit(BUTTON_RESTART_GAME, (coord_button_out[0], coord_button_out[1] + 100))

# setting for drawing fild
point_2 = 45
circle_list = []
button_list = []

# случайное кол-во закрашенных стен
ready_walls_const_count = 50

# начальное положение кота
cat_to_pos = 112

# '''setting_end'''


'''                            
                            функции говнокота и минного поля
'''
# поле уведолений
def notif_bg_up():
    screen.blit(notif_backgroung, (screen_coord[0] - 116, 0))

# ф-ция подтирание говна за котом
def blit_grenn_after_cars_move(but_coords):
    screen.blit(Green_Button, (but_coords[0] - 2, but_coords[1] - 10))


# поле
for i in range(field):
    point_1 = 45
    if i == 0:
        for j in range(field):
            # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
            circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
            circle_list.append(circle)

            butt_green = screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))
            button_list.append(butt_green)

            point_1 += 60

    elif i % 2 != 0:
        point_1 = 75

        for j in range(field):
            # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
            circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
            circle_list.append(circle)

            butt_green = screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))
            button_list.append(butt_green)

            point_1 += 60
    else:
        point_1 = 45
        for j in range(field):
            # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
            circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
            circle_list.append(circle)

            butt_green = screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))
            button_list.append(butt_green)

            point_1 += 60

    point_2 += 50

walls_array = [0] * len(circle_list)

for i in range(len(walls_array)):
    x = circle_list[i].x
    y = circle_list[i].y
    walls_array[i] = (False, x, y)

not_build_here = [80, 81, 82, 83, 84, 96, 97, 98, 99, 110, 111, 112, 113, 114, 126, 127, 128, 129, 140, 141, 142, 143,
                  144]

# границы поля ''''''
border_field = []
for i in range(field):
    border_field.append(i)
for i in range(211, 225):
    border_field.append(i)
vert = 15
for i in range(field):
    border_field.append(vert)
    vert += 15
vert = 29
for i in range(field):
    border_field.append(vert)
    vert += 15
print(border_field)
# ''''''

for j in range(ready_walls_const_count):
    random_wall_pos = random.randint(0, len(circle_list) - 1)
    if random_wall_pos not in not_build_here:
        walls_array[random_wall_pos] = (True, circle_list[random_wall_pos].x, circle_list[random_wall_pos].y)
    else:
        j -= 1


def Draw_red_walls():
    for wall in walls_array:
        if wall[0] == True:
            screen.blit(Red_Button, (wall[1] - 2, wall[2] - 9))



            # '''sprites'''
class Sprites_notif(pygame.sprite.Sprite):
    def __init__(self, image, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=(x, 100))

    def go_right(self, count_notif):
        if count_notif == 1:
            if self.rect.x < notif_screen_coord[0]:
                self.rect.x += 10
            if self.rect.x >= notif_screen_coord[0]:
                self.kill()

    def go_left(self, count_notif):
        if count_notif == 1:
            if self.rect.x > 1080 - 116:
                self.rect.x -= 10
            if self.rect.x <= 1080 - 116:
                self.rect.x = 1080 - 116


notif_1 = Sprites_notif(notification_1, x=1480 + 200)
notif_2 = Sprites_notif(notification_2, x=1480 + 200)

notif_watch = False
notif_go_back = False
notif_watch_2 = False
notif_go_back_2 = False

# '''sprites'''



screen.blit(cat_sprite_2, (circle_list[cat_to_pos][0] - 2, circle_list[cat_to_pos][1] - 3))


def step(mas, pred):
    i = pred[len(pred) - 1]
    if (i // 15) % 2 == 1:
        ns = [i - 1, i + 1, i - 15, i - 14, i + 15, i + 16]
    else:
        ns = [i - 1, i + 1, i - 15, i + 14, i + 15, i - 16]
    ans = []
    for j in ns:
        if mas[j] == False:
            ans.append([[j], pred])
    return ans


def cats_mind(mas, i):
    f = False
    mas[i] = True
    pred_1 = [i]
    next_stepold = []
    next_step = step(mas, pred_1)
    result = []
    while (f == False):
        while (next_stepold):
            g = next_stepold.pop()

            mas[g[0][0]] = True
            preda = []
            for p in g[1]:
                preda.append(p)

            preda.append(g[0][0])

            next_step += step(mas, preda)

        for j in next_step:
            if (j[0][0] < 15) or (j[0][0] > 209) or (j[0][0] % 15 == 0) or (j[0][0] % 15 == 14):
                f = True
        if next_step:
            next_stepold = next_step
        else:
            f = True
            return []
        next_step = []

    for h in next_stepold:
        if (h[0][0] < 15) or (h[0][0] > 209) or (h[0][0] % 15 == 0) or (h[0][0] % 15 == 14):
            if h[1][1] not in result:
                result.append(h[1][1])

    return result


game_win = False
game_lose = False

              # '''main cycle'''
while True:
    fpsClock.tick(FPS)
    pos = pygame.mouse.get_pos()

    # ф-ция закрашивания стен
    if (game_win == False) and (game_lose == False):
        Draw_red_walls()

    for event in pygame.event.get():

        # работа спрайтов notif_1/2
        if event.type == pygame.MOUSEBUTTONDOWN and notif_watch:
            notif_watch = False
            notif_go_back = True

        if event.type == pygame.MOUSEBUTTONDOWN and notif_watch_2:
            notif_watch_2 = False
            notif_go_back_2 = True

        # работа с полем
        for circle_in_list in circle_list:
            if cat_to_pos == circle_list.index(circle_in_list) and circle_in_list.collidepoint(
                    pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print("car there")
                notif_watch_2 = True
                notif_go_back_2 = False
            else:

                if circle_in_list.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:

                    # если закрашено
                    if walls_array[circle_list.index(circle_in_list)] == (True, circle_in_list[0], circle_in_list[1]):
                        notif_watch = True
                        notif_go_back = False

                    # если не зкарашено
                    if walls_array[circle_list.index(circle_in_list)] == (False, circle_in_list[0], circle_in_list[1]):
                        walls_array[circle_list.index(circle_in_list)] = (True, circle_in_list[0], circle_in_list[1])

                        # подтираем говно за котом
                        blit_grenn_after_cars_move(circle_list[cat_to_pos])

                        # ф-ция кота
                        cat_mind_mass = []
                        mass_cat_out = []
                        for i in range(len(walls_array)):
                            cat_mind_mass.append(walls_array[i][0])

                        try:

                            mass_cat_out = cats_mind(cat_mind_mass, cat_to_pos)

                            if len(mass_cat_out) > 1:
                                rand_pos_cat = random.randint(0, len(mass_cat_out) - 1)

                            elif len(mass_cat_out) == 1:
                                rand_pos_cat = 0

                            if mass_cat_out == []:
                                print("you win")
                                game_win = True
                                screen.blit(notif_you_win, (500, 500))
                                break

                            cat_to_pos = mass_cat_out[rand_pos_cat]
                            print(mass_cat_out[rand_pos_cat])

                            # перемещение спрата кота
                            screen.blit(cat_sprite_2, (
                                circle_list[mass_cat_out[rand_pos_cat]][0] - 2,
                                circle_list[mass_cat_out[rand_pos_cat]][1] - 3))
                        except IndexError:
                            print("you lose")
                            screen.blit(notif_you_lose, (500, 500))
                            game_lose = True
                            break
        # выход
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if button_out_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

        if button_restart_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            print("123")

    # для спрайтов
    pygame.display.update()
    notif_bg_up()
    screen.blit(notif_1.image, notif_1.rect)
    screen.blit(notif_2.image, notif_2.rect)

    # спрайт notif_1
    if notif_watch:
        notif_1.go_left(1)
    if notif_go_back:
        notif_1.go_right(1)

    if notif_watch_2:
        notif_2.go_left(1)
    if notif_go_back_2:
        notif_2.go_right(1)
