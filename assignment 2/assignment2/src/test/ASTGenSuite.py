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
        self.assertTrue(TestAST.test(input,expect,305))

    def test6(self):
        input = """
        class Rectangle extends Node {
                void name(){
                    (a.b[t0]).yt := 1;
                }
            }
        """
        expect = str(Program([ClassDecl(classname=Id("Rectangle"),parentname=Id('Node'),memlist=[MethodDecl(name=Id('name'),kind=Instance(),param=[],returnType=VoidType(),body=Block(decl=[],stmt=[Assign(FieldAccess(ArrayCell(FieldAccess(Id("a"),Id("b")),Id("t0")),Id("yt")),IntLiteral(1))]))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test7(self):
        input = """
            class Rectangle extends Shape {
                float getArea(){
                    ID.total[0] := ID.total[0] +1;
                }
            }

        """
        expect = str(Program(
        [
            ClassDecl(
                Id("Rectangle"),
                [
                MethodDecl(
                    Instance(),
                    Id("getArea"),
                    [],
                    FloatType(),
                    Block([],
                        [
                            Assign(
                                    ArrayCell(FieldAccess(Id("ID"),Id("total")),IntLiteral(0)),
                                    BinaryOp("+",ArrayCell(FieldAccess(Id("ID"),Id("total")),IntLiteral(0)),IntLiteral(1))
                            )
                        ]
                    )
                )
                ],
                Id("Shape")
            )
        ]
        ))
        self.assertTrue(TestAST.test(input,expect,307))

    def test8(self):
        input = """
            class Rectangle extends Node {
                void name(){
                    int[3] a;
                    a[1 + x.foo(2)] := a[a[1 + 1]];
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id("Rectangle"),
                [
                    MethodDecl(
                        Instance(),
                        Id("name"),
                        [],
                        VoidType(),
                        Block(
                            [
                                VarDecl(Id("a"),ArrayType(3,IntType()))
                            ],
                            [
                                Assign(
                                    ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),
                                    ArrayCell(Id("a"),ArrayCell(
                                        Id("a"),
                                        BinaryOp("+",IntLiteral(1),IntLiteral(1))
                                    )
                                    )
                                )
                            ]
                        )
                    )
                ],
                Id("Node")
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,308))

    # def test9(self):
    #     input = """
    #     class Rectangle extends Node {
    #             void name(){
    #                 s := 1+2-(3*4)/5;
    #             }
    #         }
    #     """
    #     expect = str()

    #     self.assertTrue(TestAST.test(input,expect,309))

    def test10(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void stepbrother= 1213;
            void imstuck() {

            }
        }"""
        expect = str(Program([ClassDecl(classname=Id('Test'),memlist=[AttributeDecl(Instance(),VarDecl(Id('a'),IntType(),StringLiteral("addmaximum"))),AttributeDecl(Instance(),VarDecl(Id('b'),IntType(),FloatLiteral(1.18))),AttributeDecl(Static(),VarDecl(Id('stepbrother'),VoidType(),IntLiteral(1213))),MethodDecl(name=Id('imstuck'),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[]))])]))
        print(expect)
        print(expect)
        self.assertTrue(TestAST.test(input_text, expect, 310))

        
    def test11(self):
        input = """
        class Rectangle extends Node {
                void name(){
                    if i == 0 then
                        if a >= 0 
                            then a:= 0;
                        else 
                            return 0 + x.name();
                    else 
                        if !true 
                            then continue;
                        else 
                            if a == 1 then return this.name();
                }
            }

        """
        expect = str(str(Program([ClassDecl(classname=Id('Test'),memlist=[AttributeDecl(Instance(),VarDecl(Id('a'),IntType(),StringLiteral('"addmaximum"'))),AttributeDecl(Instance(),VarDecl(Id('b'),IntType(),FloatLiteral(1.18))),AttributeDecl(Static(),VarDecl(Id('stepbrother'),VoidType(),IntLiteral(1213))),MethodDecl(name=Id('imstuck'),kind=Instance(),param=[],returnType=VoidType(),body=Block([],[]))])])))
        self.assertTrue(TestAST.test(input,expect,311))