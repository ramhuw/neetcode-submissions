protocol Observer: AnyObject {
    func notify(_ itemName: String)
}

class Customer: Observer {
    private let name: String
    private var notifications: Int = 0

    init(_ name: String) {
        self.name = name
    }

    func notify(_ itemName: String) {
        notifications += 1
    }

    func countNotifications() -> Int { return notifications }
}

class OnlineStoreItem {
    private let itemName: String
    private var stock: Int 
    private var subscribers: [any Observer]

    init(_ itemName: String, _ stock: Int) {
        self.itemName = itemName
        self.stock = stock
        self.subscribers = []
    }

    func subscribe(_ observer: Observer) {
        self.subscribers.append(observer)
    }

    func unsubscribe(_ observer: Observer) {
        self.subscribers.removeAll {
            $0 === observer
        }
    }

    func updateStock(_ newStock: Int) {
        if self.stock == 0 && newStock > 0 {
            for customer in subscribers {
                customer.notify(self.itemName)
            }
        }
        self.stock = newStock
    }
}
