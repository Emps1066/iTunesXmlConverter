from datetime import datetime
from xml.etree import ElementTree
import unittest
import os


def createTxtFile():
    fileCreationDate = datetime.now()
    sqlFileName = "sqlInserts/" + fileCreationDate.strftime("%m-%d-%Y, %H:%M:%S") + ".txt"
    f = open(sqlFileName, "w+")
    f.close()
    return sqlFileName


def setFirstInsertLine(fileName):
    file = open(fileName, 'w+')
    insertStatement = "INSERT INTO table_name (TrackID, Name, Artist, AlbumArtist, Genre, Kind, Size, TotalTime, " \
                      "TrackNumber, Year, DateModified, DateAdded, BitRate, SampleRate, PlayCount, SkipCount, Rating," \
                      "ArtworkCount, Location)"
    file.write(insertStatement)
    file.write("\n")
    file.close()


def convertXMLDataToSqlLines(fileName):
    trackList = getTrackList()
    print("track list obtained")
    print(str(len(trackList)))

def seperatePlaylistsFromTracks():
    print("===========================")


def getTrackList():
    with open("XMLFiles/ITUNES-Convert.xml", 'r') as xmlFile:
        print("=================================")
        tree = ElementTree.parse(xmlFile)
        root = tree.getroot()
        mainDict = root.findall('dict')
        for item in list(mainDict[0]):
            if item.tag == "dict":
                tracksDict = item
                break
        trackList = list(tracksDict.findall('dict'))
    return trackList


class TestConverter(unittest.TestCase):
    def test_add(self):
        fileName = createTxtFile()
        self.assertTrue(open(fileName, 'r'))
        self.tearDown(os.remove(fileName))


def main():
    fileName = createTxtFile()
    setFirstInsertLine(fileName)
    convertXMLDataToSqlLines(fileName)


if __name__ == "__main__":
    main()
