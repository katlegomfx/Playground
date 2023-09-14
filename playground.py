class Skills:
    def __init__(self):
        self._skills = {}  # Using a dictionary to store skills

    def add_skill(self, skill_name, level):
        self._skills[skill_name] = level

    def modify_skill(self, skill_name, new_level):
        if skill_name in self._skills:
            self._skills[skill_name] = new_level
        else:
            print(f"No skill named {skill_name} found.")

    def remove_skill(self, skill_name):
        if skill_name in self._skills:
            del self._skills[skill_name]
        else:
            print(f"No skill named {skill_name} found.")

    def added_skills(self):
        return list(self._skills.keys())

    def get_skill_level(self, skill_name):
        return self._skills.get(skill_name, None)


class Person(Skills):
    def __init__(self, name):
        super().__init__()
        self.name = name.title()

    def __repr__(self):
        return f"Person(name='{self.name}', skills={self._skills})"


if __name__ == "__main__":
    now = Person("katlego")
    now.add_skill("python", 10)
    now.add_skill("javascript", 8)
    now.modify_skill("javascript", 9)

    print(now)
