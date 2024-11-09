from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("STRING DECODED:\n", content)

        # käytetään toml-kirjastoa
        deserialized = toml.loads(content)
        #print("DESERIALIZED:\n", deserialized)

        poetry_data = deserialized['tool']['poetry']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(poetry_data['name'],
                       poetry_data['description'],
                       poetry_data['license'],
                       poetry_data['authors'],
                       list(poetry_data['dependencies'].keys()),
                       list(poetry_data['group']['dev']['dependencies'].keys())
        )
    