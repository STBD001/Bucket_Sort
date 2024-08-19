import csv
import time
import numpy as np

# Klasa przechowująca dane ocen
class RatingData:
    def __init__(self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

MAX_RANKINGS = 10000000
BUCKET_RANGE = 11

# Funkcja usuwająca puste wpisy w polu ranking
def remove_empty_ratings(arr):
    return [rating for rating in arr if rating.rating > 0]

# Funkcja sortująca kubełkowo
def bucket_sort(arr):
    bucket = [0] * BUCKET_RANGE
    for rating in arr:
        bucket[int(rating.rating)] += 1
    idx = 0
    for i in range(BUCKET_RANGE):
        for _ in range(bucket[i]):
            arr[idx].rating = i
            idx += 1

def main():
    # Wczytanie danych z pliku
    filename = 'C:\\Users\\Dell\\Downloads\\Dane.csv'
    ratings = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Pomijanie nagłówka
        for row in csvreader:
            if len(ratings) >= MAX_RANKINGS:
                break
            id = int(row[0])
            title = row[1]
            rating = float(row[2])
            if rating <= 10.0:
                ratings.append(RatingData(id, title, rating))

    ratings = remove_empty_ratings(ratings)

    # Sortowanie i mierzenie czasu dla różnych ilości danych
    for num in [10000, 100000, 500000, 1000000, len(ratings)]:
        start_time = time.time()
        bucket_sort(ratings[:num])
        end_time = time.time()
        elapsed_ms = (end_time - start_time) * 1e6
        print(f"Czas sortowania dla {num} elementów: {elapsed_ms:.2f} mikrosekundy")

if __name__ == "__main__":
    main()
