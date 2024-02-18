def solve_test_case(n, trump_suit, cards):
    # Separate cards into trump and non-trump
    trump_cards = []
    non_trump_cards = []
    for card in cards:
        if card[1] == trump_suit:
            trump_cards.append(card)
        else:
            non_trump_cards.append(card)

    # Sort the cards
    trump_cards.sort(key=lambda x: (x[0], x[1]))
    non_trump_cards.sort(key=lambda x: (x[0], x[1]))

    played_rounds = []
    for _ in range(n):
        # Play a non-trump card if available, else play the lowest trump card
        if non_trump_cards:
            card1 = non_trump_cards.pop(0)
        else:
            card1 = trump_cards.pop(0)

        card2 = None
        # If there are trump cards available, try to find one that beats the played card
        if trump_cards:
            for trump_card in trump_cards:
                if trump_card[1] == card1[1]:
                    if trump_card[0] > card1[0]:
                        card2 = trump_card
                        trump_cards.remove(trump_card)
                        break
                else:
                    card2 = trump_card
                    trump_cards.remove(trump_card)
                    break
            else:
                card2 = None
        else:
            card2 = None

        played_rounds.append((card1, card2))

    return played_rounds


def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        trump_suit = input().strip()
        cards = input().strip().split()

        result = solve_test_case(n, trump_suit, cards)

        if result:
            for round in result:
                if round[1]:
                    print(round[0], round[1])
                else:
                    print("IMPOSSIBLE")
        else:
            print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
