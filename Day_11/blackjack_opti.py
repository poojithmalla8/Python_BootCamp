from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def array_sum(array):
    return sum(array)


def print_cards(title, card_list, total):
    print(f"{title}'s Cards: {card_list} (Total: {total})")


def play_blackjack():
    print(logo)

    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]

    print_cards("Your", player, array_sum(player))
    print(f"Dealer's First Card: {dealer[0]} ")

    if array_sum(player) == 21:
        print("BlackJack! You win!!")
        return

    while True:
        choice = input("Do you wish to continue? 'yes' or 'no': ")
        if choice.lower() != 'yes':
            break

        player.append(random.choice(cards))
        player_total = array_sum(player)
        print_cards("Your", player, player_total)

        if player_total > 21:
            print("Busted ❌")
            print("Dealer Won")
            print_cards("Dealer", dealer, array_sum(dealer))
            return

    while array_sum(dealer) < 17:
        dealer.append(random.choice(cards))

    dealer_total = array_sum(dealer)
    print_cards("Dealer", dealer, dealer_total)

    player_total = array_sum(player)
    if dealer_total > 21 or player_total > dealer_total:
        print("Congratulations Player Won 🏆")
    elif player_total == dealer_total:
        print("Draw 😎")
    else:
        print("Dealer Won")


play_blackjack()
