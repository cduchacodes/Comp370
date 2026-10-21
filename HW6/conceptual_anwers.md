# What is Refactoring?
Refactoring is changing the code's structure. Refactoring doesn't 
change what the code does, but it does reorganize it to make it easier 
to read, test, and maintain. Three techniques of refactoring are:
### 1. Break code into functions
Taking a large block of code and turning it into a function can be 
helpful for making the code easier to understand. 
### 2. Turn repeated code into functions
Taking repeated code and turning it into a function helps avoid 
repetitive code. This helps make the code more readable and shortens the 
number of lines the code takes up. It also makes it easier to change 
the code by only having to update the shared function instead of every 
place the code is used.
### 3. Organize code into classes
Use classes to represent how information is stored and used. The way the
classes are created should map to how the data is stored in real life 
and how it is used.

# Why Does Code Go Through Phases of Messiness?
There are lots of reasons for "messiness" throughout a data science 
project. First, at the beginning of the project, it can be confusing on 
where to start, so you try some ideas to get a feel of what might or 
might not work. Then comes data collection which is extremely messy. 
Cleaning up the data takes a lot of time, but so does collecting the right
data in the right format. Then you have to run some sort of analysis 
which can be messy depending on the data you collected, and you might 
have to go back to cleaning up the data. Finally, the code you spent so 
much time writing works, but the code itself can also be messy. This is 
where refactoring comes in, where you clean up the structure of the 
code to make it more readable and easier to maintain.

# Techniques for Modular Code
### 1. 
Breaking large chunks of code into functions
### 2. 
Separating the code into different files based on their purpose. For 
example separating the data cleaning and the analysis.
### 3.
Have each part be responsible for a single task and have the 
interact through standard data types like a csv files. This way you can 
easily add a piece in or remove something without having to rewrite all 
the code.