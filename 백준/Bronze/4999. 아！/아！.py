import sys

is_ahh = False

user_sound = str(sys.stdin.readline().strip())
doc_sound = str(sys.stdin.readline().strip())


if len(user_sound) >= len(doc_sound):
    print('go')

else:
    print('no')
