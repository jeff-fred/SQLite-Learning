import sqlite3
import data_management as d_m


# Generate grid on to frame
def generate_frame_grid(frame, totalRows, totalColumns):
    rows = 0
    while rows < totalRows+1:
        frame.rowconfigure(rows, weight=1)
        rows += 1

    columns = 0
    while columns < totalColumns:
        frame.columnconfigure(columns, weight=1)
        columns += 1


