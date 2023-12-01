def multipleReplace(text, dict):
    res = [i for i in list(dict.keys()) if i in text]  # get the matching part.

    for i in res:
        text = text.replace(i, dict[i])
    return text
