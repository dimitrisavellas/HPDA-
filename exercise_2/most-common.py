import json
from collections import Counter

JSON_FILE = "word_frequencies.json"

if __name__ == "__main__":
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        all_chapter_words = json.load(f)

    total_counts = Counter()
    for chapter_counts in all_chapter_words.values():
        total_counts.update(chapter_counts)

    for i, (word, count) in enumerate(total_counts.most_common(10), 1):
        print(f"{i}. {word}: {count}")