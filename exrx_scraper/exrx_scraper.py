import requests
import re
from bs4 import BeautifulSoup


class MuscleGroup:
    """Elementary muscle group object

    A muscle group has multiple muscles that constitute it.
    An individual muscle can optionally regions (i.e. Sternal + Clavicular Pectoralis Majors)

    Each muscle group will have a URL that leads to a page of its constituent's associated workouts.
    Each individual muscle may optionally have a URL that leads to its associated workouts.
    """
    # TODO: Implement MuscleGroup class.


page = requests.get('https://exrx.net/Lists/Directory')
contents = page.content

exrx = BeautifulSoup(contents, 'html.parser')
# Muscles start at index 0, last one is at 58.
raw_data = exrx.find("article").find_all("li")[:59]  # Retrieve all bullets in the "article" component.

# TODO: Muscle groups contain ALL the data between their index & their final muscles index.
# TODO: Let's iterate over the whole list & use that index by itself to compose our muscle groups.
raw_data_sub = []
idxs = [0, 3, 9, 13, 20, 31, 38, 44, 49, 53]  # I found each index by hand & hard-coded this.
for idx in idxs:
    raw_data_sub.append(str(raw_data[idx]))

# TODO: Create a loop that uses regex to get all the components we need.
