
"""
 * @author nhphung
"""
# from _typeshed import NoneType
from typing import MutableSequence
from AST import * 
from Visitor import *
from StaticError import *
from abc import ABC, abstractmethod, ABCMeta
import copy


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

    def getVar(self,var:str):
        for i in self.listVarInBlock:
            if i.name == var:
                return i

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
    
    def getBlockChildNumber(self,number):
        return self.blockChild[number-1]

    def __str__(self) -> str:
        a = '(((((((((((((((block' + (' of loop' if self.isLoop else '') + '))))))))))))))))))\n'
        for i in self.listVarInBlock:
            a += str(i) + '\n'
        for i in self.blockChild:
            a += '\n\n~~~~~~~~~~~~ block child (for, if, nested block) ~~~~~~~~~~~~~~~~~~~~~\n'
            a += str(i) +'\n'
            a += '~~~~~~~~~~~~~~~~~~~~~~~~~~ end of nested ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n'
        a += '((((((((((((((end block' + (' of loop' if self.isLoop else '') + ')))))))))))))))'
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
        a = '-------------------method------------------\n'
        a += 'instance method: {:25s} \n'.format(self.name)
        a +='-------------------------------------------\n'
        a += str(self.block) + '\n'
        a +='-------------------------------------------\n'
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
        self.rettype = return_type
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
        a = '==========================global method===========================\n'
        a += 'global method: {:25s} ||    class : {:32s} \n'.format(self.name,self.eleparent)
        a += '=================================================================\n'
        for i in self.params:
            a+= str(i) + '\n'
        a += str(self.block) + '\n'
        a += '=================================================================\n'
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
                if type(symbol.rettype) == ClassType and symbol.rettype.classname.name not in listClassName:
                    raise Undeclared(Class(),symbol.rettype.classname.name)
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

    @staticmethod
    def findfather(lst:List[ClassSymbol],name):
        for i in lst:
            if i.name == name:
                return i
    @staticmethod
    def construcHierrachy(startNode:ClassSymbol,lst:List[ClassSymbol],glob_env:List[Symbol]): 
        # this method need lst is list of class symbol
        construct = True
        result = {'attribute': startNode.listAttribute, 'method': startNode.listMethod, 'father':[startNode.name]}
        currrent_name:list[str] = startNode.theName['attribute'] + startNode.theName['method'] 
        current_node = startNode
        while(construct):
            if (current_node.eleparent == None) or (current_node.eleparent == startNode.name): 
                construct = False
            else:
                current_node = UsefulTool.findfather(lst,current_node.eleparent)
                result['father'].append(current_node.name)
                for i in current_node.listAttribute:
                    if i.name not in currrent_name:
                        currrent_name.append(i.name)
                        if type(i) == MemVar:
                            result['attribute'].append(i)
                        else: result['method'].append(i)
                for i in glob_env:
                    if (i.name not in currrent_name)  and (i.eleparent == current_node.name) and (type(i) != ClassSymbol):
                        x = copy.deepcopy(i)
                        x.eleparent = startNode.name
                        glob_env.append(x)
                        currrent_name.append(i.name)
        return result
    @staticmethod
    def getMethod(classDict:dict,method:str):
        for i in classDict['method']:
            if i.name == method:
                return i
    
    @staticmethod
    def validConvertType(lhs,rhs,classDict):
        if (type(lhs) in [BoolType,IntType]) and (type(lhs) in [BoolType,IntType]):
            if (type(rhs) != type(lhs)):
                return False
            return True
        if (type(lhs) == FloatType) and (type(rhs) not in [IntType,FloatType]):
            return False
        if type(lhs) == ClassType:
            if type(rhs) != ClassType:
                return False
            if rhs.classname.name not in classDict[lhs.classname.name]['father']:
                return False
        if (type(lhs) == ArrayType):
            if type(rhs) != ArrayType:
                return False
            if lhs.size != rhs.size:
                return False
            if lhs.eleType != rhs.eleType:
                return False
        return True
        


            

class VariableLoad(BaseVisitor):
    # this class for loading variable in ast tree into 

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = []
        self.classCount = 0
        self.classDictionary = {}

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
        # self.global_envi += (listIo_method + [class_io])

    def check(self):
        self.caculate_glob()
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast:Program, param:list):
        for i in ast.decl:
            param += [self.visit(i,param)]
            self.classCount += 1
        UsefulTool.recheckClass(self.global_envi)
        lst = []
        for i in param:
            if type(i) == ClassSymbol:
                lst.append(i)
        for i in lst:
            self.classDictionary[i.name] = UsefulTool.construcHierrachy(i,lst,param)
    
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
        if type(ast.kind) == Static:
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
            if type(i) == For:
                x = BlockEle([],True)
                self.visit(i,(x,True))
                param[0].addChildBlock(x)        
            elif type(i) == Block:
                x = BlockEle([],False)
                self.visit(i,(x,is_in_loop))
                param[0].addChildBlock(x)   
            elif type(i) == If:
                x = BlockEle([],False)
                self.visit(i.thenStmt,(x,is_in_loop))
                param[0].addChildBlock(x)   
                if  type(i.elseStmt) != None: 
                    x2 = BlockEle([],False)
                    self.visit(i.elseStmt,(x2,is_in_loop))
                    param[0].addChildBlock(x2)
    
    def visitFor(self, ast:For, param:tuple[BlockEle,bool]):
        param[0].addvar(MemVar(ast.id.name,IntType(),False))
        self.visit(ast.loop,param)

    

class StaticChecker(BaseVisitor):
    
    global_class:List[ClassSymbol] = []
    global_att:List[VarSymbol] = []
    global_method:List[MethodSymbol] = []
    classDictionary:dict[str,dict] = None
            
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        t = VariableLoad(self.ast)
        t.check()
        for i in t.global_envi:
            if type(i) == ClassSymbol:
                StaticChecker.global_class.append(i)
            elif type(i) == MethodSymbol:
                StaticChecker.global_method.append(i)
            else:
                StaticChecker.global_att.append(i)
        StaticChecker.classDictionary = t.classDictionary
        return self.visit(self.ast,[])

    def visitProgram(self,ast:Program, glob_env): 
        # c = glob_env + scope [[]]
        for i in ast.decl:
            self.visit(i,[])
        return 'a'
                        
    def visitClassDecl(self, ast:ClassDecl, param:list):
        for i in ast.memlist:
            if type(i) == AttributeDecl:
                self.visit(i,ast.classname.name)
            else: self.visit(i,ast.classname.name)

    def visitAttributeDecl(self, ast:AttributeDecl, classname):
        # vi la attribute nen param duoc truyen vao la rong (tam nay k phai local dau bro, phai la this.x)
        if type(ast.decl) == ConstDecl:
            decl:ConstDecl = ast.decl
            typeVar = type(decl.constType)
            if (typeVar == VoidType):
                raise TypeMismatchInConstant(decl)
            if decl.value == None:
                raise IllegalConstantExpression(None)
            new_order = {'local_id':[],'scope': Class,'type':Constant,'value':decl,'this':classname}
            rhs = self.visit(decl.value,new_order)
            if not UsefulTool.validConvertType(typeVar,rhs,StaticChecker.classDictionary):
                raise TypeMismatchInConstant(decl)
            # if ((typeVar == IntType) and type(x) != IntType) or ((typeVar == BoolType) and type(x) != BoolType):
            #     raise TypeMismatchInConstant(decl)
            # elif (typeVar == FloatType) and type(x) not in [IntType,FloatType]:
            #     raise TypeMismatchInConstant(decl)
            # elif (typeVar == ClassType) and (typeVar.classname.name != x.classname.name):
            #         raise TypeMismatchInConstant(decl)
            # elif ((typeVar == ArrayType) and type(x) != ArrayType):
            #     raise TypeMismatchInConstant(decl)
            # elif ((typeVar == ArrayType) and type(x) == ArrayType):
            #     if type(typeVar.eleType) != type(x.eletype):
            #         raise TypeMismatchInConstant(ast)
        else:
            new_order = {'local_id':[],'scope': Class,'type':Attribute,'value':ast.decl,'this':classname}
            if ast.decl.varInit: self.visit(ast.decl.varInit,new_order)
    
    def visitMethodDecl(self, ast:MethodDecl, classname):
        suspect = None
        if type(ast.kind) == Static:
            for i in StaticChecker.global_method:
                if (i.name == ast.name.name) and (i.eleparent == classname):
                    suspect:MethodSymbol = i
                    break
            new_order = {'local_id':[suspect.params],'scope':Method,'type':Method,'value':suspect,'this':classname}
            self.visit(ast.body,new_order)
        elif type(ast.kind) == Instance:
            dictOfClass = StaticChecker.classDictionary[classname]
            for i in dictOfClass['method']:
                if(i.name == ast.name.name):
                    suspect:MemMethod = i
                    break
            if suspect == None:
                UsefulTool.inspectError(ast)
            new_order = {'local_id':[suspect.params],'scope':Method,'type':Method,'value':suspect,'this':classname}
            self.visit(ast.body,new_order)
    
    def visitBlock(self, ast:Block, param):
        if param['type'] == Method:
            current_scope:List[List[MemVar]] = copy.deepcopy(param['local_id'])
            block:BlockEle = param['value'].block
            method = param['value']
            for i in ast.decl:
                if type(i) == VarDecl:
                    new_order = {'local_id':current_scope,'scope':param['scope'],'type':Variable,'value':i,'this':param['this']}
                    self.visit(i,new_order)
                    current_scope[0].append(block.getVar(i.variable.name))
                elif type(i) == ConstDecl:
                    new_order = {'local_id':current_scope,'scope':param['scope'],'type':Constant,'value':i,'this':param['this']}
                    self.visit(i,new_order)
                    current_scope[0].append(block.getVar(i.constant.name))
            count = 0
            for i in ast.stmt:
                if type(i) == Assign:
                    self.visit(i, {'local_id':[block.listVarInBlock],'this':param['this']})
                elif type(i) in [Break,Continue]:
                    raise MustInLoop(i)
                elif type(i) == Return:
                    self.visit(i,{'local_id':[block.listVarInBlock],'this':param['this'],'method':method})
                elif type(i) == Block:
                    count+= 1
                    new_order = {'local_id':[block.listVarInBlock],'scope':Block,'type':Block,'value':block.getBlockChildNumber(count),'this':param['this'],'method':method}
                    self.visit(i,new_order)
                elif type(i) == For:
                    change = False
                    if type(i.loop) == Block:
                        change = True
                        count+=1
                    new_order = {'local_id':[block.listVarInBlock],'scope':Block,'type':Block,'value':block.getBlockChildNumber(count) if change else block,'this':param['this'],'method':method}
                    expr1 = self.visit(i.expr1,new_order)
                    expr2 = self.visit(i.expr2,new_order)
                    if (type(expr1) != IntType) or (type(expr2) != IntType):
                        raise TypeMismatchInStatement(i)
                    self.visit(i,new_order)
                elif type(i) == If:
                    new_order = {'local_id':[block.listVarInBlock],'scope':Block,'type':Block,'value':block, 'this':param['this'],'method':method}
                    expr = self.visit(i.expr,new_order)
                    if type(expr) != BoolType:
                        raise TypeMismatchInStatement(i)
                    count+=1
                    new_order['value'] = block.getBlockChildNumber(count)
                    self.visit(i.thenStmt,new_order)
                    if i.elseStmt != None:
                        count+=1
                        new_order['value'] = block.getBlockChildNumber(count)
                        self.visit(i.elseStmt,new_order)
                elif type(i) == CallStmt:
                    new_order = {'local_id':[block.listVarInBlock],'this':param['this']}
                    self.visit(i,new_order)
        elif param['type'] == Block:
            current_scope:List[List[MemVar]] = [[]] + param['local_id']
            block:BlockEle = param['value']
            method =  param['method']
            for i in ast.decl:
                if type(i) == VarDecl:
                    current_scope[0].append(block.getVar(i.variable.name))
                elif type(i) == ConstDecl:
                    new_order = {'local_id':current_scope,'scope':Block,'type':Constant,'this':param['this']}
                    self.visit(i,new_order)
                    current_scope[0].append(block.getVar(i.constant.name))
            count = 0
            for i in ast.stmt:
                if type(i) == Assign:
                    self.visit(i, {'local_id':current_scope,'this':param['this']})
                elif type(i) in [Break,Continue] and not block.isLoop:
                    raise MustInLoop(i)
                elif type(i) == Return:
                    self.visit(i,{'local_id':current_scope,'this':param['this'],'method':method})
                elif type(i) == Block:
                    count+= 1
                    new_order = {'local_id':current_scope,'scope':Block,'type':Block,'value':block.getBlockChildNumber(count),'this':param['this'],'method':method}
                    self.visit(i,new_order)
                elif type(i) == For:
                    count+=1
                    new_order = {'local_id':current_scope,'scope':Block,'type':Block,'value':block.getBlockChildNumber(count) ,'this':param['this'],'method':method}
                    expr1 = self.visit(i.expr1,new_order)
                    expr2 = self.visit(i.expr2,new_order)
                    if (type(expr1) != IntType) or (type(expr2) != IntType):
                        raise TypeMismatchInStatement(i)
                    self.visit(i,new_order)
                elif type(i) == If:
                    new_order = {'local_id':current_scope,'scope':Block,'type':Block,'value':block, 'this':param['this'],'method':method}
                    expr = self.visit(i.expr,new_order)
                    if type(expr) != BoolType:
                        raise TypeMismatchInStatement(i)
                    count+=1
                    new_order['value'] = block.getBlockChildNumber(count)
                    self.visit(i.thenStmt,new_order)
                    if i.elseStmt != None:
                        count+=1
                        new_order['value'] = block.getBlockChildNumber(count)
                        self.visit(i.elseStmt,new_order)
                elif type(i) == CallStmt:
                    new_order = {'local_id':current_scope,'this':param['this']}
                    self.visit(i,new_order)

    def visitConstDecl(self, ast:ConstDecl, param:dict):
        # param =  {'local_id':current_scope,'scope':param['scope'],'value':ConstDecl,'this':param['this']}
        # pass xuong duoi cai nay chi con instance declare trong method voi scope
        # dont add anything to param
        new_order =  {'local_id':param['local_id'],'scope':param['scope'],'type':Constant,'value':ast,'this':param['this']}
        typeVar = ast.constType
        if (typeVar == VoidType):
                raise TypeMismatchInConstant(ast)
        if ast.value == None:
            raise IllegalConstantExpression(None)
        rhs = self.visit(ast.value,new_order)
        if not UsefulTool.validConvertType(typeVar,rhs,StaticChecker.classDictionary):
            raise TypeMismatchInConstant(ast)    

    def visitFor(self, ast:For, param):
        # param: {'local_id':List[List[Memvar]],'scope':Blocl,'type':Block,'value':block, 'this':param['this'],'method':Method check return : keep it safe}
        current_scope = [param['value'].listVarInBlock] + param['local_id']
        new_order = {'local_id':current_scope,'scope':Block,'type':Block,'value':param['value'] ,'this':param['this'],'method':param['method']}
        self.visit(ast.loop,new_order)
    
    
    def visitReturn(self, ast:Return, param):
        # param {'local_id':current_scope,'this':param['this'],'method':method})
        return_type = param['method'].rettype
        new_order = {'local_id':param['local_id'],'scope':Method,'type':Return,'value':ast,'this':param['this']}
        x = self.visit(ast.expr,new_order)
        if type(return_type) != type(x):
            raise TypeMismatchInStatement(ast)
    
    def visitAssign(self, ast:Assign, param):
        # param {'local_id':current_scope,'this':param['this']}
        new_order = {'local_id':param['local_id'],'scope':Method,'type':Assign,'value':ast,'this':param['this']}
        lhs = self.visit(ast.lhs,new_order)
        rhs = self.visit(ast.exp,new_order)
        if not UsefulTool.validConvertType(lhs,rhs,StaticChecker.classDictionary):
            raise TypeMismatchInStatement(ast)
        
    
    def visitCallStmt(self, ast:CallStmt, param):
        # param {'local_id':current_scope,'this':param['this']}
        new_order = {'local_id':param['local_id'],'scope':Method,'type':CallStmt,'value':ast,'this':param['this']}
        if type(ast.obj) == Id:
            found = None
            for i in new_order['local_id']:
                for j in i:
                    if j.name == ast.obj.name: 
                        found = j
                        break
                if found != None:
                    if type(found.type) != ClassType:
                        raise TypeMismatchInStatement(ast)
                    for classSym in StaticChecker.global_class:
                        if classSym.name == found.type.classname.name:
                            if ast.method.name in classSym.theName['method'] and ast.method.name not in StaticChecker.classDictionary[classSym.name]['method']:
                                raise IllegalMemberAccess(ast)
                            elif ast.method.name not in classSym.theName['method']:
                                raise Undeclared(Method(),ast.method.name)
                            break
                    method:MemMethod = UsefulTool.getMethod(StaticChecker.classDictionary[classSym.name],ast.method.name)
                    if type(method.rettype) != VoidType:
                        raise TypeMismatchInStatement(ast)
                    if len(method.params) != len(ast.param):
                        raise TypeMismatchInStatement(ast)
                    for indexer in range(0,len(ast.param)):
                        rhs = self.visit(ast.param[indexer],new_order)
                        if not UsefulTool.validConvertType(method.params[indexer].type,rhs,StaticChecker.classDictionary):
                            raise TypeMismatchInStatement(ast)
            if (found == None):
                if ast.obj.name not in StaticChecker.classDictionary:
                    raise Undeclared(Identifier(),ast.method.name)
                else:
                    if (ast.obj.name,ast.method.name) not in StaticChecker.global_method:
                        if ast.method.name in StaticChecker.classDictionary[ast.obj.name]['method']:
                            raise IllegalMemberAccess(ast)
                        else:
                            for i in StaticChecker.global_method:
                                if (i.name == ast.method.name) and (i.eleparent == ast.obj.name):
                                    i:MethodSymbol
                                    if type(i.rettype) != VoidType:
                                        raise TypeMismatchInStatement(ast)
                                    if len(i.params) != len(ast.param):
                                        raise TypeMismatchInStatement(ast)
                                    for indexer in range(0,len(ast.param)):
                                        rhs = self.visit(ast.param[indexer],new_order)
                                        if not UsefulTool.validConvertType(i.params[indexer].type,rhs,StaticChecker.classDictionary):
                                            raise TypeMismatchInStatement(ast)
                                    break
                            # check param
                            
                    #search for static class
        else:
            class_search = self.visit(ast.obj,new_order)
            if type(class_search) != ClassType:
                raise TypeMismatchInStatement(ast)
            for classSym in StaticChecker.global_class:
                if classSym.name == class_search.classname.name:
                    if ast.method.name in classSym.theName['method'] and ast.method.name not in StaticChecker.classDictionary[classSym.name]['method']:
                        raise IllegalMemberAccess(ast)
                    elif ast.method.name not in classSym.theName['method']:
                        raise Undeclared(Method(),ast.method.name)
                    break
            method:MemMethod = UsefulTool.getMethod(StaticChecker.classDictionary[classSym.name],ast.method.name)
            if type(method.rettype) != VoidType:
                raise TypeMismatchInStatement(ast)
            if len(method.params) != len(ast.param):
                raise TypeMismatchInStatement(ast)
            for indexer in range(0,len(ast.param)):
                rhs = self.visit(ast.param[indexer],new_order)
                if not UsefulTool.validConvertType(method.params[indexer].type,rhs,StaticChecker.classDictionary):
                    raise TypeMismatchInStatement(ast)
        


    # From now on, its expression
    
    def visitBinaryOp(self, ast:BinaryOp, param):
        leftExp = self.visit(ast.left,param)
        rightExp = self.visit(ast.right,param)
        if ast.op in ['&&', '||']:
            if type(leftExp) != BoolType: 
                raise TypeMismatchInExpression(ast)
            if type(rightExp) != BoolType: 
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ['==','!=']:
            if ((type(leftExp) == BoolType) and (type(rightExp) != BoolType)) or ((type(leftExp) != BoolType) and (type(rightExp) == BoolType)): 
                raise TypeMismatchInExpression(ast)
            if ((type(leftExp) == IntType) and (type(rightExp) != IntType)) or ((type(leftExp) != IntType) and (type(rightExp) == IntType)): 
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ['>','<','>=','<=']:
            if type(leftExp) not in [FloatType,IntType]: 
                raise TypeMismatchInExpression(ast)
            if type(rightExp) not in [FloatType,IntType]: 
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op in ['\\','%']:
            if type(leftExp) != IntType: 
                raise TypeMismatchInExpression(ast)
            if type(rightExp) != IntType: 
                raise TypeMismatchInExpression(ast)
            return IntType()
        if ast.op in ['+','-','*','/']:
            if (type(leftExp) not in [IntType,FloatType]) or (type(rightExp) not in [IntType,FloatType]):
                raise TypeMismatchInExpression(ast)
            if ast.op == '/': return FloatType()
            if type(leftExp) == type(rightExp):
                return leftExp
            return FloatType()
        if ast.op == '^':
            if type(leftExp) != StringType: 
                raise TypeMismatchInExpression(ast)
            if type(rightExp) != StringType: 
                raise TypeMismatchInExpression(ast)
            return StringType()
    
    def visitUnaryOp(self, ast:UnaryOp, param):
        exp = self.visit(ast.body,param)
        if ast.op == '!':
            pass
        return None
    
    def visitCallExpr(self, ast, c): 
        return None
    
    def visitNewExpr(self, ast, param):
        return None
    
    def visitArrayCell(self, ast, param):
        return None
    
    def visitFieldAccess(self, ast, param):
        return None
    
    def visitId(self, ast:Id, param):
        return ast.name


    def visitArrayLiteral(self, ast:ArrayLiteral, param):
        if type(ast.value[0]) == ArrayLiteral:
            raise IllegalArrayLiteral(ast)
        first_ele_type = self.visit(ast.value[0],None)
        count = 0
        for i in ast.value:
            x = self.visit(i,None)
            if (type(x) != type(first_ele_type)) or (type(i)==ArrayLiteral):
                raise IllegalArrayLiteral(ast)
            count+=1
        return ArrayType(size=count,eleType=first_ele_type)

    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()
    
    def visitNullLiteral(self, ast, param):
        return VoidType()
    
    def visitSelfLiteral(self, ast, className):
        return ClassType(Id(className))



