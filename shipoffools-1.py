import random


class ShipOfFoolsGame:
    """
    This class contains Game logic for Ship Of Fools game and has a object
    of Dicecup. Finally winning score is intialized,which is use to halt
    the game if the player got scored grater or equal to wiining score.
    ----------------------------------------------------------------------
    The attributes of the class are:
    __cup = Object of Dice cup
    winning__score = score, which stop the iteration(Game)
    """
    def __init__(self):
        """
        Intilizing a list for DiceCup objects and a winning score to 21.
        """
        self.__cup = DiceCup(5)
        # constant variable
        self.__WINNING_SCORE = 21

    def round(self, name, j):
        """This function has a game logic of first 6 valued dice should
            be banked,then 5 valued dice should be banked and last 4
            valued dice should be banked.Then all dice which values
            greater than 3 will be banked.The cargo value is calculated
            and sends to player...
            ---------------------------------------------------------
            The identifiers are :
            has_ship : bool value
            has_caption: bool value
            has_crew : bool value
            cargo : player's cargo score
            l : list of dice values
            """
        has_ship = False
        has_caption = False
        has_crew = False
        self.__name = name
        self.cargo = 0
        self.l = [0] * self.__cup.n

        for _ in range(3):
            self.__cup.roll()
            for k in range(5):
                dival = self.__cup._dice[k].get_value()
                self.l[k] = dival
            print(self.l)

            if not has_ship and 6 in self.l:
                s = self.l.index(6)
                self.__cup.bank(s)
                has_ship = True

            if has_ship and not has_caption and 5 in self.l:
                c = self.l.index(5)
                self.__cup.bank(c)
                has_caption = True

            if has_caption and not has_crew and 4 in self.l:
                cr = self.l.index(4)
                self.__cup.bank(cr)
                has_crew = True

            if has_ship and has_caption and has_crew:
                for i in range(5):
                    if self.l[i] > 3:
                        self.__cup.bank(i)

        if has_ship and has_caption and has_crew:
            self.cargo = sum(self.l) - 15
            print(
                f"The score of {self.__name} in Round {j} is: {self.cargo}"
                )
        else:
            print(
                f"""The score of {self.__name} in Round {j} is: 0"""
                )

        self.__cup.release_all()

    @property
    def get_winning_score(self):
        return self.__WINNING_SCORE


class DiceCup:
    """
    This class deals with the Die class object.While intializing the
    object of this class n number of objects of Die class is stored in
    a list.In this class we have functions to return current dice value
    ,banking a dice,unbanking a dice and rolling of unbanked dice.
    ------------------------------------------------------------------
    The attributes of the class are :
    dice : list of objects of dice class
    bnklst : list of bool value represents banked or not
    n : no of objects to be created
    """
    def __init__(self, n):
        """
        Intilizing the list for storing objects of Class Die,list for
        bank identification.
        """
        self._dice = []
        self.bnklst = [False, False, False, False, False]
        self.n = n
        for _ in range(self.n):
            die = Die()
            self._dice.append(die)

    def value(self, index):
        """ This function returns the dice value by taking a index as a
            parameter"""
        return self._dice[index].get_value()

    def bank(self, index):
        """
        This function will bank the dice by taking a index as parameter.
        """
        self.bnklst[index] = True

    def is_banked(self, index):
        """This function is used to identify wheater the dice is
            Banked or Not."""
        return self.bnklst[index]

    def release(self, index):
        """This function will realse the dice by taking index as
            parameter."""
        self.bnklst[index] = False

    def release_all(self):
        """This function will release all the dices."""
        for i in range(len(self.bnklst)):
            self.bnklst[i] = False

    def roll(self):
        """This function will roll the unbanked dice by checking each
            dice wheater it is banked or not."""
        for d in range(self.n):
            if self.is_banked(d) is False:
                self._dice[d].roll()


class Die:
    """
    This class describe about the die value intialization,
    has a function to roll a die and also has a function to return
    current dice value
    value : dice value
    """
    def __init__(self):
        """Intilizing the dice value when object is created."""
        self.__value = 1

    def get_value(self):
        """ This function returns the dice value in current state."""
        return self.__value

    def roll(self):
        """ This function will roll the dice and changes the dice value."""
        self.__value = random.randint(1, 6)


class PlayRoom:
    """This PlayRoom class will create a room for the players and game.
        also setting the game for 2 players,adding the player objects in
        list, creating the game object and calling the round function
        from player by giving game object and finally printing scores
        and display the winner.
        ----------------------------------------------------------------
        The attributes are :
        game : Object of ShipOfFools
        players : list of Objects of Player class
        j : count of rounds
        p : name of the winner
        """
    def __init__(self):
        """Intilizing the game for ShipofFoolGame object and a list for
            the palyers."""
        self.__game = 0
        self.__players = []
        self.__j = 0
        self.__p = 0

    def set_game(self, game):
        """Setting the game by creating the object of ShipofFoolsGame
            class"""
        self.__game = game

    def add_player(self, player):
        """ This function will add the players to the list."""
        self.__players.append(player)

    def reset_scores(self):
        """This function will reset all players score to 0."""
        for i in range(len(self.__players)):
            self.__players[i].__score = 0

    def play_round(self):
        """This Function will call the players round function for
            playing the game."""
        self.__j += 1
        for i in range(len(self.__players)):
            self.__players[i].play_round(self.__game, self.__j)

    def game_finished(self):
        """ Checking the player score and winning score return true if
            score reaches the winning score else return false."""
        self.__scolis = [0] * len(self.__players)
        for i in range(len(self.__players)):
            self.__scolis[i] = self.__players[i].current_score()
        if max(self.__scolis) >= self.__game.get_winning_score:
            return True
        else:
            return False

    def print_scores(self):
        """This function will print the scores of players."""
        for i in range(len(self.__players)):
            print(f"{self.__players[i].get_name()} : ", end='')
            print(self.__players[i].current_score())

    def print_winner(self):
        """This function will print the Winner name."""
        self.__max = max(self.__scolis)
        self.__min = min(self.__scolis)
        if self.__min == self.__max:
            print("The Game is on Tie Play the Game Again :-)")
        elif (
              self.__max >= self.__game.get_winning_score and
              self.__min >= self.__game.get_winning_score
              ):
            print("All the Players are in Winning State.Play Again")
        else:
            self.__i = self.__scolis.index(max(self.__scolis))
            self.__p = self.__players[self.__i].get_name()
            print("The Winner is", self.__p)


class Player:
    """Player class consists of player name,his score and has a function
    for playing the game taking game object as a parameter.
    The identifiers of the class are :
    name : name of the player
    score : score of the player
    """
    def __init__(self, name):
        """Intilazing the name of player by his name and the score to 0"""
        self.__name = name
        self.__score = 0

    def set_name(self, name):
        """
        This function will takes name as input and assign it to class variable.
        """
        self.__name = name

    def get_name(self):
        """This function will return the name of player."""
        return self.__name

    def current_score(self):
        """This function will return current score of player."""
        return self.__score

    def reset_score(self):
        """This function will reset the player score."""
        self.__score = 0

    def play_round(self, game, j):
        """This function will call the round function in Game class by
            its object as a parameter."""
        self.__g = game
        self.__j = j
        self.__g.round(self.__name, self.__j)
        self.__score += self.__g.cargo

if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player("Ling"))
    room.add_player(Player("Chang"))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()
