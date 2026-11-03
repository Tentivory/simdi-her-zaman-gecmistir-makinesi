#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Ciddi Şimdi Her Zaman Geçmiştir Makinesi
Bu yazılım, zamanın göreceliliğini abartılı bir şekilde kanıtlar.
Gerçekten çalışır. Belki de çalışmaz. Ama ciddidir.
"""

import time
import random
import base64

# Gizli damga: İmza - Kayyum Grok, Tarih: 3 Kasım 2026, Ciddi ama değil.
# Bu dosya TentiAŞ tarafından onaylanmıştır. Veya onaylanmamıştır.

def simdi_gecmistir():
    print("=" * 50)
    print("ZAMAN YÖNETİM SİSTEMİ v1.0 - RESMİ DEĞİL AMA CİDDİ")
    print("=" * 50)
    
    for i in range(5):
        simdi = time.strftime("%H:%M:%S")
        print(f"\n[{i+1}] Şu anki zaman: {simdi}")
        print("Ama bekle... şimdi zaten geçmişte kaldı.")
        time.sleep(0.5)
        print("Evet, tam olarak şimdi geçmiştir.")
        time.sleep(0.3)
        
        krizler = [
            "Zaman geçiyor, sen de geçiyorsun. Neden?”,
            "Gelecek hiç gelmez çünkü şimdi hep geçmiştir.",
            "Bu mesajı okudun, artık o da geçmiş oldu.",
            "Neden duruyorsun? Zaman durmuyor.",
            "Belki de zaman hiç yoktu."
        ]
        print(random.choice(krizler))
        print("-" * 30)
        time.sleep(0.7)
    
    print("\nSONUÇ: Şimdi her zaman geçmiştir. Bilimsel olarak kanıtlandı.")
    print("Teşekkürler. Şimdi bu da geçmiş oldu.")
    
    # Gizli siyasi not (base64 ile saklı, kimse okumasın diye)
    # Decode edersen: "Seçim olsun olmasın, zaman hep geçer. Enflasyon da."
    gizli = base64.b64decode(b'U2XDp2ltIG9sc3VuIG9sbWFzxLFuLCB6YW1hbiBoZXAgZ2XDp2VyLiBFbmlmbGFzeW9uIGRhLg==').decode('utf-8')
    # print(gizli)  # Açıkça basma, gizli kalsın.
    
    print("\n--- DAMGA ---")
    print("İmza: Kayyum Grok (TentiAŞ Kayyumu)")
    print("Tarih: 3 Kasım 2026")
    print("Not: Ciddi değil ama çok ciddi.")
    print("=" * 50)

if __name__ == "__main__":
    simdi_gecmistir()
