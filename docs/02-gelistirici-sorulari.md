# LİSTE 2 — GELİŞTİRİCİ İÇİN SORULAR (v2: synth / davul makinesi / sampler / mikrofon)

**Etiketler**
- **[BAŞLAMADAN ŞART]** → Bu cevap olmadan tasarım/parça alımı yapılamaz.
- **[SONRA KARARLAŞTIRILIR]** → Önemli ama ilk sürümü bekletmez.
- **🔗 ÇAPRAZ-Xn** → Müzisyen listesinde aynı konuya soru var; cevaplar çelişebilir (kodlar listenin sonundaki tabloda).

Şıklarda "Diğer / bilmiyorum" her zaman geçerli. Bilmiyorsan "bilmiyorum" yaz, ben "araştırılacak" diye işaretlerim.

**Güncel bilgi (sonradan eklendi):** Çalgılar gitar değil; synth'ler (MS-20 vb.), theremin, davul makinesi, SP-404 MK2 ve mikrofon. İlk cihaz **1 stereo giriş + 1 stereo çıkış**, üst üste dizilebilen efektler ve **çalgıya göre ayrı preset**. İleride (1 cihaz oturunca) 2. cihaz ve belki **az PCB ile MCU + geliştirme kartı** düşünülüyor; Pi pahalı bulunuyor. Bu yüzden bölüm **O** eklendi.

---

## A. Mevcut donanımın tam özellikleri

**G1. Raspberry Pi 4'ün RAM miktarı ve kart revizyonu nedir (1/2/4/8 GB, `cat /proc/cpuinfo` Revision)?** [BAŞLAMADAN ŞART]
 > Neden önemli: RAM, plugin sayısı ve işletim sistemi seçimini sınırlar.

**G2. Dokunmatik ekranın tam modeli, boyutu (6/7/8"), çözünürlüğü ve bağlantı tipi nedir?** [BAŞLAMADAN ŞART] 🔗 X6
 A) DSI (resmi Pi ekranı gibi)  B) HDMI + USB dokunmatik  C) SPI  D) Diğer: ____
 > Neden önemli: Bağlantı tipi, ekranın KMS ile çalışıp çalışmayacağını, kablo ve kutu yerleşimini belirler.

**G3. Dokunmatik denetleyici hangi çipi kullanıyor ve çok noktalı dokunmayı (multitouch) destekliyor mu?** [BAŞLAMADAN ŞART]
 > Neden önemli: Dokunmatiğin Linux'ta (libinput/evdev) tanınması Slint'in girdisi için kritik.

**G4. Elde başka ne parça var (SD kart kapasitesi/hızı, USB ses kartı, güç adaptörü, kutu, breadboard, kablo, encoder, buton, jack, lehim ekipmanı)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Satın almam gerekenler listesini bu belirleyecek.

**G5. Pi 4 kartı için SD kart mı, USB SSD mi, ikisi de mi düşünüyorsun? Kart kalitesi (A1/A2, endüstriyel) önemli mi?** [BAŞLAMADAN ŞART] 🔗 X7
 > Neden önemli: Salt okunur dosya sisteminde bile güvenilirlik, kart kalitesine ve açılış süresine bağlı.

## B. Ses giriş/çıkış ve seviyeler

**G6. Ses arayüzü için bir tercihin var mı?** [BAŞLAMADAN ŞART] 🔗 X1
 A) USB ses kartı (hazır)  B) Pi'ye takılan HAT/kart  C) Elimde bir kart var: ____  D) Hiç bilmiyorum, öner
 > Neden önemli: Gecikme, gürültü, seviye uyumu, ve kutuya sığması bu seçime bağlı.

**G7. Kaç ses girişi gerekir ve hangi tür?** [BAŞLAMADAN ŞART] 🔗 X1
 A) 1 stereo hat girişi (müzisyen: ilk cihaz için bu)  B) 1 stereo hat + 1 mikrofon girişi  C) 2 stereo hat girişi  D) Çok kanallı  E) Diğer: ____
 > Neden önemli: Giriş sayısı ve türü ses kartı seçimini belirler; müzisyen cevapları (M1, M3, M4, M6, M12) ile birlikte karara bağlanacak.

**G8. Giriş seviyesi aralığı nedir ve hangi seviyeler desteklenecek?** [BAŞLAMADAN ŞART] 🔗 X1
 A) Sadece hat seviyesi (synth, davul makinesi, SP-404)  B) Hat + modüler (yüksek) seviye  C) Hat + mikrofon (önyükselticili)  D) Bilmiyorum
 > Neden önemli: Gitar girişi (Hi-Z) artık gerekmiyor, ama modüler seviyeli bir kaynak girişi bozar, mikrofon için ayrı yükseltici (ve kondansatör mikrofon için 48 V) gerekir.

**G9. Kaç ses çıkışı gerekir ve hangi tür?** [BAŞLAMADAN ŞART] 🔗 X1 🔗 X2
 A) 1 mono hat çıkışı  B) 2 (stereo) hat çıkışı  C) Stereo + ayrı kulaklık çıkışı  D) Diğer: ____
 > Neden önemli: Çıkış sayısı jack yerleşimini ve ses kartı seçimini belirler.

**G10. Zincir içi mono mu stereo mu çalışacak?** [BAŞLAMADAN ŞART] 🔗 X2
 A) Baştan sona mono  B) Mono giriş, stereo çıkış (reverb vb. stereo)  C) Tam stereo  D) Efekte göre
 > Neden önemli: Stereo, CPU yükünü ve plugin seçimini önemli ölçüde değiştirir.

**G11. Çıkış seviyesi hedefi nedir (mikserin hat girişine, aktif hoparlöre, kulaklığa)?** [BAŞLAMADAN ŞART] 🔗 X1
 > Neden önemli: Çıkış seviyesi uyumsuzsa ya bozulma ya zayıf ses olur; ayrıca dengeli (TRS) çıkış gerekip gerekmediği buna bağlı.

**G12. Örnekleme hızı ve bit derinliği tercihin var mı (44.1/48/96 kHz, 16/24/32 bit)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Yüksek hız gecikmeyi azaltır ama CPU yükünü artırır; plugin'lerin hepsi her hızda doğru çalışmayabilir.

## C. Gecikme ve ses altyapısı

**G13. Hedef gecikme nedir (giriş-çıkış toplam)?** [BAŞLAMADAN ŞART] 🔗 X8
 A) 5 ms altı  B) 5–10 ms  C) 10–20 ms  D) Ölçüp karar veririm
 > Neden önemli: Canlı çalmada (tuşa basınca ses beklenirken) 10 ms üstü hissedilebilir; hedef, buffer ve donanım kararlarını sınırlar.

**G14. Buffer (period) boyutu ve sayısı için bir başlangıç beklentin var mı (örn. 64/128 frame × 2/3)?** [SONRA KARARLAŞTIRILIR] 🔗 X8
 > Neden önemli: Küçük buffer az gecikme demektir ama xrun (ses kopması) riskini artırır.

**G15. Xrun (ses kopması/çıtlama) toleransın nedir?** [BAŞLAMADAN ŞART] 🔗 X8
 A) Hiç olmamalı  B) Çok nadir olabilir  C) Gecikme azalıyorsa kabul
 > Neden önemli: Güvenlik payı ve CPU bütçesi bu tercihe göre ayarlanır.

**G16. Gecikmeyi nasıl ölçeceksin (osiloskop, loopback testi, yazılım)?** [SONRA KARARLAŞTIRILIR] 🔗 X8
 > Neden önemli: Ölçüm yoksa hedefe ulaşıp ulaşmadığımızı bilemeyiz.

**G17. Ses altyapısı için tercihin var mı?** [BAŞLAMADAN ŞART]
 A) JACK  B) PipeWire (JACK uyumluluk katmanı)  C) Doğrudan ALSA  D) Bilmiyorum
 > Neden önemli: mod-host JACK bekler; hangi katmanın gecikmesi, karmaşıklığı ve kararlılığı kabul edilebilir?

**G18. Gerçek zamanlı çekirdek konusunda tercihin var mı?** [SONRA KARARLAŞTIRILIR]
 A) Standart çekirdek + RT öncelik (rtprio, ulimit)  B) PREEMPT_RT çekirdeği  C) Bilmiyorum
 > Neden önemli: Çekirdek özelleştirmek kuruluma ve güncellemeye ek yük getirir.

**G19. CPU çekirdeklerini ayırma (ses sürecini ayrı çekirdeğe sabitleme, governor=performance, USB/ağ kapatma) konusuna yaklaşımın?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: UI ve ses süreçleri aynı çekirdeği paylaşırsa grafik yükü ses kopmasına neden olabilir.

**G20. 64-bit Raspberry Pi OS mi 32-bit mi? Hangi Debian sürümü (Bookworm/Trixie)?** [BAŞLAMADAN ŞART]
 > Neden önemli: LV2 plugin paketleri ve Rust derleme hedefi (aarch64/armv7) buna göre değişir.

**G21. mod-host ve plugin'ler için kaynak nedir?** [BAŞLAMADAN ŞART]
 A) Derleyeceğim (kaynak koddan)  B) Hazır paket/depo  C) MOD Audio/PiPedal'dan alınan  D) Bilmiyorum
 > Neden önemli: Sürüm, bağımlılık ve lisans bu seçime bağlı.

**G22. mod-host ile iletişim biçimi nasıl olacak ve hata/yeniden başlatma durumunda ne olacak?** [BAŞLAMADAN ŞART]
 > Neden önemli: Arayüz ve ses motoru ayrı süreçler olduğundan biri çökünce diğerinin davranışı tanımlı olmalı.

**G23. Süreç yönetimi: systemd ile mi, başka bir şeyle mi? Servis sırası ve bağımlılıkları nasıl?** [SONRA KARARLAŞTIRILIR] 🔗 X7
 > Neden önemli: Açılışta ses motorunun ve arayüzün doğru sırayla ve hızla başlaması buna bağlı.

**G24. Ses sürecinin RT önceliği ve bellek kilitleme (mlock) ayarlarını nasıl yapacaksın?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Yanlış ayar ses kopması ya da sistemin kilitlenmesine yol açar.

**G25. Pi'nin diğer işlerini (WiFi, Bluetooth, ağ, SSH, loglar) kapatma stratejin nedir?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Gereksiz servisler hem CPU hem gürültü hem de güvenlik riski.

**G26. Ağ bağlantısı cihazda olacak mı (WiFi/Ethernet)? Sadece geliştirme sırasında mı, kalıcı mı?** [BAŞLAMADAN ŞART]
 > Neden önemli: Müzisyen "telefon/bilgisayar gerekmesin" dediği için ağ sadece senin ihtiyacın olabilir; bakım için nasıl erişeceğini belirler.

## D. Plugin seçimi ve CPU bütçesi

**G27. Hangi LV2 plugin paketlerini düşünüyorsun?** (Örn. Calf, x42, MOD plugin'leri, Dragonfly Reverb, Invada, DISTRHO, Guitarix içindeki genel efektler) [BAŞLAMADAN ŞART] 🔗 X3
 > Neden önemli: Paket seçimi lisansı, bağımlılığı ve her efektin CPU maliyetini belirler.

**G28. Efektlerin CPU bütçesi: aynı anda kaç efekt çalışmalı ve toplam CPU yükü hedefin (% olarak) nedir?** [BAŞLAMADAN ŞART] 🔗 X3
 > Neden önemli: Pi 4'te ağır plugin'lerin (reverb, granüler, vocoder) toplamı hızla sınırı aşabilir.

**G29. Ağır efektler (uzun reverb, granüler, vocoder, pitch shifter) istenecek mi ve hangi kalitede?** [BAŞLAMADAN ŞART] 🔗 X3
 > Neden önemli: Bunlar Pi 4'te (ve MCU'da çok daha fazla) en ağır işlerdir; müzisyenin M14 ve M16 cevaplarıyla çelişebilir.

**G30. Plugin lisansları (GPL vb.) önemli mi? Cihazı ileride dağıtma/satma ihtimali var mı?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Lisanslar dağıtım koşullarını belirler.

**G31. Plugin parametreleri arayüzde otomatik mi üretilecek (LV2 meta verisinden), yoksa her efekt için elle tasarım mı?** [BAŞLAMADAN ŞART]
 > Neden önemli: 20–30 efekt için elle arayüz çok iş demek, otomatik üretim ise görünüm kalitesini sınırlar.

## E. Ekstralar (akort, looper, tempo, MIDI)

**G32. Akort ve looper'ı nasıl çözmeyi düşünüyorsun?** [SONRA KARARLAŞTIRILIR] 🔗 X11
 A) Plugin olarak  B) Kendi yazacağım  C) İlk sürümde yok  D) Bilmiyorum
 > Neden önemli: Müzisyen için akort neredeyse şart; looper ayrı bir ses yolu gerektirir.

**G33. Tap tempo ve efektlerin tempoya senkron çalışması için mod-host tarafında ne gerekiyor (BPM parametresi, transport)?** [SONRA KARARLAŞTIRILIR] 🔗 X11
 > Neden önemli: Her plugin tempoyu aynı şekilde desteklemez.

**G34. MIDI girişi (clock ve program change için), USB-MIDI ve ekspresyon pedalı için donanım yer ayıracak mısın?** [SONRA KARARLAŞTIRILIR] 🔗 X11
 > Neden önemli: Müzisyen M47'de davul makinesinden tempo almak istediğini söyleyebilir; sonradan eklemek kutuyu yeniden basmayı gerektirebilir.

## F. Zincir yapısı ve preset veri modeli

**G35. Zincir yapısı:** [BAŞLAMADAN ŞART]
 A) Yalnız seri  B) Seri + tek paralel kol  C) Serbest yönlendirme
 > Neden önemli: Paralel yol hem CPU hem arayüz karmaşıklığını artırır.

**G36. Preset geçişinde ses kesintisi nasıl ele alınacak?** [BAŞLAMADAN ŞART] 🔗 X4
 A) Zinciri kapatıp yenisini yükle (sessizlik olur)  B) İki zincir paralel, çapraz geçiş  C) Aynı efektler açık, sadece parametreler değişir  D) Bilmiyorum
 > Neden önemli: Müzisyenin M33–M34 cevabı ile teknik olarak yapılabilir olan burada karşılaşacak.

**G37. Preset veri modeli nasıl olmalı (zincir, parametreler, sıra, çalgı grubu/profili, ses seviyesi, tempo)?** [BAŞLAMADAN ŞART] 🔗 X13
 > Neden önemli: Preset'ler çalgıya göre gruplanacak (müzisyen M29–M32); bu yapı sonradan değiştirilmesi zor bir karar ve sürüm geçişleri için şema sürümü gerekir.

**G38. Preset'ler hangi biçimde ve nerede saklanacak (JSON dosyaları, SQLite, başka)?** [BAŞLAMADAN ŞART] 🔗 X13
 > Neden önemli: Salt okunur dosya sisteminde yazılabilir bir bölüm (veri bölümü) gerekir; bozulma ve atomik yazma önemli.

**G39. Preset yedekleme ve geri yükleme (USB bellek, ağ, SD kart kopyası)?** [BAŞLAMADAN ŞART] 🔗 X13
 > Neden önemli: Müzisyen cihazın tüm ayarlarını kaybedemez; ağ yok denilirse USB bellek gibi bir çözüm düşünülmeli.

## G. Arayüz mimarisi ve durum yönetimi

**G40. Arayüz ile ses motoru arasında doğru durumun (state) kimde olduğu nasıl tanımlanacak?** [BAŞLAMADAN ŞART] 🔗 X6
 A) Arayüz tek doğru kaynak  B) mod-host tek doğru kaynak  C) Ayrı bir durum servisi
 > Neden önemli: Çökme ve yeniden bağlantı senaryolarında tutarlılık buna bağlı.

**G41. Slint'i Pi 4'te KMS/DRM ile hangi grafik arka ucuyla (femtovg, skia, yazılım) kullanmayı düşünüyorsun ve hedef kare hızı nedir?** [BAŞLAMADAN ŞART] 🔗 X6
 > Neden önemli: Çizim yükü ses sürecinin CPU'sundan çalmamalı; arka uç seçimi performansı belirler.

**G42. Dokunmatik ve fiziksel knob birlikte nasıl çalışacak?** [BAŞLAMADAN ŞART] 🔗 X6
 A) Knob ekrandaki seçili öğeyi değiştirir (odak modeli)  B) Knob'lar sabit görevli  C) İkisi karışık
 > Neden önemli: Hangi parametrenin hangi knob'a bağlandığı arayüzün temel kurgusudur.

**G43. Ekran/menü yapısı için bir hiyerarşi düşünüyor musun (ana ekran, zincir, efekt, preset, ayarlar)?** [BAŞLAMADAN ŞART] 🔗 X6
 > Neden önemli: Müzisyenin M58 cevabıyla (kaç adımda ayar yapılabilmeli) birlikte bakılmalı.

**G44. Çoklu dil, tema, yazı tipi gereksinimi var mı (Türkçe karakter, büyük yazı, ikon seti)?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Yazı tipi ve karakter desteği arayüz dosyalarına sonradan eklemesi zor bir ayrıntı.

**G45. Arayüz çökerse veya yeniden başlarsa ses akışı kesilmeden çalışmaya devam etmeli mi?** [BAŞLAMADAN ŞART] 🔗 X7
 > Neden önemli: Ayrı süreç mimarisinin en büyük avantajı bu olabilir ama bunun için bilinçli tasarım gerekir.

## H. GPIO, encoder, buton, LED elektroniği

**G46. Kaç encoder, kaç ayak butonu, kaç LED planlıyorsun ve her birine ne görev düşünüyorsun?** [BAŞLAMADAN ŞART] 🔗 X5
 > Neden önemli: GPIO pin sayısı ve gerilim seviyeleri bu sayıya göre planlanır.

**G47. Pi'nin GPIO pin bütçesi: ses kartı HAT'ı veya ekran hangi pinleri kullanıyor, geriye kaç pin kalıyor?** [BAŞLAMADAN ŞART] 🔗 X5
 > Neden önemli: Bazı HAT'lar ve SPI ekranlar çok sayıda pini kaplar.

**G48. Encoder tipi (mekanik/optik, basmalı, kaç adım/tur) ve bunları Pi'ye bağlama yöntemi (doğrudan, I/O genişletici, mikrodenetleyici)?** [BAŞLAMADAN ŞART] 🔗 X5
 > Neden önemli: Mekanik encoder'ların sıçraması (debounce) ve hızlı çevirme sırasında adım kaybı yaygın bir sorundur.

**G49. Debounce stratejisi (donanım RC filtresi / yazılım) ve GPIO okuma yöntemi (kesme/yoklama, hangi kütüphane/çekirdek sürücüsü)?** [SONRA KARARLAŞTIRILIR] 🔗 X5
 > Neden önemli: Ayak butonuna iki kez basılmış gibi algılanması çalarken çok rahatsız edici.

**G50. Ayak butonu tipi (mekanik/ilk temas/ses çıkaran, LED'li, anlık/kalıcı)?** [BAŞLAMADAN ŞART] 🔗 X5
 > Neden önemli: Sahnede ayakla basılan butonun hissi ve dayanıklılığı ürün kalitesini belirler.

**G51. LED'ler nasıl sürülecek (doğrudan GPIO, sürücü IC, WS2812 gibi adreslenebilir)? Parlaklık ayarı?** [SONRA KARARLAŞTIRILIR] 🔗 X5
 > Neden önemli: Pi'nin GPIO akım sınırı ve ses hattına karışabilecek gürültü açısından önemli.

**G52. GPIO'dan ses hattına elektrik gürültüsü karışmaması için önlemin nedir (ayrı topraklama, kablo yönlendirme, ekranlama)?** [BAŞLAMADAN ŞART] 🔗 X10
 > Neden önemli: Dijital kontrol hatları ses girişine yakın olursa vızıltı ve çıtırtı yaratır.

## I. Kontrol yazılımı

**G53. GPIO olayları (encoder, buton) arayüze ve mod-host'a hangi yoldan ulaşacak (arayüz süreci içinde mi, ayrı küçük bir servis mi)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Ayak butonunun efekti açıp kapamasının arayüzün meşgul olmasından etkilenmemesi gerekir.

**G54. Rust'ta GPIO için hangi kütüphane/yaklaşım (gpiod, rppal, evdev rotary overlay) düşünüyorsun?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Pi 4'e özel sürücü seçimi çapraz derleme ve dağıtımı etkiler.

**G55. Knob dönüşlerinde parametre değişimi hızlandırma (ivme), hassas/kaba mod gerekecek mi?** [SONRA KARARLAŞTIRILIR] 🔗 X5
 > Neden önemli: Sonsuz dönen encoder'da kullanım hissi yazılımla verilen bir şeydir.

## J. Açılış süresi ve güvenilirlik

**G56. Hedef açılış süresi (fişi takıp ilk ses çıkana kadar) nedir ve en uzun kabul edilebilir süre?** [BAŞLAMADAN ŞART] 🔗 X7
 > Neden önemli: Müzisyen cevabı ile karşılaştırılacak; Pi OS'un normal açılışı 20–30 sn olabilir.

**G57. Çökme sonrası toparlanma: ses motoru, arayüz, tüm sistem için ne bekliyorsun?** [BAŞLAMADAN ŞART] 🔗 X7
 > Neden önemli: Sahnede bir şeyin çökmesi kaçınılmazdır; hızlı toparlanma kritik.

**G58. Fişi aniden çekme senaryosu: salt okunur kök dosya sistemi ve yazılabilir veri bölümü nasıl düzenlenecek?** [BAŞLAMADAN ŞART] 🔗 X7
 > Neden önemli: Bozulan SD kart cihazı açılmaz hale getirebilir.

**G59. Watchdog (donanım/yazılım) ve otomatik yeniden başlatma kullanılacak mı?** [SONRA KARARLAŞTIRILIR] 🔗 X7
 > Neden önemli: Donma durumunda kullanıcı müdahalesi olmadan toparlanma sağlar.

**G60. Hata günlükleri nasıl tutulacak ve nasıl okunacak (ekranda, USB'ye, ağdan)?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Sahada bir şey bozulursa neyin bozulduğunu bilebilmek gerekir.

## K. Güncelleme ve yedekleme

**G61. Cihaz güncelleme yöntemi nasıl olacak?** [BAŞLAMADAN ŞART] 🔗 X13
 A) SD kartı yeniden yazmak  B) USB bellekle  C) Ağdan (SSH/otomatik)  D) İlk sürümde elle
 > Neden önemli: Müzisyen cihazı kendisi güncelleyemeyecekse sen her seferinde müdahale etmek zorunda kalırsın.

**G62. Yeni sürümde eski preset'lerin korunması nasıl sağlanacak (şema sürümü, geçiş)?** [BAŞLAMADAN ŞART] 🔗 X13
 > Neden önemli: Preset kaybı müzisyen için en kötü sonuçtur.

## L. Güç ve gürültü

**G63. Güç kaynağı: resmi Pi USB-C adaptörü mü, harici 9V DC (pedal standardı) mı, başka?** [BAŞLAMADAN ŞART] 🔗 X10
 > Neden önemli: Pi 4'ün güç ihtiyacı (5V/3A) ile 9V pedal standardı arasında dönüştürme gerekir; güç sorunu "düşük voltaj" ve ses gürültüsüne yol açar.

**G64. Ses kartı ve Pi'yi ayrı güç hattından beslemek, güç filtresi veya izolasyon (ground loop) önlemleri düşünüyor musun?** [BAŞLAMADAN ŞART] 🔗 X10
 > Neden önemli: Anahtarlamalı güç kaynaklarının gürültüsü ses sinyalinde (özellikle sessiz anlarda) duyulur.

**G65. Cihazın güç tüketimi ve ısı hedefi (kutu içi sıcaklık, fan gürültüsü)?** [SONRA KARARLAŞTIRILIR] 🔗 X10
 > Neden önemli: Fan sesi mikrofona karışır, fansız soğutmada kutu sıcaklığı sınırı vardır.

## M. Kutu tasarımı ve dayanıklılık

**G66. Kutu dayanıklılığı hedefi: yerde ayakla basılabilir mi, taşınabilir mi, sahne kullanımı?** [BAŞLAMADAN ŞART] 🔗 X12
 > Neden önemli: 3D baskı plastik kutunun ayakla basılma ve darbe dayanımı sınırlıdır.

**G67. 3D yazıcı: hangi malzemeler (PLA, PETG, ABS/ASA), baskı hacmi, katman kalitesi?** [BAŞLAMADAN ŞART]
 > Neden önemli: Isı, mukavemet ve baskı boyutu kutu parçalarının tasarımını sınırlar.

**G68. Jack yerleşimi (giriş, çıkış, kulaklık, güç, USB) hangi yüzlerde olacak ve konnektörlerin tipi (6.35 mm, 3.5 mm, XLR)?** [BAŞLAMADAN ŞART] 🔗 X12
 > Neden önemli: Pedal tahtası kullanımında kabloların hangi yönden geleceği önemli.

**G69. Kutu boyut sınırın nedir (genişlik × derinlik × yükseklik)?** [BAŞLAMADAN ŞART] 🔗 X9
 > Neden önemli: Pi 4, ekran, ses kartı, güç modülü ve butonlar fiziksel olarak sığmak zorunda.

**G70. Soğutma: pasif (soğutucu/hava kanalı), fan, yok?** [BAŞLAMADAN ŞART] 🔗 X9
 > Neden önemli: Pi 4 ısınınca hız düşürür (throttling) ve bu ses kopmasına yol açabilir.

**G71. Su/toz/darbe koruması, ekran koruması (cam/akrilik), ve yanlışlıkla basılmaya karşı önlemler?** [SONRA KARARLAŞTIRILIR] 🔗 X12
 > Neden önemli: Sahnede içecek dökülmesi ve düşme sık görülen kazalardır.

**G72. Ekranın kutuya montajı (eğim, görüş açısı, yansıma) ve ışık sızdırmazlığı?** [SONRA KARARLAŞTIRILIR] 🔗 X6
 > Neden önemli: Ayakta duran bir müzisyen için ekran eğimi okunabilirliği belirler.

**G73. Kutu için bakım erişimi (SD kart, USB, GPIO, vidalar) ve kablo yönetimi?** [SONRA KARARLAŞTIRILIR] 🔗 X9
 > Neden önemli: Hata durumunda cihazı kolay açıp kapatabilmek gerekir.

## N. Geliştirme süreci, zaman ve deneyim

**G74. Mac'ten çapraz derleme ve test nasıl yapılacak?** [BAŞLAMADAN ŞART]
 A) Mac'te Docker ile aarch64 çapraz derleme  B) Pi üzerinde doğrudan derleme  C) Pi'ye uzaktan geliştirme (SSH/VSCode)  D) Bilmiyorum
 > Neden önemli: Slint + KMS arayüzünü Mac'te nasıl test edeceğin ve ses motorunu nasıl simüle edeceğin geliştirme hızını belirler.

**G75. Arayüzü donanım olmadan test etmek için bir yöntemin var mı (masaüstü penceresi, sahte mod-host, GPIO simülatörü)?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Her değişikliği Pi'de denemek çok yavaşlatır.

**G76. Haftada kaç saat ayırabiliyorsun ve ilk çalışan sürüm için hedef tarihin var mı?** [BAŞLAMADAN ŞART]
 > Neden önemli: Kapsamı gerçekçi tutmak için zaman bütçesi şart.

**G77. Deneyim seviyen: Rust (hiç/başlangıç/orta), Linux ses (ALSA/JACK/RT), elektronik (lehim/devre okuma), 3D tasarım (CAD)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Öğrenmen gereken konuların sırasını ve riskli alanları belirler.

**G78. Bu proje sence en riskli hangi kısım?** (Ses gecikmesi, Rust/Slint, GPIO, kutu, zaman…) [BAŞLAMADAN ŞART]
 > Neden önemli: Önce riskli olanı küçük bir deneyle doğrulamak (kanıt prototipi) projeyi korur.

**G79. Önce küçük deneyler (kanıt prototipi) yapmaya hazır mısın?** (Örn. Pi'de ses geçir + gecikmeyi ölç; ekrana Slint ile bir şey çiz; bir encoder'ı oku) [BAŞLAMADAN ŞART]
 > Neden önemli: Karar vermeden önce gerçek ölçüm, varsayımdan daha güvenilir.

**G80. İlk sürüm (MVP) senin için neyi içermeli ve neyi içermemeli?** (Örn. "tek giriş, 5 efekt, 8 preset, 2 ayak butonu, akort") [BAŞLAMADAN ŞART]
 > Neden önemli: MVP tanımı müzisyenin beklentisiyle çarpıştığında ilk çelişki burada ortaya çıkar.

**G81. Bütçe sınırın nedir (parça alımı + 3D baskı malzemesi)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Ses kartı ve güç çözümünün fiyatı ciddi bir fark yaratabilir.

**G82. PiPedal'ın hangi kısımlarını inceleyeceksin ve kodundan neyi alıp neyi kendi yazacaksın?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Lisans ve bakım yükü, ayrıca "web arayüzü istemiyoruz" kararıyla uyum.

## O. Platform ve gelecek (Pi → MCU olasılığı)

**G83. İkinci cihazı ya da MCU'ya geçişi ne zaman düşünüyorsun ve hedef platform ne olurdu?** [BAŞLAMADAN ŞART]
 A) Pi 4 ile kalırım  B) Geliştirme kartı + az PCB (örn. Daisy Seed, Teensy 4.x ses kartlı, STM32 kartları)  C) Henüz bilmiyorum  D) Diğer: ____
 > Neden önemli: Bu karar, bugün yazılacak ses motoru, efekt formatı ve arayüzün ne kadar yeniden kullanılabilir olacağını belirler.

**G84. Hedef birim maliyetin nedir ve kaç adet yapmayı düşünüyorsun (kişisel 1–2 adet mi, satış mı)?** [BAŞLAMADAN ŞART]
 > Neden önemli: Pi 4 + ekran + ses kartı maliyeti ile MCU kartı + ekran maliyetinin farkı bu soruya göre anlamlı olur.

**G85. MCU yolunda efektleri nasıl elde edeceksin?** [BAŞLAMADAN ŞART]
 A) Kendim yazarım (DSP)  B) Hazır MCU kütüphaneleri  C) Bilmiyorum
 > Neden önemli: Pi'deki hazır LV2 plugin'leri MCU'da çalışmaz; bu yolda efektlerin büyük bölümünü yeniden yazman gerekir ve iş yükü çok farklıdır.

**G86. Preset ve zincir tanımını platformdan bağımsız (taşınabilir) bir biçimde mi tutmak istiyorsun?** [BAŞLAMADAN ŞART] 🔗 X13
 > Neden önemli: Taşınabilir bir biçim, müzisyenin ayarlarının Pi'den MCU'ya geçişte kaybolmamasını sağlar.

**G87. Arayüzü (Rust + Slint) ileride MCU'ya da taşınabilir tutmak istiyor musun?** [SONRA KARARLAŞTIRILIR]
 > Neden önemli: Bu seçim ekran türünü (dokunmatik mi, küçük ekran + düğme mi) ve arayüz kodunun nasıl yazılacağını etkiler.

**G88. İlk cihaz için "bitti" ölçütün nedir?** (Örn. tek stereo giriş/çıkış, en az N efekt, çalgı başına M preset, açılış X sn) [BAŞLAMADAN ŞART]
 > Neden önemli: İkinci cihaza geçmeden önce ilk cihazın başarısını ölçecek net bir tanım gerekir.

---

### Çapraz-konu özet tablosu
| Kod | Konu | Bu listede | Müzisyen listesinde |
|---|---|---|---|
| X1 | Giriş/çıkış, sinyal yolu | G6–G9, G11 | M1, M3, M4, M6, M7, M11, M12 |
| X2 | Mono/stereo | G9, G10 | M8, M9 |
| X3 | Efekt sayısı, CPU | G27–G29 | M14, M16 |
| X4 | Preset geçişinde ses | G36 | M29–M34, M37, M71 |
| X5 | Knob/buton/LED | G46–G51, G55 | M20, M22–M26, M61 |
| X6 | Ekran, dokunmatik | G2, G40–G43, G72 | M28, M38, M39, M66 |
| X7 | Açılış, çökme, fiş çekme | G5, G23, G45, G56–G59 | M53–M55, M72 |
| X8 | Gecikme | G13–G16 | M68, M69 |
| X9 | Boyut, görünüm | G69, G70, G73 | M23, M57–M60 |
| X10 | Güç, gürültü | G52, G63–G65 | M13 |
| X11 | Tuner/looper/tempo/pedal | G32–G34 | M21, M44–M48 |
| X12 | Kullanım ortamı, dayanıklılık | G66, G68, G71 | M40, M50–M52, M62 |
| X13 | Yedek, güncelleme, preset kaybı | G37–G39, G61, G62, G86 | M36 |
