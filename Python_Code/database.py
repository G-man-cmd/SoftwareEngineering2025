import psycopg2
import sys

class Database:

    def __init__(self,dbname,user,passwd,host,port=5432):
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.passwd,
                host=self.host,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database.")

            print("Creating auxilary tables.")

            self.execute_query('''CREATE TABLE IF NOT EXISTS public.current_game (
                                player_id INTEGER PRIMARY KEY,
                                hardware_id INTEGER UNIQUE NOT NULL,
                                team_name VARCHAR(1) CHECK (team_name IN ('G', 'R')) NOT NULL,
                                score INTEGER DEFAULT 0,
                                CONSTRAINT fk_player FOREIGN KEY (player_id) REFERENCES public.players(id) ON DELETE CASCADE
                                );
                            ''')

            self.execute_query('''CREATE TABLE IF NOT EXISTS public.high_score (
                                    player_id INTEGER PRIMARY KEY,
                                    codename VARCHAR(255) NOT NULL,
                                    score INTEGER DEFAULT 0,
                                    CONSTRAINT fk_player FOREIGN KEY (player_id) REFERENCES public.players(id) ON DELETE CASCADE
                                );
                                ''')



        except Exception as error:
            print(f"Error connecting to PostgreSQL database: {error}")
            print("\n Quitting! \n")
            sys.exit()

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
    
    def load_players(self,red_team,green_team):
        for key in red_team.keys():
            name = red_team[key][0]
            h_id = red_team[key][1]
            self.cursor.execute(f"", params)

    def fetch_results(self):
        try:
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error fetching results: {e}")
            return None