import pygame
import sys
import random
from hand_tracker import HandTracker

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Hand Controlled")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Load assets
bg_img = pygame.image.load("assets/bg.png").convert()
bg_img = pygame.transform.smoothscale(bg_img, (WIDTH, HEIGHT))

bird_img = pygame.image.load("assets/bird.png").convert_alpha()
bird_img = pygame.transform.smoothscale(bird_img, (50, 50))

pipe_img = pygame.image.load("assets/pipe.png").convert_alpha()
pipe_img = pygame.transform.smoothscale(pipe_img, (70, 500))

# Hand Tracker (moved up to avoid IDE warnings)
tracker = HandTracker()

def draw_text(text, size, color, x, y):
    font_obj = pygame.font.SysFont(None, size)
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    win.blit(text_surface, text_rect)

def main_game(tracker): # noqa: shadowed-name
    bird_x = 100
    bird_y = HEIGHT // 2
    bird_radius = 25
    bird_velocity = 0
    gravity = 0.5
    jump_strength = -10
    score = 0
    pipes = []

    def create_pipe():
        y = random.randint(200, HEIGHT - 200)
        return {"x": WIDTH, "top": y - 150, "bottom": y + 150}

    prev_y = 0.5
    running = True
    while running:
        clock.tick(30)
        win.blit(bg_img, (0, 0))

        # Hand input
        hand_y = tracker.get_hand_y()
        if prev_y - hand_y > 0.05:
            bird_velocity = jump_strength
        prev_y = hand_y

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Create pipes
        if len(pipes) == 0 or pipes[-1]["x"] < WIDTH - 250:
            pipes.append(create_pipe())

        # Move and draw pipes
        for pipe in pipes:
            pipe["x"] -= 5

            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            top_rect = flipped_pipe.get_rect(topleft=(pipe["x"], pipe["top"] - 500))
            win.blit(flipped_pipe, top_rect)

            bottom_rect = pipe_img.get_rect(topleft=(pipe["x"], pipe["bottom"]))
            win.blit(pipe_img, bottom_rect)

        # Remove passed pipes and update score
        if pipes and pipes[0]["x"] < -70:
            pipes.pop(0)
            score += 1

        # Collision detection
        for pipe in pipes:
            if bird_x + bird_radius > pipe["x"] and bird_x - bird_radius < pipe["x"] + 70:
                if bird_y - bird_radius < pipe["top"] or bird_y + bird_radius > pipe["bottom"]:
                    return score

        # Off-screen (top or bottom)
        if bird_y + bird_radius > HEIGHT or bird_y - bird_radius < 0:
            return score

        # Draw bird
        win.blit(bird_img, (bird_x - bird_radius, int(bird_y) - bird_radius))

        # Draw score
        draw_text(f"Score: {score}", 40, (0, 0, 0), 80, 40)

        # Draw copyright
        draw_text("© 2025 Yash Yadav", 20, (50, 50, 50), 120, 70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tracker.release()
                pygame.quit()
                sys.exit()

        pygame.display.update()

def game_over_screen(score_to_show, tracker): # noqa: shadowed-name
    while True:
        win.fill((0, 0, 0))
        draw_text("GAME OVER", 70, (255, 0, 0), WIDTH // 2, HEIGHT // 3)
        draw_text(f"Your Score: {score_to_show}", 50, (255, 255, 255), WIDTH // 2, HEIGHT // 2)
        draw_text("Press SPACE to Play Again", 30, (200, 200, 200), WIDTH // 2, HEIGHT * 2 // 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tracker.release()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return

        pygame.display.update()
        clock.tick(30)

# Game loop
while True:
    final_score = main_game(tracker)
    game_over_screen(final_score, tracker)
