import json
import os
import argparse

__description__ = "Command Line tool for parsing directory structure for C3G."
__help__ = "Directoy containing software versions."

IGNORED_KEYWORDS = [".version"]
OP_FILE = "package_versions.json"

def debug(msg):
	print("[!] {}".format(msg))

def args_parse():
	parser = argparse.ArgumentParser(description=__description__)
	parser.add_argument('-d', type=str, help=__help__, required=True)
	args = parser.parse_args()
	return args

def main():
	output_json = {
		"packages": {}
	}

	args = args_parse()
	package_dir = args.d
	packages = os.listdir(package_dir)

	debug("Found {} packages.".format(len(packages)))

	for package in packages:
		versions = [version for version in os.listdir(os.path.join(package_dir,package)) if version not in IGNORED_KEYWORDS]
		output_json['packages'][package] = versions

	debug("Generating JSON file!")

	with open(OP_FILE, 'w') as output_file:
		json.dump(output_json, output_file)

	debug("File Creation Successful!")
	debug("Check package_versions.json.")

if __name__ == "__main__":
	main()