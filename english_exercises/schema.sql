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

drop table if exists MultiQuestion;
create table MultiQuestion(
  id integer primary key autoincrement,
  category text not null,
  level text not null,
  questionstring text not null,
  openanswer text not null,
  choiceanswer integer not null,
);

drop table if exists MultiQuestionAnswer;
create table MultiQuestionAnswer(
  id integer primary key autoincrement,
  user text foreign key not null,
  givenoanswer text not null,
  givenchoiceanswer integer not null
);