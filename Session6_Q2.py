def compavg (hits, bats):
  avg = float(hits) / float(bats)

  return avg

lastName = input("Enter last name: ")
hits = float(input("Enter hits: ")) 
bats = float(input("Enter bats: ")) 

avg = compavg(hits,bats)

print("Last Name: ", lastName) 
print("Batting average: ", avg)