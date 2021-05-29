from random import shuffle


def get_random_answer() -> list[int]:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 4
    answer = []
    while count > 0:
        shuffle(numbers)
        answer.append(numbers.pop())
        count -= 1

    return answer


def get_input() -> list[str]:
    str_input = input('Guess a number with 4 digit: ')
    str_inputs = list(str_input)

    guess = list(map(lambda x: int(x), str_inputs))

    if len(guess) != 4:
        raise RuntimeError("The number should exactly 4 digit: ")

    if len(set(guess)) != len(guess):
        raise RuntimeError("The number cannot be duplicated")

    return guess


def check_status(guess: list[int], answer: list[int]) -> tuple[int, int]:
    A = 0
    B = 0

    for index, ans in enumerate(answer):
        if ans == guess[index]:
            A += 1
            continue
        if ans in guess:
            B += 1

    return (A, B)


def main():
    answer = get_random_answer()
    correct_status = (4, 0)
    status = (0, 0)
    while status != correct_status:
        try:
            guess = get_input()
        except RuntimeError as e:
            print(e)
            continue
        except:
            print('Input is not valid, try again')
            continue

        status = check_status(guess, answer)
        if status != correct_status:
            print("{0}A{1}B".format(status[0], status[1]))

    print('You win! The answer is ' +
          "".join(list(map(lambda x: str(x), answer))))


main()
