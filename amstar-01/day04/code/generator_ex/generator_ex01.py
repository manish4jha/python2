import random

def vowels():
    yield "a"
    yield "e"
    yield "i"
    yield "o"
    yield "u"


def create_emoticon_generator():
    i = 5
    while i > 0:
        strings = "!@#$^*_-=+?/,.:;~"
        grouped_strings = [("(", ")"), ("<", ">"), ("[", "]"), ("{", "}")]
        grp = random.choice(grouped_strings)
        face_strings_list = [random.choice(strings) for _ in range(3)]
        face_strings = "".join(face_strings_list)
        emoticon = (grp[0], face_strings, grp[1])
        emoticon = "".join(emoticon)
        yield emoticon
        i -= 1

''''       
if __name__ == "__main__":
    for i in vowels():
        print(i)

    g = create_emoticon_generator()
    print([next(g) for _ in range(10)])
'''
