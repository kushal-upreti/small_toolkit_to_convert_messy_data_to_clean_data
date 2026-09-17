class Report:

    def __init__(self, dataset, average, city_count, oldest, youngest):
        self.dataset = dataset
        self.average = average
        self.city_count = city_count
        self.oldest = oldest
        self.youngest = youngest

    def display(self):

        print("\n========== REPORT ==========")

        print("Rows loaded:", self.dataset.rows_loaded)
        print("Rows cleaned:", self.dataset.rows_cleaned)
        print("Rows dropped:", self.dataset.rows_dropped)

        print("\nDropped reasons:")

        for reason, count in self.dataset.dropped_reasons.items():
            print(f"{reason}: {count}")

        print("\n\n******** Flagged duplicate Id for Review **********")
        print(f"Duplicated Id: {self.dataset.duplicate_ids}")

        print("\nAverage score:", self.average)

        print("\nPeople per city:")

        for city, count in self.city_count.items():
            print(f"{city}: {count}")

        if self.oldest is not None:
            print(
                f"\nOldest: {self.oldest.name}, "
                f"Age: {self.oldest.age}"
            )

        if self.youngest is not None:
            print(
                f"Youngest: {self.youngest.name}, "
                f"Age: {self.youngest.age}"
            )