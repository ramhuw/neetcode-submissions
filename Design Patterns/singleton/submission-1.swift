class Singleton {

    static var value: String?

    private init() {}

    static func getInstance() -> Singleton {
        Singleton()
    }

    func getValue() -> String? {
        Singleton.value
    }

    func setValue(_ value: String) {
        Singleton.value = value
    }
}
