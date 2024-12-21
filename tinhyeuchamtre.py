import time
import sys

def fade_in_text(text, delay=0.1):
    """Simulate fade-in effect by printing text character by character with a delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Newline after the text

def fade_in_words(text, delay=0.1):
    """Simulate fade-in effect for words."""
    words = text.split(" ")
    for word in words:
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fade_in_and_move_from_right(space, text, delay=0.1, move_speed=1):
    """Simulate fade-in effect while moving text from right to left."""
    print(" " * space, end="")  # Add leading spaces to simulate starting from the right
    fade_in_text(text, delay)

def show_each_letter(text, delay=0.1):
    """Display each letter with a delay, similar to typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flash_line_fade_in_out_once(text, times=1):
    """Simulate flashing text (fade in and out)."""
    for _ in range(times):
        sys.stdout.write("\033[1;32m" + text + "\033[0m")  # Green text color for visibility
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r" + " " * len(text))  # Clear the line
        sys.stdout.flush()
        time.sleep(0.5)
    print()  # Move to the next line after flashing

# Test with the lines you've provided
line1a = "▶ Anh thường nghĩ"
line1 = "▶ Mình quên mất rồi"
line2 = "♫ Thời gian ngỡ trôi sẽ cách lòng"
line3 = "▶ Cảm xúc nhất thời"
line4 = "♪ Mà đâu biết say một đời …"
line5 = "𝄫 Rồi khi đã biết là, "
line5a = "\t\t\t người em vốn thiết tha"
line6 = "♩ Chẳng phải nơi này"
line6a = "\t\t\t mà từ một nơi xa"
line7 = "𝄞 Lặng nghe em nói"
line7a = "𝄞 Lòng anh đau nhói"
line8 = "𝄞 Cứ trách sao không nhận ra"
line8a = "tình yêu sớm hơn..."

time.sleep(0.5)
print()
fade_in_words(line1a, 0.02)
fade_in_text(line1, 0.2)
print()

time.sleep(0.9)
fade_in_and_move_from_right(35, line2, 0.15, 20)

time.sleep(1.5)
fade_in_words(line1a, 0.05)
fade_in_text(line3, 0.2)
print()

time.sleep(0.9)
fade_in_and_move_from_right(35, line4, 0.15, 20)

time.sleep(0.9)
show_each_letter(line5, delay=0.08)
time.sleep(0.6)
fade_in_text(line5a, 0.2)
print()

time.sleep(0.5)
fade_in_and_move_from_right(30, line6, 0.09, 20)
show_each_letter(line6a, delay=0.09)
print()

time.sleep(1)
flash_line_fade_in_out_once(line7, 2)
time.sleep(0.5)
flash_line_fade_in_out_once(line7a, 2)

fade_in_text(line8, 0.2)
if line8a.endswith("..."):
    main_text = line8a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print()
