[![Build Status](https://travis-ci.org/sarahg177/unicorn_attractor.svg?branch=master)](https://travis-ci.org/sarahg177/unicorn_attractor)

# Unicorn Issue Attractor

My fourth milestone project for Code Institute Full Stack Developer course, Full Stack Frameworks with Django. This is a web application for users to create tickets for bugs and features. The app consists of a Home, Registration, Login, Tickets, Blog pages and includes a statics page showing a graph of how many bugs and features are tended to on a daily, weekly and monthly basis. It also shows the highest voted bug and highest paid feature. Users are able to create, read, update and delete their ticket data.   

## UX

This web application has been developed to allow users to report bugs that they have, which they would like fixing. Other users can then vote for bugs that they also have and would like fixing. The users can also add features to the database that they would like to own. Other users can ask and pay for this feature too at a price of £20 per vote. The highest voted bug and highest paid feature has the higher priority for implementing that bug or feature. I promise to always spend at least 50% of my time working on developing the highest paid feature.

### Style

 For this application I decided to use Bootstrap design and utilised the bootstrap.css framework for the frontend of the application adding custon css style where necessary to override values. I used the blue background as I felt this looked like a brainstorm and represents features emerging from the screen.
 
 ### User Stories
 
 As a user I would like to:
 
 * Create a ticket for a bug or feature.
 * View the details of all bugs and features in the database.
 * Be able to comment on bugs and features.
 * Track the statics of what is being worked on on a daily, weekly and monthly basis.
 * Track what tickets have been completed, working on and waiting to be looked at.
 * Track which bug and feature is the highest vote and paid for.
 * Invest in feature which I would like to own.
 * Have access to a blog.
 

## Wireframes

![wireframes](./static/images/unicorn_tracker_wireframes.png) 

My wireframes can be viewed at https://xd.adobe.com/view/36aa27bd-8b1d-48fe-46ce-3070c8d2f6a1-409b/?fullscreen 

## Project Features

### Desktop/Tablet View

#### Home Page

The home page consists of a welcome page explaining to the user what the application can be used for. A registration and login button is included in the Navbar. The user can view the tickets if they are not logged in.

### Registration Page

The registration page consists of a form with 3 fields, username, password and password verification and a Register button. If the user already has an account there is a link to take them to the login page to sign in.

### Login Page

The login page consists of a form with 2 fields, username and password and a Login button.

###Tickets Page

The tickets page consists a button to Create a new ticket. The page is empty until some tickets are added, once they have been added the page consists of a list of the current bugs and features. The lists consists of each ticket showing:

* Title: Shows the title of the bug that the user has given it
Ticket Status: This shows as coloured badge of 
    * Todo - red
    * Doing - yellow
    * Done - green 
* Views: represneted by an eye, shows the number of times users have viewed this ticket
* Votes (for bugs): represented by a hand, shows the number of votes the ticket has received
* Money Raised (for features): represented by £, shows the amount of money raised for the ticket
* Date: shows the date the ticket was created
* Time: shows the time the ticket was created
* User: shows which user submitted the ticket
* View Details: button which redirects the user to view the details page for that ticket
* I have this too (for bugs): button which allows the user to vote for the ticket. This adds a vote and increments the number of votes. The user can only vote once for each ticket.
* I want to have this too (for features): button which allows the user to buy for a vote for the ticket. This pops up a box to checkout using Stripe. The form consist of 4 fields, email, card number, expiry date and CVC and a button to Pay £20. The user can buy as many votes as they wish.

### Ticket Details Page

The ticket details page consist of the full details of the submitted ticket as above including - 
* Details: full description of the ticket.
* Comments: any comments which have been submitted by other other, showing:
    * User who submitted a comment
    * Date and time the comment was submitted
* Comment form: A textbox where the user can leave their own comments, which will be displayed below the previous comments.

### Create a New Ticket Page

The create a new ticket page consists of a form with 3 fields, a dropdrown option Issue type, which is set to Feature as default, title and description and a save button

### Edit Ticket Page

The edit ticket page shows a form similar to creat a ticket page but to edit the ticket all of the fields are populated with the ticket details. The fields can be edited and will update the database once submitted.

### Graphs Page

The graphs page consist of a bar chart signifying the bugs and features tended to on a daily, weekly and monthly basis. The page also displays the Highest Voted Bug and Highest Paid Feature. Showing the ticket title and the votes or money raised retropectively. I created the bar chart using Highcharts.com

### Blog Page

The Blog page consists of all of the blogs submitted by users displaying the blog title, contents and the publisher author. This page is paginated showing 5 blog posts on each page. On this page the user can create a post by clicking the button at the top of the page. 


### New Blog Post Page

The new blog post consist of a form with 4 fields, title, content, tag and published date. The published date field is pre populated with today's date. To button at the bottom saves the blog post.  

## Feature Left to Implement
As more bugs and feature are completed add another html page and filter out the done ticket status.

## Technologies Used

For this project the following technologies were used:

* HTML5
* CSS3
* Bootstrap
* Python
* Django
* JavaScript
* Postgresql
* PyCharm

## Testing

### TestCase


### Travis

I have included Travis testing for continuous intergration testing.

### Manual Testing

For testing this application use login details: 
* Username: test
* Password: testing1234

Testing for this project has been done with several browsers and devices.

#### Browsers

##### Mobile
* Safari
* Chrome

##### Desktop
* Safari
* Chrome
* Opera

#### Devices
* iMac
* MacBook Pro
* iPhone X
* iPad Air
* iPad Pro


## Deployment

### GitHub
The code for this project can be viewed on GitHub https://github.com/sarahg177/unicorn_attractor

### Heroku
The application has been deployed to Heroku and can be viewed at https://unicorn-issue.herokuapp.com/

## Credits

* Lightbulb image: http://hddfhm.com
* Mentor Spencer Barriball who has helped me immensely and kept me going when I have struggled. 
* Students from Slack and the Code Institute tutors for all of their help
