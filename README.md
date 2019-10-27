# blog by quality_assurance

# Instructions
1. Clone this repo.
2. Install Flask using the following command:
```
pip install -U Flask
```
3. Run app.py to start the Flask app.
```
python3 app.py
```

# Modules
### Auth Module
---
```
  hash() uses the builtin hashlib to hash a given password.
  * Implements SHA256
  * Uses a Flask app wide salt
  * Returns a hexadecimal representation of the hash

  auth() authenticates a given password with a given hash.
  * Uses hash() to compute a hash and compare it against the given hash

  hash() is necessary to generate a hash to either store or compare against.
  auth() is necessary as a wrapper function for authentication.

  hash() and auth() will be used for signup or login functionality.
  The calculated hash will be stored in the database in place of password.
```

---

### DBConn Module
---
```
  conn() connects the Flask app to the database.
  * Connection stored in Flask's g object

  close() terminates an existing SQLite Connection.
  * Close an existing connection in g if it exist

  conn() and close() are necessary to connect to the database for data addition/retrieval.

  conn() and close() are used in app context to be automatically invoked on HTTP request.
```

---

### DBFunc Module
---
```
  header_types() returns the types of a table's columns.

  insert() adds a row to a given table.

  get() returns certain piece(s) of data from the database.

  header_types() can clarify the type of the data that needs to be inserted into the database.
  insert() and get() are necessary in retrieving or adding data to the database.

  header_types() can be used to identify the column types of tables to insure no error with 
  wrong datatype insertions.
  insert() and get() are used throughout the Flask app to add, edit, or view data in the following:
    * /signup
    * /login
    * /<username>
    * /<username>/<blog_id>
    * ...
```

---

### Edit Module
---
```
  
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
