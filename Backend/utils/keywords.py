from data.policies import STOP_WORDS


def extract_keywords(content):
    words = content.lower().split()
    keywords = []

    for word in words:
        cleaned_word = word.strip(".,!?():;\"'")
        if cleaned_word and cleaned_word not in STOP_WORDS:
            keywords.append(cleaned_word)
    return keywords
