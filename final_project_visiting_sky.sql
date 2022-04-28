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
 restaurant_cuisine_type ENUM ('South Asian', 'Thai', 'Dessert', 'Traditional British Food', 'Italian', 'Indian', 'Grill', 'American Diner', 'Vegan') not null,
 restaurant_dietary_options ENUM ('Vegetarian options', 'Vegan options', 'Vegetarian and Vegan options', 'Vegetarian, Vegan and Halal options', 'Vegetarian and Halal options'),
 food_affordablity varchar (100) not null);

 drop table restaurants; 

insert into restaurants values (1, 'Tiger Lily', '167 - 169 Thornbury Rd, Osterley TW7 4QG', 'Quite close to Sky Campus as it is 1.5 miles away which is a 5 minute drive or 15 minutes via Public transport', 'tigerlilyofosterley.co.uk', '', 'Delicious authentic Thai cuisine with a bar. A peaceful elegant restaurant with bamboo outdoor terrance.', 'Thai', 'Vegetarian and Vegan options',
'£10-38 depending on dishes'); 
insert into restaurants values (2, 'The Hare and Hounds' , 'Wyke Green, Osterely Lane, Isleworth TW7 5PR', 'Quite close to Sky Campus as it is 1.0 miles away which is a 4 minute drive or an 18 minute walk.', 'hareandhoundsosterley.co.uk', '', 'A Classic Pub with fantastic fireplaces filled with Candles and nice garden to enjoy during the summer.', 
'Traditional British food', 'Vegetarian options', '£15 - £30 depending on dishes');
insert into restaurants values (3, 'Terminal 6 Lounge & Bar', 'Osterely Park Hotel, 764 Great West Road, Isleworth TW7 5NA', 'Quite close to Sky Campus as it is 0.8 miles away which a 4 minute drive or a 12 minute walk', 'www.terminal6lounge.com', '', 'A delicious Indian restaurant with a magnificent tudor style building and a pub that is well known amongst the local community.', 
'Indian', 'Vegetarian Options', '£20 - £40 depending on dishes'); 
insert into restaurants values (4, 'Sahara Grill Hounslow', '101-105 High St, Hounslow TW3 1QT','Close to Sky Campus as it is 3.5 miles miles away which is a 14 minute drive or 26 minutes via Public transport.', 'www.saharagrill.co.uk/branches/saharagrillhounslow', '', 'With a stunning interior, sahara grill with a large range of grilled options and asian cuisine.', 'Grill', 'Vegetarian and Halal options', 
 '£15-£45 depending on dishes');
insert into restaurants values (5, 'Man vs Food', '42 Syon Lane, Isleworth TW7 5NQ', 'Very Close to Sky Campus as it is 0.3 miles away which is a 6 minte walk and a 2 minute drive.', 'www.manvsfoodlondon.co.uk' ,'', 'Up for an adventure? Man vs Food is your place! This American inspired diner have huge portions are designed to make you indulge and stop you in your tracks.', 'American Diner',
 'Vegetarian, Vegan and Halal options' , '£18 - £50 depending on dishes');
insert into restaurants values (6, 'Vegology ', '30 Bath Rd, Hounslow TW3 3EB', 'Close to Sky Campus as it is 2.8  miles away which is a 9 minute drive or 32 minutes via Public transport.', 'www.vegologyldn.com', '', 'Known for their scrumptious vegan and vegetarian dishes for breakfast, lunch and dinner!', 'Vegan', 'Vegetarian and Vegan options', '£7 - £20 depending on dishes');
insert into restaurants values (7, 'Farfesh Lounge', '1 Spur Rd, Isleworth TW7 5BD', 'Quite close to Sky Campus as it is 0.8 miles away which a 4 minute drive or a 16 minute walk.', 'www.farfeshlounge.co.uk', '', 'A relaxed hangout with tantalising italian cuisine and a touch of arabian nights with shisha.', 'Italian', 'Vegetarian options', '£20 - £40 depending on dishes');
insert into restaurants values (8, 'Creams cafe' , '7 High St, Hounslow TW3 1RH', 'Close to Sky Campus as it is 2.7 miles away which is a 13 minute drive or 32 minutes via Public transport.', 'www.creamscafe.co.uk', '', 'Delicious gelato, pancakes and waffles with cosy booths to choose from.', 'Dessert', 'Vegan Options', '£4 - £15 depending on dessert');
insert into restaurants values (9, 'Heavenly Desserts', 'Unit 19 High St, Quater TW3 1BQ', 'Close to Sky Campus as it is 2.7 miles away which is a 13 minute drive or 32 minutes via Public transport.', 'https://heavenlydesserts.co.uk/', '', 'A wide variety of gelato, waffles, hot drinks and delicious cold drinks to choose from. These desserts are truly heavenly.', 'Dessert', 'Vegan options', '£4 - £15 depending on dessert');
insert into restaurants values (10, 'Nirala', '224 Uxbridge Rd, Feltham TW13 5DL', 'Close to Sky Campus as it is 2.7 miles away which is a 10 minute drive or 26 minutes via Public transport.', 'www.niralafoods.com','', 'With so many south asian sweet treats to choose from, Nirala sweets brings authentic south asian desserts to London being freshly made.', 'Dessert', 'Vegan options', '£5 - £20 depending on dessert');
select * from restaurants;

create table outdoor_activities(
 id int primary key auto_increment,
 outdoor_name varchar (100) not null,
 outdoor_address varchar (1000) not null, 
 outdoor_website varchar (100) not null,
 outdoor_image longblob,
 outdoor_descriptions varchar(1000),
 outdoor_affordablity varchar (100) not null);

drop table outdoor_activities;

insert into outdoor_activities values (1 , 'National Trust - Osterely Park and House', 'Jersey Rd, Isleworth TW7 4RB, United Kingdom', 'https://www.nationaltrust.org.uk/osterley-park-and-house' , '', 'Stroll up the tree-lined drive, past the grazing Charolais cattle and you''d think you''re in the country, not urban Hounslow. Surrounded by gardens, park and farmland, Osterley is one of the last surviving country estates in London.',
'£13 - £20 - Depending on ticket type');
insert into outdoor_activities values (2, 'Syon Park', 'Brent Lea, Brentford TW8 8JF, United Kingdom', 'https://www.syonpark.co.uk/', '', 'Syon park is a historic park founded over 400 years ago. With Garden Centres and Conservatories, the park is well known for its preservation of wild life across the span of many years. Particularly on a summers day, this is one of local communities favourite places to be!', 
' £13.50 - £45 - Depending on ticket type');
insert into outdoor_activities values (3, 'Hanwell zoo' , 'Church Rd, London W7 3BP, United Kingdom', 'https://hanwellzoo.co.uk/', '', 'Hanwell Zoo is the perfect place for all animal lovers. where passion for animals, conservation and nature fills our little Zoo to the brim! Go Wild in West London.' , '£13 - £20 - Depending on ticket');
insert into outdoor_activities values (4, 'Kew Gardens' , 'Kew, Richmond, London, TW9 3AE.', 'https://www.kew.org/', '', 'Kew gardens is reported to be one of London''s most popular attractions and also a UNESCO World Heritage Site.','£5 - £25 - Depending on ticket type');
insert into outdoor_activities values (5, 'Puttstars harrow', 'St Georges Shopping Centre, Harrow HA1 1AS, United Kingdom' , 'https://www.puttstars.co.uk/harrow', '' , 'For some affordable fun, Puttstars is all about experience and of course immense fun. Whether it''s teamwork as a group, cheering over a hole in one, or supporting one another to putt over the bridge. Perfect for all ages!' , '£6-13 depending on ticket type');
insert into outdoor_activities values (6, 'The Merry Pedaller' , '14 Warren Road Twickenham, London TW2 7DL England', 'https://www.merrypedallerbiketours.co.uk/', '', 'Unique bike tours can enjoy 2 of the largest Royal Parks of London still full of deer, cycle River Thames routes to Hampton Court Palace or Windsor Castle or maybe sample traditional beer. Our tours link together or can be bespoke to suit your requirements, alternate dates 
can be requested for 4+ people, group discounts available we have 20 bikes and various childrens bikes too but more can be provided if needed!','£35 - £150  - Depending on ticket type');    
insert into outdoor_activities values (7, 'The London Stand Up Paddle Company', 'Water Lane Richmond, Richmond-upon-Thames TW9 1TH England,', 'https://www.standuppaddle.london/', '',  'Join in and get active outdoors with the added benefit of a full body workout. Stand Up Paddling (SUP) is perfect for those who love the water and some intense activity.', '£40 - £120 - depending on ticket type');
insert into outdoor_activities values (8, 'Twickenham Stadium' , 'Whitton Road Twickeham Stadium, Twickenham TW2 7BA England' , 'https://www.twickenhamstadium.com/', '', 'It is the world''s largest rugby union stadium, the second largest in the United Kingdom, behind Wembley Stadium, and the fourth largest in Europe. It is ultimately know as the home of Rugby.', '£25 - £190 - Depending on ticket');
insert into outdoor_activities values (9, 'World Rugby Museum', 'Stadium, 200 Whitton Rd, Twickenham TW2 7BA, United Kingdom', 'https://worldrugbymuseum.com/', '', 'The award-winning World Rugby Museum is the definitive home for everything and anything about rugby. Housing the world’s most prestigious collection of rugby memorabilia and offering memorable tours of the iconic stadium.', '£16.50 - £40 - Depending on ticket');
insert into outdoor_activities values (10, 'Tate Britain' , 'Millbank, London SW1P 4RG', 'https://www.tate.org.uk/visit/tate-britain', '', 'Tate Britain is the world centre for the understanding and enjoyment of British art and promotes interest in British art internationally. Unrivalled displays show the development of art in Britain from Tudor times to the present day.', '£20 - 80 - Depending on ticket');

select * from outdoor_activities ;

create table local_events( 
id int primary key auto_increment,
event_name varchar (100) not null,
event_location varchar (100) not null,
event_start_date date,
event_end_date date,
event_website varchar (100) not null,
event_image longblob ,
event_category varchar(100));

drop table local_events;

insert into local_events values (1, 'Pub in the park with Tom Kerridge', 'Chiswick House', '2022-09-02', '2022-09-04', 'https://www.pubintheparkuk.com/chiswick','', 'Food, Music');
insert into local_events values (2, 'Junction II Festival', 'Trent Park' ,' 2022-06-18' , '2022-06-19', 'https://www.junction2.london/festival', '', 'Music');
insert into local_events values (3, 'Christmas at Kew', 'Kew Gardens', '2022-11-16', '2023-01-08', 'https://www.kew.org/kew-gardens/whats-on/christmas', 'Activity');
insert into local_events values (4, 'Foodies Festival', 'Syon Park', '2022-06-03', '2022-06-05' , 'https://foodiesfestival.com/events/syon-park-london/' , '', 'Food / Music');
insert into local_events values (5, 'Enchanted Woodland', 'Syon Park', '2022-11-11', '2022-11-27', 'http://www.enchantedwoodland.com/', '', 'Activity');
insert into local_events values (6, 'A Humorous Affair-A Jubilee Family Activity', 'Hogarth House', '2022-06-02', '2022-06-02', 'https://hogarthshouse.org/events_exhibitions/family_jubilee2022/','', 'Activity');
insert into local_events values (7 , 'Open Mic Nights : Jubilee Special', 'Open Mic Nights : Jubilee Special', '2022-06-03', '2022-06-03', 'https://www.visitgunnersbury.org/whats-on/special-events/open-mic-nights-jubilee-special/', '', 'Comedy');
insert into local_events values (8, 'Waterworks Festival', 'Gunnersbury Park', '2022-09-17', '2022-09-17', 'https://ra.co/promoters/96536', '', 'Arts');
insert into local_events values (9, 'Duck Pond Market', 'Chiswick House', '2022-10-29', '2022-10-29', 'https://duckpondmarket.com/chiswick', '', 'Activity');
insert into local_events values( 10, 'Outdoor Theatre : Jungle Book', 'Osterley Park', '2022-08-05', '2022-08-05', 'https://www.nationaltrust.org.uk/osterley-park-and-house/whats-on', '', 'Theatre');

-- Tables left; into_london, recommendations and discounts
-- create table into_london
-- create table


