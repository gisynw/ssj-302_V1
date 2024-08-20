class PartyAnimal:
  x = 0
  id = 0

  def __init__(self) -> None:
      PartyAnimal.id += 1
  def party(self) :
    self.x = self.x + 1
    print("So far",self.x)

an = PartyAnimal()
bn = PartyAnimal()

an.party()
an.party()
an.party()

print(PartyAnimal.x)
print(PartyAnimal.id)