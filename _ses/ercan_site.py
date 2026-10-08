# Sitedeki mini triyaj için Ercan Abi replikleri (oyundaki sesle aynı: edge-tts tr-TR-AhmetNeural, -6% / -8Hz).
# Çalıştır: python -X utf8 _ses/ercan_site.py  -> ses/ercan-*.mp3
import asyncio, os
import edge_tts

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPLIK = {
    "karsilama": "Hoş geldin hocam. Kapıda bir hasta var, nereye alalım?",
    "kirmizi": "Kırmızı alan, aynen hocam. Göğüs ağrısı bekletilmez. EKG'yi on dakikada çekiyorum.",
    "sari": "Sarı mı hocam? Adam terliyor, nabız yüz dört. Kalpse beklerken kaybederiz. Kırmızıya alıyorum.",
    "yesil": "Yeşil mi? Hocam şaka yapıyorsun herhalde. Göğüs ağrısı bu. Kırmızıya alıyorum, sonra konuşuruz.",
}


async def ana():
    os.makedirs(os.path.join(KOK, "ses"), exist_ok=True)
    for ad, metin in REPLIK.items():
        yol = os.path.join(KOK, "ses", "ercan-" + ad + ".mp3")
        await edge_tts.Communicate(metin, "tr-TR-AhmetNeural", rate="-6%", pitch="-8Hz").save(yol)
        print(ad, os.path.getsize(yol) // 1024, "KB")


asyncio.run(ana())
