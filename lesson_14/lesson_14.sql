create table users(
id BIGINT auto_increment primary key,
username VARCHAR(50) not null unique,
password VARCHAR(255) not null,
email VARCHAR(255) not null unique);

create table seller(
id BIGINT auto_increment primary key,
company VARCHAR(150) not null unique,
phone VARCHAR(20) not null);

create table products(
id BIGINT auto_increment primary key,
name VARCHAR(150) not null,
cost DECIMAL(10,2) not null,
count INT not null,
seller_id BIGINT not null,
foreign key (seller_id) references seller(id));

create table orders(
id BIGINT auto_increment primary key,
user_id BIGINT not null,
product_id BIGINT not null,
count INT not null,
foreign key (user_id) references users(id),
foreign key (product_id) references products(id)
);

