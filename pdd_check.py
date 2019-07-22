#!/usr/bin/env python3

import sys

def main():
	if len(sys.argv) < 2:
		print("пример запуска: ./pdd_check.py chapter_11.txt")
		return

	a, count = read_answers_from_file(sys.argv[1])

	while True:
		print("ответы для проверки:")

		b = read_answers_from_stdin(count)

		check_answers(a, b)

		is_retry = input("проверить себя ещё? (y/n): ")
		if is_retry != "y":
			return

def read_answers_from_file(file):
	a = {}

	with open(file) as f:
		count = int(f.readline())

		for i in range(1, count + 1):
			a[i] = f.readline()

	return (a, count)

def read_answers_from_stdin(count):
	a = {}

	for i in range(1, count + 1):
		a[i] = input(str(i) + ": ")

	return a

def check_answers(a, b):
	for k in b:
		if int(a[k]) != int(b[k]):
			print(str(k) + ": ожидалось " + str(a[k]).strip() + "; выбрано " + str(b[k]).strip())

if __name__ == "__main__":
	main()
