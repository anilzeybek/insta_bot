--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2021-03-20 01:18:47

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
-- TOC entry 200 (class 1259 OID 24635)
-- Name: blacklist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blacklist (
    account text,
    request_declined integer,
    blacklist_date date DEFAULT now(),
    client_id bigint NOT NULL
);


ALTER TABLE public.blacklist OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 24692)
-- Name: blacklist_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.blacklist_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blacklist_client_id_seq OWNER TO postgres;

--
-- TOC entry 3067 (class 0 OID 0)
-- Dependencies: 209
-- Name: blacklist_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.blacklist_client_id_seq OWNED BY public.blacklist.client_id;


--
-- TOC entry 208 (class 1259 OID 24684)
-- Name: clients; Type: TABLE; Schema: public; Owner: goeku
--

CREATE TABLE public.clients (
    id bigint NOT NULL,
    email character varying(200) NOT NULL,
    password character varying(200) NOT NULL
);


ALTER TABLE public.clients OWNER TO goeku;

--
-- TOC entry 207 (class 1259 OID 24682)
-- Name: clients_id_seq; Type: SEQUENCE; Schema: public; Owner: goeku
--

CREATE SEQUENCE public.clients_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clients_id_seq OWNER TO goeku;

--
-- TOC entry 3068 (class 0 OID 0)
-- Dependencies: 207
-- Name: clients_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: goeku
--

ALTER SEQUENCE public.clients_id_seq OWNED BY public.clients.id;


--
-- TOC entry 201 (class 1259 OID 24642)
-- Name: dm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dm (
    sender_account text,
    sent_account text,
    message text,
    dm_date date DEFAULT now(),
    client_id bigint NOT NULL
);


ALTER TABLE public.dm OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 24701)
-- Name: dm_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dm_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dm_client_id_seq OWNER TO postgres;

--
-- TOC entry 3069 (class 0 OID 0)
-- Dependencies: 210
-- Name: dm_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dm_client_id_seq OWNED BY public.dm.client_id;


--
-- TOC entry 202 (class 1259 OID 24649)
-- Name: dm_profiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dm_profiles (
    profile_name text,
    dm_message text,
    client_id bigint NOT NULL
);


ALTER TABLE public.dm_profiles OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 24710)
-- Name: dm_profiles_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.dm_profiles_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dm_profiles_client_id_seq OWNER TO postgres;

--
-- TOC entry 3070 (class 0 OID 0)
-- Dependencies: 211
-- Name: dm_profiles_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.dm_profiles_client_id_seq OWNED BY public.dm_profiles.client_id;


--
-- TOC entry 203 (class 1259 OID 24655)
-- Name: follow_requests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.follow_requests (
    requester_account text,
    requested_account text,
    accepted integer,
    declined integer,
    request_date date DEFAULT now(),
    client_id bigint NOT NULL
);


ALTER TABLE public.follow_requests OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 24719)
-- Name: follow_requests_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.follow_requests_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.follow_requests_client_id_seq OWNER TO postgres;

--
-- TOC entry 3071 (class 0 OID 0)
-- Dependencies: 212
-- Name: follow_requests_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.follow_requests_client_id_seq OWNED BY public.follow_requests.client_id;


--
-- TOC entry 204 (class 1259 OID 24662)
-- Name: likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.likes (
    liker_account text,
    liked_account text,
    like_date date DEFAULT now(),
    client_id bigint NOT NULL
);


ALTER TABLE public.likes OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 24728)
-- Name: likes_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.likes_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.likes_client_id_seq OWNER TO postgres;

--
-- TOC entry 3072 (class 0 OID 0)
-- Dependencies: 213
-- Name: likes_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.likes_client_id_seq OWNED BY public.likes.client_id;


--
-- TOC entry 205 (class 1259 OID 24669)
-- Name: summary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.summary (
    summary_id text NOT NULL,
    account text,
    sent_likes integer,
    sent_requests integer,
    sent_dm integer,
    end_date date DEFAULT now(),
    client_id bigint NOT NULL
);


ALTER TABLE public.summary OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 24737)
-- Name: summary_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.summary_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.summary_client_id_seq OWNER TO postgres;

--
-- TOC entry 3073 (class 0 OID 0)
-- Dependencies: 214
-- Name: summary_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.summary_client_id_seq OWNED BY public.summary.client_id;


--
-- TOC entry 206 (class 1259 OID 24676)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    account text,
    client_id bigint NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 24746)
-- Name: users_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_client_id_seq OWNER TO postgres;

--
-- TOC entry 3074 (class 0 OID 0)
-- Dependencies: 215
-- Name: users_client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_client_id_seq OWNED BY public.users.client_id;


--
-- TOC entry 2900 (class 2604 OID 24694)
-- Name: blacklist client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.blacklist ALTER COLUMN client_id SET DEFAULT nextval('public.blacklist_client_id_seq'::regclass);


--
-- TOC entry 2911 (class 2604 OID 24687)
-- Name: clients id; Type: DEFAULT; Schema: public; Owner: goeku
--

ALTER TABLE ONLY public.clients ALTER COLUMN id SET DEFAULT nextval('public.clients_id_seq'::regclass);


--
-- TOC entry 2902 (class 2604 OID 24703)
-- Name: dm client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dm ALTER COLUMN client_id SET DEFAULT nextval('public.dm_client_id_seq'::regclass);


--
-- TOC entry 2903 (class 2604 OID 24712)
-- Name: dm_profiles client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dm_profiles ALTER COLUMN client_id SET DEFAULT nextval('public.dm_profiles_client_id_seq'::regclass);


--
-- TOC entry 2905 (class 2604 OID 24721)
-- Name: follow_requests client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.follow_requests ALTER COLUMN client_id SET DEFAULT nextval('public.follow_requests_client_id_seq'::regclass);


--
-- TOC entry 2907 (class 2604 OID 24730)
-- Name: likes client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.likes ALTER COLUMN client_id SET DEFAULT nextval('public.likes_client_id_seq'::regclass);


--
-- TOC entry 2909 (class 2604 OID 24739)
-- Name: summary client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.summary ALTER COLUMN client_id SET DEFAULT nextval('public.summary_client_id_seq'::regclass);


--
-- TOC entry 2910 (class 2604 OID 24748)
-- Name: users client_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN client_id SET DEFAULT nextval('public.users_client_id_seq'::regclass);


--
-- TOC entry 3046 (class 0 OID 24635)
-- Dependencies: 200
-- Data for Name: blacklist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blacklist (account, request_declined, blacklist_date, client_id) FROM stdin;
\.


--
-- TOC entry 3054 (class 0 OID 24684)
-- Dependencies: 208
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: goeku
--

COPY public.clients (id, email, password) FROM stdin;
1	ghvn01@gmail.com	password
2	ghvn03@gmail.com	$2b$10$Zph1yQaxmjD1n1cg9w550eu1200cx8Madl3U4WsvS409SUKGuWIQ2
3	ghvn04@gmail.com	$2b$10$MMYpyzlpot0EPQ59/l3DvudHtXM.aPWZ5LPgwykPTjc2tA90pQLO6
4	g@gmail.com	$2b$10$yr/ctiyTai8dLEIHFfsRZ.ZA5d1b5XjSg5fZ1tZcJWBXbs7.SRW3u
\.


--
-- TOC entry 3047 (class 0 OID 24642)
-- Dependencies: 201
-- Data for Name: dm; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dm (sender_account, sent_account, message, dm_date, client_id) FROM stdin;
\.


--
-- TOC entry 3048 (class 0 OID 24649)
-- Dependencies: 202
-- Data for Name: dm_profiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dm_profiles (profile_name, dm_message, client_id) FROM stdin;
asdasd	asdasd	4
\.


--
-- TOC entry 3049 (class 0 OID 24655)
-- Dependencies: 203
-- Data for Name: follow_requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.follow_requests (requester_account, requested_account, accepted, declined, request_date, client_id) FROM stdin;
\.


--
-- TOC entry 3050 (class 0 OID 24662)
-- Dependencies: 204
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.likes (liker_account, liked_account, like_date, client_id) FROM stdin;
\.


--
-- TOC entry 3051 (class 0 OID 24669)
-- Dependencies: 205
-- Data for Name: summary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.summary (summary_id, account, sent_likes, sent_requests, sent_dm, end_date, client_id) FROM stdin;
\.


--
-- TOC entry 3052 (class 0 OID 24676)
-- Dependencies: 206
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (account, client_id) FROM stdin;
\.


--
-- TOC entry 3075 (class 0 OID 0)
-- Dependencies: 209
-- Name: blacklist_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.blacklist_client_id_seq', 1, false);


--
-- TOC entry 3076 (class 0 OID 0)
-- Dependencies: 207
-- Name: clients_id_seq; Type: SEQUENCE SET; Schema: public; Owner: goeku
--

SELECT pg_catalog.setval('public.clients_id_seq', 4, true);


--
-- TOC entry 3077 (class 0 OID 0)
-- Dependencies: 210
-- Name: dm_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dm_client_id_seq', 1, false);


--
-- TOC entry 3078 (class 0 OID 0)
-- Dependencies: 211
-- Name: dm_profiles_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.dm_profiles_client_id_seq', 1, false);


--
-- TOC entry 3079 (class 0 OID 0)
-- Dependencies: 212
-- Name: follow_requests_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.follow_requests_client_id_seq', 1, false);


--
-- TOC entry 3080 (class 0 OID 0)
-- Dependencies: 213
-- Name: likes_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.likes_client_id_seq', 1, false);


--
-- TOC entry 3081 (class 0 OID 0)
-- Dependencies: 214
-- Name: summary_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.summary_client_id_seq', 1, false);


--
-- TOC entry 3082 (class 0 OID 0)
-- Dependencies: 215
-- Name: users_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_client_id_seq', 1, false);


--
-- TOC entry 2913 (class 2606 OID 24691)
-- Name: clients clients_email_key; Type: CONSTRAINT; Schema: public; Owner: goeku
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_email_key UNIQUE (email);


--
-- TOC entry 2915 (class 2606 OID 24689)
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: goeku
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (id);


-- Completed on 2021-03-20 01:18:47

--
-- PostgreSQL database dump complete
--

