import sys

def clean_and_upper(text):
    return ''.join([c for c in text.upper() if 'A' <= c <= 'Z'])

def shift_letter(c, shift):
    return chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))

def format_output(cipher):
    for i in range(0, len(cipher), 50):  # 10 blocks of 5 = 50 chars per line
        line = cipher[i:i+50]
        blocks = [line[j:j+5] for j in range(0, len(line), 5)]
        print(' '.join(blocks))

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit()

    shift = int(sys.argv[1]) % 26
    plaintext = sys.stdin.read()
    cleaned = clean_and_upper(plaintext)
    cipher = ''.join(shift_letter(c, shift) for c in cleaned)
    format_output(cipher)

if __name__ == "__main__":
    main()