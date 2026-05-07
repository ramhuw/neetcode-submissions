class Singleton {

    static var value: String = ""
    static var set: Bool = false

    private init() {}

    static func getInstance() -> Singleton {
        Singleton()
    }

    func getValue() -> String? {
        Singleton.set ? Singleton.value : nil
    }

    func setValue(_ value: String) {
        Singleton.value = value
        Singleton.set = true
    }
}
