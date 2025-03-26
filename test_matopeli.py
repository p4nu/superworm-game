import pytest
import pygame
from matopeli import gameLoop, message

def test_message_rendering():
    pygame.init()
    width, height = 640, 480
    window = pygame.display.set_mode((width, height))
    font_style = pygame.font.SysFont(None, 50)
    try:
        message("Test Message", (255, 0, 0))
        assert True  # If no errors occur, the test passes
    except Exception as e:
        pytest.fail(f"Message rendering failed: {e}")

def test_game_initialization():
    pygame.init()
    try:
        gameLoop()  # Ensure the game loop initializes without crashing
        assert True
    except Exception as e:
        pytest.fail(f"Game initialization failed: {e}")
