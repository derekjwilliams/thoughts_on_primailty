class BetaN:
    def __init__(self):
        self.N = set(range(10))  # we'll simulate ℕ by {0, 1, ..., 9}
        self.ideal_points = ["ultrafilter_1", "ultrafilter_2"]

    def points(self):
        return self.N.union(self.ideal_points)

    def bounded_function(self, n):
        """Simulate a bounded continuous function on ℕ"""
        if n in self.N:
            return n % 3  # example: just return n mod 3
        elif n == "ultrafilter_1":
            return 1     # pretend "ultrafilter_1" extends to value 1
        elif n == "ultrafilter_2":
            return 2     # pretend "ultrafilter_2" extends to value 2
        else:
            raise ValueError(f"Unknown point: {n}")

def main():
    space = BetaN()
    print("Points in βℕ (simulation):")
    for p in space.points():
        print(f"  Point: {p},  f(p) = {space.bounded_function(p)}")

if __name__ == "__main__":
    main()