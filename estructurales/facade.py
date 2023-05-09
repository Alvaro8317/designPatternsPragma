class SubsystemA:
    def method1(self):
        return "Subsystem A, Method 1"
    
    def method2(self):
        return "Subsystem A, Method 2"

class SubsystemB:
    def method1(self):
        return "Subsystem B, Method 1"
    
    def method2(self):
        return "Subsystem B, Method 2"

class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        
    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem_a.method1())
        results.append(self._subsystem_b.method1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem_a.method2())
        results.append(self._subsystem_b.method2())
        return "\n".join(results)

if __name__ == "__main__":
    facade = Facade()
    print(facade.operation())
