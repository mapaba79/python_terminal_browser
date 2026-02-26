import pytest
from browser import LinkManager, resolve_url

def test_link_manager_indexing():
    manager = LinkManager()
    manager.add_link("Test", "https://example.com")
    assert manager.get_url(1) == "https://example.com"
    assert manager.get_url(99) is None


def test_resolve_relative_urls():
    base = "https://example.com/blog/"
    relative = "post-1"
    # Expected: https://example.com/blog/post-1
    assert resolve_url(base, relative) == "https://example.com/blog/post-1"


def test_resolve_absolute_urls():
    base = "https://example.com"
    absolute = "https://google.com"
    assert resolve_url(base, absolute) == "https://google.com"
