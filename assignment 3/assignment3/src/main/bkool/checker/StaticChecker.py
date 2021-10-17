
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



class MemberInClass(ABC):
    def __init__(self,name:str):
        self.name = name

    # check id in the membertype list
    def __eq__(self, item_name:str): 
        return item_name == self.name
            

class MemVar(MemberInClass):
    def __init__(self,name:str,type:Type,isConst:bool):
        super().__init__(name)
        self.type = type
        self.isConst = isConst

    def __str__(self):
        return "instance var: " + self.name 

class BlockEle():
    def __init__(self,listVarInBlock:list[MemVar],isLoop:bool):
        self.listVarInBlock = listVarInBlock
        self.isLoop = isLoop
        self.blockChild = []
        self.theName = []

    def addChildBlock(self,block_of_method):
        '''
        this function add nested block
        '''
        self.blockChild.append(block_of_method)

    def addvar(self,var:MemVar):
        '''
        this function has check var name valid in its
        '''
        if var.name in self.theName:
            if var.isConst: 
                raise Redeclared(Constant(),var.name)
            else:
                raise Redeclared(Variable(),var.name)
        self.listVarInBlock.append(var)
        self.theName.append(var.name)

    def __str__(self) -> str:
        a = '(((((((((((((((block' + ('of loop' if self.isLoop else '') + '))))))))))))))))))\n'
        for i in self.listVarInBlock:
            a += str(i) +'\n'
        a += '~~~~~~~~~~~~ block child (for, if, nested block) ~~~~~~~~~~~~~~~~~~~~~\n'
        for i in self.blockChild:
            a += str(i) +'\n'
        a += '~~~~~~~~~~~~~~~~~~~~~~~~~~ end of nested ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        a += '((((((((((((((((((((((|)))))))))))))))))))))))'
        return a

class MemMethod(MemberInClass):
    def __init__(self,name:str,returnType:Type,listParam:List[MemVar]=None):
        super().__init__(name)
        self.rettype = returnType
        self.params = listParam
        self.block = BlockEle([],False)
        # list list var decl

    def check(self):
        local = self.params + self.block.listVarInBlock
        self.checkParamFirst()
        for i in range(0,len(self.block.listVarInBlock)):
            if self.block.listVarInBlock[i].name in local[:len(self.params)+i:]:
                if self.block.listVarInBlock[i].isConst:
                    raise Redeclared(Constant(),self.block.listVarInBlock[i].name)
                else:
                    raise Redeclared(Variable(),self.block.listVarInBlock[i].name)

    def checkParamFirst(self):
        count = 0
        if len(self.params) > 2:
            for i in self.params[:-1:]:
                for j in self.params[count::]:
                    if j.name == i.name:
                        raise Redeclared(Parameter(),i.name)
                count += 1

    def __str__(self):
        a = '-----method-----'
        a += 'instance method: {:25s} \n'.format(self.name)
        a += str(self.block) + '\n'
        a +='----------------'
        return a



class Symbol():
    def __init__(self,elename,eleparent) :
        self.name = elename
        self.eleparent = eleparent
    
    def __eq__(self, o: tuple) :
        return (o[0] == self.name) and (o[1] == self.eleparent)

    


class VarSymbol(Symbol): 
    '''
    ### global attribute represent 
    '''
    def __init__(self,name:str,class_name:str,vartype:Type,isConst:bool=False):
        super().__init__(name,class_name)
        self.vartype = vartype
        self.isConst = isConst
    
    def is_Constant(self):
        return self.isConst

    def __str__(self):
        return  'global var: {:25s} {:32s}'.format(self.name,self.eleparent)

class MethodSymbol(Symbol): # method type
    def __init__(self,name:str,parent_name:str,partype:List[MemVar],rettype:Type):
        super().__init__(name,parent_name)
        self.params = partype
        self.return_type = rettype
        self.block = BlockEle([],False)
    
    def check(self):
        local = self.params + self.block.listVarInBlock
        self.checkParamFirst()
        for i in range(0,len(self.block.listVarInBlock)):
            if self.block.listVarInBlock[i].name in local[:len(self.params)+i:]:
                if self.block.listVarInBlock[i].isConst:
                    raise Redeclared(Constant(),self.block.listVarInBlock[i].name)
                else:
                    raise Redeclared(Variable(),self.block.listVarInBlock[i].name)

    def checkParamFirst(self):
        count = 0
        if len(self.params) > 2:
            for i in self.params[:-1:]:
                for j in self.params[count::]:
                    if j.name == i.name:
                        raise Redeclared(Parameter(),i.name)
                count += 1
    def __str__(self):
        a = '-----global method-----\n'
        a += 'global method: {:25s} {:32s} \n'.format(self.name,self.eleparent)
        a += str(self.block) + '\n'
        a += '----------------------'
        return a
        

class ClassSymbol(Symbol): 
    '''
    class type, contain instance attribute, instance method and whole bunch of shit
    '''
    def __init__(self,name:str,parent:str=None,attributeList:List[MemVar]=[],methodlist:List[MemMethod]=[]):
        super().__init__(name,parent)
        self.listAttribute = attributeList 
        self.listMethod = methodlist
        # only store instance  
        self.theName = {'attribute': [], 'method': []} # this thing store both to check
    
    def add(self,o):
        if type(o) == MemVar:
            self.addInstanceVar(o)
        else: self.addMethod(o)

    def addInstanceVar(self,attr:MemVar):
        self.addName(attr.name,False)
        self.listAttribute.append(attr)

    def addMethod(self,method:MemMethod):
        self.addName(method.name,True)
        self.listMethod.append(method)

    def addName(self,name:str,isMethod:bool):
        if isMethod:
            if name in self.theName['attribute'] + self.theName['method']:
                raise Redeclared(Method(),name)
            self.theName['method'].append(name)
        else: 
            if name in self.theName['attribute']:
                raise Redeclared(Attribute(),name)
            self.theName['attribute'].append(name)

    def __str__(self):
        a = '============================================ class =======================================\n'
        a += "class: " + self.name + "|| inherited (optional): " + (self.eleparent if self.eleparent else '-1') + '\n' 
        a += 'instance attribute:\n'
        for i in self.listAttribute:
            a = a+ str(i) + '\n'
        a += 'instance method:\n'
        for i in self.listMethod:
            a = a+ str(i) + '\n'
        a += '==========================================================================================\n'
        return a

class UsefulTool():
    @staticmethod
    def checkListSymbol(o:List[object]):
        pass

    @staticmethod
    def inspectError(p):
        for i in range(0,10):
            print('\n')
        print(p)
        for i in range(0,10):
            print('\n')




class VariableLoad(BaseVisitor,Utils):
    # this class for loading variable in ast tree into 

    
 
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = None

    def caculate_glob(self):
        listIo_method = [MethodSymbol('readInt', 'io', None, IntType()),
                         MethodSymbol('writeInt', 'io', [MemVar('anArg', IntType(), False)], VoidType()),
                         MethodSymbol('writeIntLn', 'io', [MemVar('anArg', IntType(), False)], VoidType()),
                         MethodSymbol('readFloat', 'io', None, FloatType()),
                         MethodSymbol('writeFloat', 'io', [MemVar('anArg', FloatType(), False)], VoidType()),
                         MethodSymbol('writeFloatLn', 'io', [MemVar('anArg', FloatType(), False)], VoidType()),
                         MethodSymbol('readBool', 'io', None, BoolType()),
                         MethodSymbol('writeBool', 'io', [MemVar('anArg', BoolType(), False)], VoidType()),
                         MethodSymbol('writeBoolLn', 'io', [MemVar('anArg', BoolType(), False)], VoidType()),
                         MethodSymbol('readStr', 'io', None, StringType()),
                         MethodSymbol('writeStr', 'io', [MemVar('anArg', StringType(), False)], VoidType()),
                         MethodSymbol('writeStrLn', 'io', [MemVar('anArg', StringType(), False)], VoidType()), ]
        class_io = ClassSymbol(name='io')
        for i in listIo_method:
            class_io.addName(i.name, True)
        global_envi = listIo_method + [class_io]
        self.global_envi = global_envi

    def check(self):
        self.caculate_glob()
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast:Program, param:list):
        for i in ast.decl:
            param += [self.visit(i,param)]
    
    
    def visitClassDecl(self, ast:ClassDecl, param:List):
        current_class = ClassSymbol(ast.classname.name,ast.parentname.name if ast.parentname else None,[],[])
        for i in ast.memlist:
            self.visit(i,(param,current_class))
        return current_class

    def visitMethodDecl(self, ast:MethodDecl, param:tuple[List,ClassSymbol]):
        method_name = ast.name.name
        if type(ast.kind) == Static or ast.name.name == '<init>':
            x = MethodSymbol(method_name,param[1].name,[],ast.returnType)
            for i in ast.param:
                param_i = MemVar(None,None,False)
                self.visit(i,param_i)
                x.params.append(param_i)
                x.checkParamFirst()
            self.visit(ast.body,(x.block,False))
            x.check()
            param[0].append(x)
            param[1].addName(method_name,True)
        else:
            x = MemMethod(method_name,ast.returnType,[])
            for i in ast.param:
                param_i = MemVar(None,None,False)
                self.visit(i,param_i)
                x.params.append(param_i)
                x.checkParamFirst()
            self.visit(ast.body,(x.block,False))
            x.check()
            param[1].add(x)
    
    def visitAttributeDecl(self, ast:AttributeDecl, param:tuple[List,ClassSymbol]):
        if type(ast.kind) == Static:
            x = VarSymbol(None,param[1].name,None,False)
            if type(ast.decl) == ConstDecl:
                x.isConst = True
            self.visit(ast.decl,x)
            param[0].append(x)
            param[1].addName(x.name,False)
            
        else:
            x = MemVar(None,None,False)
            if type(ast.decl) == ConstDecl:
                x.isConst = True
            self.visit(ast.decl,x)
            param[1].add(x)

    def visitVarDecl(self, ast:VarDecl, param):
        param.name = ast.variable.name
        param.vartype = ast.varType

    def visitConstDecl(self, ast, param):
        param.name = ast.variable.name
        param.vartype = ast.varType
    
    
    def visitBlock(self, ast:Block, param:tuple[BlockEle,bool]):
        # inherit for loop so you need this bitch
        is_in_loop = param[1]
        param[0].isLoop = is_in_loop
        for i in ast.decl:
            x = MemVar(None,None,True)
            if type(i) == VarDecl:
                x.isConst = False
            self.visit(i,x)
            param[0].addvar(x)
        for i in ast.stmt:
            if type(i) == For and type(i.loop) == Block:
                x = BlockEle([],True)
                self.visit(i,(x,True))
                param[0].addChildBlock(x)        
            elif type(i) == Block:
                x = BlockEle([],False)
                self.visit(i,(x,is_in_loop))
                param[0].addChildBlock(x)   
            elif type(i) == If:
                if type(i.thenStmt) == Block:
                    x = BlockEle([],False)
                    self.visit(i.thenStmt,(x,is_in_loop))
                    param[0].addChildBlock(x)   
                    if  type(i.elseStmt) == Block: 
                        x2 = BlockEle([],False)
                        self.visit(i.elseStmt,(x2,is_in_loop))
                        param[0].addChildBlock(x2)
    
    
    def visitFor(self, ast:For, param:tuple[BlockEle,bool]):
        param[0].addvar(MemVar(ast.id.name,IntType(),False))
        self.visit(ast.loop,param)

    

class StaticChecker(BaseVisitor,Utils):
    
    global_envi = None
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        t = VariableLoad(self.ast)
        t.check()
        StaticChecker.global_envi = t.global_envi
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast:Program, c): 
        for i in c:
            print(i)
        return 'a'

   
    
    def visitClassDecl(self, ast:ClassDecl, param):
        pass


    def visitAttributeDecl(self, ast:AttributeDecl, param:dict):
        pass
    
    def visitStatic(self, ast, param):
        return
    
    def visitInstance(self, ast, param):
        return 
    
    def visitVarDecl(self, ast:VarDecl, param:dict):
        return 
    
    def visitConstDecl(self, ast:ConstDecl, param:dict):
        return
    
    def visitMethodDecl(self, ast:MethodDecl, param:dict):
        return None
    
    
    
    def visitBinaryOp(self, ast, param):
        return None
    
    def visitUnaryOp(self, ast, param):
        return None
    
    def visitCallExpr(self, ast, c): 
        pass
    
    def visitNewExpr(self, ast, param):
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


    def visitClassType(self, ast:ClassType, param):
        return ast

    def visitIntLiteral(self, ast, param):
        return IntType(),1
    
    def visitFloatLiteral(self, ast, param):
        return FloatType(),1
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType(),1
    
    def visitStringLiteral(self, ast, param):
        return StringType(),1
    
    def visitNullLiteral(self, ast, param):
        return VoidType(),-1
    
    def visitSelfLiteral(self, ast, param):
        return ClassType('<init>'),0
    

    def visitId(self, ast:Id, param):
        return ast.name


class A {
    int a ;
    void foo () {
        a := 5;
    } 
}