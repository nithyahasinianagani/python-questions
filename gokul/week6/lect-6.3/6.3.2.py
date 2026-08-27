# create a function , clean to remove punctuation from the text and keep only the alphas


x="dkashdhas!;'.//.-#$!@"


def clean(text):
    result = ""

    for char in text:
        if char.isalpha():
            result += char

    return result

print(clean(x))