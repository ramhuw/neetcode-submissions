class DynamicArray(capacity: Int) {

    private var arr: IntArray = IntArray(size=capacity, init= { _ -> 0 })
    private var _size: Int = 0
    private var _capacity: Int = capacity

    init {
        require(capacity > 0)
    }

    fun get(i: Int): Int {
        return arr[i]
    }

    fun set(i: Int, n: Int) {
        arr[i] = n
    }

    fun pushback(n: Int) {
        if (_size == _capacity) {
            resize()
        }
        arr[_size] = n
        _size += 1
    }

    fun popback(): Int {
        _size -= 1
        return arr[_size]
    }

    private fun resize() {
        arr = IntArray(2 * _capacity, { x -> if (x < _size) { arr[x] } else { 0 }})
        _capacity *= 2
    }

    fun getSize(): Int {
        return _size
    }

    fun getCapacity(): Int {
        return _capacity
    }
}