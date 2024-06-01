import pytest
from pathlib import Path

from src.parsing import parse_html


@pytest.fixture
def real_response():
    return Path("tests/resources/5-31-24-response.txt").read_text()


def test_parsing(real_response):
    nerdfonts = parse_html(real_response)
    assert len(nerdfonts) == 67

    assert "0xProto" in nerdfonts
    assert "JetBrainsMono" in nerdfonts
    assert "ZedMono" in nerdfonts
