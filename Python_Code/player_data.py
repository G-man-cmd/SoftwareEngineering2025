class Player:
    row: int
    gunID: int
    playerID: int
    Nickname: str
    score: int
    baseBonus: bool
    Team:str

    def __init__(self, row: int, gunID: int, playerID: int, Nickname: str, team:str) -> None:
        self.row = row
        self.gunID = gunID
        self.Team = team
        self.playerID = playerID
        self.Nickname = Nickname
        self.score = 0
        self.baseBonus = False

    def stringify(self) ->str:
        return (f"Nickname: {self.Nickname}\n"
                f"Team: {self.team}\n"
                f"Gun ID: {self.gunID}\n"
                f"ID: {self.playerID}"
                f"Score: {self.score}\n"
                f"Base Bonus: {self.baseBonus}\n\n"
                )