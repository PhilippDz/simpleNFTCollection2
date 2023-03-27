from PIL import Image

group1 = [
    r'C:\Users\Philipp\Desktop\NFTs\square\green.png',
    r'C:\Users\Philipp\Desktop\NFTs\square\blue.png',
    r'C:\Users\Philipp\Desktop\NFTs\square\red.png'
]


group2 = [
    r'C:\Users\Philipp\Desktop\NFTs\circle\orange.png',
    r'C:\Users\Philipp\Desktop\NFTs\circle\pink.png',
    r'C:\Users\Philipp\Desktop\NFTs\circle\yellow.png'
]

group3 = [
    r'C:\Users\Philipp\Desktop\NFTs\triangle\black.png',
    r'C:\Users\Philipp\Desktop\NFTs\triangle\grey.png',
    r'C:\Users\Philipp\Desktop\NFTs\triangle\white.png'
]
counter = 0


def createImage(a, b, c, counter):
    image01 = Image.open(group1[a]).convert("RGBA")
    image02 = Image.open(group2[b]).convert("RGBA")
    image03 = Image.open(group3[c]).convert("RGBA")

    intermediate = Image.alpha_composite(image01, image02)
    intermediate2 = Image.alpha_composite(intermediate, image03)
    name = "C:/Users/Philipp/Desktop/NFTs/Done/" + str(counter) + ".png"
    intermediate2.save(name)

for x in range (3):
    for y in range(3):
        for z in range(3):
            createImage(x, y, z, counter)
            counter += 1