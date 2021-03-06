--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2021-03-07 00:29:46

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
-- TOC entry 203 (class 1259 OID 24611)
-- Name: blacklist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.blacklist (
    account text,
    request_declined integer,
    blacklist_date date DEFAULT now()
);


ALTER TABLE public.blacklist OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 24604)
-- Name: dm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dm (
    sender_account text,
    sent_account text,
    message text,
    dm_date date DEFAULT now()
);


ALTER TABLE public.dm OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 24597)
-- Name: follow_requests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.follow_requests (
    requester_account text,
    requested_account text,
    accepted integer,
    declined integer,
    request_date date DEFAULT now()
);


ALTER TABLE public.follow_requests OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 24590)
-- Name: likes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.likes (
    liker_account text,
    liked_account text,
    like_date date DEFAULT now()
);


ALTER TABLE public.likes OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 24618)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    account text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 3008 (class 0 OID 24611)
-- Dependencies: 203
-- Data for Name: blacklist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.blacklist (account, request_declined, blacklist_date) FROM stdin;
ozgekurdoglu	0	2021-02-11
gingeroses	0	2021-02-11
done_ozdal	0	2021-02-11
pilates_life_coaching_by_fatih	0	2021-02-15
figenadar	0	2021-02-15
gulnur.e	0	2021-02-15
cc.faces	0	2021-02-15
ayfer_ua	0	2021-02-15
busraperest	0	2021-02-16
serrasinasenocak	0	2021-02-16
anarch__woomen	0	2021-02-16
ilknura.34	0	2021-02-16
gzm_slmn	0	2021-02-16
akbasakgun	0	2021-02-16
sngl__on	0	2021-02-16
selenaysak	0	2021-02-16
neva.kutbay	0	2021-02-16
nurarboycoaching	0	2021-02-16
niluferaynaci	0	2021-02-16
serap.yalcinnn	0	2021-02-16
gamz.altunn	0	2021-02-16
milasirian	0	2021-02-16
emi.karaks	0	2021-02-16
aslidurgutciper	0	2021-02-16
satiyebuhan60	0	2021-02-16
haticedag3458	0	2021-02-16
serdarpavlov	0	2021-02-16
34hayatvar	0	2021-02-16
sertbaslale	0	2021-02-16
niluferkcebeci	0	2021-02-16
sevgidenizbirol	0	2021-02-16
kubrayldrm41	0	2021-02-16
serpilhy	0	2021-02-16
cigdemucuncu	0	2021-02-16
husniyedogrul	0	2021-02-16
nesibekantarci	0	2021-02-16
sennur.varlik	0	2021-02-17
ilhem_b_mina	0	2021-02-17
alyaspinkworld	0	2021-02-17
mer.vehasdemir	0	2021-02-17
nazan_atasayan	0	2021-02-17
gulsahuzuneryilmaz	0	2021-02-17
hlycl	0	2021-02-17
burcuondr_	0	2021-02-17
biyo_leyla	0	2021-02-17
fatmock	0	2021-02-17
buse.ozturkler	0	2021-02-17
svaricioglu	0	2021-02-17
ermlsl	0	2021-02-17
ozgemoztas	0	2021-02-17
arzuguzu	0	2021-02-17
gulnurmutlu	0	2021-02-17
drozgecan	0	2021-02-17
ysmykd	0	2021-02-17
larisalora5450	0	2021-02-17
leyylaylcn	0	2021-02-17
nagham_kurdi	0	2021-02-17
myagmurkarabulut	0	2021-02-17
yasemin_burunguz	0	2021-02-17
hulyaninellezzetleri36	0	2021-02-17
byrmdygask	0	2021-02-17
belkisbusra	0	2021-02-17
aynurka3057	0	2021-02-17
ayla_ckrkci	0	2021-02-17
sevilbinay	0	2021-02-17
maloxatxolmatova43	0	2021-02-17
elifmemis95	0	2021-02-17
karadeniz.guzeli.14	0	2021-02-17
zzeynpinan	0	2021-02-17
slcn_blgn	0	2021-02-17
han.gulseren	0	2021-02-17
gorkemgulbahcee	0	2021-02-17
ebruli_phibrows	0	2021-02-17
uzm.est.simalunsal	0	2021-02-17
bluediamondflower	0	2021-02-17
isabelzey_beauty	0	2021-02-17
beauty_handan	0	2021-02-17
guzel7974	0	2021-02-17
52.86.07.16	0	2021-02-17
2365.ra	0	2021-02-17
tcyurend	0	2021-02-17
fatma_sahin0363	0	2021-02-17
nacggytnzhy	0	2021-02-17
meryemkahramangngr	0	2021-02-17
nazcukur	0	2021-02-17
_songulyigitt	0	2021-02-17
gulen3752	0	2021-02-17
arzumentesoglu	0	2021-02-17
aydilge_byz	0	2021-02-17
burcinkaya97	0	2021-02-17
ecrenhsret	0	2021-02-17
pelinsimsekk16	0	2021-02-17
zubeydenarin1	0	2021-02-17
xo.baysel	0	2021-02-17
yagmurbldir	0	2021-02-17
gamzet4ks	0	2021-02-17
asyaozer948	0	2021-02-17
ozlemcalimli6	0	2021-02-17
busener19	0	2021-02-17
mervekuru324	0	2021-02-17
zuhalakinyuksel	0	2021-02-17
proxone.proxone	0	2021-02-17
melisss.sx14	0	2021-02-17
mertemkorkmaz	0	2021-02-17
nilufer5inci	0	2021-02-17
burcu72.79	0	2021-02-17
glhandarbaz	0	2021-02-17
elifdemirorn	0	2021-02-17
lady__birdss	0	2021-02-17
nilgungezer52	0	2021-02-17
purpleblogers	0	2021-02-17
meltem.topal34	0	2021-02-17
nesibe.basol	0	2021-02-17
fatos_kangalci	0	2021-02-17
akaraygun95	0	2021-02-17
asumanbaydarol	0	2021-02-17
safiye_muallime	0	2021-02-17
el_emeklerim24	0	2021-02-17
gunduzelibolaysegul	0	2021-02-17
d.bulak	0	2021-02-17
aysenyuncu	0	2021-02-17
sebnemacar	0	2021-02-17
nnniyannnn	0	2021-02-17
merve__kahveci	0	2021-02-17
tuba_toman34	0	2021-02-17
belgnyldrm	0	2021-02-17
olgaustuner	0	2021-02-17
burcutanoren	0	2021-02-17
_oz.ayd_an	0	2021-02-17
mukaddessycl	0	2021-02-17
hicran.onal	0	2021-02-17
neshemiyyy	0	2021-02-17
berrinde	0	2021-02-17
safranbolummmm	0	2021-02-17
yildirimzuhal	0	2021-02-17
sadiyeakcam	0	2021-02-17
gazelle1701	0	2021-02-17
erde.maktas	0	2021-02-17
55mzzezmn55	0	2021-02-17
gokcetepeee	0	2021-02-17
merlin.tapar	0	2021-02-17
senidaa	0	2021-02-17
asivak_turkey	0	2021-02-17
emeltoker55	0	2021-02-17
thezeynno	0	2021-02-17
lefkosa.gayrimenkul	0	2021-02-17
yagmursd	0	2021-02-17
dgecgel	0	2021-02-17
nisantasi.ozferahgida	0	2021-02-17
bozanx2763	0	2021-02-17
omertoksoz0	0	2021-02-17
gulinef	0	2021-02-17
the162458	0	2021-02-17
siaren.ect	0	2021-02-17
gulay.sarp	0	2021-02-17
birbuketpaptya	0	2021-02-17
i.i.cicen	0	2021-02-17
turkyillmazmeehtap	0	2021-02-17
askinnurkopkal	0	2021-02-17
morogata	0	2021-02-17
c.e_b_a_	0	2021-02-17
liyazonayakkabi	0	2021-02-17
bestami_bozkurt_4	0	2021-02-17
musakilincarslan	0	2021-02-17
the_professional_studio	0	2021-02-17
seyhaningunlugu	0	2021-02-17
kemal.aksz	0	2021-02-17
hatun_1983	0	2021-02-17
soffff91	0	2021-02-17
pointerturkiye52	0	2021-02-18
malaak_turko2	0	2021-02-18
oriflameeseval	0	2021-02-18
dark___angelll	0	2021-02-18
film_izlenir	0	2021-02-18
zeyneldamla_yrdmcl	0	2021-02-18
meftunnmavii	0	2021-02-18
singfiller.com.tr	0	2021-02-18
mukremin184	0	2021-02-18
feray_gnynk	0	2021-02-18
dr.nevriearif	0	2021-02-18
t.a.s.1982	0	2021-02-18
gulistan.ergin	0	2021-02-18
dry__clk92	0	2021-02-18
zu.leyha718	0	2021-02-18
arzuklk58	0	2021-02-18
dilarademirtasbeautystudio	0	2021-02-18
ayhanofficalz	0	2021-02-18
sevgul9640	0	2021-02-18
guzel.sevenadamlar	0	2021-02-18
ismailders	0	2021-02-18
avenuekalicioje.ist	0	2021-02-18
vldngkts	0	2021-02-18
mb.oe_	0	2021-02-18
doriauna.cole	0	2021-02-18
abyasarr	0	2021-02-18
serra_demirkan	0	2021-02-18
hulyaunsal1978	0	2021-02-18
wikanaz	0	2021-02-18
aysunemirtoprakk	0	2021-02-18
herbal.semo	0	2021-02-18
_kh_farangis_kh_	0	2021-02-18
hayallerimin_kirikligi	0	2021-02-18
mugeozkardes	0	2021-02-18
drarzuozgeneci	0	2021-02-18
medine.a	0	2021-02-18
34_love_	0	2021-02-18
ayla_yiildirim	0	2021-02-18
surucuozturk	0	2021-02-18
ayancan41	0	2021-02-18
ayse_utku__	0	2021-02-18
gunnuralkar	0	2021-02-18
sehnazsertbakan	0	2021-02-18
estetik_urunler_	0	2021-02-18
azat23478	0	2021-02-18
elifdenizlimanoglu	0	2021-02-18
dosthane0731	0	2021-02-18
birensevi	0	2021-02-18
aya_chernova	0	2021-02-18
gamzeguler_	0	2021-02-18
zubeydekalayci	0	2021-02-18
gulsahozgol	0	2021-02-18
edaat.s	0	2021-02-18
bykr_aylin	0	2021-02-18
yusufemirsancak	0	2021-02-18
sibelozgucsahin	0	2021-02-18
dsozdol	0	2021-02-18
hulyadige	0	2021-02-18
gamzebaraz	0	2021-02-18
bzygt_melek	0	2021-02-18
gulapnurdan	0	2021-02-18
68mari.sajadipour	0	2021-02-18
nasipselvi	0	2021-02-18
gizemygun	0	2021-02-18
srkblc77777	0	2021-02-18
niis_permanent_makeup	0	2021-02-18
m.ebadi1212	0	2021-02-18
bahar.fidan365	0	2021-02-18
mervealtayy_	0	2021-02-18
hilalakin182	0	2021-02-18
serrocan01	0	2021-02-18
ffatihh.7	0	2021-02-18
hurriyetrahsa	0	2021-02-18
esrataneraydin	0	2021-02-18
canankazakoglu	0	2021-02-18
caglaguvercinn	0	2021-02-18
_hamza_emir_78	0	2021-02-18
maria.iram3030	0	2021-02-18
elif_cicekci	0	2021-02-18
sebahat7526	0	2021-02-18
thelightoflaluna	0	2021-02-18
gulsah.akgul.akdag	0	2021-02-18
tuba_hacioglu	0	2021-02-18
elifertantaskin	0	2021-02-18
seygunesdede	0	2021-02-18
mehrnoosh.basiri	0	2021-02-18
kamilaolbrych	0	2021-02-18
hacer.albayrakdanaci	0	2021-02-18
senem.urhan	0	2021-02-18
tilbeakaslan	0	2021-02-18
wishisland27	0	2021-02-18
cocoandmiuu	0	2021-02-18
zeytinyagi10	0	2021-02-18
kcemrecakiroglu	0	2021-02-18
seher_kizilsoy	0	2021-02-18
aslinurcobann	0	2021-02-18
gozde.danismanlik	0	2021-02-18
zulfiya9542	0	2021-02-18
tarcin.klcoglu	0	2021-02-18
naide1903	0	2021-02-18
nimetgamzeatunc	0	2021-02-18
phlvnozlemyldrm	0	2021-02-18
fminell	0	2021-02-18
huriyekuscu	0	2021-02-18
busractinkya	0	2021-02-18
01no	0	2021-02-18
peyman.fulya	0	2021-02-18
tcgulaysozeri	0	2021-02-18
roba.isaa	0	2021-02-18
rumeysakru	0	2021-02-18
erennburcu___	0	2021-02-18
asli.buran.tuntas	0	2021-02-18
aysha_berhel	0	2021-02-18
zehra_urek	0	2021-02-18
mrv_mrr	0	2021-02-18
denizb.krt	0	2021-02-18
_melike__ozcann	0	2021-02-18
gzzdekayaa	0	2021-02-18
microblading_mariam	0	2021-02-18
gozdeyilmazbeauty	0	2021-02-18
bellebeautyclub	0	2021-02-18
aysel.azra2020	0	2021-02-18
apo_mannheim	0	2021-02-18
drdermiss	0	2021-02-18
rinoplastika.dr.asvari.javdani	0	2021-02-18
rencar_otomotiv	0	2021-02-18
feromen.fero	0	2021-02-18
emine_kuafor_17	0	2021-02-18
goldrenovation	0	2021-02-18
dolunay_officiall_cagla	0	2021-02-18
enejan_o	0	2021-02-18
motivasyonhome	0	2021-02-18
bulent.fera	0	2021-02-18
kilincdilek762	0	2021-02-18
tegemed	0	2021-02-18
mimitbeyy	0	2021-02-18
akanmuge	0	2021-02-18
illy9389	0	2021-02-18
zaferperformance	0	2021-02-18
deniz_spor.1	0	2021-02-18
dilanbilgin	0	2021-02-18
best_turkish_novels_	0	2021-02-18
gizem.karell	0	2021-02-18
emine_yesldag	0	2021-02-18
rojda_gun_	0	2021-02-18
gulcinguducu	0	2021-02-18
nazlimuserref	0	2021-02-18
vatansevercagla1	0	2021-02-18
onkdksmsjsj	0	2021-02-18
anaeva020	0	2021-02-18
dilancmkrtn	0	2021-02-18
ozlemosmnoglu	0	2021-02-18
buketofeklermehmet	0	2021-02-18
guzel_gunler__25_	0	2021-02-18
asligulustun	0	2021-02-18
meryymeteyigit	0	2021-02-18
ozlemyakisann	0	2021-02-18
milaskaaaa1310	0	2021-02-18
susmak_guzel__	0	2021-02-18
yagmursena19	0	2021-02-18
banuekrentas	0	2021-02-18
sedahn16	0	2021-02-18
hll_mina_dmr	0	2021-02-18
armenyapi	0	2021-02-18
aysun542021	0	2021-02-18
sultan.talii	0	2021-02-18
muge_kas_tasarm	0	2021-02-18
burcukoc_1	0	2021-02-18
selmaulu288690	0	2021-02-18
eylembanu	0	2021-02-18
capparr18	0	2021-02-18
nuraycinar_	0	2021-02-18
melih_gorkemli	0	2021-02-18
motoreferanss	0	2021-02-18
merve_ucar58	0	2021-02-18
umitaksu_	0	2021-02-18
tcaliyorulmaz	0	2021-02-18
ganoexcelturkiye45	0	2021-02-18
tugbayldran	0	2021-02-18
arjen.durms	0	2021-02-18
evyasamsunum	0	2021-02-18
shenay1983	0	2021-02-18
nerminnigre	0	2021-02-18
dilanhalisdemir	0	2021-02-18
kivancvatansever	0	2021-02-18
aysel_kipcak	0	2021-02-18
yelizyagmurcetin	0	2021-02-18
_neslihan_gs	0	2021-02-18
bebek.ekgida.tarifleri.dev	0	2021-02-18
fikretyildiz513	0	2021-02-18
izmirlove3545	0	2021-02-18
shapp.o	0	2021-02-18
arzu._arzum	0	2021-02-18
leylo.s68	0	2021-02-18
elif_bertug	0	2021-02-18
ksctgc	0	2021-02-18
atessebile	0	2021-02-18
sahibini7im	0	2021-02-18
aneshka32_	0	2021-02-18
aasenacetek	0	2021-02-18
nkrakovna	0	2021-02-19
emelpilatesanatomi	0	2021-02-19
ayseburcakt	0	2021-02-19
danielharrington482	0	2021-02-19
sarisoykader	0	2021-02-19
zerrin__sahin	0	2021-02-19
selmaozkan1	0	2021-02-19
i.alkhattab	0	2021-02-19
haticebahise	0	2021-02-19
nese_gorkem	0	2021-02-19
aysegulbalkaya4	0	2021-02-19
zulfiyelegoz	0	2021-02-19
jasmin.erdogan	0	2021-02-19
ozlemelifusluu	0	2021-02-19
esracakallikli	0	2021-02-19
murat1907fb1907	0	2021-02-19
moonlighttenten	0	2021-02-19
zeynepkavakk	0	2021-02-19
kareli8690	0	2021-02-19
yagmurboranaksu	0	2021-02-19
haticecavas	0	2021-02-19
aysunbekt	0	2021-02-19
mihrican_korucuoglu	0	2021-02-19
asliinna	0	2021-02-19
shabnam_shahidzadeh	0	2021-02-19
fusun_kayan	0	2021-02-19
poyraz_og	0	2021-02-19
tubahkngullu	0	2021-02-19
wdl.emir	0	2021-02-19
nwrlrhmn3058	0	2021-02-19
cemre.fan402	0	2021-02-19
minok0101	0	2021-02-19
r_95.a_96	0	2021-02-19
piinaaree	0	2021-02-19
ayakgaci	0	2021-02-19
sevvoland	0	2021-02-19
iremdulgar	0	2021-02-19
jasmin_3269	0	2021-02-19
gulten061	0	2021-02-19
ipekkirpik_malzeme_antalya	0	2021-02-19
phibrows_shiraz20	0	2021-02-19
serengull58	0	2021-02-19
sayara747	0	2021-02-19
gzmklvz	0	2021-02-19
organikolye	0	2021-02-19
bbrows_studio	0	2021-02-19
asliakn	0	2021-02-19
yasarakinci_25	0	2021-02-19
sunguaysun	0	2021-02-19
rose_tln_	0	2021-02-19
yaseminnyky	0	2021-02-19
gul_gul888	0	2021-02-19
su.ulusan	0	2021-02-19
karadeniz__kizi___	0	2021-02-19
atiyeasilturk	0	2021-02-19
kutlu_yeliz	0	2021-02-19
belek_murat	0	2021-02-19
bilgebozkurtttt	0	2021-02-19
tugba.syhkc	0	2021-02-19
beriilla	0	2021-02-19
neopinksoft	0	2021-02-19
selmabilgin123	0	2021-02-19
n_97ji	0	2021-02-19
nrnaln	0	2021-02-19
busseee_mm	0	2021-02-19
sevara_2363	0	2021-02-19
nuraydartar	0	2021-02-19
mayapernepesova	0	2021-02-19
sofi.ssweet	0	2021-02-19
gamze_tskrn_	0	2021-02-19
emlatlla	0	2021-02-19
aslihank	0	2021-02-19
yoksa_sen	0	2021-02-19
yelizdamyan2	0	2021-02-19
ilac_medicine	0	2021-02-19
guney_3801	0	2021-02-19
nevin_asli	0	2021-02-19
kahpelik_son_moda54	0	2021-02-19
hmzyigit	0	2021-02-19
toprak_su_0678	0	2021-02-19
hatice.yunusoglu	0	2021-02-19
ayseaskerler	0	2021-02-19
ozlemyalcinkya	0	2021-02-19
dilakrca	0	2021-02-19
makeupserpill	0	2021-02-19
umid.humbetov	0	2021-02-19
valiyevag	0	2021-02-19
dr__rafig	0	2021-02-19
elensu_halime	0	2021-02-19
zeynep.ayyildiz	0	2021-02-19
faatma.durmus	0	2021-02-19
essin.gny	0	2021-02-19
istegeldimburdayiim	0	2021-02-19
mylife35710	0	2021-02-19
hakankuyuofficial	0	2021-02-19
gunel6806	0	2021-02-19
botchednosey	0	2021-02-19
nilay.oztrk	0	2021-02-19
elcinsumer	0	2021-02-19
5858_fatos	0	2021-02-19
demirrozalin	0	2021-02-19
_hamza_atlan	0	2021-02-19
hatice_arslan_karakaplan	0	2021-02-19
toprakdekor38	0	2021-02-19
neslihan_cinar19	0	2021-02-19
haktekk	0	2021-02-19
marjinhairlab	0	2021-02-19
burcuukalp	0	2021-02-19
baraa_bachroui_85	0	2021-02-19
m_e_.m0	0	2021-02-19
hjimuradi	0	2021-02-19
_erkekescort.35	0	2021-02-19
charynovbatov	0	2021-02-19
pulsar72	0	2021-02-19
asumankorkmazz	0	2021-02-19
emarkalite	0	2021-02-19
eminebolearas	0	2021-02-19
dsportwomen	0	2021-02-19
nilhangurses	0	2021-02-19
benmanolya._	0	2021-02-19
pusicanta	0	2021-02-19
0nlinezoo	0	2021-02-19
merve.tnrkl	0	2021-02-19
duayentasarim	0	2021-02-19
zeynep_yahya_ebrar	0	2021-02-19
hatice_serbest77	0	2021-02-19
nankaemi	0	2021-02-19
altmanemir	0	2021-02-19
merve.aratemurofficial	0	2021-02-19
mirabeaute_nails	0	2021-02-19
elif.kerpc	0	2021-02-19
ayse_mlye	0	2021-02-19
gulvaryo78	0	2021-02-19
sgmelis	0	2021-02-19
gokce.erbil	0	2021-02-19
tusdatadusdatakonya	0	2021-02-19
cibirayfer	0	2021-02-19
kahve_molasii	0	2021-02-19
perabaskiatolyesi	0	2021-02-19
hacerhazarhun	0	2021-02-19
nesrin.abnz	0	2021-02-19
nkabill	0	2021-02-19
beyz_tur	0	2021-02-19
ugurlu_peruk	0	2021-02-19
annadellarte	0	2021-02-19
angay62	0	2021-02-19
canaralofficial	0	2021-02-19
sumaya_ashraf.18	0	2021-02-19
osama_429a	0	2021-02-19
edayakut93	0	2021-02-19
mrtok34	0	2021-02-19
emin08	0	2021-02-19
sehnaz_yesilyurt	0	2021-02-19
ransserie	0	2021-02-19
efdesign3d	0	2021-02-19
bellezza_pingmentation_turkiye	0	2021-02-19
cevahirhadi	0	2021-02-19
gamzebulu34	0	2021-02-19
kubziiim	0	2021-02-19
stefaniabelleimicroblading_pmu	0	2021-02-19
fotografkahvem	0	2021-02-19
pro_removerx	0	2021-02-19
aishanbeautycenter	0	2021-02-19
selda_akyurt	0	2021-02-19
palettasarimcom	0	2021-02-19
meralparlak1982	0	2021-02-19
uzm.psikolog.lale_hasanoglu	0	2021-02-19
nesrncetn	0	2021-02-19
mexrisha.93	0	2021-02-19
sema_tekin_tansever	0	2021-02-19
nikisvoronos	0	2021-02-19
aydogdunurgul2	0	2021-02-19
demiraysudemet	0	2021-02-19
kirmizitoprak_sponsorr	0	2021-02-21
canan__8186	0	2021-02-21
ferdak.der	0	2021-02-21
incdaily34	0	2021-02-21
ozkok.vc	0	2021-02-21
volcan_alavi	0	2021-02-21
hande.su20	0	2021-02-21
fatosekeen	0	2021-02-21
ozgul34	0	2021-02-21
wishlist_by_sez	0	2021-02-21
senayaralbulut	0	2021-02-21
gizemmmburak	0	2021-02-21
asli_yldizz	0	2021-02-21
bilbilaltyeva	0	2021-02-21
ucarseyda	0	2021-02-21
mimarsultan	0	2021-02-21
sabrinaas88	0	2021-02-21
ozlem_esaspehlivan	0	2021-02-21
fatmatlyeds	0	2021-02-21
duyges	0	2021-02-21
gulsum_ay	0	2021-02-21
nazli_yildiz65	0	2021-02-21
rossy.meza.10	0	2021-02-21
61haticek	0	2021-02-21
ecekkahraman	0	2021-02-21
halilibrahmkahraman	0	2021-02-21
meryemm.karabuga	0	2021-02-21
zynp_bulut	0	2021-02-21
ipek__kiprik	0	2021-02-21
gamzeakkaya57	0	2021-02-21
serenyusuf2017	0	2021-02-21
hantal14	0	2021-02-21
inci_cakici	0	2021-02-21
jyf01ghi	0	2021-02-21
sementa_71	0	2021-02-21
aydaam0zx	0	2021-02-21
melekyildizbeber	0	2021-02-21
cosmeticmeddevrim	0	2021-02-21
ttugbauzun	0	2021-02-21
zelish34_estetikmalzemeler	0	2021-02-21
yuksekserpil	0	2021-02-21
aslihan_ozturk_mira_oyku	0	2021-02-21
fitlifencnxnxnxmxnx	0	2021-02-21
giovanni_gkhznp_	0	2021-02-21
ozgur.karabacak.60	0	2021-02-21
fzt.nihankarakuzay	0	2021-02-21
begum_ozbay	0	2021-02-21
elitcarelazer	0	2021-02-21
yasmisaaaaaa	0	2021-02-21
burcukurl	0	2021-02-21
kirdokozlem	0	2021-02-21
hyilmazhy	0	2021-02-21
nazli.koc.20	0	2021-02-21
cgdm_gs	0	2021-02-21
smmm.fatma_cetinkaya	0	2021-02-21
iremgrcn	0	2021-02-21
em.y36	0	2021-02-21
_hilal.bakacak_	0	2021-02-21
dilekkrms	0	2021-02-21
shadi.aaraz	0	2021-02-21
elifcolak790	0	2021-02-21
arsaljarral09	0	2021-02-21
1__purple	0	2021-02-21
ysmnklsc	0	2021-02-21
ilayfic3	0	2021-02-21
gulsahokkk	0	2021-02-21
feridehusrev	0	2021-02-21
l4veenn	0	2021-02-21
setenaypeker	0	2021-02-21
marybrave84	0	2021-02-21
kadirkaya6929	0	2021-02-21
kaderacarx_	0	2021-02-21
neslihansungur	0	2021-02-21
roxykaleb	0	2021-02-21
ahmet_cihan_ay	0	2021-02-21
gokcakin	0	2021-02-21
sevimlekurabiyeler	0	2021-02-21
mervesabuncu17	0	2021-02-21
astiniofficial	0	2021-02-21
yalan_dunya_30_34	0	2021-02-21
yldzmine770	0	2021-02-21
ayse_81	0	2021-02-21
gulnursengl	0	2021-02-21
turkiye.kirpik.tirnak.malzeme	0	2021-02-21
mervecanbay7130	0	2021-02-21
parlakyildiz_merve	0	2021-02-21
kameliq_kamelota	0	2021-02-21
nevin.omer	0	2021-02-21
eezzoo_27	0	2021-02-21
hazalinyemekleri	0	2021-02-21
lemonn.flower	0	2021-02-21
fate8943	0	2021-02-21
safiyecihantokat	0	2021-02-21
gozdegrsoyy	0	2021-02-21
esg8289	0	2021-02-21
eli_ftemiz	0	2021-02-21
ozbrr	0	2021-02-21
sibel.5505	0	2021-02-21
kardelen.asmin	0	2021-02-21
emine_7750	0	2021-02-21
suzibasak	0	2021-02-21
fidandoqan	0	2021-02-21
selda.seven7	0	2021-02-21
karayalcinsafi	0	2021-02-21
kadercoskun	0	2021-02-21
meleksiimaaa	0	2021-02-21
nursunkosansu	0	2021-02-21
pinargumus82	0	2021-02-21
aycaorakburkek	0	2021-02-21
ozdngnyflbl	0	2021-02-21
snmylcn	0	2021-02-21
betulgolalancosu	0	2021-02-21
nhlhmrtblkr	0	2021-02-21
genomguzellik	0	2021-02-21
ergulesra.camoglu	0	2021-02-21
ntrpnn	0	2021-02-21
tansu.25	0	2021-02-21
arassayse	0	2021-02-21
seher.aliihsan	0	2021-02-21
berff46	0	2021-02-21
vatansevernecla	0	2021-02-21
meltem_meyra_miray	0	2021-02-21
eda_taser_torunbas	0	2021-02-21
tugbakeklik86	0	2021-02-21
kalpyarasi_yk	0	2021-02-21
fatmauzzunn	0	2021-02-21
eda.atmis	0	2021-02-21
sarikayaideal	0	2021-02-21
esragkce96	0	2021-02-21
gulten.karakas	0	2021-02-21
aleynasumer48	0	2021-02-21
miraors	0	2021-02-21
binnaz.erkan	0	2021-02-21
ozgurlenc__zeliha	0	2021-02-21
bircandemir475	0	2021-02-21
rana.aynur	0	2021-02-21
dilan_ekizz	0	2021-02-21
nurtengumrukcu	0	2021-02-21
nar.london	0	2021-02-21
ezel_hbo	0	2021-02-21
dilarayil91	0	2021-02-21
alevcsk81	0	2021-02-21
seher_khrmn	0	2021-02-21
azra_elifnur	0	2021-02-21
filiz_akman72	0	2021-02-21
sevda.genc.56	0	2021-02-21
sporyapfitolfitkal	0	2021-02-21
songuloztop	0	2021-02-21
busra.albayrak5829	0	2021-02-21
ferhanaltinbas	0	2021-02-21
cennet_nefes_yasamkocu	0	2021-02-21
esra_ctf	0	2021-02-21
efeaynadekorasyon	0	2021-02-21
seziyetkili	0	2021-02-21
gulsah_barut	0	2021-02-21
ffigenunlu	0	2021-02-21
sevalkarahan	0	2021-02-21
akyelhayriye	0	2021-02-21
mavi.beyaz.1334	0	2021-02-22
hana_enver_	0	2021-02-22
duygu_.kurt	0	2021-02-22
zorianagunesh	0	2021-02-22
tomrissuzan	0	2021-02-22
yvz_rahii	0	2021-02-22
nilaybayduraydin	0	2021-02-22
dry_bt	0	2021-02-22
jasminaa__jasminaa	0	2021-02-22
yenigulhatice	0	2021-02-22
this_lovex	0	2021-02-22
sibelpenso	0	2021-02-22
turkersule	0	2021-02-22
natalia_goddess_pmu	0	2021-02-22
crn_nr	0	2021-02-22
vvvv_designer	0	2021-02-22
pratikahsapkutu	0	2021-02-22
muhrata	0	2021-02-22
tati19812019	0	2021-02-22
sydney_p_parrish	0	2021-02-22
klcneriman	0	2021-02-22
gonulsargiin	0	2021-02-22
cezmiasci	0	2021-02-22
asim.dernek	0	2021-02-22
betulurucoglu	0	2021-02-22
sibel.gungor	0	2021-02-22
ruhuzehiirr	0	2021-02-22
idilkarakussss	0	2021-02-22
selmagungorhuner	0	2021-02-22
masalsozlerr	0	2021-02-22
iremtanyildiiz	0	2021-02-22
kubraa_saygii	0	2021-02-22
livegulsh	0	2021-02-22
tugba_yigit15	0	2021-02-22
elifffmercannn	0	2021-02-22
as_sibelkarabag	0	2021-02-22
sevdali8146	0	2021-02-22
____svdt___evn	0	2021-02-22
sedm.kaya	0	2021-02-22
sibel_akbal	0	2021-02-22
1burcuuozdemir	0	2021-02-22
reyhanylmazsevilmis	0	2021-02-22
omerenasaf_handemiraras	0	2021-02-22
simaysrll	0	2021-02-22
canansaglam54	0	2021-02-22
hulyabas00	0	2021-02-22
herbnuralsahin	0	2021-02-22
zouyayaalihaydar	0	2021-02-22
gulsmonal	0	2021-02-22
cgrdfnalan	0	2021-02-22
mehtapzehir	0	2021-02-22
selenmuge	0	2021-02-22
azbilinen	0	2021-02-22
dmlacanal	0	2021-02-22
butik___mai	0	2021-02-22
hndcsknr	0	2021-02-22
ilaydadonmezoglu	0	2021-02-22
mehmetttseddd	0	2021-02-22
betelgeusedonusumdanismanlik	0	2021-02-22
emineulusy755	0	2021-02-22
mhmtyksl06	0	2021-02-22
sedaakgun409	0	2021-02-22
svl_ydr	0	2021-02-22
aysenur_gunn	0	2021-02-22
fundagokesme	0	2021-02-22
nsamba.patrick.376	0	2021-02-22
gezemedigimden	0	2021-02-22
albina.khramova	0	2021-02-22
dr.burcuzabun	0	2021-02-22
sibelunal34	0	2021-02-22
dt.ulkukologlu	0	2021-02-22
temelcimuazzez	0	2021-02-22
santosredward	0	2021-02-22
camlicacini	0	2021-02-22
nur777829	0	2021-02-22
meral.trn	0	2021-02-22
asti_li_serriyamin	0	2021-02-22
eminegner37	0	2021-02-22
kosehasozdemir	0	2021-02-22
grbt_drl47	0	2021-02-22
arzukaradag1980	0	2021-02-22
yasmin_ye	0	2021-02-22
sacideoruc	0	2021-02-22
seda_sfrn	0	2021-02-22
leyla.oruc.372	0	2021-02-22
zafersogutcu	0	2021-02-22
esrkaradumann	0	2021-02-22
senayyde	0	2021-02-22
duygunun_tasarimlari34	0	2021-02-22
ozlembuy	0	2021-02-22
zumrutcum21	0	2021-02-22
baran_samir1695	0	2021-02-22
ilknur.aslan.ozer	0	2021-02-22
stylebaku_caffe	0	2021-02-22
tmydlny	0	2021-02-22
filizkayafilizz	0	2021-02-22
sukranyc	0	2021-02-22
fundaakdemir24	0	2021-02-22
miracsudemertcan	0	2021-02-22
ozlemyaman210	0	2021-02-22
tc_elnare_demir	0	2021-02-22
mayoshaa	0	2021-02-22
glsnbzky	0	2021-02-22
buket.kosar.1	0	2021-02-22
mehtapdeniz_58	0	2021-02-22
caglayankerem	0	2021-02-22
aydancvkl	0	2021-02-22
polly.keller.35	0	2021-02-22
ghyzlane_saphir	0	2021-02-22
bilir_ferda	0	2021-02-22
zzehraturkan	0	2021-02-22
gulseren.eker	0	2021-02-22
serenayccoban	0	2021-02-22
melismeteli	0	2021-02-22
mehresema	0	2021-02-22
ardaninpavyonu7	0	2021-02-22
ilknurdamar_official	0	2021-02-22
s.yilmaz	0	2021-02-22
ozoz.en	0	2021-02-22
makeuptg_	0	2021-02-22
atcasila	0	2021-02-22
kim_oldugumu_biliyorsun43	0	2021-02-22
phistudio_nj	0	2021-02-22
lbeyzapolat	0	2021-02-22
morbeyaz__	0	2021-02-22
zulalkann	0	2021-02-22
saharfooladii_phibrows	0	2021-02-22
dsnbusra	0	2021-02-22
oriflame_avon_prizren	0	2021-02-22
ferferi_shop21	0	2021-02-22
mervenuragir	0	2021-02-22
ketiholl	0	2021-02-22
mer.veozkan	0	2021-02-22
maliymsc	0	2021-02-22
kuafor.sevgii	0	2021-02-22
sibelyurdakull	0	2021-02-22
nesesaloglu	0	2021-02-22
visionary_vizyoner	0	2021-02-22
bli.nail	0	2021-02-22
nuranyurdan10	0	2021-02-22
yemek_zmn	0	2021-02-22
onyeomatony	0	2021-02-22
__gun_nlg	0	2021-02-22
mucankus	0	2021-02-22
sinemmkucukkk	0	2021-02-22
halil_buse_uzdemir_aydn	0	2021-02-22
busraoncel_	0	2021-02-22
eli_eli.howard	0	2021-02-22
tekmerv	0	2021-02-22
hamide_zumra_aydin	0	2021-02-22
soran.ogretmen	0	2021-02-22
sedadgn9401	0	2021-02-22
simplehappiness74	0	2021-02-22
knaile	0	2021-02-22
funda_alaadin	0	2021-02-22
sevvallelmasss	0	2021-02-22
nida0434	0	2021-02-22
yagmurebrarozyurt	0	2021-02-22
_selyrose	0	2021-02-22
selen_dogann	0	2021-02-22
emine_ozer_sari	0	2021-02-22
lezzetsekertiziouzou	0	2021-02-22
elinguzellik	0	2021-02-22
semra.tarar	0	2021-02-22
dencae	0	2021-02-22
belgin_aytemur_	0	2021-02-22
gulsennevzatt	0	2021-02-22
pinosha_pnr	0	2021-02-22
fatmasabuncu1903	0	2021-02-22
eylullrslnn	0	2021-02-22
minebektas23	0	2021-02-22
b.ewin	0	2021-02-22
yaprakgulseren	0	2021-02-22
babysharkcam	0	2021-02-22
gems_anotolia	0	2021-02-22
life_meuble	0	2021-02-22
wa.rd6435	0	2021-02-22
lucchesi_estetica	0	2021-02-22
vascularsocialworld	0	2021-02-22
ilaydayaslan	0	2021-02-22
kirpikmarketim1	0	2021-02-22
doruk_media	0	2021-02-22
hilalsngr	0	2021-02-22
emeltatayy	0	2021-02-22
gulbahar_gulsumm	0	2021-02-22
tiktokirpik	0	2021-02-22
karas_grouptr	0	2021-02-22
coktatliseyler_acibadem	0	2021-02-22
mygalacos69	0	2021-02-22
sedikahocaoglu	0	2021-02-22
cyd.brky.11	0	2021-02-22
poshlashmarket	0	2021-02-22
isimlikadresim	0	2021-02-22
nani_beauty_salon	0	2021-02-22
merkezi.n	0	2021-02-22
nursoltan_nnn	0	2021-02-22
sakuraliman	0	2021-02-22
ozturk2918_sezen_bayan_kuaforu	0	2021-02-22
serpil_ayar_guzellik_merkezi	0	2021-02-22
tuana_bayan_kuaforu1	0	2021-02-22
essra.tass	0	2021-02-22
osman.demr	0	2021-02-22
soulmateone	0	2021-02-22
helisderiveaksesuar	0	2021-02-22
maha_sabbah2015	0	2021-02-22
h.nn568	0	2021-02-22
namo_0009	0	2021-02-22
madamcarlotta	0	2021-02-22
sametkorkutt	0	2021-02-22
emine.ozturkkkkkk	0	2021-02-22
sayestee	0	2021-02-22
vedat_kaplan1903	0	2021-02-22
izieli_gitardersleri	0	2021-02-22
personal_buyer_europe_	0	2021-02-22
sedakirimm	0	2021-02-22
leilaallanazarova	0	2021-02-22
yanik5781	0	2021-02-22
vero.brows	0	2021-02-22
hayat_ek	0	2021-02-22
evasarlak	0	2021-02-22
next_babykids	0	2021-02-22
arina_zanash	0	2021-02-22
oya.canbaz	0	2021-02-22
sevcan_saman	0	2021-02-22
bslrwh6	0	2021-02-22
flowerbombbrows	0	2021-02-22
elita_elif	0	2021-02-22
naribanderin47	0	2021-02-22
betul.filiz_	0	2021-02-22
turkandadas	0	2021-02-22
lleilahuseyn	0	2021-02-22
aksudekor	0	2021-02-22
glyasl	0	2021-02-22
gokcetrndrms	0	2021-02-22
yareen.u1	0	2021-02-22
tolga.aykutt	0	2021-02-22
hemelsgumruk	0	2021-02-22
ibrahimatci47	0	2021-02-22
yudumakpinar7	0	2021-02-22
sukran_bozturk	0	2021-02-22
yummy_time_by_s	0	2021-02-22
beyzanur.efe	0	2021-02-22
rus_dili_istanbul	0	2021-02-22
plastica_2021_	0	2021-02-22
celik_yaseminn	0	2021-02-22
aysu_gul	0	2021-02-22
beyhan_3458	0	2021-02-22
evininanasi	0	2021-02-22
matthiew_hector_garza	0	2021-02-22
tyg.birgul	0	2021-02-22
ipek_gecmen	0	2021-02-22
pasazade_mert	0	2021-02-22
feray.kuyu	0	2021-02-22
simruyarenoncel	0	2021-02-22
fatoszenginnn	0	2021-02-22
ulgoesokmelzo	0	2021-02-22
busra_akvardar	0	2021-02-22
nejlakiskac	0	2021-02-22
asy_saricam	0	2021-02-22
buketcil	0	2021-02-22
________dilek_____________	0	2021-02-22
kubrakkarakus	0	2021-02-22
capten__mohammed77	0	2021-02-22
mrycann80	0	2021-02-22
ikrardabahar	0	2021-02-22
serenaskar	0	2021-02-22
hadiyebayraktar	0	2021-02-22
muallademirel	0	2021-02-22
vildanfeimovaa	0	2021-02-22
mira2712db	0	2021-02-22
baharylmzak	0	2021-02-22
melis_yildizel	0	2021-02-22
hcrkrtt	0	2021-02-22
kaanazizkrsdudu	0	2021-02-22
songul.ozerenler.73	0	2021-02-22
nagehan_emre_akkurt	0	2021-02-22
dygnrs	0	2021-02-22
rsl.lsltny	0	2021-02-22
doganay_leyla_	0	2021-02-22
brfndgn29	0	2021-02-22
b__4110	0	2021-02-22
aleynaffan	0	2021-02-22
akblkarzu	0	2021-02-22
ssiirevii	0	2021-02-22
melle_yasmin	0	2021-02-22
aziza.9426	0	2021-02-22
yarenymkkk	0	2021-02-22
naz_unal	0	2021-02-22
yildiznida_	0	2021-02-22
orhanatay7373	0	2021-02-22
bengul_cokuk	0	2021-02-22
dlnavsr	0	2021-02-22
dry.elanr	0	2021-02-22
avec17avec	0	2021-02-22
aybigehazel	0	2021-02-22
silvahanife	0	2021-02-22
sevcan_kaba	0	2021-02-22
farm.asikozmetik	0	2021-02-22
sahra_okcu	0	2021-02-22
yagmurazizekaratas	0	2021-02-22
ybiberoglu	0	2021-02-22
nuranyilmaz34	0	2021-02-22
perihansahin0	0	2021-02-22
selinmerl	0	2021-02-22
serapergul63	0	2021-02-22
_fashion_addict._	0	2021-02-22
ebruardaa	0	2021-02-22
01_omer_0101	0	2021-02-22
emineakarr6034	0	2021-02-22
esraamarangoz	0	2021-02-22
aykuterkut1985	0	2021-02-22
cilem.saglam	0	2021-02-22
ferayeslin	0	2021-02-22
sehriban_eris	0	2021-02-22
deryaacek	0	2021-02-22
mervee_kalkan	0	2021-02-22
crnyyldrm	0	2021-02-22
minikk.papatya	0	2021-02-22
baroyadair	0	2021-02-22
zahidearslan01	0	2021-02-22
asli.cem	0	2021-02-22
arzuyelizzz_	0	2021-02-22
gukaykosee	0	2021-02-22
farnazshahhoseini	0	2021-02-22
zeynepkrc123	0	2021-02-22
sencan.raz	0	2021-02-22
cglsagalticii	0	2021-02-22
caglaberk1905	0	2021-02-22
selin_ceylin94	0	2021-02-22
yokyookturkey	0	2021-02-22
ozge_berber	0	2021-02-22
teslimeneyaman	0	2021-02-22
edabldk	0	2021-02-22
ebru_ksgz	0	2021-02-22
evrimsengel_unlu	0	2021-02-22
arch_meral_	0	2021-02-22
erkisneslihan	0	2021-02-22
yulduz_deniz_	0	2021-02-22
selin.4795	0	2021-02-22
sevgi071	0	2021-02-22
leyla13125	0	2021-02-22
muzikcisenay	0	2021-02-22
serpil_d.k	0	2021-02-22
heval_hvl	0	2021-02-22
filizkurtuluskurun	0	2021-02-22
nzlgks	0	2021-02-22
remziyekcmn	0	2021-02-22
nuran4582	0	2021-02-22
diana_mamedova28	0	2021-02-22
yagmuraydin3436	0	2021-02-22
nagihandiri	0	2021-02-22
flz_bts	0	2021-02-22
aaaassssliii	0	2021-02-22
yilmazz.omurr	0	2021-02-22
asmn_aysgl_	0	2021-02-22
bilgeeekaan	0	2021-02-22
silence_virture_34	0	2021-02-22
kirazmevsimi.design	0	2021-02-22
sibel_demirbilekk	0	2021-02-22
ayysnr.oztrk	0	2021-02-22
ceyy_da	0	2021-02-22
ayse_nur_saral	0	2021-02-22
uzman_estetisyen34	0	2021-02-22
gulsahbaltaaa	0	2021-02-22
ezgicikk	0	2021-02-22
gulcinncetn	0	2021-02-22
ferablg	0	2021-02-22
haticecagla	0	2021-02-22
ez_1907_sar	0	2021-02-22
aysekuvanc	0	2021-02-22
ragazza.accesoires	0	2021-02-22
surayyoabduhalimova	0	2021-02-22
melekekinciselvi_	0	2021-02-22
selmakcay3	0	2021-02-22
esmanurlu07	0	2021-02-22
hulyaa.4747	0	2021-02-22
gulumsertarkan9	0	2021-02-22
doneerdeem	0	2021-02-22
beautyloverestetik	0	2021-02-22
sbnmcee	0	2021-02-22
berrindberber	0	2021-02-22
turanfigenbakis	0	2021-02-22
kayakunt	0	2021-02-22
efeburakomer	0	2021-02-22
batmane_batmanee	0	2021-02-22
atliisra	0	2021-02-22
ist.ahiska	0	2021-02-22
fatmazehrakaya2018	0	2021-02-22
guldanebayram8	0	2021-02-22
ceemckr	0	2021-02-22
zehrahiragungor	0	2021-02-22
acan.ozlm88	0	2021-02-22
nefes_ahmad	0	2021-02-22
_yagmurdindar	0	2021-02-22
tcaygun	0	2021-02-22
dmr_emelll	0	2021-02-22
mahdibakhtiari55	0	2021-02-22
fulyagonen783	0	2021-02-22
ilaydaozlems	0	2021-02-22
drydrnn.n	0	2021-02-22
gizemyildiirimm	0	2021-02-22
tria.event	0	2021-02-22
bien.beautystudio	0	2021-02-22
yusuf.bahceli	0	2021-02-22
jazel_bayel	0	2021-02-22
isilkec	0	2021-02-22
ibrahimserenkck	0	2021-02-22
aslihankilicnailart	0	2021-02-22
sinemkoyuncuoglu79	0	2021-02-22
bugisusevi	0	2021-02-22
hafizdan_inciler	0	2021-02-22
sblhlt	0	2021-02-22
guleycann	0	2021-02-22
gulsen_capkurt	0	2021-02-22
siyah_beyaz18811938	0	2021-02-22
kelif2975	0	2021-02-22
sukriyeburak_duz	0	2021-02-22
azraagrbas_08	0	2021-02-22
watrs_tristan68mp	0	2021-02-22
val_josette61bz	0	2021-02-22
alexis.lazer	0	2021-02-22
calmes_brett90fx	0	2021-02-22
medikalmdg	0	2021-02-22
gu.ll4410	0	2021-02-22
arkis.ticaret	0	2021-02-22
sherrock_ruthanne65ad	0	2021-02-22
parlak4776	0	2021-02-22
incefikirce	0	2021-02-22
ayfertaruk1961_phiacademy	0	2021-02-22
eminesonmez2526	0	2021-02-22
phibrows_arzukaya	0	2021-02-22
mamoo_the_love_fariba	0	2021-02-22
esnys	0	2021-02-22
fadikaselalp	0	2021-02-22
bb.farida	0	2021-02-22
aysunyukselonar	0	2021-02-22
__elaaxx	0	2021-02-22
dyy.kms	0	2021-02-22
laviniaa.n	0	2021-02-22
kbra_altn	0	2021-02-22
mervelkyc	0	2021-02-22
fundaalmiranisa	0	2021-02-22
hndn_official	0	2021-02-22
cxkenan	0	2021-02-22
pnb.344	0	2021-02-22
esratillaa34	0	2021-02-22
_sweet_dream_88	0	2021-02-22
mevludecelk	0	2021-02-22
salis.ch	0	2021-02-22
oliviabozkurt	0	2021-02-22
terzi.burcu	0	2021-02-22
narintopaloglu	0	2021-02-22
leyla_dpt_narcicegi	0	2021-02-22
vildos05	0	2021-02-22
blogamiii	0	2021-02-22
selviezer	0	2021-02-22
achilova_1905	0	2021-02-22
ta.ya9974	0	2021-02-22
beautifull_woman86	0	2021-02-22
snykocc	0	2021-02-22
_buseakin	0	2021-02-22
eliffkkuzey	0	2021-02-22
petslove_66	0	2021-02-22
fit_woman_ceyla	0	2021-02-22
can_romanticprens	0	2021-02-22
serhat_smsk123	0	2021-02-22
murvet_1995	0	2021-02-22
zeynndesing	0	2021-02-22
sehidegull	0	2021-02-22
nazaneliuz	0	2021-02-22
abasizsoner	0	2021-02-22
eraymzr	0	2021-02-22
emlnisaunsal	0	2021-02-22
gangaalla	0	2021-02-22
sbl.ozkls	0	2021-02-22
n.karacali	0	2021-02-22
farzane575nisely	0	2021-02-22
nurr.acrr	0	2021-02-22
fifi_mamalam123	0	2021-02-22
yaseminy00	0	2021-02-22
nooshin.pm	0	2021-02-22
melis_marina_korenkova	0	2021-02-22
maral91_20	0	2021-02-22
atallahrym	0	2021-02-22
hh.aky	0	2021-02-22
gizemm.goktass	0	2021-02-22
dilyayesil	0	2021-02-22
hulyakutuk_	0	2021-02-22
merve.senlioglu	0	2021-02-22
betul_yucel_46_	0	2021-02-22
aytengoreli	0	2021-02-22
bera_mualla	0	2021-02-22
nimduru	0	2021-02-22
sukranvarinli	0	2021-02-22
eylemkara2134	0	2021-02-22
ala__merve	0	2021-02-22
esrakarad	0	2021-02-22
es.ra4660	0	2021-02-22
deryaa.yildzz	0	2021-02-22
sevimdemir6246	0	2021-02-22
zuleyhacnr	0	2021-02-22
edaarslan_official	0	2021-02-22
gercek_dusler2021	0	2021-02-22
foreverbeautyadana	0	2021-02-22
emineozlemkaplan	0	2021-02-22
nicelash.extension	0	2021-02-22
arifesahra	0	2021-02-22
naturalnyyy	0	2021-02-22
vefa_mili81	0	2021-02-22
pinar.cayiroglu	0	2021-02-22
_seda.gunes	0	2021-02-22
nezahatcinarr	0	2021-02-22
sengulcayroglu	0	2021-02-22
italiangoddess777	0	2021-02-22
ipekyuceerim	0	2021-02-22
helinozgurr5	0	2021-02-22
eegedikli	0	2021-02-22
tc.sema._akgun	0	2021-02-22
sahracaliskancan	0	2021-02-22
sbilging	0	2021-02-22
biancacastilhoo_	0	2021-02-22
aysenur_gevrek	0	2021-02-22
pnrkblt	0	2021-02-22
sadiyeselcuk	0	2021-02-22
ugurboceklikiz	0	2021-02-22
irozkaya	0	2021-02-22
nurdankmryuce	0	2021-02-22
aynur.turpcutezbicer	0	2021-02-22
esra.aksoy.avci	0	2021-02-22
nermingokay	0	2021-02-22
eda_bayram79	0	2021-02-22
sophiaserini	0	2021-02-22
feridesenses	0	2021-02-22
bsrakhrmn23	0	2021-02-22
neclacakti	0	2021-02-22
nur_srgn	0	2021-02-22
ayse.erten.96	0	2021-02-22
_ha_ssss_	0	2021-02-22
omgmamaa	0	2021-02-22
misswoodentr	0	2021-02-22
klip_fann11	0	2021-02-22
minesarimusaoglu	0	2021-02-22
sirinceislerisler	0	2021-02-22
victoriandmakeup	0	2021-02-22
ggsahiin	0	2021-02-22
ipekkynslck	0	2021-02-22
sade77sade	0	2021-02-22
esma_gms_krhn0	0	2021-02-22
jingmei_medicos_factory	0	2021-02-22
jeffreysincoheren	0	2021-02-22
ayse_sevda_kanaviceleri	0	2021-02-22
starkozmetikzazahan	0	2021-02-22
gokkusagi_tasarim16	0	2021-02-22
bloomipekkirpik	0	2021-02-22
melek.blog1_	0	2021-02-22
ruyabutikandfashion	0	2021-02-22
pnb_akdeniz	0	2021-02-22
aratbilge	0	2021-02-22
ilbeykaraman	0	2021-02-22
esmerkiz8585	0	2021-02-22
srdconcept	0	2021-02-22
ozlem_ozcan24	0	2021-02-22
fa__risou	0	2021-02-22
bernahoca22	0	2021-02-22
hulyaosmancelebioglu	0	2021-02-22
srf_hrn_er	0	2021-02-22
burcuzahidekozi	0	2021-02-22
ekimozdmr	0	2021-02-22
pilatesoops	0	2021-02-22
busrasbdo	0	2021-02-22
bagcierkan	0	2021-02-22
kubraaoztrkk	0	2021-02-22
dilekk_sude34	0	2021-02-22
ipekkurtalan	0	2021-02-22
mehmetin_yolu_1923	0	2021-02-22
seldaozcicek	0	2021-02-22
iz.healthcare	0	2021-02-22
uzm.dr.yusuftopal	0	2021-02-22
gunes12k	0	2021-02-22
socialnetworknitro	0	2021-02-22
bozoglumelis	0	2021-02-23
sevgiakyuz67	0	2021-02-23
pervinkurekci	0	2021-02-23
selma_kose60	0	2021-02-23
kordelserra	0	2021-02-23
dondu_toxoy	0	2021-02-23
arasi_s_mama	0	2021-02-23
ozlemm.taskinn	0	2021-02-23
dewillaa	0	2021-02-23
handanarya	0	2021-02-23
enecanazymova	0	2021-02-23
tebeta_umuc	0	2021-02-23
digdemsezgin	0	2021-02-23
slmnvzt	0	2021-02-23
hayatttt6779	0	2021-02-23
gezentikizilderili	0	2021-02-23
fenomen_ogretmen	0	2021-02-23
esmer.aydilek	0	2021-02-23
ebruduru_	0	2021-02-23
saricicekhulya	0	2021-02-23
zeynepbusrabalci	0	2021-02-23
sara.a.zand	0	2021-02-23
sevindik_nebahat	0	2021-02-23
borcesonguc	0	2021-02-23
777a.star	0	2021-02-23
berfevberfev	0	2021-02-23
brc_yldzz	0	2021-02-23
sevdaatalay	0	2021-02-23
ezgiboydagg	0	2021-02-23
serpilerdemcam	0	2021-02-23
satye78	0	2021-02-23
tuln_ersoz	0	2021-02-23
arzusuzmen	0	2021-02-23
elifcakarmentes	0	2021-02-23
meltemtekigul1	0	2021-02-23
cavansir__eliyev__official	0	2021-02-23
selale8786	0	2021-02-23
natia_ultras	0	2021-02-23
yasemingnlalan	0	2021-02-23
b_lkgirl	0	2021-02-23
deryakayaduman	0	2021-02-23
merveakaltin	0	2021-02-23
_berfinkilic	0	2021-02-23
lilet.kimar	0	2021-02-23
meltem_ozdemir_sav	0	2021-02-23
kevserrr.17	0	2021-02-23
seravarolyedek_	0	2021-02-23
temizel.asiye	0	2021-02-23
koray8sena	0	2021-02-23
aylinhira	0	2021-02-23
nuesguzellik	0	2021-02-23
seherkocabay5124	0	2021-02-23
ozqe_533	0	2021-02-23
cagriyurdakulu	0	2021-02-23
nrglaktas	0	2021-02-23
wonder_medical_technology_tr	0	2021-02-23
yigit.tk52	0	2021-02-23
esen_zeynepada	0	2021-02-23
privlendin_kaktus	0	2021-02-23
vildn.tk	0	2021-02-23
esgunoglukadriye	0	2021-02-23
cam.balkon.ist	0	2021-02-23
ceyiz_urunleriiii	0	2021-02-23
eylul_guzellik_salonu	0	2021-02-23
petenmurat	0	2021-02-23
duygusamyeli	0	2021-02-23
zelihagunay1	0	2021-02-23
vildan_savuran	0	2021-02-23
eminesaral53	0	2021-02-23
di_la_ni_lu	0	2021-02-23
seldauzunozkrt	0	2021-02-23
seherryilmz1	0	2021-02-23
creamygifts	0	2021-02-23
essra.guveenn	0	2021-02-23
lhshmy4915	0	2021-02-23
pelin_alacam	0	2021-02-23
son_durak256	0	2021-02-23
yasminnimyas06	0	2021-02-23
eecelingoo	0	2021-02-23
kader_balcc	0	2021-02-23
nz.ats	0	2021-02-23
mrvylm__m	0	2021-02-23
gzn_a	0	2021-02-23
zehraaatoprk	0	2021-02-23
elifaytaac	0	2021-02-23
deryatugcecelebi	0	2021-02-23
sinemelifemre	0	2021-02-23
edanur.yldzz41	0	2021-02-23
sufyansafder2002	0	2021-02-23
rukiyedrk_	0	2021-02-23
emrulah.surmeli.0134	0	2021-02-23
muratt.dalkilic	0	2021-02-23
uzm.est.cemresaracoglu	0	2021-02-23
cgdmozp	0	2021-02-23
serap_ongel	0	2021-02-23
chichomastercom	0	2021-02-23
neslibugarhan33	0	2021-02-23
cigdemaltinadakaraca	0	2021-02-23
duygu.cengizz	0	2021-02-23
rengrebf	0	2021-02-23
karolin.karakulah	0	2021-02-23
dryyyarslan	0	2021-02-23
nurdabanli	0	2021-02-23
ekinonlaynn	0	2021-02-23
esrayildiz003	0	2021-02-23
nurctf	0	2021-02-23
ermisneriman	0	2021-02-23
gulianahan	0	2021-02-23
sudesuat6	0	2021-02-23
elakkayanurla	0	2021-02-23
mine.strr	0	2021-02-23
av.gulbaharkaya	0	2021-02-23
mmina.yildiz	0	2021-02-23
arsoydilara	0	2021-02-23
yuzgeny	0	2021-02-23
hulyaaribozoglu	0	2021-02-23
ysmsl2021	0	2021-02-23
semahkanbolat	0	2021-02-23
meysunk	0	2021-02-23
elifzengince	0	2021-02-23
rusemsevukk	0	2021-02-23
mustafabogaz	0	2021-02-23
sny.1986	0	2021-02-23
mycol_orfulworld	0	2021-02-23
gulsegencc	0	2021-02-23
gulcinesila7	0	2021-02-23
smeyyecakir	0	2021-02-23
pinaaryilmazz	0	2021-02-23
denizonayserpil	0	2021-02-23
mineldeniz3434	0	2021-02-23
mihribann.35_	0	2021-02-23
slvsvl.krcn	0	2021-02-23
_nuraylaa	0	2021-02-23
elif_deveci_1	0	2021-02-23
ays98077	0	2021-02-23
nehirmelek	0	2021-02-23
emelstcu	0	2021-02-23
dlk_pl	0	2021-02-23
gokceuygursen	0	2021-02-23
gulmisali.tr	0	2021-02-23
pinarkb	0	2021-02-23
betuldemircn	0	2021-02-23
theope.meno	0	2021-02-23
ayseaydinalp	0	2021-02-23
topkaya.mine	0	2021-02-23
handeucangonenc	0	2021-02-23
salihasaglik	0	2021-02-23
direnlengerli	0	2021-02-23
sevimredjep1	0	2021-02-23
bir_ten	0	2021-02-23
_esragungormez_	0	2021-02-23
__denizcelik	0	2021-02-23
ilkayatly	0	2021-02-23
ozim1974	0	2021-02-23
dbboa	0	2021-02-23
betty_organizasyon	0	2021-02-23
cemredeniz7254	0	2021-02-23
nazbaro543	0	2021-02-23
sedacetinyavuz	0	2021-02-23
farmasihulya___	0	2021-02-23
atagokselsukran	0	2021-02-23
_duygusenol	0	2021-02-23
prensesannesi2727	0	2021-02-23
zeynepk.r	0	2021-02-23
burcu_guc_	0	2021-02-23
o_reyhan_d	0	2021-02-23
kupa_kzzz	0	2021-02-23
tbrn.ural	0	2021-02-23
sselinbakk	0	2021-02-23
aysin.nuri.huma	0	2021-02-23
edahuskalar	0	2021-02-23
mervetaspinar1453	0	2021-02-23
derinkeskinn90	0	2021-02-23
a.k.a.2.0.1.9	0	2021-02-23
28_isilatici_28	0	2021-02-23
kayaebruu	0	2021-02-23
ozlem.klcoglu	0	2021-02-23
dilek_eymen_defne	0	2021-02-23
smrsakarya	0	2021-02-23
beomde3452	0	2021-02-23
53dogukanzuhal53	0	2021-02-23
sultan.keskin.566148	0	2021-02-23
urgun_ozgur	0	2021-02-23
eliff_sgt_	0	2021-02-23
nanittayaalaoui	0	2021-02-23
atg.kozmetik	0	2021-02-23
babasinin_kizi190573	0	2021-02-23
turkansertac	0	2021-02-23
demircifat	0	2021-02-23
kuaforismailankara	0	2021-02-23
biraz.edebiyat06	0	2021-02-23
eyess_makeup	0	2021-02-23
glsmorak	0	2021-02-23
ceylan_tamer_k.m.u	0	2021-02-23
bysevim_ozdemir	0	2021-02-23
bahardemirtasas	0	2021-02-23
damlaefeerdem	0	2021-02-23
farmasi_5429	0	2021-02-23
siblle	0	2021-02-23
kzk6831	0	2021-02-23
tm_ithalat	0	2021-02-23
fdmgl	0	2021-02-23
avonu_indirimli_gelis_fiyatl	0	2021-02-23
_ojelendikk	0	2021-02-23
sezendmrkl	0	2021-02-23
lazerepilasyoncihazi	0	2021-02-23
brnklima	0	2021-02-23
ergundeniz3	0	2021-02-23
simurgg_guzellik	0	2021-02-23
aysem_guzellik_estetik	0	2021-02-23
zerrinatkl	0	2021-02-23
endam_gulll	0	2021-02-23
siyah_kadin_fyz	0	2021-02-23
tubikoo	0	2021-02-23
eliffdkr	0	2021-02-23
ilknurlal	0	2021-02-23
edizatamelek	0	2021-02-23
sumeyyebasbugu	0	2021-02-23
ffff__yyy	0	2021-02-23
fuck_it_ceramics	0	2021-02-23
fulyatolga	0	2021-02-23
ozge.saatci	0	2021-02-23
berrin_ztrk	0	2021-02-23
angela_angels__	0	2021-02-23
selmasunku	0	2021-02-23
hkrizantemc	0	2021-02-23
tubaalayi	0	2021-02-23
geniusvelovis	0	2021-02-23
ebrar.rrr	0	2021-02-23
nehirsariozkan	0	2021-02-23
gul.cemal.9250	0	2021-02-23
pelolii	0	2021-02-23
buttiksepeti	0	2021-02-23
gereksizpost.tr	0	2021-02-23
xdd.gulsum	0	2021-02-23
ylcmrv	0	2021-02-23
semihyildirim190358	0	2021-02-23
aliyyeffa.17	0	2021-02-23
ibtis.sammar5	0	2021-02-23
gezen.tavuq	0	2021-02-23
halil_ibrahim_atik_	0	2021-02-23
sedafidanx	0	2021-02-23
kandela.mum	0	2021-02-23
serpil_cuma	0	2021-02-23
ayfersahnn	0	2021-02-23
gulhuriye3434	0	2021-02-23
gulcanehlibasman	0	2021-02-23
saraa_tayebii	0	2021-02-23
aysehatundaderler	0	2021-02-23
ozlemdonmezzzz	0	2021-02-23
selmas.kartal	0	2021-02-23
gulserenyldrm2	0	2021-02-23
sezen5906	0	2021-02-23
duyguupoyrazz	0	2021-02-23
nes83588	0	2021-02-23
gnscigdem	0	2021-02-23
hakaner.san	0	2021-02-23
nathaliabiancadesigner	0	2021-02-23
suzanyahyaoglu	0	2021-02-23
coooo234ls	0	2021-02-23
dream_sohrabi	0	2021-02-23
adanurlove	0	2021-02-23
melekjale	0	2021-02-23
ayse3464	0	2021-02-23
elifhanum	0	2021-02-23
smyyeatilla	0	2021-02-23
charoghchi_shima	0	2021-02-23
busra.dyms.yldz	0	2021-02-23
_basakk34xx	0	2021-02-23
lolammira	0	2021-02-23
_estetisyengmzdnc	0	2021-02-23
sakir_bariser49	0	2021-02-23
baze_seyler_elimz_de_degl_duam	0	2021-02-23
\.


--
-- TOC entry 3007 (class 0 OID 24604)
-- Dependencies: 202
-- Data for Name: dm; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dm (sender_account, sent_account, message, dm_date) FROM stdin;
qlua.nisantasi	elifdemirorn	En güzel ve en doğal Microblading kaş & Dudak renklendirme işlemleri Qlua kalıcı makyaj da	2021-02-17
qlua.nisantasi	lady__birdss	Qlua kalıcı makyaj Nişantaşı merkez ve yeni Bakırköy şubesiylede hizmetinizde	2021-02-17
qlua.nisantasi	nilgungezer52	Harika microblading kaşlarmı, doğal dudaklarmı en güzeli Qlua'da	2021-02-17
qlua.nisantasi	meltem.topal34	Qlua microblading Nişantaşı ve Bakırköy şubesiyle en doğal uygulamalara imza atmakta	2021-02-17
qlua.nisantasi	nesibe.basol	Dudak renklendirme ve Microblading kaş işlemleri Qlua da detay için lütfen sayfamızı ziyaret et	2021-02-17
qlua.nisantasi	fatos_kangalci	Eşsiz kaş tasarımları ve dudak renklendirme işlemleri Qlua da	2021-02-17
qlua.nisantasi	akaraygun95	En güzeli, en özeli Microblading kaş tasarımları ve dudak renklendirme Qlua da	2021-02-17
qlua.nisantasi	asumanbaydarol	Nişantaşı Qlua kalıcı makyaj artık Bakırköyde	2021-02-17
qlua.nisantasi	safiye_muallime	Aradığın doğal ve güzel kaş & dudaklar Qlua da lütfen detay için sayfamıza bakın	2021-02-17
qlua.nisantasi	tcgulaysozeri	Qlua kalıcı makyaj Nişantaşı merkez ve yeni Bakırköy şubesiylede hizmetinizde	2021-02-18
qlua.nisantasi	roba.isaa	En güzel ve en doğal Microblading kaş & Dudak renklendirme işlemleri Qlua kalıcı makyaj da	2021-02-18
qlua.nisantasi	erennburcu___	Qlua microblading Nişantaşı ve Bakırköy şubesiyle en doğal uygulamalara imza atmakta	2021-02-18
qlua.nisantasi	asli.buran.tuntas	Dudak renklendirme ve Microblading kaş işlemleri Qlua da detay için lütfen sayfamızı ziyaret et	2021-02-18
qlua.nisantasi	aysha_berhel	Harika microblading kaşlarmı, doğal dudaklarmı en güzeli Qlua'da	2021-02-18
qlua.nisantasi	zehra_urek	En güzeli, en özeli Microblading kaş tasarımları ve dudak renklendirme Qlua da	2021-02-18
qlua.nisantasi	mrv_mrr	Aradığın doğal ve güzel kaş & dudaklar Qlua da lütfen detay için sayfamıza bakın	2021-02-18
qlua.nisantasi	denizb.krt	Eşsiz kaş tasarımları ve dudak renklendirme işlemleri Qlua da	2021-02-18
qlua.nisantasi	_melike__ozcann	İstanbulun en gözde Microblading kaş tasarımları ve dudakları Qlua da	2021-02-18
qlua.nisantasi	gzzdekayaa	Nişantaşı Qlua kalıcı makyaj artık Bakırköyde	2021-02-18
qlua.nisantasi	faatma.durmus	Qlua microblading Nişantaşı ve Bakırköy şubesiyle en doğal uygulamalara imza atmakta	2021-02-19
qlua.nisantasi	istegeldimburdayiim	Harika microblading kaşlarmı, doğal dudaklarmı en güzeli Qlua'da 	2021-02-19
qlua.nisantasi	mylife35710	Eşsiz kaş tasarımları ve dudak renklendirme işlemleri Qlua da	2021-02-19
qlua.nisantasi	gunel6806	En güzel ve en doğal Microblading kaş & Dudak renklendirme işlemleri Qlua kalıcı makyaj da	2021-02-19
qlua.nisantasi	botchednosey	Nişantaşı Qlua kalıcı makyaj artık Bakırköyde	2021-02-19
qlua.nisantasi	nilay.oztrk	Qlua kalıcı makyaj Nişantaşı merkez ve yeni Bakırköy şubesiylede hizmetinizde 	2021-02-19
qlua.nisantasi	5858_fatos	İstanbulun en gözde Microblading kaş tasarımları ve dudakları Qlua da	2021-02-19
qlua.nisantasi	demirrozalin	Dudak renklendirme ve Microblading kaş işlemleri Qlua da detay için lütfen sayfamızı ziyaret et	2021-02-19
qlua.nisantasi	hatice_arslan_karakaplan	Aradığın doğal ve güzel kaş & dudaklar Qlua da lütfen detay için sayfamıza bakın	2021-02-19
qlua.nisantasi	neslihan_cinar19	En güzeli, en özeli Microblading kaş tasarımları ve dudak renklendirme Qlua da	2021-02-19
\.


--
-- TOC entry 3006 (class 0 OID 24597)
-- Dependencies: 201
-- Data for Name: follow_requests; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.follow_requests (requester_account, requested_account, accepted, declined, request_date) FROM stdin;
\.


--
-- TOC entry 3005 (class 0 OID 24590)
-- Dependencies: 200
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.likes (liker_account, liked_account, like_date) FROM stdin;
qlua.nisantasi	ozgekurdoglu	2021-02-11
qlua.nisantasi	pilates_life_coaching_by_fatih	2021-02-15
qlua.nisantasi	figenadar	2021-02-15
qlua.nisantasi	cc.faces	2021-02-15
qlua.nisantasi	nurarboycoaching	2021-02-16
qlua.nisantasi	34hayatvar	2021-02-16
qlua.nisantasi	husniyedogrul	2021-02-16
qlua.nisantasi	nesibekantarci	2021-02-16
qlua.nisantasi	hlycl	2021-02-17
qlua.nisantasi	biyo_leyla	2021-02-17
qlua.nisantasi	larisalora5450	2021-02-17
qlua.nisantasi	hulyaninellezzetleri36	2021-02-17
qlua.nisantasi	aynurka3057	2021-02-17
qlua.nisantasi	ebruli_phibrows	2021-02-17
qlua.nisantasi	uzm.est.simalunsal	2021-02-17
qlua.nisantasi	bluediamondflower	2021-02-17
qlua.nisantasi	isabelzey_beauty	2021-02-17
qlua.nisantasi	beauty_handan	2021-02-17
qlua.nisantasi	xo.baysel	2021-02-17
qlua.nisantasi	proxone.proxone	2021-02-17
qlua.nisantasi	purpleblogers	2021-02-17
qlua.nisantasi	el_emeklerim24	2021-02-17
qlua.nisantasi	gunduzelibolaysegul	2021-02-17
qlua.nisantasi	d.bulak	2021-02-17
qlua.nisantasi	aysenyuncu	2021-02-17
qlua.nisantasi	sebnemacar	2021-02-17
qlua.nisantasi	burcutanoren	2021-02-17
qlua.nisantasi	mukaddessycl	2021-02-17
qlua.nisantasi	neshemiyyy	2021-02-17
qlua.nisantasi	berrinde	2021-02-17
qlua.nisantasi	senidaa	2021-02-17
qlua.nisantasi	asivak_turkey	2021-02-17
qlua.nisantasi	lefkosa.gayrimenkul	2021-02-17
qlua.nisantasi	nisantasi.ozferahgida	2021-02-17
qlua.nisantasi	bozanx2763	2021-02-17
qlua.nisantasi	omertoksoz0	2021-02-17
qlua.nisantasi	siaren.ect	2021-02-17
qlua.nisantasi	gulay.sarp	2021-02-17
qlua.nisantasi	birbuketpaptya	2021-02-17
qlua.nisantasi	askinnurkopkal	2021-02-17
qlua.nisantasi	liyazonayakkabi	2021-02-17
qlua.nisantasi	the_professional_studio	2021-02-17
qlua.nisantasi	seyhaningunlugu	2021-02-17
qlua.nisantasi	pointerturkiye52	2021-02-18
qlua.nisantasi	oriflameeseval	2021-02-18
qlua.nisantasi	film_izlenir	2021-02-18
qlua.nisantasi	singfiller.com.tr	2021-02-18
qlua.nisantasi	feray_gnynk	2021-02-18
qlua.nisantasi	dr.nevriearif	2021-02-18
qlua.nisantasi	dilarademirtasbeautystudio	2021-02-18
qlua.nisantasi	sevgul9640	2021-02-18
qlua.nisantasi	guzel.sevenadamlar	2021-02-18
qlua.nisantasi	ismailders	2021-02-18
qlua.nisantasi	avenuekalicioje.ist	2021-02-18
qlua.nisantasi	herbal.semo	2021-02-18
qlua.nisantasi	estetik_urunler_	2021-02-18
qlua.nisantasi	elifdenizlimanoglu	2021-02-18
qlua.nisantasi	aya_chernova	2021-02-18
qlua.nisantasi	dsozdol	2021-02-18
qlua.nisantasi	gizemygun	2021-02-18
qlua.nisantasi	niis_permanent_makeup	2021-02-18
qlua.nisantasi	m.ebadi1212	2021-02-18
qlua.nisantasi	maria.iram3030	2021-02-18
qlua.nisantasi	sebahat7526	2021-02-18
qlua.nisantasi	gulsah.akgul.akdag	2021-02-18
qlua.nisantasi	elifertantaskin	2021-02-18
qlua.nisantasi	kamilaolbrych	2021-02-18
qlua.nisantasi	senem.urhan	2021-02-18
qlua.nisantasi	zulfiya9542	2021-02-18
qlua.nisantasi	fminell	2021-02-18
qlua.nisantasi	01no	2021-02-18
qlua.nisantasi	rumeysakru	2021-02-18
qlua.nisantasi	microblading_mariam	2021-02-18
qlua.nisantasi	gozdeyilmazbeauty	2021-02-18
qlua.nisantasi	bellebeautyclub	2021-02-18
qlua.nisantasi	apo_mannheim	2021-02-18
qlua.nisantasi	drdermiss	2021-02-18
qlua.nisantasi	rinoplastika.dr.asvari.javdani	2021-02-18
qlua.nisantasi	rencar_otomotiv	2021-02-18
qlua.nisantasi	feromen.fero	2021-02-18
qlua.nisantasi	emine_kuafor_17	2021-02-18
qlua.nisantasi	goldrenovation	2021-02-18
qlua.nisantasi	motivasyonhome	2021-02-18
qlua.nisantasi	bulent.fera	2021-02-18
qlua.nisantasi	kilincdilek762	2021-02-18
qlua.nisantasi	tegemed	2021-02-18
qlua.nisantasi	mimitbeyy	2021-02-18
qlua.nisantasi	illy9389	2021-02-18
qlua.nisantasi	zaferperformance	2021-02-18
qlua.nisantasi	deniz_spor.1	2021-02-18
qlua.nisantasi	dilanbilgin	2021-02-18
qlua.nisantasi	best_turkish_novels_	2021-02-18
qlua.nisantasi	gizem.karell	2021-02-18
qlua.nisantasi	dilancmkrtn	2021-02-18
qlua.nisantasi	hll_mina_dmr	2021-02-18
qlua.nisantasi	armenyapi	2021-02-18
qlua.nisantasi	muge_kas_tasarm	2021-02-18
qlua.nisantasi	burcukoc_1	2021-02-18
qlua.nisantasi	motoreferanss	2021-02-18
qlua.nisantasi	evyasamsunum	2021-02-18
qlua.nisantasi	bebek.ekgida.tarifleri.dev	2021-02-18
qlua.nisantasi	shapp.o	2021-02-18
qlua.nisantasi	sahibini7im	2021-02-18
qlua.nisantasi	aneshka32_	2021-02-18
qlua.nisantasi	aasenacetek	2021-02-18
qlua.nisantasi	danielharrington482	2021-02-19
qlua.nisantasi	sarisoykader	2021-02-19
qlua.nisantasi	yagmurboranaksu	2021-02-19
qlua.nisantasi	shabnam_shahidzadeh	2021-02-19
qlua.nisantasi	tubahkngullu	2021-02-19
qlua.nisantasi	ayakgaci	2021-02-19
qlua.nisantasi	ipekkirpik_malzeme_antalya	2021-02-19
qlua.nisantasi	phibrows_shiraz20	2021-02-19
qlua.nisantasi	sayara747	2021-02-19
qlua.nisantasi	gzmklvz	2021-02-19
qlua.nisantasi	organikolye	2021-02-19
qlua.nisantasi	bbrows_studio	2021-02-19
qlua.nisantasi	nuraydartar	2021-02-19
qlua.nisantasi	mayapernepesova	2021-02-19
qlua.nisantasi	sofi.ssweet	2021-02-19
qlua.nisantasi	aslihank	2021-02-19
qlua.nisantasi	yoksa_sen	2021-02-19
qlua.nisantasi	essin.gny	2021-02-19
qlua.nisantasi	hakankuyuofficial	2021-02-19
qlua.nisantasi	elcinsumer	2021-02-19
qlua.nisantasi	_hamza_atlan	2021-02-19
qlua.nisantasi	toprakdekor38	2021-02-19
qlua.nisantasi	haktekk	2021-02-19
qlua.nisantasi	burcuukalp	2021-02-19
qlua.nisantasi	baraa_bachroui_85	2021-02-19
qlua.nisantasi	m_e_.m0	2021-02-19
qlua.nisantasi	hjimuradi	2021-02-19
qlua.nisantasi	pulsar72	2021-02-19
qlua.nisantasi	asumankorkmazz	2021-02-19
qlua.nisantasi	dsportwomen	2021-02-19
qlua.nisantasi	nilhangurses	2021-02-19
qlua.nisantasi	pusicanta	2021-02-19
qlua.nisantasi	0nlinezoo	2021-02-19
qlua.nisantasi	merve.tnrkl	2021-02-19
qlua.nisantasi	duayentasarim	2021-02-19
qlua.nisantasi	zeynep_yahya_ebrar	2021-02-19
qlua.nisantasi	hatice_serbest77	2021-02-19
qlua.nisantasi	nankaemi	2021-02-19
qlua.nisantasi	altmanemir	2021-02-19
qlua.nisantasi	merve.aratemurofficial	2021-02-19
qlua.nisantasi	mirabeaute_nails	2021-02-19
qlua.nisantasi	elif.kerpc	2021-02-19
qlua.nisantasi	ayse_mlye	2021-02-19
qlua.nisantasi	gulvaryo78	2021-02-19
qlua.nisantasi	sgmelis	2021-02-19
qlua.nisantasi	gokce.erbil	2021-02-19
qlua.nisantasi	tusdatadusdatakonya	2021-02-19
qlua.nisantasi	kahve_molasii	2021-02-19
qlua.nisantasi	perabaskiatolyesi	2021-02-19
qlua.nisantasi	hacerhazarhun	2021-02-19
qlua.nisantasi	nesrin.abnz	2021-02-19
qlua.nisantasi	nkabill	2021-02-19
qlua.nisantasi	beyz_tur	2021-02-19
qlua.nisantasi	annadellarte	2021-02-19
qlua.nisantasi	angay62	2021-02-19
qlua.nisantasi	canaralofficial	2021-02-19
qlua.nisantasi	sumaya_ashraf.18	2021-02-19
qlua.nisantasi	osama_429a	2021-02-19
qlua.nisantasi	mrtok34	2021-02-19
qlua.nisantasi	emin08	2021-02-19
qlua.nisantasi	ransserie	2021-02-19
qlua.nisantasi	efdesign3d	2021-02-19
qlua.nisantasi	bellezza_pingmentation_turkiye	2021-02-19
qlua.nisantasi	cevahirhadi	2021-02-19
qlua.nisantasi	gamzebulu34	2021-02-19
qlua.nisantasi	stefaniabelleimicroblading_pmu	2021-02-19
qlua.nisantasi	fotografkahvem	2021-02-19
qlua.nisantasi	pro_removerx	2021-02-19
qlua.nisantasi	aishanbeautycenter	2021-02-19
qlua.nisantasi	palettasarimcom	2021-02-19
qlua.nisantasi	nesrncetn	2021-02-19
qlua.nisantasi	wishlist_by_sez	2021-02-21
qlua.nisantasi	mimarsultan	2021-02-21
qlua.nisantasi	ipek__kiprik	2021-02-21
qlua.nisantasi	cosmeticmeddevrim	2021-02-21
qlua.nisantasi	zelish34_estetikmalzemeler	2021-02-21
qlua.nisantasi	elitcarelazer	2021-02-21
qlua.nisantasi	arsaljarral09	2021-02-21
qlua.nisantasi	ilayfic3	2021-02-21
qlua.nisantasi	setenaypeker	2021-02-21
qlua.nisantasi	sevimlekurabiyeler	2021-02-21
qlua.nisantasi	turkiye.kirpik.tirnak.malzeme	2021-02-21
qlua.nisantasi	hazalinyemekleri	2021-02-21
qlua.nisantasi	gozdegrsoyy	2021-02-21
qlua.nisantasi	eli_ftemiz	2021-02-21
qlua.nisantasi	aycaorakburkek	2021-02-21
qlua.nisantasi	genomguzellik	2021-02-21
qlua.nisantasi	nar.london	2021-02-21
qlua.nisantasi	ferhanaltinbas	2021-02-21
qlua.nisantasi	cennet_nefes_yasamkocu	2021-02-21
qlua.nisantasi	efeaynadekorasyon	2021-02-21
qlua.nisantasi	seziyetkili	2021-02-21
qlua.nisantasi	yenigulhatice	2021-02-22
qlua.nisantasi	natalia_goddess_pmu	2021-02-22
qlua.nisantasi	pratikahsapkutu	2021-02-22
qlua.nisantasi	muhrata	2021-02-22
qlua.nisantasi	sydney_p_parrish	2021-02-22
qlua.nisantasi	asim.dernek	2021-02-22
qlua.nisantasi	masalsozlerr	2021-02-22
qlua.nisantasi	livegulsh	2021-02-22
qlua.nisantasi	sedm.kaya	2021-02-22
qlua.nisantasi	herbnuralsahin	2021-02-22
qlua.nisantasi	cgrdfnalan	2021-02-22
qlua.nisantasi	azbilinen	2021-02-22
qlua.nisantasi	betelgeusedonusumdanismanlik	2021-02-22
qlua.nisantasi	mhmtyksl06	2021-02-22
qlua.nisantasi	fundagokesme	2021-02-22
qlua.nisantasi	nsamba.patrick.376	2021-02-22
qlua.nisantasi	gezemedigimden	2021-02-22
qlua.nisantasi	albina.khramova	2021-02-22
qlua.nisantasi	dr.burcuzabun	2021-02-22
qlua.nisantasi	dt.ulkukologlu	2021-02-22
qlua.nisantasi	santosredward	2021-02-22
qlua.nisantasi	camlicacini	2021-02-22
qlua.nisantasi	zafersogutcu	2021-02-22
qlua.nisantasi	duygunun_tasarimlari34	2021-02-22
qlua.nisantasi	zumrutcum21	2021-02-22
qlua.nisantasi	stylebaku_caffe	2021-02-22
qlua.nisantasi	fundaakdemir24	2021-02-22
qlua.nisantasi	polly.keller.35	2021-02-22
qlua.nisantasi	serenayccoban	2021-02-22
qlua.nisantasi	melismeteli	2021-02-22
qlua.nisantasi	ilknurdamar_official	2021-02-22
qlua.nisantasi	atcasila	2021-02-22
qlua.nisantasi	phistudio_nj	2021-02-22
qlua.nisantasi	saharfooladii_phibrows	2021-02-22
qlua.nisantasi	oriflame_avon_prizren	2021-02-22
qlua.nisantasi	ferferi_shop21	2021-02-22
qlua.nisantasi	maliymsc	2021-02-22
qlua.nisantasi	kuafor.sevgii	2021-02-22
qlua.nisantasi	bli.nail	2021-02-22
qlua.nisantasi	onyeomatony	2021-02-22
qlua.nisantasi	mucankus	2021-02-22
qlua.nisantasi	soran.ogretmen	2021-02-22
qlua.nisantasi	lezzetsekertiziouzou	2021-02-22
qlua.nisantasi	elinguzellik	2021-02-22
qlua.nisantasi	pinosha_pnr	2021-02-22
qlua.nisantasi	fatmasabuncu1903	2021-02-22
qlua.nisantasi	babysharkcam	2021-02-22
qlua.nisantasi	gems_anotolia	2021-02-22
qlua.nisantasi	life_meuble	2021-02-22
qlua.nisantasi	wa.rd6435	2021-02-22
qlua.nisantasi	lucchesi_estetica	2021-02-22
qlua.nisantasi	vascularsocialworld	2021-02-22
qlua.nisantasi	ilaydayaslan	2021-02-22
qlua.nisantasi	kirpikmarketim1	2021-02-22
qlua.nisantasi	doruk_media	2021-02-22
qlua.nisantasi	hilalsngr	2021-02-22
qlua.nisantasi	emeltatayy	2021-02-22
qlua.nisantasi	gulbahar_gulsumm	2021-02-22
qlua.nisantasi	tiktokirpik	2021-02-22
qlua.nisantasi	karas_grouptr	2021-02-22
qlua.nisantasi	coktatliseyler_acibadem	2021-02-22
qlua.nisantasi	mygalacos69	2021-02-22
qlua.nisantasi	sedikahocaoglu	2021-02-22
qlua.nisantasi	cyd.brky.11	2021-02-22
qlua.nisantasi	poshlashmarket	2021-02-22
qlua.nisantasi	isimlikadresim	2021-02-22
qlua.nisantasi	nani_beauty_salon	2021-02-22
qlua.nisantasi	merkezi.n	2021-02-22
qlua.nisantasi	nursoltan_nnn	2021-02-22
qlua.nisantasi	sakuraliman	2021-02-22
qlua.nisantasi	ozturk2918_sezen_bayan_kuaforu	2021-02-22
qlua.nisantasi	serpil_ayar_guzellik_merkezi	2021-02-22
qlua.nisantasi	tuana_bayan_kuaforu1	2021-02-22
qlua.nisantasi	essra.tass	2021-02-22
qlua.nisantasi	osman.demr	2021-02-22
qlua.nisantasi	soulmateone	2021-02-22
qlua.nisantasi	helisderiveaksesuar	2021-02-22
qlua.nisantasi	maha_sabbah2015	2021-02-22
qlua.nisantasi	h.nn568	2021-02-22
qlua.nisantasi	namo_0009	2021-02-22
qlua.nisantasi	madamcarlotta	2021-02-22
qlua.nisantasi	sametkorkutt	2021-02-22
qlua.nisantasi	emine.ozturkkkkkk	2021-02-22
qlua.nisantasi	sayestee	2021-02-22
qlua.nisantasi	vedat_kaplan1903	2021-02-22
qlua.nisantasi	izieli_gitardersleri	2021-02-22
qlua.nisantasi	personal_buyer_europe_	2021-02-22
qlua.nisantasi	sedakirimm	2021-02-22
qlua.nisantasi	leilaallanazarova	2021-02-22
qlua.nisantasi	yanik5781	2021-02-22
qlua.nisantasi	vero.brows	2021-02-22
qlua.nisantasi	hayat_ek	2021-02-22
qlua.nisantasi	evasarlak	2021-02-22
qlua.nisantasi	next_babykids	2021-02-22
qlua.nisantasi	arina_zanash	2021-02-22
qlua.nisantasi	oya.canbaz	2021-02-22
qlua.nisantasi	sevcan_saman	2021-02-22
qlua.nisantasi	bslrwh6	2021-02-22
qlua.nisantasi	flowerbombbrows	2021-02-22
qlua.nisantasi	elita_elif	2021-02-22
qlua.nisantasi	naribanderin47	2021-02-22
qlua.nisantasi	aksudekor	2021-02-22
qlua.nisantasi	tolga.aykutt	2021-02-22
qlua.nisantasi	hemelsgumruk	2021-02-22
qlua.nisantasi	ibrahimatci47	2021-02-22
qlua.nisantasi	yummy_time_by_s	2021-02-22
qlua.nisantasi	beyzanur.efe	2021-02-22
qlua.nisantasi	rus_dili_istanbul	2021-02-22
qlua.nisantasi	feray.kuyu	2021-02-22
qlua.nisantasi	nejlakiskac	2021-02-22
qlua.nisantasi	aleynaffan	2021-02-22
qlua.nisantasi	bengul_cokuk	2021-02-22
qlua.nisantasi	yagmurazizekaratas	2021-02-22
qlua.nisantasi	ybiberoglu	2021-02-22
qlua.nisantasi	selinmerl	2021-02-22
qlua.nisantasi	cilem.saglam	2021-02-22
qlua.nisantasi	sencan.raz	2021-02-22
qlua.nisantasi	yokyookturkey	2021-02-22
qlua.nisantasi	edabldk	2021-02-22
qlua.nisantasi	sibel_demirbilekk	2021-02-22
qlua.nisantasi	ragazza.accesoires	2021-02-22
qlua.nisantasi	surayyoabduhalimova	2021-02-22
qlua.nisantasi	esmanurlu07	2021-02-22
qlua.nisantasi	beautyloverestetik	2021-02-22
qlua.nisantasi	tria.event	2021-02-22
qlua.nisantasi	bien.beautystudio	2021-02-22
qlua.nisantasi	aslihankilicnailart	2021-02-22
qlua.nisantasi	bugisusevi	2021-02-22
qlua.nisantasi	watrs_tristan68mp	2021-02-22
qlua.nisantasi	val_josette61bz	2021-02-22
qlua.nisantasi	alexis.lazer	2021-02-22
qlua.nisantasi	calmes_brett90fx	2021-02-22
qlua.nisantasi	medikalmdg	2021-02-22
qlua.nisantasi	arkis.ticaret	2021-02-22
qlua.nisantasi	sherrock_ruthanne65ad	2021-02-22
qlua.nisantasi	incefikirce	2021-02-22
qlua.nisantasi	ayfertaruk1961_phiacademy	2021-02-22
qlua.nisantasi	eminesonmez2526	2021-02-22
qlua.nisantasi	phibrows_arzukaya	2021-02-22
qlua.nisantasi	mamoo_the_love_fariba	2021-02-22
qlua.nisantasi	bb.farida	2021-02-22
qlua.nisantasi	aysunyukselonar	2021-02-22
qlua.nisantasi	fundaalmiranisa	2021-02-22
qlua.nisantasi	hndn_official	2021-02-22
qlua.nisantasi	cxkenan	2021-02-22
qlua.nisantasi	oliviabozkurt	2021-02-22
qlua.nisantasi	blogamiii	2021-02-22
qlua.nisantasi	zeynndesing	2021-02-22
qlua.nisantasi	eraymzr	2021-02-22
qlua.nisantasi	yaseminy00	2021-02-22
qlua.nisantasi	atallahrym	2021-02-22
qlua.nisantasi	hulyakutuk_	2021-02-22
qlua.nisantasi	edaarslan_official	2021-02-22
qlua.nisantasi	gercek_dusler2021	2021-02-22
qlua.nisantasi	foreverbeautyadana	2021-02-22
qlua.nisantasi	emineozlemkaplan	2021-02-22
qlua.nisantasi	nicelash.extension	2021-02-22
qlua.nisantasi	biancacastilhoo_	2021-02-22
qlua.nisantasi	aynur.turpcutezbicer	2021-02-22
qlua.nisantasi	eda_bayram79	2021-02-22
qlua.nisantasi	neclacakti	2021-02-22
qlua.nisantasi	ayse.erten.96	2021-02-22
qlua.nisantasi	misswoodentr	2021-02-22
qlua.nisantasi	klip_fann11	2021-02-22
qlua.nisantasi	minesarimusaoglu	2021-02-22
qlua.nisantasi	sirinceislerisler	2021-02-22
qlua.nisantasi	victoriandmakeup	2021-02-22
qlua.nisantasi	ggsahiin	2021-02-22
qlua.nisantasi	ipekkynslck	2021-02-22
qlua.nisantasi	sade77sade	2021-02-22
qlua.nisantasi	esma_gms_krhn0	2021-02-22
qlua.nisantasi	jingmei_medicos_factory	2021-02-22
qlua.nisantasi	jeffreysincoheren	2021-02-22
qlua.nisantasi	ayse_sevda_kanaviceleri	2021-02-22
qlua.nisantasi	starkozmetikzazahan	2021-02-22
qlua.nisantasi	gokkusagi_tasarim16	2021-02-22
qlua.nisantasi	bloomipekkirpik	2021-02-22
qlua.nisantasi	melek.blog1_	2021-02-22
qlua.nisantasi	ruyabutikandfashion	2021-02-22
qlua.nisantasi	pnb_akdeniz	2021-02-22
qlua.nisantasi	aratbilge	2021-02-22
qlua.nisantasi	ilbeykaraman	2021-02-22
qlua.nisantasi	esmerkiz8585	2021-02-22
qlua.nisantasi	srdconcept	2021-02-22
qlua.nisantasi	fa__risou	2021-02-22
qlua.nisantasi	pilatesoops	2021-02-22
qlua.nisantasi	busrasbdo	2021-02-22
qlua.nisantasi	ipekkurtalan	2021-02-22
qlua.nisantasi	iz.healthcare	2021-02-22
qlua.nisantasi	uzm.dr.yusuftopal	2021-02-22
qlua.nisantasi	gunes12k	2021-02-22
qlua.nisantasi	socialnetworknitro	2021-02-22
qlua.nisantasi	arasi_s_mama	2021-02-23
qlua.nisantasi	fenomen_ogretmen	2021-02-23
qlua.nisantasi	saricicekhulya	2021-02-23
qlua.nisantasi	borcesonguc	2021-02-23
qlua.nisantasi	meltem_ozdemir_sav	2021-02-23
qlua.nisantasi	seravarolyedek_	2021-02-23
qlua.nisantasi	nuesguzellik	2021-02-23
qlua.nisantasi	wonder_medical_technology_tr	2021-02-23
qlua.nisantasi	vildn.tk	2021-02-23
qlua.nisantasi	cam.balkon.ist	2021-02-23
qlua.nisantasi	creamygifts	2021-02-23
qlua.nisantasi	sufyansafder2002	2021-02-23
qlua.nisantasi	uzm.est.cemresaracoglu	2021-02-23
qlua.nisantasi	cgdmozp	2021-02-23
qlua.nisantasi	chichomastercom	2021-02-23
qlua.nisantasi	cigdemaltinadakaraca	2021-02-23
qlua.nisantasi	ermisneriman	2021-02-23
qlua.nisantasi	mmina.yildiz	2021-02-23
qlua.nisantasi	ysmsl2021	2021-02-23
qlua.nisantasi	mustafabogaz	2021-02-23
qlua.nisantasi	gulsegencc	2021-02-23
qlua.nisantasi	emelstcu	2021-02-23
qlua.nisantasi	gulmisali.tr	2021-02-23
qlua.nisantasi	topkaya.mine	2021-02-23
qlua.nisantasi	sevimredjep1	2021-02-23
qlua.nisantasi	betty_organizasyon	2021-02-23
qlua.nisantasi	farmasihulya___	2021-02-23
qlua.nisantasi	mervetaspinar1453	2021-02-23
qlua.nisantasi	atg.kozmetik	2021-02-23
qlua.nisantasi	kuaforismailankara	2021-02-23
qlua.nisantasi	eyess_makeup	2021-02-23
qlua.nisantasi	ceylan_tamer_k.m.u	2021-02-23
qlua.nisantasi	farmasi_5429	2021-02-23
qlua.nisantasi	tm_ithalat	2021-02-23
qlua.nisantasi	avonu_indirimli_gelis_fiyatl	2021-02-23
qlua.nisantasi	lazerepilasyoncihazi	2021-02-23
qlua.nisantasi	simurgg_guzellik	2021-02-23
qlua.nisantasi	aysem_guzellik_estetik	2021-02-23
qlua.nisantasi	sumeyyebasbugu	2021-02-23
qlua.nisantasi	fuck_it_ceramics	2021-02-23
qlua.nisantasi	tubaalayi	2021-02-23
qlua.nisantasi	geniusvelovis	2021-02-23
qlua.nisantasi	buttiksepeti	2021-02-23
qlua.nisantasi	xdd.gulsum	2021-02-23
qlua.nisantasi	semihyildirim190358	2021-02-23
qlua.nisantasi	aliyyeffa.17	2021-02-23
qlua.nisantasi	ibtis.sammar5	2021-02-23
qlua.nisantasi	kandela.mum	2021-02-23
qlua.nisantasi	aysehatundaderler	2021-02-23
qlua.nisantasi	gnscigdem	2021-02-23
qlua.nisantasi	hakaner.san	2021-02-23
qlua.nisantasi	nathaliabiancadesigner	2021-02-23
qlua.nisantasi	suzanyahyaoglu	2021-02-23
\.


--
-- TOC entry 3009 (class 0 OID 24618)
-- Dependencies: 204
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (account) FROM stdin;
baharacarofficiall
melekguzel_lik
gulsenkilicalanmakeup
ellifestetik
cihanyigitmakeup
edacakmak.phibrows
ozlemyalcin.kastasarim
crnbeautycenter
burcukeskinbicer
beautyqueenguzellikmerkezi
microartkastasarim
kas_tasarim_merkezi
mehtapcevik35
makeuptugcem
nuray_gozellik_salonu_
mia.lifeestetik
sinemceguzelliksalonu
arisguneslivip
miraycelebiii
ipek.kiprik.dilek
anexsusbeautylounge
marsbeautycenter2
aplusestetikdidim
artemissestetik
yaseminozcan_beauty
permanentmakeup_byelifbaltas
ariskaramanvip
aysetankastasarim
_sky_beautybar
ceyda_hairdresser_
kuaforerkanpinarguzellik
makeupbahar__
necla_otaci
shedibrows
sultangazimaxsisguzellik
arnavutkoymaxsisguzellik
cerendemirbeauty
moskuafor
mitramirzaii_pmu
derya_guzelliksalonu
deryaustunerbeauty
moonlightgunesli
arisusakvip
eda_hair.style_makeup
tanemguzellikmerkezi
kuaforokan
farmasi_ozleemgn
merveadak4
cigdemyavuzestetik
nurcantankisi
hairlookkbeauty
oky_cigdem
bytugbaacademy
muhteberyasar_permanentmakeup
zeynepyilmazbeauty
tugbacakmak.kaskirpiktasarim
nilayakkusbeauty
ebrudanguzellik
auraguzelliksalonueskisehir
pandora_kadikoy_vip
aliye_karatass
salon_akademi
homepilateshome
mondekuafor
byhavvakansu
ariselbistan
duyguunll
aris_corum_vip
asel_kalici_makyaj
lilium.manavgat
phibrows_sinemkasap
fulyaguzelliksalonu
elif_izerafet_kuaforgelinlik
phibrows_gulsencakar
murat.kuaforr
emsaldoganizmit
ilknur.beauty.studio
sos.hairmakeup
melisresitoglu_
denizliclinicacenter
ceydaguzellik.studyosu
a2clinic
dalmisbeauty
alin_guzellik_merkezi
serapcakinofficial
yaseminerenbeautycenter
arisistanbulceyhan
hikmetozcan.58
phibrows.bircanozcan
tenguzelliksalonu
makeup.gulsah
gulay.polat.kas.tasarim
haliskuaforveguzellik
fatmakastasarm
beautybyfundiish_memmingen
arismanisaluxe
handeugtn2
microblading_kas_bursaa
marilyn.alsancak
nehirozalbeautystudio
phibrows_cigdemtastan
kubrademir.official
trio_oznur
be.you.tifuull
hombitkisel_betul
gulsahyavas_guzellikstudio
mehmettatlierenkoy
ariskayseriluxe
altnkaya_beauty
duygukandemirmakeup
estenaz.guzellik
laledalkilic
asliyesilot
ahmetkayacoiffeur
mersinkastasarim
seymakalicimakyaj
menekse_makeup.artist
ajanslove
dermalazer
zeraguzellik
sempatibayankuaforuveguzellik
makyaj.saglik.guzellik
sevgi_ilhan_celebi
ariskonyavip
ariscankirivip
kuaforcananatesofficial
mymarke_t
elifgezer_angels
sareguzellik.konya
arisgaziantepvip
pudrakuafor
ay_nailartmakeup
ariscukurambarvip
egevelaguzellik
firatbicak.official
arisaydinvip
arissivasvip
ariselazigvip
emsaldogancayyolu
phibrows_sevalyalin
beautystudio_bnk
estetikveguzellikk
yasemintekinguzellik
gozdeyilmazbeauty
salonhaticekocak
kasdizayn_elifbilici
mujgandeligoz_hairmakeup
aristestetik
byhanova_estetikbeauty
makeupderyausta
ozgeee_ozgeee_
phibrows_dilarasahin
derinnguzelliksalonu
asli.duman88
kuafor_elif_karakas
kalici_makyaj_sanati
phibrows_ayseuzunlar
dc.guzellik_salonu
stellaestetik
sinem_gonullu
sule.dogan.18
_nesrinoguz
aalestaguzellik
annabellavip.erzincann
estebeauty.iy
maya_elit_guzellik_salonu
busecavdarofficial
ella.beautycenter
hommbitkisel1961
gulderendengiz.makeup
kibeautynisantasi
bilgedargunguzelliksalonu
nail_lashstudio
annabellavip.erzincan
nbrowss
berkaysoykan1
luxurybeautycenterofficial
dr.elnoura
beauty_sahartatoo
ozlemkuaford
unalkipritci
bdeluxeguzellik
arya_guzellik_estetik
slimfitestetik
goldess2bayankuafor
leylaghasemzade2020
primeguzellik
asdermesttik
bymehtap_beauty
makeupartist_mehtapacar
kozmetikadresiniz
nailart.sinemm
eda_by_nailart
makeupnalantnrvrdi
mayadaguzellik
derya.derya.hair.makeup
kugu_kuafor_antalya
magicbrows._
sgguzellik
alfiya_nail_lash
mcflypermanentmakeup
makeuptubatunc
arisbursaluxe
hakankaranfil_nisantasi
baharkaplanbeauty
phibrowsartist_yaseminyilmaz
emsaldogan_kayseri
permanentmakeup_duygukeder
adessma_beautysalonn
dilek.kuafor.guzellik
royal_kisisel_bakim_salonu
buketsagirguzellik
tarakuaforatasehir
pandoravipkonya
lifeart_sactasarim
gulnazbrows
vahitcinkayaofficial
ucrenkakademi
hakankaranfil_goztepe
istanbulclinicmaltepe
venusestetikmerkezi
monalisa_pendik
saloneminekaman
elvira.guzellik
estheetic_
ipek_2019kuafrvegzellik
kalicimakyajzen
zenkuaforguzellikmerkezi
essikemalpasa
kozmodernbeautyclub
4dkastasarimi
hanimicro_turkey
ozgee_makeupartist
atasoybeautycenter
gizemakgunbeauty
softestetikveguzellik
seyhanakay.guzelliksalonu
cilemonurhairstudio
phibrows_selmakaya
kuaforselmaa
keysibeautysaloon
safakparsibeauty
nejla_kuafor
nursunatelier
asivak_turkey
nasim_hatami_guzellik
nasim_hatami_kaliciguzelik
pinarbayer85
arya_estetikk
senar.incekara
sineminguzellikatolyesi
nevaguzellik
kalicimakyaj_nur
byela_beauty
hichange_belginsemiz
seher_ural
byaslihancihan
uzm.estetisyen.esra.bozkurt
necibecetinn
eyess_makeup
bluemoon_kirikkale
aysunincibeauty
deryaabasaran
irmak_kas_dizayni_guzellik
fehimedalgic_guzellik_estetik
eyebrow_sinemis
destemonakuafor
bahar_guzellik_
makeupmugekarlidag
makeupyagmuryldrm
esmira_kuafor
mugeestetik
seven_beautycenter
inovaestetikguzellik
kubrabeklebeauty
fatosozen_phibrows
kalicimakyajaysun
phibrowsserapkaragulle
cansusabaz
beautylambent
saloonreinaoffical
demakuafor21
melekakyuzbeautyandnailstudio
eda_makeupp
baharozdemir.beauty
yakutguzelliksalonu
phi_sebine
phibrows_sebine
cosmonaz_sancaktepe
didem_akkoy
rahimesain_microblading
florya.beautyline
dermopark_nigde
eda_aksoylu_medaderm
mikrokaynakmustafa
sema_poyraz_tozan
pandora_hairstudio
didemozkanbeautyacademy
hairmakeupmeryem
_estebeauty_
sudemcansumakeup
mandalaguzelliksalonu
marakeshbeauty
maral.beautystudio
arzuemre_guzellikmerkezi
monalisasaglikguzellik
slimfit_nail_studio
moykuafor
ilaydandeda
mk_turbantasarimmakeup
evrim_semirgin
cemregunayofficial
mia.lifehuseyingazii
ilke.ozdemirhan
kuafor_okan_kurunlu
y.s_kastasarim
hsnmakeup
emeloksuzbeauty
sedatbigayesim
tugcegurbuznailart
havva_karaman
pasifik_nurcanarslan
bymelikekilic
tugce_balturk
libra.cihangir
ayya_kuafor
semrakocakbeautyhair
dogalguzellikmerkezi
elmakuafor
sevimbasaranguzellikmerkezi
esteliavip_gebze
sunakaya_guzelliksalonu
cicekkarakoc_official
uzm.est.guleldemir
hairmakeupstudio_mila
makeup_cagrcan_kuafor_recep
drwell_brows
opdrcengizbozkurt
ulya_bakirova
moodbeautystudiotr
phinails_sebahatsancur
serapcinarofficial
prensesbeautylounge
svitlana.beauty
denizkayayavuz
phibrows.pinar
tameraslanhairstudio
surmeliogluofficial
hknailstudio_akademi
isil_asrin
byilaydaalim
hommcosmetic_bitkiselguzellik
lilyum_kisisel_bakm
este_rana
vedaydinguluofficial
farmasiurunleri10
nurayyildizcanakkale
aysan.vip.clinic
estebeautypazarcik
hermaguzellik
nazelinesringuzellik
fatos_yurteri
begonya_agda_guzellik_salonu
sirius_guzellik_merkezi_
selinduman_ipekkirpik
kuafor_nevlihan
kastasarimankara
rabia_makeupartist
adele_schonheitssalon_
serenbaskinbeauty
ozlem.atmacaoglu
jolie_bcs
merveciiceek
kizzcoiffureguzellik
sankuaforcorumguzellik
fi.estetikzonguldak
zemzemzeze
muzeyyenbilgin.fd
aylaermakeup
gunaytuncayy
kuaforyeniyol
arzutoker80
tugbagulhankuafor
cigdemsguzellikbakim
esteluxxestetik
eslinaestetikedirne
selmanailarttt
phibrows_esrakaraagac
gozderolofficial
beautyankaraa
yarenkuafor
zeynaguzellik
sancoiffureugur
aplusnailbeauty
nurtepeguzellik
begumkonukbeautystudio
zuhalkaratasmakeup
wellnesspointtr
prenses_kuafor_ve_moda_evi
lashes.brows.istanbul
carinacarebeauty
betulgizembaytokk
nurten_avar
medilaguzellik
lotusyoga_kuafor_guzellik
nilgunbaytok
makeup_gamze_ersoy
tuvaguzellik_makeup
ariskadikoyluxe
ecebaharbeauty_aesthetic
roselifeguzellik
dilekuzunguzellikmerkezi
serpiluzunguzelliksalonu
monalisasagguzelikantalya
dilanbeautysalon
zeynepbeautyhouse_
hairstyle_melahat
kalici.makyaj.merkezi
artestguzellik
kabukibeauty
esila_estetik_guzellik
er.guzellik
bymakeupaydannnnn
umitsaadetkaraca
blueistanbulvip
ilknurdamar_official
salon.avrupa.serap.gurbaz
taliaguzellikmerkezi
guzellikmarketim
hulya_boztoprak
cekmekoyguzellikmerkezi
nluxx.tr
makeup_sinem_oncel
hediyeguzellikmerkezi
meyspilatesbeauty
ozlemyildirimvip
sehererdem_beautystudyo
makeupduygufirat
missclassmanisa
cbmevalifee
tdestetik
diodermguzellik
est.tulayduzgun
miragecrown_
gokcecicekbeauty
love.lashes_studio
numberonekuafor
leyla_igneliepilasyon
estheticclinicall
doganildiz_
estanbulguzellik
mehmettatliatakoytowers
avon06tr
divadonnabeauty
tatalissss_permanent
limanguzelliksalonu
ahmettanis_beauty
lavi_katibeautycenter
semaozkurtbeauty
kayseriduende
este.makeup.hulya
vanessaguzellikmerkezi
beauty_master_leila
kirpiksbeautyhome
yapraknuruzmanestetisyen
artsest.folkart
aura.sinop
passionisguzellikkk
makeup_ozgeryuzlu
eleganciasalonkastamonu
nancyblogr
senay_makeup
_tugbabiyikk
arzumusalovabeauty
degisimsanat
phibrows_sulesahsuvar
istclinic
sara_tatoo_ankara
tugba.sendogan
gokbenozcanbeauty
vampbeautycenterr
sametkaraca.akademi
bibeautybybircan
adiraluxe.batman
bella_guzellik_merkezi
nrhn_huncalife1
phibrows_taylanaltinli
makeupsinemcagatay
kuafor_madamee
sinemaydinestetikguzellik
dr_alkan
eminekidalestetik
by.gulsuncansiz
sedaaltuntasbeauty
pro_retouchh
emsaldoganetiler
sevgieroglu_25
limaestetik
ayak_sagligi_estetik_merkezi
arap_makyaj_dunyasiii
arap_makyaj_dunyasii
mystilblog
eliss_guzellik_derik
elitstylewomen
berrineren_estetik_academy
selin.eyel
yellow.beautycenter
yarentinbeauty
nurayyildizsamsun
eylem_kartal1guzelikmerkezi
1aysegulcinar
ruyakuaforkirikkale
ilkaybayar_kalicimakyaj
sinem.basaran_beauty
estelika_clinic
ebruozcanestetik_guzellik
isil_eroglu
qlua_kalicimakyaj
sanat_istanbul_guzellik
bluemoonestetikveguzellik
byaynurgurses
gulhan_kazan_beauty
fusuntuncelbeauty
farmasicim_elif07
meryemuzarbeauty
senaysengulll
farmasigebze_gunay
canssumsm
zeynepyildirimkastasarim
alona.pmu
microblading_zelis
gulsenguzelliksalonuu
pinaronurofficial
didembeautycenter
fatossivasli_
nilgunhosca
bozokuaforfulya
salonbynyagmur
cuccioturkey
kozmetik.beauty
saloonelfguzellik
esteticalifeguzellik
neslimgungen_bursa
mayaluxguzellikmerkezi
phi_bernasaglam
bytugceakman
phibrows_tugceakman
dilek.dalkran
mat.kuafor
luviaestetik_
zabitpolat
aselguzelliksalonuuu
permanentmakeup_gulgun
phibrows_figentavlu
arnatural_beauty
kalicimakyajatolyesii
banuakkusguzellikmerkezi
bakirkoyguzellik2
beauty_taksim
kesantirnak
phinails__volhacoskunacademyyy
the_best_unversal_istanbul
sevgiledegisim
songullekeyiflisunumlar
gulcinpekdemirmicroblading
tugceuzpermanentmakeup
homm.bitkiselle_
hasret_tatto
zeynepustundag84
farmasi.ikizler41
beautyaynur
nursoykanbeauty
shahrzad_permanent
serapkayrakbeautybar
demet.makeupartist
bade.turgutt
lifecitytarsus
farmasi_muhtesemguzellik
shimaclinical
beauty_fairy_touch
asbeauty.tr
koksalkaplanbeautycenter
wonderfacebeauty
mombrowbeauty
beauty_lashesartist
helenestetikizmir
mervegungordu.f.d
seriyasbeauty
avjinguzellikuzmani
nurakinguzelliksalonutrb
almina_kuafor_sungurlu
sesillce
merveilk_beauty_beykent
turana.beauty
md_beauty_art_studio
guzellikkulubumodda
dr.serkan_ozturk
farmasi_online_katalog1
noblebeautty
ebubrows
hairinnsacsimulasyonu
millenium_nailpoint
hilalozkanguzellikmerkezi
fatmselen_
lavie.beautycenter
oriflamesevdan
hamiyamak
yesimyilmaz_microblading
medinedemirer_phibrows
ys_beauty_guzellik_
sultankoyunbeautycenterrr
sennabeautyalanya
makeupzonebyserpildurmus
pirilguzellikmerkezi
makeupaysenalkan
lokman_aktar_samsun
atesogluguzellikestetic
tirnakbutikcadde
mrv.kalicimakyaj.proteztirnak
nikolkuafor
beyhanatesoglu
bendisguzellikmerkezi
aylin__durgun
ecemguzellikmerkezi
roza_motlagh
estetima_guzellik
kas_tasarim_nurgul
reineestetik
sibelaydinmakeup
huseyinbektas.official
ozges_beauty
tugce_alp_beauty
kardelen.guzellik.salonu
hk.beauty.centerr
petekbebek
bestemutlumakeup
bluedermtr
elanurozturk_beauty
tugbayesilovaguzellik
oflu_ayaz_34
olibyc_lash
meryem.2604
selince_guzellik_evi
kalicimakyaj_sema
arzuerulkebas
hulya.kuaforrr
bytugbaaycan
banuparlakguzellikmaltepe
banuparlakguzelliksakarya
esteluxxestetiik
homm.bitkiselecemm
fulyabeautycenter
phibrows_pariabasiri
gulferrunutkan
saloonsguzelliksolarium
oznur_surucu_beauty_center
tirnakbutikatasehir
csbeauty.academy
esrausta9
ay.guzellik.salonu
floraguzellikmerkezii
selvi_kalicimakyaj_egitimi
farmasicim_hatice3460
oksana_peeva
bernamakeupartist
pirlantabakirkoy
aysegulgonennisantasi
makeup.artist.sehererden
bernamakeupartistt
annakuafor_antalya
humeyraakyuz07
ruyaguzellik27
artemissesenyurt
phi_nanobrowspmu_cansuaslan
cansuaslan_phiacademy
melda.buyukturk
rahsan.bilge
serapkartalbeautyart
makeupozlemboran
drosmanozcanofficial
microbladingmrsbrows
rotaestetikantalya
phibrows_yahya
erentasofficial_
semasenboke
estenormguzellikmerkezi
nesibekantarci
sinda_nermin
rujumfarmasi
salonmiracletr_aydin
superstarguzellikmerkezi
bakibijuteri
queenteambeauty
ozlemarasbeauty
gozdece_beauty
haticesaracbeauty
mila_guzelliikk
ebruliibeauty
phibrows_fisunoncul
vildanbeautycenter
beauty_engineer_hkmt
gulkaplan_salonfc
bitlisguzellikmerkezi
hera.guzellik
makbule_alanya_07
mervedonmezbeauty
zeynepguzellikk
esteticafaceclinic
sogolll.microblading
angelofbeauty
haticebeauty_bodrum
mervedabakbeauty
ela_mujde
myvogue_estetik
morlifeguzellik
secilaksoysaglik
handanfatsabeauty
jasminnailbar
akanamed.umraniye
dr.elifdagli
merveoznurbeauty
byfundabarlik
limmaestetik
mia.lifeyenimahalle
renewestetik
dilanpolatantep
kalicimakyajuzmanim
duzcesteline
santeformklinik
beriaestetik
ceylanatillabeautyacademy
dsroyalestetikguzellik
luxuryworldbeauty
cilertuna
ashrah_guzellik_merkezi
snmydin
evaguzellikmerkezi_yozgat
hilal.beauty.studio
zeynebin_guncesi_
pirlantalevent
sibeluyanacademy
lookesnisantasi
baharsencann
swarovskiguzellik
sibeluyanartofbeauty
peemekozmetik
gulayestetikguzellik
aysegulmakeup
elizanbeautycenter
byperibeauty
emsaldoganatasehir
proportionmakeup
neseguzelliksalonu
ardora.beauty
pozcu.lilium
miraybitkisel43
rotaestetikflorya
allin_beauty_istanbul
naz_ustunerr
appigmentsturkey
fatossivasli_guzellik_salonu
hayalbeauty.salon
esteliavip
selmataylistudio
sabinabaghirovaa
esraipekcii
elit.akademi.guzellik
wellnesspoint_antalya
bisabrows
est_dior.beauty
drzerclinic
hombitkiselcigdem48
drgulcingungorolcum
aybiikebeauty
ebru.roma
dilekturkvip
livinpremium
centrallifeguzellik
gulsumbingolguzellik
mirasolbeauty
mustafa.deve.33
mira_estetik_ve_guzellik
leylainanir_nisantasi
ergulkeskinofficial
longtimelinerturkey
betulbingolbeauty
betulbingolbeautycenter
thesecrettbeauty
phibrows_mekiyeaydin
unluellerguzelliksalonu
pinarbaytokkalicimakyaj
sedaaldemir_makeupstudio
mypigmentss
mineozbeybeauty
mirayefeoglu
kalicimakyajj_istanbul
fatmagulhommbitkisel_15
labellakisiselbakim
altinaybeauty_
_betultoprak_
phibrows.nejlakartal
farmasieylem58
pekinguzelliksalonu
phibrows_sebihaayan.bodrum
caprice.guzellik
caprice.guzelliksalonu
1oneriblogum
leydicecoguzelliksalonu
deluxe.estetik.guzellik
lashqueen_tr
hanifbeauty
tirnakbutik
niha_guzellik_salonu
iiiiirrrrreeeeemmmmm
zulfiyamake
ozgeozelbeautyturkey
kalicimakyajmaltepe
nesekoc_pmu
nes_guzellik
bbbeautyclinic
phibrows_helin
mclilyumguzellikk
streamofthreelife
aylaozkanmakeup
servetcetinestetik
hira_kalicimakyaj
baharimestetik
sevdazengin.kilic
kozmakeup.dunyasi
sibeldemirakademibodrum
serap.loren
seraploren.beautyconsultancy
est.nisatugrul
salonsantanaa
kyssa_nails_permanent
anka_pmu
elham_permanentmakeup
ns_guzellik
yoncaaguzellikmerkezi
phibrows_aslikoyuncu
beautybyyagmur
serpilcanikpmu
kemal._uzun27
_beysce
handyhand.beautycenter
adiguzellikbymelikeadiguzel
phibrows_nazdemirel
aysenur.kky
isabella_emineluslu
t.a_kalicimakyaj
esrahistudio
hicranbeauty_center
atiyecolaklii
petra.estetik
muge_yapar
semraguzelbeauty
zelihaayazstudio
asivak_boya_mersin
turksanatmuzigiizmir
bakirkoyesteclinic
glamguzellik
emineeceyran
zumbeautycenter
hatice.guzellik
meyrayasam
secilignecii_beauty
bybusracelik
nazlipiyalamardin
madina_makeup_lashes
armin_guzellik_merkezi
atikelerkastasarim
atikelerguzelliktunceli
seydatanirstudio
halimedogandemirbeauty
can.makeup.studio
by_juliaarabaci
nazlipiyalaclinic
nazlipiyala
muratakay_estetik
phibrows_zeynepozturk
phibrowszeynepozturk
seydahazirci
alinsbeautycenter
sibelkecelibeauty
estedore_tr
healthyish.beauty
semira_brows
uysubeautycenter
nevrayuksel
konyaguzelliksalonu.florya
justfor_beauty
yuppie.beauty.villa
brassivaestetikveguzellik
sihirlipudra
gozdestetik
beauty_pardadies
yesimcylnnn
uzm.estetisyenayselyldrm
medlife.batman
zekiye_celik34
burcunaz_phibrows
nur_degerli
begum.onel
cigdemmerten_zfc
matrushka_nail_studio
arzekr_
avonpendikmagaza
songultogrubeauty
ozgeguzellik07
saloon_aysha_zumrut
surenessguzellik
esrabykayabeauty
nihannailart
hulyauzunnn
phibrows.seydazaloglu
phibrows_damla
ferhatt_cinar.fd
rihanna_ipek_kirpik
damla_aksit
fatihdilbaz_01
rabia.alparslan.kalicimakyaj
ayguzelliikavsallar
love_guzellik_merkezi
sevilsakaa
ipek_kirpik_zsa
lilyum.beauty
muratturkelbagdatcaddesi
nursenakilic_beauty
selinkilicbeautyy
gnaguzellik
ozgeaytasguzellikatolyesi
uzm.est.damlaklc
kirpik_dersleri_online
estetisyenemineakbulut
papatyammcom
d.k.beauty_
hilalbeautynail
emsaldoganacademy
cemsirin_makeup
farmasi.sirinkeklikci
estemolguzellk
estemol.guzellik
may_vip_salonu
dr.may_klinik
yesimgorkembeauty
anna_kalicimakyaj
vanessa_guzellik_sirinmercan
es.medica
phibrows_rabia_krkmz
bugunhobimiz
lilium.epilasyon.midyat
justmebloggg
heraaltinoran
bayanika07
atolye.guzellik
miabeautyclinic
yildizarasbeauty
eylemsoyhan_phiacademy
farmasiiieylul
guzellik_atolyesi
polenakademi
maltepe.nail.studyosu
baharsertdemirbeautystudio
beautylashesym
lalunabeauty_tr
makeupsezenn
browsstudiomk
farmasi_direktor_keziban
sup.left
altunavcii
misa_guzellikestetik_merkezi
ebruguzellikmerkezi_
busrabektasbeauty
makeupgozdesenkal
pm.aziza
mehmetozturkguzellik
salonyonca
mihrikalicimakyaj
beautyangelsacademyturkiye
elizisaziye
dr._konul
nebahattuncer_ogrencileri
gnsdcl1758
minee_beautycare
gulsahcavusalp_beauty
dr.aliaydinmedikalestetik
istanbul_estetik34
hommbitkisel_rabianacak
atomy_istanbul_nihzen
semamakeupguzelliksalonu
pierrecardin_gano_oriflame
hommbitkisel397
moreandmore.global
redwinekuafor
neslihan.phiacedemy
sara.amirsalari
altamirabeauty
esteliaplus
dilekyildirimbahcelievler
bygonca_brows
natali_wow_brows
emineakkoc_kalicimakyaj
nurhanarabaci173426
hayatkozmetik
sengulbozkirbeautyland
goldenratio.yk
madamzguzelliksalonu
nihalbeautyvipcenter
gozdederelibeauty
the_gold_eskisehirr
ayyaguzellikizmir
nuryildizguzelliksalonu
melektemelofficial
nazliyalcinofficial
ilknurmakeup
basakildanbeauty
miraypermanentmakeup
burcuderican
serpil_babacan
beauty_dilek
meraladay
anda.kozmetik
ilayda.ates.kars
dermesstetik
by_elf_
kuaforcerentelek
busrayilmazbeautyhome
kirpikkasguzellikgaziantep
zeynepdemirbeauty
sevshines
therimed_guzellik
ismailkaratunc
serapgokolmez_s.r.p.cure
enesoness.hair
farmasi_iksir
suguzellikurfa
farmasii_aysecetin
sedaacarhairmakeup
edalivlog
nehirdurmusoglu
monagunenn
ayseg_ul1994
anet_lisnovska
dijitaldunyasi
laramirza_
be.you.tiful_03
figenadar
savemguzellikmerkezi
monroeguzellikmerkezi
violetguzellikmerkez
ceylanbrowbar
selenguzellikakademi
farmasi_izmir_duygu
microblading_aysen
ipek_kirpik_kas
elena_permanentmakeup
iz.beautybyzehra
dilarakayabeauty
evasamlinailsbeauty
beautydesigntr
ahu_beautycenter
vogueelegancebeauty
cansuuguzellik
zerrinbicer__beautycenter
guzelliksevinc
kadinca_kozmetikkk
didim_beautytime
kiymetmandirakalicimkyaj
guzelusmanova_bursa
hommbitkisell_ist
botox_dolgu_turkiye
nsakademi
vizyonguzellikestetik
nexusmicroblading
gzlk_uzmn_kuaforesra
nisisguzelliksalonu
uzm.estetisyen.dilekmecefoglu
songulkavakbeauty
hommsepetim
uniqueantalyaa
guldoganbeauty
kalicimakyaj.manikur.ankara
damlasasmazbeauty
dudakdolgusu_istanbull
uzman_estesyan_kosmetolog
__ess__guzellik
ckbeautybar_
saloneylulbeauty
makeuppkrc
jasminepilates_
hilalzuccaciye42
ipekarpatguzelliksalonu
permanentmakeup_aynur
ozlemsamiloglumakeup
clinicbebek
ufuksenaydin
misskettybeautycenter
uz.merveatac
melekyaman_kalicimakyaj
cbankamed
beautyloungesamsun
dore_kuaforguzellik_anamur
drsafakgoktas
dilankoroglubeauty
burcuacarofficial
studio_good_
miracle_beauty_s
olga_beautyzoone
makeup.canankapan
anjelique_beauty_ilknur
armoniguzellik
mervekaraadeniz
melek_trkoglu_
yaseminyalcinvipbeauty
kalicimakyaj.tanya
zynaydbeautystudio
emsaldogan_mersin
estelineguzelliksaglikbakim
elif.pmu
kalicimakyajserpilcakir
rcerenbeauty
imerkuafor
_zenbeautylounge
seherunver_makeupstudio
arisguzelliksiirt
nefguzellikstudyo
jahzaraguzellik
akademiroyalsakarya
sevgiguzelliksalonu_
ngbeauty_bakirkoy
demoobeauty
phibrows_basak
aycandemirbeauty
gulferunutkan
essenovabeauty
sasha_guzellik_salonu
sirius_beauty_center_konya
farmasi_satis3838
drmuratkocyigit
newlife_estetik
saliha.oriflame
salihe_ramaza
ahilas_003
oriflame1kozmetik
edakerime
afet_rahmanova
sibeldemirmakeup
ipeksiestetik
seyda_kaya_beauty
frmsakarya
guzellik_ve_ask
banuozcelikguzelliksalonu
microblading0908
ro_beautyhome
merickuafor
nadiyemesutogluguzellik
ceylan.erdogan.77
zk_guzellik_kuafor_salonu
aygularslan_makeup
farmasi_kendini.sev
carsi.pazar46
masome.phibrows
yesimkanburphibrows
pinarr.sarii
kozmetikciniz_ayse
phi_face
sibel_tekbaran
selmaserpermanentmakeup
selaresguzellik
nilsahars
lutfiye.lazena
assistant.beauty
phibrows.nesrinkaral
salon_zeyneppp
minebeautyofart
basak.ozsoy.pmu
ftosyldz
earthkozmetik
gonca_askar.kasdizayn
estalya_guzellik
menakozmetik
milabeautybysemihanur
rabiacetinbeauty
estetikmoonlight
satibabacan
farmasi_farmasiset
emsaldoganankara
ipektenestetik.duygu
fatosulger_official
mugekepenekbeautycenter
arisistanbulsilifkesube
nurhanayy730
ppinardagdeviren
fuat.tekedereli
sevcan.beauty
egemendelux
pinarpinarguzellik
pudraakokusu
dileksbeauty
hanife_kosmetolog
byzeynepalay
artistyutta
farmasi._.sirnak
hazalatakbeauty
enkozmetiks
naturelguzelliksalonu.bandirma
afroditguzelliksefakoy
cansusaribeautycenter
makeuptocare
sedefbeautystudio
arisuskudarvip
pnr.svgi
semakorkmazerbeauty
denizliguzellikmerkezi
profdryeldakapicioglu
saracikeliff
emotion_58
queenbeautyantalya
vegabeautycenter
c_o_phibrows
glowybeytepe
makeup.by_anastasia
farmaasi.01
sistaservicebeauty
yaseminn_arac
apak_sifa
artofhair_byozlemberker
basaksehirartofhair
labonsbeautyclub
olga_tirnak_mavisehir
\.


--
-- TOC entry 2874 (class 2606 OID 24625)
-- Name: users users_account_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_account_key UNIQUE (account);


-- Completed on 2021-03-07 00:29:47

--
-- PostgreSQL database dump complete
--

