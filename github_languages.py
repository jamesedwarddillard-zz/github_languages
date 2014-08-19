import sys
import operator
from collections import defaultdict
import requests
from secrets import USERNAME, PASSWORD

def get_repositories(user):
	"""Retrieve a list of a user's repositories"""
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url, auth=(USERNAME, PASSWORD))
	return response.json()

def get_language_dictionaries(repositories):
    """
    Return a list of dictionaries containing the languages used in each
    repository
    """
    language_dictionaries = []
    for repository in repositories:
        url = "https://api.github.com/repos/{owner}/{repo}/languages"
        url = url.format(owner=repository["owner"]["login"], repo=repository["name"])
        response = requests.get(url, auth=(USERNAME, PASSWORD))
        language_dictionaries.append(response.json())
    return language_dictionaries

def main():
	repositories = get_repositories(sys.argv[1])
	language_dictionaries = get_language_dictionaries(repositories)
	print language_dictionaries

if __name__ == "__main__":
	main()
