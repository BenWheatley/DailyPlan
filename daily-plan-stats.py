#!/usr/bin/python

import matplotlib.pyplot as plt
import datetime

def main():
	for year in range(2016, 2022):
		process(year)

def process(year):
	fileName = str(year)+".md"
	with open(fileName, "r") as file:
		days = []
		currentDay = 0
		for line in file:
			if line.startswith("-"):
				currentDay.appendTask(line)
			elif findWeekday(line):
				currentDay = Day(year, line)
			elif len(line.strip("\n")) > 0:
				print("unexpected content:", line)

def findWeekday(line):
	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	for day in weekdays:
		if line.startswith(day):
			return True
	return False

class Day(object):
	def __init__(self, year, dateLine):
		date = dateLine.split()
		print("appending", dateLine, year, date)
		month = date[2]
		day = date[1]
		self.day = datetime.datetime.strptime("{0} {1} {2}".format(month, day, year), '%B %d %Y')
		self.tasks = []
	
	def appendTask(self, line):
		self.tasks.append(line)

if __name__ == '__main__':
	main()