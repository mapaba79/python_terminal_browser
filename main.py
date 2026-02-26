from rich.console import Console
from rich.prompt import Prompt
from browser import fetch_content, parse_and_format, LinkManager

def main():
    console = Console()
    link_manager = LinkManager()

    console.print("[bold yellow]Minimalist Terminal Browser[/bold yellow]")
    current_url = Prompt.ask("Enter URL", default="http://example.com")

    while True:
        with console.status(f"[bold green]Loading {current_url}..."):
            html = fetch_content(current_url)

        # Render page
        content = parse_and_format(html, current_url, link_manager)
        console.clear()
        console.print(f"[dim]Source: {current_url}[/dim]\n")
        console.print(content)
        console.print("\n[bold cyan]" + "="*30 + "[/bold cyan]")

        # Interaction
        user_input = Prompt.ask(
            "\n[Link #], [URL], or [bold red]'q'[/bold red] to quit"
        ).strip()

        if user_input.lower() == 'q':
            break

        if user_input.isdigit():
            next_url = link_manager.get_url(int(user_input))
            if next_url:
                current_url = next_url
            else:
                console.print("[bold red]Invalid link number![/bold red]")
        else:
            current_url = user_input

if __name__ == "__main__":
    main()
