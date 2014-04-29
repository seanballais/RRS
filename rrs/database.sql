/* Initialize database(s) and table(s)   */
/*
CREATE TABLE Users(
	userid 				INTEGER PRIMARY KEY 	AUTOINCREMENT NOT NULL,
	username 			VARCHAR(255)	NOT NULL, 
	password 			VARCHAR(255)	NOT NULL,
	emailadd 			VARCHAR(255)	NOT NULL,
	user_privileges 	TEXT			NOT NULL, 
	firstname 			TEXT			NOT NULL,
	lastname 			TEXT			NOT NULL,
	middlename 			TEXT			NOT NULL
);
*/
/* Insert records */

insert into Users values(0,'admin','admin', 'sfballais123@gmail.com', 'super_admin', '', '', '');