# Scancode analysis in OSS_Report format
## When you first set up your environment -linux
$ pip install virtualenv     
$ virtualenv -p /usr/bin/python3.6 venv     
$ source venv/bin/activate        
$ pip install http://mod.lge.com/code/rest/archive/latest/projects/OSC/repos/fosslight_source/archive?format=zip             

<hr />       

## How to run it by command
### Print result to OSS Report
$ fosslight_source -p [Path_to_scan]
### Print result to OSS Report and json file
$ fosslight_source -p [Path_to_scan] -j
### Print result to OSS Report and set output file name
$ fosslight_source -p [Path_to_scan] -o [output_file_name_without_file_extension]     
## Converting scancode json result to OSS report
$ fosslight_convert -p [Path_of_scancode_json_files]       
### Converting scancode json and set output file name      
$ fosslight_convert -p [Path_of_scancode_json_files] -o [output_file_name_without_file_extension]       

<hr />     

## How to make a wheel file
$ python setup.py bdist_wheel
