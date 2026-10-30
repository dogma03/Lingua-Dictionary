from dataclasses import dataclass

@dataclass
class Translation:
    word: str
    word_translation: str
    sentence: str
    sentence_translation:str


result = Translation(
    'apple',
    'яблокo',
    'i eat an apple',
    'я съел яблоко'
)
print(result)
