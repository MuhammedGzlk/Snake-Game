import json
import os

class HighScoreManager:
    def __init__(self, file_path='high_score.json'):
        self.file_path = file_path
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def get_high_score(self, username):
        return self.scores.get(username, 0)

    def update_score(self, username, score):
        if self.get_high_score(username) < score:
            self.scores[username] = score
            with open(self.file_path, 'w') as f:
                json.dump(self.scores, f, indent=4)