import docx2txt
import requests
from celery import shared_task

from checker.models import Paragraph, Docx
from checker.services.file import process_paragraphs


@shared_task()
def process_file(pk: int):
    file = Docx.objects.get(pk=pk)
    uuid = file.uuid
    document = docx2txt.process(file.file.path)
    paragraphs = process_paragraphs(document)

    file.paragraphs_loaded = len(paragraphs)
    file.save(update_fields=["paragraphs_loaded"])

    cut = 100
    counter = 0
    len_c = len(paragraphs)
    paragraphs = list(paragraphs.values())
    for i in range(0, len(paragraphs) // cut + 1):
        vals = paragraphs[i * cut : (i + 1) * cut + 1]
        dct = {x: vals[x] for x in range(len(vals))}

        x = requests.post("http://109.248.175.223:5000/api", json=dct)
        for el_id, type_id in x.json().items():
            Paragraph.objects.create(type_id=type_id, docx=file, text=dct[int(el_id)])

        counter += len(vals)
        print(f"processing {uuid}, {counter}/{len_c}")
        file.paragraphs_processed = counter
        file.save(update_fields=["paragraphs_processed"])

    return f"ok, {pk}"
