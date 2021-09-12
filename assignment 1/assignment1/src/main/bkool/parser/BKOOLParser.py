# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\6\2^\n\2\r\2\16\2_\3\2\3\2\3\3\3\3\3\3\3\3\5\3h\n\3")
        buf.write("\3\3\3\3\7\3l\n\3\f\3\16\3o\13\3\3\3\3\3\3\4\3\4\3\4\5")
        buf.write("\4v\n\4\3\5\5\5y\n\5\3\5\3\5\3\5\3\5\7\5\177\n\5\f\5\16")
        buf.write("\5\u0082\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\7\5\7\u008f\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00a1\n\t\3\n\3\n")
        buf.write("\3\n\3\n\7\n\u00a7\n\n\f\n\16\n\u00aa\13\n\5\n\u00ac\n")
        buf.write("\n\3\13\3\13\3\13\3\13\7\13\u00b2\n\13\f\13\16\13\u00b5")
        buf.write("\13\13\3\f\3\f\3\r\3\r\3\r\5\r\u00bc\n\r\3\16\3\16\3\16")
        buf.write("\5\16\u00c1\n\16\3\17\3\17\5\17\u00c5\n\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\7\22\u00d1\n\22")
        buf.write("\f\22\16\22\u00d4\13\22\3\22\7\22\u00d7\n\22\f\22\16\22")
        buf.write("\u00da\13\22\3\22\3\22\3\23\5\23\u00df\n\23\3\23\3\23")
        buf.write("\3\23\3\23\7\23\u00e5\n\23\f\23\16\23\u00e8\13\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fe\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u010c\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0115\n\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u011d\n\27\f\27\16\27\u0120\13\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u0128\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\32\3\32\6\32\u0135\n\32\r\32")
        buf.write("\16\32\u0136\3\32\3\32\3\32\5\32\u013c\n\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0159\n\36\3\36\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u016a\n\"")
        buf.write("\3#\3#\3#\3#\3#\5#\u0171\n#\3$\3$\3$\3$\3$\5$\u0178\n")
        buf.write("$\3%\3%\3%\5%\u017d\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u0189\n&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0194\n&\f&\16")
        buf.write("&\u0197\13&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\5)\u01a4")
        buf.write("\n)\3)\3)\3*\3*\3*\7*\u01ab\n*\f*\16*\u01ae\13*\3+\3+")
        buf.write("\5+\u01b2\n+\3,\3,\3-\3-\3-\3-\7-\u01ba\n-\f-\16-\u01bd")
        buf.write("\13-\3-\3-\3.\3.\3.\3.\5.\u01c5\n.\3.\2\4,J/\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\2\t\6\2\3\3\n\n\f\r\23\23\3\2\30\31\3")
        buf.write("\2!&\4\2\32\33()\4\2\34\37**\4\2\32\33\'\'\3\2\21\22\2")
        buf.write("\u01dc\2]\3\2\2\2\4c\3\2\2\2\6u\3\2\2\2\bx\3\2\2\2\n\u008b")
        buf.write("\3\2\2\2\f\u008e\3\2\2\2\16\u0097\3\2\2\2\20\u009d\3\2")
        buf.write("\2\2\22\u00ab\3\2\2\2\24\u00ad\3\2\2\2\26\u00b6\3\2\2")
        buf.write("\2\30\u00bb\3\2\2\2\32\u00c0\3\2\2\2\34\u00c4\3\2\2\2")
        buf.write("\36\u00ca\3\2\2\2 \u00cc\3\2\2\2\"\u00ce\3\2\2\2$\u00de")
        buf.write("\3\2\2\2&\u00fd\3\2\2\2(\u00ff\3\2\2\2*\u010b\3\2\2\2")
        buf.write(",\u0114\3\2\2\2.\u0121\3\2\2\2\60\u0129\3\2\2\2\62\u013b")
        buf.write("\3\2\2\2\64\u013d\3\2\2\2\66\u013f\3\2\2\28\u0141\3\2")
        buf.write("\2\2:\u0158\3\2\2\2<\u015e\3\2\2\2>\u0160\3\2\2\2@\u0162")
        buf.write("\3\2\2\2B\u0169\3\2\2\2D\u0170\3\2\2\2F\u0177\3\2\2\2")
        buf.write("H\u017c\3\2\2\2J\u0188\3\2\2\2L\u0198\3\2\2\2N\u019c\3")
        buf.write("\2\2\2P\u01a0\3\2\2\2R\u01a7\3\2\2\2T\u01b1\3\2\2\2V\u01b3")
        buf.write("\3\2\2\2X\u01b5\3\2\2\2Z\u01c4\3\2\2\2\\^\5\4\3\2]\\\3")
        buf.write("\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\2\2")
        buf.write("\3b\3\3\2\2\2cd\7\5\2\2dg\7:\2\2ef\7\t\2\2fh\7:\2\2ge")
        buf.write("\3\2\2\2gh\3\2\2\2hi\3\2\2\2im\7/\2\2jl\5\6\4\2kj\3\2")
        buf.write("\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2")
        buf.write("pq\7\60\2\2q\5\3\2\2\2rv\5\b\5\2sv\5\f\7\2tv\5\16\b\2")
        buf.write("ur\3\2\2\2us\3\2\2\2ut\3\2\2\2v\7\3\2\2\2wy\5\n\6\2xw")
        buf.write("\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\5\32\16\2{\u0080\5\20\t")
        buf.write("\2|}\7\66\2\2}\177\5\20\t\2~|\3\2\2\2\177\u0082\3\2\2")
        buf.write("\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2")
        buf.write("\2\2\u0082\u0080\3\2\2\2\u0083\u0084\7\65\2\2\u0084\t")
        buf.write("\3\2\2\2\u0085\u008c\7\27\2\2\u0086\u008c\7\26\2\2\u0087")
        buf.write("\u0088\7\27\2\2\u0088\u008c\7\26\2\2\u0089\u008a\7\26")
        buf.write("\2\2\u008a\u008c\7\27\2\2\u008b\u0085\3\2\2\2\u008b\u0086")
        buf.write("\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0089\3\2\2\2\u008c")
        buf.write("\13\3\2\2\2\u008d\u008f\7\27\2\2\u008e\u008d\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\5\30\r")
        buf.write("\2\u0091\u0092\7:\2\2\u0092\u0093\7\61\2\2\u0093\u0094")
        buf.write("\5\22\n\2\u0094\u0095\7\62\2\2\u0095\u0096\5\"\22\2\u0096")
        buf.write("\r\3\2\2\2\u0097\u0098\7:\2\2\u0098\u0099\7\61\2\2\u0099")
        buf.write("\u009a\5\22\n\2\u009a\u009b\7\62\2\2\u009b\u009c\5\"\22")
        buf.write("\2\u009c\17\3\2\2\2\u009d\u00a0\7:\2\2\u009e\u009f\7 ")
        buf.write("\2\2\u009f\u00a1\5B\"\2\u00a0\u009e\3\2\2\2\u00a0\u00a1")
        buf.write("\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00ac\3\2\2\2\u00a3\u00a8")
        buf.write("\5\24\13\2\u00a4\u00a5\7\65\2\2\u00a5\u00a7\5\24\13\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00a2\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ac")
        buf.write("\23\3\2\2\2\u00ad\u00ae\5\26\f\2\u00ae\u00b3\7:\2\2\u00af")
        buf.write("\u00b0\7\66\2\2\u00b0\u00b2\7:\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\25\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\5\32\16\2\u00b7\27\3\2\2\2\u00b8\u00bc\5 \21\2\u00b9")
        buf.write("\u00bc\5\36\20\2\u00ba\u00bc\5\34\17\2\u00bb\u00b8\3\2")
        buf.write("\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\31")
        buf.write("\3\2\2\2\u00bd\u00c1\5\36\20\2\u00be\u00c1\5 \21\2\u00bf")
        buf.write("\u00c1\5\34\17\2\u00c0\u00bd\3\2\2\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c0\u00bf\3\2\2\2\u00c1\33\3\2\2\2\u00c2\u00c5\5")
        buf.write(" \21\2\u00c3\u00c5\5\36\20\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\7\63\2")
        buf.write("\2\u00c7\u00c8\78\2\2\u00c8\u00c9\7\64\2\2\u00c9\35\3")
        buf.write("\2\2\2\u00ca\u00cb\7:\2\2\u00cb\37\3\2\2\2\u00cc\u00cd")
        buf.write("\t\2\2\2\u00cd!\3\2\2\2\u00ce\u00d2\7/\2\2\u00cf\u00d1")
        buf.write("\5$\23\2\u00d0\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d8\3\2\2\2")
        buf.write("\u00d4\u00d2\3\2\2\2\u00d5\u00d7\5&\24\2\u00d6\u00d5\3")
        buf.write("\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write("\u00dc\7\60\2\2\u00dc#\3\2\2\2\u00dd\u00df\7\26\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\5\32\16\2\u00e1\u00e6\5\20\t\2\u00e2\u00e3")
        buf.write("\7\66\2\2\u00e3\u00e5\5\20\t\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7")
        buf.write("\65\2\2\u00ea%\3\2\2\2\u00eb\u00fe\5.\30\2\u00ec\u00fe")
        buf.write("\5\60\31\2\u00ed\u00ee\5\64\33\2\u00ee\u00ef\7\65\2\2")
        buf.write("\u00ef\u00fe\3\2\2\2\u00f0\u00f1\5\66\34\2\u00f1\u00f2")
        buf.write("\7\65\2\2\u00f2\u00fe\3\2\2\2\u00f3\u00f4\58\35\2\u00f4")
        buf.write("\u00f5\7\65\2\2\u00f5\u00fe\3\2\2\2\u00f6\u00f7\5:\36")
        buf.write("\2\u00f7\u00f8\7\65\2\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa")
        buf.write("\5(\25\2\u00fa\u00fb\7\65\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fe\5\"\22\2\u00fd\u00eb\3\2\2\2\u00fd\u00ec\3\2\2")
        buf.write("\2\u00fd\u00ed\3\2\2\2\u00fd\u00f0\3\2\2\2\u00fd\u00f3")
        buf.write("\3\2\2\2\u00fd\u00f6\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fe\'\3\2\2\2\u00ff\u0100\5*\26\2\u0100")
        buf.write("\u0101\7.\2\2\u0101\u0102\5B\"\2\u0102)\3\2\2\2\u0103")
        buf.write("\u010c\7:\2\2\u0104\u0105\5J&\2\u0105\u0106\5L\'\2\u0106")
        buf.write("\u010c\3\2\2\2\u0107\u0108\5,\27\2\u0108\u0109\7+\2\2")
        buf.write("\u0109\u010a\7:\2\2\u010a\u010c\3\2\2\2\u010b\u0103\3")
        buf.write("\2\2\2\u010b\u0104\3\2\2\2\u010b\u0107\3\2\2\2\u010c+")
        buf.write("\3\2\2\2\u010d\u0115\b\27\1\2\u010e\u0115\7:\2\2\u010f")
        buf.write("\u0110\7\61\2\2\u0110\u0111\5B\"\2\u0111\u0112\7\62\2")
        buf.write("\2\u0112\u0115\3\2\2\2\u0113\u0115\7\25\2\2\u0114\u010d")
        buf.write("\3\2\2\2\u0114\u010e\3\2\2\2\u0114\u010f\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\u011e\3\2\2\2\u0116\u0117\f\6\2\2")
        buf.write("\u0117\u0118\7+\2\2\u0118\u0119\7:\2\2\u0119\u011d\5P")
        buf.write(")\2\u011a\u011b\f\4\2\2\u011b\u011d\5L\'\2\u011c\u0116")
        buf.write("\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u0120\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f-\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0121\u0122\7\13\2\2\u0122\u0123\5<\37")
        buf.write("\2\u0123\u0124\7\16\2\2\u0124\u0127\5&\24\2\u0125\u0126")
        buf.write("\7\b\2\2\u0126\u0128\5&\24\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128/\3\2\2\2\u0129\u012a\7\17\2\2\u012a")
        buf.write("\u012b\7:\2\2\u012b\u012c\7.\2\2\u012c\u012d\5> \2\u012d")
        buf.write("\u012e\t\3\2\2\u012e\u012f\5> \2\u012f\u0130\7\7\2\2\u0130")
        buf.write("\u0131\5\62\32\2\u0131\61\3\2\2\2\u0132\u0134\7/\2\2\u0133")
        buf.write("\u0135\5&\24\2\u0134\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3")
        buf.write("\2\2\2\u0138\u0139\7\60\2\2\u0139\u013c\3\2\2\2\u013a")
        buf.write("\u013c\5&\24\2\u013b\u0132\3\2\2\2\u013b\u013a\3\2\2\2")
        buf.write("\u013c\63\3\2\2\2\u013d\u013e\7\4\2\2\u013e\65\3\2\2\2")
        buf.write("\u013f\u0140\7\6\2\2\u0140\67\3\2\2\2\u0141\u0142\7\20")
        buf.write("\2\2\u0142\u0143\5@!\2\u01439\3\2\2\2\u0144\u0159\5T+")
        buf.write("\2\u0145\u0159\7:\2\2\u0146\u0147\5J&\2\u0147\u0148\7")
        buf.write("+\2\2\u0148\u0149\7:\2\2\u0149\u0159\3\2\2\2\u014a\u014b")
        buf.write("\5J&\2\u014b\u014c\7+\2\2\u014c\u014d\7:\2\2\u014d\u014e")
        buf.write("\5P)\2\u014e\u0159\3\2\2\2\u014f\u0150\7\61\2\2\u0150")
        buf.write("\u0151\5B\"\2\u0151\u0152\7\62\2\2\u0152\u0159\3\2\2\2")
        buf.write("\u0153\u0154\5J&\2\u0154\u0155\5L\'\2\u0155\u0159\3\2")
        buf.write("\2\2\u0156\u0159\7\25\2\2\u0157\u0159\7\24\2\2\u0158\u0144")
        buf.write("\3\2\2\2\u0158\u0145\3\2\2\2\u0158\u0146\3\2\2\2\u0158")
        buf.write("\u014a\3\2\2\2\u0158\u014f\3\2\2\2\u0158\u0153\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015a\3")
        buf.write("\2\2\2\u015a\u015b\7+\2\2\u015b\u015c\7:\2\2\u015c\u015d")
        buf.write("\5P)\2\u015d;\3\2\2\2\u015e\u015f\5B\"\2\u015f=\3\2\2")
        buf.write("\2\u0160\u0161\5B\"\2\u0161?\3\2\2\2\u0162\u0163\5B\"")
        buf.write("\2\u0163A\3\2\2\2\u0164\u0165\5D#\2\u0165\u0166\t\4\2")
        buf.write("\2\u0166\u0167\5D#\2\u0167\u016a\3\2\2\2\u0168\u016a\5")
        buf.write("D#\2\u0169\u0164\3\2\2\2\u0169\u0168\3\2\2\2\u016aC\3")
        buf.write("\2\2\2\u016b\u016c\5F$\2\u016c\u016d\t\5\2\2\u016d\u016e")
        buf.write("\5D#\2\u016e\u0171\3\2\2\2\u016f\u0171\5F$\2\u0170\u016b")
        buf.write("\3\2\2\2\u0170\u016f\3\2\2\2\u0171E\3\2\2\2\u0172\u0173")
        buf.write("\5H%\2\u0173\u0174\t\6\2\2\u0174\u0175\5F$\2\u0175\u0178")
        buf.write("\3\2\2\2\u0176\u0178\5H%\2\u0177\u0172\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178G\3\2\2\2\u0179\u017a\t\7\2\2\u017a\u017d")
        buf.write("\5H%\2\u017b\u017d\5J&\2\u017c\u0179\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017dI\3\2\2\2\u017e\u017f\b&\1\2\u017f\u0189")
        buf.write("\5T+\2\u0180\u0189\7:\2\2\u0181\u0182\7\61\2\2\u0182\u0183")
        buf.write("\5B\"\2\u0183\u0184\7\62\2\2\u0184\u0189\3\2\2\2\u0185")
        buf.write("\u0189\7\25\2\2\u0186\u0189\5N(\2\u0187\u0189\7\24\2\2")
        buf.write("\u0188\u017e\3\2\2\2\u0188\u0180\3\2\2\2\u0188\u0181\3")
        buf.write("\2\2\2\u0188\u0185\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189\u0195\3\2\2\2\u018a\u018b\f\t\2\2\u018b")
        buf.write("\u0194\5L\'\2\u018c\u018d\f\b\2\2\u018d\u018e\7+\2\2\u018e")
        buf.write("\u0194\7:\2\2\u018f\u0190\f\7\2\2\u0190\u0191\7+\2\2\u0191")
        buf.write("\u0192\7:\2\2\u0192\u0194\5P)\2\u0193\u018a\3\2\2\2\u0193")
        buf.write("\u018c\3\2\2\2\u0193\u018f\3\2\2\2\u0194\u0197\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196K\3\2\2")
        buf.write("\2\u0197\u0195\3\2\2\2\u0198\u0199\7\63\2\2\u0199\u019a")
        buf.write("\5B\"\2\u019a\u019b\7\64\2\2\u019bM\3\2\2\2\u019c\u019d")
        buf.write("\7,\2\2\u019d\u019e\7:\2\2\u019e\u019f\5P)\2\u019fO\3")
        buf.write("\2\2\2\u01a0\u01a3\7\61\2\2\u01a1\u01a4\5R*\2\u01a2\u01a4")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a6\7\62\2\2\u01a6Q\3\2\2\2\u01a7")
        buf.write("\u01ac\5B\"\2\u01a8\u01a9\7\66\2\2\u01a9\u01ab\5B\"\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ad\3\2\2\2\u01adS\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01af\u01b2\5Z.\2\u01b0\u01b2\5X-\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2U\3\2\2\2\u01b3\u01b4")
        buf.write("\t\b\2\2\u01b4W\3\2\2\2\u01b5\u01b6\7/\2\2\u01b6\u01bb")
        buf.write("\5Z.\2\u01b7\u01b8\7\66\2\2\u01b8\u01ba\5Z.\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\7\60\2\2\u01bfY\3\2\2\2\u01c0\u01c5\78\2")
        buf.write("\2\u01c1\u01c5\7\67\2\2\u01c2\u01c5\79\2\2\u01c3\u01c5")
        buf.write("\5V,\2\u01c4\u01c0\3\2\2\2\u01c4\u01c1\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5[\3\2\2\2*_gmux\u0080")
        buf.write("\u008b\u008e\u00a0\u00a8\u00ab\u00b3\u00bb\u00c0\u00c4")
        buf.write("\u00d2\u00d8\u00de\u00e6\u00fd\u010b\u0114\u011c\u011e")
        buf.write("\u0127\u0136\u013b\u0158\u0169\u0170\u0177\u017c\u0188")
        buf.write("\u0193\u0195\u01a3\u01ac\u01b1\u01bb\u01c4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'string'", "'then'", "'for'", "'return'", "'true'", 
                     "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'='", "'<='", "'>='", "'!='", 
                     "'=='", "'<'", "'>'", "'!'", "'&&'", "'||'", "'^'", 
                     "'.'", "'new'", "':'", "':='", "'{'", "'}'", "'('", 
                     "')'", "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INTEGER", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "ADD", "SUB", "MUL", "FLOAT_DIV", "INT_DIV", "MOD", 
                      "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "NOT", 
                      "AND", "OR", "CONCAT", "DOT", "NEW", "COLON", "ASSIGN_EQ", 
                      "CURLY_OPEN", "CURLY_CLOSE", "ROUND_OPEN", "ROUND_CLOSE", 
                      "SQUARE_OPEN", "SQUARE_CLOSE", "SEMI", "COMMA", "FLOAT_LIT", 
                      "INTEGER_LIT", "STRING_LIT", "ID", "COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declare = 1
    RULE_members = 2
    RULE_attribute_declare = 3
    RULE_field = 4
    RULE_method_declare = 5
    RULE_constructor_declare = 6
    RULE_var_declare = 7
    RULE_list_params = 8
    RULE_parameter = 9
    RULE_parameter_type = 10
    RULE_return_type = 11
    RULE_type_attribute = 12
    RULE_array_type = 13
    RULE_class_type = 14
    RULE_primitive_type = 15
    RULE_block_statement = 16
    RULE_local_attribute = 17
    RULE_statement = 18
    RULE_assignment_satement = 19
    RULE_lhs = 20
    RULE_prefix_attribute_invo = 21
    RULE_if_statement = 22
    RULE_for_statement = 23
    RULE_loop_block_statement = 24
    RULE_break_statement = 25
    RULE_continue_statement = 26
    RULE_return_statement = 27
    RULE_method_invo_statement = 28
    RULE_bool_exp = 29
    RULE_int_exp = 30
    RULE_return_exp = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_operands = 36
    RULE_index_represent = 37
    RULE_obj_create = 38
    RULE_list_args_wrapped = 39
    RULE_list_exps_as_args = 40
    RULE_literals = 41
    RULE_boolean_literal = 42
    RULE_array_literal = 43
    RULE_literal_replica = 44

    ruleNames =  [ "program", "class_declare", "members", "attribute_declare", 
                   "field", "method_declare", "constructor_declare", "var_declare", 
                   "list_params", "parameter", "parameter_type", "return_type", 
                   "type_attribute", "array_type", "class_type", "primitive_type", 
                   "block_statement", "local_attribute", "statement", "assignment_satement", 
                   "lhs", "prefix_attribute_invo", "if_statement", "for_statement", 
                   "loop_block_statement", "break_statement", "continue_statement", 
                   "return_statement", "method_invo_statement", "bool_exp", 
                   "int_exp", "return_exp", "exp", "exp1", "exp2", "exp3", 
                   "operands", "index_represent", "obj_create", "list_args_wrapped", 
                   "list_exps_as_args", "literals", "boolean_literal", "array_literal", 
                   "literal_replica" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INTEGER=10
    STRING=11
    THEN=12
    FOR=13
    RETURN=14
    TRUE=15
    FALSE=16
    VOID=17
    NIL=18
    THIS=19
    FINAL=20
    STATIC=21
    TO=22
    DOWNTO=23
    ADD=24
    SUB=25
    MUL=26
    FLOAT_DIV=27
    INT_DIV=28
    MOD=29
    ASSIGN=30
    LTE=31
    GTE=32
    NEQ=33
    EQ=34
    LT=35
    GT=36
    NOT=37
    AND=38
    OR=39
    CONCAT=40
    DOT=41
    NEW=42
    COLON=43
    ASSIGN_EQ=44
    CURLY_OPEN=45
    CURLY_CLOSE=46
    ROUND_OPEN=47
    ROUND_CLOSE=48
    SQUARE_OPEN=49
    SQUARE_CLOSE=50
    SEMI=51
    COMMA=52
    FLOAT_LIT=53
    INTEGER_LIT=54
    STRING_LIT=55
    ID=56
    COMMENT=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declareContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 90
                self.class_declare()
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 95
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def members(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MembersContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MembersContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declare" ):
                return visitor.visitClass_declare(self)
            else:
                return visitor.visitChildren(self)




    def class_declare(self):

        localctx = BKOOLParser.Class_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(BKOOLParser.CLASS)
            self.state = 98
            self.match(BKOOLParser.ID)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 99
                self.match(BKOOLParser.EXTENDS)
                self.state = 100
                self.match(BKOOLParser.ID)


            self.state = 103
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 104
                self.members()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_declareContext,0)


        def method_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declareContext,0)


        def constructor_declare(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembers" ):
                return visitor.visitMembers(self)
            else:
                return visitor.visitChildren(self)




    def members(self):

        localctx = BKOOLParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.attribute_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.method_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.constructor_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def field(self):
            return self.getTypedRuleContext(BKOOLParser.FieldContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_declare" ):
                return visitor.visitAttribute_declare(self)
            else:
                return visitor.visitChildren(self)




    def attribute_declare(self):

        localctx = BKOOLParser.Attribute_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL or _la==BKOOLParser.STATIC:
                self.state = 117
                self.field()


            self.state = 120
            self.type_attribute()
            self.state = 121
            self.var_declare()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 122
                self.match(BKOOLParser.COMMA)
                self.state = 123
                self.var_declare()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = BKOOLParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_field)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(BKOOLParser.STATIC)
                self.state = 134
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(BKOOLParser.FINAL)
                self.state = 136
                self.match(BKOOLParser.STATIC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(BKOOLParser.Return_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def list_params(self):
            return self.getTypedRuleContext(BKOOLParser.List_paramsContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declare" ):
                return visitor.visitMethod_declare(self)
            else:
                return visitor.visitChildren(self)




    def method_declare(self):

        localctx = BKOOLParser.Method_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 139
                self.match(BKOOLParser.STATIC)


            self.state = 142
            self.return_type()
            self.state = 143
            self.match(BKOOLParser.ID)
            self.state = 144
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 145
            self.list_params()
            self.state = 146
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 147
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def list_params(self):
            return self.getTypedRuleContext(BKOOLParser.List_paramsContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_declare" ):
                return visitor.visitConstructor_declare(self)
            else:
                return visitor.visitChildren(self)




    def constructor_declare(self):

        localctx = BKOOLParser.Constructor_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructor_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKOOLParser.ID)
            self.state = 150
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 151
            self.list_params()
            self.state = 152
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 153
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKOOLParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(BKOOLParser.ID)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ASSIGN:
                self.state = 156
                self.match(BKOOLParser.ASSIGN)
                self.state = 157
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParameterContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_params" ):
                return visitor.visitList_params(self)
            else:
                return visitor.visitChildren(self)




    def list_params(self):

        localctx = BKOOLParser.List_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_params)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ROUND_CLOSE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.parameter()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SEMI:
                    self.state = 162
                    self.match(BKOOLParser.SEMI)
                    self.state = 163
                    self.parameter()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_type(self):
            return self.getTypedRuleContext(BKOOLParser.Parameter_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKOOLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.parameter_type()
            self.state = 172
            self.match(BKOOLParser.ID)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 173
                self.match(BKOOLParser.COMMA)
                self.state = 174
                self.match(BKOOLParser.ID)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_type" ):
                return visitor.visitParameter_type(self)
            else:
                return visitor.visitChildren(self)




    def parameter_type(self):

        localctx = BKOOLParser.Parameter_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.type_attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = BKOOLParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_type)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.class_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_type_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_attribute" ):
                return visitor.visitType_attribute(self)
            else:
                return visitor.visitChildren(self)




    def type_attribute(self):

        localctx = BKOOLParser.Type_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_attribute)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.class_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.primitive_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_OPEN(self):
            return self.getToken(BKOOLParser.SQUARE_OPEN, 0)

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def SQUARE_CLOSE(self):
            return self.getToken(BKOOLParser.SQUARE_CLOSE, 0)

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 192
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 193
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 196
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 197
            self.match(BKOOLParser.INTEGER_LIT)
            self.state = 198
            self.match(BKOOLParser.SQUARE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def local_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Local_attributeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Local_attributeContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = BKOOLParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKOOLParser.CURLY_OPEN)

            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.local_attribute() 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)


            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 211
                    self.statement() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 217
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_local_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_attribute" ):
                return visitor.visitLocal_attribute(self)
            else:
                return visitor.visitChildren(self)




    def local_attribute(self):

        localctx = BKOOLParser.Local_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_local_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 219
                self.match(BKOOLParser.FINAL)


            self.state = 222
            self.type_attribute()
            self.state = 223
            self.var_declare()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 224
                self.match(BKOOLParser.COMMA)
                self.state = 225
                self.var_declare()
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def method_invo_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invo_statementContext,0)


        def assignment_satement(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_satementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Block_statementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_statement)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.for_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.break_statement()
                self.state = 236
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.continue_statement()
                self.state = 239
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 241
                self.return_statement()
                self.state = 242
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 244
                self.method_invo_statement()
                self.state = 245
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 247
                self.assignment_satement()
                self.state = 248
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 250
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_satementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN_EQ(self):
            return self.getToken(BKOOLParser.ASSIGN_EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_satement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_satement" ):
                return visitor.visitAssignment_satement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_satement(self):

        localctx = BKOOLParser.Assignment_satementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_satement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.lhs()
            self.state = 254
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 255
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def prefix_attribute_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Prefix_attribute_invoContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.operands(0)
                self.state = 259
                self.index_represent()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.prefix_attribute_invo(0)
                self.state = 262
                self.match(BKOOLParser.DOT)
                self.state = 263
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_attribute_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def prefix_attribute_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Prefix_attribute_invoContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_prefix_attribute_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_attribute_invo" ):
                return visitor.visitPrefix_attribute_invo(self)
            else:
                return visitor.visitChildren(self)



    def prefix_attribute_invo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Prefix_attribute_invoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_prefix_attribute_invo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 268
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 269
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 270
                self.exp()
                self.state = 271
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 4:
                self.state = 273
                self.match(BKOOLParser.THIS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 282
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 276
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 277
                        self.match(BKOOLParser.DOT)
                        self.state = 278
                        self.match(BKOOLParser.ID)
                        self.state = 279
                        self.list_args_wrapped()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 280
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 281
                        self.index_represent()
                        pass

             
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def bool_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_expContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKOOLParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(BKOOLParser.IF)
            self.state = 288
            self.bool_exp()
            self.state = 289
            self.match(BKOOLParser.THEN)
            self.state = 290
            self.statement()
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 291
                self.match(BKOOLParser.ELSE)
                self.state = 292
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN_EQ(self):
            return self.getToken(BKOOLParser.ASSIGN_EQ, 0)

        def int_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Int_expContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Int_expContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def loop_block_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Loop_block_statementContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKOOLParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKOOLParser.FOR)
            self.state = 296
            self.match(BKOOLParser.ID)
            self.state = 297
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 298
            self.int_exp()
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 300
            self.int_exp()
            self.state = 301
            self.match(BKOOLParser.DO)
            self.state = 302
            self.loop_block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_loop_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_block_statement" ):
                return visitor.visitLoop_block_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_block_statement(self):

        localctx = BKOOLParser.Loop_block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_loop_block_statement)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(BKOOLParser.CURLY_OPEN)
                self.state = 306 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 305
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 308 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.state = 310
                self.match(BKOOLParser.CURLY_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKOOLParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKOOLParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKOOLParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(BKOOLParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def return_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Return_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKOOLParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKOOLParser.RETURN)
            self.state = 320
            self.return_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invo_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DOT)
            else:
                return self.getToken(BKOOLParser.DOT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def list_args_wrapped(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.List_args_wrappedContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,i)


        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo_statement" ):
                return visitor.visitMethod_invo_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invo_statement(self):

        localctx = BKOOLParser.Method_invo_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_method_invo_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 322
                self.literals()
                pass

            elif la_ == 2:
                self.state = 323
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 324
                self.operands(0)
                self.state = 325
                self.match(BKOOLParser.DOT)
                self.state = 326
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.state = 328
                self.operands(0)
                self.state = 329
                self.match(BKOOLParser.DOT)
                self.state = 330
                self.match(BKOOLParser.ID)
                self.state = 331
                self.list_args_wrapped()
                pass

            elif la_ == 5:
                self.state = 333
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 334
                self.exp()
                self.state = 335
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 6:
                self.state = 337
                self.operands(0)
                self.state = 338
                self.index_represent()
                pass

            elif la_ == 7:
                self.state = 340
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 8:
                self.state = 341
                self.match(BKOOLParser.NIL)
                pass


            self.state = 344
            self.match(BKOOLParser.DOT)
            self.state = 345
            self.match(BKOOLParser.ID)
            self.state = 346
            self.list_args_wrapped()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_exp" ):
                return visitor.visitBool_exp(self)
            else:
                return visitor.visitChildren(self)




    def bool_exp(self):

        localctx = BKOOLParser.Bool_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_bool_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_int_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_exp" ):
                return visitor.visitInt_exp(self)
            else:
                return visitor.visitChildren(self)




    def int_exp(self):

        localctx = BKOOLParser.Int_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_int_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_exp" ):
                return visitor.visitReturn_exp(self)
            else:
                return visitor.visitChildren(self)




    def return_exp(self):

        localctx = BKOOLParser.Return_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.exp1()
                self.state = 355
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.NEQ) | (1 << BKOOLParser.EQ) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 356
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKOOLParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.exp2()
                self.state = 362
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.AND) | (1 << BKOOLParser.OR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 363
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FLOAT_DIV(self):
            return self.getToken(BKOOLParser.FLOAT_DIV, 0)

        def INT_DIV(self):
            return self.getToken(BKOOLParser.INT_DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKOOLParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.exp3()
                self.state = 369
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD) | (1 << BKOOLParser.CONCAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 370
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.exp3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKOOLParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 376
                self.exp3()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.operands(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def obj_create(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_createContext,0)


        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)



    def operands(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.OperandsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_operands, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.CURLY_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT]:
                self.state = 381
                self.literals()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 382
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.ROUND_OPEN]:
                self.state = 383
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 384
                self.exp()
                self.state = 385
                self.match(BKOOLParser.ROUND_CLOSE)
                pass
            elif token in [BKOOLParser.THIS]:
                self.state = 387
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW]:
                self.state = 388
                self.obj_create()
                pass
            elif token in [BKOOLParser.NIL]:
                self.state = 389
                self.match(BKOOLParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 403
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 401
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 392
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 393
                        self.index_represent()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 394
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 395
                        self.match(BKOOLParser.DOT)
                        self.state = 396
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 397
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 398
                        self.match(BKOOLParser.DOT)
                        self.state = 399
                        self.match(BKOOLParser.ID)
                        self.state = 400
                        self.list_args_wrapped()
                        pass

             
                self.state = 405
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_representContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUARE_OPEN(self):
            return self.getToken(BKOOLParser.SQUARE_OPEN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SQUARE_CLOSE(self):
            return self.getToken(BKOOLParser.SQUARE_CLOSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_represent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_represent" ):
                return visitor.visitIndex_represent(self)
            else:
                return visitor.visitChildren(self)




    def index_represent(self):

        localctx = BKOOLParser.Index_representContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_index_represent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 407
            self.exp()
            self.state = 408
            self.match(BKOOLParser.SQUARE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_createContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_create

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_create" ):
                return visitor.visitObj_create(self)
            else:
                return visitor.visitChildren(self)




    def obj_create(self):

        localctx = BKOOLParser.Obj_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_obj_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(BKOOLParser.NEW)
            self.state = 411
            self.match(BKOOLParser.ID)
            self.state = 412
            self.list_args_wrapped()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_args_wrappedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROUND_OPEN(self):
            return self.getToken(BKOOLParser.ROUND_OPEN, 0)

        def ROUND_CLOSE(self):
            return self.getToken(BKOOLParser.ROUND_CLOSE, 0)

        def list_exps_as_args(self):
            return self.getTypedRuleContext(BKOOLParser.List_exps_as_argsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_args_wrapped

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_args_wrapped" ):
                return visitor.visitList_args_wrapped(self)
            else:
                return visitor.visitChildren(self)




    def list_args_wrapped(self):

        localctx = BKOOLParser.List_args_wrappedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_args_wrapped)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.state = 415
                self.list_exps_as_args()
                pass
            elif token in [BKOOLParser.ROUND_CLOSE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 419
            self.match(BKOOLParser.ROUND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exps_as_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_list_exps_as_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exps_as_args" ):
                return visitor.visitList_exps_as_args(self)
            else:
                return visitor.visitChildren(self)




    def list_exps_as_args(self):

        localctx = BKOOLParser.List_exps_as_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_list_exps_as_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.exp()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 422
                self.match(BKOOLParser.COMMA)
                self.state = 423
                self.exp()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal_replica(self):
            return self.getTypedRuleContext(BKOOLParser.Literal_replicaContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Array_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKOOLParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literals)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.FLOAT_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.literal_replica()
                pass
            elif token in [BKOOLParser.CURLY_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = BKOOLParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CURLY_OPEN(self):
            return self.getToken(BKOOLParser.CURLY_OPEN, 0)

        def literal_replica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Literal_replicaContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Literal_replicaContext,i)


        def CURLY_CLOSE(self):
            return self.getToken(BKOOLParser.CURLY_CLOSE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BKOOLParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 436
            self.literal_replica()
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 437
                self.match(BKOOLParser.COMMA)
                self.state = 438
                self.literal_replica()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 444
            self.match(BKOOLParser.CURLY_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_replicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literal_replica

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_replica" ):
                return visitor.visitLiteral_replica(self)
            else:
                return visitor.visitChildren(self)




    def literal_replica(self):

        localctx = BKOOLParser.Literal_replicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal_replica)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(BKOOLParser.INTEGER_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.boolean_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.prefix_attribute_invo_sempred
        self._predicates[36] = self.operands_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prefix_attribute_invo_sempred(self, localctx:Prefix_attribute_invoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def operands_sempred(self, localctx:OperandsContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




