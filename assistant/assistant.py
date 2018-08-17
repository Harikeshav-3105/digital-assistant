import wolframalpha
import os
import json
import requests     
import sys
from weather import Weather
from weather import Unit
import geocoder
import requests
import webbrowser
import wikipedia
import random
import requests
import speech_recognition as sr
from gtts import gTTS

app_id = "YERQA8-KG2P6T357L"
client = wolframalpha.Client(app_id)
inst = None

def init():
    global inst
    inst = Brain()


class Brain:
    def fetch(self):
            main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=21d02c03cbd143d8a65fab4bac5f181f"
            open_bbc_page = requests.get(main_url).json()
            article = open_bbc_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"]+str(" - ")+ar["description"])
                    
            for i in range(len(results)):
                print(i + 1, results[i])
                if i == 4:
                    break
                return results[i]
        
    def main(self, query):
        try:    
            if "what" in query and "name" in query or "who are you" in query:
                name = "'My name is Henry'"
                print(name)
                return name

            if query == "who's birthday is on february 26":
                name = "Suhani's birthday is on february 26"
                print(name)
                return name
            
            if "latest" in query and "news" in query or "news" in query:
                    self.fetch()
                    return

            if query == "":
                    print("invalid command!")
                    return

            if query == "quit" or query == "exit":
                    sys.exit()
                    return

            if "search" in query or "open" in query:
                query = query.split(' ')
                query = " ".join(query[1:])
                ans = "Here's what I found on the web for " +  query
                print(ans)
                webbrowser.get().open("https://www.google.com/search?client=safari&rls=en&q="+query+"&ie=UTF-8&oe=UTF-8", new=2)
                return ans

            else:    
                try:
                    result = client.query(query)
                    answer = next(result.results).text
                    print(answer)
                    return answer
                        
                                
                except:
                    try:
                        query = query.split(' ')
                        query = " ".join(query[2:])
                        page = wikipedia.summary(query, sentences=2)
                        print(page)
                        return page

                    except:
                        query = query.split(' ')
                        query = " ".join(query[1:])
                        answer = "Here's what I found on the web for " + "'" +  query + "'"
                        print(answer)
                        webbrowser.get().open("https://www.google.com/search?client=safari&rls=en&q="+query+"&ie=UTF-8&oe=UTF-8", new=2)
                        return answer
        
        except KeyboardInterrupt:
            os.system("clear")
            sys.exit()

    def run(self):   
        while True:    
            n = 0
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                n=(n+1)     
                print("Say something!")
                audio = r.listen(source)

            try:
                s = (r.recognize_google(audio))
                message = (s.lower())
                print("> " + message)
                reply = self.main(query=message)
                tts = gTTS(reply)
                tts.save("ans.mp3")
                os.system("afplay ans.mp3")

            except sr.UnknownValueError:
                print("$could not understand audio")
            except sr.RequestError as e:
                print("Could not request results$; {0}".format(e))
