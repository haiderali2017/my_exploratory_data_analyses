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

### Passenger_Contact
|     Field      |     Data Type      |     Description                          |     Constraints     |
|----------------|--------------------|------------------------------------------|---------------------|
|     Ps_ID      |     INT            |     Passenger ID from passenger table    |     Foreign key     |
|     Cell_No    |     INT            |     Cell phone number                    |     NOT NULL        |
|     Email      |     Varchar(50)    |     Email of the passenger               |     NOT NULL        |

### Booking Ticket
|     Field              |     Data Type    |     Description                                                                      |     Constraints    |
|------------------------|------------------|--------------------------------------------------------------------------------------|--------------------|
|     PsID               |     INT          |     Passenger id                                                                     |     Foreign Key    |
|     Emp_ID             |     INT          |     Employee id                                                                      |     Foreign Key    |
|     BrID               |     INT          |     Booking branch of passenger                                                      |     Foreign Key    |
|     Ticket_id          |     INT          |     ID of ticket                                                                     |     Primary Key    |
|     BookingDate        |     Date         |     Keeps the booking date.                                                          |     NOT NULL       |
|     BookingTime        |     Time         |     The time of flight                                                               |     NOT NULL       |
|     Flight_ID          |     INT          |     Flight number, a PK of Flight_Schedule to determine flying details & costs.    |     Foreign Key    |
|     Travel_Class_ID    |     INT          |     Provides the information of travelling   class of the passengers.                |     Foreign Key    |
|     Net_Fare           |     Float(20)    |     Total amount                                                                     |     Foreign Key    |

### Air Fare
|     Field              |     Data Type    |     Description                              |     Constraints    |
|------------------------|------------------|----------------------------------------------|--------------------|
|     PsID               |     INT          |     PK from passenger                        |     Foreign Key    |
|     Travel_Class_ID    |     INT          |     Unique id.                               |     Foreign Key    |
|     Flight_ID          |     INT          |     Unique number to identify the flight.    |     Foreign Key    |
|     Fare               |     INT          |     Stores service charge amount.            |     NOT NULL       |
|     F_SC               |     INT          |     Stores fuel surcharge amount.            |     NOT NULL       |
|     Net_Fare           |     Float(20)    |     Total amount                             |     Primary Key    |

### Cancellation
|     Field          |     Data Type    |     Description                                 |     Constraints    |
|--------------------|------------------|-------------------------------------------------|--------------------|
|     PsID           |     INT          |     Passenger primary key                       |     Foreign Key    |
|     Emp_ID         |     INT          |     Unique row id.                              |     Foreign Key    |
|     Flight_ID      |     INT          |     Unique number to identify the flight.       |     Foreign Key    |
|     Cancel_id      |     INT          |     Cancellation of flight by passenger.        |     Primary Key    |
|     Cancel_time    |     Date/time    |     Time of flight cancellation by passenger    |     NOT NULL       |
|     Ticket_id      |     INT          |     ID of ticket                                |     NOT NULL       |

### Extension
|     Field        |     Data Type    |     Description                              |     Constraints    |
|------------------|------------------|----------------------------------------------|--------------------|
|     Ext_id       |     INT          |     Extension of flight by passenger.        |     Primary Key    |
|     Ext_time     |     Time         |     Extension time of flight                 |     NOT NULL       |
|     Ext_Date     |     date         |     Date of extenion                         |     NOT NULL       |
|     Flight_ID    |     INT          |     Unique number to identify the flight.    |     Foreign Key    |
|     PsID         |     INT          |     Passenger primary key                    |     Foreign Key    |
|     Emp_ID       |     INT          |     Unique row id.                           |     Foreign Key    |
|     Ticket_id    |     INT          |     ID of ticket                             |     NOT NULL       |
