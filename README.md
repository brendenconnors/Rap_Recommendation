# Rap Recommendation
## A lyric based hip hop recommendation engine

### Motivation
  With my Spotify often playing >50% of my day, often times I run out of new music. I have always been interested in how songs are being recommended for me, thinking about the features of my current song and seeing how that compares to what is played next. How is a set of songs being recommended for me based off of my playlist? What did I listen to recently that made my Discover Weekly this good/bad? 

  To build my own recommendation engine, I will be doing this only using song lyrics,and specifically Hip Hop/Rap lyrics. We will look to extract some simple features from the lyrics, as well as get a Doc2Vec vector representation that we can use to calculate similarity scores. I want to build my own recommendation engine for my own intense interest, to help fill my/my friends' playlists, and learn/use some NLP techniques along the way.
  
### Data
  The process of getting the data is obtained from the following steps.
  
  1. Get a record of as many hip hop artists we can using Wikipedia_artist_scraper.py.
  2. Use Genius.com's API to search by artist name, get their unique artist ID for Genius, and then get all the unique song IDs associated with that artist. Done with Genius_ID_Grabber.ipynb.
  3. Using the song IDs, scrape Genius.com for lyrics, and song durations (if available). Done using Multithreaded_Scraper.py
  4. Extract and store features from the lyrics. Done using Lyric_Features.ipynb
  5. Get and store a Doc2Vec vector representation of the lyrics using Doc2Vec_Representation.ipynb

### Recommendation
  Similarity scores are calculated amongst the Doc2Vec vectors and extracted feature vectors seperately. Doc2Vec similarity scores are computed using the cosine similarity between document vectors, and the euclidean distance is used to measure similarity in our feture vectors (dimensionality is small so curse of dimensionality is not relevant).These two similarity scores are combined into one final similarity score which fuels our recommendations. All functions to compute similarity, return recommendations, etc. are found in recommendation_engine.py. Look at the parameters if you want to tinker with how you recommendations are calculated and weighted.
  
  Recommendation_Final.ipynb is a notebook with some widgets that allows you to get recommendations pretty easily. When loading in a Doc2Vec model, choose from doc2vec_len20.model , doc2vec_len50,... These are Doc2Vec models trained to produce different length document vectors. These different lengths can sometimes result in very different recommendations. Try them all out and see which works best for you. Have some fun seeing what it thinks you may like, I hope you enjoy!
  
### Next Steps
  
  - Increase our set of song lyrics. Get artists that fell through the cracks. 
  - Include more genres.
  - Further cleaning. Scraping Genius results in some files that are not songs (interviews, snippets, poetry,...). Do a better job of removing all of these.
  - Create a simple web app for users to get recommendations.
