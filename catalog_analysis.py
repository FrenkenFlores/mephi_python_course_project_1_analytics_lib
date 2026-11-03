
import math
from typing import List, Dict, Union, Literal

MOVIES = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"]
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]


def average_rating(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]]
            ]
        ]
) -> float:
    """
    Returns the average rating of movies catalog.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        float: the catalog average value

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    if not movies:
        return 0.0
    try:
        return round(
            sum([movie["rating"] for movie in movies]) / len(movies),
            1
        )
    except KeyError as e:
        raise KeyError("Can't find \"rating\" field in movie object") from e



def catalog_age_stats(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]]
            ]
        ],
    current_year: int = 2026
) -> tuple[int, int, int]:
    """
    Returns the age of the oldest, newest and the average age of movies in catalog
    in relation to the current year.

    Args:
        movies(List[Dict]): list of catalog movie objects
        current_year(int): the current year that will be used to calculate the age

    Returns:
        tuple: the oldest, newest and average age

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    if not movies:
        return (0, 0, 0)

    ages = [abs(current_year - movie["year"]) for movie in movies]
    min_age = min(ages)
    max_age = max(ages)
    avg_age = math.ceil(sum(ages)/len(ages))
    return (
        min_age,
        max_age,
        avg_age
    )



def duration_in_hours(
    minutes: int
) -> str:
    """
    Converts minuts into format: HHч MMм.

    Args:
        minutes(int): minutres in int format that will be converted into str

    Returns:
        str: the formated time

    Raises:
        ValueError: if negative minutes provided
    """
    if minutes < 0:
        raise ValueError("Minutes can't be negative")
    hours = minutes // 60
    minutes_left = minutes % 60
    return f"{hours}ч {minutes_left}м"


def rating_tier(
    rating: float
) -> Literal["шедевр", "хорошо", "средне", "слабо"]:
    """
    Return the rating label

    Args:
        rating(float): the movie rating

    Returns:
        Literal: the rating label
    """
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"



def main():
    print(average_rating(movies=MOVIES))
    print(catalog_age_stats(movies=MOVIES))
    print(duration_in_hours(5))
    print(rating_tier(7))


if __name__ == "__main__":
    main()
