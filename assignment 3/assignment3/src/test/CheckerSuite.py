import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
            static Test2 abcc(Test1 a){
                int a;
                Test2 an;
                for i := 1 to 100 do 
                {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
            void aneue,onichann= 1213;
        }
        class Test2 {
            int a = "addmaximum",b = 0001.18;
            Test abc;
            void aneue,onichann= 1213;
        }"""
        expect = "successful"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 400)) 
    