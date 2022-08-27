import os

from checker.services.generators import generate_charset


def _base_process(text):
    paragraphs = {}
    c = 1
    title = True
    for line in text:
        if title:
            if line and len(line) > 2 and line[:2] == "1.":
                title = False
        else:
            if line:
                paragraphs[c] = line
                c += 1
    return paragraphs


def process_paragraphs(text):
    text = text.split("\n")
    return _base_process(text)


def process_word_paragraphs(text):
    text = text.split("\\r")
    return _base_process(text)


def media_upload_path(instance, filename):
    return os.path.join(f"uploads/{generate_charset(7)}/", filename)
