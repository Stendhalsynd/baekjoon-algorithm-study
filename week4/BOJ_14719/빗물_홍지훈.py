def trapRainWater(rainWater, area):
    compare = 0
    tempSum = 0
    for height in area:
      if height != 0 and compare <= height:
        compare = height
        rainWater += tempSum
        tempSum = 0
        continue
      if height < compare:
        tempSum += compare - height
    return rainWater

def divideArea(heights):
    highest = 0
    hightestIndex = 0

    for idx, val in enumerate(heights):
      if val > highest:
        highest = val
        hightestIndex = idx

    frontArea = heights[:hightestIndex + 1]
    backArea = heights[hightestIndex:][::-1]
    return frontArea,backArea

def getTotalRainWater(trapRainWater, divideArea, heights, rainWater):
    frontArea, backArea = divideArea(heights)

    rainWater = trapRainWater(rainWater, frontArea)
    rainWater = trapRainWater(rainWater, backArea)
    return rainWater

H, W = input().split()
heights = list(map(int, input().split()))

rainWater = 0
rainWater = getTotalRainWater(trapRainWater, divideArea, heights, rainWater)

print(rainWater)
