create database if not exists member_words;

use member_words;

drop table if exists users;

create table users (
    id int primary key auto_increment,
    user_name varchar(50) unique key,
    user_passwd varchar(50),
    current_plan int,
    goal_plan int,
    is_pause boolean
);
