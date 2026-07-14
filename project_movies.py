def save_reviews(movies, ratings):
    "Saves reviews to a text file"
    try:
        with open('movie_reviews.txt', 'w') as file:
            file.write('=== Movie Rating System ===\n')
            
            for movie, rating in zip(movies, ratings):
                file.write(f"Movie: {movie}\n")
                file.write(f"Rating: {rating:.1f}\n")

            if rating > 8:
                classification = "Excellent"
            elif rating >= 7:
                classification = "Very Good"
            elif rating >= 5:
                classification = "Regular"
            else:
                classification = "Bad"

            file.write(f"Classification: {classification}\n")
            file.write("-" * 40 + "\n\n")
            
            # Statistics
            if len(ratings) > 0:
                average_rating = sum(ratings) / len(ratings)
                file.write(f'\n=== Statistics ===\n')
                file.write(f'Total movies reviewed: {len(movies)}\n')
                file.write(f'Average rating: {average_rating:.2f}\n')
                file.write(f'Highest rating: {max(ratings):.1f}\n')
                file.write(f'Lowest rating: {min(ratings):.1f}\n')
        
        print('Reviews successfully saved to "movie_reviews.txt".')
    except Exception as e:
        print(f'Error saving reviews: {e}')


def main():
    """Main function of movie evaluator"""
    print('=== Movie Rating System ===\n')
    
    movies = []
    ratings = []
    
    evaluate_again = 'y'
    
    while evaluate_again == 'y':
        name_movie = input('What is the name of this movie? ')
        
        # Validate the rating
        while True:
            try:
                ratings_movie = float(input('From 0 to 10, what rating do you give this movie?: '))
                
                if ratings_movie < 0 or ratings_movie > 10:
                    print('Invalid note! Enter a note between 0 and 10.')
                    continue
                
                break  # valid note, leave from loop
            except ValueError:
                print('Invalid note! Enter only numbers.')
        
        # Add the movie and its rating to the lists
        movies.append(name_movie)
        ratings.append(ratings_movie)
        
        # Classify the movie
        if ratings_movie > 8:
            print(f'The movie "{name_movie}" was classified as Excellent!')
        elif ratings_movie >= 7:
            print(f'The movie "{name_movie}" was classified as Very Good.')
        elif ratings_movie >= 5:
            print(f'The movie "{name_movie}" was classified as Regular.')
        else:
            print(f'The movie "{name_movie}" was classified as Bad.')
        
        print()
        evaluate_again = input('Do you want to rate another movie? (y/n): ').lower()
        print()
    
    # Show statistics
    if len(ratings) > 0:
        average_rating = sum(ratings) / len(ratings)
        print('\n=== Movie Review Summary ===')
        print(f'Movies reviewed: {", ".join(movies)}')
        print(f'Registered ratings: {[f"{ratings:.1f}" for ratings in ratings]}')
        print(f'Average rating: {average_rating:.2f}')
        print(f'Total movies reviewed: {len(movies)}')
        
        # Ask if the user wants to save the reviews
        print()
        save = input('Do you want to save the reviews in txt file? (y/n): ').lower()
        if save == 'y':
            save_reviews(movies, ratings)
    else:
        print('No movies were reviewed.')

    print('\nThanks for using the Movie Rating System!')
if __name__ == "__main__":
    main()
"""Main function of movie evaluator"""
