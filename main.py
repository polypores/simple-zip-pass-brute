import zipfile
import os

zip_file = input("[+] ZIP file: ")
word_list = input("[+] Password list: ")

def alertAndExit(message):
	print(message)
	os.sys.exit()

try:
	zipf = zipfile.ZipFile(zip_file)
except zipfile.BadZipfile:
	alertAndExit("[!] Bad or collapsed zip file.")
except FileNotFoundError:
	alertAndExit("[!] Zip file is not found.")
	
try:
	open(word_list, "rb")
except FileNotFoundError:
	alertAndExit("[!] Wordlist is not found.")
	
with open(word_list, "rb") as f:
	passes = [x.strip() for x in f.readlines()]
	for x in passes:
		print(x)
		print(f"Trying {x.decode('utf8')}")
		try:
			zipf.extractall('results', None, x)
			print("[*] Password found.")
			alertAndExit(f"[*] Password: {x.decode('utf8')}")
		except Exception:
			pass
	print("[!] Valid password is not found.")