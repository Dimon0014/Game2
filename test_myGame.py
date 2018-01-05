from unittest import TestCase


class TestMyGame(TestCase):
    def test_setup(self):
        from game import MyGame
        game = MyGame('Test', 100, 100)
        assert game.is_stopped is True
