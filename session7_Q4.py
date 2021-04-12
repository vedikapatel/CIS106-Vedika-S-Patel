def compavg(game1, game2, game3):
  avg = (game1 + game2 + game3) / 3
    
  return avg

def compavgHanCap(game1, game2, game3, hanCap):
  avgHanCap = (game1 + hanCap + (game2 + hanCap) + (game3 + hanCap)) / 3
    
  return avgHanCap

lastName = input("Enter bowler last name: ")
game1 = float(input("Enter game 1 score: "))
game2 = float(input("Enter game 2 score: "))
game3 = float(input("Enter game 3 score: "))
hanCap = float(input("Enter handicap score: "))
compavg(game1, game2, game3)
avg = compavg(game1, game2, game3)
compavgHanCap(game1, game2, game3, hanCap)
avgHanCap = compavgHanCap(game1, game2, game3, hanCap)
print("Bowler last name: " + lastName)
print("Average score: " , avg)
print("Average score with handicap: " , avgHanCap)