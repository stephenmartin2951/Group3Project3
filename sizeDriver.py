import visualizations as vis
import utils as utl

#Create Size DataFrames
PaperSizeDF = vis.createDataFrame('size/PaperMCPaperSize.csv')
BakkesSizeDF = vis.createDataFrame('size/bakkesmodorgBakkesModSDKSize.csv')

PaperSizeDF = utl.addDate(PaperSizeDF, "Date", "CleanDate")
PaperSizeDF = PaperSizeDF.drop("Date", axis=1)
PaperSizeDF = PaperSizeDF.groupby(["CleanDate"], as_index=False).mean()

BakkesSizeDF = utl.addDate(BakkesSizeDF, "Date", "CleanDate")
BakkesSizeDF = BakkesSizeDF.drop("Date", axis=1)
BakkesSizeDF = BakkesSizeDF.groupby(["CleanDate"], as_index=False).mean()



vis.createLineChart(PaperSizeDF, "CleanDate", "Size", "Date", "Size in KBs", "Historical Trend of Repo Size",True, 'repoSizeTrendPaper', 'sizeVis')
vis.createLineChart(BakkesSizeDF, "CleanDate", "Size", "Date", "Size in KBs", "Historical Trend of Repo Size",True, 'repoSizeTrendBakkes', 'sizeVis')

