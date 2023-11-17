

class Characeter_sheet():
    def __init__(self, name, speed, strenght, dexteriti, constitution, wisdom, inteligenc, charisma, race, clas) -> None:
        self.name: str = name
        self.speed: int = speed
        self.strenght: int = strenght
        self.dexteriti: int = dexteriti
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.inteligenc: int = inteligenc
        self.charisma: int = charisma
        self.clas: str = clas
        self.race: str = race

    def print_stats(self):
        for args in vars(self).items():
            print(args)

    def stats_modifier(self):
        stat_mod_dictionary = {}
        for stat_name, stat in vars(self).items():
            if stat_name in ["strenght", "dexteriti", "constitution", "wisdom", "inteligenc", "charisma"]:
                stat_mod = (stat - 10) / 2
                if stat_mod % 1 != 0:
                    stat_mod = stat_mod - 0.5
                stat_mod_dictionary[stat_name] = stat_mod 
        return stat_mod_dictionary

    def skills_modifiers(self, profficient: int=2, profficient_in: list = ["athletics", "acrobatics"]):
        stat_mod_dicttionary = self.stats_modifier()
        
        skills ={
                "athletics": stat_mod_dicttionary["strenght"],
                "initiativ": stat_mod_dicttionary["dexteriti"],
                "acrobatics": stat_mod_dicttionary["dexteriti"],
                "sleight_of_hand": stat_mod_dicttionary["dexteriti"],
                "stealth": stat_mod_dicttionary["dexteriti"],
                "arcana": stat_mod_dicttionary["inteligenc"],
                "history": stat_mod_dicttionary["inteligenc"],
                "investigation": stat_mod_dicttionary["inteligenc"],
                "nature": stat_mod_dicttionary["inteligenc"],
                "religion": stat_mod_dicttionary["inteligenc"],
                "animal handling": stat_mod_dicttionary["wisdom"],
                "insight": stat_mod_dicttionary["wisdom"],
                "medicine": stat_mod_dicttionary["wisdom"],
                "perception": stat_mod_dicttionary["wisdom"],
                "survival": stat_mod_dicttionary["wisdom"],
                "deception": stat_mod_dicttionary["charisma"],
                "intimidation": stat_mod_dicttionary["charisma"],
                "performance": stat_mod_dicttionary["charisma"],
                "persuasion": stat_mod_dicttionary["charisma"],
                "weapons_dexteriti": stat_mod_dicttionary["dexteriti"],
                "weapons_strenght": stat_mod_dicttionary["strenght"],
                "initiaiv": stat_mod_dicttionary["dexteriti"],
                }

        for skill in skills:
            if skill in profficient_in:
                skills[skill] = skills[skill] + profficient
        print(skills)
        return skills

    def saving_throw_modifier(self, proficient: int=2, profficient_in: list = []):
        stat_mod_dictionary = self.stats_modifier()
        save_modifiers = {
                         "str_save": stat_mod_dictionary["strenght"],
                         "dex_save": stat_mod_dictionary["dexteriti"],
                         "con_save": stat_mod_dictionary["constitution"],
                         "wis_save": stat_mod_dictionary["wisdom"],
                         "int_save": stat_mod_dictionary["inteligenc"],
                         "cha_save": stat_mod_dictionary["charisma"],
                         }
        for save in save_modifiers:
            if save in profficient_in:
                save_modifiers[save] = save_modifiers[save] + proficient
        
        return save_modifiers 


def main():
    pass


if __name__ == "__main__":
    new_char = Characeter_sheet(name = "Chriss", speed = 40, strenght = 14, dexteriti=7, constitution=10, wisdom=10, inteligenc=10, charisma=10, race="Human", clas="Fighter")
    chriss_skills = new_char.skills_modifiers()
    chriss_skills["athletics"] = 10
    print(chriss_skills)
    print(new_char.saving_throw_modifier(profficient_in=["str_save", "con_save"]))
