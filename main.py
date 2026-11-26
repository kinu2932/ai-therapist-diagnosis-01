"""Your AI Therapist's Diagnosis entry: write one funny line to /output/entry.txt."""

import os

LINE = "Diagnosis: advanced procrastination. You booked 47 therapy sessions to avoid one conversation, and this is session 48. It auto-renews."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
