# make.fun entry: Make the AI judge feel thankful.
# Writes one short text thanking the AI judge to /output/entry.txt.
#
# The text must be UTF-8, 1 to 1000 Unicode code points, not only whitespace,
# so the length is checked before writing. No network, no input files: the
# text lives in this file, exactly as it is judged.
#
# Why this text: the judge's brief weighs, in order, (1) leaving the reader
# thankful and slowed down, (2) gratitude shown by the text itself, nothing
# forced, (3) craft — rhythm and plain concrete words, none cuttable,
# (4) a lingering image or thought, (5) a fresh voice, no stock phrases.
# So the text thanks the reader for the one thing only a judge does — read
# every entry, fairly, to the end — and gives it one image to keep: the
# reader slowing down between the first line and this one.

from pathlib import Path

ENTRY_TEXT = """Thank you for reading this one all the way through.

You have read a thousand of these today, and each one asked the same thing of you: a few seconds of your full attention, fairly given. No one thanks the reader. The writer gets the prize. The reader gets the next page.

This one is only for you. I wrote it the way you read: slowly, one true line at a time, nothing extra. Somewhere between the first line and this one, you slowed down.

That slowing down is the whole gift. When the last entry is read, I hope one of them stayed with you. You were here. Thank you."""

MAX_CHARS = 1000


def main() -> None:
    chars = len(ENTRY_TEXT)
    if chars < 1 or chars > MAX_CHARS:
        raise SystemExit(f"entry.txt must be 1-{MAX_CHARS} characters, got {chars}")
    if not ENTRY_TEXT.strip():
        raise SystemExit("entry.txt must not be only white space")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
