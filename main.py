from drawer import drawer
from drawer import WINDOW_SIZE
import csv
import numpy as np

with open('data.csv') as f:
    r = csv.reader(f)
    data = [e for e in r]
datas = np.array(data).reshape(-1)
datas = [int(data) for data in datas]

config = {
    "datas": datas,
    "lines": [
        [(0, 0), (WINDOW_SIZE, 0)],
        [(0, 0), (0, WINDOW_SIZE)],
    ]
}

drawer(config)
