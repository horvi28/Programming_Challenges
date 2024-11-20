triplet_score = {
    1: 1000,
    6: 600,
    5: 500,
    4: 400,
    3: 300,
    2: 200
}

single_score = {
    1: 100,
    5: 50,
    2: 0,
    3: 0,
    4: 0,
    6: 0
}

def count_values(dices: list) -> dict:
    counted_values = {}
    for dice in dices:
        if dice in counted_values:
            counted_values[dice] += 1
        else:
            counted_values[dice] = 1
    return counted_values

def task02(array):
    score = 0
    counted_values = count_values(array)
    for number in triplet_score.keys():
        if number in array:
            quantity = counted_values[number]
            while quantity > 0:
                if quantity >= 3:
                    score += triplet_score[number]
                    quantity -= 3
                elif quantity >= 1:
                    score += single_score[number]
                    quantity -= 1
    return score


if __name__ == "__main__":
    tests = [
                [5, 1, 3, 4, 1], # Result: 250
                [1, 1, 1, 3, 1], # Result: 1100
                [2, 4, 4, 5, 4], # Result: 450
                [1, 1, 1, 1, 3], # Result: 1100
                [3, 4, 5, 3, 3], # Result: 350
                [3, 3, 2, 4, 6], # Result: 0
                [1, 1, 1, 1, 5], # Result: 1150
                [6, 6, 6, 6, 6]  # Result: 600
            ]

    for t in tests:
        print(task02(t))