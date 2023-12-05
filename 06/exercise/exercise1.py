from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

preprocess_1 = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    transforms.Resize((224, 224), antialias=True)
])

preprocess_2 = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, hue=0.2)
])

preprocess_3 = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomRotation(degrees=90), #-90から90度の範囲
    transforms.CenterCrop(size=(224, 224))
])
#サンプル画像を読み込んで前処理を適応
image_path = "./exercise_data/dog_img.png"
image = Image.open(image_path)
processed_image = preprocess_3(image)
#テンソルに変換した画像を表示
plt.imshow(processed_image.permute(1, 2, 0)) #チャンネル次元を最後に移動
plt.show()