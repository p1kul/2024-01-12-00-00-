import unittest
import logging
import tor

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            human1 = tor.Runner('Иван',speed= -1)
            human1.walk()
            self.assertEqual(human1.distance,1)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость объекта Runner',exc_info=True)

    def test_run(self):
        try:
            human2 = tor.Runner(name = 2)
            human2.run()
            self.assertEqual(human2.distance, 10)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)








