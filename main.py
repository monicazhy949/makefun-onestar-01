"""One-line one-star review of an everyday essential, for make.fun."""
import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "One star. Sleep takes eight hours a night, returns me unrested, "
    "and then ships a Monday anyway."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
