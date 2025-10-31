import cv2
from collections import Counter # библиотека для подсчета элементов

def dominant_color(image_path):
    # Читаем изображение
    img = cv2.imread(image_path)
    
    # Преобразование формата BGR в RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Получаем список всех цветов (R,G,B) на картинке
    colors = []
    height, width, _ = rgb_img.shape
    for y in range(height):
        for x in range(width):
            pixel = tuple(rgb_img[y,x])  # Получаем значения цвета конкретного пикселя
            colors.append(pixel)
            
    # Определяем наиболее часто встречающийся цвет
    most_common_color = Counter(colors).most_common(1)[0][0]
    
    # Возвращаем описание цвета
    color_map = {
        (255, 0, 0): "красный",
        (0, 255, 0): "зеленый",
        (0, 0, 255): "синий",
        (255, 255, 0): "желтый",
        (255, 0, 255): "фиолетовый",
        (0, 255, 255): "голубой",
        (255, 255, 255): "белый",
        (0, 0, 0): "черный",
    }
    
    closest_color = min(color_map.keys(), key=lambda col: sum((col[i]-most_common_color[i])**2 for i in range(3)))
    # находим ближайший известный цвет к преобладающему цвету на изображении
    return color_map[closest_color] 

if __name__ == "__main__":
    path_to_image = input("Введите путь к изображению: ")
    detected_color = dominant_color(path_to_image)
    print(f"Доминирующий цвет на изображении: {detected_color}.")