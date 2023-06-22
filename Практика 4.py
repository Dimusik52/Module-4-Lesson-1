def is_palindrom(stroka):
    if stroka == stroka[::-1]:
        return True
    else:
        return False

inp = str(input())

print(is_palindrom(inp))