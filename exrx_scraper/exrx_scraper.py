import requests
import re
import pickle
from bs4 import BeautifulSoup


class MuscleGroup:
    def __init__(self, name, muscles, link):
        self.name = name
        self.muscles = muscles  # <- the "muscles" attr. should be a list of Muscle objects.
        self.link = link


class Muscle:
    def __init__(self, name, link):
        self.name = name
        self.link = link


def scrape_exrx_directory():
    """

    :return: Returns a list of the CSS elements that contain what we need to id & group muscles.
    """
    page = requests.get('https://exrx.net/Lists/Directory')
    contents = page.content

    exrx = BeautifulSoup(contents, 'html.parser')
    # Muscles start at index 0, last one is at 58.
    raw_data = exrx.find("article").find_all("li")[:59]  # Retrieve all bullets in the "article" component.
    raw_data_sub = []
    idxs = [0, 3, 9, 13, 20, 31, 38, 44, 49, 53]  # I found each index by hand & hard-coded this.
    for idx in idxs:
        raw_data_sub.append(str(raw_data[idx]))
    return raw_data_sub


def scrape_exrx_muscle(muscle_url):
    """

    :return: Returns a list of the CSS elements that contain workout names & URLs for a given muscle.
    """
    # TODO:
    page = requests.get('https://exrx.net/Lists/Directory')
    contents = page.content

    exrx = BeautifulSoup(contents, 'html.parser')
    # Muscles start at index 0, last one is at 58.
    raw_data = exrx.find("article").find_all("li")[:59]  # Retrieve all bullets in the "article" component.
    raw_data_sub = []
    idxs = [0, 3, 9, 13, 20, 31, 38, 44, 49, 53]  # I found each index by hand & hard-coded this.
    for idx in idxs:
        raw_data_sub.append(str(raw_data[idx]))
    return raw_data_sub


def scrape_exrx_workouts(MuscleGroup_obj):
    # Returns the MuscleGroup_obj with the workouts appended to the appropriate muscle
    # TODO: implement this
    # TODO: add workout attrs to the Muscle class.
    return 0


def create_MuscleGroups(x):
    """

    :param x: HTML/CSS elements that have a muscle groups embedded within
    :return: a list of all the MuscleGroup objects
    """
    PATTERN = r'ExList/'
    allmuscles = []

    current = ''  # used to skip over duplicates (i.e. if Muscle = 'Chest' twice in a row in CSS).
    for entry in x:
        result = MuscleGroup(None, [], None)  # Reset after every iteration
        U = re.split(PATTERN, entry)[1:]
        for u in U:
            groupName = re.search('(.*)Wt"', u)
            if groupName is not None:
                result.name = groupName.group(1)
                result.link = f'https://exrx.net/Lists/ExList/{result.name}Wt'
            else:
                u_muscle = Muscle(None, None)  # (name, link)
                u_muscle.name = re.search('Wt#(.*)"', u).group(1)
                u_muscle.link = f'https://exrx.net/Lists/ExList/{result.name}Wt#{u_muscle.name}'
                result.muscles.append(u_muscle)
        allmuscles.append(result)
    return allmuscles


def scrape_muscleData():
    # Getting the muscle data
    exrx_css = scrape_exrx_directory()
    muscle_data = create_MuscleGroups(exrx_css)
    # Delete duplicates
    duplicates = []
    for i in range(0, len(muscle_data)):
        # print(f'{muscle_data[i].name}')
        # print(f'{muscle_data[i].link}')
        carry = ''
        for j in range(0, len(muscle_data[i].muscles)):
            if muscle_data[i].muscles[j].name == carry:
                # print(i, j)
                duplicates.append([i, j])
            # print(f'    {muscle_data[i].muscles[j].name}')
            # print(f'    {muscle_data[i].muscles[j].link}')
            carry = muscle_data[i].muscles[j].name
    for [i, j] in duplicates:
        muscle_data[i].muscles.pop(j)
    print(f'Successfully scraped muscle data.')
    return muscle_data


def save_muscleData(filename, data):
    # Save object to file
    with open(filename, 'wb') as outp:
        pickle.dump(data, outp, pickle.HIGHEST_PROTOCOL)
        print(f'Muscle data: {outp}')
    return None


def load_muscleData(filename):
    with open(filename, 'rb') as inp:
        infile = pickle.load(inp)
        print(f'Loaded file: {inp}')
    return infile


if __name__ == "__main__":
    AllMuscles = scrape_muscleData()
    save_muscleData('muscle_data.pkl', AllMuscles)
    del AllMuscles
    exit(0)
