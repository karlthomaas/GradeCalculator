class Arvutus:
    def __init__(self, tund):
        self.tund = tund
        self.koik_hinded = []

    def get_klass(self):
        return self.tund

    def hinded(self, *args):
        for arg in args:
            self.koik_hinded.append(arg)

    def get_hinded(self):
        return self.koik_hinded

    def hinnete_keskmine(self):
        return sum(self.koik_hinded) / len(self.koik_hinded)

    def lopphinde_eesmark(self, lopphinne, toode_arv):
        # 1. Keskmine hinne
        # 2. Hindeid kokku
        # 3. Mitme tööga vaja
        # 4. Hinnete protsent kokku

        varu_hinded = self.koik_hinded.copy()
        varu_hinded2 = self.koik_hinded.copy()
        noutav_protsent = lopphinne * (len(self.koik_hinded) + toode_arv) - sum(self.koik_hinded)

        if toode_arv == 1:
            if noutav_protsent < 100:
                return f'Kui te sooritate järgmise töö hindele: {round(noutav_protsent, 1)}%, siis ' \
                       f'te saate kursuse koondhindeks {lopphinne}%.'
            else:

                return f'Teil ei ole võimalik saada {lopphinne}% {toode_arv} tööga, aga ' \
                f'kui ei teeksite järgmise {toode_arv} töö hindele 100%, ' \
                f'saaksite te kursuse koondhindeks: {sum(varu_hinded) / len(varu_hinded)}%. ' \
                f'Tehes järgmised {toode_arv} töö hindele 90%, saaksite kursuse koondhindeks:' \
                f' {sum(varu_hinded2) / len(varu_hinded)}%'

        # calculates with given reps
        elif noutav_protsent / toode_arv < 100:
            # rounds the requireed_average_grade to 1
            return round(noutav_protsent / toode_arv, 1)
        else:
            toode_arv2 = toode_arv
            while toode_arv > 0:
                varu_hinded.append(100)
                varu_hinded2.append(90)
                toode_arv -= 1
            return f'Teil ei ole võimalik saada {lopphinne}% {toode_arv2} tööga, aga ' \
                   f'kui ei teeksite järgmised {toode_arv2} tööd hindele 100%, ' \
                   f'saaksite te kursuse koondhindeks: {sum(varu_hinded) / len(varu_hinded)}%. ' \
                   f'Tehes järgmised {toode_arv2} tööd hindele 90%, saaksite kursuse koondhindeks:' \
                   f' {sum(varu_hinded2) / len(varu_hinded)}%'

eesti_keel = Arvutus('Eesti keel')
eesti_keel.hinded(90, 100)

muusika = Arvutus('Muusika')
muusika.hinded(80, 95)
print(muusika.lopphinde_eesmark(100, 2))