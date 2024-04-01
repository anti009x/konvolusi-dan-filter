1. Filter Citra Digital
Filter citra digital digunakan untuk memodifikasi atau meningkatkan citra. Filter ini dapat dibagi menjadi beberapa jenis berdasarkan fungsinya:
1.1 Low Pass Filter (Lolos Bawah)
Low Pass Filter (LPF) digunakan untuk menghilangkan noise atau detail halus dari citra, sehingga menghasilkan citra yang lebih halus. LPF melewatkan frekuensi rendah dan menghilangkan frekuensi tinggi.
1.2 High Pass Filter (Lolos Atas)
High Pass Filter (HPF) digunakan untuk meningkatkan detail atau tepi pada citra. HPF melewatkan frekuensi tinggi dan menghilangkan frekuensi rendah, sehingga dapat digunakan untuk deteksi tepi.
1.3 High Boost
High Boost adalah teknik filter yang digunakan untuk meningkatkan kontras citra dengan menambahkan versi tajam dari citra ke versi aslinya. Ini sering digunakan untuk memperjelas detail citra yang kabur.
1.4 Filter Penebalan Garis
Filter penebalan garis digunakan untuk membuat garis atau tepi dalam citra menjadi lebih tebal. Ini berguna dalam aplikasi pengolahan citra seperti pengenalan pola atau peningkatan visualisasi.
2. Pengaburan (Blurring)
Pengaburan digunakan untuk menghaluskan citra, mengurangi detail dan noise. Ada beberapa metode pengaburan:
2.1 Media
Filter median menggantikan setiap piksel dalam citra dengan median dari nilai piksel di sekitarnya. Ini efektif untuk mengurangi noise salt-and-pepper.
2.2 Blur
Blur atau Box Blur adalah teknik pengaburan sederhana yang menggantikan setiap piksel dengan rata-rata nilai piksel di sekitarnya. Ini menghasilkan efek pengaburan yang seragam.
2.3 Gaussian
Gaussian Blur menggunakan kernel Gaussian untuk menghaluskan citra. Ini mengurangi noise dan detail dengan cara yang lebih alami dibandingkan dengan Box Blur.
2.4 Bilateral
Bilateral Filter adalah teknik pengaburan yang mengurangi noise sambil mempertahankan tepi. Ini melakukan ini dengan mempertimbangkan perbedaan intensitas piksel, sehingga tepi tetap tajam sementara area homogen dihaluskan.
3. Noise Filter
Filter noise digunakan untuk mengurangi atau menghilangkan noise dari citra.
3.1 Menambahkan Noise
Dalam beberapa kasus, noise ditambahkan ke citra untuk tujuan pengujian atau untuk meningkatkan kinerja algoritma pengolahan citra tertentu.
3.2 Menggunakan Filter Median
Filter median efektif untuk mengurangi noise salt-and-pepper, seperti yang dijelaskan di atas.
3.3 FastNIMeanDenoising
Metode ini digunakan untuk mengurangi noise pada citra grayscale. Ini menggunakan algoritma Non-Local Means untuk menghilangkan noise sambil menjaga detail citra.
3.4 FastNlMeansDenoisingColored
Mirip dengan FastNIMeanDenoising, tetapi dioptimalkan untuk citra berwarna. Ini mengurangi noise pada citra berwarna sambil mempertahankan kualitas dan detail citra.
