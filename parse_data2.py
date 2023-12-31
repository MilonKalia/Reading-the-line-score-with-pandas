import os
import pandas as pd
from bs4 import BeautifulSoup

SCORE_DIR = "data/scores"

box_scores = os.listdir(SCORE_DIR)
box_scores = [os.path.join(SCORE_DIR, f) for f in box_scores if f.endswith(".html")]

def parse_html(box_score):
    with open(box_score) as f:
        html = f.read()
    soup = BeautifulSoup(html)
    [s.decompose() for s in soup.select("tr.over_header")]
    [s.decompose for s in soup.select("tr.thread")]
    return soup

def read_line_score(soup):
    line_score = pd.read_html(str(soup), attrs={"id": "line_score"})[0]
    cols = list(line_score.columns)
    cols[0] = "team"
    cols[-1] = "total"
    line_score.columns = cols
    line_score = line_score[["team", "total"]]
    return line_score

box_score =box_scores[0]
soup = parse_html(box_score)
line_score = read_line_score(soup)
teams = list(line_score["team"])
print(line_score)
