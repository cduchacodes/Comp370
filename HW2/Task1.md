# Task 1
### Question Definition
The first part of the data science process is defining the question. In         
the last homework, we were tasked with looking at the frequency with 
which troll tweets mention “Trump” by name. While we never actually 
defined a question, a possible question that we would have answered 
is: "what is the percentage of tweets that mention Trump by name?"


### Data Collection
The actual collection of the data was already done, but we had to
download the csv file, in order to do some actions to it. From there,
modifying the data so that it can be worked it also falls under the
umbrella of data collection. We did a lot to the data to make it 
workable including
* Keeping only the first 10,000 tweets
* Keeping only tweets in English
* Removing the tweets with a "?" character
* Keeping only the `tweet_id, publish_date, content` columns


### Data Annotation
The data annotation phase is about making features that will be used for 
later in the data analysis phase. Creating the `trump_mention` column 
goes into this phase because we added a new feature (the trump_mention 
column) and used it in the next phase.

### Data Analysis
This phase is about using the features from before to get numbers that 
help answer the question we asked at the beginning. In this case doing 
the computation of the % of tweets that mnetion Trump was data analysis. 
We used the trump_mention column from before to help us figure out how 
many tweets mentioned Trump. In the end we found that 2.2% of tweets 
mention Trump, which can help us talk about the frequency that troll 
tweets mention Trump by name