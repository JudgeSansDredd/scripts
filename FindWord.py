import re


def find_word(needles, haystack):
    look_alikes = {
        'e': '3',
        'r': u'\u0154'
    }
    for needle in needles:
        char_array = [
            f"[{x.upper()}{x.lower()}{look_alikes[x.lower()] if x.lower() in look_alikes else ''}]"
            for x
            in needle
        ]
        exp = '[\W_]{0,2}'.join(char_array)
        if re.search(exp, haystack):
            return True
    return False

haystacks = [
    "This is f.r.e.e.",
    "This is free",
    "Freedom from something",
    "This is also fr33",
    "This is another way of saying F." + u'\u0154' + ".E.E.",
    "This should not get flagged"
]

needles = ["free"]

flagged_haystacks = [x for x in haystacks if find_word(needles, x)]

print(flagged_haystacks)
