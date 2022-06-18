import sqlite3 as sql
import datetime

class Highscores:
    """This class will CRUD data from highscores DB."""

    def __init__(self) -> None:
        """
            Connect and create DB.
        """
        self.db_name = "./Database/highscores.db"
        self.tb_name = "highscores"
        self.con = sql.connect(self.db_name)
        self.cur = self.con.cursor()

        self.create()

    
    def create(self) -> None:
        """
            Create highscore table if not
            exists.
        """
        script = f"""
            CREATE TABLE IF NOT EXISTS {self.tb_name} (
                nickname VARCHAR NOT NULL,
                score INTEGER NOT NULL,
                date VARCHAR
            );
        """

        self.cur.execute(script)


    def save(self, score, nickname) -> None:
        """
            Save a new highscore.
        """
        date = datetime.date.today().strftime("%d-%m-%Y")
        script = f"INSERT INTO {self.tb_name}(nickname, score, date) VALUES('{nickname}', {score}, '{date}');"
        
        self.cur.execute(script)
        self.con.commit()

        
    def get(self) -> list:
        """
            Get the 5 best highscores.
        """
        script = f"SELECT * FROM {self.tb_name} ORDER BY score DESC LIMIT 5;"

        scores = self.cur.execute(script).fetchall()

        return scores