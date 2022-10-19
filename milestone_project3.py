user_input="Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit:"
movie=[]


def list_movies():

    print(movie)

def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movie.append({
        'title': title,
        'director': director,
        'year': year
    })



def find_movie():
    title = input("Enter movie title you're looking for: ")

    for i in movie:
        if i["title"] == title:
            movie(i)

    
   
    

def menu():
    name=input(user_input)


    while name!='q':
        if name=='l':
            list_movies()
        elif name=='a':
            add_movies()

        elif name=='f':
            find_movie()

        name=input(user_input)

menu()

        