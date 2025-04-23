from dataclasses import dataclass
from io import TextIOBase
from PIL import Image, ImageDraw

@dataclass
class ColorMethods:
    @staticmethod
    def rgb_to_tuple(rgb: int):
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return (r, g, b)
    
    @staticmethod
    def hex_to_rgb(hex: str):
        HEX = "0123456789ABCDEF"
        rgb = 0
        for c in hex:
            rgb *= 16
            rgb += HEX.find(c)
        return rgb
    
    @staticmethod
    def tuple_to_hex(r: int, g: int, b: int):
        HEX = "0123456789ABCDEF"
        return HEX[r // 16] + HEX[r % 16] + HEX[g // 16] + HEX[g % 16] + HEX[b // 16] + HEX[b % 16]
    
    @staticmethod
    def tuple_to_rgb(r: int, g: int, b: int):
        return r + g * 256 + b * 256 * 256
    
    @staticmethod
    def rgb_to_hex(rgb: int):
        HEX = "0123456789ABCDEF"
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return HEX[r // 16] + HEX[r % 16] + HEX[g // 16] + HEX[g % 16] + HEX[b // 16] + HEX[b % 16]
    
    @staticmethod
    def hex_to_tuple(hex: str):
        HEX = "0123456789ABCDEF"
        rgb = 0
        for c in hex:
            rgb *= 16
            rgb += HEX.find(c)
        r = rgb % 256
        g = (rgb // 256) % 256
        b = ((rgb // 256) // 256) % 256
        return (r, g, b)

@dataclass
class Table:
    li: list
    x: int
    y: int
    def __init__(self, file: TextIOBase):
        self.li = []
        for counter, line in enumerate(file.readlines()):
            if counter == 0: self.x = len(line.strip().split(","))
            self.li.append(line.strip().split(","))
        else:
            self.y = counter + 1
        return None
    
    def value(self, row: int, col: int):
        return self.li[row][col]
    
    def subset(self, x0: int, xn: int = 0, y0: int = 0, yn: int = 0):
        if not x0 < xn: xn = xn + self.x
        if not y0 < yn: yn = yn + self.y
        return [[x for x in y[x0:xn]] for y in self.li[y0:yn]]
    
    def subsetfloat(self, x0: int, xn: int = 0, y0: int = 0, yn: int = 0):
        if not x0 < xn: xn = xn + self.x
        if not y0 < yn: yn = yn + self.y
        return [[float(x) for x in y[x0:xn]] for y in self.li[y0:yn]]
    
    
    def get(self):
        return self.li

@dataclass
class StarMethods:
    @staticmethod
    def rotate(constellations: Table, starspos: list, index: int):
        if index <= 0: return starspos.copy()
        try:
            R = constellations.subsetfloat(2, 11)[index - 1]
        except IndexError:
            return starspos.copy()
        li = []
        for star in starspos:
            x0 = star[0]
            y0 = star[1]
            z0 = star[2]
            x = x0 * R[0] + y0 * R[1] + z0 * R[2]
            y = x0 * R[3] + y0 * R[4] + z0 * R[5]
            z = x0 * R[6] + y0 * R[7] + z0 * R[8]
            li.append([x, y, z])
        return li

@dataclass
class ImageMethods:
    def createNew(size: int = 1572, rgb: int = 0, format: int = 0):
        '''
        size: length and width
        rgb: background color
        format: 0 = square | 1 = circle
        '''
        r, g, b = ColorMethods.rgb_to_tuple(rgb)
        if format == 0:
            return Image.new("RGB", (size, size), (r, g, b))
        image = Image.new("RGB", (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.ellipse((0, size, 0, size), fill=(r, g, b, 255))
        return image
    
    def pixelSelection(x: int, y: int, size: int, edge: int):
        l = []
        match size:
            case 1:
                l.append((x, y))
            case 2:
                for i in range(x - 1, x + 2):
                    if i < 0: continue
                    if i >= edge: continue
                    for j in range(y - 1, y + 2):
                        if j < 0: continue
                        if j >= edge: continue
                        l.append((i, j))
            case 3:
                for i in range(x - 2, x + 3):
                    if i < 0: continue
                    if i >= edge: continue
                    for j in range(y - 2, y + 3):
                        if j < 0: continue
                        if j >= edge: continue
                        l.append((i, j))
            case 4:
                for i in range(x - 3, x + 4):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 3 or i == x + 3:
                        for j in range(y - 2, y + 3):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 3, y + 4):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case 5:
                for i in range(x - 4, x + 5):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 4 or i == x + 4:
                        for j in range(y - 2, y + 3):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 3 or i == x + 3:
                        for j in range(y - 3, y + 4):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 4, y + 5):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case 6:
                for i in range(x - 5, x + 6):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 5 or i == x + 5:
                        for j in range(y - 3, y + 4):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 4 or i == x + 4:
                        for j in range(y - 4, y + 5):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 5, y + 6):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case 7:
                for i in range(x - 6, x + 7):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 6 or i == x + 6:
                        for j in range(y - 3, y + 4):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 5 or i == x + 5:
                        for j in range(y - 4, y + 5):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 4 or i == x + 4:
                        for j in range(y - 5, y + 6):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 6, y + 7):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case 8:
                for i in range(x - 7, x + 8):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 7 or i == x + 7:
                        for j in range(y - 3, y + 4):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 6 or i == x + 6:
                        for j in range(y - 5, y + 6):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 5 or i == x + 5 or i == x - 4 or i == x + 4:
                        for j in range(y - 6, y + 7):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 7, y + 8):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case 9:
                for i in range(x - 8, x + 9):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 8 or i == x + 8:
                        for j in range(y - 4, y + 5):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 7 or i == x + 7:
                        for j in range(y - 5, y + 6):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 6 or i == x + 6:
                        for j in range(y - 6, y + 7):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 5 or i == x + 5:
                        for j in range(y - 7, y + 8):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 8, y + 9):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
            case _:
                for i in range(x - 9, x + 10):
                    if i < 0: continue
                    if i >= edge: continue
                    if i == x - 9 or i == x + 9:
                        for j in range(y - 4, y + 5):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 8 or i == x + 8:
                        for j in range(y - 6, y + 7):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 7 or i == x + 7:
                        for j in range(y - 7, y + 8):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    elif i == x - 6 or i == x + 6 or i == x - 5 or i == x + 5:
                        for j in range(y - 8, y + 9):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
                    else:
                        for j in range(y - 9, y + 10):
                            if j < 0: continue
                            if j >= edge: continue
                            l.append((i, j))
        return l
    
    def paintPixel(image: Image.Image, x: int, y: int, size: int, color: int, edge: int):
        r, g, b = ColorMethods.rgb_to_tuple(color)
        for pixel in ImageMethods.pixelSelection(x, y, size, edge):
            image.putpixel(pixel, (r, g, b))
        return None



def main():
    foldername = "C:/Users/oleon/Documents/Python/SkyView"
    with open(f"{foldername}/constellation.csv", "r") as ifile: constellations = Table(ifile)
    with open(f"{foldername}/stars.csv", "r") as ifile: stars = Table(ifile)
    constellation = 89
    starspos = StarMethods.rotate(constellations,
                                  stars.subsetfloat(13),
                                  constellation)
    print(constellations.x)
    print(constellations.y)
    print(stars.x)
    print(stars.y)
    # print(len(starspos))
    # print(len(rotation))
    print(starspos[0])
    
    
    return None
if __name__ == "__main__": main()