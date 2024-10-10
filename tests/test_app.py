# tests/test_app.py
from calculator import App
import pytest
from unittest.mock import MagicMock, patch

def test_app_start_exit_command(capfd, monkeypatch):
    """Test app starts on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit
