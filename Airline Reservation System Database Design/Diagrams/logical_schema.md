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

### Countries
|     Field          |     Data Type      |     Description                   |     Constraints    |
|--------------------|--------------------|-----------------------------------|--------------------|
|     CtID           |     INT            |     Unique row id.                |     Primary Key    |
|     CountryName    |     Varchar(32)    |     Room to store country name    |     NOT NULL       |

### State
|     Field        |     Data Type      |     Description                         |     Constraints    |
|------------------|--------------------|-----------------------------------------|--------------------|
|     StID         |     INT            |     Unique row id.                      |     Primary Key    |
|     StateName    |     Varchar(32)    |     State name will take place here.    |     NOT NULL       |
|     CtID         |     INT            |     Country id                          |     Foreign Key    |

### City
|     Field        |     Data Type      |     Description       |     Constraints    |
|------------------|--------------------|-----------------------|--------------------|
|     StID         |     INT            |     Unique row id.    |     Foreign Key    |
|     City_name    |     Varchar(32)    |     Name of city      |     Primary Key    |

### AirLine
|     Field             |     Data Type      |     Description                    |     Constraints    |
|-----------------------|--------------------|------------------------------------|--------------------|
|     Airline_name      |     Varchar(32)    |     Name of the Airline company    |     Primary Key    |
|     No_of_branches    |     Int            |     Branches of a specific         |     NOT NULL       |

### Branch
|     Field           |     Data Type      |     Description                                   |     Constraints     |
|---------------------|--------------------|---------------------------------------------------|---------------------|
|     BrID            |     INT            |     Unique id for each branches                   |     Primary Key     |
|     City_name       |     Varchar(32)    |     Name of city                                  |     Foreign Key     |
|     Airline_name    |     Varchar(32)    |     Name of airline to   which aircraft belong    |     Foreign Key     |
|     Branch_type     |     Varchar(16)    |     Branch Type head office or   branch           |     NOT NULL        |
|     Address         |     Varchar(32)    |     Address of the branch                         |     NOT NULL        |
|     StID            |     INT            |     State ID from state table                     |     Foreign Key     |

### AirCraft
|     Field           |     Data Type       |     Description                                 |     Constraints     |
|---------------------|---------------------|-------------------------------------------------|---------------------|
|     AcID            |     INT             |     Specific ID of that Air Craft.              |     Primary Key     |
|     Airline_name    |     Varchar(32)     |     Name of airline to which aircraft belong    |     Foreign Key     |
|     Capacity        |     INT             |     No. of seats available.                     |     NOT NULL        |
|     MfdBy           |     Varchar(128)    |     Manufacturing company.                      |     NOT NULL        |
|     MfdOn           |     DATETIME        |     Manufactured date of aircraft.              |     NOT NULL        |
|     BrID            |     INT             |     Unique Branch ID form branch                |     Foreign key     |

### Route
|     Field          |     Data Type       |     Description                            |     Constraints    |
|--------------------|---------------------|--------------------------------------------|--------------------|
|     RouteID        |     INT             |     Stores unique row id.                  |     Primary Key    |
|     City_name      |     Varchar(32)     |     From where the flight will take off    |     Foreign Key    |
|     Destination    |     Varchar (32)    |     Flight destinations.                   |     NOT NULL       |
|     AcID           |     INT             |     Specific ID of that   Air Craft.       |     Foreign Key    |

### TravelClass
|     Field              |     Data Type       |     Description                                     |     Constraints    |
|------------------------|---------------------|-----------------------------------------------------|--------------------|
|     Travel_Class_ID    |     INT             |     Unique id.                                      |     Primary Key    |
|     Name               |     Varchar(45)     |     Name of travelling class.                       |     NOT NULL       |
|     SeatID             |     INT             |     Specific seat ID of that travelling   class.    |     NOT NULL       |
|     Description        |     Varchar(100)    |     Description of that travelling class.           |     NOT NULL       |
|     AcID               |     INT             |     PK from AirCraft   table.                       |     Primary Key    |

### Flight_Schedule
|     Field         |     Data Type    |     Description                                            |     Constraints    |
|-------------------|------------------|------------------------------------------------------------|--------------------|
|     Flight_ID     |     INT          |     Unique number to identify the flight.                  |     Primary Key    |
|     FlightDate    |     DATETIME     |     Date of flight.                                        |     NOT NULL       |
|     Departure     |     TIME         |     Stores the departure time of flight.                   |     NOT NULL       |
|     Arrival       |     TIME         |     Stores the arrival time of flight on   destination.    |     NOT NULL       |
|     RouteID       |     INT          |     Stores unique row id.                                  |     Foreign Key    |

### FlightStatus
|     Field        |     Data Type       |     Description                                            |     Constraints    |
|------------------|---------------------|------------------------------------------------------------|--------------------|
|     Flight_ID    |     INT             |     Flight id from flight table                            |     Foreign key    |
|     F_Status     |     Varchar(120)    |     If scheduled flight is either delayed or   on time.    |     NOT NULL       |
