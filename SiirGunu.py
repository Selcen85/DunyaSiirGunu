import streamlit as st
import random
import time

# 1. Sayfa Ayarları
st.set_page_config(page_title="21 Mart Dünya Şiir Günü", page_icon="🖋️")

# --- KURUMSAL LOGO LINKI ---
# Buraya okulunuzun logosunun internetteki .png veya .jpg linkini yapıştırın.
# Eğer linkiniz yoksa, örnek bir logo linki bıraktım, onu değiştirebilirsiniz.
OKUL_LOGO_LINKI = "https://i.hizliresim.com/qiyfcs7.png"

# --- ESKİTME TASARIM VE VINTAGE YAPRAKLAR (CSS) ---
st.markdown("""
    <style>
    /* Ana Arka Plan Ayarları: Eskitilmiş Kağıt Dokusu ve Vintage Süsler */
    [data-testid="stAppViewContainer"] {
        background-color: #f3ead8 !important; /* Eskitilmiş kağıt tonu */
        background-image: 
            url("https://www.transparenttextures.com/patterns/natural-paper.png"), /* Hafif doku */
            url("https://img.icons8.com/ios/100/7d5a50/vintage-wrapper.png"),    /* Sol Üst Süs */
            url("https://img.icons8.com/ios/150/7d5a50/quill-with-ink.png");      /* Sağ Alt Tüy */
        background-position: center, left 20px top 20px, right 30px bottom 30px !important;
        background-repeat: repeat, no-repeat, no-repeat !important;
        background-attachment: fixed !important;
        background-size: auto, 80px, 150px !important;
        opacity: 0.96;
    }

    /* Yazı Tipi ve Genel Renkler */
    html, body, [class*="css"] {
        font-family: 'Georgia', serif !important; /* Klasik kitap fontu */
        color: #3e2723 !important; /* Mürekkep kahverengisi */
    }

    /* Şiir Kutusu Tasarımı */
   code {
        background-color: rgba(255, 255, 255, 0.5) !important; /* Biraz daha belirgin beyazlık */
        color: #1a1a1a !important; 
        font-size: 1.25rem !important;
        line-height: 1.6 !important;
        border: none !important;
        border-left: 5px solid #7d5a50 !important; 
        border-radius: 8px !important;
        padding: 25px !important;
        
        /* ÖNEMLİ: Tüm metni normal font kalınlığına zorlar, parlamaları engeller */
        font-weight: 400 !important; 
        white-space: pre !important; /* Mısra yapısını korur */
        display: block !important;
        font-family: 'Georgia', serif !important; /* Daktilo fontu yerine edebi font */
    }

    /* Buton Tasarımı */
    .stButton>button {
        border-radius: 20px !important;
        background-color: #7d5a50 !important; /* Vintage kahverengi */
        color: #f3ead8 !important; /* Arka plan tonunda yazı */
        border: 2px solid #3e2723 !important;
        padding: 12px 30px !important;
        font-weight: bold !important;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5d4037 !important;
        border-color: #f3ead8 !important;
    }

    /* Şiir Başlığı Stili */
    .siir-baslik {
        font-weight: bold !important;
        color: #2c1e12 !important;
        font-size: 1.3rem !important;
        margin-bottom: 5px;
        display: block;
        text-decoration: underline;
    }

    /* Şiir İçeriği Stili */
    .siir-icerik {
        font-weight: normal !important;
    }
    </style>
    """, unsafe_allow_html=True)


# 2. Şiir Listesi (Tüm gönderdiklerin dahil edildi)
siirler = [
    """Hoş Geldin Kadınım 
Hoş geldin kadınım benim hoş geldin 
yorulmuşsundur; 
nasıl etsem de yıkasam ayacıklarını 
ne gül suyum ne gümüş leğenim var, 
susamışsındır; 
buzlu şerbetim yok ki ikram edeyim 
acıkmışsındır; 
beyaz ketenli örtülü sofralar kuramam 
memleket gibi yoksuldur odam. 
Hoş geldin kadınım benim hoş geldin 
ayağını bastın odama 
güldün, 
kırk yıllık beton, çayır çimen şimdi 
güller açıldı penceremin demirlerinde 
ağladın, 
avuçlarıma döküldü inciler 
gönlüm gibi zengin 
hürriyet gibi aydınlık oldu odam… 
Hoş geldin kadınım benim hoş geldin.  - Nazım Hikmet""",

    """66. SONE 
Vazgeçtim bu dünyadan tek ölüm paklar beni, 
Değmez bu yangın yeri, avuç açmaya değmez. 
Değil mi ki çiğnenmiş inancın en seçkini, 
Değil mi ki yoksullar mutluluktan habersiz, 
Değil mi ki ayaklar altında insan onuru, 
O kız oğlan kız erdem dağlara kaldırmış, 
Ezilmiş, hor görülmüş el emeği, göz nuru, 
Ödlekler geçmiş başa, derken mertlik bozulmuş, 
Değil mi ki korkudan dili bağlı sanatın, 
Değil mi ki çılgınlık sahip çıkmış düzene, 
Doğruya doğru derken eğriye çıkmış adın, 
Değil mi ki kötüler kadı olmuş Yemen’e 
Vazgeçtim bu dünyadan, dünyamdan geçtim ama 
Seni yalnız komak var, o koyuyor adama. 
Çeviren: Can Yücel  - William Shakespeare""",

    """VEDA 
Hani o bırakıp giderken seni 
Bu öksüz tavrını takmayacaktın? 
Alnına koyarken veda buseni 
Yüzüme bu türlü bakmayacaktın? 
Hani ey gözlerim bu son vedada, 
Yolunu kaybeden yolcunun dağda 
Birini çağırmak için imdada 
Yaktığı ateşi yakmayacaktın? 
Gelse de en acı sözler dilime 
Uçacak sanırdım birkaç kelime... 
Bir alev halinde düştün elime 
Hani ey gözyaşım akmayacaktın? - Orhan Seyfi Orhon""",

    """TELEFON 
Gözlerin var ya çekik kara kara 
Önce gözlerindi en güzel ışık 
Beyaz dişlerindi bacakların omuzun 
Damalı örtüde bir kase çorba gibi 
Buğulu bir lezzetti karı kocalık 
Şimdi bir çınar yeşeriyor içimde 
Bir şarkı söylenir uzun uzun 
Hürriyetin rüzgârlı bayrağı oldu 
Bize yeten aydınlığı sevdamızın 
Aman dayanamazsam ne etmeli -Bütün pencereler üstlerine açık 
Kimler soyar çocukları kimler örter 
Biri on bir yaşında öteki küçük 
Ya anne diye bağırırsa uykusunda 
Belki korkmuş belki de susamıştır 
Geceleri su içmeye alışık 
Çorap öyle mi giydirilir don öylemi bağlanır 
Gömleği bir tuhaf sarkıyor arkasında 
Çocuklara bakma dayanırım 
Gide gide çoğaldım halkım ben artık 
Dağ taş kalabalık kalabalık 
Satarmıyım onları onlar da çocuklarım 
Ben kadınım çocuklarımla varım 
Telefon nafile açmam seni 
Söylemez dillerim yarınla bağlı 
Tutmaz parmaklarım kocamdan belli 
Telefon benimki de analık 
Çocuklara bakma dayanırım 
Sevgiydim önce bir çeşit incelik 
Şimdi ise yarıyorum kaba saba 
Tuzlu bir deniz kokusu havada 
Benimle başladı bu müthiş tazelik 
Benimle yaklaştı güzel günler 
O günlerin eşiğinde beni hatırlayın 
Hatırlayın onların vahşetini 
Her telefon çalışta kesik kesik  - Oktay Rıfat Horozcu""",

    """KARIMA 
Sofalar seninle serin 
Odalar seninle ferah 
Günüm sevinçle uzun 
Yatağında kalktığım sabah 
Elmanın yarısı sen yarısı ben 
Günümüz gecemiz evimiz barkımız bir 
Mutluluk bir çimendir bastığın yerde biter 
Yalnızlık gittiğin yoldan gelir - Oktay Rıfat Horozcu""",

    """OLVİDO 
Hoyrattır bu akşamüstleri daima. 
Gün saltanatıyla gitti mi bir defa 
Yalnızlığımla doldurup her yeri 
Bir renk çığlığı içinde bahçemizden, 
Bir el çıkarmaya başlar bohçamızdan 
Lavanta çiçeği kokan kederleri; 
Hoyrattır bu akşamüstleri daima. 
Dalga dalga hücum edip pişmanlıklar 
Unutuşun o tunç kapısını zorlar 
Ve ruh, atılan oklarla delik deşik; 
İşte, doğduğun eski evdesin birden 
Yolunu gözlüyor lamba ve merdiven, 
Susmuş ninnilerle gıcırdıyor beşik 
Ve cümle yitikler, mağluplar, mahzunlar… 
Söylenmemiş aşkın güzelliğiyledir 
Kağıtlarda yarım bırakılmış şiir; 
İnsan, yağmur kokan bir sabaha karşı 
Hatırlar bir gün bir camı açtığını, 
Duran bir bulutu, bir kuş uçtuğunu, 
Çöküp peynir ekmek yediği bir taşı… 
Bütün bunlar aşkın güzelliğiyledir. 
Aşklar uçup gitmiş olmalı bir yazla 
Halay çeken kızlar misali kolkola. 
Ya sizler! Ey geçmiş zaman etekleri, 
İhtiyaç ağaçlı, kuytu bahçelerden 
Ayışığı gibi sürüklenip giden; 
Geceye bırakıp yorgun erkekleri 
Salman etekler fısıltıyla, nazla. 
Ebedi aşığın dönüşünü bekler 
Yalan yeminlerin tanığı çiçekler 
Artık olmayacak baharlar içinde. 
Ey, ömrün en güzel türküsü aldanış! 
Aldan, geçmiş olsa bile ümitsiz kış; 
Her garipsi ayak izi kar içinde 
Dönmeyen aşığın serptiği çiçekler. 
Ya sen! Ey sen! Esen dallar arasından 
Bir parıltı gibi görünüp kaybolan 
Ne istersin benden akşam saatinde? 
Bir gülüşü olsun görülmemiş kadın, 
Nasıl ölümsüzsün aynasında aşkın; 
Hatıraların bu uyanma vaktinde 
Sensin hep, sen, esen dallar arasından. 
Ey unutuş! kapat artık pencereni, 
Çoktan derinliğe çekmiş deniz beni; 
Çıkmaz artık sular altından o dünya. 
Bir duman yükselir gibidir kederden 
Macerası çoktan bitmiş o şeylerden. 
Amansız gecenle yayıl dört yanıma 
Ey unutuş! Kurtar bu gamlardan beni.  - Ahmet Muhip Dıranas""",

    """SERENAD 
Yeşil pencerenden bir gül at bana, 
Işıklarla dolsun kalbimin içi. 
Geldim işte mevsim gibi kapına 
Gözlerimde bulut, saçlarımda çiğ. 
Açılan bir gülsün sen yaprak yaprak 
Ben aşkımla bahar getirdim sana; 
Tozlu yollarından geçtiğim uzak 
İklimden şarkılar getirdim sana. 
Şeffaf damlalarla titreyen, ağır 
Koncanın altında bükülmüş her sak. 
Seninçin dallardan süzülen ıtır, 
Seninçin karanfil, yasemin zambak… 
Bir kuş sesi gelir dudaklarından; 
Gözlerin, gönlümde açan nergisler. 
Düşen öpüşlerdir dudaklarından 
Mor akasyalarda ürperen seher. 
Pencerenden bir gül attığın zaman 
Işıkla dolacak kalbimin içi. 
Geçiyorum mevsim gibi kapından 
Gözlerimde bulut, saçlarımda çiğ. - Ahmet Muhip Dıranas""",

    """KARŞI 
Gerin, bedenim, gerin; 
Doğan güne karşı. 
Duyur duyurabilirsen, 
Elinin kolunun gücünü, 
Ele güne karşı. 
Bak! Dünya renkler içinde! 
Bu güzel dünya içinde 
Sevin sevinebilirsen 
İnsanlığın haline karşı. 
Durmadan isliden saatlerde 
Dişli dişliye karşı; 
Dişlilerin arasında, 
Güçsüz güçlüye karşı. 
Herkes bir şeye karşı. 
Küçük hanım, yatağında, uykuda, 
Rüyalarına karşı. 
Gerin, bedenim, gerin, 
Doğan güne karşı. - Orhan Veli Kanık""",

    """ANLATAMIYORUM 
Ağlasam sesimi duyar mısınız, 
Mısralarımda; 
Dokunabilir misiniz, 
Gözyaşlarıma, ellerinizle? 
Bilmezdim şarkıların bu kadar güzel, 
Kelimelerinse kifayetsiz olduğunu 
Bu derde düşmeden önce. 
Bir yer var, biliyorum; 
Her şeyi söylemek mümkün; 
Epeyce yaklaşmışım, duyuyorum; 
Anlatamıyorum. - Orhan Veli Kanık""",

    """SARHOŞ GEMİ 
Ölü sularından iniyordum nehirlerin 
Baktım yedekçilerim iplerimi bırakmış 
Cırlak kızıl deriler, nişan atmak için 
Hepsini soyup alaca direklere çarpmış. 
Bana ne tayfalardan; umrumda değildi 
Pamuklar, buğdaylar, Felemenk ve İngiltere; 
Bordamda gürültüler, patırtılar kesildi; 
Sular aldı gitti beni can attığım yere. 
Med zamanları, çılgın çalkantılar üstünde, 
Koştum, bir çocuk beyni gibi sağır, geçen kış; 
Adaların karalardan çözüldüğü günde 
Yeryüzü böylesine allak bullak olmuş. 
Denize bir kasırgayla açıldı gözlerim; 
Ölüm kervanı dalgaları kattım önüme; 
Bir mantardan hafif, tam on gece, hora teptim; 
Bakmadım fenerlerin budala gözlerine. 
Çocukların bayıldığı mayhoş elmalardan 
Tatlıydı çam tekneme işleyen yeşil sular; 
Ne şarap lekesi kaldı, ne kusmuk yıkanan 
Güvertemde; demir, dümen ne varsa tarumar. 
O zaman gömüldüm artık denizin şi’irine, 
İçim dışım süt beyaz köpükten, yıldızlardan; 
Yardığım yeşil maviliğin derinlerine 
Bazen bir ölü süzülürdü, dalgın ve hayran. 
Sonra birden mavilikleri kaplar meneviş 
Işık çağıltısında, çılgın ve perde perde 
İçkilerden sert, bütün musukilerden geniş 
Arzu, buruk ve kızıl, kabarır denizlerde. 
Gördüm şimşekle çatlayıp yarılan gökleri 
Girdapları, hortumu; benden sorun akşamı, 
Bir güvercin sürüsü gibi savrulan fecri. 
İnsana sır olanı, gördüğüm demler oldu. 
Güneşi gördüm, alçakta, kanlı bir ayinde; 
Sermiş parıltısını uzun mor pıhtılara. 
Eski bir dram oynuyor gibiydi, enginde, 
Ürperip uzaklaşan dalgalar, sıra sıra. 
Yeşil geceyi gördüm, ışıl ışıl karları; 
Beyaz öpüşler çıkar denizin gözlerine, 
Uyanır, çın çın öter fosforlar, mavi sarı; 
Görülmedik sular geçer derinlerinden döne döne. 
Azgın boğalar gibi kayalara saldıran 
Dalgalar aylarca sürükledi durdu beni; 
Beklemedim meryemin nurlu topuklarından 
Kudurmuş denizlerin imana gelmesini. 
Ülkeler gördüm görülmedik, çiçeklerini 
Gözler karışmış, insan yüzlü panter gözleri; 
Büyük ebemkuşakları gerilmiş engine, 
Morarmış sürüleri çeken dizginler gibi 
Bataklıklar gördüm, geniş fıkır fıkır kaynar; 
Sazlar içinde çürür koskoca bir ejderha, 
Durgun havada birden bire yarılır sular, 
Enginler şarıl şarıl dökülür girdaplara 
Gümüş güneşler, sedef dalgalar, mercan gökler; 
İğrenç leş yığınları boz, bulanık koylarda; 
Böceklerin kemirdiği dev yılanlar düşer, 
Eğrilmiş ağaçlardan simsiyah kokularla. 
Çıldırırdı çocuklar görseler mavi sularda 
O altın, o gümüş, cıvıl cıvıl balıkları. 
Yürüdüm beyaz köpükler üstünde, uykuda 
Zaman zaman kanadında bir cennet rüzgârı. 
Bazen doyardım artık kutbuna, kıtasına; 
Deniz şıpır şıpır kuşatır sallardı beni; 
Garip sarı çiçekler sererdi dört yanıma; 
Duraklar kalırdım düz çökmüş bir kadın gibi.
Sallanan bir ada; üstümde vahşi kuşlarım 
Bal rengi gözleri, çığlıkları, pislikler; 
Akşamları, çürük iplerinden akın akın 
Ölüler inerdi uykuya gerisin geri. 
İşte ben, o yosunlu koylarda yatan gemiyim 
Bir kasırgayla atıldım kuş uçmaz engine; 
Sızmışken kıyıda, sularda sarhoş; gövdemi 
Hanza kadırgaları takamazken peşine. 
Büründüm mor dumanlara, başı boş, derbeder, 
Delip geçtim karşımdaki kızıl semaları; 
Güvertemde cins şaire mahsus yiyecekler: 
Güneş yosunlan, mavilik meduzaları. 
Koştum, benek benek ışıklara sarılı teknem, 
Çılgın teknem, ardında yağız denizatları, 
Temmuz güneşinde sapır sapır dökülürken 
Kızgın hunilere koyu mavi gök katları. 
Titrerdim uzaklardan geldikçe iniltisi 
Azgın Behemotların, korkunç Maelstromların. 
Ama ben, o mavi dünyaların serserisi 
Özledim eski hisarlarını Avrupa’nın. 
Yıldız yıldız adalar, kıtalar gördüm; coşkun 
Göklerinde gez gezebildiğin kadar, serbest. 
O sonsuz gecelerde mi saklanmış uyursun 
Milyonlarla altın kuş, sen ey gelecek kudret.
Yeter, yeter, ağladıklarım; artık doymuşum 
Fecre, aya, güneşe; hepsi acı, boş, dipsiz; 
Aşkın acılığı dolmuş içime, sarhoşum; 
Yarılsın artık bu tekne, alsın beni deniz. 
Gönlüm avrupanın bir suyunda, siyah, soğuk, 
Bir çukurda birikmiş kokulu akşam vakti; 
Başında çömelmiş yüzdürür mahzun bir çocuk 
Mayıs kelebeği gibi kağıt gemisini. 
Ben sizinle sarmaş dolaş olmuşum, dalgalar; 
Pamuk yüklü gemilerin altında gezemem 
Doyurmaz artık bayraklar, bandıralar 
Mahkum gemilerinin sularında yüzemem 
Çeviren: Sabahattin Eyüboğlu - Arthur Rimbaud""",

    """GÜZ 
Çiçeğin rengi soldu, bitti şarkısı kuşun. 
Yol tenha, dal mecâlsiz, su durgun. 
Tabut yapılan tahta, ev ev taşınan odun. 
Bahar, ümit yerine, ey kış, içimde korkun! 
Allah’ım! kararmasa şu göğün... 
Dal senin, ağaç senin, döktüğün 
Yapraklarla, mevsimlerle, gün gün. 
Geçip gidişi ömrün... - Ziya Osman Saba""",

    """NEFES ALMAK 
Nefes almak, içten içe, derin derin, 
Taze, ılık, serin, 
Duymak havayı bağrında. 
Nefes almak, her sabah uyanık. 
Ağaran güne penceren açık. 
Bir ağaç gölgesinde, bir su kenarında. 
Üstünde gökyüzü, ufuklara karşı. 
Senin her yer: Caddeler, meydan, çarşı... 
Kardeşim, nefes alıyorsun ya! 
Koklar gibi maviliği, rüzgârı öper gibi, 
Ananın südünü emer gibi, 
Kana kana, doya doya... 
Nefes almak, kolunda bir sevgili, 
Kırlarda, bütün bir pazar tatili. 
Bahar, yaz, kış. 
Nefes almak, akşam, iş bitince, 
Çoluk çocuğunla artık bütün gece, 
Nefesin nefeslere karışmış. 
Yatakta rahat, unutmuş, uykulu, 
Yanında karına uzatıp bir kolu, 
Nefes almak. 
O dolup boşalan göğse... 
Uyumak, sevmek nefes nefese, 
Kalkıp adım atmak, tutup ıslık çalmak. 
Sürahide, ışıl ışıl, içilecek su. 
Deniz kokusu, toprak kokusu, çiçek kokusu. 
Yüzüme vuran ışık, kulağıma gelen ses. 
Ah, bütün sevdiklerim, her şey, herkes... 
Anlıyorum, birbirinden mukaddes, 
Alıp verdiğim her nefes.  - Ziya Osman Saba""",

    """SON 
İçimden hep iyilik geliyor 
Yaşadığımız dünyayı seviyorum 
Kin tutmak benim harcım değil 
Çektiğim bütün sıkıntıları unuttum 
Parasız pulsuzum ne çıkar 
Gelecek güzel günlere inanıyorum 
Gelecek güzel günlere 
Sonunda galip geleceğine eminim 
İyiliğin, zekânın ve cesaretin 
İmanım var zaferine 
Aşkın, adaletin ve hürriyetin 
Yetiştiğim halkın içinde 
Bütün şiirini duydum 
Çalışmanın ve sefaletin 
Kulak verin işe gidenlerin türkülerine 
Yorgun argın dönüşlerini seyredin. 
Şairleri peygamberleri düşünüyorum 
Yaşamak o kadar tatlı ki 
Daimî bir sevgi içinde 
Galip sesini işitiyorum hakkın 
Asırlarca zulme ve işkenceye 
Gelecek güzel günlere inanıyorum 
İmanım var bereketine toprağın 
Ve makinenin kudretine 
Parasızım pulsuzum ne çıkar 
Huzuru içindeyim rahata kavuşanların 
Hayatının son senelerinde. -Necati Cumalı""",

    """A BE CE 
Güzelliğini düşün bir 
İnci gibi harflerin 
Kuş tüyü, kamış, ağaç ya da divitin 
Ucunda a be ce... 
Kıvraklığını düşün dilin 
Akarsuyun, ay ışığının 
Yapraklarla oynaşan yelin 
Dağılan köpüğün 
Saçılan dantelin 
Şiirin, öykünün, denemenin 
Sıcaklığını düşün 
Bir sevda öpücüğü 
Dost eli 
Kimi zaman kıvrak, şen 
Kimi zaman kederli 
Saran, sürükleyen düşüncenin 
Tutkulu, candan, yürekten 
Ak kağıda kara oya 
Balçığa, mermere, zamana işlenen 
A be ce... - Kemal Burkay""",

    """ŞU GİDEN ATLIYA TÜRKÜ 
Ben demedim mi 
Hazırlandılar 
Onların yüz bin kolları var 
Kırbaçları sert, yamçıları sağlam, atları kavi 
Yeğin git kese sür atınla birleş 
Ben demedim mi 
Ben demedim mi 
Tekin değil koyaklar, dağ yamaçları 
Yağmur yağar ki sis basar ki kurt iner ki 
Ay bulanığında gümüş rengi çakallar 
Ben demedim mi 
Yalnız gitme demedim mi 
Çiğdeme sor, chşmeye sor 
Tek açan menevşeye sor 
Ayrılık getirir ayrılıklar 
Birleş demedim mi 
Ben demedim mi  - Gülten Akın""",

    """BİR KAYIĞA BİNER GECELERİ 
Tadını, yağmura duygulanmanın 
Paylaşır kuşlarla biri gizlice 
Gülmesini tutamamış bir sincap 
Sallanır utanç bahçesinde 
Yalnız atlar yıkılır düzlerde suya özlemlerinden 
Bir ben miyim yalnızlığa yenilen, sen, sen, sen 
Uzun sokakların ucunda evleri 
İlk denemelerden geri dönülmüştür 
İtildikçe, içe durduğu bilinen 
Bazı dostları yitirmeye gidilir 
Yalnız atlar yıkılır düzlerde suya özlemlerinden 
Bir ben miyim yalnızlığa yenilen, sen, sen, sen 
Bir kayığa biner geceleri 
Sığlıkta o kadın tek başına 
Dua biçiminde inceltir korkuyu 
Sunar içtenliksiz, tanrısına 
Yalnız atlar yıkılır düzlerde suya özlemlerinden 
Bir ben miyim yalnızlığa yenilen, sen, sen, sen - Gülten Akın""",

    """SAFRANBOLU’DA ESKİ BİR GÜNEŞ SAATİ 
azıcık hüzün yakışır sana 
azıcık okuldan kaçan çocuklar 
bir paket birinci cigarası 
azıcık yalnızlık yakışır sana 
yani Lonca 
atarabaları nazarlıklar 
mermere tunca söze zamana 
nakışlı adın 
usta bir hattat gibi adın 
bir tespihçi bir sedefkâr gibi 
hicazkâr şarkılardır yadigarın 
ya da Sadi Yaver Ataman 
Köprülü Mehmet Paşa 
Mimar İnce Yavuz 
sen ki laciverdi bir gökyüzünün 
en parlak yıldızıydın 
hâlâ mum yakıp 
dilek tutuyor mu 
alfabeye başlayan çocukların  
deli bir sultan bile kayırmış seni 
kervanlarının sesi duyulur 
beyaz evlerin varken 
ut çalınırken sofalarında 
anıtlaşan bir uygarlıksın 
bir geçmiş zamanı 
bir Cenevizliden bir Selçukludan öğrenirim 
bakarım ufkundaki tükenmeyen serapa 
jaaz değil 
ut sesleri yakışır sana 
bindallı kızların 
ve çocukluğumun küçük sinemalarına 
beni götüren arnavut kaldırımların 
anlamıyorum tecimenlerin töresini 
loncalı ustamdan kaldı bu kundura 
nargileydi çarşı kahvesinde 
ustamın fiyakası 
şimdi çayların eski tadı yok 
ben beni özleyen bu şehirde 
neden sultan değilim- Hüseyin Avni Cinozoğlu""",

    """MACAR RAPSODİSİ 
Dr. Hartha’ların ölümsüz anılarına 
Macar ovalarında ve Tuna kıyısında 
Martha’nın gözlerinde ve bütün şarkılarda 
Ve kurşuna dizilen gençlerin avucunda 
Barut isine batmış bayraklarla beraber 
Peşte sokaklarında tankların çiğnediği 
Genç yürekler içinde üç renkli şafak 
Sen gözyaşları, alınteri, en büyük sevda… 
Sen, yirminci yüzyılda hukuk kitaplarında 
Ve tekmil nutuklarda ismi geçen 
İnsanoğlunun beyninde, namlu arpacığında 
Doğacak çocuğumun gelecek ninnisinde 
Ve güzelim denizlerin tuzundaki lezzet 
Şakaklarımızda zonklayan kavga 
Ve cümle mahkûmların rüyası 
Ey hürriyet! 
Ve sen, gerçek insanı yaratamayan insan 
Sen, ey kardeş kanıyla beslenen insanoğlu! 
Yangın başladı Peşte’de… Kardeşim, yangın! 
Taze göğüsler üstünde tanklar horada 
Sevgilim alevler içinde, sevgilim orada 
Tutulmuş bütün caddeler, tutulmuş 
Yanına varamıyorum 
Sanırsın anacığım boğazlanıyor 
Kurtaramıyorum… 
El yordamıyla, tıkanmış sokaklarda 
Ey ölümsüz şarkı, ey merhamet
Seni bulamıyorum! 
Utanıyorum kendimden, petekteki arıdan 
Bir başka yıldıza göç etmek istiyorum… 
Utanıyorum buluttan, kımıldanan topraktan 
Dağdaki kurttan, kuştan 
Aslan yavrusu emziren ceylandan 
İnsanlığımdan utanıyorum 
Oysaki insanlığın tekmil antenleri 
Peşte üstündedir… 
Oysaki insanlığın Magna Carta’dan bu yana 
Nice özgürlük antlaşmasına kanıyla imza koymuş 
En yakışıklı oğullarını bu yola kurban etmiş 
Ve bir zerresi için 
Nice can satmıştır… 
Utanıyorum kendimden kardeşim 
Aynalara bakamıyorum! 
Nerde kaldı çigan havaları, o çılgın kemanlar 
Nerde dudak dudağa sevgililer? 
Duyuyor musunuz şair Petöfi’nin sesini 
Duyuyor musunuz tankların homurtusunda 
Macar Rapsodisi’ni? 
Biç beni, makineli tüfekle biç 
Öldüremezsin! 
Çıkar şarkılardan ve cümle kitaplardan adımı 
Yine de silemezsin! 
Ben, hayır ve şer misali insan kanındayım 
1789’da ve Türk ihtilali’ndeyim! 
Bugün bir tomurcukta, yarın darağacındayım 
Ben, ne satılacak dava, ne kemik, ne etim 
Ben, ölümsüzlüğün elindeki bayrak, 
Ben, hürriyetim! - Şinasi Özdenoğlu""",

    """SU 
Su yok, toprak çatlıyor 
Çekti elini bulutlar, 
Gökyüzü taş 
Korkusu büyüyor karanlığın 
Düştükçe içimize 
Yeryüzü kum 
Bir alaca çırpınış var 
Kendine kıyıyor toplum, 
Sular kan - Yekta Güngör Özden""",

    """İSTEMEM 
Bir mavi akşam mıydı üstümüze düşen 
Ya da dalları mı anıların 
Yaprak yaprak dökülen. 
Bilmeyiz nerde başlar, nerde biter 
Bu zehir zemberek karanlık, 
ve öldürülen yalnızlık 
Yüreğimize çöken 
bir renkle yıkanır düşlerin dizinde 
Beni ben yapan düşüncem, 
Ben bana yetiyorum 
başka bir şey istemem. - Yekta Güngör Özden""",

    """AŞK İKİ KİŞİLİKTİR 
Değişir rüzgârın yönü 
Solar ansızın yapraklar; 
Şaşırır yolunu denizde gemi 
Boşuna bir liman arar; 
Gülüşü bir yabancının 
Çalmıştır senden sevdiğini; 
İçinde biriken zehir 
Sadece kendini öldürecektir; 
Ölümdür yaşanan tek başına 
Aşk iki kişiliktir. 
Bir anı bile kalmamıştır 
Geceler boyu sevişmelerden; 
Binlerce yıl uzaklardadır 
Binlerce kez dokunduğun ten; 
Yazabileceğin şiirler 
Çoktan yazılıp bitmiştir; 
Ölümdür yaşanan tek başına, 
Aşk iki kişiliktir. 
Avutamaz olur artık 
Seni bildiğin şarkılar; 
Boşanır keder zincirlerinden 
Sular tersin tersin akar; 
Bir hançer gibi çeksen de sevgini 
Onu ancak öldürmeye yarar: 
Uçarı kuşu sevdanın 
Alıp başını gitmiştir; 
Ölümdür yaşanan tek başına, 
Aşk iki kişiliktir. 
Yitik bir ezgisin sadece, 
Tüketilmiş ve düşmüş, gözden. 
Düşlerinde bir çocuk hıçkırır 
Gece camlara sürtünürken; 
Çünkü hiç bir kelebek 
Tek başına yaşayamaz sevdasını, 
Severken hiçbir böcek 
Hiçbir kuş yalnız değildir; 
Ölümdür yaşanan tek başına, 
Aşk iki kişiliktir.- Ataol Behramoğlu""",

    """SİZİN İÇİN GÜNLERDİR PUL BİRİKTİRİYORUM 
dün sesiniz kalmıştı durakta 
arkanızdan yetişemedim 
bari şimdi dinleyin lütfen 
kanat uçup durmasın adımlarınız 
günler var ki size niyetliyim 
ama hep böyle durgun dudaklısınız 
Çok mu gevezeyim - 
haklısınız... 
bir tarihiniz vardır elbette 
peki ya coğrafyanız 
küçük bir gezinti yapardık sizinle 
sözcüklerinize kadar ıslanırdınız 
yanlış anlamayın lütfen 
birlikte kaynardı suyumuz 
Çok mu cüretliyim - 
haklısınız... 
size dokunsam - biliyorum - hükümet sarsılır ama 
bir ah ile bu alemi viran ederim ben de 
divan şairleri bile söyleyemez bu lafı 
inanır mısınız 
öyle bakmayın lütfen 
yalan söyleyecek değilim ya göz göre göre 
hem bir tutuşursam dilimde patlarsınız 
Çok mu serseriyim - 
haklısınız 
ama siz tam da bu şiirin fikrisiniz - Enver Ercan""",

    """GÖZLERİ ÖZGÜRLÜĞÜN 
Her gün karanfil kokmazdı 
Her bulut taşımazdı yağmur. 
Dalgalar düşmandı gözlerine, 
Gözleri nar çiçeği... 
Güneşi sağardık her bağbozumu 
Yön yitiren tarla kuşlarıydı gülen. 
Eski çerçeveli fotoğraflardan. 
Çocuklar çığlıklarla doğardı 
Çocuklar su. 
Çocuklar dalgaları taşırdı okyanuslardan 
Ve kuş üzümlerini 
Babil’in asma bahçelerinden... 
Yük katarları geçiyordu 
Tutsak kadınlar dolu vagonlarda. 
Yük katarları, mevsimler gibi hızlı... 
Geçiyordu. 
Açmaz mıydı menekşeler yeniden ? 
Kumsala yazılı aşklar siliniyordu. 
Kilimler dokuyordu güz yaprağı 
Kaç kez sebil etmişti geceyi kül rengi akşamlardan 
Dudakları silinmişti yine de 
Dudakları fırtınalardan. 
Kim yazardı tarihini ölümsüz sevilerin 
Elleri olmasaydı. 
Elleri başkaldıran... 
Her gün karanfil kokmazdı 
Her bulut taşımazdı yağmur. 
Dalgalar düşmandı gözlerine, 
Gözleri nar çiçeği. 
Yük katarları geçiyordu. 
Posta trenleri, ekspresler 
Kampanalar çalıyordu giz mavisi istasyonlarda 
Posta trenleri yorgundu taşımaktan gözlerini. 
Ne çok gözleri vardı özgürlüğün 
Dalgaların silemediği... - Celal Ülgen""",

    """İKİ KALP 
İki kalp arasında en kısa yol: 
Birbirine uzanmış ve zaman zaman 
Ancak parmak uçlarıyla değebilen 
İki kol. 
Merdivenlerin oraya koşuyorum, 
Beklemek gövde gösterisi zamanın; 
Çok erken gelmişim seni bulamıyorum, 
Bir şeyin provası yapılıyor sanki. 
Kuşlar toplanmışlar göçüyorlar 
Keşke yalnız bunun için sevseydim seni. - Cemal Süreya""",

    """YERÇEKİMLİ KARANFİL
Sanki hiçbir şey uyaramaz
İçimizdeki sessizliği
Ne söz, ne kelime, ne hiçbir şey
Gözleri getirin gözleri.
Başka değil, anlaşıyoruz böylece
Yaprağın daha bir yaprağa değdiği
O kadar yakın, o kadar uysal
Elleri getirin elleri
Diyorum, bir şeye karşı komaktır günümüzde aşk
Birleşip salıverelim iki tek gölgeyi. - Edip Cansever""",

    """Göğe Bakma Durağı
İkimiz birden sevinebiliriz göğe bakalım
Şu kaçamak ışıklardan şu şeker kamışlarından
Bebe dişlerinden güneşlerden yaban otlarından
Durmadan harcadığım şu gözlerimi al kurtar
Şu aranıp duran korkak ellerimi tut
Bu evleri atla bu evleri de bunları da
Göğe bakalım

Falanca durağa şimdi geliriz göğe bakalım
İnecek var deriz otobüs durur ineriz
Bu karanlık böyle iyi afferin Tanrıya
Herkes uyusun iyi oluyor hoşlanıyorum
Hırsızlar polisler açlar toklar uyusun
Herkes uyusun bir seni uyutmam bir de ben uyumam
Herkes yokken biz oluruz biz uyumayalım
Nasıl olsa sarhoşuz nasıl olsa öpüşürüz sokaklarda
Beni bırak göğe bakalım

Senin bu ellerinde ne var bilmiyorum göğe bakalım
Tuttukça güçleniyorum kalabalık oluyorum
Bu senin eski zaman gözlerin yalnız gibi ağaçlar gibi
Sularım ısınsın diye bakıyorum ısınıyor
Seni aldım bu sunturlu yere getirdim
Sayısız penceren vardı bir bir kapattım
Bana dönesin diye bir bir kapattım
Şimdi otobüs gelir biner gideriz
Dönmiyeceğimiz bir yer beğen başka türlüsü güç
Bir ellerin bir ellerim yeter belliyelim yetsin
Seni aldım bana ayırdım durma kendini hatırlat
Durma kendini hatırlat. - Turgut Uyar""",

    """Üçüncü Şahsın Şiiri
gözlerin gözlerime değince
felaketim olurdu ağlardım
beni sevmiyordun bilirdim
bir sevdiğin vardı duyardım
çöp gibi bir oğlan ipince
hayırsızın biriydi fikrimce
ne vakit karşımda görsem
öldüreceğimden korkardım
felaketim olurdu ağlardım

ne vakit maçka'dan geçsem
limanda hep gemiler olurdu
ağaçlar kuş gibi gülerdi
bir rüzgar aklımı alırdı
sessizce bir cigara yakardın
parmaklarımın ucunu yakardın
kirpiklerini eğerdin bakardın
üşürdüm içim ürperirdi
felaketim olurdu ağlardım

akşamlar bir roman gibi biterdi
jezabel kan içinde yatardı
limandan bir gemi giderdi
sen kalkıp ona giderdin
benzin mum gibi giderdin
sabaha kadar kalırdın
hayırsızın biriydi fikrimce
güldü mü cenazeye benzerdi
hele seni kollarına aldı mı
felaketim olurdu ağlardım - Attila İlhan""",

    """Desem Ki
Desem ki vakitlerden bir nisan akşamıdır
Rüzgarların en ferahlatıcısı senden esiyor
Sende seyrediyorum denizlerin en mavisini
Ormanların en kuytusunu sende görmekteyim
Senden kopardım çiçeklerin en solmazını
Toprakların en bereketlisini sende sürdüm
Sende tattım yemişlerin cümlesini
Desem ki sen benim için,
Hava kadar lazım,
Ekmek kadar mübarek,
Su gibi aziz bir şeysin;
Nimettensin, nimettensin.
Desem ki...
İnan bana sevgilim inan
Evimde şenliksin, bahçemde bahar;
Ve soframda en eski şarap.
Ben sende yaşıyorum,
Sen bende hüküm sürmektesin.
Bırak ben söyleyeyim güzelliğini,
Rüzgarla nehirlerle, kuşlarla beraber.
Günlerden sonra bir gün,
Şayet sesimi fark edemezsen
Rüzgarların nehirlerin kuşların sesinden,
Bil ki ölmüşüm.
Fakat yine üzülme müsterih ol
Kabirde böceklere ezberletirim güzelliğini
Ve neden sonra
Tekrar duyduğun gün sesimi gök kubbede
Hatırla ki mahşer günüdür
Ortalığa düşmüşüm seni arıyorum - Cahit Sıtkı Tarancı""",

    """Bir Gece Ansızın Gelebilirim
Bu kadar yürekten çağırma beni
Bir gece ansızın gelebilirim
Beni bekliyorsan, uyumamışsan
Sevinçten kapında ölebilirim
Belki de hayata yeni başlarım
İçimde küllenen kor alevlenir
Bakarsın hiç gitmem kölen olurum
Belki de seversin beni kimbilir
Kal dersen, dağlarca severim seni
Bir deniz olurum ayaklarında
Aşk bu özleyiş bu, hiç belli olmaz
Kalbim duruverir dudaklarında.
Ya da unuturum kim olduğumu
Hatırlamam belki adımı bile
Belki de çıldırır, deli olurum
Sana kavuşmanın heycanıyle
Aşk bu, bilinir mi nereye varır
Ne durdurur özlemini, seveni
Bakarsın ansızın gelebilirim
Bu kadar yürekten çağırma beni.- Ümit Yaşar Oğuzcan""",

    """Lavinia
Sana gitme demeyeceğim.
Üşüyorsun ceketimi al.
Günün en güzel saatleri bunlar.
Yanımda kal.

Sana gitme demeyeceğim.
Gene de sen bilirsin.
Yalanlar istiyorsan yalanlar söyleyeyim,
İncinirsin.

Sana gitme demeyeceğim,
Ama gitme, Lavinia.
Adını gizleyeceğim
Sen de bilme, Lavinia.   1957 - Özdemir Asaf""",

    """Bence Şimdi Sen De Herkes Gibisin
Gözlerim gözünde aşkı seçmiyor
Onlardan kalbime sevda geçmiyor
Ben yordum ruhumu biraz da sen yor
Çünkü bence şimdi herkes gibisin

Yolunu beklerken daha dün gece
Kaçıyorum bugün senden gizlice
Kalbime baktım da işte iyice
Anladım ki sen de herkes gibisin

Büsbütün unuttum seni eminim
Maziye karıştı şimdi yeminim
Kalbimde senin için yok bile kinim
Bence sen de şimdi herkes gibisin - Nazım Hikmet Ran""",

    """Yaşadıklarımdan Öğrendiğim Bir şey Var
Yaşadıklarımdan öğrendiğim bir şey var:
Yaşadın mı, yoğunluğuna yaşayacaksın bir şeyi
Sevgilin bitkin kalmalı öpülmekten
Sen bitkin düşmelisin koklamaktan bir çiçeği

İnsan saatlerce bakabilir gökyüzüne
Denize saatlerce bakabilir, bir kuşa, bir çocuğa
Yaşamak yeryüzünde, onunla karışmaktır
Kopmaz kökler salmaktır oraya

Kucakladın mı sımsıkı kucaklayacaksın arkadaşını
Kavgaya tüm kaslarınla, gövdenle, tutkunla gireceksin
Ve uzandın mı bir kez sımsıcak kumlara
Bir kum tanesi gibi, bir yaprak gibi, bir taş gibi dinleneceksin

İnsan bütün güzel müzikleri dinlemeli alabildiğine
Hem de tüm benliği seslerle, ezgilerle dolarcasına

İnsan balıklama dalmalı içine hayatın
Bir kayadan zümrüt bir denize dalarcasına

Uzak ülkeler çekmeli seni, tanımadığın insanlar
Bütün kitapları okumak, bütün hayatları tanımak arzusuyla yanmalısın
Değişmemelisin hiç bir şeyle bir bardak su içmenin mutluluğunu
Fakat ne kadar sevinç varsa yaşamak özlemiyle dolmalısın

Ve kederi de yaşamalısın, namusluca, bütün benliğinle
Çünkü acılar da, sevinçler gibi olgunlaştırır insanı
Kanın karışmalı hayatın büyük dolaşımına
Dolaşmalı damarlarında hayatın sonsuz taze kanı

Yaşadıklarımdan öğrendiğim bir şey var:
Yaşadın mı büyük yaşayacaksın, ırmaklara,göğe,bütün evrene karışırcasına
Çünkü ömür dediğimiz şey, hayata sunulmuş bir armağandır
Ve hayat, sunulmuş bir armağandır insana - Ataol Behramoğlu""",

    """Sessiz Gemi
Artık demir almak günü gelmişse zamandan
Meçhule giden bir gemi kalkar bu limandan.

Hiç yolcusu yokmuş gibi sessizce alır yol;
Sallanmaz o kalkışta ne mendil, ne de bir kol.

Rıhtımda kalanlar bu seyahatten elemli,
Günlerce siyah ufka bakar gözleri nemli,

Biçare gönüller! Ne giden son gemidir bu!
Hicranlı hayatın ne de son matemidir bu.

Dünyada sevilmiş ve seven nafile bekler;
Bilmez ki giden sevgililer dönmeyecekler.

Bir çok gidenin her biri memnun ki yerinden,
Bir çok seneler geçti; dönen yok seferinden. - Yahya Kemal Beyatlı""",

    """Beşinci Mektup
Ayrılık diye bir şey yok.
Bu bizim yalanımız.
Sevmek var aslında, özlemek var, beklemek var.
Şimdi neredesin? Ne yapıyorsun?

Güneş çoktan doğdu.
Uyanmış olmalısın.
Saçlarını tararken beni hatırladın, değil mi?
Öyleyse ayrılmadık.
Sadece özlemliyiz ve bekliyoruz.

Zamanı hatırlatan her şeyden nefret ediyorum.
Önce beklemekten.
Ömür boyunca ya bekliyor ya bekletiyor insan.
İkisi de kötü, ikisi de hazin tarafı yaşantımızın.

Bir çocuğun önce doğmasını bekliyorlar,
Sonra yürümesini, konuşmasını, büyümesini...
Zaman ilerliyor, bu defa para kazanmasını,
Kanunlara saygı göstermesini,
İnsanları sevmesini, aldanmasını, aldatmasını bekliyorlar.

Ve sonra ölümü bekleniyor insanoğlunun.
Ya o? Ya o?
İnsanlardan dostluk bekliyor, sevgilisinden sadakat,
Çocuklarından saygı ve bir parça huzur bekliyor,
Saadet bekliyor yaşamaktan.

Zaman ilerliyor, bir gün o da ölümü bekliyor artık.
Aradıklarının çoğunu bulamamış,
Beklediklerinin çoğu gelmemiş bir insan olarak
Göçüp gidiyor bu dünyadan.

İşte yaşamak maceramız bu.
Yaşarken beklemek, beklerken yaşamak
Ve yaşayıp beklerken ölmek!

Özleme bir diyeceğim yok.
O kömür kırıntıları arasında parlayan bir cam parçası.
O nefes alışı sevgimizin, kavuşmalarımızın anlamı.
O tek güzel yönü bekleyişlerimizin.

İnsanlığımız özleyişlerimizle alımlı,
Yaşantımız özlemlerle güzel.
Özlemin buruk bir tadı var, hele seni özlemenin.
Bir kokusu var bütün çiçeklere değişmem.
Bir ışığı var, bir rengi var seni özlemenin, anlatılmaz.

Verdiğin bütün acılara dayanıyorsam;
Seni özlediğim içindir.
Beklemenin korkunç zehri öldürmüyorsa beni;
Seni özlediğim içindir.
Yaşıyorsam; içimde umut varsa,
Yine seni özlediğim içindir.

Seni bunca özlemesem; bunca sevemezdim ki! - Ümit Yaşar Oğuzcan""",

    """Güz Çiçeklerinden Nazıma Bir Çelenk
Niçin öldün Nazım?
Ne yaparız şimdi biz
Şarkılarından yoksun?
Nerde buluruz başka bir pınar ki
Orda bizi karşıladığın gülümseme olsun?
Seninki gibi ateşle su karışık
Acıyla sevinç dolu
Gerçeğe çağıran bakışı nerde
Bulalım?
Kardeşim,
Öyle yeni duygular, düşünceler yarattın ki
Bende,
Denizden esen acı rüzgâr
Kapacak olsa bunları
Bulut gibi, yaprak gibi sürüklenir
Yaşarken seçtiğin
Ve ölümünden sonra sana barınak olan
Oraya, uzak toprağa düşerler.
Al sana bir demet Şili kasımpatıları
Al güney denizleri üstündeki ayın soğuk parlaklığını,
Halkların savaşını, kendi dövüşümü
Ve yurdumun kederli davullarının boğuk
Gürültüsünü
Kardeşim benim, dünyada nasıl yalnızım sensiz,
Çiçek açmış kiraz ağacının altınına benzeyen
Yüzüne hasret,
Benim için ekmek olan, susuzluğumu gideren, kanıma
Güç veren
Dostluğundan yoksun.
Hapisten çıktığında karşılaşmıştık seninle,
Zorbalık ve acı kuyusu gibi loş hapisten,
Zulmün izlerini görmüştüm ellerinde,
Kinin oklarını aramıştım gözlerinde,
Ama parlak bir yüreğin vardı,
Yara ve ışık dolu bir yürek.
Ne yapayım ben şimdi?
Tasarlanabilir mi dünya
Her yanına ektiğin çiçekler olmadan
Nasıl yaşamalı seni örnek almadan,
Senin halk zekanı, ozanlık gücünü duymadan?
Böyle olduğun için teşekkürler,
Teşekkürler türkülerinle yaktığın ateş için. - Pablo Neruda""",

    """Yaşamaya Dair
Yaşamak şakaya gelmez,
Büyük bir ciddiyetle yaşayacaksın
Bir sincap gibi mesela,
Yani, yaşamanın dışında ve ötesinde hiçbir şey beklemeden,
Yani bütün işin gücün yaşamak olacak.

Yaşamayı ciddiye alacaksın,
Yani o derecede, öylesine ki,
Mesela, kolların bağlı arkadan, sırtın duvarda,
Yahut kocaman gözlüklerin,
Beyaz gömleğinle bir laboratuarda
İnsanlar için ölebileceksin,
Hem de yüzünü bile görmediğin insanlar için,
Hem de hiç kimse seni buna zorlamamışken,
Hem de en güzel en gerçek şeyin
Yaşamak olduğunu bildiğin halde.

Yani, öylesine ciddiye alacaksın ki yaşamayı,
Yetmişinde bile, mesela, zeytin dikeceksin,
Hem de öyle çocuklara falan kalır diye değil,
Ölmekten korktuğun halde ölüme inanmadığın için,
Yaşamak yanı ağır bastığından.

Diyelim ki, ağır ameliyatlık hastayız,
Yani, beyaz masadan,
Bir daha kalkmamak ihtimali de var.
Duymamak mümkün değilse de biraz erken gitmenin kederini
Biz yine de güleceğiz anlatılan Bektaşi fıkrasına,
Hava yağmurlu mu, diye bakacağız pencereden,
Yahut da sabırsızlıkla bekleyeceğiz
En son ajans haberlerini.

Diyelim ki, dövüşülmeye değer bir şeyler için,
Diyelim ki, cephedeyiz.
Daha orda ilk hücumda, daha o gün
Yüzükoyun kapaklanıp ölmek de mümkün.
Tuhaf bir hınçla bileceğiz bunu,
Fakat yine de çıldırasıya merak edeceğiz
Belki yıllarca sürecek olan savaşın sonunu.

Diyelim ki hapisteyiz,
Yaşımız da elliye yakın,
Daha da on sekiz sene olsun açılmasına demir kapının.
Yine de dışarıyla birlikte yaşayacağız,
İnsanları, hayvanları, kavgası ve rüzgarıyla
Yani, duvarın ardındaki dışarıyla.

Yani, nasıl ve nerede olursak olalım
Hiç ölünmeyecekmiş gibi yaşanacak...

Bu dünya soğuyacak,
Yıldızların arasında bir yıldız,
Hem de en ufacıklarından,
Mavi kadifede bir yaldız zerresi yani,
Yani bu koskocaman dünyamız.

Bu dünya soğuyacak günün birinde,
Hatta bir buz yığını
Yahut ölü bir bulut gibi de değil,
Boş bir ceviz gibi yuvarlanacak
Zifiri karanlıkta uçsuz bucaksız.

Şimdiden çekilecek acısı bunun,
Duyulacak mahzunluğu şimdiden.
Böylesine sevilecek bu dünya
'Yaşadım' diyebilmen için... - Nazım Hikmet Ran""",

    """Haziranda Ölmek Zor
İşten çıktım
Sokaktayım
Elim yüzüm üstümbaşım gazete
Sokakta tank paleti
Sokakta düdük sesi
Sokakta tomson
Sokağa çıkmak yasak
Sokaktayım
Gece leylâk
Ve tomurcuk kokuyor
Yaralı bir şahin olmuş yüreğim
Uy anam anam
Haziranda ölmek zor!
Havada tüy
Havada kuş
Havada kuş soluğu kokusu
Hava leylâk
Ve tomurcuk kokuyor
Ne anlar acılardan/güzel haziran
Ne anlar güzel bahar!
Kopuk bir kol sokakta
Çırpınıp durur
Çalışmışım onbeş saat
Tükenmişim onbeş saat
Acıkmışım yorulmuşum uykusamışım
Anama sövmüş patron
Ter döktüğüm gazetede
Sıkmışım dişlerimi
Islıkla söylemişim umutlarımı
Susarak söylemişim
Sıcak bir ev özlemişim
Sıcak bir yemek
Ve sıcacık bir yatakta
Unutturan öpücükler
Çıkmışım bir kavgadan
Vurmuşum sokaklara
Sokakta tank paleti
Sokakta düdük sesi
Sarı sarı yapraklarla birlikte sanki
Dallarda insan iskeletleri
Asacaklar aydemir'i
Asacaklar gürcan'ı
Belki başkalarını
Pis bir ota değmiş gibi sızlıyor genzim
Dökülüyor etlerim
Sarı yapraklar gibi
Asmak neyi kurtarır
Sarı sarı yaprakları kuru dallara?
Yolunmuş yaprakları
Kırılmış dallarıyla
Ne anlatır bir ağaç
Hani rüzgâr
Hani kuş
Hani nerde rüzgârlı kuş sesleri?
Asılmak sorun değil
Asılmamak da değil
Kimin kimi astığı
Kimin kimi neden niçin astığı
Budur işte asıl sorun!
Sevdim gelin morunu
Sevdim şiir morunu
Moru sevdim tomurcukta
Moru sevdim memede
Ve öptüğüm dudakta
Ama sevmedim, hayır
İğrendim insanoğlunun
Yağlı ipte sallanan morluğundan!
Neden böyle acılıyım
Neden böyle ağrılı
Neden niçin bu sokaklar böyle boş
Niçin neden bu evler böyle dolu?
Sokaklarla solur evler
Sokaklarla atar nabzı
Kentlerin
Sokaksız kent
Kentsiz ülke
Kahkahanın yanıbaşı gözyaşı
İşten çıktım
Elim yüzüm üstümbaşım gazete
Karanlıkta akan bir su
Gibi vurdum kendimi caddelere
Hava leylâk
Ve tomurcuk kokusu
Havada köryoluna
Havada suçsuz günahsız
Gitme korkusu
Ah desem
Eriyecek demirleri bu korkuluğun
Oh desem
Tutuşacak soluğum
Asmak neyi kurtarır
Öldürmek neyi
Yaşatmaktır önemlisi
Güzel yaşatmak
Abeceden geçirmek kıracın çekirgesini
Ekmeksiz yuvasız hekimsiz bırakmamak
Ah yavrum
Ah güzelim
Canım benim / sevdiceğim
Bitanem
Kısa sürdü bu yolculuk
N'eylersin ki sonu yok!
Gece leylâk
Ve tomurcuk kokuyor
Uy anam anam
Haziranda ölmek zor!
Nerdeyim ben
Nerdeyim ben
Nerdeyim?
Kimsiniz siz
Kimsiniz siz
Kimsiniz?
Ne söyler bu radyolar
Gazeteler ne yazar
Kim ölmüş uzaklarda
Göçen kim dünyamızdan?
Asmak neyi kurtarır
Öldürmek neyi?
Yolunmuş yaprakları
Ve kırılmış dallarıyla bir ağaç
Söyler hangi güzelliği?
Kökü burda
Yüreğimde
Yaprakları uzaklarda bir çınar
Islık çala çala göçtü bir çınar
Göçtü memet diye diye
Şafak vakti bir çınar
Silkeledi kuşlarını
Güneşlerini:
«oğlum sana sesleniyorum işitiyor musun, memet,
memet! »
Gece leylâk
Ve tomurcuk kokuyor
Üstümbaşım elim yüzüm gazete
Vurmuşum sokaklara
Vurmuşum karanlığa
Uy anam anam
Haziranda ölmek zor!
Bu acılar
Bu ağrılar
Bu yürek
Neyi kimden esirgiyor bu buz gibi sokaklar
Bu ağaçlar niçin böyle yapraksız
Bu geceler niçin böyle insansız
Bu insanlar niçin böyle yarınsız
Bu niçinler niçin böyle yanıtsız?
Kim bu korku
Kim bu umut
Ne adına
Kim için?
«uyarına gelirse
tepemde bir de çınar»
Demişti on yıl önce
Demek ki on yıl sonra
Demek ki sabah sabah
Demek ki «manda gönü»
Demek ki «şile bezi»
Demek ki «yeşil biber»
Bir de memet'in yüzü
Bir de güzel istanbul
Bir de «saman sarısı»
Bir de özlem kırmızısı
Demek ki göçtü usta
Kaldı yürek sızısı
Geride kalanlara
Nerdeyim ben
Nerdeyim?
Kimsiniz siz
Kimsiniz?
Yıllar var ki ter içinde
Taşıdım ben bu yükü
Bıraktım acının alkışlarına
3 haziran '63'ü
Bir kırmızı gül dalı
Şimdi uzakta
Bir kırmızı gül dalı
İğilmiş üzerine
Yatıyor oralarda
Bir eski gömütlükte
Yatıyor usta
Bir kırmızı gül dalı
İğilmiş üzerine
Okşar yanan alnını
Bir kırmızı gül dalı
Nâzım ustanın
Gece leylâk
Ve tomurcuk kokuyor
Bir basın işçisiyim
Elim yüzüm üstümbaşım gazete
Geçsem de gölgesinden tankların tomsonların
Şuramda bir çalıkuşu ötüyor
Uy anam anam
Haziranda ölmek zor! - Hasan Hüseyin Korkmazgil""",

    """Anlar
Eğer,yenıden başlayabilseydim yaşamaya,
İkincisinde daha çok hata yapardım.
Kusursuz olmaya çalışmaz,sırtüstü yatardım.
Neşeli olurdum, ilkinde olmadıgım kadar,
Çok az şeyi
Ciddiyetle yapardım.
Temizlik sorun bile olmazdı asla.
Daha çok riske girerdim.
Seyahat ederdim daha fazla.
Daha çok güneş doguşu izler,
Daha çok dağa tırmanır,daha çok nehirde yüzerdim.
Görmedigim bir çok yere giderdim.
Dondurma yerdim doyasıya ve daha az bezelye.
Gerçek sorunlarım olurdu hayali olanların yerine.
Yaşamın her anını gerçek ve verimli kılan insanlardandım.
Yeniden başlayabilseydim eger,yalnız mutlu anlarım olurdu.
Farkında mısınız bilmem. yaşam budur zaten.
Anlar,sadece anlar.Siz de anı yaşayın.
Hiçbir yere yanında su,şemsiye ve paraşüt almadan,
Gitmeyen insanlardandım ben.
Yeniden başlayabilseydim eger,hiçbir şey taşımazdım.
Eger yeniden başlayabilseydim,
İlkbaharda pabuçlarımı fırlatır atardım.
Ve sonbahar bitene kadar yürürdüm çıplak ayaklarla.
Bilinmeyen yollar keşfeder,güneşin tadına varır,
Çocuklarla oynardım,bir şansım olsaydı eger.
Ama işte 85'indeyim ve biliyorumn...
Ölüyorum.... - Jorge Luis Borges""",

    """Hasretinden Prangalar Eskittim
Seni, anlatabilmek seni.
İyi çocuklara, kahramanlara.
Seni anlatabilmek seni,
Namussuza, halden bilmeze,
Kahpe yalana.

Ard arda kaç zemheri,
Kurt uyur, kuş uyur, zindan uyurdu.
Dışarda gürül- gürül akan bir dünya...
Bir ben uyumadım,
Kaç leylim bahar,
Hasretinden prangalar eskittim.
Saçlarına kan gülleri takayım,
Bir o yana
Bir bu yana...

Seni bağırabilsem seni,
Dipsiz kuyulara,
Akan yıldıza,
Bir kibrit çöpüne varana,
Okyanusun en ıssız dalgasına
Düşmüş bir kibrit çöpüne.

Yitirmiş tılsımını ilk sevmelerin,
Yitirmiş öpücükleri,
Payı yok, apansız inen akşamlardan,
Bir kadeh, bir cıgara, dalıp gidene,
Seni anlatabilsem seni...
Yokluğun, Cehennemin öbür adıdır
Üşüyorum, kapama gözlerini... - Ahmed Arif""",

    """Mutlu Aşk Yoktur
İnsan her şeyi elinde tutamaz hiç bir zaman
Ne gücünü ne güçsüzlüğünü ne de yüreğini
Ve açtım derken kollarını bir haç olur gölgesi
Ve sarıldım derken mutluluğuna parçalar o şeyi
Hayatı garip ve acı dolu bir ayrılıktır her an
Mutlu aşk yoktur
Hayatı Bu silahsız askerlere benzer
Bir başka kader için giyinip kuşanan
Ne yarar var onlara sabah erken kalkmaktan
Onlar ki akşamları aylak kararsız insan
Söyle bunları Hayatım Ve bunca gözyaşı yeter
Mutlu aşk yoktur
Güzel aşkım tatlı aşkım kanayan yaram benim
İçimde taşırım seni yaralı bir kuş gibi
Ve onlar bilmeden izler geçiyorken bizleri
Ardımdan tekrarlayıp ördüğüm sözcükleri
Ve hemen can verdiler iri gözlerin için
Mutlu aşk yoktur
Vakit çok geç artık hayatı öğrenmeye
Yüreklerimiz birlikte ağlasın sabaha dek
En küçük şarkı için nice mutsuzluk gerek
Bir ürperişi nice pişmanlıkla ödemek
Nice hıçkırık gerek bir gitar ezgisine
Mutlu aşk yoktur
Bir tek aşk yoktur acıya garketmesin
Bir tek aşk yoktur kalpte açmasın yara
Bir tek aşk yoktur iz bırakmasın insanda
Ve senden daha fazla değil vatan aşkı da
Bir tek aşk yok yaşayan gözyaşı dökmeksizin
Mutlu aşk yoktur ama
Böyledir ikimizin aşkı da - Louis Aragon""",

    """Denge
Sizin alınız al inandım
Sizin morunuz mor inandım
Tanrınız büyük amenna
Şiiriniz adamakıllı şiir
Dumanı da caba

Bütün ağaçlarla uyuşmuşum
Kalabalık ha olmuş ha olmamış
Sokaklarda yitirmiş cebimde bulmuşum
Ama sokaklar şöyleymiş
Ağaçlar böyleymiş
Ama sizin adınız ne
Benim dengemi bozmayınız

Aşkım da değişebilir gerçeklerim de
Pırıl pırıl dalgalı bir denize karşı
Yangelmişim diz boyu sulara
Hepinize iyiniyetle gülümsüyorum
Hiçbirinizle dövüşemem
Benim bir gizli bildiğim var
Sizin alınız al inandım
Morunuz mor inandım
Ben tam kendime göre
Ben tam dünyaya göre
Ama sizin adınız ne
Benim dengemi bozmayınız - Turgut Uyar""",

    """Yakarı 
Kafalar ver bize ateş olsun kor olsun
Göksel yıldırımlarla yanmış kafalar
Uyanık kafalar adamakıllı gerçek kafalar
Yansıyarak senin varlığından gelsin

İç'in göklerinde doğurt bizleri
Sağnaklı uçurumlarla delik deşik
Ve bir esrime dolaşsın içimizi
Bir cırnakla akkor halindeki

Açız işte açız doyur bizi
Yıldızlar arası sarsıntılarla
N'olur göksel lavlar aksın
Kan yerine damarlarımızda

Ayır bizi böl parçala bizi
Ateşten ellerin keskin yanıyla
Ölünen o yeri ölümün de uzağında
Aç işte üstümüze o alev kubbeleri

Silkele beynimiz sarsılsın
O senin görgün ve yordamın içre
Yeni bir tufanın pençeleriyle
Bozulsun zekâmız alt üst olsun - Antonin Artaud""",

    """ODA
Gün günden odamın şeklini alıyorum
İşliyorum bu iniltili varlığı yeniden
Kim bilir, duyuyorum yazgısını belki de
Kuru bir dal parçasını içinden yiye yiye
Dal olan bir böceğin
O garip yazgısını

Ne ölüme benzer ne ölümsüzlüğe. - Edip Cansever""",

    """Çocuklar Gibi
Bende hiç tükenmez bir hayat vardı
Kırlara yayılan ilkbahar gibi
Kalbim hiç durmadan hızla çarpardı
Göğsümün içinde ateş var gibi

Bazı nur içinde, bazı sisteyim
Bazı beni seven bir göğüsteyim
Kah el üstündeydim, kah hapisteydim
Her yere sokulan bir rüzgar gibi

Aşkım iki günlük iptilalardı
Hayatım tükenmez maceralardı
İçimde binlerce istekler vardı
Bir şair, yahut bir hükümdar gibi

Hissedince sana vurulduğumu
Anladım ne kadar yorulduğumu
Sakinleştiğimi, durulduğumu
Denize dökülen bir pınar gibi

Şimdi şiir bence senin yüzündür
Şimdi benim tahtım senin dizindir
Sevgilim, saadet ikimizindir
Göklerden gelen bir yadigar gibi

Sözün şiirlerin mükemmelidir
Senden başkasını seven delidir
Yüzün çiçeklerin en güzelidir
Gözlerin bilinmez bir diyar gibi

Başını göğsüme sakla sevgilim
Güzel saçlarında dolaşsın elim
Bir gün ağlayalım, bir gün gülelim
Sevişen yaramaz çocuklar gibi - Sabahattin Ali""",

    """Leylim Ley
Döndüm daldan düşen kuru yaprağa
Seher yeli dağıt beni kır beni
Götür tozlarımı burdan uzağa
Yarin çıplak ayağına sür beni

Aldım sazı çıktım gurbet görmeye
Dönüp yare geldim yüzüm sürmeye
Ne lüzum var şuna buna sormaya
Senden ayrı ne hal oldum gör beni

Ayın şavkı vurur sazım üstüne
Söz söyleyen yoktur sözüm üstüne
Gel ey hilal kaşlım dizim üstüne
Ay bir yandan sen bir yandan sar beni

Yedi yıldır uğramadım yurduma
Dert ortağı aramadım derdime
Geleceksen bir gün düşüp ardıma
Kula değil yüreğine sor beni - Sabahattin Ali""",

    """Kuğu Ezgisi
Kuğuların ölüm öncesi ezgileri şiirlerim,
Yalpalayan hayatımın kara çarşaflı
bekçi gizleri.

Ne zamandır ertelediğim her acı,
Çıt çıkarıyor artık, başlıyor yeni bir ezgi,
-bu şiir -
Sendelerken yaşamım ve bilinmez yönlerim,
Dost kalmak zorunda bana ve
sizlere!

Çünkü saldırgan olandan kopmuştur o,
uykusunu bölen derin arzudan.
Büyüsünü bir içtenlikten alırsa
Kendi saf şiddetini yaşar artık,
-bu şiir -
Kuramadığım güzelliklerin sessiz görünümü,
ulaşılamayanın boyun eğen yansısı,
Sevda ile seslenir sizlere! - Nilgün Marmara""",

    """Sevgilerde
Sevgileri yarınlara bıraktınız
Çekingen, tutuk, saygılı.
Bütün yakınlarınız
Sizi yanlış tanıdı.

Bitmeyen işler yüzünden
(Siz böyle olsun istemezdiniz)

Bir bakış bile yeterken anlatmaya her şeyi
Kalbinizi dolduran duygular
Kalbinizde kaldı.

Siz geniş zamanlar umuyordunuz
Çirkindi dar vakitlerde bir sevgiyi söylemek.
Yılların telâşlarda bu kadar çabuk
Geçeceği aklınıza gelmezdi.

Gizli bahçenizde
Açan çiçekler vardı,
Gecelerde ve yalnız.
Vermeye az buldunuz
Yahut vakit olmadı - Behçet Necatigil""",

    """Siz Aşktan N'anlarsınız Bayım
Çok şey öğrendim geçen üç yıl boyunca
Alt katında uyumayı bir ranzanın
Üst katında çocukluğum...
Kağıttan gemiler yaptım kalbimden
Ki hiçbiri karşıya ulaşmazdı.
Aşk diyorsunuz,
limanı olanın aşkı olmaz ki bayım!

Allah’la samimi oldum geçen üç yıl boyunca
Havı dökülmüş yerlerine yüzümün
Büyük bir aşk yamadım
Hayır
Yüzüme nur inmedi, yüzüm nura indi bayım
Gözyaşlarım bitse tesbih tanelerim vardı
Tesbih tanelerim bitse göz yaşlarım...
Saydım, insanın doksan dokuz tane yalnızlığı vardı.
Aşk diyorsunuz ya
Ben istemenin allahını bilirim bayım

Çok şey öğrendim geçen üç yıl boyunca
Balkona yorgun çamaşırlar asmayı
Ki uçlarından çile damlardı.
Güneşte nane kurutmayı
Ben acılarımın başını
evcimen telaşlarla okşadım bayım.
Bir pardösüm bile oldu içinde kaybolduğum.
İnsan kaybolmayı ister mi?
Ben işte istedim bayım.
Uzaklara gittim
Uzaklar sana gelmez, sen uzaklara gidersin
Uzaklar seni ister, bak uzaklar da aşktan anlar bayım

Süt içtim acım hafiflesin diye
Çikolata yedim bir köşeye çekilip
Zehrimi alsın diye
Sizin hiç bilmediğiniz, bilmeyeceğiniz
İlahiler öğrendim.
Siz zehir nedir bilmezsiniz
Zehir aşkı bilir oysa bayım!

Ben işte miraç gecelerinde
Bir peygamberin kanatlarında teselli aradım,
Birlikte yere inebileceğim bir dost aradım,
Uyuyan ve acılı yüzünde kardeşimin
Bir şiir aradım.
Geçen üç yıl boyunca
Yüzü dövmeli kadınların yüzünde yüzümü aradım.
Ülkem olmayan ülkemi
Kayboluşumu aradım.
Bulmak o kadar kolay olmasa gerek diye düşünmüştüm.
Bir ters bir yüz kazaklar ördüm
Haroşa bir hayat bırakmak için.
Bırakmak o kadar kolay olmasa gerek diye düşünmüştüm.

Kimi gün öylesine yalnızdım
Derdimi annemin fotoğrafına anlattım.
Annem
Ki beyaz bir kadındır
Ölüsünü şiirle yıkadım.
Bir gölgeyi sevmek ne demektir bilmezsiniz siz bayım
Öldüğü gece terliklerindeki izleri okşadım.
Çok şey öğrendim geçen üç yıl boyunca
Acının ortasında acısız olmayı,
Kalbim ucu kararmış bir tahta kaşık gibiydi bayım.
Kendimin ucunu kenar mahallelere taşıdım.
Aşk diyorsunuz ya,
İşte orda durun bayım
Islak unutulmuş bir taş bezi gibi kalakaldım
Kendimin ucunda
Öyle ıslak,
Öyle kötü kokan,
Yırtık ve perişan.

Siz aşkı ne bilirsiniz bayım
Aşkı aşk bilir yalnız! - Didem Madak""",

    """Karadut
Karadutum, çatal karam, çingenem
Nar tanem, nur tanem, bir tanem
Ağaç isem dalımsın salkım saçak
Petek isem balımsın a gülüm
Günahımsın, vebalimsin.

Dili mercan, dizi mercan, dişi mercan
Yoluna bir can koyduğum
Gökte ararken yerde bulduğum
Karadutum, çatal karam, çingenem
Daha nem olacaktın bir tanem
Gülen ayvam, ağlayan narımsın
Kadınım, kısrağım, karımsın.

Sigara paketlerine resmini çizdiğim
Körpe fidanlara adını yazdığım
Karam, karam
Kaşı karam, gözü karam, bahtı karam
Sıla kokar, arzu tüter
Ilgıt ılgıt buram buram.
Ben beyzade, kişizade,
Her türlü dertten topyekün azade
Hani şu ekmeği elden suyu gölden.
Durup dururken yorulan
Kibrit çöpü gibi kırılan
Yalnız sanat çıkmazlarında başını kaşıyan
Artık otlar göstermelik atlar gibi bedava yaşayan
Sen benim mihnet içinde yanmış kavrulmuşum

N'etmiş, n'eylemiş, n'olmuşum
Cömert ırmaklar gibi gürül gürül
Bahtın karışmış bahtıma çok şükür.
Yunmuş, yıkanmış adam olmuşum.

Karam, karam
Kaşı karam, gözü karam, bahtı karam
Sensiz bana canım dünya haram olsun. - Bedri Rahmi Eyüboğlu""",

    """Ay Zeytin Gece
Kamçılı karanlıktı geldin üstüme
Bütün masalları dolaştın
Ay zeytin gece
Ay vurmuştu alnına
Perçemlerin Tokat akıtması
Yorgundu atılmış yılan derisi
Değiştirilmiş güvercin gömleği tende
Nereye gidiyorsun, dedim
Zeytinlerin arasından
Siste silinip giderken yollar
Aydı zeytindi geceydi
Korkmadım bağırdım ardından
Aydaki zeytindeki gecedeki delikanlı
Nereye böyle
Aldı rüzgar sesimi duyurmadı
Vurdu geçti durduğum yeri
Gümüşünü silkeledi yüzüme
Atının kanatları
Ben öldüm, ölüm bulunamadı
Kamçılı bir karanlıktı
Hikayemin gecesini dürdüm de
Kimse çıkamadı dışarı
Ay kaldı zeytin kaldı gece kaldı
Sis kaldı yollar kaldı
Karanlıktı - Murathan Mungan""",

    """Evde Yoklar
Durmadan avuçlarım terliyor,
İnildiyor ardımdan
Girdiğim çıktığım kapılar.
Trenim gecikmeli, yüreğim burgun,
Bir bir uzaklaşıyor sevdiğim insanlar.
Ne zaman bir dosta gitsem,
Evde yoklar.

Dolanıp duruyorum ortalıkta.
Kedim hımbıl, yaprak döküyor çiçeğim,
Rakım bir türlü beyazlaşmıyor.
Anahtarım güç dönüyor kilidinde,
Nemli aldığım sigaralar.
Ne zaman bir dosta gitsem,
Evde yoklar.

Kimi zaman çocuğum,
Bir müzik kutusu başucumda
Ve ayımın gözleri saydam.
Kimi zaman gardayım
Yanımda bavulum, yılgın ve ihtiyar.
Ne zaman bir dosta gitsem,
Evde yoklar.

Bekliyorum bir kapının önünde,
Cebimde yazılmamış bir mektupla.
Bana karşı ben vardım
Çaldığım kapıların ardında,
Ben açtım, ben girdim
Selamlaştık ilk defa. - Metin Altıok"""
]

# --- KURUMSAL LOGO VE İSİM BÖLÜMÜ ---
# Logoyu ve okul adını sayfanın en üstüne yerleştirir.
cols = st.columns([1, 4]) # Logoya 1 birim, okul adına 4 birim yer ayırır.
with cols[0]:
    if OKUL_LOGO_LINKI:
        st.image(OKUL_LOGO_LINKI, width=100) # Logoyu gösterir.
with cols[1]:
    st.markdown("""
        ## İzmir Özel Tevfik Fikret Okulları
        ### 21 Mart Dünya Şiir Günü Antolojisi
    """)

st.divider() # Araya kalın bir çizgi çeker.


# 3. Ana Başlık ve Karşılama (Sadece 1 kez yazılır)
st.title("🎉 21 Mart Dünya Şiir Günü'nüz Kutlu Olsun! 🌸")
st.markdown("""
    ### Merhaba Şiir Dostu! ✨
    🖋️ **Bir kalemden dökülen mısralar, bugün bir çiçek gibi gönlünüzde açsın.**
    
    Öğrencilerimizden velilerimize, öğretmenlerimizden çalışanlarımıza yolu şiirden geçen herkes için hazırladığımız 
    bu küçük köşeye hoş geldiniz. Şiir, hayatın gri renkleri arasındaki en güzel gökkuşağıdır.
    
    🌷 *Aşağıdaki kutucuğa tıklayarak size özel seçilen şiiri okuyabilirsiniz.*🌷
""")

st.write("---")

# 4. Buton ve Şiir Seçme (Yaprak Animasyonuyla Birlikte)        
if st.button('Bir Mısra Güzellik Seç 📜'):
    # SONBAHAR YAPRAKLARI ANİMASYONU
    st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999;">
            <style>
                .leaf { position: absolute; top: -10%; animation: fall linear infinite; }
                @keyframes fall {
                    0% { top: -10%; transform: translateX(0) rotate(0deg); }
                    100% { top: 110%; transform: translateX(100px) rotate(360deg); }
                }
            </style>
            <div class="leaf" style="left: 10%; font-size: 30px; animation-duration: 7s; color: #d4a373;">🍂</div>
            <div class="leaf" style="left: 30%; font-size: 25px; animation-duration: 9s; color: #bc6c25;">🍁</div>
            <div class="leaf" style="left: 50%; font-size: 35px; animation-duration: 6s; color: #dda15e;">🍃</div>
            <div class="leaf" style="left: 70%; font-size: 28px; animation-duration: 10s; color: #606c38;">🍂</div>
            <div class="leaf" style="left: 90%; font-size: 32px; animation-duration: 8s; color: #a44a3f;">🍁</div>
        </div>
    """, unsafe_allow_html=True)

    # Şiir Seçimi
    secilen = random.choice(siirler)
    
    # Başlık ve Şiiri Ayırıp Şık Gösterme
    # Şiiri tek parça halinde gösteriyoruz (Eski düzen)
    st.code(secilen, language=None)

    st.write("---")
    st.markdown("🌸 *Dünya, şiirle daha güzel bir yer.*")
else:
    # Butona basılmadan önce görünen mesaj
    st.info("Ruhunuza iyi gelecek bir şiir için tıklamanız yeterli. ✨")

# 5. Alt Bilgi (Kurumsal Bilgi Eklendi)
st.divider()
st.caption("🖋️ İzmir Özel Tevfik Fikret Okulları - Kalemin mısrayla buluştuğu günler dileriz. ✨🌸")
