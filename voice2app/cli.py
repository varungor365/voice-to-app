import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown

from voice2app.generator import generate_app_structure, transcribe_audio

console = Console()


def main() -> None:
    parser = argparse.ArgumentParser(description="Voice-to-App Generator")
    parser.add_argument("audio_file", help="Path to the audio file (mp3, wav, m4a)")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM to use for generation")
    parser.add_argument("--outdir", default=".", help="Directory to save the generated app")
    args = parser.parse_args()

    audio_file = Path(args.audio_file).expanduser()
    if not audio_file.is_file():
        console.print(f"[bold red]Error:[/bold red] Audio file not found: {audio_file}")
        sys.exit(1)

    output_dir = Path(args.outdir).expanduser().resolve()

    try:
        console.print("[cyan]Transcribing audio with Whisper...[/cyan]")
        transcript = transcribe_audio(str(audio_file))
        console.print("[bold green]Transcript:[/bold green]")
        console.print(f"> {transcript}\n")

        console.print(f"[cyan]Generating app structure with {args.model}...[/cyan]")
        description, files = generate_app_structure(transcript, model=args.model)

        console.print("\n[bold magenta]=== Generator Notes ===[/bold magenta]")
        console.print(Markdown(description))
        console.print("[bold magenta]=======================[/bold magenta]\n")

        output_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            relative_path = Path(filename)
            if relative_path.is_absolute() or relative_path.name != filename:
                raise ValueError(
                    f"Refusing unsafe generated filename {filename!r}; only a single file name is allowed."
                )
            destination = output_dir / relative_path
            destination.write_text(content, encoding="utf-8")
            console.print(f"[bold green]Saved code to: {destination}[/bold green]")

    except Exception as exc:  # noqa: BLE001
        console.print(f"[bold red]Error:[/bold red] {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
