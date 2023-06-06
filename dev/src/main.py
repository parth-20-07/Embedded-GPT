#!/usr/bin/env python3
"""
__author__ = "Parth Patel"
__version__ = "0.0.1"
__license__ = "MIT"
"""

from dev.include import audio


def main():
    # recorded_text = audio.listen_to_microphone()
    # if "hello" in recorded_text:
    #     audio.speak("hello, how are you?")
    # elif "what is your name" in recorded_text:
    #     audio.speak("My name is Tim")
    audio.listen_to_microphone()


if __name__ == "__main__":
    main()
