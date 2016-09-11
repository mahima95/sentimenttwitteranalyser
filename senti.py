from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob


#consumer key, consumer secret, access token, access secret.
ckey='nH71B9e8Zq28j3gWL3Up2mZbt'
csecret='UdpDP70SS3sbZz5ohVGs3LgluHyjOixB5yMNtFdKKqOVwGYrlH'
atoken='1477539541-VT8uK6Hg4FaeCUTlaEsGqlo1HXuKy2xXHwX1VmF'
asecret='C6yJkuyjdLrabi6F4vYcvvhoHaTJUf4UUB9kldaiNus27'




def sentimentanalysis(text):
	b=TextBlob(text)
	a=str(b.sentiment)
	print a
	return a

class listener(StreamListener):

    def on_data(self, data):
	tweet=data.split(',"text":"')[1].split('","source')[0]
	SentimentRating=sentimentanalysis(tweet)
	saveME=tweet+'\n::SENTIMENTAL RATING='+SentimentRating+'\n\n'
	output=open('output6.csv','a')
	output.write(saveME)
	output.close()
        ##print(tweet)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
		
