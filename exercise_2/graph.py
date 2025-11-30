#!/usr/bin/env python3
import re
import matplotlib.pyplot as plt

FILENAME = "moby_dick.txt"

def load_chapters(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Cut off everything before CHAPTER 1.
    start_match = re.search(r"CHAPTER\s+1\.", text)
    book_text = text[start_match.start():] if start_match else text

    parts = re.split(r"(CHAPTER [IVXLCDM\d]+\. .+)", book_text)
    chapter_texts = []
    for i in range(1, len(parts), 2):
        chapter_texts.append(parts[i+1].strip())
    return chapter_texts

def word_frequencies_per_chapter(chapter_texts, word):
    freqs = []
    for chapter in chapter_texts:
        words = re.findall(r"\b\w+\b", chapter.lower())
        total = len(words)
        count = words.count(word.lower())
        rel = count / total if total > 0 else 0
        freqs.append(rel)
    return freqs

if __name__ == "__main__":
    chapters = load_chapters(FILENAME)
    search_word = input("Enter word to search: ").strip().lower()

    rel_freqs = word_frequencies_per_chapter(chapters, search_word)

    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(rel_freqs) + 1), rel_freqs, width=0.8)
    plt.title(f"Relative Frequency of '{search_word}' per Chapter")
    plt.xlabel("Chapter")
    plt.ylabel("Relative Frequency")
    plt.tight_layout()
    plt.show()
