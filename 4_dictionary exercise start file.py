# This program uses a dictionary as a deck of cards.

def main():
    # Create a deck of cards.
   
    deck = create_deck() #no arguments in def create_deck so nothing goes in parenthesees
    # Get the number of cards to deal.
    
    num_cards = int(input('How many cards should I deal? '))



    # Deal the cards.

    deal_cards(deck,num_cards)#numcards is an int object and deck is a dictionary object
    #why don't we have a variable like with deck = create deck?
        #deal_cards is not a value returning function and doesn't have to have a variable to save it into

    

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck(): #value returning function; creates a dictionary called deck
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck #have to return for a value returning function 
    #have to save it into some type of variable in the main function
#Cannot have duplicate keys in a dictionary


# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number): #not empty, expects two objects sent to it 
                                #first one has to be a dictionary and second one has to be an object
                                #want to print out the total value of the cards  (handValue variable (accumulator))
    # Initialize an accumulator for the hand value.
    handValue = 0
   

    
    

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.

    if number > 52:
        number = 52
    

    # Deal the cards and accumulate their values.
    '''
    for count in range(number):
        card,value = deck.popitem()
        print(card)
        handValue += value

    '''
    import random
    for count in range(number): #number is th number of cards that the user wants
                                #for loop repeats that number of times
                                #value of count is irrelevent because we're not using it anywhere
        card = deck[random.choice(list(deck))]#default for dictionary is the key
                                            #the key is only converted to a list
                                            #innermost function in parenthesees performed first
                                            #choice is a method of the random module that allows you to pick a random element in the list
        print(card)  #saved into a random variable called card      
        #prints name of card             
        value = deck[card] #gets the value of the card
        handValue += value #increment the accumulator variable by whatever value is returned for the number of times the user put in
        

    # Display the value of the hand.
    print('the value of the hand is',handValue)
    
    

# Call the main function.
main()
