# Project Write Up

### Summary
  I chose to use Hip Hop/Rap song lyrics to create a song recommendation engine. To do this I had to webscrape and use Genius.com's API to get my lyrics. Because I wanted a very large dataset, this took up much of the time on the project. One of the best parts of this process was getting my web scraper to work on multiple threads. Initially I was looking at a runtime of 60-70 hours to get all the data that I wanted (~3 seconds per song, 115K songs), but was able to cut this down to ~ 5 or 6 hours. Coming into this I completely underestimated the amount of time I was looking at. After getting all the lyrics that I wanted, I began to look at how I could compare these lyrics. Clearly, some vector representation of the lyrics was needed. Initially, I was planning on just extracting features from the lyrics (lexical diversity, syllable variance, syllables per second, etc.) and using those to compute similarities. I did end up using these features, but I also created a doc2vec vector representation of each lyric document. Now that I have two seperate vectors for each song, I compute similarity scores for both sets and combine these into one final similarity score. I had a ton of fun working on this project and it something that I want to keep improving. 
  
  
### Introduction
  I chose to do this for a few reasons. First, I love rap. Second, I have always been interested in song recommendation algorithms. Third, I could always use songs to add to my playlists! The dataset is unique because of how large it is, and also that it requires a decent amount of effort to get. Genius.com, the website that stores all the lyrics I used, actually has an API. However, you can not actually use it to get lyrics of songs, which is the whole point of their website. In a roundabout way, you have to use their API to get artist IDs, then song IDs, and then scrape the URLs associated with each ID. There doesn't seem to be another place on the internet to get a large amount of lyrics like this that is easier.
  
### Data
  The data is simply just text files full of song lyrics. I do not tokenize and clean the data much when we are writing to files. I want to keep the structure of the lyrics (like rap 'lines') for feature extraction. The full dataset contains ~115,000 songs from ~1,100 different artists. While there are ~115,000 song files, not all of these are actually songs. Genius has records of interviews, skits, etc. that get mixed in with songs. Steps are taken to remove as much of these as possible but there definitely are some still in there. 
  
### Methods
  To obtain data I used APIs and web scraping. I used pretty basic tokenization and normalization techniques when preparing data for feature extraction. To get document vector representations, doc2vec was used. Doc2vec is completely new to me, but it seems to have worked very well. I am looking forward to working with it more, and fine tuning some of the parameters for my specific use.
  
### Results
  It is difficult to quantify results for a project like this. However, there are definitely a few sanity checks that have been run that show that this model is working.
  
  - Recommendations for Who Shot Ya? by The Notorious B.I.G.  |  Try out 'Slap! Slap! Slap!' by Missy Elliott
  - Recommendations for Hard in da Paint by Waka Flocka Flame | Try out 'Faneto' by Chief Keef   *** This is pretty accurate, this is when I knew it wasn't half bad
  - Recommendations for Gucci Gang by Lil Pump | Try out 'Life Like Me' by Lil Pump
  - Recommendations for Gold Digger by Kanye West | Try out 'Money in the Bank' by Swizz Beatz
  - Recommendations for It Was a Good Day by Ice Cube | Try out 'Hype Shit' by Saafir
  
### Future Improvements

- Remove more of the non-songs, there are still some lurking in there
- Get artists that fell through the cracks (Tupac isn't on here)
- Tweak my doc2vec model parameters to get the best representation
- Create a web app for users to get recommendations






  
