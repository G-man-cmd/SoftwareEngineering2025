import psycopg2
import sys

import time
import hashlib

def generate_unique_id(input_string):
    current_time = str(time.time_ns())
    unique_data = input_string + current_time
    hash_value = hashlib.sha256(unique_data.encode()).hexdigest()
    return int(hash_value[:6], 16)

# Example usage:
unique_id = generate_unique_id("example_string")
print(unique_id)


class Database:

    def __init__(self,dbname='photon',user='student',passwd=None,host='localhost',port=5432):
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
            self.execute_query("truncate current_game;")



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
            player_id = generate_unique_id(name)

            self.execute_query(f"INSERT INTO public.players (id,codename) values ({player_id},'{name}');")
            self.execute_query(f"INSERT INTO public.current_game (player_id,hardware_id,team_name,score) values ({player_id},{h_id},'R',0);")
            
        for key in green_team.keys():
            name = green_team[key][0]
            h_id = green_team[key][1]
            player_id = generate_unique_id(name)

            self.execute_query(f"INSERT INTO public.players (id,codename) values ({player_id},'{name}');")
            self.execute_query(f"INSERT INTO public.current_game (player_id,hardware_id,team_name,score) values ({player_id},{h_id},'G',0);")

    def fetch_results(self):
        try:
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error fetching results: {e}")
            return None
