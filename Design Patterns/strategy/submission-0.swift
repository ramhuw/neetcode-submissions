class Person {
    private let lastName: String
    private let age: Int
    private let married: Bool

    init(_ lastName: String, _ age: Int, _ married: Bool) {
        self.lastName = lastName
        self.age = age
        self.married = married
    }

    func getLastName() -> String { return lastName }
    func getAge() -> Int { return age }
    func isMarried() -> Bool { return married }
}

protocol PersonFilter {
    func apply(_ person: Person) -> Bool
}

class AdultFilter: PersonFilter {
    func apply(_ person: Person) -> Bool {
        return person.getAge() >= 18
    }
}

class SeniorFilter: PersonFilter {
    func apply(_ person: Person) -> Bool {
        return person.getAge() >= 65
    }
}

class MarriedFilter: PersonFilter {
    func apply(_ person: Person) -> Bool {
        return person.isMarried()
    }
}

class PeopleCounter {
    private var filter: PersonFilter? = nil

    func setFilter(_ filter: PersonFilter) {
        self.filter = filter
    }

    func count(_ people: [Person]) -> Int {
        return people.filter(filter!.apply).count
    }
}
