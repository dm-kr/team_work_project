import random

class RockPaperScissors:
    ACTIONS = ("rock", "paper", "scissors")

    def __init__(self, points_to_win: int):
        self.goal = points_to_win
        self.player_points = 0
        self.bot_points = 0
    
    def make_a_turn(self, action: str):
        if action not in self.ACTIONS:
            return "Unknown action"
        
        bot_action = random.choice(self.ACTIONS)
        message = "Draw"
        if action == self.what_beats(bot_action):
            self.bot_points += 1
            message = f"Bot wins with {bot_action}"
            if self.bot_points == self.goal:
                message += f"\nBot have won the game {self.player_points}:{self.bot_points}"
        elif bot_action == self.what_beats(action):
            self.player_points += 1
            message = f"Player wins, bot choose {bot_action}"
            if self.player_points == self.goal:
                message += f"\nPlayer have won the game {self.player_points}:{self.bot_points}"
        
        return message


    def what_beats(self, action: str):
        match action:
            case "rock":
                return "scissors"
            case "paper":
                return "rock"
            case "scissors":
                return "paper"