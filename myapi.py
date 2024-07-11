import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response
    
    def abuse_detection(self,text):
        response = paralleldots.abuse(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion_prediction(self,text):
        response = paralleldots.emotion(text)
        return response
    def do_taxonomy(self,text):
        response = paralleldots.taxonomy(text)
        return response
    

obj = API()

print(obj.emotion_prediction('Under the Uruguay Round, the national governments of all the member countries have negotiated improved access to the markets of the member countries so as to enable business enterprises to convert trade concessions into new business opportunities.'))