import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            a:integer;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class Exam {
                                final int a = new A(1,a,"Khoa");
                            }"""
        expect = str(Program(decl=[ClassDecl(classname=Id(name='Exam'), memlist=[AttributeDecl(kind=Instance(), decl=ConstDecl(constant=Id(name='a'), constType=IntType(), value=NewExpr(classname=Id(name='A'), param=[IntLiteral(value=1), Id(name='a'), StringLiteral(value='"Khoa"')])))], parentname=None)]))
        self.assertTrue(TestAST.test(input,expect,302))
   