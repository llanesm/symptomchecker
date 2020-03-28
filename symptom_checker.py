class Illness:

    def __init__(self):
        """Initializes base scores to 0"""
        self._flu_score = 0
        self._cold_score = 0
        self._corona_score = 0
        self._allergy_score = 0

    def questionnaire(self):
        """Goes through symptom checklist to ask user about individual symptoms"""
        # ask user about each potential symptom and accumulate scores for each ailment
        self.fever()
        self.headache()
        self.aches_pains()
        self.fatigue()
        self.exhaustion()
        self.stuffy()
        self.sneezing()
        self.sore_throat()
        self.cough()
        self.short_breath()
        self.runny_nose()
        self.diarrhea()

    def fever(self):
        """Asks user if they have a fever, then adds to
        scores of ailments that have fever as a symptom"""
        fever = input("Do you have a fever (temp over 100), yes or no? ")
        fever.lower()
        if fever != "yes" and fever != "no":
            print("Please answer yes or no.")
            self.fever()
        if fever == "yes":
            self._flu_score += 10       # 10 added for common symptom
            self._corona_score += 10
            self._cold_score += 1       # 1 added for rare symptom

    def headache(self):
        """Asks user if they have a headache, then adds to
        scores of ailments that have headache as a symptom"""
        headache = input("Do you have a headache, yes or no? ")
        headache.lower()
        if headache != "yes" and headache != "no":  # validate
            print("Please answer yes or no.")
            self.headache()
        if headache == "yes":
            self._corona_score += 5     # 5 added for sometimes symptom
            self._cold_score += 1
            self._flu_score += 10
            self._allergy_score += 5

    def aches_pains(self):
        """Asks user if they have aches or pains, then adds to
        scores of ailments that have aches and pains as a symptom"""
        aches_pains = input("Do you have generalized aches or pains, yes or no? ")
        aches_pains.lower()
        if aches_pains != "yes" and aches_pains != "no":
            print("Please answer yes or no.")
            self.aches_pains()
        if aches_pains == "yes":
            self._corona_score += 5
            self._cold_score += 1
            self._flu_score += 10

    def fatigue(self):
        """Asks user if they have fatigue or weakness, then adds to
        scores of ailments that have fatigue and weakness as a symptom"""
        fatigue = input("Are you experiencing fatigue or weakness, yes or no? ")
        fatigue.lower()
        if fatigue != "yes" and fatigue != "no":
            print("Please answer yes or no.")
            self.fatigue()
        if fatigue == "yes":
            self._corona_score += 5
            self._cold_score += 1
            self._flu_score += 10
            self._allergy_score += 5

    def exhaustion(self):
        """Asks user if they've had exhaustion, then adds to
        scores of ailments that have extreme exhaustion as a symptom"""
        exhaustion = input("Are you feeling especially exhausted, yes or no? ")
        exhaustion.lower()
        if exhaustion != "yes" and exhaustion != "no":
            print("Please answer yes or no.")
            self.exhaustion()
        if exhaustion == "yes":
            self._corona_score += 5
            self._flu_score += 10

    def stuffy(self):
        """Asks user if they have a stuff nose, then adds to
        scores of ailments that have stuffy as a symptom"""
        stuffy = input("Do you have a stuffy nose, yes or no? ")
        stuffy.lower()
        if stuffy != "yes" and stuffy != "no":
            print("Please answer yes or no.")
            self.stuffy()
        if stuffy == "yes":
            self._corona_score += 1
            self._cold_score += 10
            self._flu_score += 5
            self._allergy_score += 10

    def sneezing(self):
        """Asks user if they've been sneezing, then adds to
        scores of ailments that have sneezing as a symptom"""
        sneezing = input("Have you been sneezing, yes or no? ")
        sneezing.lower()
        if sneezing != "yes" and sneezing != "no":
            print("Please answer yes or no.")
            self.sneezing()
        if sneezing == "yes":
            self._corona_score += 1
            self._cold_score += 10
            self._flu_score += 10
            self._allergy_score += 10

    def sore_throat(self):
        """Asks user if they have a sore throat, then adds to
        scores of ailments that have sore throat as a symptom"""
        sore = input("Do you have a sore throat, yes or no? ")
        sore.lower()
        if sore != "yes" and sore != "no":
            print("Please answer yes or no.")
            self.sore_throat()
        if sore == "yes":
            self._corona_score += 1
            self._cold_score += 10
            self._flu_score += 10

    def cough(self):
        """Asks user if they have a cough, then adds to
        scores of ailments that have cough as a symptom"""
        cough = input("Do you have a cough, yes or no? ")
        cough.lower()
        if cough != "yes" and cough != "no":
            print("Please answer yes or no.")
            self.cough()
        if cough == "yes":
            self._corona_score += 10
            self._flu_score += 10
            self._cold_score += 10
            self._allergy_score += 5

    def short_breath(self):
        """Asks user if they've had shortness of breath, then adds to
        scores of ailments that have shortness of breath as a symptom"""
        breath = input("Are you experiencing shortness of breath, yes or no? ")
        breath.lower()
        if breath != "yes" and breath != "no":
            print("Please answer yes or no.")
            self.short_breath()
        if breath == "yes":
            self._corona_score += 10
            self._flu_score += 1
            self._cold_score += 1
            self._allergy_score += 10

    def runny_nose(self):
        """Asks user if they have a runny nose, then adds to
        scores of ailments that have runny nose as a symptom"""
        runny_nose = input("Do you have a runny nose, yes or no? ")
        runny_nose.lower()
        if runny_nose != "yes" and runny_nose != "no":
            print("Please answer yes or no.")
            self.runny_nose()
        if runny_nose == "yes":
            self._corona_score += 1
            self._cold_score += 10
            self._flu_score += 5
            self._allergy_score += 10

    def diarrhea(self):
        """Asks user if they've been having diarrhea, then adds to
        scores of ailments that have diarrhea as a symptom"""
        diarrhea = input("Have you been having diarrhea, yes or no? ")
        diarrhea.lower()
        if diarrhea != "yes" and diarrhea != "no":
            print("Please answer yes or no.")
            self.diarrhea()
        if diarrhea == "yes":
            self._corona_score += 5
            self._flu_score += 5