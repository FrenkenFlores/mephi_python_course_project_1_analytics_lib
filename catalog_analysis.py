
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
                List[str]
            ]
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
                List[str]
            ]
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

    try:
        ages = [abs(current_year - movie["year"]) for movie in movies]
    except KeyError as e:
        raise KeyError("Can't find key \"year\"") from e
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


def decade_label(
    year: int
) -> Literal["новые", "недавние", "старые"]:
    """
    Returns the label that represents the movie age.

    Args:
        year(int): the movie year
    
    Returns:
        Literal: the age label
    """
    match year:
        case y if y > 2020:
            return "новые"
        case y if y > 2014:
            return "недавние"
        case y if y < 2015:
            return "старые"


def count_long_movies(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ],
    threshold: int = 120
) -> int:
    """
    Returns the number of movies with duration bigger then threshold.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        int: the number of filtered movies

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    count = 0
    try:
        for movie in movies:
            if movie["duration_min"] > threshold:
                count += 1
    except KeyError as e:
        raise KeyError("Key \"duration_min\" is not found") from e
    return count


def normalize_title(
    title: str
) -> str:
    """
    Reformat title into "Title Case" format.

    Args:
        title(str): the movie title
    
    Returns:
        str: the formated title
    """
    fomrated_words = []
    for word in title.split():
        fomrated_words.append(word[0].upper() + word[1:])
    return " ".join(fomrated_words)


def make_slug(
    title: str
) -> str:
    """
    Return a slug for the given title in format "some-value".

    Args:
        title(str): the movie title
    
    Returns:
        str: the created slug based on the title
    """
    return title.lower().replace(' ', '-')


def format_report_line(
    movie: Dict[
        str,
        Union[
            str,
            int,
            float,
            Dict[str, str],
            List[str]
        ]
    ]
) -> str:
    """
    Return movie report.

    Args:
        movie(Dict): list of catalog movie objects

    Returns:
        str: formated report

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    try:
        report = (
            f'"{movie["title"]}" ({movie["year"]}) — '
            f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
            f'жанры: {', '.join(sorted(movie["genres"]))}'
        )
    except KeyError as e:
        raise KeyError(
            "Could not find needed keys:"
            "\"title\", \"year\", \"rating\", \"duration_min\", \"genres\""
        ) from e
    return report


def titles_sorted_by_rating(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ]
) -> List[str]:
    """
    Returns the titles for movies catalog that is sorted by rating.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        List[str]: list of titles

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    try:
        titles = [
            movie["title"] for movie in sorted(movies, key=lambda x: x["rating"])
        ]
    except KeyError as e:
        raise KeyError("Couldn't find keys: \"title\", \"rating\"") from e
    return titles


def top_n_by_rating(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ],
    n: int = 3
) -> List[tuple[str, str]]:
    """
    Returns a list of top n titles and ratings for movies catalog.

    Args:
        movies(List[Dict]): list of catalog movie objects
        n(int): number of elements

    Returns:
        List[tuple(str, str)]: list of titles and ratings

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    try:
        titles = [
            (
                movie["title"],
                movie["rating"]
            )
            for movie in sorted(movies, key=lambda x: x["rating"], reverse=True)
        ][:n]
    except KeyError as e:
        raise KeyError("Couldn't find keys: \"title\", \"rating\"") from e
    return titles


def count_by_genre(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ]
) -> Dict[str, int]:
    """
    Returns a counter dict that counts how many movies in each genre.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        Dict[str, int]: dict with the number of movies in every genre

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    count_dict = {}
    for movie in movies:
        try:
            for genre in movie["genres"]:
                count_dict[genre] = count_dict.get(genre, 0) + 1
        except KeyError as e:
            raise KeyError("Couldn't find key: \"genres\"") from e
    return count_dict


def actor_filmography(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ]
) -> Dict[str, List[str]]:
    """
    Returns a dict with the actors and there movies.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        Dict[str, List[str]]: dict with the actors and movies

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    actors_movies = {}
    for movie in movies:
        try:
            for actor in movie["actors"]:
                actors_movies[actor] = actors_movies.get(actor, []) + [movie["title"]]
        except KeyError as e:
            raise KeyError("Couldn't find keys: \"actors\", \"title\"") from e
    return actors_movies


def all_genres(
    movies: List[
        Dict[
            str,
            Union[
                str,
                int,
                float,
                Dict[str, str],
                List[str]
            ]
        ]
    ]
) -> set[str]:
    """
    Returns a set with all genres.

    Args:
        movies(List[Dict]): list of catalog movie objects

    Returns:
        set[str]: a set with all genres

    Raises:
        KeyError: if the movie dict object has invalid format
    """
    genres_set = set()
    for movie in movies:
        try:
            for genre in movie["genres"]:
                genres_set.add(genre)
        except KeyError as e:
            raise KeyError("Couldn't find key: \"genres\"") from e
    return genres_set


def main():
    print(average_rating(movies=MOVIES))
    print(catalog_age_stats(movies=MOVIES))
    print(duration_in_hours(5))
    print(rating_tier(7))
    print(decade_label(2023))

    for movie in MOVIES:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    i = len(MOVIES) - 1
    while i > 0:
        if MOVIES[i]["rating"] > 9.0:
            print(MOVIES[i]["title"])
            break
        i -= 1
    else:
        print("Шедевров не найдено")
    print(count_long_movies(MOVIES))
    print(normalize_title(MOVIES[2]["title"]))
    print(make_slug(MOVIES[0]["title"]))
    print(format_report_line(MOVIES[0]))
    print(titles_sorted_by_rating(MOVIES))
    print(top_n_by_rating(MOVIES))
    print(count_by_genre(MOVIES))
    print(actor_filmography(MOVIES))

    d = {
        movie["title"]: movie["rating"]
        for movie in MOVIES
        if movie["rating"] > average_rating(movies=MOVIES)
    }
    print(d)
    print(all_genres(MOVIES))


if __name__ == "__main__":
    main()
