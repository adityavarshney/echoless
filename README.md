## Welcome to Echoless

Echoless analyzes posts by any Twitter handle by aggregating sentiments towards keywords in tweets. Using natural language processing and classification, Echoless can find the trending topics in a news feed. By demonstrating sentiment and ranking a handle on a political spectrum, the tool cleanly demonstrates viewpoints that users encounter frequently while using social media. With this information now available, users can look to the other side of the spectrum and find other viewpoints that may negate or counter the beliefs reverberating throughout their echo chambers. 

### Prerequisites

To use `main.py`, you will need Google Application Credentials in order to make calls to the Google Cloud and Machine Learning APIs. See more instructions on Google's page for Application Credentials: https://developers.google.com/identity/protocols/application-default-credentials. Additionally, the page on sentiment analysis may also be useful: https://cloud.google.com/natural-language/docs/sentiment-tutorial. 

### Modules

This project uses the following python modules:
- python-twitter
- watson-developer-cloud
- pymongo
- pandas
- flask
- requests

Per the instructions on Google's Cloud NLP page, running `pip install --upgrade google-cloud-language` is also necessary to communicate with Google's Cloud platform. 

### Running Echoless

Once the necessary dependencies are installed, run `python main.py`. Then go to `http://127.0.0.1:5000/` to see the webpage in action. At this point, scroll down and enter any twitter handle into the search box and hit "Run" to generate the Keywords vs. Sentiment and Political Spectrum visualizations. (Note: depending on your machine and your internet connectivity, this process could take up to about two minutes.)  
