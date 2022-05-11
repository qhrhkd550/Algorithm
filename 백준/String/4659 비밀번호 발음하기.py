'''
  * 아이디어 1
    - 주어진 조건대로 처리하면 간단하다.
'''
import sys
input = lambda : sys.stdin.readline().rstrip()


def aeiou_check():
    for i in password:
        if i in 'aeiou':
            return True
    return False

def continue_three_check():
    for i in range(len(password) - 2):
        if password[i] in 'aeiou':
            if password[i+1] in 'aeiou' and password[i+2] in 'aeiou':
                return False

        elif password[i] not in 'aeiou':
            if password[i+1] not in 'aeiou' and password[i+2] not in 'aeiou':
                return False

    return True

def same_word_check():
    for i in range(len(password) - 1):
        if password[i] not in 'eo':
            if password[i] == password[i+1]:
                return False

    return True


while True:
    password = input()
    if password == 'end':
        break

    if aeiou_check():
        if continue_three_check():
            if same_word_check():
                print("<" + password + "> is acceptable.")
            else:
                print("<" + password + "> is not acceptable.")
                continue

        else:
            print("<" + password + "> is not acceptable.")
            continue
    else:
        print("<" + password + "> is not acceptable.")
        continue
