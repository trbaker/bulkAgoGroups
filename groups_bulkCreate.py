from arcgis.gis import GIS
import csv

gis = GIS("https://<yourOrg>.maps.arcgis.com", "","")


with open('data/bulkGroups.csv') as csvfile:
    csv_f = csv.reader(csvfile)
    for row in csv_f:
        # see if group name already exists
        groupId = gis.groups.search('title:' + row[1])
        try:
            if groupId[0] is not None:
                print('group already exists: ', row[1], sep='')
        except:
            #create new group, add members, and change owner
            newgroup=gis.groups.create(title=row[1],
                tags = ['gis, gps'],
                description = 'description goes here ',
                snippet = 'snippet here ',
                access = row[0],
                is_invitation_only = 'False',
                )
            newgroup
            newowner=row[2].replace(" ", "")
            #print('-',newowner,'-')
            #newgroup.add_users(['username'])
            #newgroup.reassign_to(newowner)
            print("Successfully created group: ", row[1], sep='')


print('script complete')

