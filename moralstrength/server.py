from typing import Union
from moralstrength import estimate_morals
from moralstrength.lexicon_use import select_version

from fastapi import FastAPI

from moralstrength.moralstrength import string_moral_values

app = FastAPI()


@app.get("/parse")
def parse_text_moral_strength_lexicon(
    text: str, lexicon: str = None, model: str = None
) -> dict:
    """Uses MoralStrength lexicon only to parse text"""

    if lexicon is not None:
        select_version(lexicon)
        df = estimate_morals([text], process=True)
        return df.iloc[0].fillna(0).to_dict()
    elif model is not None:
        return string_moral_values(text, model=model)

    else:
        raise ValueError("Must specify either lexicon or model")
