create database fund;

use fund;

create table arkeps(id int primary key auto_increment,
	date date not null,
    est float4 ,
    act float4 ,
    ticker varchar(24) not null);