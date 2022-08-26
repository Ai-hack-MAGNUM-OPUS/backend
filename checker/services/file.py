def process_paragraphs(text):
    paragraphs = {}
    c = 0
    for line in text:
        ind = line[:2]
        if len(ind) == 2 and ind[1] == ".":
            try:
                ind = int(ind[0])
                c = ind
                paragraphs[c] = ""
            except ValueError:
                print()
            if c:
                paragraphs[c] += line
    return paragraphs