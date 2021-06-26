import img2pdf
import os

dirname = "path to img dict"
imgs = []
for fname in os.listdir(dirname):
	if not fname.endswith(".jpg"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open("path to save pdf/pic.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))