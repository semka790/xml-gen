import xml.etree.ElementTree as ET

COUNT = str(input("Сколько строк нужно? "))


dec = ET.Element("dec", TypeName="ials21")

fiscCod = ET.SubElement(dec, "fiscCod")

fiscal = ET.SubElement(fiscCod, "fiscal")
fiscal.text = "1006600058053"
name = ET.SubElement(fiscCod, "name")
name.text = "CTIF"
datefisc = ET.SubElement(fiscCod, "datefisc")
cuatm = ET.SubElement(fiscCod, "cuatm")
cuatm.text = "0110"
fisc = ET.SubElement(fiscCod, "fisc")
fisc.text = "31"
caem = ET.SubElement(fiscCod, "caem")
nrinscr = ET.SubElement(fiscCod, "nrinscr")

nrinscr.text = COUNT
dataPrezent = ET.SubElement(fiscCod, "dataPrezent")

dinamicTable = ET.SubElement(dec, "dinamicTable")

for num in range(1, int(COUNT) + 1):
    row = ET.SubElement(dinamicTable, "row")
    row.set("line", str(num))
    number = ET.SubElement(row, "number")
    number.text = str(num)
    tinsalcds = ET.SubElement(row, "tinsalcds")
    namettl = ET.SubElement(row, "namettl")
    tinsotcds = ET.SubElement(row, "tinsotcds")
    codsurcdc = ET.SubElement(row, "codsurcdc")
    sumvencur = ET.SubElement(row, "sumvencur")
    nrluni = ET.SubElement(row, "nrluni")
    alpha3cod = ET.SubElement(row, "alpha3cod")
    sumscpcur = ET.SubElement(row, "sumscpcur")
    sumscmcur = ET.SubElement(row, "sumscmcur")
    sumscsmcur = ET.SubElement(row, "sumscsmcur")
    sumscncur = ET.SubElement(row, "sumscncur")
    sumschcur = ET.SubElement(row, "sumschcur")
    sumsctotcur = ET.SubElement(row, "sumsctotcur")
    summedcur = ET.SubElement(row, "summedcur")
    sumded2cur = ET.SubElement(row, "sumded2cur")
    sumimpcur = ET.SubElement(row, "sumimpcur")

totalRow = ET.SubElement(dinamicTable, "totalRow")

ventotcur = ET.SubElement(totalRow, "ventotcur")
scpcur = ET.SubElement(totalRow, "scpcur")
scmcur = ET.SubElement(totalRow, "scmcur")
scsmcur = ET.SubElement(totalRow, "scsmcur")
scncur = ET.SubElement(totalRow, "scncur")
schcur = ET.SubElement(totalRow, "schcur")
sctotcur = ET.SubElement(totalRow, "sctotcur")
medcur = ET.SubElement(totalRow, "medcur")
ded2cur = ET.SubElement(totalRow, "ded2cur")
impreticur = ET.SubElement(totalRow, "impreticur")

GroupsummContr = ET.SubElement(dec, "GroupsummContr")
summContr = ET.SubElement(GroupsummContr, "summContr")

director = ET.SubElement(dec, "director")
director_two = ET.SubElement(director, "director")
contabil = ET.SubElement(director, "contabil")

dinamicTable2 = ET.SubElement(dec, "dinamicTable2")
row_two = ET.SubElement(dinamicTable2, "row")
row_two.set("line", "1")
number_two = ET.SubElement(row_two, "number")
number_two.text = "1"
tinang = ET.SubElement(row_two, "tinang")
tinpin = ET.SubElement(row_two, "tinpin")
tinpih = ET.SubElement(row_two, "tinpih")


mydata = ET.tostring(dec, encoding="unicode")
myfile = open(input("Имя файла: "), "w")
myfile.write(mydata)
