import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

atiklar = {

# ORGANİK
"muz kabuğu": {"time": "2-5 hafta", "soil": "1/10", "note": "Doğada hızlıca ayrışır, kompost için idealdir."},
"elma kabuğu": {"time": "2 ay", "soil": "1/10", "note": "Organik, toprağa faydalıdır."},
"portakal kabuğu": {"time": "6 ay", "soil": "1/10", "note": "Asidik içeriği nedeniyle daha yavaş ayrışır."},
"limon kabuğu": {"time": "6 ay", "soil": "1/10", "note": "Asidik yapısı var."},
"karpuz kabuğu": {"time": "2-4 hafta", "soil": "1/10", "note": "Su içeriği yüksek, hızlı ayrışır."},
"domates": {"time": "2 hafta", "soil": "1/10", "note": "Çok hızlı ayrışır."},
"salatalık": {"time": "2 hafta", "soil": "1/10", "note": "Su içeriği yüksek."},
"marul": {"time": "1-2 hafta", "soil": "1/10", "note": "Çok hızlı ayrışır."},
"ekmek": {"time": "2-3 hafta", "soil": "1/10", "note": "Küflenme ile hızlı ayrışır."},
"pirinç": {"time": "1-2 hafta", "soil": "1/10", "note": "Hızlı ayrışan organik madde."},
"makarna": {"time": "1-2 hafta", "soil": "1/10", "note": "Nemi çekerek ayrışır."},
"patates": {"time": "2-3 hafta", "soil": "1/10", "note": "Çürüyerek ayrışır."},
"soğan": {"time": "2 hafta", "soil": "1/10", "note": "Hızlı ayrışır."},
"çay posası": {"time": "1-2 hafta", "soil": "1/10", "note": "Kompost için mükemmel."},
"kahve telvesi": {"time": "2-4 hafta", "soil": "1/10", "note": "Toprağa azot katar."},
"yumurta kabuğu": {"time": "1 yıl", "soil": "1/10", "note": "Kalsiyum içerir, toprağa faydalı."},

# KAĞIT
"gazete": {"time": "6 hafta", "soil": "2/10", "note": "Mürekkep nedeniyle biraz zararlı olabilir."},
"kağıt": {"time": "2-6 hafta", "soil": "2/10", "note": "Geri dönüştürülebilir."},
"defter": {"time": "2-5 ay", "soil": "2/10", "note": "Tel veya tutkal içerebilir."},
"karton": {"time": "2 ay", "soil": "2/10", "note": "Geri dönüştürülebilir."},
"kağıt bardak": {"time": "5 yıl", "soil": "4/10", "note": "İç yüzeyi plastik kaplıdır."},
"kağıt tabak": {"time": "5 yıl", "soil": "4/10", "note": "Plastik kaplama içerir."},
"kağıt mendil": {"time": "2-4 hafta", "soil": "2/10", "note": "Hızlı ayrışır."},
"peçete": {"time": "2-4 hafta", "soil": "2/10", "note": "Organik atıklarla kompostlanabilir."},
"kitap": {"time": "2-5 ay", "soil": "2/10", "note": "Tutkal ve mürekkep içerir."},
"kartvizit": {"time": "2 ay", "soil": "2/10", "note": "Parlak olanlar plastik kaplı olabilir."},
"zarf": {"time": "2 ay", "soil": "2/10", "note": "Tutkal içerir."},

# PLASTİK
"plastik poşet": {"time": "10-20 yıl", "soil": "8/10", "note": "Mikroplastik bırakır, hayvanlar için tehlikeli."},
"plastik şişe": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Mikroplastik bırakır."},
"pet şişe": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Geri dönüştürülmeli, mikroplastik oluşturur."},
"plastik kap": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Mikroplastik bırakır."},
"plastik tabak": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Tek kullanımlık, çok zararlı."},
"plastik bardak": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Mikroplastik bırakır."},
"plastik çatal": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Tek kullanımlık plastik."},
"plastik kaşık": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Tek kullanımlık plastik."},
"plastik pipet": {"time": "≈ 200 yıl", "soil": "8/10", "note": "Deniz canlıları için tehlikeli."},
"plastik oyuncak": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Zehirli kimyasallar içerebilir."},
"plastik kapak": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Mikroplastik bırakır."},
"plastik diş fırçası": {"time": "≈ 500 yıl", "soil": "9/10", "note": "Bambu alternatifi önerilir."},
"plastik torba": {"time": "≈ 20 yıl", "soil": "7/10", "note": "Hafif plastik, kolayca dağılır."},
"plastik ambalaj": {"time": "≈ 400 yıl", "soil": "9/10", "note": "Mikroplastik bırakır."},
"plastik balon": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Hayvanlar için tehlikeli."},

# CAM
"cam şişe": {"time": "≈ 4000 yıl", "soil": "3/10", "note": "Geri dönüştürülebilir, kimyasal bırakmaz."},
"cam bardak": {"time": "≈ 4000 yıl", "soil": "3/10", "note": "Geri dönüştürülebilir."},
"cam kavanoz": {"time": "≈ 4000 yıl", "soil": "3/10", "note": "Geri dönüştürülebilir."},
"cam tabak": {"time": "≈ 4000 yıl", "soil": "3/10", "note": "Geri dönüştürülebilir."},
"cam pencere": {"time": "≈ 4000 yıl", "soil": "3/10", "note": "Mineral yapısı doğaya zararsız ama uzun sürer."},

# METAL
"alüminyum kutu": {"time": "≈ 200 yıl", "soil": "5/10", "note": "Geri dönüştürülmeli, enerji tasarrufu sağlar."},
"teneke kutu": {"time": "≈ 50 yıl", "soil": "5/10", "note": "Paslanarak ayrışır."},
"konserve kutusu": {"time": "≈ 50 yıl", "soil": "5/10", "note": "Geri dönüştürülebilir."},
"metal kapak": {"time": "≈ 50 yıl", "soil": "5/10", "note": "Geri dönüştürülebilir."},
"çivi": {"time": "≈ 100 yıl", "soil": "4/10", "note": "Demir, paslanarak ayrışır."},
"metal tel": {"time": "≈ 100 yıl", "soil": "4/10", "note": "Paslanır."},
"metal kaşık": {"time": "≈ 100 yıl", "soil": "4/10", "note": "Geri dönüştürülebilir."},

# TEKSTİL
"pamuk tişört": {"time": "6 ay", "soil": "2/10", "note": "Doğal elyaf, hızlı ayrışır."},
"yün kazak": {"time": "1-5 yıl", "soil": "2/10", "note": "Doğal elyaf, toprağa faydalı."},
"naylon çorap": {"time": "30-40 yıl", "soil": "7/10", "note": "Sentetik, mikroplastik bırakır."},
"polyester kıyafet": {"time": "≈ 200 yıl", "soil": "8/10", "note": "Sentetik, mikroplastik bırakır."},
"kot pantolon": {"time": "1 yıl", "soil": "3/10", "note": "Pamuk bazlı ama boyalar zararlı olabilir."},
"bez çanta": {"time": "6 ay", "soil": "2/10", "note": "Doğal, geri dönüştürülebilir."},

# ELEKTRONİK
"telefon": {"time": "≈ 1000 yıl", "soil": "10/10", "note": "Zehirli metaller içerir, e-atık olarak geri dönüştürülmeli."},
"bilgisayar": {"time": "≈ 1000 yıl", "soil": "10/10", "note": "Ağır metaller ve zehirli maddeler içerir."},
"tablet": {"time": "≈ 1000 yıl", "soil": "10/10", "note": "Zehirli metaller içerir."},
"kulaklık": {"time": "≈ 100 yıl", "soil": "7/10", "note": "Plastik ve metal karışımı."},
"klavye": {"time": "≈ 100 yıl", "soil": "7/10", "note": "Plastik ve elektronik parçalar."},
"mouse": {"time": "≈ 100 yıl", "soil": "7/10", "note": "Plastik ve elektronik bileşenler."},

# PİL VE BATARYA
"kalem pil": {"time": "≈ 100 yıl", "soil": "10/10", "note": "Ağır metaller içerir, toprak ve suyu kirletir."},
"şarjlı pil": {"time": "≈ 500 yıl", "soil": "10/10", "note": "Lityum ve diğer zehirli maddeler içerir."},
"telefon bataryası": {"time": "≈ 500 yıl", "soil": "10/10", "note": "Lityum-iyon, son derece zehirli."},
"laptop bataryası": {"time": "≈ 500 yıl", "soil": "10/10", "note": "Ağır metaller içerir, mutlaka geri dönüştürülmeli."},

# SİGARA
"sigara izmariti": {"time": "1-5 yıl", "soil": "8/10", "note": "Zehirli kimyasallar ve mikroplastik içerir."},
"sigara paketi": {"time": "5 yıl", "soil": "5/10", "note": "Plastik kaplama içerir."},

# DİĞER
"strafor": {"time": "≈ 500 yıl", "soil": "9/10", "note": "Mikroplastik bırakır, geri dönüşümü zor."},
"sakız": {"time": "5 yıl", "soil": "6/10", "note": "Sentetik kauçuk içerir."},
"bebek bezi": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Plastik ve kimyasallar içerir."},
"ıslak mendil": {"time": "≈ 100 yıl", "soil": "7/10", "note": "Plastik elyaflar içerir, tuvalete atılmamalı."},
"diş ipi": {"time": "30 yıl", "soil": "6/10", "note": "Naylon bazlı."},
"pipet": {"time": "≈ 200 yıl", "soil": "8/10", "note": "Tek kullanımlık plastik."},
"maske": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Plastik elyaf içerir, mikroplastik bırakır."},
"lastik": {"time": "≈ 80 yıl", "soil": "7/10", "note": "Zehirli kimyasallar içerir."},
"araba lastiği": {"time": "≈ 80 yıl", "soil": "7/10", "note": "Ağır, zehirli kimyasallar içerir."},
"deri ayakkabı": {"time": "25-40 yıl", "soil": "5/10", "note": "Tabaklamada kullanılan kimyasallar zararlı."},
"ahşap": {"time": "10-15 yıl", "soil": "2/10", "note": "Doğal, toprağa faydalı."},
"tahta": {"time": "10 yıl", "soil": "2/10", "note": "Doğal malzeme."},
"tahta kaşık": {"time": "1-3 yıl", "soil": "1/10", "note": "Hızlı ayrışır, çevre dostu."},
"tahta çubuk": {"time": "1 yıl", "soil": "1/10", "note": "Hızlı ayrışır."},
"balon": {"time": "≈ 450 yıl", "soil": "9/10", "note": "Lateks veya plastik, hayvanlar için tehlikeli."},
"cd": {"time": "≈ 1 milyon yıl", "soil": "10/10", "note": "Polikarbonat plastik, neredeyse hiç ayrışmaz."},
"dvd": {"time": "≈ 1 milyon yıl", "soil": "10/10", "note": "Polikarbonat plastik, neredeyse hiç ayrışmaz."},
"lego": {"time": "≈ 1300 yıl", "soil": "9/10", "note": "ABS plastik, çok uzun süre kalır."}

}

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
async def atik(ctx, *, madde):
    madde = madde.lower()

    if madde in atiklar:
        bilgi = atiklar[madde]
        
        embed = discord.Embed(
            title=f"🌍 {madde.upper()} - Geri Dönüşüm Bilgisi",
            color=discord.Color.green()
        )
        embed.add_field(name="⏱️ Ayrışma Süresi", value=bilgi["time"], inline=False)
        embed.add_field(name="🌱 Toprak Hasarı", value=bilgi["soil"], inline=False)
        embed.add_field(name="📝 Not", value=bilgi["note"], inline=False)
        embed.set_footer(text="Çevreyi korumak hepimizin sorumluluğu! ♻️")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu atık hakkında bilgi bulunamadı.")

bot.run("Token Here")
