import os
from PIL import Image
import subprocess

def deliver_image():
	raw = os.listdir("raw")
	if raw == []:
		return False
	f = open("num.txt", "rb")
	num_str = f.read().decode("utf-8")
	num = int(num_str)
	f.close()
	old_name = "raw/" + raw[0]
	image_to_add = Image.open(old_name)
	new_name = str(num + 1) + ".png"
	image_to_add.save(new_name)
	f = open("num.txt", "wb")
	f.write(str(num + 1).encode("utf-8"))
	f.close()
	os.remove("raw/" + raw[0])
	return new_name

def push_to_github():
	subprocess.call(["git", "add", "."])
	subprocess.call(["git", "commit", "-m", "新增一张图片"])
	subprocess.call(["git", "push", "origin", "master"])

if __name__ == "__main__":
	print(deliver_image())
