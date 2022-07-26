# Video Vantage
Have you ever found yourself watching a YouTube video and then realize it was a complete waste of time? Video Vantage solves this problem by calculating an individual rating for each comment under the video using NLP and generates an overall rating for the video. This saves time because you are able to detect if a video is beneficial before making a significant time investment. [Chrome Extension](https://chrome.google.com/webstore/detail/video-vantage/oodmlhamhkdjlnjfiahfehecngaeffbe).

## Getting Started
To test this on your local machine you will need to setup a virtualenv and run `pip install -r requirements.txt` to install the necessary dependencies.

### Running
Currently the Ajax script is communicating with a Heroku server, but to test this locally two files need to be changed. In `manifest.json` set the allowed URL to `http://127.0.0.1:5000/*`. Secondly, in `background.js` change the POST url to `http://127.0.0.1:5000/predict/`. Now this can be simply run with `python run.py` which starts up the server. View [this](https://thoughtbot.com/blog/how-to-make-a-chrome-extension) article to see how to load a chrome extension. Then navigate to any YouTube video and click on the extension in the top right and it should return a rating in 2-3 seconds.

## Built With
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  * [JQuery](https://jquery.com/)
  * [Google Chrome Extension APIs](https://developer.chrome.com/extensions)
  
## Pull Requests
Feel free to open pull requests and I would be more than happy to review them.
