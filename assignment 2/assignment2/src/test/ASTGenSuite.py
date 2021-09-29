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
        expect = str(Program([ClassDecl(Id('main'),[AttributeDecl(Instance(),ConstDecl(Id('a'),IntType(),IntLiteral(3))),MethodDecl(Instance(),Id('<init>'),[],VoidType(),Block([],[])),MethodDecl(Instance(),Id('<init>'),[],VoidType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test3(self):
        input = """
        class Exam {
                        static int a = 5, b;
                    }
        }"""
        expect = str(Program(decl=[ClassDecl(classname=Id(name='Exam'), memlist=[AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='a'), varType=IntType(), varInit=IntLiteral(value=5))), AttributeDecl(kind=Static(), decl=VarDecl(variable=Id(name='b'), varType=IntType(), varInit=None))], parentname=None)]))
        self.assertTrue(TestAST.test(input,expect,303))
    