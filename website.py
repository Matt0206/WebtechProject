from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)

#api scrapes reddit and responds with JSON that includes link to img
def get_meme():
	url = "https://meme-api.com/gimme"
	response = json.loads(requests.request("GET", url).text)	#gets us link to our img
	meme_large = response["preview"][-2]	#links second largest meme image
	subreddit = response["subreddit"]	#links name of the subreddit
	return meme_large, subreddit	#returns the link to the img and the name of the subreddit

#default route/ main route
#assigns meme_large to meme pic and subreddit to subreddit
@app.route("/")
def index():
	meme_pic,subreddit = get_meme()
	return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
