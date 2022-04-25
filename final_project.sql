create database if not exists visiting_sky;

use visiting_sky;

create table sky_campus( 
id int primary key auto_increment,
campus_name varchar(50) not null, 
campus_location varchar(100) not null);

drop table sky_campus;
 
 
 create table restaurants( 
 id int primary key auto_increment,
 restaurant_name varchar(100) not null, 
 restaurant_address varchar(100) not null, 
 restaurant_location varchar(1000), 
 restaurant_website varchar (100),
 restaurant_image longblob, 
 restaurant_description longtext,
 cusisine_type enum( 'Asian','Italian','Dessert','Other') not null);

insert into restaurants values (1, 'Tiger Lily', '167 - 169 Thornbury Rd, Osterley TW7 4QG', 'Quite close to Sky Campus as it is 1.5 miles away which is a 5 minute drive or 15 minutes via Public transport', 'tigerlilyofosterley.co.uk','', 'Delicious authentic Thai cuisine with a bar. A peaceful elegant restaurant with bamboo outdoor terrance.', 'Asian'); 

select * from restaurants
