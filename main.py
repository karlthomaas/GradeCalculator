class Arvutus:
    def __init__(self, tund):
        self.tund = tund
        self.hinded = []

    def get_class(self):
        return self.tund

    def grades(self, *args):
        for arg in args:
            self.hinded.append(arg)

    def get_grades(self):
        return self.hinded

    def average_grade(self):
        return sum(self.hinded) / len(self.hinded)

    def required_average_grade(self, average_grade, reps):
        # 1. Keskmine hinne
        # 2. Hindeid kokku
        # 3. Mitme tööga vaja
        # 4. Hinnete protsent kokku

        varu_hinded = self.hinded.copy()
        varu_hinded2 = self.hinded.copy()
        required_average_grade = average_grade * (len(self.hinded) + reps) - sum(self.hinded)

        if reps == 1:
            if required_average_grade < 100:
                return round(required_average_grade, 1)
            else:
                return f'Ühe tööga, teil ei ole võimalik saada hinnet: {average_grade}'

        # calculates with given reps
        elif required_average_grade / reps < 100:
            # rounds the requireed_average_grade to 1
            return round(required_average_grade / reps, 1)
        else:
            toode_arv = reps
            while reps > 0:
                varu_hinded.append(100)
                varu_hinded2.append(90)
                reps -= 1
            return f'Teil ei ole võimalik saada {average_grade}% {toode_arv} tööga, aga ' \
                   f'kui ei teeksite järgmised {toode_arv} tööd hindele 100, ' \
                   f'saaksite te hindeks: {sum(varu_hinded) / len(varu_hinded)}. ' \
                   f'Tehtes järgmised {toode_arv} tööd hindele 90%, saaksite hindeks:' \
                   f' {sum(varu_hinded2) / len(varu_hinded)}'

eesti_keel = Arvutus('Eesti keel')
eesti_keel.grades(90, 100)

muusika = Arvutus('Muusika')
muusika.grades(80, 95)
print(muusika.required_average_grade(90, 1))