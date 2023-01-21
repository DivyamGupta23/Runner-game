import pygame
from sys import exit
from random import randint

pygame.mixer.init()


def obstacle_movement(obstacle_list):
    if obstacle_list:
        #     sky_rect.right -= 2
        #     if sky_rect.left <= 800:
        #         sky_rect.right = 900
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= snail_speed
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        # for obstacle_rect in obstacle_list:
        #     if obstacle_rect.right < 0:
        #         snail_speed += 0.2

        return obstacle_list
    else:
        return []


def collision(player, obstacle):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player.player_rect.colliderect(obstacle_rect):
                return False

    return True


jump_sound = pygame.mixer.Sound('audio/jumping.mp3')
bg_sound = pygame.mixer.music.load('audio/theme2.mp3')
pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.set_volume((0.5))
pygame.init()
# player_speed = 6

width = 800
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
pygame.display.set_icon(pygame.image.load('graphics/Player/run1.png'))
ground_speed = 5
text_font = pygame.font.Font('font/Pixeltype.ttf', 40)
runner_font = pygame.font.Font('font/Pixeltype.ttf', 90)
quote_font = pygame.font.Font('font/Pixeltype.ttf', 24)

snail_img = pygame.transform.scale(pygame.image.load('graphics/enemy/turret1.png'), (50, 60)).convert_alpha()
snail_img2 = pygame.transform.scale(pygame.image.load('graphics/enemy/turret2.png'), (50, 60)).convert_alpha()
snail_frames = [snail_img, snail_img2]
snail_frames_index = 0
snail_surf = snail_frames[snail_frames_index]
fly_img = pygame.transform.scale(pygame.image.load('graphics/enemy/heli1.png'), (44, 44)).convert_alpha()
fly_img2 = pygame.transform.scale(pygame.image.load('graphics/enemy/heli2.png'), (44, 44)).convert_alpha()
fly_img3 = pygame.transform.scale(pygame.image.load('graphics/enemy/heli3.png'), (44, 44)).convert_alpha()
fly_img4 = pygame.transform.scale(pygame.image.load('graphics/enemy/heli4.png'), (44, 44)).convert_alpha()
sound_icon = []
speaker_img = pygame.transform.scale(pygame.image.load('graphics/speaker.png'), (25, 25)).convert_alpha()
mute_img = pygame.transform.scale(pygame.image.load('graphics/mute.png'), (25, 25)).convert_alpha()
sound_icon.append(speaker_img)
sound_icon.append(mute_img)
sound_index = 0
sound_surf = sound_icon[sound_index]
sound_rect = sound_surf.get_rect(center=(750, 35))

player_size = (34, 65)

fly_frames = [fly_img2, fly_img3, fly_img4]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]
snail_speed = 6
playr1_img = pygame.transform.scale(pygame.image.load('graphics//Player/run1.png'),
                                    player_size).convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.player_walk = []
        self.player_jump = []
        self.player1_img = pygame.transform.scale(pygame.image.load('graphics//Player/run1.png'),
                                                  player_size).convert_alpha()
        self.player2_img = pygame.transform.scale(pygame.image.load('graphics//Player/run2.png'),
                                                  player_size).convert_alpha()
        self.player3_img = pygame.transform.scale(pygame.image.load('graphics//Player/run3.png'),
                                                  player_size).convert_alpha()
        self.player4_img = pygame.transform.scale(pygame.image.load('graphics//Player/run4.png'),
                                                  player_size).convert_alpha()
        self.player5_img = pygame.transform.scale(pygame.image.load('graphics//Player/run5.png'),
                                                  player_size).convert_alpha()
        self.player6_img = pygame.transform.scale(pygame.image.load('graphics//Player/run6.png'),
                                                  player_size).convert_alpha()
        self.player_walk.append(self.player1_img)
        self.player_walk.append(self.player2_img)
        self.player_walk.append(self.player3_img)
        # self.player_walk.append(self.player4_img)
        self.player_walk.append(self.player5_img)
        self.player_walk.append(self.player6_img)

        self.current_player_sprite = 0

        self.player_j1 = pygame.transform.scale(pygame.image.load('graphics/Player/Jump/jump1.png'),
                                                player_size).convert_alpha()
        self.player_j2 = pygame.transform.scale(pygame.image.load('graphics/Player/Jump/jump2.png'),
                                                player_size).convert_alpha()
        self.player_j3 = pygame.transform.scale(pygame.image.load('graphics/Player/Jump/jump3.png'),
                                                player_size).convert_alpha()
        self.player_j4 = pygame.transform.scale(pygame.image.load('graphics/Player/Jump/jump4.png'),
                                                player_size).convert_alpha()
        self.player_jump.append(self.player2_img)
        self.player_jump.append(self.player3_img)
        # self.player_jump.append(self.player_j3)
        # self.player_jump.append(self.player_j4)

        self.player_surf = self.player_walk[self.current_player_sprite]
        self.player_rect = self.player1_img.get_rect(center=(xpos, ypos))

    def update(self):
        if self.player_rect.bottom < 300:
            self.current_player_sprite += 0.1
            if self.current_player_sprite >= len(self.player_jump):
                self.current_player_sprite = 0
            self.player_surf = self.player_jump[int(self.current_player_sprite)]
        else:
            self.current_player_sprite += 0.14
            if self.current_player_sprite >= len(self.player_walk):
                self.current_player_sprite = 0
            self.player_surf = self.player_walk[int(self.current_player_sprite)]


class Player_idle(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.player_idle = []

        self.idle1 = pygame.transform.scale(pygame.image.load('graphics//idle/idle1.png'),
                                            player_size).convert_alpha()
        self.idle2 = pygame.transform.scale(pygame.image.load('graphics//idle/idle2.png'),
                                            player_size).convert_alpha()
        self.idle3 = pygame.transform.scale(pygame.image.load('graphics//idle/idle3.png'),
                                            player_size).convert_alpha()
        self.idle4 = pygame.transform.scale(pygame.image.load('graphics//idle/idle4.png'),
                                            player_size).convert_alpha()

        self.player_idle.append(self.idle1)
        self.player_idle.append(self.idle2)
        self.player_idle.append(self.idle3)
        self.player_idle.append(self.idle4)

        self.current_idle_sprite = 0

        self.idle_surf = self.player_idle[int(self.current_idle_sprite)]
        self.idle_rect = self.idle1.get_rect(center=(xpos, ypos))

    def update(self):
        if self.idle_rect.bottom <= 300:
            self.current_idle_sprite += 0.08
            if self.current_idle_sprite >= len(self.player_idle):
                self.current_idle_sprite = 0
            self.idle_surf = self.player_idle[int(self.current_idle_sprite)]


player_gravity = 0
obstacle_list = []

game_active = False

your_score = 0


def get_score():
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render('SCORE:  ' + str(current_score), False, 'black')
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_score


sky_img = pygame.image.load('graphics/trees.png').convert_alpha()
sky_rect = sky_img.get_rect(center=(400, 150))
ground_img = pygame.image.load('graphics/newground.png').convert_alpha()
text_surface = text_font.render("score :  ", False, (136, 208, 192))
text_rect = text_surface.get_rect(center=(400, 30))
game_over_txt = text_font.render('game over', False, (136, 208, 192))
start_time = 0
ground_rect = ground_img.get_rect(center=(0, 383))
# text_shadow = text_font.render('Score - ', False, (255, 255, 255))
player_start = pygame.transform.rotozoom(pygame.image.load('graphics/Player/player_stand.png'), 0, 2)
clock = pygame.time.Clock()
fps = 60

obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time, 1000)

snail_anim_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anim_timer, 300)

fly_anim_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_anim_timer, 200)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(86)
run = True
sprites1 = pygame.sprite.Group()
sprites2 = pygame.sprite.Group()
player = Player(80, 300 - playr1_img.get_height() + 10)
player_idle = Player_idle(80, 267)
sprites1.add(player)
sprites2.add(player_idle)
while run:  # MAIN LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            exit()
        # mouse_pos = pygame.mouse.get_pos()

        if game_active:

            # if event.type == pygame.MOUSEBUTTONDOWN and player.player_rect.bottom >= 300:
            #     player_gravity = -21
            #     jump_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_UP or event.key == pygame.K_w:
                    if player.player_rect.bottom >= 300:
                        player_gravity = -21
                        jump_sound.play()
            if event.type == obstacle_time:
                if randint(0, 2):
                    obstacle_list.append(snail_surf.get_rect(bottomright=(randint(810, 1100), 300)))
                else:
                    obstacle_list.append(fly_surf.get_rect(bottomright=(randint(810, 1100), 210)))
            if event.type == snail_anim_timer:
                if snail_frames_index == 0:
                    snail_frames_index = 1
                else:
                    snail_frames_index = 0
                snail_surf = snail_frames[snail_frames_index]
            if event.type == fly_anim_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    if sound_index == 1:
                        sound_index = 0
                        pygame.mixer.music.unpause()
                    else:
                        sound_index = 1
                        pygame.mixer.music.pause()
                    sound_surf = sound_icon[sound_index]


        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # for obstacle_rect in obstacle_list:
                #     obstacle_rect.right = -1
                player_gravity = -21
                jump_sound.play()
                game_active = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sound_rect.collidepoint(pygame.mouse.get_pos()):
                    if sound_index == 1:
                        sound_index = 0
                        pygame.mixer.music.unpause()
                    else:
                        sound_index = 1
                        pygame.mixer.music.pause()
                    sound_surf = sound_icon[sound_index]

            start_time = int(pygame.time.get_ticks() / 1000)
    if game_active:

        screen.blit(ground_img, ground_rect)
        screen.blit(sky_img, sky_rect)
        your_score = get_score()
        screen.blit(player.player_surf, player.player_rect)
        screen.blit(sound_surf, sound_rect)
        sprites1.update()
        player_gravity += 1
        player.player_rect.y += player_gravity

        ground_rect.left -= ground_speed
        if ground_rect.right <= 800:
            ground_rect.left = -1.33

        # ground_speed += 0.01

        if player.player_rect.bottom > 300:
            player.player_rect.bottom = 300
        # if player.player_rect.top < 0:fscore

        # player.player_rect.top = 0

        obstacle_list = obstacle_movement(obstacle_list)
        for obstacle_rect in obstacle_list:
            if obstacle_rect.right < 0:
                snail_speed += 0.1
            # speed -= 50
        # snail_rect.left -= snail_speed
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        #     snail_speed += 0.2

        # player.player_rect.left += player_speed

        if player.player_rect.left >= 800:
            player.player_rect.right = 0
            #

        # collision(player.player_rect, obstacle_list)
        for obstacle_rect in obstacle_list:
            if player.player_rect.colliderect(obstacle_rect):
                game_active = False


    else:

        screen.blit(ground_img, ground_rect)
        screen.blit(sky_img, sky_rect)
        screen.blit(sound_surf, sound_rect)
        obstacle_list.clear()
        player_gravity = 0
        snail_speed = 6
        # pygame.mixer.music.stop()
        # player.player_rect.midbottom = (80, 300)
        # screen.blit(pygame.transform.rotozoom(pygame.image.load('graphics/pattern.png'), 0, 3), (0, 0))
        # screen.blit(player1_img, player.player_rect)
        screen.blit(runner_font.render("Runner ", False, 'black'), (285, 20))
        screen.blit(text_font.render("Press  Space  To Jump ", False, 'black'), (260, 70))
        screen.blit(text_font.render("Your Score:  " + str(your_score) + " s", False, 'black'), (300, 170))
        screen.blit(player_idle.idle_surf, player_idle.idle_rect)
        sprites2.update()
        if your_score >= 20:
            screen.blit(text_font.render("Good Job ", False, 'black'), (340, 210))
        elif your_score < 20 and your_score != 0:
            screen.blit(text_font.render("You  Can  Do  Better ", False, 'black'), (290, 215))

    clock.tick(60)
    pygame.display.update()
