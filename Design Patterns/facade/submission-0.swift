class Order {
    private let contents: String
    private let takeOut: Bool

    init(_ contents: String, _ takeOut: Bool) {
        self.contents = contents
        self.takeOut = takeOut
    }

    func getOrder() -> String { return contents }
    func isTakeOut() -> Bool { return takeOut }
}

class Cashier {
    func takeOrder(_ contents: String, _ takeOut: Bool) -> Order {
        return Order(contents, takeOut)
    }
}

class Food {
    private let contents: String

    init(_ contents: String) {
        self.contents = contents
    }

    func getFood() -> String { return contents }
}

class Chef {
    func prepareFood(_ order: Order) -> Food {
        return Food(order.getOrder())
    }
}

class PackagedFood: Food {
    init(_ food: Food) {
        super.init(food.getFood() + " in a bag")
    }
}

class KitchenStaff {
    func packageOrder(_ food: Food) -> PackagedFood {
        return PackagedFood(food)
    }
}

class DriveThruFacade {
    private let cashier = Cashier()
    private let chef = Chef()
    private let kitchenStaff = KitchenStaff()

    func takeOrder(_ orderContents: String, _ takeOut: Bool) -> Food {
        let order = self.cashier.takeOrder(orderContents, takeOut)
        let food = self.chef.prepareFood(order)
        return if order.isTakeOut() {
            self.kitchenStaff.packageOrder(food)
        } else {
            food
        }
    }
}
