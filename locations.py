#initialize
import webbrowser

#functions
url = ["https://tinyurl.com/3uy6mj7s", #cancun
        "https://tinyurl.com/yc62xyvt", #New York City
        "https://tinyurl.com/d969cvwn", #Italy
        "https://tinyurl.com/4w7cpxr8"] #Venice
descriptions = [
    "Cancun is a warm beach spot with clear blue water and lots of fun outdoor activities.",
    "New York City is a big, busy place full of famous sights, bright lights, and many things to do.",
    "Italy is a large country with beautiful cities, great food, and tons of things to explore.",
    "Venice is a small, peaceful city built on water with boats, bridges, and old buildings."]

def locations():
        print("ready to go on vacation")
        weather = input("do you want to go to a place that is warm? (yes/no): ")
        if weather == "yes":
            webbrowser.open(url[0])
            print(descriptions[0])
        elif weather == "no":
            continent = input("do you want to go to Europe? (yes/no): ")

            if continent == "yes":
                size = input("do you want a big place to explore? (yes/no): ")
                if size == "yes":
                    webbrowser.open(url[2])
                    print(descriptions[2])
                else:
                    webbrowser.open(url[3])
                    print(descriptions[3])
            else:
                webbrowser.open(url[1])
                print(descriptions[1])
#main
locations()
# sources of information

#picture of cancun
#website Name:Expert Vagabond
#url: https://expertvagabond.com/cancun-things-to-do/
#author name: Matthew Karsten
#article name:Cancun Mexico: 25 Best Things To Do In 2025
#date: Published March 25, 2019 — Updated March 28, 2025

#picture of New York City
#website Name:The New York Pass
#url: https://newyorkpass.com/en/things-to-do/10-days-in-new-york-city
#author name: Suz Pathmanathan
#article name:10 Days in New York City – The Ultimate Itinerary

#picture of Italy
#website Name: britannica
#url: https://www.britannica.com/place/Italy
#author name: Giuseppe Nangeroni
#article name: Italy
#date: last updated  Mar. 1, 2026

#picture of Venice
#website Name:TripAdvisor
#url:https://www.tripadvisor.com/Articles-leebaG4YCtbU-4_days_in_venice_italy_itinerary.html
#author name:Maria Kirsten Adelmann
#article name:4 perfect days in Venice
#date:Aug 2, 2024
