import unittest
from TestUtils import TestAST
from AST import *
from main.bkool.utils.AST import ConstDecl, IntType

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {
            final static int a = 3;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Static(),ConstDecl(Id('a'),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,301))
   