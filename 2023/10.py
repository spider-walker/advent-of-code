print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Solution Day 6")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

from pathlib import Path


def count_x(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count


def solve_a(camel_cards):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards.reverse()
    camel_cards.sort(
        key=lambda card: (
            5 in card["pairs"],
            4 in card["pairs"],
            3 in card["pairs"] and 2 in card["pairs"],
            3 in card["pairs"] and count_x(card["pairs"], 1) == 2,
            count_x(card["pairs"], 2) == 2,
            count_x(card["pairs"], 2) == 1 and count_x(card["pairs"], 1) == 3,
            count_x(card["pairs"], 1) == 5,
            cards.index(card["hand"][0]),
            cards.index(card["hand"][1]),
            cards.index(card["hand"][2]),
            cards.index(card["hand"][3]),
            cards.index(card["hand"][4]),
        ),
        reverse=False,
    )
    sum_of_values = 0
    for c, camel_card in enumerate(camel_cards):
        sum_of_values += camel_card["bids"] * (c + 1)

    print(sum_of_values)
    return sum_of_values


def solve_b(camel_cards):
    print("--- Part Two ---")
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    cards.reverse()
    camel_cards.sort(
        key=lambda card: (
            5 in card["pairs"] ,
            4 in card["pairs"],
            3 in card["pairs"] and 2 in card["pairs"],
            3 in card["pairs"] and count_x(card["pairs"], 1) == 2,
            count_x(card["pairs"], 2) == 2,
            count_x(card["pairs"], 2) == 1 and count_x(card["pairs"], 1) == 3,
            count_x(card["pairs"], 1) == 5,
            cards.index(card["hand"][0]),
            cards.index(card["hand"][1]),
            cards.index(card["hand"][2]),
            cards.index(card["hand"][3]),
            cards.index(card["hand"][4]),
        ),
        reverse=False,
    )
    sum_of_values = 0
    for c, camel_card in enumerate(camel_cards):
        print(camel_card)
        sum_of_values += camel_card["bids"] * (c + 1)

    print(sum_of_values)
    return sum_of_values


def read_data(file_name):
    lines = Path(file_name).read_text().splitlines()
    camel_cards = []
    for line in lines:
        hand = line.split(" ")[0]

        bids = int(line.split(" ")[1])
        pairs = {i: hand.count(i) for i in hand}
        count_j = pairs.get("J", 0)
        # print(hand,count_j)
        pairs_without_j = pairs.copy()
        if 1 <= count_j <= 4:
            del pairs_without_j["J"]
            idx = list(pairs_without_j.values()).index(
                max(list(pairs_without_j.values()))
            )
            pairs_without_j[list(pairs_without_j.keys())[idx]] = pairs_without_j[list(pairs_without_j.keys())[idx]] + count_j

        camel_cards.append({"hand": hand, "bids": bids, "pairs": list(pairs_without_j.values())})
    return camel_cards


# rs = read_lines = read_data("input")
# rs = solve_a(rs)

rs = read_lines = read_data("input")
rs = solve_b(rs)
# 247072115
# 247178142
# 247178142
# 247162126
# 247094319
# 249071353
# 249047606
# 250741882
# 250741882
# 249138943
# 249138943
