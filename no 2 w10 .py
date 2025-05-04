from abc import ABC, abstractmethod

# Kelas abstrak Section
class Section(ABC):
    @abstractmethod
    def describe(self):
        pass

# Kelas-kelas konkret untuk masing-masing section
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

# Kelas abstrak Profile
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

# Kelas konkret untuk profil LinkedIn
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

# Kelas konkret untuk profil Facebook
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

# Program utama
profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook]: ")
profile = eval(profile_type.lower())()
print(f"Profil {type(profile).__name__} sedang dibuat...")
print("Profil mempunyai Section:")
for section in profile.getSections():
    print(section)
