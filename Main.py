from datetime import datetime
from xml.etree import ElementTree
import unittest
import os

importantTags = ['TrackID', 'Name', 'Artist', 'AlbumArtist', 'Genre', 'Kind', 'Size', 'TotalTime', " \
                      "'TrackNumber', 'Year', 'DateModified', 'DateAdded', 'BitRate', 'SampleRate', 'PlayCount',
                 'SkipCount', 'Rating', " \
                      "'ArtworkCount', 'Location']


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

#TODO finish algorithm
def convertXMLDataToSqlLines(fileName):
    trackList = createTrackList()
    print("track list obtained")
    for song in trackList:
        insertStatementLine = "("
        songKeys = song.keys()
        for tag in importantTags:
            if tag in songKeys:

            else:




# TODO reformat this method
def createTrackList():
    with open("XMLFiles/ITUNES-Convert.xml", 'r') as xmlFile:
        print("=================================")
        tree = ElementTree.parse(xmlFile)
        root = tree.getroot()
        dictRoot = root.findall('dict')
        for song in list(dictRoot[0]):
            if song.tag == "dict":
                tracksDict = song
                break
        trackList = list(tracksDict.findall('dict'))
        dictTemp = {}
        finalList = []
        for i in range(len(trackList)):
            for j in range(len(trackList[i])):
                if trackList[i][j].tag == "key":
                    dictTemp[trackList[i][j].text] = trackList[i][j + 1].text
            finalList.append(dictTemp)
        return finalList


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
