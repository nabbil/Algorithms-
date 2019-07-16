

class Hangman():
    def __init__(self):
        self.chances = 8
        self.word = list()
        self.hidden_Word = str()
        self.correct_gusses = int()
        self.word_list = ("Mango", "pear", "peach", "plum")

    def start(self):
        print("Welcome to HAngman")
        print("-" * 60)
        self.hidden_Word = random.choice(self.word_list)
        self.word = ['_'] * len(self.hidden_word)
        self.correct_gusses = "".join(self.word).count("_")
        self.instructions()

    def instructions(self):
        print("".join([i + " " for i in self.word]))
        print("You have {} chances left".format(self.chances))

    # here is the logic

    def ask(self):
        letter = input("Guess a Letter...")
        if letter.lower() == "quit":
            return False
        elif letter.lower() not in self.hidden_Word:
            print("{} is incorrect, please try again".format(letter))
            self.chances -= 1
        else:
            print("{} has been found !!".format(letter))
            for index, l in enumerate(self.hidden_word):
                if l is letter:
                    self.word[index] = letter
            self.correct_gusses = "".join(self.word).count("_")
        return True

    def main():
        game = Hangman()
        game.start()

        while True:
            while True:
                if game.ask() == False:
                    break
                if game.chances == 0:
                    print("What a loser!")


main()
