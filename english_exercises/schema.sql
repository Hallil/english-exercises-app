drop table if exists entries;
create table OpenQuestions (
  id integer primary key autoincrement,
  category text not null,
  level text not null,
  question text not null,
  answer text not null,
);
