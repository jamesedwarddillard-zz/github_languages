import sys
import operator
from collections import defaultdict
import requests
from secret import USERNAME, PASSWORD

def get_repositories(user):
	"""Retrieve a list of a user's repositories"""
	url = "https://api.github.com/users/{user}/repos".format(user=user)
	response = requests.get(url, auth=(USERNAME, PASSWORD))
	return response.json()

def main():
	repositories = get_repositories(sys.argv[1])
	print repositories

if __name__ == "__main__":
	main()
