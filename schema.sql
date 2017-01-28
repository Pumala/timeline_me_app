CREATE TABLE customer (
    customer_id serial PRIMARY KEY,
    username text,
    password text,
    first_name text,
    last_name text,
    birthday date,
    joined date,
    bio text,
    avatar text,
);

CREATE TABLE auth_token (
    token_id text PRIMARY KEY,
    token_expires timestamp DEFAULT now() + interval '30 days'.
    customer_id integer REFERENCES customer (id)
);

CREATE TABLE moment (
    moment_id serial PRIMARY KEY,
    name text,
    started date,
    ended date,
    description text,
    customer integer REFERENCES customer (id)
);

CREATE TABLE picture (
    picture_id text PRIMARY KEY,
    moment_id integer REFERENCES moment (id)
);
