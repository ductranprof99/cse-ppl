grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : class_declare EOF ;


// declarations

class_declare: CLASS ID (EXTENDS ID)? CURLY_OPEN members* CURLY_CLOSE;

members: attribute_declare | method_declare | constructor_declare;



attribute_declare: field type_attribute var_declare ( COMMA var_declare )* SEMI;

field: | STATIC | FINAL | STATIC FINAL | FINAL STATIC;

method_declare: STATIC ? return_type ROUND_OPEN list_params ROUND_CLOSE block_statement;

constructor_declare: ID ROUND_OPEN list_params ROUND_CLOSE  block_statement;

var_declare: ID ( ASSIGN exp) ? ;





// list parameter of method and constructor

list_params: | parameter (SEMI parameter)* ;

parameter: parameter_type ID (COMMA ID)*;

parameter_type: (primitive_type ~VOID) | array_type | class_type ;





//type

return_type: primitive_type | array_type | class_type;

type_attribute: class_type| array_type | primitive_type;

class_type: ID;

array_type: (primitive_type ~VOID) SQUARE_OPEN INTEGER_LIT SQUARE_CLOSE ;

primitive_type: INTEGER | FLOAT | BOOLEAN | STRING | VOID ;






// statements

block_statement: CURLY_CLOSE block_var_declare* statement* CURLY_CLOSE;

block_var_declare: (FINAL)? type_attribute var_declare ( COMMA var_declare )* SEMI;

//------------------------------------------------

statement:  (assignment_satement
         |  if_statement
         |  for_statement
         |  break_statement
         |  continue_statement
         |  return_statement
         |  method_invo_statement
         ) SEMI;  // end with semicolon

// ------- assignment -------------

assignment_satement: lhs ASSIGN_EQ exp;

lhs: ID
   | operands DOT_OP ID
   | operands index_represent
   ;



if_statement: IF bool_exp THEN statement (ELSE statement)? ;

for_statement: FOR   ASSIGN_EQ int_exp (TO | DOWNTO) int_exp DO loop_block_statement;

loop_block_statement: CURLY_OPEN statement+ CURLY_CLOSE
                    | statement;

break_statement: BREAK ;
continue_statement: CONTINUE;
return_statement: RETURN return_exp ;

method_invo_statement: prefix_method_invo ID DOT_OP ID list_args_wrapped ;

prefix_method_invo: | ID
                    | prefix_method_invo DOT_OP ID list_args_wrapped
                    | ROUND_OPEN exp ROUND_CLOSE
                    | prefix_method_invo index_represent
                    | THIS
                    ;
// expressions

bool_exp: exp;

int_exp: exp;

return_exp: exp;

exp: exp1 (LT | GT | LTE | GTE | EQ | NEQ) exp1 | exp1;

exp1: exp2 (AND | OR | ADD | SUB) exp1 | exp2;

exp2: exp3 ( MUL | FLOAT_DIV | INT_DIV | MOD | CONCAT ) exp2 | exp3;

exp3: (NOT | ADD | SUB) exp3 | operands;


operands: literals
        | ID
        | operands DOT_OP ID
        | operands DOT_OP ID list_args_wrapped
        | ROUND_OPEN exp ROUND_CLOSE
        | operands index_represent
        | THIS
        | obj_create
        ;

index_represent: SQUARE_OPEN exp SQUARE_CLOSE;

obj_create: NEW ID list_args_wrapped;

list_args_wrapped:  ROUND_OPEN (list_exps_as_args | ) ROUND_CLOSE;

list_exps_as_args: exp ( COMMA exp )*;







// keywords tokens
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INTEGER: 'int';
STRING: 'string';
THEN: 'then' ;
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

// operator

ADD: '+';
SUB: '-';
MUL: '*';
FLOAT_DIV: '/';
INT_DIV: '\\';
MOD: '%';
ASSIGN: '=';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
EQ : '==' ;
LT : '<' ;
GT : '>' ;
NOT: '!';
AND: '&&';
OR: '||';
CONCAT: '^';
DOT_OP: '.';
fragment DOT: '.';
NEW: 'new';
COLON: ':';
ASSIGN_EQ: ':=';

// separator and parenthesis
CURLY_OPEN: '{';
CURLY_CLOSE: '}';
ROUND_OPEN: '(';
ROUND_CLOSE: ')';
SQUARE_OPEN:'[';
SQUARE_CLOSE: ']';
SEMI: ';';
COMMA: ',';


// another skip-error tokens and literals
literals: INTEGER_LIT | FLOAT_LIT | STRING_LIT | boolean_literal | array_literal ;

boolean_literal: TRUE | FALSE ;

array_literal: CURLY_OPEN FLOAT_LIT (COMMA FLOAT_LIT)*
             | CURLY_OPEN INTEGER_LIT (COMMA INTEGER_LIT)*
             | CURLY_OPEN STRING_LIT (COMMA STRING_LIT)*
             | CURLY_OPEN boolean_literal (COMMA boolean_literal)*
             ;
FLOAT_LIT : DIGIT+ DOT (DIGIT | EXPONENT)*
	      | DIGIT* DOT DIGIT+ EXPONENT?
	      | DIGIT+ EXPONENT
	      ;
STRING_LIT: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;
INTEGER_LIT: DIGIT+;
ID: [_a-zA-Z][_a-zA-Z0-9]* ;




COMMENT: (MUL_COMMENT|ONE_COMMENT) -> skip;
WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;


//Fragment
fragment EXPONENT: [eE] SUB? DIGIT+ ;
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

fragment MUL_COMMENT: '/*' (.)*? '*/';
fragment ONE_COMMENT: '#' ~[\r\n]*;
fragment UNDERSCORE: '_';

fragment DIGIT: [0-9] ;
