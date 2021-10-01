import unittest
from TestUtils import TestAST
from AST import *
from main.bkool.utils.AST import ConstDecl, IntType

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test1(self):
        input = """class main {
            final int a = 3;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),ConstDecl(Id('a'),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test2(self):
        input = """class main {
            final int a = 3;

            main(){}
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id('main'),[AttributeDecl(Instance(),ConstDecl(Id('a'),IntType(),IntLiteral(3))),MethodDecl(Instance(),Id('<init>'),[],None,Block([],[])),MethodDecl(Instance(),Id('<init>'),[],None,Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test3(self):
        input = """
        class Exam {
                        static int a = 5, b;
                    }
        }"""
        expect = str(Program(decl=[ClassDecl(classname=Id(name='Exam'), memlist=[AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='a'), varType=IntType(), varInit=IntLiteral(value=5))), AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='b'), varType=IntType(), varInit=None))], parentname=None)]))
        self.assertTrue(TestAST.test(input,expect,303))
     
    def test4(self):
        input = """
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
        
                return this.length * this.width;
                }
                }

        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[])),MethodDecl(Id(<init>),Instance,[param(Id(length),FloatType),param(Id(width),FloatType)],Block([],[AssignStmt(FieldAccess(Self(),Id(length)),Id(length)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 304)) 

    def test5(self):
        input = """
        class S {
            int[5] a = {1,2,3};
        }
        """
        expect = str(Program([ClassDecl(Id('S'),[AttributeDecl(kind=Instance(),decl=VarDecl(variable=Id('a'),varType=ArrayType(size=5,eleType=IntType()),varInit=ArrayLiteral(value=[IntLiteral(value=1),IntLiteral(value=2),IntLiteral(value=3)])))])]))
        print(expect)
        self.assertTrue(TestAST.test(input,expect,305))

    def test6(self):
        input = """
        
        """
        expect = str()
        self.assertTrue(TestAST.test(input,expect,306))