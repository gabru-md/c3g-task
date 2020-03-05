This repository contains the task for C3G. The task is related to the project idea titled "Automatic update of the C3G software stack catalog".

This repository contains the following files:

1. readme.txt
2. catalog_info.txt
3. how_to_proceed.txt
4. create_json.py
5. package_versions.json

catalog_info.txt - file contains the information that an ideal catalog must possess.
how_to_proceed.txt - defines the workflow of automating the updation task for the JSON.
create_json.py - contains the code for the script used to generate package_versions.json.
package_versions.json - contains the generated JSON data of the file structure.

How to use the script?

1. Clone the repository

$~ git clone https://bitbucket.org/mugqic/gsoc_2020
$~ git clone https://github.com/gabru-md/c3g-task

2. Enter the c3g-task folder

$~ cd c3g-task

4. Run the script

$~ python3 create_json.py -d ../gsoc_2020/data_test/SoftStackCatalog/modulefiles/mugqic/

5. Done

You can now see the output JSON file in your folder.


Author

Manish Devgam