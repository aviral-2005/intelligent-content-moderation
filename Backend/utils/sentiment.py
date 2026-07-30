from data.policies import POSITIVE_WORDS, NEGATIVE_WORDS


def analyze_sentiment(keywords):

    positive = 0
    negative = 0

    for word in keywords:

        if word in POSITIVE_WORDS:
            positive += 1

        elif word in NEGATIVE_WORDS:
            negative += 1

    if positive > negative:
        return "Positive"

    elif negative > positive:
        return "Negative"

    return "Neutral"
