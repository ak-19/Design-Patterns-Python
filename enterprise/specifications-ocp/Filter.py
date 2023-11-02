class Filter:
    def filter(self, spec, items):
        for i in items:
            if spec.is_satisfied(i):
                yield i    