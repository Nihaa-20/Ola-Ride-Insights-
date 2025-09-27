# queries.py

# Dictionary of SQL queries
all_queries = {
    "1. Successful Bookings":
        "SELECT Booking_ID, Customer_ID, Date, Vehicle_Type, Booking_Value, Payment_Method FROM OLA_DataSet WHERE Booking_Status = 'Success';",

    "2. Average Ride Distance per Vehicle Type":
        "SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Ride_Distance FROM OLA_DataSet GROUP BY Vehicle_Type;",

    "3. Total Cancelled Rides by Customers":
        "SELECT Canceled_Rides_by_Customer, COUNT(*) AS Total FROM OLA_DataSet WHERE Canceled_Rides_by_Customer<>'NA' GROUP BY Canceled_Rides_by_Customer UNION ALL SELECT 'Total', COUNT(*) FROM OLA_DataSet WHERE Canceled_Rides_by_Customer<>'NA';",
 
    "4. Top 5 Customers by Rides":
        "SELECT Customer_ID, COUNT(Booking_ID) AS Total_Rides FROM OLA_DataSet GROUP BY Customer_ID ORDER BY Total_Rides DESC LIMIT 5;",

    "5. Rides cancelled by drivers due to personal and car-related issues":
        "SELECT Canceled_Rides_by_Driver, COUNT(*) AS Total FROM OLA_DataSet WHERE Canceled_Rides_by_Driver='Personal & Car related issue' GROUP BY Canceled_Rides_by_Driver;",

    "6. Max & Min Driver Ratings for Prime Sedan":
        "SELECT MAX(Driver_Ratings) AS Max_Rating, MIN(Driver_Ratings) AS Min_Rating FROM OLA_DataSet WHERE Vehicle_Type = 'Prime Sedan';",

    "7. Rides Paid via UPI":
        "SELECT Booking_ID, Customer_ID, Date, Booking_Value, Vehicle_Type FROM OLA_DataSet WHERE Payment_Method = 'UPI';",

    "8. Average Customer Rating per Vehicle Type":
        "SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Customer_Rating FROM OLA_DataSet GROUP BY Vehicle_Type;",

    "9. Total Booking Value of Successful Rides":
        "SELECT SUM(Booking_Value) AS Total_Booking_Value FROM OLA_DataSet WHERE Booking_Status = 'Success';",

    "10. Incomplete Rides with Reason":
        "SELECT Booking_ID, Customer_ID, Date, Incomplete_Rides_Reason FROM OLA_DataSet WHERE Incomplete_Rides='Yes' AND Incomplete_Rides_Reason<>'NA';"
}
