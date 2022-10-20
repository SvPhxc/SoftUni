from project.movie import Movie
import unittest
# test name if name empty
# test name if name not empty
# test year if year is less than 1887
# test year if year greater than 1887
# test actor if name not in list
# test actor if name in list
# test grater than both cases
# test repr for output
class TestMovie(unittest.TestCase):

    def test_init__expect_correct_attr(self):
        movie = Movie('Deadpool', 2016, 9.5)
        self.assertEqual(movie.name, 'Deadpool')
        self.assertEqual(movie.year, 2016)
        self.assertEqual(movie.rating, 9.5)
        self.assertEqual(movie.actors, [])

    def test_init__expect_error(self):
        with self.assertRaises(ValueError) as ve:
            Movie("", 1996, 4.6)
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

        with self.assertRaises(ValueError) as ve:
            Movie("Shrek", 1867, 9.3)
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor(self):
        movie = Movie('Fats and Furious', 2001, 10)
        movie.add_actor('Vin Disel')
        movie.add_actor('Poul Walker')
        self.assertEqual(movie.actors, ['Vin Disel', 'Poul Walker'])
        result = movie.add_actor('Poul Walker')
        self.assertEqual(result, "Poul Walker is already added in the list of actors!")

    def test_gt(self):
        a = Movie('Fast Five', 2011, 8.5)
        b = Movie('Need For Speed', 2014, 5.4)
        result1 = str(a > b)
        self.assertEqual(result1, f'"{a.name}" is better than "{b.name}"')
        c = Movie("Tokyo Drift", 2006, 9.8)
        result2 = str(a > c)
        self.assertEqual(result2, f'"{c.name}" is better than "{a.name}"')

    def test_repr(self):
        movie = Movie('Fats and Furious', 2001, 10)
        movie.add_actor('Vin Disel')
        movie.add_actor('Poul Walker')
        self.assertEqual(str(movie), f"Name: Fats and Furious\nYear of Release: 2001\nRating: 10.00\nCast: Vin Disel, Poul Walker")

if __name__ == "__main__":
    unittest.main()
