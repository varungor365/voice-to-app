import argparse
import sys
import os
from rich.console import Console
from rich.markdown import Markdown
from voice2app.generator import transcribe_audio, generate_app_structure

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🎙️ Voice-to-App Generator")
    parser.add_argument("audio_file", help="Path to the audio file (mp3, wav, m4a)")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM to use for generation")
    parser.add_argument("--outdir", default=".", help="Directory to save the generated app")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.audio_file):
        console.print(f"[bold red]Error:[/bold red] Audio file not found at {args.audio_file}")
        sys.exit(1)
        
    try:
        console.print("[cyan]🎙️ Transcribing audio with Whisper...[/cyan]")
        transcript = transcribe_audio(args.audio_file)
        console.print("[bold green]Transcript:[/bold green]")
        console.print(f"> {transcript}\n")
        
        console.print(f"[cyan]🧠 Generating app structure using {args.model}...[/cyan]")
        desc, files = generate_app_structure(transcript, model=args.model)
        
        console.print("\n[bold magenta]=== Generator Notes ===[/bold magenta]")
        console.print(Markdown(desc))
        console.print("[bold magenta]=======================[/bold magenta]\n")
        
        os.makedirs(args.outdir, exist_ok=True)
        
        for filename, content in files.items():
            filepath = os.path.join(args.outdir, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            console.print(f"[bold green]✅ Saved code to: {filepath}[/bold green]")
            
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
