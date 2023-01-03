from rembg import remove
from PIL import Image
input_path = 'zzz.jpg' #original file name
output_path = 'zzz.png' #new file with background removed
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

