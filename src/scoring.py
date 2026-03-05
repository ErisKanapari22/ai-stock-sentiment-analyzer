def label_from_compound(compound: float) -> str:

    if compound >= 0.05:
        return "positive"

    if compound <= -0.05:
        return "negative"

    return "neutral"