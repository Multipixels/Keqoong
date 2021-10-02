import random
import loot_constants as lc

#PULLS

def getThreeStarStandardSelection():
  randomSelection = random.randint(0, len(lc.standardThreeStarWeapons)-1)

  return lc.standardThreeStarWeapons[randomSelection]

def getFourStarStandardSelection():

  characterOrBanner = random.randint(0, 1)

  if characterOrBanner == 0:
    randomSelection = random.randint(0, len(lc.standardFourStarWeapons)-1)
    return lc.standardFourStarWeapons[randomSelection]
  else:
    randomSelection = random.randint(0, len(lc.standardFourStarCharacters)-1)
    return lc.standardFourStarCharacters[randomSelection]

def getFiveStarStandardSelection():

  characterOrBanner = random.randint(0, 1)

  if characterOrBanner == 0:
    randomSelection = random.randint(0, len(lc.standardFiveStarWeapons)-1)
    return lc.standardFiveStarWeapons[randomSelection]
  else:
    randomSelection = random.randint(0, len(lc.standardFiveStarCharacters)-1)
    return lc.standardFiveStarCharacters[randomSelection]

#GENERATION

def generateWishes():
  description = ""

  for i in range(10):

    randomSelection = random.randint(1, 1000)

    if 1 <= randomSelection <= 6:
      description += "🌟 " + getFiveStarStandardSelection() + '\n'
    elif 7 <= randomSelection <= 57:
      description += "⭐ " + getFourStarStandardSelection() + '\n'
    elif 58 <= randomSelection <= 1000:
      description += "🔹 " + getThreeStarStandardSelection() + '\n'

  return description







