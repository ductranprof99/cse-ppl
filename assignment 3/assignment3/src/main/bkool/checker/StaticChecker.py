
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
    
    def setNameandType(self,name,typ):
        self.type = typ
        self.name = name

    def __str__(self):
        return "instance var: " + self.name + ' type:' + str(self.type)

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
    
    def visitBlock(self,listClassName:list[str]):
        for memvar in self.listVarInBlock:
            if type(memvar.type) == ClassType and memvar.type.classname.name not in listClassName:
                raise Undeclared(Class(),memvar.type.classname.name)
            for i in self.blockChild:
                i.visitBlock(listClassName)

    def __str__(self) -> str:
        a = '(((((((((((((((block' + (' of loop' if self.isLoop else '') + '))))))))))))))))))\n'
        for i in self.listVarInBlock:
            a += str(i) + '\n'
        a += '\n\n~~~~~~~~~~~~ block child (for, if, nested block) ~~~~~~~~~~~~~~~~~~~~~\n'
        for i in self.blockChild:
            a += str(i) +'\n'
        a += '~~~~~~~~~~~~~~~~~~~~~~~~~~ end of nested ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n'
        a += '(((((((((((((((((' + ('end of loop' if self.isLoop else '') + ')))))))))))))))))'
        return a

class MemMethod(MemberInClass):
    def __init__(self,name:str,returnType:Type,listParam:List[MemVar]):
        super().__init__(name)
        self.rettype = returnType
        self.params = listParam
        self.block = BlockEle([],False)
        self.checkParamFirst()
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
        listName = []
        for i in self.params:
            if i.name not in listName:
                listName.append(i.name)
            else:
                raise Redeclared(Parameter(),i.name)
        
            

    def __str__(self):
        a = '-----method-----'
        a += 'instance method: {:25s} \n'.format(self.name)
        a += str(self.block) + '\n'
        a +='----------------'
        return a


class Symbol():
    def __init__(self,elename:str,eleparent:str) :
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

    def setNameandType(self,name,typ):
        self.name = name
        self.vartype = typ

    def __str__(self):
        return  'global var: {:25s} {:32s}'.format(self.name,self.eleparent)

class MethodSymbol(Symbol): # method type
    def __init__(self,name:str,parent_name:str,params:List[MemVar],return_type:Type):
        super().__init__(name,parent_name)
        self.params = params
        self.return_type = return_type
        self.block = BlockEle([],False)
        self.checkParamFirst()
    
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
        listName = []
        for i in self.params:
            if i.name not in listName:
                listName.append(i.name)
            else:
                raise Redeclared(Parameter(),i.name)
        

    def __str__(self):
        a = '-----global method-----\n'
        a += 'global method: {:25s} {:32s} \n'.format(self.name,self.eleparent)
        for i in self.params:
            a+= str(i) + '\n'
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
    def checkEleClassType(self,listClsName:list[str]):
        for memvar in self.listAttribute:
            if type(memvar.type) == ClassType and memvar.type.classname.name not in listClsName:
                raise Undeclared(Class(),memvar.type.classname.name)
        for method in self.listMethod:
            if type(method.rettype) == ClassType and method.rettype.classname.name not in listClsName:
                raise Undeclared(Class(),method.rettype.classname.name)
            for param in method.params:
                if type(param.type) == ClassType and param.type.classname.name not in listClsName:
                    raise Undeclared(Class(),param.type.classname.name)
            method.block.visitBlock(listClsName)
            


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
    def inspectError(p):
        for i in range(0,10):
            print('\n')
        print(p)
        for i in range(0,10):
            print('\n')

    @staticmethod
    def recheckClass(lstSym:List[Symbol]):
        listClassName = []
        for i in lstSym:
            if type(i) == ClassSymbol:
                listClassName.append(i.name)
                if UsefulTool.count(lstSym,i.eleparent) == 0 and i.eleparent != None:
                    raise Undeclared(Class(),i.eleparent)
                if UsefulTool.count(lstSym,i.name) >= 2:
                    raise Redeclared(Class(),i.name)
        for symbol in lstSym:
            if type(symbol) == VarSymbol:
                if type(symbol.vartype) == ClassType and symbol.vartype.classname.name not in listClassName:
                    raise Undeclared(Class(),symbol.vartype.classname.name)
            if type(symbol) == MethodSymbol:
                if type(symbol.return_type) == ClassType and symbol.return_type.classname.name not in listClassName:
                    raise Undeclared(Class(),symbol.return_type.classname.name)
                for memvar in symbol.params: 
                    if type(memvar.type) == ClassType and memvar.type.classname.name not in listClassName:
                        raise Undeclared(Class(),memvar.type.classname.name)
                symbol.block.visitBlock(listClassName)
            if type(symbol) == ClassSymbol:
                symbol.checkEleClassType(listClassName)

    @staticmethod
    def count(lst:List[Symbol],name):
        count = 0
        for i in lst:
            if type(i) == ClassSymbol and name == i.name:
                count+=1
        return count


class VariableLoad(BaseVisitor,Utils):
    # this class for loading variable in ast tree into 

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = None
        self.classCount = 0

    def caculate_glob(self):
        listIo_method = [MethodSymbol('readInt', 'io', [], IntType()),
                         MethodSymbol('writeInt', 'io', [MemVar('anArg', IntType(), False)], VoidType()),
                         MethodSymbol('writeIntLn', 'io', [MemVar('anArg', IntType(), False)], VoidType()),
                         MethodSymbol('readFloat', 'io',  [], FloatType()),
                         MethodSymbol('writeFloat', 'io', [MemVar('anArg', FloatType(), False)], VoidType()),
                         MethodSymbol('writeFloatLn', 'io', [MemVar('anArg', FloatType(), False)], VoidType()),
                         MethodSymbol('readBool', 'io',  [], BoolType()),
                         MethodSymbol('writeBool', 'io', [MemVar('anArg', BoolType(), False)], VoidType()),
                         MethodSymbol('writeBoolLn', 'io', [MemVar('anArg', BoolType(), False)], VoidType()),
                         MethodSymbol('readStr', 'io',  [], StringType()),
                         MethodSymbol('writeStr', 'io', [MemVar('anArg', StringType(), False)], VoidType()),
                         MethodSymbol('writeStrLn', 'io', [MemVar('anArg', StringType(), False)], VoidType()), ]
        class_io = ClassSymbol(name='io')
        for i in listIo_method:
            class_io.addName(i.name, True)
        # self.global_envi = listIo_method + [class_io]
        self.global_envi = []

    def check(self):
        self.caculate_glob()
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast:Program, param:list):
        for i in ast.decl:
            param += [self.visit(i,param)]
            self.classCount += 1
        UsefulTool.recheckClass(self.global_envi)
    
    def visitClassDecl(self, ast:ClassDecl, param:List):
        current_class = ClassSymbol(ast.classname.name,ast.parentname.name if ast.parentname else None,[],[])
        for i in ast.memlist:
            self.visit(i,(param,current_class))
        return current_class

    def visitMethodDecl(self, ast:MethodDecl, param:tuple[List,ClassSymbol]):
        x = None
        method_name = ast.name.name
        params = []
        for eachParam in ast.param:
            params.append(self.visit(eachParam,None))
        if type(ast.kind) == Static or ast.name.name == '<init>':
            x = MethodSymbol(method_name,param[1].name,params,ast.returnType)
        else:
            x = MemMethod(method_name,ast.returnType,params)
        self.visit(ast.body,(x.block,False))
        if type(x) == MethodSymbol:
            param[0].append(x)
            param[1].addName(method_name,True)
        else:
            param[1].add(x)
    
    def visitAttributeDecl(self, ast:AttributeDecl, param:tuple[List,ClassSymbol]):
        if type(ast.kind) == Static:
            x = self.visit(ast.decl,param[1].name)
            param[0].append(x)
            param[1].addName(x.name,False)
        else:
            x = self.visit(ast.decl,None)
            param[1].add(x)

    def visitVarDecl(self, ast:VarDecl, param):
        if param:
            return VarSymbol(name=ast.variable.name,class_name=param,vartype=ast.varType)
        return MemVar(isConst=False,name=ast.variable.name,type=ast.varType)

    def visitConstDecl(self, ast:ConstDecl, param):
        if param:
            return VarSymbol(name=ast.constant.name,class_name=param,vartype=ast.constType,isConst=True)
        return MemVar(isConst=True,name=ast.constant.name,type=ast.constType)
    
    def visitBlock(self, ast:Block, param:tuple[BlockEle,bool]):
        # inherit for loop so you need this bitch
        is_in_loop = param[1]
        param[0].isLoop = is_in_loop
        for i in ast.decl:
            x = self.visit(i,[])
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
        # c = glob_env + scope [[]]
        parser = {'global_env': c, 'scope': [[]]}
        for i in ast.decl:
            self.visit(i,parser)

    def visitClassDecl(self, ast:ClassDecl, param:dict):
        listSymbol:list[Symbol] = param['global_env']
        scope = param['scope']
        

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


