
import discord 
from discord.ext import commands
import os
from main import gen_pass
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def gen(ctx, count_gen = 10):
    await ctx.send(gen_pass(count_gen))
@bot.command()
async def mem(ctx):
    r = random.choice(os.listdir('images'))
    with open('images/'+ r , 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command()
async def bunga(ctx):
    r = 'IMG-20160823-WA0020.jpg'
    with open('kerajinan_tangan/'+ r , 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send('''1. Alat dan bahan

c. Langkah selanjutnya adalah dengan melipat kertas origami warna orange menjadi dua bagian, lalu gunting sejajar. Sementara itu, untuk membuat mahkota bunga, lipat lah kertas origami warna putih menjadi beberapa lipatan, lalu gunting menyerupai mahkota bunga.
d. Lilitkan kertas berwarna orange yang sudah digunting pada tangkai yang telah dibuat sebelumnya. Beri lem tembak dan pasang mahkota putih satu per satu dengan cara melingkar sehingga membentuk rangkaian mahkota yang pertama enam helai mahkota bunga.
e. Untuk membuat kelopak bunga, Anda perlu menggunting kertas origami berwarna hijau tua membentuk bintang, lalu beri lubang pada bagian tengahnya dan masukkan tangkai. Beri lem tembak pada bawah bunga dan tempelkan pada kelopak bunga serta lipat setiap sisi kelopak bunga.
f. Buatlah mahkota bunga menjadi mekar dan Anda dapat membuat serangkaian bunga ini untuk diletakkan di dalam vas.''',file=picture)

@bot.command()
async def kupu_kupu(ctx):
    r = 'maxresdefault (1).jpg'
    with open('kerajinan_tangan/'+ r , 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send('''Lipatlah kertas menjadi dua bagian. Caranya, dengan melipat sudut kiri atas ke sudut kanan bawah.Selanjutnya, lipat kembali kertas secara diagonal ke semua bagian.Lalu, lipat ke dalam hingga membentuk segitiga seperti gunung.Kemudian, balik kertas dan lipat kembali ke bagian tengah hingga ujung atas melebihi bagian atas.Terakhir, lipat untuk mengunci dan menarik bagian sayap.

''',file=picture)
@bot.command()
async def tas(ctx):
    r = 'tas.jpg'
    with open('kerajinan_tangan/'+ r , 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send('''Menyiapkan Alat dan Bahan Terlebih Dahulu

5. Menggabungkan Anyaman-Anyaman Plastik
Anyaman-anyaman plastik yang sudah rapi tinggal disambungkan satu sama lain. Anda tinggal menyelipkan anyaman pada bagian vertikal anyaman lainnya. Proses ini harus dilakukan terus-menerus hingga anyaman berbentuk melingkar seperti kantung.
6. Membuat Tali Tas dari Sisa Lipatan
Jika tas plastik sudah terbentuk sempurna, maka Anda bisa melanjutkan prosesnya dengan membuat tali tas. Manfaatkan sisa lipatan plastik yang sudah dianyam untuk membuat bentuk segitiga. Kemudian, hubungkan ujung segitiga dengan segitiga lainnya agar saling mengunci dan membentuk tali panjang.
7. Menjahit Tali Agar Menyatu dengan Tas Plastik
Anda bebas menentukan panjang tali sesuai kebutuhan dan selera. Tali plastik yang sudah jadi bisa segera dijahit pada kedua ujung tas plastik. Pastikan bahwa jahitannya benar-benar kuat supaya tali tas tidak mudah sobek.
8. Melapisi Bagian Dalam Tas dengan Furing
Langkah terakhir dalam cara membuat kerajinan dari plastik deterjen berbentuk tas adalah melapisi bagian dalam tas dengan furing. Penggunaan furing akan membuat tas plastik lebih kuat karena terdiri dari lapisan ganda. Usahakan untuk memilih furing yang warnanya senada dengan plastik kemasan Rinso supaya tampak lebih eye catching. Anda juga bisa menambahkan ritsleting supaya tas dapat ditutup dengan sempurna.

Wah, cara membuat kerajinan dari plastik deterjen Rinso ternyata praktis dan hasilnya sangat bermanfaat, ya. Mulai sekarang, jangan buang dulu bungkus Rinso yang sudah kosong. Manfaatkan plastik kemasan Rinso untuk membuat kerajinan tangan yang punya nilai pakai.''',file=picture)

@bot.command()
async def tong(ctx):
    r = 'th (1).jpeg'
    with open('kerajinan_tangan/'+ r , 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send('''
. Semakin banyak botol air yang Anda miliki, semakin besar tempat sampah yang akan Anda buat.
Cuci botol bekas sebelum memasuki proses produksi. Ini juga merupakan botol untuk menjaganya tetap steril dari kuman berbahaya.
Setelah semua botol dibilas, keringkan agar tidak banyak air yang keluar.
Kumpulkan semua botol untuk membentuk lingkaran atau ikuti kreasi Anda sendiri. Untuk menyatukannya, Anda bisa menggunakan lem panas atau menggunakan kawat agar lebih kuat.''',file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run("TOKEN")