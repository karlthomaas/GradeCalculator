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
        required_average_grade = average_grade * (len(self.hinded) + reps) - sum(self.hinded)

        if reps == 1:
            if required_average_grade < 100:
                return round(required_average_grade, 1)
            else:
                return f'Ühe tööga, teil ei ole võimalik saada hinnet {average_grade}'

        # calculates with given reps
        elif required_average_grade / reps < 100:
            # rounds the requireed_average_grade to 1
            return round(required_average_grade / reps, 1)
        else:
            grade = average_grade
            # loops until, it get's the lowest average grade possible
            while required_average_grade > 100:
                grade -= 1
                print(grade)
                required_average_grade = grade * (len(self.hinded) + reps) - sum(self.hinded)
            return f'Kõige madalam lõpuhinne, mida te saaksite nende hinnetega on: {grade}'

        # if required_average_grade > 100 and reps == 1:
        #     print(required_average_grade)
        #     return 'Nope'
        # elif required_average_grade > 100 and reps == 2:
        #     required_average_grade = required_average_grade / 2
        #     if required_average_grade > 100:
        #         return 'Nope'
        #     else:
        #         return required_average_grade
        # else:
        #     return required_average_grade


tund1 = Arvutus('Vene keel')
# 90
tund1.grades(99, 80, 83, 95)
# print(tund1.average_grade())
# print(tund1.required_average_grade(90, 1))

tund2 = Arvutus('Muusika')
tund2.grades(80, 95, 60)
print(tund2.required_average_grade(87, 2))