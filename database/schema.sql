CREATE TABLE EPG(
  ACTOR CHARACTER VARYING(1024),
  CATEGORY CHARACTER VARYING(1024),
  CH_ID BIGINT NOT NULL,
  DESCR CHARACTER VARYING(8192),
  DIRECTOR CHARACTER VARYING(1024),
  DISPLAY_DURATION BIGINT,
  DURATION BIGINT,
  ID BIGINT PRIMARY KEY,
  LARR BIGINT,
  MARK_ARCHIVE BIGINT,
  MARK_MEMO BIGINT,
  MARK_REC BIGINT,
  NAME CHARACTER VARYING(8192),
  OPEN BIGINT,
  ON_DATE DATE,
  RARR BIGINT,
  REAL_ID CHARACTER VARYING(1024),
  START_TIMESTAMP BIGINT,
  STOP_TIMESTAMP BIGINT,
  T_TIME TIME,
  T_TIME_TO TIME,
  TIME TIMESTAMP,
  TIME_TO TIMESTAMP
);

CREATE TABLE RADIO(
  ID BIGINT PRIMARY KEY,
  NAME CHARACTER VARYING(8192),
  NUMBER BIGINT NOT NULL,
  CMD CHARACTER VARYING(8192),
  COUNT BIGINT,
  STATUS BIGINT,
  VOLUME_CORRECTION BIGINT,
  FAV BIGINT,
  RADIO BOOLEAN
);
