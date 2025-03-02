select * from bike_sales;

#1
select count(*) as Total_Bikes_Sold from bike_sales;

#2
select Brand, avg(Price_INR) as Average_Resale_Price 
from bike_sales
group by Brand
order by Average_Resale_Price DESC;

#3
select state, count(Resale_Price_INR) as Total_Sales
from bike_sales
group by state
order by Total_Sales DESC; 

#4
select Brand, Model, Mileage_km_l
from bike_sales
order by Mileage_km_l DESC
limit 5;

#5
select Fuel_Type, avg(Resale_Price_INR) as Average_Resale_Price
from bike_sales
group by Fuel_Type
order by Average_Resale_Price desc;

#6
select Owner_Type, count(*) as Count_of_Bikes
from bike_sales
group by Owner_Type
order by Count_of_Bikes DESC;

#7
select Year_of_Manufacture, count(*) as No_Of_Bikes
from bike_sales
group by Year_of_Manufacture
order by No_Of_Bikes desc;

#8
select City_Tier, avg(Resale_Price_INR) as Avg_Resale_Price
from bike_sales
group by City_Tier
order by Avg_Resale_Price;

#9
select count(*) as insured_bikes
from bike_sales
where Insurance_Status = 'Active';

#10
select Brand, avg(Resale_Price_INR) as Resale_Value
from bike_sales
group by Brand
order by Resale_Value
limit 5;

#11
select Fuel_Type, AVG(Avg_Daily_Distance_km) as Average_Daily_Distance
from bike_sales
group by Fuel_Type;

#12
select Seller_Type, Count(Seller_Type)
from bike_sales
group by Seller_Type;

#13
select Brand,Model,Engine_Capacity_cc
from bike_sales
where Engine_Capacity_cc > 200;

#14
select Year_of_Manufacture, avg(Resale_Price_INR) as AVG_Resale_Price
from bike_sales
group by Year_of_Manufacture;

#15
select Brand, Model, Mileage_km_l
from bike_sales
order by Mileage_km_l asc
limit 5;

#16
select State, AVG(Resale_Price_INR) as Resale_Value
from bike_sales
group by State;

#17
select Brand,Model,City_Tier
from bike_sales
where City_Tier='Tier 1';

#18
select Brand, Fuel_Type, avg(Price_INR) as Price
from bike_sales
group by Brand, Fuel_Type
Order by Price desc;

#19
select Brand, Model, Resale_Price_INR
from bike_sales
where Resale_Price_INR > 
(select avg(Resale_Price_INR) from bike_sales);

#20
select Year_of_Manufacture, count(*) as count
from bike_sales
group by Year_of_Manufacture
order by Year_of_Manufacture ASC;