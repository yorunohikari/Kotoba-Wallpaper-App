import ctypes

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    if not result:
        raise ctypes.WinError()

if __name__ == "__main__":
    image_path = "C:/Users/ACER/Documents/vocab-wallpaper/backgrounds/japstudy_bg.jpg"  # Absolute path to your generated image
    change_wallpaper(image_path)
