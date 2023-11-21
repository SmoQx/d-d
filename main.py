

class Characeter_sheet():
    def __init__(self, name, speed, str_, dex_, con_, wis_, int_, cha_, race, clas) -> None:
        self.name: str = name
        self.speed: int = speed
        self.str_: int = str_
        self.dex_: int = dex_
        self.con_: int = con_
        self.wis_: int = wis_
        self.int_: int = int_
        self.cha_: int = cha_
        self.clas: str = clas
        self.race: str = race

    def print_stats(self):
        for args in vars(self).items():
            print(args)

    def stats_modifier(self):
        stat_mod_dictionary = {}
        for stat_name, stat in vars(self).items():
            if stat_name in ["str_", "dex_", "con_", "wis_", "int_", "cha_"]:
                stat_mod = (stat - 10) / 2
                if stat_mod % 1 != 0:
                    stat_mod = stat_mod - 0.5
                stat_mod_dictionary[stat_name] = stat_mod 
        return stat_mod_dictionary

    def skills_modifiers(self, profficient: int=2, profficient_in: list = ["athletics", "acrobatics"]):
        stat_mod_dicttionary = self.stats_modifier()
        
        skills ={
                "athletics": stat_mod_dicttionary["str_"],
                "initiativ": stat_mod_dicttionary["dex_"],
                "acrobatics": stat_mod_dicttionary["dex_"],
                "sleight_of_hand": stat_mod_dicttionary["dex_"],
                "stealth": stat_mod_dicttionary["dex_"],
                "arcana": stat_mod_dicttionary["int_"],
                "history": stat_mod_dicttionary["int_"],
                "investigation": stat_mod_dicttionary["int_"],
                "nature": stat_mod_dicttionary["int_"],
                "religion": stat_mod_dicttionary["int_"],
                "animal handling": stat_mod_dicttionary["wis_"],
                "insight": stat_mod_dicttionary["wis_"],
                "medicine": stat_mod_dicttionary["wis_"],
                "perception": stat_mod_dicttionary["wis_"],
                "survival": stat_mod_dicttionary["wis_"],
                "deception": stat_mod_dicttionary["cha_"],
                "intimidation": stat_mod_dicttionary["cha_"],
                "performance": stat_mod_dicttionary["cha_"],
                "persuasion": stat_mod_dicttionary["cha_"],
                "weapons_dex_": stat_mod_dicttionary["dexteriti"],
                "weapons_str_": stat_mod_dicttionary["strenght"],
                "initiaiv": stat_mod_dicttionary["dex_"],
                }

        for skill in skills:
            if skill in profficient_in:
                skills[skill] = skills[skill] + profficient
        print(skills)
        return skills

    def saving_throw_modifier(self, proficient: int=2, profficient_in: list = []):
        stat_mod_dictionary = self.stats_modifier()
        save_modifiers = {
                         "str__save": stat_mod_dictionary["str_"],
                         "dex_save": stat_mod_dictionary["dex_"],
                         "con_save": stat_mod_dictionary["con_"],
                         "wis_save": stat_mod_dictionary["wis_"],
                         "int_save": stat_mod_dictionary["int_"],
                         "cha_save": stat_mod_dictionary["cha_"],
                         }
        for save in save_modifiers:
            if save in profficient_in:
                save_modifiers[save] = save_modifiers[save] + proficient
        
        return save_modifiers 


def main():
    pass


if __name__ == "__main__":
    new_char = Characeter_sheet(name = "Chriss", speed = 40, str_ = 14, dex_=7, con_=10, wis_=10, int_=10, cha_=10, race="Human", clas="Fighter")
    chriss_skills = new_char.skills_modifiers()
    chriss_skills["athletics"] = 10
    print(chriss_skills)
    print(new_char.saving_throw_modifier(profficient_in=["str__save", "con_save"]))
