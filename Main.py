from datetime import datetime
from xml.etree import ElementTree

importantTags = ['TrackID', 'Name', 'Artist', 'Album Artist', 'Composer' 'Genre', 'Kind', 'Size', 'Total Time',
                 'Track Number', 'Year', 'Date Modified', 'Date Added', 'Bit Rate', 'Sample Rate', 'Play Count',
                 'Skip Count', 'Rating',
                 'Artwork Count', 'Location']
UUID = False

def createTxtFile():
    fileCreationDate = datetime.now()
    sqlFileName = "sqlInserts/" + fileCreationDate.strftime("%m-%d-%Y, %H:%M:%S") + ".txt"
    f = open(sqlFileName, "w+")
    f.close()
    return sqlFileName


def setFirstInsertLine():
    if(UUID = True):
        insertStatement = "INSERT INTO table_name (TrackID, Name, Artist, AlbumArtist, " \
                          "Composer, Genre, Kind, Size, TotalTime, " \
                          "TrackNumber, Year, DateModified, DateAdded, BitRate, SampleRate, PlayCount, SkipCount, Rating," \
                          "ArtworkCount, Location)"
    insertStatement = "INSERT INTO table_name (TrackID, Name, Artist, AlbumArtist, " \
                      "Composer, Genre, Kind, Size, TotalTime, " \
                      "TrackNumber, Year, DateModified, DateAdded, BitRate, SampleRate, PlayCount, SkipCount, Rating," \
                      "ArtworkCount, Location)"
    return insertStatement


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
        insertStatementLine = insertStatementLine[:-2]
        insertStatementLine = insertStatementLine + "),\n"
        masterInsertStatement = masterInsertStatement + insertStatementLine
    masterInsertStatement = masterInsertStatement[:-2]
    return masterInsertStatement


# TODO allow user to choose file
def createTrackList():
    finalList = []
    with open("XMLFiles/ITUNES-Convert.xml", 'r') as xmlFile:
        tree = ElementTree.parse(xmlFile)
        root = tree.getroot()
        dictRoot = root.findall('dict')
        for item in list(dictRoot[0]):
            if item.tag == "dict":
                tracksDict = item
                break
        trackList = list(tracksDict.findall('dict'))
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

def enableUUIDFunctionality():
    val = input("Would you like to use UUID for this database? (Enter Y if yes else enter any other key:")
    if val == "y" or val == "Y":
        UUID = True
        print("UUID has being enabled")


def main():
    fileName = createTxtFile()
    enableUUIDFunctionality()
    insertStatement = convertXMLDataToSqlStatement()
    convertSqlStatementIntoTxt(fileName, insertStatement)
    print("Itunes library has successfully being converted into sql")


if __name__ == "__main__":
    main()
