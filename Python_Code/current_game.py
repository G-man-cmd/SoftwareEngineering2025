class Player:
    def __init__(self, player_id, player_name, hardware_id, team_name, score=0):
        if team_name not in ('G', 'R'):
            raise ValueError("team_name must be 'G' (Green) or 'R' (Red)")
        self.player_id = player_id
        self.player_name = player_name
        self.hardware_id = hardware_id
        self.team_name = team_name
        self.score = score
    
    def info(self):
        print(self.player_id,
        self.player_name,
        self.hardware_id,
        self.team_name,
        self.score)

    def update_score(self, points: int):
        self.score += points


class CurrentGame:
    def __init__(self):
        self.teams = {'G': [], 'R': []}

    def add_player(self, player: Player):
        self.teams[player.team_name].append(player)

    def get_team(self, team_name: str):
        if team_name not in self.teams:
            raise ValueError("Invalid team name. Use 'G' or 'R'.")
        return self.teams[team_name]

    def get_scores(self):
        return {
            "G": {p.player_id: p.score for p in self.teams['G']},
            "R": {p.player_id: p.score for p in self.teams['R']}
        }

    def total_team_score(self, team_name: str):
        return sum(player.score for player in self.teams.get(team_name, []))

    def get_player_by_hardware_id(self, hardware_id):
        for team in self.teams.values():
            for player in team:
                if player.hardware_id == hardware_id:
                    return player  
        return None  

    def display_game_state(self):
        print("Current Game State:")
        for team, players in self.teams.items():
            print(f"Team {team}:")
            for player in players:
                print(f"  Player ID: {player.player_id}, Name: {player.player_name}, Score: {player.score}, Hardware ID: {player.hardware_id}")
    
    def reset_game(self):
        self.teams = {'G': [], 'R': []}
