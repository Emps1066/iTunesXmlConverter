from datetime import datetime
from xml.etree import ElementTree

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


def setFirstInsertLine():
    insertStatement = "INSERT INTO table_name (TrackID, Name, Artist, AlbumArtist, Genre, Kind, Size, TotalTime, " \
                      "TrackNumber, Year, DateModified, DateAdded, BitRate, SampleRate, PlayCount, SkipCount, Rating," \
                      "ArtworkCount, Location)"
    return insertStatement


# TODO finish algorithm
# TODO remove unwanted commas
def convertXMLDataToSqlStatement():
    trackList = createTrackList()
    print("track list obtained")
    masterInsertStatement = "\nVALUES "
    for song in trackList:
        insertStatementLine = "( "
        songKeys = song.keys()
        for tag in importantTags:
            if tag in songKeys:
                insertStatementLine = insertStatementLine + '"' + song.get(tag) + '", '
            else:
                insertStatementLine = insertStatementLine + "NULL, "
        insertStatementLine = insertStatementLine + "),\n"
        masterInsertStatement = masterInsertStatement + insertStatementLine
    return masterInsertStatement


# TODO reformat this method
def createTrackList():

    finalList = []
    with open("XMLFiles/ITUNES-Convert.xml", 'r') as xmlFile:
        print("=================================")
        tree = ElementTree.parse(xmlFile)
        root = tree.getroot()
        dictRoot = root.findall('dict')
        for item in list(dictRoot[0]):
            if item.tag == "dict":
                tracksDict = item
                break
        trackList = list(tracksDict.findall('dict'))
        print(trackList[3000][3].text)
        for i in range(len(trackList)):
            dictTemp = {}
            for j in range(len(trackList[i])):
                if trackList[i][j].tag == 'key':
                    dictTemp[trackList[i][j].text] = trackList[i][j+1].text
            finalList.append(dictTemp)
    return finalList


def convertSqlStatementIntoTxt(fileName, insertStatement):
    file = open(fileName, 'w+')
    sqlScript = setFirstInsertLine() + insertStatement
    file.write(sqlScript)
    file.write("\n")
    file.close()


def main():
    fileName = createTxtFile()
    insertStatement = convertXMLDataToSqlStatement()
    convertSqlStatementIntoTxt(fileName, insertStatement)
    print("Itunes library has successfully being converted into sql")


if __name__ == "__main__":
    main()
