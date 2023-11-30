BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"UserID"	varchar(20),
	"Email"	varchar(50),
	"Password"	varchar(30),
	"FirstName"	varchar(50),
	"LastName"	varchar(50),
	"Address"	varchar(50),
	"City"	varchar(50),
	"State"	varchar(50),
	"Zipcode"	int,
	"Payment"	varchar(30),
	PRIMARY KEY("UserID")
);
CREATE TABLE IF NOT EXISTS "Inventory" (
	"ISBN"	INTEGER,
	"Name"	TEXT,
	"Quantity"	INTEGER,
	"Price"	REAL,
	PRIMARY KEY("Name")
);
CREATE TABLE IF NOT EXISTS "Shopping Cart" (
	"userID"	TEXT,
	"ISBN"	INTEGER,
	"Quantity"	INTEGER
);
INSERT INTO "Users" VALUES ('Jaw1321','Jaw1321@msstate.edu','password','Justin','Whitt','123 Main St','Springfield','CA',12345,'Visa');
INSERT INTO "Users" VALUES ('Ple132','testuser@mail.com','wrongword','Dave','Johnson','456 Oak Avenue','Riverside','NY',98765,'Mastercard');
INSERT INTO "Users" VALUES ('jfl234','emily.d@example.com','thisone','adam','Davis','789 Pine Street','Oakville','TX',54321,'Discover Card');
INSERT INTO "Users" VALUES ('lke234','michael.anderson@email.com','Wowzers2','Jim','Anderson','321 Elm Road','Lakeside','FL',87654,'American Express');
INSERT INTO "Users" VALUES ('delta555','sarah.b@example.net','DeltaPass#555','Sarah','Brown','555 Cedar Lane','Meadowville','AZ',43210,'PayPal');
INSERT INTO "Users" VALUES ('klg572','email.com','pass','kanyan','gressett','123 fart','chunky','MS',39323,'visa');
INSERT INTO "Inventory" VALUES (446310786,'To Kill a Mockingbird',20,5.99);
INSERT INTO "Inventory" VALUES (399501487,'Lord of the Flies',25,9.99);
INSERT INTO "Inventory" VALUES (451208633,'The Divine Comedy',32,6.99);
INSERT INTO "Inventory" VALUES (348756129,'1984',12,6.99);
INSERT INTO "Inventory" VALUES (140177396,'Of Mice and Men',16,4.99);
INSERT INTO "Inventory" VALUES (123479872,'The Great Gatsby',23,5.99);
INSERT INTO "Inventory" VALUES (783506528,'The Hobbit',19,10.99);
INSERT INTO "Inventory" VALUES (276497543,'The Outsiders',25,5.99);
INSERT INTO "Inventory" VALUES (724925613,'Pride and Prejudice',28,12.99);
INSERT INTO "Inventory" VALUES (387592341,'Moby-Dick',35,4.99);
INSERT INTO "Inventory" VALUES (927435210,'War and Peace',29,7.99);
INSERT INTO "Inventory" VALUES (257692210,'The Odyssey',24,5.99);
INSERT INTO "Inventory" VALUES (204658216,'The Illiad',21,5.99);
INSERT INTO "Inventory" VALUES (7438216,'The Scarlet Letter',28,11.99);
INSERT INTO "Inventory" VALUES (729720019,'Jane Eyre',18,5.99);
INSERT INTO "Inventory" VALUES (269798521,'The Catcher in the Rye',23,12.99);
INSERT INTO "Inventory" VALUES (250159638,'The Brothers Karamazov',35,5.99);
INSERT INTO "Inventory" VALUES (165939801,'Brave New World',17,9.99);
INSERT INTO "Inventory" VALUES (234895011,'The Trial',27,6.99);
INSERT INTO "Inventory" VALUES (435901458,'Middlemarch',22,4.99);
COMMIT;
