protocol State {
    func handleRequest(_ doc: Document)
}

class Document {
    private var state: State = Draft()
    private var approved: Bool = false

    func getState() -> State { return state }

    func setState(_ state: State) {
        self.state = state
    }

    func publish() {
        state.handleRequest(self)
    }

    func setApproval(_ isApproved: Bool) {
        self.approved = isApproved
    }

    func isApproved() -> Bool { return approved }
}

class Draft: State {
    func handleRequest(_ doc: Document) {
        doc.setState(Review())
    }
}

class Review: State {
    func handleRequest(_ doc: Document) {
        if doc.isApproved() {
            doc.setState(Published())
        } else {
            doc.setState(Draft())
        }
    }
}

class Published: State {
    func handleRequest(_ doc: Document) {
        
    }
}
