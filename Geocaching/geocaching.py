import xlsxwriter

#create file (workbook) and worksheet
outWorkbook = xlsxwriter.Workbook('C:/Users/I538909/Desktop/out.xlsx')
outSheet = outWorkbook.add_worksheet()
c = 2

#declare data
lat = ["S 38° 51.669", "N 46° 18.790", "N 33° 46.152", "N 51° 03.299", "N 49° 00.975", "N 61° 12.903", "S 22° 38.313", "N 43° 43.434", "N 53° 16.090", "N 24° 50.977"]
longt = [ "E 000° 56.641", "W 045° 30.169", "E 016° 27.645", "E 121° 32.967", "E 012° 44.139", "E 006° 58.658", "W 074° 05.549", "E 175° 46.677", "W 149° 15.980", "E 132° 47.903"]

#write header
outSheet.write("B1", "Koordinaten")
outSheet.write("C1", "Location")
outSheet.write("D1", "Mögliches Paar?")

outSheet.set_column(1,1,30)
outSheet.set_column(3,3,15)

#write data to file

for i in range(0, len(lat)):
    for j in range(0, len(longt)):
        outSheet.write("B" + str(c) , lat[i] + " " + longt[j])
        c = c + 1

outWorkbook.close()