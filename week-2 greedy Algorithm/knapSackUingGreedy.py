#knapsack using greedy


class Item:
  def __init__(self,value,weight):
    self.value=value
    self.weight=weight
    
def knapSack(W,arr):
  arr.sort(key=lambda x:(x.value/x.weight), reverse=True)
  finalValue=0.0
  for item in arr:
    if item.weight<= W:
      W-=item.weight
      finalValue+=item.value
    else:
      finalValue+=item.value*(W/item.weight)
      break
  return finalValue


W=50
arr=[Item(60,10),Item(100,20),Item(120,30)]
maxValue=knapSack(W,arr)
print(maxValue)