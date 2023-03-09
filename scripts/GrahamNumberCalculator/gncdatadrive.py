# work in progress
from pathlib import Path
import pandas as pd
import math

input = Path("./scripts/GrahamNumberCalculator/Data/Input/DATA/gncDatafile.csv")
output = Path(
    "./scripts/GrahamNumberCalculator/Data/Input/DATA/gncoutputDatafile.csv")
data = pd.read_csv(filepath_or_buffer: input | ReadCsvBuffer[bytes], , ,)

multiplier = 22.5


def graham_number(row):
    eps = row['EPS']
    book_value = row['Book Value per Share']
    graham_number = round(
        math.sqrt(multiplier * eps * book_value), 2)
    return graham_number


data['Graham Number'] = data.apply(graham_number, axis=1)

print(data.head())
