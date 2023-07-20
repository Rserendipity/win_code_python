create database if not exists member_words;

use member_words;

drop table if exists word;

create table word (
    id int primary key auto_increment,
    ch0 varchar(200),
    ch1 varchar(200),
    ch2 varchar(200),
    ch3 varchar(200),
    en0 varchar(200),
    en1 varchar(200),
    en2 varchar(200),
    en3 varchar(200)
);
