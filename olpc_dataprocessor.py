import os
import glob
import csv
import sys
import string
import shutil
import sqlite3



#global stuff 
directory = "Providence/*"
gs = glob.glob("Providence/*")
gs = glob.glob(directory)

fields = ['activity','activity_id',
             'checksum','icon-color',
             'mime_type','mtime',
             'share-scope',
             'tags','timestamp',
             'title','title_set_by_user',
             'user','uid',
             'description','mountpoint']

all_fields = ['uid', 'buddies_id', 'fulltext', 'mtime', 'mountpoint', 'title', 'share-scope', 'tamtam_subactivity',
              'progress', 'preview', 'mime_type', 'activity_id', 'title_set_by_user','description', 'tags',
              'timestamp', 'bundle_id', 'ctime', 'checksum', 'buddies', 'zoom', 'keep', 'icon-color', 'activity']


class OLPCDataprocessor:

    def __init__(self,rootdir):
        self.rootdir = rootdir
        self.count = 0 
        self.records = [] 
        for (path,dirs,files) in os.walk(rootdir):
            if "metadata" in path:
                print (path)
                record = self.processFiles(path,files)
                record = self.formatRecord(record)
                self.records.append(record)
                self.count = self.count + 1
        self.writeOutput() 
        self.printStatistics()

    def getFileContent(self,path,f):
        if f in fields:
            path = os.path.join(path,f)
            fle = open(path)
            data= fle.read()
            if len(data.strip()) > 0: 
                return data
            else: 
                return "NO DATA"
        else:
            return f


    def formatRecord(self,record):
        fields_list = list(all_fields)
        new_record = [] 
        for field in fields_list:
            if field in record:
                new_record.append(record[field])
            else:
                new_record.append('NO_DATA')
        return new_record
   


    def processFiles(self,path,files):
        c = {} 
        for f in files:
            content = self.getFileContent(path,f)
            c[f] = content
        return c

    def writeOutput(self):
        first = True
        writer = csv.writer(open('output.csv', 'wb'), delimiter=',')
        for record in self.records:
            if first:
                writer.writerow(all_fields)
                first = False
            writer.writerow(record)


    def printStatistics(self):
        print("*****Results********") 
        print("Total metadata found: %s" %(self.count)) 
        print("Formatted data written to: %s" %('output.csv'))
        from pprint import pprint 
        pprint("Fields included:")
        pprint(all_fields)


                
if __name__ == "__main__":
    print (sys.argv)
    if len(sys.argv) >= 2: 
       rootdir = sys.argv[1]
       OLPCDataprocessor(rootdir)
       
    else:
        print "usage: olpc_dataprocessor.py  path olpc to log data root folder"
        
