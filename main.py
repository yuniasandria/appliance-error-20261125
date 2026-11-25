"""The Funniest Honest Appliance Error — microwave edition.

One line, at most 200 characters: the funniest honest error message an
appliance could show. The laugh comes from the truth of the fault: everyone
mashes the +30s button instead of typing a time, and the microwave knows.
"""

LINE = (
    "ERROR E9: You pressed +30 seconds 14 times instead of typing 7:00. "
    "Your rice has now cooked for 7 minutes and none of it was a decision."
)


def main():
    import os

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)

    assert len(LINE) <= 200, "line exceeds 200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have surrounding whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
