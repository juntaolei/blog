# **blog** *by* **quality_assurance**

# Instructions
1. Clone this repository using Git or downloading a zip.
2. Install Flask using the following command:
```
pip3 install -U Flask
```
3. Run app.py to start the Flask app.
```
python3 app.py
```
4. Visit ```http://127.0.0.1:5000``` to view the app.

# Modules
### Required Flask Components
---
```
  Flask, g, session, redirect, url_for, render_template, request, and current_app are Flask components that are used.
  
  Flask constructor is used to create the Flask app.
  g is used as a namespace object to store data during an application context.
  session is used to store data during a user's session.
  redirect is used to route the application.
  url_for is used as a method in redirecting to a different route.
  render_template is used a way to render templates in Flask.
  request is used as a method to receive data from client side.
  current_app is used as a proxy to access data associated with the current application.
```

---

### Standard Python Lib
---
```
  search() is imported from re in order to use regular expressions.
  Number is imported from numbers to act as a type for most types of number.
  sha256() is imported from hashlib to perform the SHA-256 hash algorithmn.
  connect() is imported from sqlite3 to establish a SQLite3 Connection.
```

---

### Auth Module (User Generated)
---
```
  hash(password) uses the builtin hashlib to hash a given password.
  auth(username, password) authenticates a given password with a given hash.
  register(username, password, displayname) registers the user if the user does not exist.
  update_auth(username, currentpassword, newpassword) updates the password given the current password is valid.
```

---

### DBConn Module (User Generated)
---
```
  conn() connects the Flask app to the database, storing the connection stored in Flask's g object.
  close() terminates an existing SQLite Connection in g if it exist.
```

---

### DBFunc Module (User Generated)
---
```
  header_types(tbl_name) returns the types of a table's columns.
  insert(tbl_name, values) adds a row to a given table with given values.
  get(tbl_name, column, conditional=””) returns certain piece(s) of data from the database based on the conditional(s).
```

---

### Edit Module
---
```
  create_post(userid, author, title, content) inserts a row for a blog post into the blogs table.
  update_post(blogid, blogcontent, blogtitle) updates a row from the blogs table.
  update_user(username, field, newvalue) updates a certain attribute of a user in the users table
  delete_post(blogid) deletes a row from the blogs table given the blog id
```

# Roster + Role
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
