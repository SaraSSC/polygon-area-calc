class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        output = ""
        for line in range(self.height):
            for line in range(self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, shape: "Rectangle") -> int:
        return int(self.get_area() / shape.get_area())

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_side(self, side: int):
        super().set_height(side)
        super().set_width(side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_height(self, height: int):
        self.set_side(height)

    def set_width(self, width: int):
        self.set_side(width)
