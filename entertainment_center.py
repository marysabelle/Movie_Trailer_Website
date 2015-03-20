import fresh_tomatoes
import media

#The following 12 movies are some of my favorite ones.
#They come with: title, storyline, porter image and a link to its trailer from Youtube.

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

batlestar_galactica = media.Movie("Batlestar Galactica",
                                  "When an old enemy, the Cylons, resurfaces and obliterate the 12 colonies, the crew of the aged Galactica protects a small civilian fleet - the last of humanity - as they journey toward the fabled 13th colony of Earth.",
                                  "https://telestrekoza.com/link-gallery/uploads/cancelled/BSG/Posters/BSG-S2-Poster-01.jpg",
                                  "https://www.youtube.com/watch?v=q2x14ZhEc9k")

the_hunger_games = media.Movie("The Hunger Games",
                               "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games, a televised fight to the death in which two teenagers from each of the twelve Districts of Panem are chosen at random to compete.",
                               "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=SMGRhAEn6K0")

independance_day = media.Movie("Independance Day",
                               "The aliens are coming and their goal is to invade and destroy. Fighting superior technology, Man's best weapon is the will to survive.",
                               "http://imageserver.moviepilot.com/independence-day-indepence-day-2-set-for-2016-but-its-major-star-won-t-be-onboard.jpeg",
                               "https://www.youtube.com/watch?v=SBx5Jrs9eGc")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=hfpbZmQHkWw")

kill_bill = media.Movie("Kill Bill",
                        "The Bride wakens from a four-year coma. The child she carried in her womb is gone. Now she must wreak vengeance on the team of assassins who betrayed her - a team she was once part of.",
                        "http://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
                        "https://www.youtube.com/watch?v=-czwy-aVbbU")

a_knights_tale = media.Movie("A Night's Tale",
                             "After his master dies, a peasant squire, fueled by his desire for food and glory, creates a new identity for himself as a knight.",
                             "http://tesseraguild.com/wp-content/uploads/2015/01/A-Knights-Tale-2001-movie-poster.jpg",
                             "https://www.youtube.com/watch?v=ClNPiTjo808")

leon_the_professional = media.Movie("Leon The Professional",
                                    "Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a professional assassin, after her family is murdered. Léon and Mathilda form an unusual relationship, as she becomes his protégée and learns the assassin's trade.",
                                    "http://upload.wikimedia.org/wikipedia/en/0/03/Leon-poster.jpg",
                                    "https://www.youtube.com/watch?v=FAOzXGibKJc")

the_wedding_singer = media.Movie("The Wedding Singer",
                                  "Robbie, the singer and Julia, the waitress are both engaged to be married but to the wrong people. Fortune intervenes to help them discover each other.",
                                  "http://upload.wikimedia.org/wikipedia/en/8/84/The_Wedding_Singer_film_poster.jpg",
                                  "https://www.youtube.com/watch?v=PxIKKgIkLUw")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = media.Movie("School of Rock",
                             "When struggling musician Dewey Finn finds himself out of work, he takes over his roommate's job as an elementary school substitute teacher and turns class into a rock band.",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s every day at midnight.",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=5nOF93SzX6s")

movies = [avatar, batlestar_galactica, the_hunger_games, independance_day, the_matrix, kill_bill, a_knights_tale,
          leon_the_professional, the_wedding_singer, toy_story, school_of_rock, midnight_in_paris,]
fresh_tomatoes.open_movies_page(movies)
