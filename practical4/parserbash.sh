#bash script to parse through all blast XML files, taking only the top hit from each file.


cd blasthits

for element in *.xml

do python3 ../newtrialparser.py $element

done