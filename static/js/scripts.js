document.addEventListener('DOMContentLoaded', function() {
    var canvas = new fabric.Canvas('c');

    // Добавление текстовой заметки
    var text = new fabric.Text('Hello, world!', { left: 100, top: 100 });
    canvas.add(text);

    // Добавление круга
    var circle = new fabric.Circle({ radius: 50, fill: 'green', left: 200, top: 200 });
    canvas.add(circle);

    // Добавление изображения
    fabric.Image.fromURL('path/to/image.jpg', function(img) {
        img.set({ left: 300, top: 300 });
        canvas.add(img);
    });
});
