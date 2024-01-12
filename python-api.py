# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

import requests


# def get_movies_from_omdb(name):
#     base_url = "http://www.omdbapi.com/?i=tt3896198&apikey=2aea5ad1"
#     params = {"t": name, "r": "json"}
#     response = requests.get(base_url, params=params)
#     print(response.json())
#     print("test")
#     return response.json()


# def extract_movie_titles(response_dict):
#     movie_title_list = []
#     similar_dict_results_list = response_dict["Similar"]["Results"]
#     for results_dict in similar_dict_results_list:
#         movie_title_list.append(results_dict["Name"])
#     return movie_title_list


# def get_related_titles(movie_title_list):
#     extended_movie_title_list = []
#     for movie_title in movie_title_list:
#         step_one = get_movies_from_omdb(movie_title)
#         step_two = extract_movie_titles(step_one)
#         for a_movie_title in step_two:
#             if a_movie_title not in extended_movie_title_list:
#                 extended_movie_title_list.append(a_movie_title)
#     return extended_movie_title_list


def get_movie_data(name):
    search_dict = {
        "t": name,
        "r": "json"}
    base_url = "http://www.omdbapi.com/?i=tt3896198&apikey=2aea5ad1"
    response = requests.get(base_url, params=search_dict)
    return response.json()


def get_movie_rating(ombd_dict):
    final_rating = 0
    ratings_list = ombd_dict["Ratings"]
    for rating in ratings_list:
        if rating["Source"] == "Rotten Tomatoes":
            r_t_rating = rating["Value"]
            final_rating = int(str(r_t_rating)[:-1])
    return final_rating


def get_sorted_recommendations(movie_titles_list):
    # recommended_movies = get_related_titles(movie_titles_list)
    movies_with_ratings = []

    # for movie in recommended_movies:
    for movie in movie_titles_list:
        movie_data = get_movie_data(movie)
        movie_rating = get_movie_rating(movie_data)
        print(movie + " | Rating: " + str(movie_rating))
        movies_with_ratings.append((movie, movie_rating))


    sorted_movies = sorted(movies_with_ratings, key=lambda x: (x[1], x[0]), reverse=True)
   # print(sorted_movies)
    sorted_movie_titles = [movie[0] for movie in sorted_movies]
    return sorted_movie_titles


get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
