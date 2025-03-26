import unittest
import pygame
from unittest.mock import patch, MagicMock
from matopeli import message, gameLoop

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.font_style = pygame.font.SysFont(None, 50)

    def tearDown(self):
        pygame.quit()

    def test_message_rendering(self):
        """Test if the message function renders text correctly."""
        with patch('pygame.font.Font.render') as mock_render:
            message("Test Message", (255, 0, 0))
            mock_render.assert_called_once_with("Test Message", True, (255, 0, 0))

    @patch('matopeli.random.randrange')
    def test_food_position(self, mock_randrange):
        """Test if the food is placed within the game boundaries."""
        mock_randrange.side_effect = [100, 200]
        foodx = round(mock_randrange(0, 640 - 10) / 10.0) * 10.0
        foody = round(mock_randrange(0, 480 - 10) / 10.0) * 10.0
        self.assertTrue(0 <= foodx <= 640 - 10)
        self.assertTrue(0 <= foody <= 480 - 10)

    @patch('pygame.event.get')
    def test_game_quit_event(self, mock_event_get):
        """Test if the game quits when QUIT event is triggered."""
        mock_event_get.return_value = [MagicMock(type=pygame.QUIT)]
        with self.assertRaises(SystemExit):
            gameLoop()

    @patch('pygame.event.get')
    def test_snake_movement(self, mock_event_get):
        """Test if the snake moves correctly based on key presses."""
        mock_event_get.side_effect = [
            [MagicMock(type=pygame.KEYDOWN, key=pygame.K_RIGHT)],
            [MagicMock(type=pygame.QUIT)]
        ]
        with patch('matopeli.clock.tick'), self.assertRaises(SystemExit):
            gameLoop()

    @patch('pygame.event.get')
    def test_snake_collision_with_wall(self, mock_event_get):
        """Test if the game ends when the snake collides with the wall."""
        mock_event_get.side_effect = [
            [MagicMock(type=pygame.KEYDOWN, key=pygame.K_UP)],
            [MagicMock(type=pygame.QUIT)]
        ]
        with patch('matopeli.clock.tick'), self.assertRaises(SystemExit):
            gameLoop()

if __name__ == '__main__':
    unittest.main()