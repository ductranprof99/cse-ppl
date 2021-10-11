
"""
 * @author nhphung
"""
# from _typeshed import NoneType
from typing import MutableSequence
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from abc import ABC, abstractmethod, ABCMeta



class MemberType(ABC):
    def __init__(self,name:str,parent_name:str):
        '''
        member type present member in class (attribute and method)\n
        if member is static then their classname cannot be None \n
        parent name in attribute/method case is the class contain them in class case is the class that they inherited.
        '''
        self.name = name
        self.parent_name = parent_name 

    # check id in the membertype list
    def __eq__(self, item_name:str): 
        return item_name == self.name
            

class VType(MemberType): 
    '''
    # attribute/variable represent \n
    if Vtype is static -> its in global scope and store in global \n
    if Vtype is instance -> its a var and store in lower order scope
    '''
    def __init__(self,name:str,class_name:str,vartype:Type,isConst:bool=False):
        super().__init__(name,class_name)
        self.vartype = vartype
        self.isConst = isConst
    
    def is_Constant(self):
        return self.isConst

class MType(MemberType): # method type
    def __init__(self,name:str,parent_name:str,partype:List[Type],rettype:Type):
        '''
        method type in class\n
        parameter \n
        parent_name: will not None if method not static\n
        param_type: list of parameter type\n
        return_type: return type
        '''
        super().__init__(name,parent_name)
        self.param_type = partype
        self.return_type = rettype


class Ctype(MemberType): 
    '''
    class type, contain instance attribute, instance method and whole bunch of shit
    '''
    def __init__(self,name:str,parent:str=None,attributeList:List[MemberType]=None,methodlist:List[MemberType]=None):
        super().__init__(name,parent)
        self.listAttribute = attributeList 
        self.listMethod = methodlist
        # only store instance  
    
    def addMethod(self,method:MemberType):
        self.listMethod.append(method)
        

class Symbol:
    def __init__(self,element:MemberType):
        self.element = element

    def __eq__(self, info): 
        # info 0 = item name, info 1 = parent (class container) name
        # find item in list of Symbol
        if info[1] == None:   
            return info[0] == self.element.name
        return info[0] == self.element.name and info[1] == self.element.parent_namee
    

class StaticChecker(BaseVisitor,Utils):
    listIo_method = [MType('readInt','io',None,IntType()),
    MType('writeInt','io',[IntType()],VoidType()),
    MType('writeIntLn','io',[IntType()],VoidType()),
    MType('readFloat','io',None,FloatType()),
    MType('writeFloat','io',[FloatType()],VoidType()),
    MType('writeFloatLn','io',[FloatType()],VoidType()),
    MType('readBool','io',None,BoolType()),
    MType('writeBool','io',[BoolType()],VoidType()),
    MType('writeBoolLn','io',[BoolType()],VoidType()),
    MType('readStr','io',None,StringType()),
    MType('writeStr','io',[StringType()],VoidType()),
    MType('writeStrLn','io',[StringType()],VoidType()),]

    global_envi ={'global': [Symbol(i) for i in listIo_method] + [Symbol(Ctype(name='io'))]}
            
    '''
    cau truc cua global environment la 1 dict (hacker man)
    block k co ten cu the, voi co the truy xuat truc tiep
    {
     level 0: 
     'global':[chua list[Symbol] class, static method, static attribute (global scope)],
     level 1:
     'class':str: chua ten class ('ten_class'),
     'ten_class': [chua list[Symbol] cua class scope = instance method/instance att],
     level 2:
     'method':str: chua ten method ('ten_method')
     'ten_method': [chua list[Symbol] cua method scope = var declare in method],
     level 3:
     'block': [chua list[Symbol] cua block scope = var declare in block],
    }
    '''
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast:Program, c): 
        for i in ast.decl:
            c['global'].append(self.visit(i,c))

   
    def visitVarDecl(self, ast, param):
        return None
    
    def visitConstDecl(self, ast, param):
        return None
    
    def visitClassDecl(self, ast:ClassDecl, param):
        name = ast.classname
        parent_name = ast.parentname
        if name in param['global']:
            raise Redeclared(Class(),name)
        if parent_name not in param['global']:
            raise Undeclared(Class(),parent_name)
        class_order = {'global': param['global'], 'class': name, name: []}
        for i in ast.memlist:
            class_order[name] += self.visit(i,class_order)
        # if there no error

    
    def visitStatic(self, ast, param):
        return None
    
    def visitInstance(self, ast, param):
        return None
    
    def visitMethodDecl(self, ast, param):
        return None
    
    def visitAttributeDecl(self, ast, param):
        return None
    
    
    
    def visitClassType(self, ast, param):
        return None
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            if c[1]:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(ast)
        else:
            return res.mtype.rettype
    
    def visitNewExpr(self, ast, param):
        return None
    
    def visitId(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitBlock(self, ast, param):
        return None
    
    def visitIf(self, ast, param):
        return None
    
    def visitFor(self, ast, param):
        return None
    
    def visitContinue(self, ast, param):
        return None
    
    def visitBreak(self, ast, param):
        return None
    
    def visitReturn(self, ast, param):
        return None
    
    def visitAssign(self, ast, param):
        return None
    
    def visitCallStmt(self, ast, param):
        pass 
    




    # Visit Literal Values => Return Type of Literal

    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        '''return type and length of array literal'''
        globalType = self.visit(ast.value[0])
        for i in ast.value:
            type_ele = self.visit(i,param)
            if type(type_ele[0]) is ArrayType:
                raise IllegalArrayLiteral(i)
            elif type_ele[1] == 0:
                raise IllegalArrayLiteral(i)
            elif type(type_ele[0]) is not globalType[0]:
                raise IllegalArrayLiteral(i)
        return globalType, len(ast.value)


    def visitIntLiteral(self, ast, param):
        return IntType(),1
    
    def visitFloatLiteral(self, ast, param):
        return FloatType(),1
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType(),1
    
    def visitStringLiteral(self, ast, param):
        return StringType(),1
    
    def visitNullLiteral(self, ast, param):
        return VoidType(),0
    
    def visitSelfLiteral(self, ast, param):
        return ClassType('init'),0
    
