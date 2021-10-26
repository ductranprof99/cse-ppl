import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test00(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
            Test2 abcc(Test2 a,a){
                Test2 an;
                for i := 1 to 100 do 
                {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
            }
            void aneue,onichann= 1213;
        }
        """
        expect = "Redeclared Parameter: a"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 400)) 

    def test01(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
        }
        class Test {
            int a = "addmaximum",b = 0001.18;
            Test abc;
            void aneue,onichann= 1213;
        }"""
        expect = "Redeclared Class: Test"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 401)) 

    def test15(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static Test2 abc;
            static Test2 abcc(Test2 a){
                Test2 an;
                for i := 1 to 100 do 
                {
                    Test3 an;
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
        expect = "Undeclared Class: Test3"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 415)) 
    
    def test100(self):
        """
        successful test series
        """
        input_text = """
        class Shape {
            float length,width;
            float getArea() {

            }
            Shape(float length,width){
                this.length := length;
                this.width := width;
            }
        }
        class Rectangle extends Shape {
            float getArea(){
                return this.length*this.width;
            }
        }
        class Triangle extends Shape {
            float getArea(){
                return this.length*this.width / 2;
            }
        }
        
        """
        expect = ""
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 500)) 

    def test101(self):
        input = """
            class Ex {
                final int val = 10 \\ True;
                final int a = 1 + 2 * 4;
                int b = 10 + 20 * 30;
            }
            """
        expect = []
        self.assertTrue(TestChecker.test(input, str(expect), 501))
