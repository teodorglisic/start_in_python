def check_palindrome(word: str) -> bool:
    x = 1
    inner_res = True

    word = word.upper()

    if len(word) % 2 == 0:
        a = len(word) / 2
    else:
        a = (len(word) - 1) / 2

    while inner_res is not False and x < a:
        if word[x - 1] == word[len(word) - x]:
            x += 1
        else:
            inner_res = False

    return inner_res
