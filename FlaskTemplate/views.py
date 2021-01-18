from flask import render_template, request
from FlaskTemplate import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    # TODO: Create a query parameter so as to add our name to the URL like 
    # https://first-project.azurewebsites.net/name=Grace
    name = request.args.get('name')

    return render_template(
        'index.html',
        # Display the name on the website.
        name = name
    )

