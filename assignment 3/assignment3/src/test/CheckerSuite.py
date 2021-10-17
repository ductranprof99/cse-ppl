import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        input = """
            class Shape {
                static float mehter;
                float length,shape,shape;
                float getArea(int shape) {
                    length = 5;
                }
               
                
            }
            
            
                

        """
        # Neu muon check class truoc check param thi sao
        expect =''
        self.assertTrue(TestChecker.test(input, expect, 400)) 
    