"""
Course: CSE 251 
Lesson: L02 Prove
File:   prove.py
Author: Jonathan Acosta

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py" and leave it running.
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the description of the assignment.
  Note that the names are sorted.
- You are required to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a separate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class Request_Thread(threading.Thread):

  def __init__(self, url, data_type):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.data_type = data_type
        self.result = None

  def run(self):
        global call_count
        call_count += 1
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        data = response.json()
       
        
        title = data.get("title","")
        director = data.get("director", "")
        producer = data.get("producer", "")
        released = data.get("released", "")
        characters = data.get("characters", [])
        planets = data.get("planets", [])
        starships = data.get("starships", [])
        vehicles = data.get("vehicles", [])
        species = data.get("species", [])
        
        # result = f" {self.data_type} Details: \n"
        # result = f"{title}\n{director}\n{producer}\n{released}\n\n"
        # result += f"Characters: {len(characters)}\n{','.join(characters)}\n\n"
        # result += f"Planets: {len(planets)}\n{','.join(planets)}\n\n"
        # result += f"Starships: {len(starships)}\n{','.join(starships)}\n\n"
        # result += f"Vehicles: {len(vehicles)}\n{','.join(vehicles)}\n\n"
        # result += f"Species: {len(species)}\n{','.join(species)}\n\n"

        result = {
            'Title': title,
            'Director': director,
            'Producer': producer,
            'Released': released,
            'Characters': characters,
            'Planets': planets,
            'Starships': starships,
            'Vehicles': vehicles,
            'Species': species
        }

        self.result = result


# TODO Add any functions you need here


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    
    response = requests.get(TOP_API_URL)
    top_api_urls = response.json()

    film_url = top_api_urls.get('films','') + '6/'
    film_thread = Request_Thread(film_url, 'Film')
    film_thread.start()
    film_thread.join()

    if film_thread.result is not None:
        result_dict = film_thread.result
        print(f" {result_dict['Title']}")
        print(f" Director: {result_dict['Director']}")
        print(f" Producer: {result_dict['Producer']}")
        print(f" Released: {result_dict['Released']}\n")

        print(f" Characters: {len(result_dict['Characters'])}")
        print(f" {', '.join(result_dict['Characters'])}\n")

        print(f" Planets: {len(result_dict['Planets'])}")
        print(f" {', '.join(result_dict['Planets'])}\n")

        print(f" Starships: {len(result_dict['Starships'])}")
        print(f" {', '.join(result_dict['Starships'])}\n")

        print(f" Vehicles: {len(result_dict['Vehicles'])}")
        print(f" {', '.join(result_dict['Vehicles'])}\n")

        print(f" Species: {len(result_dict['Species'])}")
        print(f" {', '.join(result_dict['Species'])}\n")
        #print(film_thread.result)

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()