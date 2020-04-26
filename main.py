from PIL import Image

background = Image.open('images/1.png')
foreground = Image.open('images/2.png')
Bx, By = background.size
Fx, Fy = foreground.size

print(background.size)
print(foreground.size)
final1 = Image.new("RGBA", background.size)
final1.paste(background, (0, 0), background)
final1.paste(foreground, (int((Bx-Fx)/2), int((By-Fy)/2)), foreground)
final1.show()
