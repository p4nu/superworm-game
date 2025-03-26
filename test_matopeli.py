import pytest
from matopeli import message

def test_message_rendering(monkeypatch):
    # Mock the font_style.render method
    def mock_render(msg, antialias, color):
        return f"Rendered: {msg} with color {color}"

    monkeypatch.setattr("matopeli.font_style.render", mock_render)

    # Mock the window.blit method
    def mock_blit(mesg, position):
        return f"Blitted: {mesg} at {position}"

    monkeypatch.setattr("matopeli.window.blit", mock_blit)

    result = message("Test Message", (255, 255, 255))
    assert result == "Blitted: Rendered: Test Message with color (255, 255, 255) at [106.66666666666667, 160.0]"
