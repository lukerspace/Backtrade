create database fund;
create table arkeps(id int primary key auto_increment,
	date date not null,
    est int ,
    act int ,
    ticker varchar(24));
    