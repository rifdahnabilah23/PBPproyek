Nama    : Rifdah Nabilah Rahma

NPM     : 2206082890

Kelas   : PBP B

Link Adaptable : https://riifood.adaptable.app/

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