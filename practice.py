# Variables
"""
Write a separate program to accomplish each problem.
-- STRINGS -- 
1. Simple Message: Store a message in a variable, and then print that message
2. Simple Messages: Store a message in a variable, and print that message. Then change the value of your variable
   to a new message and print the new message.
3. Personal Message: Store a person's name in a variable, and print a message to that person. Your message should
   be simple, such as, "Hello Eric, would you like to learn Python today?"
4. Name Cases: Store a person's name in a variable, and then print that person's name in lowercase, uppercase, and titlecase
5. Famous Quote: Find a quote from a famous person you admore. Print the quote and the name of its author. Your output should
   look similar to something like: Albert Einstein once said, "A person who never made a mistake never tried anything new".
6. Famous Quote 2: Repeat #5, but this time store the famous person's name in a variable called famous_person. Then compose
   your message and store it in a new variable called message. Print your message.
7. Stripping Names: Store a person's name, and include some whitespace characters at the beginning and end of the name.
   Print the name once, so the whitespace around the name is displayed, then print using each of the three stripping 
   methods, lstrip(), rstrip(), and strip(). If you don't know what they do, test it!
-- NUMBERS --
8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure
   to enclose your operations in print statements to see the results. You should create four lines that look like this:
       print(5 + 3)
9. Favorite Number: Store your favorite number in a variable. Then, using that variable, create a message that reveals your 
   favorite number. Print that message.
"""

# Lists
"""
To practice using VSCode, try creating a new folder and a file inside that folder to answer these problems
1. Names: Store the names of a few of your friends in a list called names. Print each person's name by
   accessing each element in the list, one at a time.
2. Greetings: Start with the list you used in #1, but instead of just printing each person's name, print
   a message to them. The text of each message should be the same, but each message should be personalized
   with the person's name. Challenge: Use a for loop to do this
3. Your Own List: Think of your favorite mode of transportation, and make a list that stores several examples.
   Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."
4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at
   least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
   You'll have to think of someone else to invite.
    * Start with your program from #4. Add a print statement at the end of your program stating the name of the guest who can't
      make it.
    * Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
    * Print a second set of invitation messages, one for each person who is still in your list
6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guest to invite to dinner.
    * Start with your program from #4 or #5. Add a print statement to the end of your program informing people that you found a bigger
      dinner table.
    * Use insert() to add one new guest to the beginning of your list.
    * Use insert() to add one new guest to the middle of your list.
    * Use append() to add one new guest to the end of your list.
    * Print a new set of invitation messages, one for each person in your list.
7. Shrinking Guest List: You just found out that your new dineer table won't arrive in time for dinner, and y ou have space for only two guests.
    * Start with your program from #3. Add a new line that prints a message saying that you can invite only two people for dinner.
    * Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
      print a message to that person letting them know you're sorry you can't invite them to dinner
    * Print a message to each of the two people still on your list, letting them know they're still invited
8. Seeing the World: Think of at least five places in the world you'd like to visit>
    * Store the locations in a list. Make sure the list is not in alphabetical order.
    * Print your list in its original order. Don't worry about print the list neatly, just print it as a raw Python list
    * Use sorted() to print your list in alphabetical order without modifying the actual list
    * Show that your list is still in its original order by printing it again
    * Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
    * Show that your list is still in its original order by printing it again.
    * Use reverse() to change the order of your list. Print the list to show it's back to its original order
    * Use reverse() to change the order of your list again. Print the list to show it's back to its original order.
    * Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed
    * Use sort() to change your list so it's stored in reverse alphabetical rder. Print the list to show that its order has changed
9. Dinner Guests: Working with one of the programs from #4 - #7, use len() to print a message indicating the number of people
   you are inviting to dinner.
10. Every Function: Think of something you could store in a list. Write a program that creates a list containing these items and then
    use each function you know of at least once. 
"""

# Working With Lists
"""
1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of 
   each pizza.
    * Modify your for loop to print a sentence using the name of the pizza isntead of printing just the name of the pizza. For each pizza
      you should have one line of output containing a simple statement like: I like pepperoni pizza.
    * Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more
      lines about the kinds of pizza you like and then an additional sentence, such as: I really love pizza!
2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then
   use a for loop to print out the name of each animal.
    * Modify your program to print a statement about each animal, such as: A dog would make a great pet.
    * Add on a line at the end of your program stating what these animals have in common. You could print a sentence such as: Any of these animals would 
      make a great pet!
-- FOR LOOPS --
3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one
   and ends at one million. Also, use sum() function to see how quickly Python can add a million numbers
6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number
7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list
8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first
   10 cubes (that is, the cube of each integer from 1 to 10) and use a for loop to print out the value of each cube.
9. Cube Comprehension: (HARD) Use a list comprehension to generate a list of the first 10 cubes
10. Slices: Using oen of the programs you wrote, add several lines to the end of the program that do the following:
    * Print the message: The first three items in the list are: Then use a slice to print the first three items from that program's list
    * Print the message: Three items from the middle of the list are: Use a slice to print three items from the middle of the list
    * Print the message: The last three items in the list are: Use a slice to print the last three items in the list
11. My Pizzas, Your Pizzas: Start with your program from #1. Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following
    * Add a new pizza to the original list.
    * Add a different pizza to the list friend_pizzas
    * Prove that you have two separate lists. Print the message: My favorite pizzas are:, and then use a for loop to print the first list. Print the message,
      My friend's favorite pizzas are:, and then use a for loop to print the second lilst. Make sure each new pizza is stored in the appropriate list
12. Buffet: A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
    * Use a for loop to print each food the restaurant offers
    * Try to modify one of the items, and make sure that Python rejects the change
    * The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a
      for loop to print each of the items on the revised menu.
"""

# If Statements
"""
1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
   Your code should look something like this:
        car = 'subaru'
        print('Is car == 'subaru'? I predict True.')
        print(car == 'subaru')

        print('\nIs car == 'audi'? I predict False.')
        print(car == 'audi')
    * Look closely at your results, and make sure you understand why eaach line evaluates to True or False
    * Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False
2. More Conditional Tests: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more test and add
   them to conditional_tests.py. Have at least one True and one False result for each of the following:
    * Tests for equality and inequality with strings
    * Tests using the lower() function
    * Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
    * Tests using the 'and' keyword and the 'or' keyword
    * Test whether an item is in a list
    * Test whether an item is not in a list
3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'
    * Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
    * Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
4. Alien Colors #2: Choose a color for an alien as you did in #3 and write an if-else chain.
    * if the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
    * If the alien's color isn't green, print a statement that the player just earned 10 points
    * Write one version of this program that runs the if block and another that runs the else block
5. Alien Colors #3: Turn your if-else chain from #4 into an if-elif-else chain
    * if the alien's color is green, print a statement that the player just earned 5 points for shooting the alien
    * If the alien's color is yellow, print a statement that the player just earned 10 points
    * If the alien is red, print a message that the player earned 15 points 
    * Write three versions of this program, making sure each message is printed for the appropriate color alien
6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
    * If the person is less than 2 years old, print a message that the person is a baby.
    * If the person is at least 2 years but less than 4, print a message that the person is a toddler
    * If the person is at least 4 years old but less than 13, print a message that the person is a kid
    * If the person is at least 13 years old but less than 20, print a message that the person is a teenager 
    * If the person is at least 20 years old but less than 65, print a message that the person is an adult
    * If the person is age 65 or older, print a message that the person is an elder
7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list
    * Make a list of your three favorite fruits and call it favorite_fruits
    * Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should
      print a statement, such as: You really like bananas!
8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each
   user after they log in to a website. Loop through the list, and print a greeting to each user:
    * If the username is 'admin' print a special greeting, such as Hello admin, would you like to see a status report?
    * Otherwise, print a generic greeting, such as: Hello Eric, thank you for logging in again.
9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
    * If the list is empty, print the message: We need to find some users!
    * Remove all of the usernames from your list, and make sure the correct message is printed
10. Checking Usernnames: Do the following to create a program that simulates how websites ensure that everyone has a unique username
    * Make a list of five or more usernames called current_users
    * Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list
    * Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter
      a new username. If a username has not been used, print a message saying that the username is available.
    * Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted
11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st and 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
    * Store the numbers 1 through 9 in a list
    * Loop through the list
    * Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
      and each result should be a separate line.
"""

# Dictionaries (Need to go over this with Rob)
#yo