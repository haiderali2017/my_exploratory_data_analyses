## Tables
### Employee
|     Field      |     Data Type      |     Description                               |     Constraints    |
|----------------|--------------------|-----------------------------------------------|--------------------|
|     Emp_ID     |     INT            |     Unique row id.                            |     Primary Key    |
|     Name       |     Varchar(32)    |     Name of person                            |     NOT NULL       |
|     Address    |     Varchar(64)    |     Address of the person                     |     NOT NULL       |
|     Gender     |     Varchar(6)     |     Specific gender of that person            |     NOT NULL       |
|     BrID       |     INT            |     Associated branch id from Branch Table    |     Foreign Key    |

### Passenger
|     Field          |     Data Type      |     Description                       |     Constraints    |
|--------------------|--------------------|---------------------------------------|--------------------|
|     Ps_ID          |     INT            |     Passenger primary key             |     Primary Key    |
|     Name           |     Varchar(32)    |     Name of person                    |     NOT NULL       |
|     Address        |     Varchar(64)    |     Address of the person             |     NOT NULL       |
|     Gender         |     Varchar(6)     |     Specific gender of that person    |     NOT NULL       |
|     Nationality    |     Varchar(16)    |     Nationality of the person         |     NOT NULL       |

### Employee_Contact
|     Field          |     Data Type      |     Description                        |     Constraints     |
|--------------------|--------------------|----------------------------------------|---------------------|
|     Emp_ID         |     INT            |     Employee ID from employee table    |     Foreign key     |
|     Cell_No        |     INT            |     Cell phone number                  |     NOT NULL        |
|     Email          |     Varchar(50)    |     Email of the employee              |     NOT NULL        |
|     Gender         |     Varchar(6)     |     Specific gender of that person     |     NOT NULL        |
|     Nationality    |     Varchar(16)    |     Nationality of the person          |     NOT NULL        |
