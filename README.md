
# Data Centric Development with Python: flask-cookbook

# flask MongoDB Project

3rd Milestone Project module in Data Centric Development for Code Institute. Its part of the Full Stack Software Development Diploma online course.

# Live App

https://flask-app-mama-cookbook.herokuapp.com/


# Requirements

            CREATE AN ONLINE COOKBOOK:
          •	Create a web application that allows users to store and easily access cooking recipes
          •	Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
          •	Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
          •	Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
          •	Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
          •	Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
          •	Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
          •	Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)



# Objective


To create a great responsive cooking recipe website that allows users to store and easily access cooking recipes.
Project’s Core Functionality

•	Solid Structure and architecture

I really wanted to push the design and images to make the website visually stunning by using unique and different designs for each block of the website (Tour, Merchandise, About the band and Albums)


•	Great UX & UI

The goal is to make the experience and navigation look effortless through each page and create a pleasant feel for the user on a smart phone and desktop. 

•	Persuasion

To give the user a good reason to follow the up and coming albums, tours and merchandise by enjoying the first experience they have on the website to make them return again.

•	Data centric Design


•	A stunning visual website


•	Attention to detail



# Technologies Used

      •	Html5

      •	CSS 

      •	Javascript

      •	Bootstrap

      •	Flexbox

      •	Chrome and Firefox developer tools

      •	Visual studio code (Microsoft)

      •	jQuery

      •	Photoshop

      •	Cssgradient.io

      •	Flask

      •	Python

      •	MongoDB


#   Schema model for database 

https://github.com/anthony-keogh/flask-project/blob/master/static/images/UML_map.png

# Wireframe

https://github.com/anthony-keogh/flask-project/blob/master/static/images/flask-wireframe.png


# Testing

•	The majority of the testing took part in Chrome and Microsoft Explorer developer tools to test the responsiveness of the website from one device be it small smart phone up to a desktop layout of the website, then i had to marry this with different browsers.


      ----Chrome testing---------
      
  https://github.com/anthony-keogh/flask-project/tree/master/static/images/chrome



      ----Microsoft explorer--------
      
  https://github.com/anthony-keogh/flask-project/tree/master/static/images/microsoft


      ---Authentication testing-----------
  https://github.com/anthony-keogh/flask-project/tree/master/static/images/auth-testing

  https://github.com/anthony-keogh/flask-project/tree/master/static/images/auth-testing

      --Recipe Testing------------
  
  
  https://github.com/anthony-keogh/flask-project/blob/master/static/images/recipe-testing/adding%20recipe%20form%20testing.pdf


•	There were many challenges in fitting what content and design i want to put into each device and which to take out for the good of the website. There was also slight variation between what you can do in each browser, but the majority between google and Microsoft explorer were similar.


# Content

     Home

     Starter

     Main-course

     Dessert

     Recipe

     Register

     Login


# User Experience
•	achieving the main goal and functions

As mention above the main functions of the website were 
1.	Standalone design
2.	Smooth UX & UI
3.	Persuasion
      So the user experience was based on these factors and every decision was built around whether it improved these three functions or not.

•	user-friendly
This was the most important factor when analysing user experience for both the user and the browser to recognise it as a well run website. The navigation, aesthetics and the familiarity was on point and i made it very simple to use. 

•	behavioural psychology
i Incorporated different design, images, fonts and words to get the user to feel a certain way to increase the chance of them taking actions and coming back to the website for a second visit.

•	optimised website goals
i put in place solid ux methods and steps that will give the website a platform on how to improve going forward and a measuring tool to analyse what didn’t go well and what was a success.

•	making the website interesting
the website has character and a show topping design to make the user browse more around the website and stay on that website a little longer to increase the odds of a great user experience and ultimately enhance the satisfaction of the consumer

•	selling the product 
what the end result boils down to was whether the user will take action and by having all these ux steps and processes in place it will give the rock band a better percentage of the user actually following up and buying items or tickets on the website.

•	Wireframe diagram
I have provide a very simple wireframe to understand for this website that highlights the importance that each section of the website had, be it albums, tours, merchandise and about the band.


# User Interface

•	My goal as the user interface developer was to make the user's interaction as simple and efficient as possible which i think i have achive through user-centered design

•	I provided a well Guided behaviour navigation through the website with design patterns, and a clear, but simple hierarchy and readability for the user.

•	The Key sections of the website(tour, about, albums and merchandise) are very eye catching to increase the user’s attention

•	I provided a well thought out design a next step for each user interaction a person has with your interface of the website. I show familiarity in terms of what the user is going to anticipate what the next interaction should be and design to support it. 

•	The aesthetic quality of the website will enhance the user ui and ux of the website. Therefore increasing the likelihood of a interaction via email or sales on the website. 


# COLOR SCHEME

The main color in the cookbook app were:

        Purple/pink
        
        Dark 
        
        White (the white space around the pictures creates style and class to the app)

# File Management

       •  Cookbook_flask

       •  Instance (folder)


       •  Main app (folder)
       
          1.	Admin
          2.	Auth
          3.	Home
          4.	Static
          5.	templates


       •  Migrations(folder)

       •  Virtualenvironment(folder)

       •  Readme file

       •  Wireframe



# Project Approach

       •	Nav
             Navigate through the four other pages with ease

       •	Main body

       •	Footer

       • contact
 
 
 
# Project Deployment


• VS Code

Deploying it locally on VS code was very straightforward.

     1.     cd C:\Users\User\Desktop\flask_app_cookbook\mainapp-copy

     2.     flask run

• Heroku

When testing whether the app runs i would find it a lot easier to spot error when deploying it manually from github, as automatic deployement does not show much when you view it in the logs. It was harder than i taught to deploy the app successfully on heroku and getting good practice and experience from do it in this project, i can identify beforehand the common errors and laser focus i need to deploy another one in the future

     Port: 5000

     IP: 0.0.0.0


• System Variables

Without proper planning in terms of system variables the app can be much harder to run and spot any errors which i encounter with leaving out a few pieces of code. Its the back bone of getting the app to deploy properly and something that i will pay more attention to it to avoid mistakes in the future.

• gitignore

Using gitignore was very straightforward and is used to hide key pieces of secret information by combining it with app.py and env.py and then therefore telling gitignore to hide env.py in github.

• Procfile

I had issues with the procfile, i created using powershell terminal and because that there was a space in the file, which did not read the code when running on Heroku. So after testing in different terminals it worked on bash, which fix the problem.

• Config Vars

Working with config vars in heroku was very simple to use containg the postgresql key and value which was then inserting in my env.py file.


# Credits and Acknowledgements

     •	W3schools

     •	Quora 

     •	cssgradient.io

     •	Stack overflow 

     •	CSS Tutorial - Tutorialspoint

     •	www.csstutorial.net

     •	developer.mozilla.org

     •	 https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

     •	https://flask-pymongo.readthedocs.io/en/latest/

     •	https://flask.palletsprojects.com/en/1.0.x/quickstart/





