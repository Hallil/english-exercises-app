drop table if exists OpenQuestions;
create table OpenQuestions(
  id integer primary key autoincrement,
  category text not null,
  level text not null,
  question text not null,
  answer text not null
);

drop table if exists users;
create table users(
  id integer primary key autoincrement,
  username text not null UNIQUE,
  password text not null,
  correct text not null,
  incorrect text not null
);
