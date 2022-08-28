import os
import re
import convertapi


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


def doc_to_docx(file_path):
    convertapi.api_secret = '0fp22XFRPwKmNJql'
    result = convertapi.convert('docx', {'File': file_path}, from_format='doc')
    result.file.save(file_path.split(".")[0] + ".docx")
    return file_path.split(".")[0] + ".docx"


def doc_to_odt(file_path):
    convertapi.api_secret = '0fp22XFRPwKmNJql'
    result = convertapi.convert('docx', {'File': file_path}, from_format='odt')
    result.file.save(file_path.split(".")[0] + ".docx")
    return file_path.split(".")[0] + ".docx"


def media_upload_path(instance, filename):
    return os.path.join(f"uploads/{generate_charset(7)}/", filename)


def split_text(text):
    texts, groups = [], []
    regt = re.findall(r"{(.*?)}(.*?){(.*?)}", text.replace('\n', ''))
    for t in regt:
        if t[0] == t[-1]:
            texts.append(t[1])
            groups.append(int(t[0]))
        else:
            print(t)
    return texts, groups
