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

    def test02(self):
        """
        successful test series
        """
        input_text = """class A {
            final int a = true;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,BooleanLit(True))"
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 402)) 

    def test03(self):
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
        self.assertTrue(TestChecker.test(input_text, expect, 403)) 
    
    def test04(self):
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
        expect = """['Valid']"""
        # Neu muon check class truoc check param thi sao
        self.assertTrue(TestChecker.test(input_text, expect, 404)) 

    def test05(self):
        input = """
            class Ex {
                final int val = 10 \\ true;
                final int a = 1 + 2 * 4;
                int b = 10 + 20 * 30;
            }
            """
        expect = 'Type Mismatch In Expression: BinaryOp(\,IntLit(10),BooleanLit(True))'
        self.assertTrue(TestChecker.test(input, str(expect), 405))


    def test06(self):
        input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Static(),VarDecl(Id("a"),IntType())),AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),FieldAccess(Id("Ex"),Id("a"))))])])
        expect = 'Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))'
        self.assertTrue(TestChecker.test(input, str(expect), 406))

    def test07(self):
        input = """
        class A {
            int a;
            void main() {
            int b = A.a;
            }
        }
        """
        expect = 'Illegal Member Access: FieldAccess(Id(A),Id(a))'
        self.assertTrue(TestChecker.test(input, str(expect), 407))
    def test08(self):
        input = """
        class Ex extends Ey{
        int a = 10 + 20;
        Ey classY = new Ey();
        static int c = 100;
        void foo () {
            Ey classEY = new Ey();
            int value = this.classY.classC.a;
        }
        }
        class Ey {
            float a = 10.0;
            Ec classC = new Ec();
            static int b = 10;
            static void foo () {

            }
        }
        class Ec {
            float a = 10.0;
        }
        """
        expect = """['Valid']"""
        self.assertTrue(TestChecker.test(input, str(expect), 408))

    def test09(self):
        input = """
        class Ex extends Ey{
        static Ey classY = new Ey();
        void foo () {
            int value = Ex.classC.a;
        }
        }
        class Ey {
            static Ec classC = new Ec();
        }
        class Ec {
            static float a = 10.0;
        }
        """
        expect = 'Illegal Member Access: FieldAccess(FieldAccess(Id(Ex),Id(classC)),Id(a))'
        self.assertTrue(TestChecker.test(input, str(expect), 409))

    def test10(self):
        input = """
        class A {
        int a = 90;
        void foo () {
            int b = 100;
            if (this.a > b) then {
                int c;
                if (this.a > c) then {
                    int d = c + b;
                }
            }
            if (c > b) then {
                
            }
        }
    }
        """
        expect = 'Undeclared Identifier: c'
        self.assertTrue(TestChecker.test(input, str(expect), 410))

    def test11(self):
        input = """
        class A {
            final int value = 10;
        }
        class B extends A {
            void foo(int a) {
                int b = 10;
                A classA = new A();
                if (b > this.value) then {
                    int b;
                    {
                        boolean b;
                        {
                            if b then {
                                float b = classA.value;
                            }
                        }
                        {
                            boolean d = b;
                            final int a = d + 1;
                        }
                    }
                }
            }
        }
        """
        expect = 'Type Mismatch In Expression: BinaryOp(+,Id(d),IntLit(1))'
        self.assertTrue(TestChecker.test(input, str(expect), 411))

    def test12(self):
        input = """
        class A {
            final float value = 10;
        }
        class B extends A {
            A classA_global = new A();
            void foo(int a) {
                int b = 1;
                A classA = new A();
                if (b > this.value) then {
                    int i = 0;
                    for i := 1 to this.value do {
                        int c = this.classA_global;
                    }
                }
            }
        }
        """
        expect = 'Type Mismatch In Statement: For(Id(i),IntLit(1),FieldAccess(Self(),Id(value)),True,Block([VarDecl(Id(c),IntType,FieldAccess(Self(),Id(classA_global)))],[])])'
        self.assertTrue(TestChecker.test(input, str(expect), 412))
    
    def test13(self):
        input = """
        class A {
        final int value = 10;
        }
        class B extends A {
            A classA_global = new A();
            void foo(int a) {
                int b = 1;
                A classA = new A();
                if (b > this.value) then {
                    int i = 0;
                    for i := 1.0 to this.value do {
                        int c = this.classA_global;
                    }
                }
            }
        }
        """
        expect = 'Type Mismatch In Statement: For(Id(i),FloatLit(1.0),FieldAccess(Self(),Id(value)),True,Block([VarDecl(Id(c),IntType,FieldAccess(Self(),Id(classA_global)))],[])])'
        self.assertTrue(TestChecker.test(input, str(expect), 413))

    def test14(self):
        input = """
        class A {
        final float value = 10;
        }
        class B extends A {
            A classA_global = new A();
            void foo(int a) {
                int b = 1;
                A classA = new A();
                for b := 0 to 10 do {
                    {
                        break;
                    }
                }
                continue;
            }
        }
        """
        expect = 'Continue Not In Loop'
        self.assertTrue(TestChecker.test(input, str(expect), 414))


    def test15(self):
        input = """
        class A {
            int a;
            void main() {
            final int b = this.a;
            }
        }
        """
        expect = 'Illegal Constant Expression: FieldAccess(Self(),Id(a))'
        self.assertTrue(TestChecker.test(input, str(expect), 415))

    
    def test16(self):
        input = """
        class A {
            void main() {
            final int b = 10.0;
            }
        }
        """
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(b),IntType,FloatLit(10.0))"""
        self.assertTrue(TestChecker.test(input, str(expect), 416))

    def test17(self):
        input = """
        class A {
            void main() {
            final int b = 10;
            b := 5;
            }
        }
        """
        expect = """Cannot Assign To Constant: AssignStmt(Id(b),IntLit(5))"""
        self.assertTrue(TestChecker.test(input, str(expect), 417))

    def test18(self):
        input = """
        class A {
            void main() {
            final int[6] b = {1,2,3,4,5};
            b := 5;
            }
        }
        """
        expect = """Type Mismatch In Constant Declaration: ConstDecl(Id(b),ArrayType(6,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])"""
        self.assertTrue(TestChecker.test(input, str(expect), 418))

    def test19(self):
        input = """
        class A {
            void main() {
            final int[5] b = {1,2,3,4,5};
            b := 5;
            }
        }
        """
        expect = """Cannot Assign To Constant: AssignStmt(Id(b),IntLit(5))"""
        self.assertTrue(TestChecker.test(input, str(expect), 419))

    def test20(self):
        input = """
        class A {
            final int[5] b = {1,2,3,4,5};
            void main() {
            this.b := 5;
            }
        }
        """
        expect = """Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(b)),IntLit(5))"""
        self.assertTrue(TestChecker.test(input, str(expect), 420))
    
    