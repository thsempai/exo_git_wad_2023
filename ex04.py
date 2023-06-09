from openpyxl import load_workbook, Workbook

def get_first_non_empty(workbook):
    sheet = workbook.active

    for row in sheet.rows:
        for cell in row:
            if cell.value is not None:
                return cell.coordinate

Workbook.get_first_non_empty = get_first_non_empty

wb = load_workbook("test_if3.xlsx")
print(wb.get_first_non_empty())


