import pandas as pd


vowls = ["a", "e", "i", "o", "u"]

adjectives: pd.DataFrame = pd.read_csv("./english-adjectives.txt", header=None)
nouns: pd.DataFrame = pd.read_csv("./english-nouns.txt", header=None)


def get_tweet_content() -> str:
    random_adjective: str = adjectives.sample(1)[0].values[0]
    random_noun: str = nouns.sample(1)[0].values[0]

    extra_n: str = "n" if random_adjective[0] in vowls else ""

    return f"Game development is exactly like a{extra_n} {random_adjective} {random_noun}."

