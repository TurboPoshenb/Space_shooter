from pygame import*
init()
from random import*
window = display.set_mode((900, 900))
clock = time.Clock()
background = image.load('59ae9a056d4ce15e5209a548.png')
game = True

def draw_background():
    window.blit(background, (0,0))

class GameSprite(sprite. Sprite):
    # init - функція конструктор (вона створює екземпляри класу)
    def __init__(self, filename, x, y, width=50, height=80, speed=0):
        super().__init__()
        # завантажити текстуру картинки і змінити її розмір
        self.image = transform.scale(
            image.load(filename), (width, height)
        )
        self.rect = self.image.get_rect()  # get_rect - створює хітбокс розміру картинки
        # задаю кординати хітбоксу
        self.rect.x, self.rect.y = x, y  # одночасне присвоювання
        # self.rect.x = x
        # self.rect.y = y те ж саме, але одним рядком
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ufo(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > window. get_height():
            self.kill()

class Bullet(GameSprite):

    def update(self):
        self.rect.y -= self.speed

game_score = 0
lifes = 3
def label(text, size, label_font, color, x, y):
    new_font = font.SysFont(label_font, size)
    text = new_font.render(text, True, color)
    window.blit(text, (x, y))

class Player(GameSprite):
    def update(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_a]:
            self.rect.x -= self.speed
        if pressed_keys[K_d]:
            self.rect.x += self.speed
rocket = Player('rocket.png', 50, 800, speed=5)
ufos = sprite.Group()
bullets = sprite.Group()
run = True
lifes = 3
while game:
    if run == True:
        if lifes < 1:
            run = False
        while len(ufos) < 7:
            new_Ufo = Ufo("620768.png", randint(0,window.get_width() - 100), -100, 60, 50, 2)
            ufos.add(new_Ufo)
        pressed_keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    bullets.add(
                        Bullet('bullets_PNG35594.png', rocket.rect.x, rocket.rect.y, 10, 30, 5)
                    )

        rocket.update()
        interaction = sprite.groupcollide(bullets, ufos, True, True)
        for bullet in interaction:
            game_score += len(interaction[bullet])
        interaction2 = sprite.spritecollide(rocket, ufos, True)
        if len(interaction2) >0:
            lifes -=1
        bullets.update()
        ufos.update()
        window.blit(background, (0, 0))
        ufos.draw(window)
        rocket.draw()
        bullets.draw(window)
        label ("Рахунок:" + str(game_score), 40, "Montserrat", (255,255, 255), 620, 50)
        label("Життя:" + str(lifes), 40, "Montserrat", (255, 255, 255), 100, 50)
    else:
        for e in event.get():
            if e.type == QUIT:
                game = False
        label('You lose', 60, 'Alergian',(255,215,0), 375, 375)
    display.update()
    clock.tick(60)
