def split_numbers_letters(text):
    #NOTE - split_numbers_letters
    """Splits a string into its alphabetical and numerical parts.

    params:
        - str: text

    returns:
        - str: letters
        - str: numbers
    """
    letters = ''
    numbers = ''
    for char in text:
        print(char)
        if char.isalpha():
            print(char)
            text = text.replace(char, ' ')
    print(f"text: {text}")

    return letters, numbers

split_numbers_letters('R29C10')