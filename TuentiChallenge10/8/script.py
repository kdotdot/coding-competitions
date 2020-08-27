from PIL import Image

im = Image.open("img.png")
out = Image.new('RGB', im.size, 0xffffff)

val = {
    255:255,
    254:180,
    253:90,
    252:0
}

width, height = im.size
for x in range(width):
    for y in range(height):
        r,g,b,a = im.getpixel((x,y))
        if(a!=255):
            print(f'r{r} g{g} b{b} a{a}')
        #if b < g and b < r or r==g==b:
        out.putpixel((x,y), (val[r],val[g],val[b],a))

out.save('bar.png')
