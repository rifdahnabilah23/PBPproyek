Nama    : Rifdah Nabilah Rahma

NPM     : 2206082890

Kelas   : PBP B
<br>
------------- TUGAS 2 --------------
<br>

Link Adaptable : https://riifood.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
Jawab: <br>
    Jadi ini penjelasan saya dalam menyelesaikan tugas 2 PBP.
    Langkah Pertama saya membuat Proyek ini, saya membuat satu repository lokal yang ada di laptop saya. Kemudian saya menginisiasi repositori tersebut dan mengkonfigurasikannya. Setelah itu, saya menghubungkan Repositori lokal dengan repositori yang sudah saya buat di github. Selanjutnya, saya membuat dan mengaktifkan virtual environment untuk mengisolasi package dan dependecies dari aplikasi. Saya juga membuat berkas requirements.txt yang isi dengan beberapa dependecies dan menjalankannya. Selanjutnya membuat proyek django yang diberi nama RiiFood. Riifood ini merupakan aplikasi dimana bisa pengguna dapat mengetahui informasi buah-buahan, stok, dan harganya. Setelah ini, saya mencoba mengonfigurasi proyek django saya dan menjalankannya di server. Saat sudah menjalankan Django di server, kita diarahkan ke halaman web yang mana memunculkan tampilan aplikasi. Kemudian mematikan server dan virtual environment serta menggungah proyek ini ke repositori dengan menambahkan berkas .gitignore.

    Langkah kedua sebelum saya membuat aplikasi main, saya kembali mengaktifkan virtual environment di terminal direktori utama. Kemudian saya menjalankan kode "python manage.py startapp main" untuk memulai membuat aplikasi main. Kemudian saya membuka file settings.py dan menambahkan 'main' di variabel installed_apps. Selanjutnya saya membuat direktori baru di dalam direktori main yang diberi nama template, di dalam template saya juga menambahkan file main.html yang dimana file ini untuk menampilkan data RiiFood. Didalam main.html saya membuat data-data yang berisi daftar buah-buahan yang dilengkapi dengan nama, harga, stok, dan juga deskripsinya. Saya menyajikan data-data dalam bentuk tabel.

    Langkah selanjutnya saya mengimplementasikan model pada aplikasi main. Implementasi ini dilakukan dengan cara menambahkan class Product yang memiliki atribut name, date_added, amount, description, dan juga price yang masing-masing memiliki tipe data yang berbeda-beda. Atribut ini dapat ditambah sesuai dengan aplikasi yang sedang dibuat. Selain itu, ketika ingin melakukan perubahan pada model, perlu melakukan migrasi.

    Langkah selanjutnya saya akan membuat suatu fungsi pada views.py untuk dihubungkan ke dalam template main.html yang akan menampilkan data-data. Pertama saya mengimport dahulu "from django.shortcuts import render" kemudian saya menambahkan fungsi show_main dengan parameter request. Di dalam fungsi saya membuat dictionary yang berisi data nama, macam-macam buah, masing-masing stok, harga, dan deskripsi dari buah-buahan tersebut. Selanjutnya saya melakukan render untuk tampilan main.html menggunakan fungsi render. Kemudian saya mengubah isi dari main.html untuk menampilkan data yang diambil dari model.

    Langkah selanjutnya saya akan melakukan routing pada proyek agar dapat menjalankan aplikasi main. Pertama saya membuat berkas urls.py yang berada di dalam direktori main. Kemudian saya inisiasi dengan cara mengimport path dari django.urls yang berfungsi untuk pola URL. Selain itu, saya juga mengimport show_main dari modul main.views untuk tampilan ketika url tersebut diakses. Kemudian menambahkan nama aplikasi dan menambahkan kode
    urlpatterns = [path('', show_main, name='show_main'),].

    Langkah selanjutnya saya akan melakukan routing pada urls.py pada aplikasi main. Pertama saya membuka berkas urls.py yang berada di direktori utama saya. Kemudian mengimport fungsi include dari django.urls dan menambahkan rute di dalam variabel urlpatterns dengan 
    path('main/', include('main.urls')).
    Setelah itu, jika ingin melihat tampilan web kita, jalankan terlebih dahulu proyek django dengan perintah 
    python manage.py runserver
    kemudian buka link http://localhost:8000/main/ .

    Setelah menyelesaikan semua task, saya memperbaharui repositori github saya dan melakukan deploy aplikasi dengan menggunakan adaptable yang dihubungkan dengan repositori github.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.<br>
JAWAB: <br>
![Foto bagan](https://github.com/rifdahnabilah23/PBPproyek/blob/82ca085c82cdf41df0a21c308b896bd5b9d0e8de/foto%20pbp.jpg) <br>
Saat client request, dia akan masuk melalui url.py. Di dalam file ini berisi pola URL yang akan digunakan untuk meneruskan request client ke tindakan yang sesuai dengan views.py. Nah views.py ini merupakan wadah yang mengelola logika dari aplikasi yang dimana request dari client akan di proses. models.py juga akan menggabungkan data-data yang dia peroleh dari models.py dan berkas html.Selanjutnya ada models.py yang memiliki peran untuk mengakses ke data yang di butuhkan untuk memproses request dengan cara read/write dari data tersebut. Dan yang terakhir ada berkas html yang akan digunakan untuk menghasilkan tampilan halaman web yang akan dikirimkan sebagai respons kepada client. 



3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?<br>
JAWAB:<br>
    Virtual environment adalah suatu utilitas yang digunakan untuk menciptakan lingkungan Python virtual yang bersifat terisolasi. Dalam konteks ini, "terisolasi" merujuk kepada keadaan di mana lingkungan tersebut bersifat terkunci dan tidak dapat dijangkau dari luar. Ketika program Python beroperasi dalam virtualenv, ia memiliki modul-modulnya sendiri dan tidak dapat diakses oleh program dari luar. Jadi ketika  bekerja pada beberapa proyek yang memerlukan dependensi yang berbeda, virtual environment memungkinkan untuk memisahkan dependensi dari setiap proyek. Hal ini memastikan bahwa versi-dependensi yang berbeda tidak berinteraksi atau menyebabkan konflik satu sama lain. Tanpa virtual environment, mungkin akan mengalami kesulitan ketika proyek 1 memerlukan versi X dari suatu pustaka, sedangkan proyek 2 membutuhkan versi Y. Jadi, membuat aplikasi web berbasis Django tanpa menggunakan virtual environment tidak disarankan karena tidak dapat mengisolasi dependensi dengan baik dan membuat proyek menjadi tidak teratur.



4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.<br>
JAWAB :<br>
    ------ MVC (Model-View-Controller) ------ <br>
    Model merupakan kumpulan kelas yang mendefinisikan logika bisnis (model bisnis) dan prosedur akses data (model data). Selain itu, ini menentukan bagaimana data dapat dimodifikasi dan dikontrol oleh aturan bisnis.<br>

    View merupakan komponen UI seperti CSS, jQuery, html, dll. View hanya bertanggung jawab untuk menampilkan data yang diterima dari pengontrol sebagai hasilnya. Ini juga mengubah model menjadi UI. 

    Controller bertanggung jawab untuk memproses permintaan yang masuk. Ia menerima masukan dari pengguna melalui view, kemudian memproses data pengguna dengan bantuan Model dan meneruskan hasilnya kembali ke view. Biasanya, ini bertindak sebagai koordinator antara view dan Model. 


    ------ MVT (Model-View-Template) ------ 

    Model merupakan kumpulan kelas yang mendefinisikan logika bisnis (model bisnis) dan prosedur akses data (model data). Selain itu, ini menentukan bagaimana data dapat dimodifikasi dan dikontrol oleh aturan bisnis.

    View merupakan komponen UI seperti CSS, jQuery, html, dll. View hanya bertanggung jawab untuk menampilkan data yang diterima dari pengontrol sebagai hasilnya. Ini juga mengubah model menjadi UI.

    Template merupakan komponen pengganti controller dalam MVC.  Ia adalah bagian dari view yang menentukan bagaimana data dari model akan ditampilkan.

    ------ MVVM (Model-View-ViewModel) ------

    Model merupakan kumpulan kelas yang mendefinisikan logika bisnis (model bisnis) dan prosedur akses data (model data). Selain itu, ini menentukan bagaimana data dapat dimodifikasi dan dikontrol oleh aturan bisnis.

    View merupakan komponen UI seperti CSS, jQuery, html, dll. View hanya bertanggung jawab untuk menampilkan data yang diterima dari pengontrol sebagai hasilnya. Ini juga mengubah model menjadi UI.

    ViewModel bertanggung jawab untuk mengekspos metode, perintah, dan properti lain yang membantu mempertahankan status view, memanipulasi model sebagai hasil tindakan pada view, dan memicu peristiwa dalam view itu sendiri.

    --- Perbedaan ---

    MVC, MVT, dan MVVM memiliki beberapa perbedaan dalam suatu komponen diantaranya adalah sebagai berikut:

    1. Architecture and Layering
        - MVC menempatkan view sebagai lapisan paling atas  terintegrasi erat dengan controller, dan model berada di bawah. Hal ini dapat menyebabkan potensi masalah keamanan.
        - MVT memungkinkan akses langsung antara view dan model, dengan Template bertindak sebagai perantara.
        - MVVM membatasi paparan antar view, dengan tampilan yang mengikat langsung ke ViewModel, sehingga meningkatkan pemisahan perhatian.

    2. Performance
        - MVT sering kali menawarkan performa UI terbaik karena kontrol langsungnya terhadap view dan model.
        - MVVM dapat menimbulkan overhead kinerja, terutama dengan data binding, yang berpotensi memengaruhi tugas kompleks.
        - MVC memiliki kinerja yang beragam dibandingkan dengan MVT dan MVVM, karena berada di tengah-tengah.

    3. Compatibility and Customization
        - MVVM unggul dalam kompatibilitas, terutama untuk pemrosesan data, namun mungkin memiliki trade-off kinerja.
        - MVT menawarkan lebih sedikit opsi penyesuaian dibandingkan pola lainnya.
        - MVC memberikan lebih banyak peluang penyesuaian dan dianggap sebagai pola desain yang lebih matang.



Referensi: <br>
https://www.dotnettricks.com/learn/designpatterns/understanding-mvc-mvp-and-mvvm-design-patterns <br>
https://xperti.io/blogs/mvc-vs-mvp-vs-mvvm/ <br>
https://www.petanikode.com/python-virtualenv/ <br>
<br>


------------ TUGAS 3 ------------ <br>

1. Apa perbedaan antara form POST dan form GET dalam Django? <br>
JAWAB: <br>
    POST dan GET merupakan method dalam Django yang digunakan untuk menghandle form. Mereka memiliki beberapa perbedaan diantaranya method POST harus selalu digunakan jika data akan mengakibatkan perubahan pada database server, karena dapat dibuat lebih tahan terhadap serangan CSRF (cross-site forgery request) dibandingkan dengan menggunakan method GET. Sedangkan method GET hanya boleh digunakan untuk formulir yang tidak mengubah data pengguna (misalnya formulir pencarian). Ini direkomendasikan ketika ingin mem-bookmark atau membagikan URL. Selain itu, Formulir masuk Django dikembalikan menggunakan method POST, di mana browser menggabungkan data formulir, mengkodekannya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Sedangkan method GET menggabungkan data yang dikirimkan ke dalam string, dan menggunakannya untuk membuat URL. URL berisi alamat tujuan pengiriman data, serta kunci dan nilai data. <br>

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br>
JAWAB: <br>
    XML, JSON, dan HTML memiliki beberapa perbedaan diantaranya adalah sebagai berikut: <br>

    ----- Tujuan ----- 
    - XML digunakan terutama untuk membangun dan mengorganisir data dengan cara yang menjaga hierarki dan struktur data. Ini dirancang sebagai format universal untuk pertukaran data.
    - JSON digunakan untuk pertukaran data ringan antara server dan klien, dan erat kaitannya dengan JavaScript. Ini umum digunakan untuk mengirimkan data antara server dan aplikasi web.
    - HTML terutama digunakan untuk mendefinisikan struktur dan presentasi dokumen web, terutama untuk menampilkan konten di peramban web. Meskipun dapat berisi data, itu dirancang utamanya untuk menampilkan konten kepada pengguna. 

    ----- Struktur Data ----- 
    - XML menyediakan struktur hierarkis dengan elemen bertingkat dan atribut. Ini memungkinkan untuk struktur data kompleks dan berlapis.
    - JSON mewakili data sebagai pasangan kunci-nilai dan array, membuatnya mudah digunakan untuk data terstruktur. Cocok untuk merepresentasikan objek dan daftar.
    - HTML berfokus pada mendefinisikan tata letak dan presentasi konten daripada struktur data. Meskipun dapat berisi data, ia kurang memiliki kemampuan struktur data yang ketat seperti XML dan JSON. 

    ----- Keterbacaan -----
    - XML mudah dibaca oleh manusia tetapi cenderung lebih panjang karena penggunaan tag dan atributnya, membuatnya kurang ringkas.
    - JSON sangat mudah dibaca dan lebih ringkas, sehingga memudahkan manusia dan mesin untuk menguraikan dan menghasilkannya.
    - HTML dirancang untuk keterbacaan manusia dan rendering di peramban web, dengan tag yang menjelaskan bagaimana konten harus ditampilkan



3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br>
JAWAB: <br>

    JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan yang sering digunakan dalam aplikasi web modern dan API. Format ini sangat populer untuk mengirim dan menyimpan data dalam berbagai aplikasi karena kesederhanaannya, efisiensinya, dan kemampuan untuk berintegrasi dengan berbagai platform. JSON mudah dibaca dan ditulis, sehingga menjadi pilihan yang sangat baik untuk pertukaran data antar komponen perangkat lunak. JSON menjadi sangat populer karena dapat digunakan secara lintas platform. Hampir semua browser modern mendukung JSON, dan banyak bahasa pemrograman seperti Java, JavaScript, Node.js, dan Python juga mendukungnya. JSON juga mendukung jenis data ARR (Arrays and Ranges), yang memudahkan penggunaan array dan rentang data dalam kode. Selain itu, JSON dapat digunakan untuk menukar data antara aplikasi perangkat lunak atau API yang berbeda  
<br>

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
JAWAB: <br>
    Jadi ini penjelasan saya dalam menyelesaikan tugas 3 PBP. <br>

    Langkah pertama yang harus dilakukan ialah membuat input form untuk menambahkan objek model pada app. Nah pertama saya buka cmd file Riifood dan mengaktifkan virtual environment. kemudian saya membuka folder Riifood dan mengubah path dalam urls.py yaitu path main/ menjadi '' pada varibel urlpatterns. Selanjutnya saya mengimplementasikan skeleton yang dimana berperan sebagai kerangka views untuk memastikan konsistensi dalam desain situs web. cara mengimplementasikannya yaitu pertama saya membuat folder templates pada root folder, kemudian saya tambahkan file html baru untuk template dasar yang akan digunakan sebagai kerangka umum. file html baru saya beri nama base.html dan saya tambahkan kode baru yang pernah diajarkan di tutorial 2. Selanjutnya saya membuka subdirektori riifood dan menambahkan kode di file settings.py pada variabel TEMPLATES. saya menambahkan Value pada key DIRS yang berisi BASE_DIR / 'templates' supaya berkas base.html dapat terdeteksi. Kemudian saya menambahkan kode {% extends 'base.html' %} dipaling atas dan mengapit kode yang sudah saya buat di tutorial sebelumnya dengan diawali {% block content %}
    dan diakhiri {% endblock content %} pada berkas main.html di dalam direktori main dan di folder templates. Nah langkah selanjutnya saya akan membuat form input data. Pertama membuat berkas baru bernama forms.py pada direktori main yang digunakan untuk membuat struktur dari form agar dapat menerima data produk baru. Saya menambahkan beberapa kode yang sama seperti tutorial 2 kemarin. Namun di dalam class meta, saya menambahkan item di variabel fields yaitu amount dan gambar. Kemudian saya membuka file views.py pada direktori main dan menambahkan tiga import. Lalu saya menambahkan method create_product yang akan menerima parameter request. Method ini dapat digunakan suatu form untuk menambahkan data produk secara otomatis ketika data di kirimkan. Method ini menggunakan metode form POST. Selanjutnya saya mengubah dan menambahkan beberapa kode pada fungsi show_main. Saya menambahkan products = Product.objects.all(), dan mengubah semua data yang saya inisiasi manual menjadi satu key products dan value products yang akan mengambil seluruh object product yang tersimpan pada database. Selanjutnya saya membuka urls.py pada direktori main dan mengimport fungsi create_product serta menambahkan path urls ke dalam urlpatterns untuk mengakses fungsi yang sudah diimport tadi. Kemudian saya membuat berkas html baru pada direktori templates pada main dengan nama create_product.html yang selanjutnya saya tambahkan kode yang sebelumnya saya pelajari di tutorial 2. html ini digunakan saat menekan add new product, kemudian diisi data-data yang tersedia. Setelah itu, saya membuka lagi main.html disini saya menambahkan kode di dalam {% block content %}. Di tahap ini saya merapihkan tampilan html saya, sama seperti tugas 2 tampilan html saya namun ada button untuk add new product yang setiap saya isi, data yang ditampilkan akan di loop. Add new product ini akan mendirect tampilan awal ke halaman form. 

    Langkah Selanjutnya, bagaimana mengimplementasikan fungsi untuk mengembalikan data dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. Sebelumnya saya sudah menjelaskan bagaimana menampilkan data dalam format HTML pada langkah pertama. Selanjutnya saya akan menjelaskan bagaimana saya mengembalikan data dalam bentuk XML. jadi saya menambahkan import HttpResponse dan Serializer pada bagian paling atas dari file views.py pada folder main. Setelah itu, saya membuat fungsi di dalamnya dengan nama show_xml yang menerima parameter request. Di fungsi ini di bentuk sebuah variabel yang akan menyimpan seluruh data dari hasil query pada product yang kemudian akan ngereturn HttpResponse yang terdapat hasil query dari data parameter yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml". Selanjutnya saya akan menjelaskan bagaimana saya mengembalikan data dalam bentuk JSON. Masih di file dan folder yang sama yaitu views.py di main, saya membuat fungsi yang bernama show_json dengan parameter request. Di fungsi ini juga di bentuk sebuah variabel yang akan menyimpan seluruh data dari hasil query pada product yang kemudian akan ngereturn HttpResponse yang berisi hasil query dari data yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json". Selanjutnya saya akan menjelaskan bagaimana saya mengembalikan data dalam bentuk XML dan JSON berdasarkan id. Masih di file dan folder yang sama, saya akan membuat dua fungsi baru yaitu fungsi show_xml_by_id dan show_json_by_id. Fungsi ini akan menerima parameter berupa request dan id produk. Kemudian di masing-masing fungsi saya menambahkan sebuah variabel data = Product.objects.filter(pk=id), dimana ini akan menyimpan hasil dari data dengan id tertentu. Dari kedua fungsi ini akan nge return HttpResponse yang didalamnya berisi data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON). 

    Langkah Selanjutnya saya akan menjelaskan tahap saya dalam membuat routing urls untuk masing-masing views dari fungsi XML, JSON, XML by ID, dan JSON by ID. pertama saya buka file urls.py yang berada pada folder main dan mengimpor fungsi-fungsi yang sudah saya buat di tahap 2. Kemudian saa menambahkan ke dalam variabel urlpattern masing-masing path url untuk mengakses fungsi yang sudah di import sebelumnya. 

    Langkah selanjutnya saya mencoba akses kelima url pada tahap 2 menggunakan postman. Saya membuat request baru dengan method GET. Berikut ini tampilan postman jika saya mengakses: 
<br>

- HTML <br>
        ![Tampilan HTML](https://github.com/rifdahnabilah23/PBPproyek/blob/0dd40a9036ee36c44d9d38584aa6bccb0f9bd52e/Tampilan%20HTML.jpg) <br>
    - XML <br>
        ![Tampilan XML](https://github.com/rifdahnabilah23/PBPproyek/blob/0dd40a9036ee36c44d9d38584aa6bccb0f9bd52e/Tampilan%20XML.jpg) <br>
    - JSON <br>
        ![Tampilan JSON](https://github.com/rifdahnabilah23/PBPproyek/blob/0dd40a9036ee36c44d9d38584aa6bccb0f9bd52e/Tampilan%20JSON.jpg) <br>
    - XML by ID <br>
        ![Tampilan XML by ID](https://github.com/rifdahnabilah23/PBPproyek/blob/0dd40a9036ee36c44d9d38584aa6bccb0f9bd52e/Tampilan%20XML%20by%20ID.jpg) <br>
    - JSON by ID <br>
        ![Tampilan JSON by ID](https://github.com/rifdahnabilah23/PBPproyek/blob/0dd40a9036ee36c44d9d38584aa6bccb0f9bd52e/Tampilan%20JSON%20by%20ID.jpg) <br>



Referensi:<br>
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms <br>
https://docs.djangoproject.com/en/4.2/topics/forms/ <br>
https://technewuk.com/what-is-json-and-why-should-you-care/ <br>
https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb  <br>



---------------- Tugas  4   ---------------- <br>

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? <br>
JAWAB: <br>
    Django UserCreationForm adalah form di dalam django yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web. Dia memiliki 4 bagian yaitu username, password1, dan password2 (yang umumnya digunakan untuk konfirmasi password). Untuk menggunakan UserCreationForm, kita perlu mengimport dari django.contrib.auth.forms.<br>
    Kelebihan<br>
    - Mudah untuk digunakan <br>
    - Memiliki validasi bawaan untuk memastikan inputan pengguna mematuhi persyaratan yang ditentukan.<br>
    - Dapat disesuaikan dengan desain proyek.<br>

    Kekurangan <br>
    - Memiliki batas penggunaan, UserCreationForm digunakan untuk pendaftaran yang sederhana dan tidak cocok untuk pembuataan pendaftaran yang rumit.<br>
    - Masalah keamanan, saat menggunakan UserCreationForm kita perlu menambahkan langkah-langkah keamanan tambahan ke proses pendaftaran, seperti verifikasi CAPTCHA. <br>
    - Tantangan Internasional, UserCreationForm mungkin tidak menangani i18n dengan mudah untuk semua bahasa. <br>


2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
JAWAB: <br>
    Autentikasi<br>
    - Dalam proses autentikasi , identitas pengguna diperiksa untuk memberikan akses ke sistem.<br>
    - Dalam proses autentikasi, pengguna atau orang diverifikasi.<br>
    - Autentikasi menentukan apakah orang tersebut adalah pengguna atau bukan. Biasanya memerlukan detail login pengguna.<br>

    Otorisasi<br>
    - Saat dalam proses otorisasi, otoritas orang atau pengguna diperiksa untuk mengakses sumber daya. <br>
    - Saat dalam proses ini, pengguna atau orang divalidasi. <br>
    - Otorisasi mengontrol akses ke tampilan, model, dan bagian lain dari aplikasi. Ini memastikan bahwa pengguna hanya dapat mengakses data dan melakukan tindakan yang izinnya mereka miliki.<br>

    Keduanya penting untuk memastikan keamanan, privasi, dan fungsionalitas aplikasi web Django, dan mereka bekerja sama untuk menciptakan sistem kontrol akses yang kuat. <br>


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
JAWAB: <br>
    Cookies adalah potongan kecil data yang dikirimkan server ke browser web pengguna untuk mengidentifikasi dan menyimpan informasi tentang pengguna. Cookie digunakan untuk tujuan seperti membuat pengguna tetap login, mengingat preferensi pengguna, atau melacak perilaku pengguna. <br>
    Django menggunakan cookie untuk mengelola data sesi pengguna dengan menyimpan pengidentifikasi sesi unik (ID sesi) dalam cookie pada browser pengguna. ID sesi ini digunakan untuk mengaitkan interaksi pengguna dengan server di beberapa permintaan. <br>


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
JAWAB: <br>
    Penggunaan cookie dalam pengembangan web secara umum aman bila diterapkan dan dikelola dengan benar.Namun,terdapat potensi risiko dan pertimbangan keamanan yang harus diwaspadai yaitu <br>
    - Privasi Data, Menyimpan data sensitif pengguna dalam cookie tanpa enkripsi atau perlindungan yang tepat dapat memaparkannya kepada calon penyerang jika cookie disadap. <br>
    - Cross-Site Scripting (XSS), Jika aplikasi web Anda rentan terhadap serangan XSS, penyerang mungkin menyuntikkan skrip berbahaya yang dapat membaca atau memodifikasi cookie di browser pengguna. <br>
    - Masa Aktif Cookie, Cookie dapat memiliki waktu kedaluwarsa yang berbeda-beda, dan penting untuk mengelolanya dengan benar. Cookie yang tetap berada di perangkat pengguna tanpa batas waktu dapat menimbulkan risiko keamanan dan privasi. <br>


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
JAWAB: <br>

    Ceklis 1 : Mengimplementasikan fungsi registrasi, login, dan logout

    - Langkah pertama saya membuat form registrasi. 

        1. Saya membuka file views.py yang ada di main, kemudian mengimport redirect, UserCreationForm, dan messages.

        2. Masih di dalam file itu saya membuat fungsi register yang menerima parameter request yang isinya sama seperti dalam tutorial.

        3. Saya membuat file HTML baru di dalam direktori template yang ada di main dengan nama register.html. Di dalam file ini saya  isi dengan template yang tersedia di dalam tutorial.

        4. Saya import fungsi register tadi ke dalam urls.py yang berada di main.

        5. Kemudian saya hubungkan path url nya ke dalam urlpatterns supaya dapat mengakses fungsi register tadi.


    - Langkah kedua saya membuat form Login.

        1. Saya membuka file views.py yang ada di main, kemudian mengimport authenticate dan login.

        2. Masih di dalam file itu saya membuat fungsi login yang menerima parameter request yang isinya sama seperti dalam tutorial.

        3. Saya kemudian membuat file HTML baru di dalam direktori template yang ada di main dengan nama login.html. Di dalam file ini saya  isi dengan template yang tersedia di dalam tutorial.

        4. Saya import fungsi login tadi ke dalam urls.py yang berada di main.

        5. Kemudian saya hubungkan path url nya ke dalam urlpatterns supaya dapat mengakses fungsi login tadi.


    - Langkah ketiga saya membuat form Logout.

        1. Saya membuka file views.py yang ada di main, kemudian mengimport logout.

        2. Masih di dalam file itu saya membuat fungsi logout yang menerima parameter request yang isinya sama seperti dalam tutorial.

        3. Saya kemudian membuka berkas main.html yang berada dalam direktori template di main. Selanjutnya saya menambahkan beberapa kode di bawah kode add new product untuk menambah button logout.

        4. Saya import fungsi logout tadi ke dalam urls.py yang berada di main.

        5. Kemudian saya hubungkan path url nya ke dalam urlpatterns supaya dapat mengakses fungsi logout tadi.


    - Setelah semuanya sudah saya buat, kemudian mengimplementasikan form di akses halaman main. Pertama saya import login_required pada views.py yg berada di main. Lalu saya tambahkan kode
    @login_required(login_url='/login')
    di atas fungsi show_main supaya halaman main hanya dapat diakses oleh pengguna yang sudah login.

    Ceklis 4 : Menampilkan informasi pengguna sedang logged in dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    - Langkah pertama menerapkan cookies

        1. Saya mengimport HttpResponseRedirect, reverse, dan datetime pada berkas views.py yang ada pada main.

        2. Saya kemudian menambahkan fungsi last_login pada fungsi login_user dengan cara mengganti kode yang tersedia pada blok "if user is not None" dengan kode yang tersedia di tutorial.

        3. Kemudian menambahkan kode di dalam variabel context yang berada di fungsi show_main dengan kode "'last_login': request.COOKIES['last_login']"

        4. Kemudian saya ubah fungsi logout_user menjadi seperti yang di tutorial.

        5. Saya selanjutnya menambahkan potongan kode di main.html untuk menampilkan keterangan Sesi terakhir login dari kode yang sudah di buat sebelumnya.

    - Untuk menampilkan informasi pengguna sedang login seperti username, ini berkaitan dengan ceklis 3.


    Ceklis 3: Menghubungkan model Item dengan User

    - Berikut ini adalah langkah-langkah nya

        1. Saya mengimport user pada models.py yang berada di main.

        2. Kemudian menambahkan model Product dengan nama user.

        3. Saya mengubah kode yang berada di dalam fungsi create_product yang berada di views.py di main dengan kode yang sesuai di tutorial kemarin.

        4. Kemudian saya mengubah dan menambahkan kode di fungsi show_main. Kode yang saya tambahkan ialah "products = Product.objects.filter(user=request.user)" yang saya letakan di atas variabel context. Kode yang saya ubah ialah di dalam context di key nama, saya ubah jadi "'name': request.user.username,".

        5. Kemudian saya lakukan migrasi.


    Ceklis 2 : Membuat dua akun pengguna dengan masing-masing tiga dummy data

    - Berikut ini adalah langkah-langkah nya

        1. Pertama saya membuat dua akun dahulu menggunakan form register.

        2. Setelah itu, saya login masing-masing akun.

        3. Kemudian saya membuat dummy data dengan add product sebanyak 3 kali.

        4. Data-data yang sudah saya buat langsung di tampilkan di halaman utama.
        
        5. Data-data ini akan langsung di simpan di database program.


Referensi:
https://www.javatpoint.com/django-usercreationform <br>
https://www.geeksforgeeks.org/difference-between-authentication-and-authorization/ <br>
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies <br>