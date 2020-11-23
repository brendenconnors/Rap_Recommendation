## Feedback

Great work on this. This is **complete**. 

## Wiki Scrape

Not much to say here except, "wow, those wikipedia classification pages sure do 
make it easier to get all this data."

## Lyric Genius

Probably could have done without that giant print-to-screen, although it was cool
seeing all the artists. Here's a not bad [package](https://github.com/tqdm/tqdm) for 
progress bars, fwiw. Otherwise the code looks good. Very sensibly put together. 

## Scraper

I've never used the multi-threaded stuff in Python. It was cool to see 
what you needed to do to get `ProcessPoolExecutor`. As I'm sure you've noticed, 
I don't cover the creation of standalone .py files. (For instance, most people
in the class may not have seen `if  __name__ == '__main__':`, which is a feature
of app building. I'd be curious if you think that'd be good to add. My sense is that 
it'd confuse people as they learn, but I'd like to hear your thoughts. 

It'd be cool to implement this in a path-agnostic way, rather than having a line like
`C:\Users\conno\Documents\text_mining\repos\Lyric Scraper\Lyrics\\`. Do you need the double
slash since it's a raw string? I'd think not. 

And all of this is just to get the point where you can _start_ building a recommendation 
engine. Whew. Nice work to this point.

## Lyric Features

`syllapy` is cool. Thanks for showing me that. I could imagine just defining your `feature_dict` 
with `return({'duration':duration,'number_lines':number_lines, ...)`, but obviously that may be
less readable. Code looks good and sensible. I like how you've organized the whole project. 

## Doc 2 Vec

I could have probably lived with `pd.set_option('display.max_rows', 100)`. I'm impressed with 
how (relatively) easy it is to make this cell: 
```
max_epochs = 100
vec_size = 50
alpha = 0.025
model = Doc2Vec(vector_size=vec_size, alpha=alpha, min_alpha=0.00025, min_count=10, dm =1)
```
Your code is remarkably clear and easy to read. 

## Recommendation Engine

Smart to have that `std_drop` parameter. I'm guessing that was developed with some hard-won experience. 
Never seen `@` used instead of `matmul`. That's cool. I'm no numpy superstar, though. If you were 
moving this into production it might make sense to do some "culling" of the potential songs (particularly
if you were at Spotify and had millions of songs). It seems like this makes a pretty big matrix, but maybe
it's still performant. 

## Overall

Great work! I learned a lot. 


