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
        expect = """[ClassDecl(classname=Id(name='Shape'), memlist=[AttributeDecl(kind=<AST.Instance object at 0x00000258FE7B9B80>, decl=VarDecl(variable=Id(name='length'), varType=<AST.FloatType object at 0x00000258FE7B9130>, varInit=None)), AttributeDecl(kind=<AST.Instance object at 0x00000258FE7B9F40>, decl=VarDecl(variable=Id(name='width'), varType=<AST.FloatType object at 0x00000258FE7B9130>, varInit=None)), MethodDecl(kind=<AST.Instance object at 0x00000258FE7B9C70>, name=Id(name='getArea'), param=[], returnType=<AST.FloatType object at 0x00000258FE7B93D0>, body=Block(decl=[], stmt=[])), MethodDecl(kind=<AST.Instance object at 0x00000258FE7B9A00>, name=Id(name='<init>'), param=[VarDecl(variable=Id(name='length'), varType=<AST.FloatType object at 0x00000258FE7B97F0>, varInit=None), VarDecl(variable=Id(name='width'), varType=<AST.FloatType object at 0x00000258FE7B97F0>, varInit=None)], returnType=None, body=Block(decl=[], stmt=[Assign(lhs=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FE7B9BB0>, fieldname=Id(name='length')), exp=Id(name='length')), Assign(lhs=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FE7D8C40>, fieldname=Id(name='width')), exp=Id(name='width'))]))], parentname=None), ClassDecl(classname=Id(name='Rectangle'), memlist=[MethodDecl(kind=<AST.Instance object at 0x00000258FE7D8C10>, name=Id(name='getArea'), param=[], returnType=<AST.FloatType object at 0x00000258FE7D8BE0>, body=Block(decl=[], stmt=[Return(expr=BinaryOp(op='*', left=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FE7D8A60>, fieldname=Id(name='length')), right=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FE7D83A0>, fieldname=Id(name='width'))))]))], parentname=Id(name='Shape')), ClassDecl(classname=Id(name='Triangle'), memlist=[MethodDecl(kind=<AST.Instance object at 0x00000258FE7D8250>, name=Id(name='getArea'), param=[], returnType=<AST.FloatType object at 0x00000258FE7D8610>, body=Block(decl=[], stmt=[Return(expr=BinaryOp(op='/', left=BinaryOp(op='*', left=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FE7D8D00>, fieldname=Id(name='length')), right=FieldAccess(obj=<AST.SelfLiteral object at 0x00000258FEA24040>, fieldname=Id(name='width'))), right=IntLiteral(value=2)))]))], parentname=Id(name='Shape'))]"""
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
        expect = 'Type Mismatch In Expression: BinaryOp(\,IntLit(10),BooleanLit(True))'
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
        expect = 'Type Mismatch In Expression: BinaryOp(\,IntLit(10),BooleanLit(True))'
        self.assertTrue(TestChecker.test(input, str(expect), 407))
