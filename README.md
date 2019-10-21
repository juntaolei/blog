# blog by quality_assurance

Roster + Role
---
* Jun Tao Lei: Sir Project Manager 
```
  Route Functions
    * Renders the template for each page requested with routes pertaining to unique users generated using certain user attributes
    * Implement any other necessary functions required for the route
  Login/Signup Module
    * Initialize a new session when the user logs in or signs up and remove it once they log out
    * Authenticates the user in a sensible manner
```

* Grace Mao: Front-end Overlord
```
  Templates
    * Make a template that will store and format the title, headers, content, and footers for each page of the blog to be displayed
  Building Forms
    * Make the login and signup forms, as well as facilitate submission once a user is done editing a new post
    * Handle buttons in the templates (Home button on each page, submit buttons etc)
  Facilitating Entry Addition/Update Using Built Database Operations
    * On a user’s My Blog page, make a button “New Post”, which will redirect them to a blank edit page (identified by the next available id) where they can put in their title and content
    * Make the “Edit” button on any existing post’s page, provided that it is the logged in user’s own post, and allow the user to update their table of posts in the database so that, once changes are submitted, the template will display the updated post
```
 
* Sophie Nichol: Queen of Database Connection Module
```
  Initialize Database
    * Make the Users table containing the username, id, and password for every user. For each user, make a <username> table containing a row for each post they make and storing the post id, title, contents, and timestamps
  Connect Flask and SQLite3
    * Establish a database connection with Flask
    * Keep track of executions of SQLite commands and Flask actions
  Handle Database Operations
    * Facilitate any changes that the user will request to the table, such as editing the table once a user updates a blog post, creating a new row when a user makes a new post, or creating a new table when a new user joins
```
