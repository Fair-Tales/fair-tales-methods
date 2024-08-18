import pandas as pd
import string


def replace_speech_marks(text):
    new_text = text.replace('“', '"').replace('”', '"').replace('’', '\'')
    return new_text


def discount_speech_marks(text, marks=['“', '"', '”', '’', '\'']):
    new_text = text
    if text[0] in marks:
        new_text = text[1:]
    if new_text[-1] in marks:
        new_text = new_text[:-1]
    return new_text


def remove_the(text):
    new_text = text
    if text[0:3].lower() == 'the':
        new_text = text[3:].strip()
    return new_text


def compare_strings(
        string_1, string_2,
        _case_sensitive=True,
        _strip_whitespace=True,
        _replace_speech_marks=True,
        _discount_leading_trailing_marks=True,
        _remove_leading_the=False
):
    if _case_sensitive:
        s_1 = string_1
        s_2 = string_2
    else:
        s_1 = string_1.lower()
        s_2 = string_2.lower()

    if _strip_whitespace:
        s_1 = s_1.strip()
        s_2 = s_2.strip()

    if _replace_speech_marks:
        s_1 = replace_speech_marks(s_1)
        s_2 = replace_speech_marks(s_2)

    if _discount_leading_trailing_marks:
        s_1 = discount_speech_marks(s_1)
        s_2 = discount_speech_marks(s_2)

    if _remove_leading_the:
        s_1 = remove_the(s_1)
        s_2 = remove_the(s_2)

    return s_1 == s_2


def spacy_extract_sentences(df, nlp):
    sentences = pd.DataFrame()

    book_col = []
    sentences_col = []
    length_col = []
    index_col = []

    for title, text in zip(df.Title, df.Text):
        text = text.replace('\n',
                            ' ')  # This is only safe provided the line break is not being used to separate sentences w/o puntctuation...
        text = text.replace('\t', ' ')  # This allows us to save as tsv (and simplifies the whitespace)
        text = ' '.join(text.split())

        doc = nlp(text)
        sentence_list = list(doc.sents)

        for si, sen in enumerate(sentence_list):
            book_col.append(title)

            doc = sen  # nlp(sen.text.strip())
            sentences_col.append(doc)
            length_col.append(len(doc.text.translate(str.maketrans('', '', string.punctuation)).split(' ')))
            index_col.append(si)

    sentences['book'] = book_col
    sentences['sentence_length'] = length_col
    sentences['sentence'] = sentences_col
    sentences['sentence_index'] = index_col

    return sentences