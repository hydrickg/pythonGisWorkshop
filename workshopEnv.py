import arcpy, os, urllib, zipfile
from arcpy import env

url = 'https://dl.dropboxusercontent.com/u/17521862/WLIA_pythonclass_data.gdb.zip'
home = os.path.expanduser("~")
wd = home + '/pythonWorkshopWLIA2014'
fgdb = wd + '/WLIA_pythonclass_data.gdb'
env.workspace = fgdb

def refresh_data():
	if not os.path.exists(wd):
		os.makedirs(wd)
	urllib.urlretrieve(url, wd + '/data.zip')
	f = open(wd + '/data.zip', 'rb')
	z = zipfile.ZipFile(f)
	for name in z.namelist():
		z.extract(name, wd)
	f.close()
	os.remove(wd + '/data.zip')

refresh_data()

feature_classes = arcpy.ListFeatureClasses()
rasters = arcpy.ListRasters()
datasets = feature_classes + rasters
roads = feature_classes[0]