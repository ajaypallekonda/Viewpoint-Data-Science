SELECT name_table.Name, name_table.StudentID FROM name_table 
INNER JOIN mark_table on name_table.StudentID = mark_table.StudentID 
WHERE mark_table.Total_marks > (
    Select mark_table.Total_marks FROM mark_table WHERE StudentID = 'V002');