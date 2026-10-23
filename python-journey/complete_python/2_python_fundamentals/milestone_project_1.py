# Project Briefing

# As a user, I should be able to:
# 1. Add new movies to my collection. > So I can keep track of all my movies.
# 2. List all the movies in my collection. > So, I can see what movies I have.
# 3. Find a movie by using a movie title. > To locate movies easily when the collection grows.
# 4. See a menu with options to pick from.

# Implementation:
# 1. Decide where to store movies in code.
# 2. Decide what data we want to store for each movie.
# 3. Each process/requirement should have it's own function.
# 4. User should be able to terminate the program on typing 'q'.

# -------------------------------------------------------
# -------------------------------------------------------

# Thoughts
# - we start with defining first the database: we do not need one as of now, since it has not been covered in the course.
# - next up: what all data do we need for each movie: we need the name, year it was released in, user rating out of 5, genre and director.

# - lets start by setting up the program flow
#     - user starts the program
#     - user gets a menu
#     - user selects add a movie
#         - this is a list of dicts, every movie gets it's own dict
#         - add new movie, gets a function
#         - user gets option to enter name, year in numbers > non number is not accepted, user rating, out of 5, within 1 and 5, anything else is not accepted, then genre, out of given list, and finally name of director, where we can have only alphabets and nothing else.
#     - user selects show movie list, we present the movie list in a well formatted output > gets it's own function
#     - user selects search a movie > user gets option to enter movie name > we search for it by matching the name > lower with lower > if found we present the details, if not found, we mention, movie not found > gets its own function
#     - finally, user enters q, we exit the program with a message > this is made by using while loop, the functions are defined outside, but executed inside this loop


# setup adding a movie
movie_list = []


def add_movie_name():
    print("Step 1 of 5")
    movie_name = input("Enter movie name: ")
    return movie_name.lower().strip()


def add_director_name():
    print("Step 2 of 5")
    director_name = input("Enter movie's director(s) name: ")
    return director_name.lower().strip()


def add_genre():
    genre_list = ["action", "comedy", "drama", "horror"]
    print("Step 3 of 5")
    print("Genre list:")
    for index, genre in enumerate(genre_list):
        print(f"{index+1}. {genre.title()}")
    user_genre = input("Type one from the above list and press enter: ")
    while user_genre.lower().strip() not in genre_list:
        print("****Invalid format.****")
        print("Genre list:")
        for index, genre in enumerate(genre_list):
            print(f"{index+1}. {genre.title()}")
        user_genre = input("Type one from the above list and press enter: ")
    return user_genre.lower().strip()


def add_release():
    while True:
        print("Step 4 of 5")
        release_year = input("Please enter movie release year.\nIt must be a number including or between 1900 and 2026: ").strip()
        if not release_year.isnumeric():
            print("Invalid format. Please try again.")
            continue

        if 1900 <= int(release_year) <= 2026:
            return release_year.strip()
        else:
            print("Invalid year. Please try again.")


def add_rating():
    print("Step 5 of 5")
    movie_rating = input("Please rate movie out of 5.\nIt must be a number including or between 1 and 5: ").strip()
    while movie_rating not in ["1", "2", "3", "4", "5"]:
        print("Invalid Input. Please try again.")
        movie_rating = input("Please rate movie out of 5.\nIt must be a number including or between 1 and 5: ").strip()
    return movie_rating.strip()


def add_movie():
    movie_dict = {}
    movie_dict['name'] = add_movie_name()
    movie_dict['director'] = add_director_name()
    movie_dict['genre'] = add_genre()
    movie_dict["release_year"] = add_release()
    movie_dict["rating"] = add_rating()

    movie_list.append(movie_dict)

    print("Movie added successfully.")



def search_movie():
    if not movie_list:
        print("No movies in the list. Add some movies to search.")
    else:
        movie_to_search = input("Please enter the name of the movie you want to search: ")
        for movie in movie_list:
            if movie['name'] == movie_to_search.lower().strip():
                print(f"Name: {movie['name'].title()} | Directed By: {movie['director'].title()} | Genre: {movie['genre'].title()} | Released in: {movie['release_year']} | Your Rating: {movie['rating']}")
                break
        else:
            print("This movie is not present in the list.")




def show_list():
    if not movie_list:
        print("No movies in the list. Add some movies to view the list.")
    else:
        for index, movie in enumerate(movie_list):
            print(f"{index+1}. | Name: {movie['name'].title()} | Directed By: {movie['director'].title()} | Genre: {movie['genre'].title()} | Released in: {movie['release_year']} | Your Rating: {movie['rating']}")


user_options = {
    "1": add_movie,
    "2": show_list,
    "3": search_movie
}

def program():
    user_response = ''
    while user_response.lower() != 'q':
        print("Please select any of the following options to move ahead:")
        print("Enter adjacent number and press enter to proceed.")
        print("Add a Movie - 1\nView Movie List - 2\nSearch a movie - 3")
        print("Or enter 'q' to exit the program!")
        user_response = input("Enter response: ")
        if user_response.lower() in user_options:
            selected_run = user_options[user_response]
            selected_run()
        elif user_response.lower() == 'q':
            print("Program Exited Successfully.")
            break
        else:
            print("Invalid response. Try again!")


program()