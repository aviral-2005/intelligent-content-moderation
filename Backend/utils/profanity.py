from data.policies import PROFANITY_WORDS


def contains_profanity(keywords):
    for word in keywords:
        if word in PROFANITY_WORDS:
            return True

    return False