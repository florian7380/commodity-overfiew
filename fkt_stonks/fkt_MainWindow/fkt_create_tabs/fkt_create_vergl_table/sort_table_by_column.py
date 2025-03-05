from PyQt5.QtWidgets import QTableWidgetItem
import math

def sort_table_by_column(table, column):
    data = []
    for i in range(table.rowCount()):
        row_data = []
        # Get the row header text
        row_header = table.verticalHeaderItem(i).text() if table.verticalHeaderItem(i) else ""
        row_data.append(row_header)
        for j in range(table.columnCount()):
            item = table.item(i, j)
            # Safely handle empty or None items
            if item and item.text().strip():
                try:
                    value = float(item.text())
                except ValueError:
                    value = float("inf")  # Default to infinity for invalid data
            else:
                value = float("inf")
            row_data.append(value)
        data.append(row_data)
    
    # Sort the data by the clicked column
    sorted_data = sorted(data, key=lambda x: x[column + 1])
    
    # Update the vertical header labels
    headers = [row[0] for row in sorted_data]
    table.setVerticalHeaderLabels(headers)
    
    # Fill the table with sorted data
    for row_index, row in enumerate(sorted_data):
        values = row[1:]  # Skip the header
        for col_index, value in enumerate(values):
            if math.isinf(value):  # Restore empty cells for infinity values
                table.setItem(row_index, col_index, QTableWidgetItem(""))
            else:
                table.setItem(row_index, col_index, QTableWidgetItem(f"{value}"))