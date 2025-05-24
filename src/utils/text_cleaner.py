from ast import literal_eval

def ffo(text, letter):
    for i, char in enumerate(text):
        if char == letter:
            return i
    return False

def flo(text, letter):
    id = False
    for i, char in enumerate(text):
        if char == letter:
            id = i
    return id

def remove_trailers(text: str, letter: str) -> str:
    try:
        fid = ffo(text, letter[0])
        if fid != False:
            text = text[fid:]
            print(text)
            lid = flo(text, letter[1])
            text = text[:lid+1]
            text = literal_eval(text.strip())
            return text
    except Exception as e:
        print(f"An Exception occurred: {e}, {text}")