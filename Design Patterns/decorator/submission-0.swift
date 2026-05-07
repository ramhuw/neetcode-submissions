class Coffee {
    func getCost() -> Double {
        fatalError("Subclasses must override getCost()")
    }
}

class SimpleCoffee: Coffee {
    override func getCost() -> Double { return 1.1 }
}

class CoffeeDecorator: Coffee {
    let decoratedCoffee: Coffee

    init(_ coffee: Coffee) {
        self.decoratedCoffee = coffee
    }

    override func getCost() -> Double {
        return decoratedCoffee.getCost()
    }
}

class MilkDecorator: CoffeeDecorator {
    override func getCost() -> Double {
        return self.decoratedCoffee.getCost() + 0.5
    }
}

class SugarDecorator: CoffeeDecorator {
    override func getCost() -> Double {
        return self.decoratedCoffee.getCost() + 0.2
    }
}

class CreamDecorator: CoffeeDecorator {
    override func getCost() -> Double {
        return self.decoratedCoffee.getCost() + 0.7
    }
}
