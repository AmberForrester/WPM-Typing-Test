import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0, errors=0):
    stdscr.addstr(0, 0, target)
    stdscr.addstr(1, 0, f"WPM: {wpm} | Errors: {errors}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1 if char == correct_char else 2)
        stdscr.addstr(0, i, char, color)

def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def calculate_wpm(start_time, num_chars):
    time_elapsed = max(time.time() - start_time, 1)
    return round((num_chars / (time_elapsed / 60)) / 5)

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    errors = 0
    total_chars_typed = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Non-blocking input mode

    while True:
        correct_input = "".join(current_text) == target_text[:len(current_text)]
        
        # Calculate WPM based on total characters typed, including mistakes
        total_chars_typed = len(current_text)
        wpm = calculate_wpm(start_time, total_chars_typed)
        
        # Count errors based on incorrect characters
        errors = sum(1 for i, char in enumerate(current_text) if char != target_text[i])

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm, errors)
        stdscr.refresh()

        # Check if user completed the text
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  # Stop non-blocking input
            break

        try:
            key = stdscr.getkey()
        except curses.error:
            continue

        if ord(key) == 27:  # ESC key to exit the program
            return False, wpm, errors  # Exit the function and game

        if key == '\n':  # Enter key
            stdscr.nodelay(False)
            return True, wpm, errors  # Early exit, return stats

        # Handle backspace
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    return True, wpm, errors  # Completed the test, return stats

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        # Start WPM test, returns False if ESC is pressed, and return WPM and errors
        completed, final_wpm, total_errors = wpm_test(stdscr)

        if not completed:
            break  # Exit the game if ESC is pressed

        stdscr.addstr(2, 0, f"You completed the text! Your WPM: {final_wpm}, Errors: {total_errors}")
        stdscr.addstr(3, 0, "Press any key to play again or Esc to quit.")
        stdscr.refresh()
        
        try:
            key = stdscr.getkey()
        except curses.error:
            continue

        if ord(key) == 27:  # Exit on ESC key
            break

wrapper(main)
