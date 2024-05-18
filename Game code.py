
https://replit.com/@9730875/ROCK-PAPIER-sZOR

import pygame
import random

# Set the background color of the screen.
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))

font = pygame.font.SysFont("Times", 15)

text_surface = font.render("WELCOME TO ROCK PAPEER SCIZZORS!!!", True,
                           (200, 200, 200), (100, 100, 100))




def displayText(text, textcolor, x, y):
  text = font.render(text, True, textcolor)
  screen.blit(text, [x, y])


screen.blit(text_surface, [0, 0])

displayText("Press Any Key or Click to Start", (255, 255, 255),  0, 30)
pygame.display.update()


# Create a function to get the player's choice.
def get_player_choice():
  print('player choice:')
  # text_surface = font.render("How to play", True,
  #    (200, 200, 200))
  # screen.blit(text_surface, [0, ])
  displayText("How To Play:", (255, 255, 255), 0, 40)
  displayText("R: Choose Rock", (100, 100, 150), 0, 80)
  displayText("P: Choose Paper", (255, 255, 255), 0, 120)
  displayText("S: Choose Scissors", (255, 100, 100), 0, 160)
  pygame.display.update()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          return "rock"
        elif event.key == pygame.K_p:
          return "paper"
        elif event.key == pygame.K_s:
          return "scissors"


def get_player2_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)


def check_winner(player_choice, player2_choice):
  if player_choice == player2_choice:
    return "Tie"
  if (player_choice == "rock"
      and player2_choice == "scissors") or (player_choice == "paper"
                                             and player2_choice == "rock"):
    return "Player wins"
  return "Gertrude wins"


def play_game():
  startscreen = True
  while startscreen:
    #Show start screen
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        screen.fill((0, 0, 0))
        startscreen = False
    
  while True:

    player_choice = get_player_choice()

    player2_choice = get_player2_choice()

    winner = check_winner(player_choice, player2_choice)

    # Display the winner.
    text_surface = font.render(
        f"You chose {player_choice},  Gertrude chose {player2_choice}, {winner}!",
        True, (255, 255, 255))
  
    screen.fill((0,0,0))
    screen.blit(text_surface, [0,0])
    
    pygame.display.update()

    # Check if the player wants to quit.
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          pygame.quit()
          sys.exit()


# Play the game.
play_game()
