from random import shuffle as s


suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

class Deck:

    def __init__(self):
        cards = []
        for s in suits:  # Fill the deck with standard playing cards
            for val in range(1, 14):
                cards.append(self._Card(s, val))
        self.cards = cards

    def __iter__(self):
        return self.cards.__iter__()

    def __str__(self):  #TODO Fix this to state whether or not the deck is sorted or shuffled; ✅
        return 'A deck of {0} {1} cards'.format(self.size, 'sorted' if self.is_sorted else 'shuffled')


    @property  # Property to get the length of the cards list
    def size(self):
        return len(self.cards)

    @property  #TODO Implement a method to determine if the cards are sorted; ✅
    def is_sorted(self):
        for i in range(len(self.cards) - 1):
            current_card = self.cards[i]
            next_card = self.cards[i + 1]
            if (current_card.value == next_card.value and current_card.suit_name + 1 == next_card.suit_name) \
                    or (current_card.suit_name == 3 and next_card.suit_name == 0):
                continue
            else:
                return False
        return True



    def sort(self):  #TODO Implement a method to sort cards by suit and value; ✅
        # Using bubble sort;
        unordered_list = self.cards
        iteration_number = len(unordered_list) - 1
        for i in range(iteration_number, 0, -1):
            for j in range(i):
                if unordered_list[j].value > unordered_list[j + 1].value \
                        or (unordered_list[j].value == unordered_list[j + 1].value
                            and unordered_list[j].suit_name > unordered_list[j + 1].suit_name):
                    temp = unordered_list[j]
                    unordered_list[j] = unordered_list[j + 1]
                    unordered_list[j + 1] = temp


    def shuffle(self):  # Method to put cards list in random order
        shuffled_deck = s(self.cards)
        return shuffled_deck

    # A constant time search can be achieved by maintaining a separate array of integers representing card orders
    # the sorted state is where the deck is in its natural sorted order, & the 'order' array's values will be 0, 1, 2, ... 52
    # when shuffling, we alter the ordering of the 'order' array
    # when enumerating the shuffled list, we'll be getting the cards in the order represented by 'order' array:
        # deck.cards[order[index]]
    # when searching, index of an element we simply return
        # order[card's natural order index]
    def search(self, value, suit):  #TODO Implement a public search method; ✅
        for i in range(len(self.cards)):
            current_card = self.cards[i]
            if current_card.value == value and current_card.suit_name == suit:
                return i
        return -1

    def _describe_card(self): # User facing private function to create a card to search for
        print("What suit is the card?")  # Pick a suit
        prompt = ""
        i = 1
        for suit in suits: # Build prompt to pick suit
            prompt +='{}. {}\n'.format(i, suit)
            i += 1
        while True:
            s = int(input(prompt)) # Collect user info for suit
            v = int(input("Enter a number from 1 to 13 (1 = Ace, 11 = Jack, 12 = Queen, 13 = King): ")) # Collect user info for value
            if s in [1, 2, 3, 4] and v in [x for x in range(1, 14)]:
                card = self._Card(suits[s - 1], v)
                break
            print("Invalid card, try again") # If invalid try again
        return card


    class _Card: # Private inner class to create a Card
        def __init__(self, suit, value): # Need a suit and a value. Will be two integers. 0-3 for suit and 1-13 for value
            self.suit = suit
            self.value = value

        def __str__(self): # Print override
            return '{self.value_name} of {self.suit}'.format(self=self)

        def __eq__(self, card): # Equals override
            if self.suit != card.suit:
                return False
            if self.value != card.value:
                return False
            return True

        @property # Get proper suit name
        def suit_name(self):
            if self.suit == suits[0]:
                return 0
            elif self.suit == suits[1]:
                return 1
            elif self.suit == suits[2]:
                return 2
            elif self.suit == suits[3]:
                return 3
            else:
                raise ValueError()

        @property # Get proper value name
        def value_name(self):
            if self.value == 1:
                return "Ace"
            elif self.value == 11:
                return "Jack"
            elif self.value == 12:
                return "Queen"
            elif self.value == 13:
                return "King"
            else:
                return self.value





if __name__ == '__main__':  # Main method
    deck = Deck()  # Create empty Deck object


    deck.shuffle()
    deck.search(1, 2)
