import xlrd

class getData():
    def ReadData(self, path):
        workbook = xlrd.open_workbook(path)   # 获取execl路径
        sheetData = workbook.sheets()[0]      # 获取execl数据
        rows = sheetData.row_values(0)[1]     # 获取execl列数据()是行，[]是列
        cols = sheetData.col_values(1)[0]     # （）是列，[]是行

        return rows, cols
