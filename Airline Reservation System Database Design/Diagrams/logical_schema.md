## Tables
### Employee
|     Field      |     Data Type      |     Description                               |     Constraints    |
|----------------|--------------------|-----------------------------------------------|--------------------|
|     Emp_ID     |     INT            |     Unique row id.                            |     Primary Key    |
|     Name       |     Varchar(32)    |     Name of person                            |     NOT NULL       |
|     Address    |     Varchar(64)    |     Address of the person                     |     NOT NULL       |
|     Gender     |     Varchar(6)     |     Specific gender of that person            |     NOT NULL       |
|     BrID       |     INT            |     Associated branch id from Branch Table    |     Foreign Key    |
