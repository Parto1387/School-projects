import tkinter
import PIL.ImageOps
import pygame
import sys
import random
import time
from tkinter import *
from PIL import Image, ImageTk
from pygame import display
from PIL import Image

#TAB1
tab1 = Tk()
tab1.minsize(height=750, width=1350)
def opening():
    tab1.destroy()

button1= Button(tab1, text="NEXT", font=("Mefista.ttf", 30), command=opening, activebackground="lightgreen")
button1.pack(side=RIGHT)

# IMAGE1
tab1.title("Playful Cuby---کوبی بازیگوش")
image1 = Image.open('image/tab1.png')
image1 = image1.resize((1200, 680))
image1.save('image/tab1.png')
image1 = ImageTk.PhotoImage(image1)
image_label = tkinter.Label(tab1, image=image1)
image_label.pack()

tab1.mainloop()

#TAB2
tab2 = Tk()
tab2.minsize(height=750, width=1350)
def test():
    tab2.destroy()

button2= Button(tab2, text="Start the quiz", font=("Mefista", 20), command=test, activebackground="tomato")
button2.pack(side=LEFT)

# IMAGE3
tab2.title("Playful Cuby---کوبی بازیگوش")
image = Image.open('image/tab2.png')
new_image = image.resize((1100, 680))
new_image.save('image/tab2.png')
image = ImageTk.PhotoImage(image)
image_label2 = tkinter.Label(tab2, image=image)
image_label2.pack()
tab2.mainloop()

# QUIZ
questions = ("How many elements are in periodic table?",
             "What is the most abundant gas in Earth's atmosphere?",
             "Which planet in solar system is the hottest?")
options = (("A. 116", "B. 120", "C. 118"),
           ("A. Nitrogen", "B. Oxygen", "C. Hydrogen"),
           ("A. Mercury", "B. Mars", "C. Venus"))
answers = ("C", "A", "C")
guesses = []
score_q = 0
question_num = 0

for question in questions:
    print("_________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score_q += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("_________________")
print("    RESULTS      ")
print("_________________")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_q = score_q / len(questions) * 100
print(f"Your score is: {score_q}%")

# TAB3
tab3 = Tk()
tab3.minsize(height=750, width=1350)

def play():
    if score_q >= 100:
        tab3.destroy()
    else:
        print("****************************************")
        print("Your score is less that 100😨")
        print("You failed!😢")
        print("Try again later😇")
        quit()
button3= Button(tab3, text="PLAY", font=("Mefista", 60), command=play, activebackground="blueviolet")
button3.pack(side=RIGHT)

# IMAGE3
tab3.title("Playful Cuby---کوبی بازیگوش")
image = Image.open('image/bird.png')
new_image = image.resize((1000, 800))
new_image.save('image/bird.png')
image = ImageTk.PhotoImage(image)
image_label3 = tkinter.Label(tab3, image=image)
image_label3.pack()

tab3.mainloop()

# START PYGAME MODULES
pygame.init()

# GAME DISPLAY
display.width = 580
display.height = 720
main_screen = pygame.display.set_mode((display.width, display.height))

# ALL VARIABLE
floor_x = 0
gravity = 0.20
cuby_movement = 0
create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_flap, 100)
pygame.time.set_timer(create_pipe, 1300)
pipe_list = []
game_status = True
cuby_list_index = 0
game_font = pygame.font.Font('font/Minecraft Evenings.otf', 50)
score = 0
high_score = 0
active_score = True

# IMAGES *
cuby1_image = pygame.transform.scale(pygame.image.load("image/c1.png"), size=[60, 60])
cuby2_image = pygame.transform.scale(pygame.image.load("image/c2.png"), size=[60, 60])
cuby3_image = pygame.transform.scale(pygame.image.load("image/c3.png"), size=[60, 60])
cuby_list = [cuby1_image, cuby2_image, cuby3_image]
cuby_image = cuby_list[cuby_list_index]
sky_image = pygame.transform.scale(pygame.image.load("image/cbn.png"), size=[580, 800])
floor_image = pygame.transform.scale(pygame.image.load("image/FLOOR.png"), size=[580, 150])
pipe_image = pygame.transform.scale(pygame.image.load("image/pipe.png"), size=[80, 700])
over_image = pygame.transform.scale(pygame.image.load("image/game_over_PNG42.png"), size=[400, 500])
win_image = pygame.transform.scale(pygame.image.load("image/win2.png"), size=[400, 500])

# FRAME
cuby_image_rect = cuby_image.get_rect(center=(100, 300))
over_image_rect = over_image.get_rect(center=(300, 400))
win_image_rect = over_image.get_rect(center=(300, 400))

# SOUND
win_sound = pygame.mixer.Sound('sound/win.mp3')
over_sound = pygame.mixer.Sound('sound/game_over.mp3')
flap_sound = pygame.mixer.Sound('sound/flap.mp3')

# DISPLAY DEF
def generate_pipe_rect():
    random_pipes = random.randrange(250, 550)
    pipe_rect_top = pipe_image.get_rect(midbottom=(600, random_pipes - 170))
    pipe_rect_bottom = pipe_image.get_rect(midtop=(600, random_pipes))
    return pipe_rect_top, pipe_rect_bottom


def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipes


def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 720:
            main_screen.blit(pipe_image, pipe)
        else:
            reversed_pipes = pygame.transform.flip(pipe_image, False, True)
            main_screen.blit(reversed_pipes, pipe)


def check_collision(pipes):
    global active_score
    for pipe in pipes:
        if cuby_image_rect.colliderect(pipe):
            over_sound.play()
            time.sleep(3)
            active_score = True
            return False
        if cuby_image_rect.top <= -50 or cuby_image_rect.bottom >= 600:
            over_sound.play()
            time.sleep(3)
            return False
        if score >= 20:
            win_sound.play()
            time.sleep(3)
            return False
        active_score = True
    return True


def cuby_animation():
    new_cuby = cuby_list[cuby_list_index]
    new_cuby_rect = new_cuby.get_rect(center=(100, cuby_image_rect.centery))
    return new_cuby, new_cuby_rect


def display_score(status):
    if status == 'active':
        text1 = game_font.render(str(score), False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(280, 100))
        main_screen.blit(text1, text1_rect)
    if status == 'game_over':
        # SCORE
        text1 = game_font.render(f'Score : {score}', False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(300, 100))
        main_screen.blit(text1, text1_rect)
        # HIGH_SCORE
        text2 = game_font.render(f'HighScore : {high_score}', False, (255, 255, 255))
        text2_rect = text2.get_rect(center=(300, 150))
        main_screen.blit(text2, text2_rect)
    if status == 'win':
        # SCORE
        text1 = game_font.render(f'Score : {score}', False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(300, 100))
        main_screen.blit(text1, text1_rect)
        # HIGH_SCORE
        text2 = game_font.render(f'HighScore : {high_score}', False, (255, 255, 255))
        text2_rect = text2.get_rect(center=(300, 150))
        main_screen.blit(text2, text2_rect)


def update_score():
    global score, high_score, active_score
    if pipe_list:
        for pipe in pipe_list:
            if 40 < pipe.centerx < 50 and active_score:
                flap_sound.play()
                score += 1
                active_score = False
            if pipe.centerx < 0:
                active_score = True
    if score > high_score:
        high_score = score

    return high_score



# GAME TIMER
clock = pygame.time.Clock()

# GAME LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            # TERMINATE PROGRAM
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cuby_movement = 0
                cuby_movement -= 5.5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_status == False:
                game_status = True
                pipe_list.clear()
                cuby_image_rect.center = (100, 300)
                cuby_movement = 0
                score = 0
        if event.type == create_pipe:
            pipe_list.extend(generate_pipe_rect())
        if event.type == create_flap:
            if cuby_list_index < 2:
                cuby_list_index += 1
            else:
                cuby_list_index = 0

            cuby_image, cuby_image_rect = cuby_animation()

    # DISPLAY SKY
    main_screen.blit(sky_image, (0, 0))

    if game_status:
        # CHECK COLLISION
        check_collision(pipe_list)
        # DISPLAY FLOOR
        floor_x -= 1
        main_screen.blit(floor_image, (floor_x, 580))
        main_screen.blit(floor_image, (floor_x + 578, 580))
        if floor_x <= -578:
            floor_x = 0
        # DISPLAY cuby
        main_screen.blit(cuby_image, (cuby_image_rect))
        # MOVE PIPES
        pipe_list = move_pipe_rect(pipe_list)
        display_pipes(pipe_list)
        # GRAVITY AND MOVEMENT
        cuby_movement += gravity
        cuby_image_rect.centery += cuby_movement
        # CHECK FOR COLLISION
        game_status = check_collision(pipe_list)
        # SHOW SCORE
        update_score()
        display_score('active')
    else:
        if score >= 20:
            main_screen.blit(win_image, win_image_rect)
            display_score('win')
        else:
            main_screen.blit(over_image, over_image_rect)
            display_score('game_over')

    #_________#
    pygame.display.update()

    # SET GAME SPEED
    clock.tick(90)
