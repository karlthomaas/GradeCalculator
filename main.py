class Arvutus:
    def init(self, tund):
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
        retrun

karlthomas = Arvutus('Matemaatika')
karlthomas.grades(90, 87, 75, 98)
