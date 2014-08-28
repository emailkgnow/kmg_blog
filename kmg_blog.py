instructions = '''
FROM LECTURE:
Build a Blog where:
--front page lists all entries (or at least last 10 entries)
--it has a seperate form page to submit new entries via title and body (must check for errors to make sure a title and body are present)
--redirects to a permalink page for entries if entry is successful


ORIGINAL INSTRUCTIONS:
In order to be graded correctly for this homework, there are a few things to keep in mind.
We'll be grading your web app by POSTing new blog entries to your form and checking that they appear on
your blog's front page. There are a few main issues you need to keep in mind in order for this to work:

We assume your form to create new blog entries is at a path of '/newpost' from your blog's front page.
The form method must be POST, not GET. 
The form input boxes must have the names 'subject' and 'content'  
You must enter the full url into the supplied textbox above,
including the path to your blog's front page.
Don't forget to escape your output!

ADDITIONAL INSTRUCTIONS:
I realized while recording the solution to HW 3 a few things that I didn't cover in the lecture that
will be helpful to know. After submitting a blog post, I ask you to redirect to a permalink for
that post. The url format might look something like this: /blog/1001, where 1001 is the id of the post you
just submitted. To get the id of an entity you just created: obj.key().id()

Find some examples of more complex URL handling here: http://webapp-improved.appspot.com/guide/routing.html

To look up an object by id, you can use the get_by_id() function
document here: https://developers.google.com/appengine/docs/python/datastore/modelclass#Model_get_by_id

Hope this helps!
'''

import webapp2
import cgi
import re

form_entry='''<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Khalid's Blog</title>
</head>
<body>
<form method="post">
    <h1 style='color:green'>Welcome to Khalid's Blog</h1>
    <br>
    <textarea name="title"
                style="height: 25px; width: 400px;">{title}</textarea>
 <br><br>   <textarea name="text"
                style="height: 100px; width: 400px;">{entry}</textarea>
   <br><br><br> <input type="submit">
    
 </form>
"""

form_main='''<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Khalid's Blog</title>
</head>
<body>
<form method="post">
    <h1 style='color:green'>Welcome to Khalid's Blog</h1>
    <br>
    <textarea name="title"
                style="height: 25px; width: 400px;">{title}</textarea>
 <br><br>   <textarea name="text"
                style="height: 100px; width: 400px;">{entry}</textarea>
   <br><br><br> <input type="submit">
    
 </form>
"""

form_perma= '''<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Khalid's Blog</title>
</head>
<body>
<form method="post">
    <h1 style='color:green'>Welcome to Khalid's Blog</h1>
    <br>
    <textarea name="title"
                style="height: 25px; width: 400px;">{title}</textarea>
 <br><br>   <textarea name="text"
                style="height: 100px; width: 400px;">{entry}</textarea>
   <br><br><br> <input type="submit">
    
 </form>
"""

class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form.format(my_encoded_input=""))


    def post(self):
        user_input=self.request.get("text")
        new_encoded_input=mycodec(user_input)
        self.response.out.write(form.format(my_encoded_input= escape_html(new_encoded_input)))





