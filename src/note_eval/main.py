#!/usr/bin/env python
# src/my_project/main.py

import sys
from note_eval.crew import NoteEvalCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'file_path': '\src\note_eval\my_note.txt'
    }
    NoteEvalCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()