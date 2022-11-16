The code extends the capability of CloudProvider by using two inheritance layers: one layer to add a convenience method for finding files, and one layer to create a default video storage access point for ACCloud.

a) Refactor this code so that it no longer uses inheritance, but relies on composition instead.

b) Refactor the code once more so that find_files is no longer dependent on the cloudengine package.