import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from rich.console import Console
from rich.panel import Panel


class LinkManager:
    def __init__(self):
        self.links = []

    def add_link(self, text, url):
        self.links.append({"text": text, "url": url})

    def get_url(self, index):
        try:
            return self.links[index - 1]["url"]
        except (IndexError, TypeError):
            return None

    def clear(self):
        self.links = []


def resolve_url(base, url):
    return urljoin(base, url)


def fetch_content(url):
    try:
        headers = {"User-Agent": "MinimalistTerminalBrowser/1.0"}
        with httpx.Client(follow_redirects=True) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.text
    except Exception as e:
        return f"[bold red]Error:[/bold red] {str(e)}"

def parse_and_format(html, current_url, link_manager):
    soup = BeautifulSoup(html, 'html.parser')
    link_manager.clear()
    formatted_output = []

    # Filter main content tags
    for tag in soup.find_all(['h1', 'h2', 'p', 'a']):
        text = tag.get_text().strip()
        if not text: continue

        if tag.name in ['h1', 'h2']:
            formatted_output.append(f"[bold magenta]## {text.upper()} ##[/bold magenta]")

        elif tag.name == 'a' and tag.get('href'):
            full_url = resolve_url(current_url, tag['href'])
            link_manager.add_link(text, full_url)
            idx = len(link_manager.links)
            formatted_output.append(f"[bold blue][{idx}] {text}[/bold blue]")

        else:
            formatted_output.append(text)

    return "\n\n".join(formatted_output)

