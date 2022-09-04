import random
import sys
from set import *

                            # функции говнокота и минного поля
# bg
def bg():
    screen.blit(bg_img, image_One_rect)


# поле уведолений
def notif_bg_up():
    screen.blit(notif_backgroung, (screen_coord[0] - 116, 0))


# ф-ция подтирание говна за котом
def blit_grenn_after_cars_move(but_coords):
    screen.blit(Green_Button, (but_coords[0] - 2, but_coords[1] - 10))


# поле
def generation_field(point_2):
    for i in range(field):
        point_1 = 45
        if i == 0:
            for j in range(field):
                # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
                circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
                circle_list.append(circle)

                screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))
                point_1 += 60

        elif i % 2 != 0:
            point_1 = 75

            for j in range(field):
                # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
                circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
                circle_list.append(circle)

                screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))

                point_1 += 60
        else:
            point_1 = 45
            for j in range(field):
                # рисование кругов для отслеживания нажатий(коллайдер работает точнее)
                circle = pygame.draw.circle(screen, RED, (point_1, point_2), 25, width=10)
                circle_list.append(circle)

                screen.blit(Green_Button, (-27 + point_1, -34 + point_2,))

                point_1 += 60

        point_2 += 50


def generation_mass_for_walls():

    for i in range(len(walls_array)):
        x = circle_list[i].x
        y = circle_list[i].y
        walls_array[i] = (False, x, y)


# генерация рандонмых красных стен
def generation_red_wall():
    for j in range(ready_walls_const_count):
        random_wall_pos = random.randint(0, len(circle_list) - 1)
        if random_wall_pos not in not_build_here:
            walls_array[random_wall_pos] = (True, circle_list[random_wall_pos].x, circle_list[random_wall_pos].y)
        else:
            j -= 1

# рисование стен
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

# '''sprites'''


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


def draw_pos_cat(pos):
    screen.blit(cat_sprite_2, (circle_list[pos][0] - 2, circle_list[pos][1] - 3))


# запуск ф-ций поля
bg()
generation_field(point_2)
walls_array = [0] * len(circle_list)
generation_mass_for_walls()
generation_red_wall()


# для результатов игры
game_win = False
game_lose = False

# создание спрайтов уведомлений
notif_1 = Sprites_notif(notification_1, x=1480 + 200)
notif_2 = Sprites_notif(notification_2, x=1480 + 200)

# режимы уведомлений
    #notif_1
notif_watch = False
notif_go_back = False
    #notif_2
notif_watch_2 = False
notif_go_back_2 = False

# рисование начальной позиции кота
draw_pos_cat(defolt_cat_to_pos)
cat_to_pos = defolt_cat_to_pos

              # '''main cycle'''
while True:
    # количество обновлений экрана в сек
    fpsClock.tick(FPS)
    # позиция курсора
    pos = pygame.mouse.get_pos()

    # ф-ция закрашивания стен
    if (game_win == False) and (game_lose == False):
        Draw_red_walls()

    # отслеживание событий
    for event in pygame.event.get():

        # работа спрайтов notif_1
        if event.type == pygame.MOUSEBUTTONDOWN and notif_watch:
            notif_watch = False
            notif_go_back = True

        # работа спрайтов notif_2
        if event.type == pygame.MOUSEBUTTONDOWN and notif_watch_2:
            notif_watch_2 = False
            notif_go_back_2 = True

        # работа с полем
        for circle_in_list in circle_list:

            # отслеживание нажатий на клетку с котом
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

                        # массивы для вывода данных ф-ции кота
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
                                screen.blit(notif_you_win, (250, 250))
                                break

                            cat_to_pos = mass_cat_out[rand_pos_cat]

                            # перемещение спрата кота
                            draw_pos_cat(cat_to_pos)

                        except IndexError:
                            print("you lose")
                            screen.blit(notif_you_lose, (250, 250))
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
            circle_list.clear()
            walls_array.clear()
            bg()
            game_win = False
            game_lose = False
            generation_field(point_2)
            walls_array = [0] * len(circle_list)
            generation_mass_for_walls()
            generation_red_wall()
            draw_pos_cat(defolt_cat_to_pos)
            cat_to_pos = defolt_cat_to_pos


    # обновление поля уведомлений и спратов
    pygame.display.update()
    notif_bg_up()
    screen.blit(notif_1.image, notif_1.rect)
    screen.blit(notif_2.image, notif_2.rect)

    # спрайт notif_1
    if notif_watch:
        notif_1.go_left(1)
    if notif_go_back:
        notif_1.go_right(1)

    # спрайт notif_2
    if notif_watch_2:
        notif_2.go_left(1)
    if notif_go_back_2:
        notif_2.go_right(1)
