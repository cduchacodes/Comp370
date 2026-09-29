# 1. 
The dataset is 4870970 bytes, or 4.7 MB. It has 36859 (36860-1) entries plus the header.

# 2. 
The data set has four fields: title, writer, pony, and dialog.
There are many unique values within each column, way too many to list all the values that are in them,
however all the values are strings. The headers accuractely describe what the values of each column 
represent.

# 3.
Through the use of `csvtool col 1 clean_dialog.csv | sort | uniq | wc -l`, we can see that there are 
198 unique lines in the Title column, which we can take to mean the dataset covers 198 episodes.

# 4.
Some speakers have typos, where their names aren't spelled exactly the same in different rows.
For example A. K. Yearling is also sometimes spelled A.K. Yearling. This means the same speaker
could actually be counted as two unique speakers.
