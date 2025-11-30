import re
import csv
import json
from collections import Counter

FILENAME = "moby_dick.txt"

def load_chapters_with_titles(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    start_match = re.search(r"CHAPTER\s+1\.", text)
    book_text = text[start_match.start():] if start_match else text

    parts = re.split(r"(CHAPTER [IVXLCDM\d]+\. .+)", book_text)
    titles = []
    texts = []
    for i in range(1, len(parts), 2):
        titles.append(parts[i].strip())
        texts.append(parts[i+1].strip())
    return titles, texts

if __name__ == "__main__":
    chapter_titles, chapter_texts = load_chapters_with_titles(FILENAME)

    csv_rows = []
    json_data = {}

    for title, chapter in zip(chapter_titles, chapter_texts):
        words = re.findall(r"\b\w+\b", chapter.lower())
        total_words = len(words)
        unique_words = len(set(words))
        word_counts = dict(Counter(words))

        csv_rows.append([title, total_words, unique_words])
        json_data[title] = word_counts

    # CSV
    with open("chapter_stats.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["chapter-name", "chapter-length", "unique-words"])
        writer.writerows(csv_rows)

    # JSON
    with open("word_frequencies.json", "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)

    print("Wrote chapter_stats.csv and word_frequencies.json")