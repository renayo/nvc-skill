from mycroft import MycroftSkill

# import random

class Nvc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    def initialize(self):
            self.register_intent_file('start.intent', self.handle_start)
            self.other1=self.register_intent_file('other.intent', self.handle_other)
            self.register_intent_file('observe.intent', self.handle_observe)
            self.register_intent_file('feeling.intent', self.handle_feeling)
            self.register_intent_file('need.intent', self.handle_need)
            self.register_intent_file('request.intent', self.handle_request)
            self.register_intent_file('quote.intent', self.handle_quote)

    def handle_start(self, message):
            self.speak_dialog('start')

    def handle_quote(self, message):
            self.speak_dialog('quote')
        
    def handle_other(self, message):
            self.other1 = message.data.get('other')
            self.speak("Thank you. I heard you say that you would like to communicate with '" + message.data.get('other') + "'. Let's talk about what you observe in the actions of '" + message.data.get('other')+ "' that you like or don't like. Try to focus on observation separate from evaluation.")
            self.speak_dialog('exampleobserve')
            self.speak("To reply, say the wake word, followed by 'I observe that'")


    def handle_observe(self, message):
            self.observe1 = message.data.get('observation')
            self.speak_dialog('observe')
            self.speak_dialog('examplefeeling1')
            self.speak(" in stead of ")            
            self.speak_dialog('examplefeeling2')
            self.speak(" To state your feelings about '"+ message.data.get('observation') + "', say the wake word and then 'I feel ...'")
           
    def handle_feeling(self, message):
            self.feeling1 = message.data.get('feeling')
            judgments = ["patronised","abandoned","abused","attacked","betrayed","boxed-in","bullied","cheated","coerced","co-opted","cornered","diminished","distrusted","interrupted","intimidated","let down","manipulated","misunderstood","neglected","overworked","patronized","pressured","provoked","put down","rejected","taken for granted","threatened","unappeciated","unheard","unseen","unsupported","unwanted","used","should","could","would"]
            for judgment in judgments:
                if judgment in self.feeling1:
                    self.speak("Your last response contains a hint of a judgment. It may be better to reformulate your statement about your feelings.")
                    self.speak("To restate your feelings about '"+ self.observe1 + "', say the wake word and then 'I feel ...' or you can continue with needs as the next step.")
                    break
            self.speak("When you say '" + message.data.get('feeling') + "', what are needs, values, and desires within you that create these feelings? Some common needs include autonomy, integrity, interdependence, play, spiritual communion, and physical nurturance.")
            self.speak_dialog('specificneeds')
            self.speak("Accordingly, what do you need, value, or desire that creates these feelings that you have described as '" + message.data.get('feeling') +"'? To state these deeper needs, say the wake word and then 'I need ....'")
        
    def handle_need(self, message):
            self.need1 = message.data.get('need')
            self.speak_dialog('need')
            self.speak("Based on that, what do you wish to request from '" + self.other1 + "' that you are not presently receiving? You can say 'I request' ....")
        
    def handle_request(self, message):
            self.speak("Good. Putting it all together, here is something you can say to '" + self.other1 + "'. "+ self.observe1 + ". I feel " + self.feeling1 + ". I need " + self.need1 + ". I request " + message.data.get('request') + ". Ask '" + self.other1 + "' to reflect this back.")        
                   
    def stop(self):
        pass
    
def create_skill():
    return Nvc()            
