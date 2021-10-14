import random, string
from threading import Thread
from flask import Flask, render_template

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

ok_chars = string.ascii_letters + string.digits


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/commands")
def commands():
	return render_template("commands.html")

  
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)

def run():
    app.run(host='0.0.0.0', port=8000)

def liveserver():
  t = Thread(target=run)
  t.start()