def flood_fill_utill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    prevC = image[sr][sc]
    if prevC == color : return image
    floodFillUtil(image,sr,sc,prevC,color)
    return image

def floodFillUtil(image, sr, sc, pC, nC) :
    if (sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or
            image[sr][sc] != pC or image[sr][sc] == nC
        ):
        return
    image[sr][sc] = nC
    floodFillUtil(image, sr+1, sc, pC, nC)
    floodFillUtil(image, sr-1, sc, pC, nC)
    floodFillUtil(image, sr, sc+1, pC, nC)
    floodFillUtil(image, sr, sc-1, pC, nC)


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
flood_fill_utill(image, sr, sc, color)
print(image)
