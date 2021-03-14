--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blacklist; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.blacklist (
    account text,
    request_declined integer,
    blacklist_date date DEFAULT now()
);


--
-- Name: dm; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.dm (
    sender_account text,
    sent_account text,
    message text,
    dm_date date DEFAULT now()
);


--
-- Name: dm_profiles; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.dm_profiles (
    profile_name text,
    dm_message text
);


--
-- Name: follow_requests; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.follow_requests (
    requester_account text,
    requested_account text,
    accepted integer,
    declined integer,
    request_date date DEFAULT now()
);


--
-- Name: likes; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.likes (
    liker_account text,
    liked_account text,
    like_date date DEFAULT now()
);


--
-- Name: summary; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.summary (
    summary_id text NOT NULL,
    account text,
    sent_likes integer,
    sent_requests integer,
    sent_dm integer,
    end_date date DEFAULT now()
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: anilzeybek
--

CREATE TABLE public.users (
    account text
);


--
-- Data for Name: blacklist; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.blacklist (account, request_declined, blacklist_date) FROM stdin;
\.


--
-- Data for Name: dm; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.dm (sender_account, sent_account, message, dm_date) FROM stdin;
\.


--
-- Data for Name: dm_profiles; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.dm_profiles (profile_name, dm_message) FROM stdin;
yeni	Butiğimizdeki ürünleri ve mağazamızdaki indirimleri kaçırmayın
yeni	Sayfamıza göz atmış mıydınız?
\.


--
-- Data for Name: follow_requests; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.follow_requests (requester_account, requested_account, accepted, declined, request_date) FROM stdin;
niyazitecik	prn487	0	0	2021-03-08
niyazitecik	eroya.i	0	0	2021-03-08
\.


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.likes (liker_account, liked_account, like_date) FROM stdin;
niyazitecik	songul_igneoyalar52	2021-03-08
\.


--
-- Data for Name: summary; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.summary (summary_id, account, sent_likes, sent_requests, sent_dm, end_date) FROM stdin;
2b372b18-eac1-417c-9318-31c31fd2d037	niyazitecik	1	2	0	2021-03-08
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: anilzeybek
--

COPY public.users (account) FROM stdin;
efsane_mutfaklar
reklamimantep
alma_pie
nurseninnmutfagi
samira.ghorbani987
\.


--
-- Name: summary summary_pkey; Type: CONSTRAINT; Schema: public; Owner: anilzeybek
--

ALTER TABLE ONLY public.summary
    ADD CONSTRAINT summary_pkey PRIMARY KEY (summary_id);


--
-- Name: users users_account_key; Type: CONSTRAINT; Schema: public; Owner: anilzeybek
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_account_key UNIQUE (account);


--
-- PostgreSQL database dump complete
--

