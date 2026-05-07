protocol Shape: AnyObject {
    func clone() -> Shape
}

class Rectangle: Shape {
    private let width: Int
    private let height: Int

    init(_ width: Int, _ height: Int) {
        self.width = width
        self.height = height
    }

    func getWidth() -> Int { return width }
    func getHeight() -> Int { return height }

    func clone() -> Shape {
        return Rectangle(self.getWidth(), self.getHeight())
    }
}

class Square: Shape {
    private let length: Int

    init(_ length: Int) {
        self.length = length
    }

    func getLength() -> Int { return length }

    func clone() -> Shape {
        return Square(self.getLength())
    }
}

class Test {
    func cloneShapes(_ shapes: [Shape]) -> [Shape] {
        shapes.map {
            shape in shape.clone()
        }
    }
}
