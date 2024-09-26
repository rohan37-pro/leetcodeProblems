class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for book in self.booked:
            if start>=book[0] and start<book[1] or end>book[0] and end<=book[1] or book[0]>=start and book[0]<end:
                return False
        else:
            self.booked.append([start, end])
            return True


