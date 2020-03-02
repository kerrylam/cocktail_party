--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: event_cocktails; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.event_cocktails (
    event_cocktail_id integer NOT NULL,
    event_id integer NOT NULL,
    cocktail_id integer NOT NULL
);


ALTER TABLE public.event_cocktails OWNER TO vagrant;

--
-- Name: event_cocktails_event_cocktail_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.event_cocktails_event_cocktail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_cocktails_event_cocktail_id_seq OWNER TO vagrant;

--
-- Name: event_cocktails_event_cocktail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.event_cocktails_event_cocktail_id_seq OWNED BY public.event_cocktails.event_cocktail_id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.events (
    event_id integer NOT NULL,
    name character varying(25) NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.events OWNER TO vagrant;

--
-- Name: events_event_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.events_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_event_id_seq OWNER TO vagrant;

--
-- Name: events_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.events_event_id_seq OWNED BY public.events.event_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying(25) NOT NULL,
    lname character varying(25) NOT NULL,
    username character varying(25) NOT NULL,
    email character varying(25) NOT NULL,
    password character varying(25) NOT NULL
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: event_cocktails event_cocktail_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.event_cocktails ALTER COLUMN event_cocktail_id SET DEFAULT nextval('public.event_cocktails_event_cocktail_id_seq'::regclass);


--
-- Name: events event_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events ALTER COLUMN event_id SET DEFAULT nextval('public.events_event_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: event_cocktails; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.event_cocktails (event_cocktail_id, event_id, cocktail_id) FROM stdin;
1	1	11005
2	2	11006
3	1	11004
4	4	11002
5	3	13200
6	1	12196
7	5	11000
8	6	16447
9	5	16963
10	1	11006
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.events (event_id, name, user_id) FROM stdin;
1	Favorites	1
2	Jon's 30th Birthday	1
3	4th of July Party	1
4	Amy's Birthday	1
5	Favorites	2
6	Cinco de Mayo	2
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, fname, lname, username, email, password) FROM stdin;
1	Kerry	Lam	kqlam21	kqlam21@gmail.com	123
2	John	Smith	jsmith	john@gmail.com	12345
\.


--
-- Name: event_cocktails_event_cocktail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.event_cocktails_event_cocktail_id_seq', 10, true);


--
-- Name: events_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.events_event_id_seq', 6, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_user_id_seq', 2, true);


--
-- Name: event_cocktails event_cocktails_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.event_cocktails
    ADD CONSTRAINT event_cocktails_pkey PRIMARY KEY (event_cocktail_id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (event_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: event_cocktails event_cocktails_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.event_cocktails
    ADD CONSTRAINT event_cocktails_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- Name: events events_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

