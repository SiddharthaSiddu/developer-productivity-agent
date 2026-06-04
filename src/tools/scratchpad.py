import os

class Scratchpad:
    def __init__(self, filename="scratchpad.txt"):
        self.filename = filename

    def append_finding(self, note: str) -> str:
        """Saves a discovery so it doesn't get lost when context overflows."""
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"- {note}\n")
        return "✨ Insight saved to scratchpad."

    def read_all(self) -> str:
        """Recovers all notes for the agent's current session."""
        if not os.path.exists(self.filename): 
            return "Scratchpad is empty."
        with open(self.filename, "r", encoding="utf-8") as f: 
            return f.read()