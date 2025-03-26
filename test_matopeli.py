# test_wormgame.py
# Unit tests for the main collision checks in the worm game
import pytest
# Checks if the worm hits the edge of the screen (wall)
def tormaako_seinaan(x, y, leveys, korkeus):
    return x < 0 or x >= leveys or y < 0 or y >= korkeus

# Checks if the worm collides with itself
def tormaako_itseensa(mato_lista):
    pää = mato_lista[-1] # coordinates of the head
    return pää in mato_lista[:-1] # Is the head part of the rest of the worm

# Tests wall collision:
def test_tormaako_seinaan():
    # Should collide: out from the left, out from the right, out from the top, out from the bottom
    assert tormaako_seinaan(-10, 50, 600, 400)
    assert tormaako_seinaan(600, 100, 600, 400)
    assert not tormaako_seinaan(100, 100, 600, 400)

# Tests self-collision:
def test_tormaako_itseensa():
    mato = [[100, 100], [110, 100], [120, 100], [130, 100], [120, 100]]
    # Should collide: the worm has collided with itself
    mato2 = [[100, 100], [110, 100], [120, 100], [130, 100], [140, 100]]
    #
    assert tormaako_itseensa(mato)
    assert not tormaako_itseensa(mato2)
