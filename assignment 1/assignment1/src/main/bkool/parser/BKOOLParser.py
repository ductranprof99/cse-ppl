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
        buf.write("\u01c5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\6\2^\n\2\r\2\16\2_\3\2\3\2\3\3\3\3\3\3\3\3\5\3h\n\3")
        buf.write("\3\3\3\3\7\3l\n\3\f\3\16\3o\13\3\3\3\3\3\3\4\3\4\3\4\5")
        buf.write("\4v\n\4\3\5\3\5\3\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080\13")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008b\n\6\3")
        buf.write("\7\5\7\u008e\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3\n\3")
        buf.write("\n\7\n\u00a6\n\n\f\n\16\n\u00a9\13\n\5\n\u00ab\n\n\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u00b1\n\13\f\13\16\13\u00b4\13\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\5\r\u00bb\n\r\3\16\3\16\3\16\5\16")
        buf.write("\u00c0\n\16\3\17\3\17\5\17\u00c4\n\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\7\22\u00d0\n\22\f\22")
        buf.write("\16\22\u00d3\13\22\3\22\7\22\u00d6\n\22\f\22\16\22\u00d9")
        buf.write("\13\22\3\22\3\22\3\23\5\23\u00de\n\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u00e4\n\23\f\23\16\23\u00e7\13\23\3\23\3\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fc\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u010a\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u0113\n\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u011b")
        buf.write("\n\27\f\27\16\27\u011e\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0126\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\6\32\u0133\n\32\r\32\16\32\u0134")
        buf.write("\3\32\3\32\3\32\5\32\u013a\n\32\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u0157\n\36\3\36\3\36\3\36\3\36\3\37\3\37\3")
        buf.write(" \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0168\n\"\3#\3#\3#")
        buf.write("\3#\3#\5#\u016f\n#\3$\3$\3$\3$\3$\5$\u0176\n$\3%\3%\3")
        buf.write("%\5%\u017b\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0187\n")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\7&\u0192\n&\f&\16&\u0195")
        buf.write("\13&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\5)\u01a2\n)")
        buf.write("\3)\3)\3*\3*\3*\7*\u01a9\n*\f*\16*\u01ac\13*\3+\3+\5+")
        buf.write("\u01b0\n+\3,\3,\3-\3-\3-\3-\7-\u01b8\n-\f-\16-\u01bb\13")
        buf.write("-\3-\3-\3.\3.\3.\3.\5.\u01c3\n.\3.\2\4,J/\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\2\t\6\2\3\3\n\n\f\r\23\23\3\2\30\31\3\2")
        buf.write("!&\4\2\32\33()\4\2\34\37**\4\2\32\33\'\'\3\2\21\22\2\u01d9")
        buf.write("\2]\3\2\2\2\4c\3\2\2\2\6u\3\2\2\2\bw\3\2\2\2\n\u008a\3")
        buf.write("\2\2\2\f\u008d\3\2\2\2\16\u0096\3\2\2\2\20\u009c\3\2\2")
        buf.write("\2\22\u00aa\3\2\2\2\24\u00ac\3\2\2\2\26\u00b5\3\2\2\2")
        buf.write("\30\u00ba\3\2\2\2\32\u00bf\3\2\2\2\34\u00c3\3\2\2\2\36")
        buf.write("\u00c9\3\2\2\2 \u00cb\3\2\2\2\"\u00cd\3\2\2\2$\u00dd\3")
        buf.write("\2\2\2&\u00fb\3\2\2\2(\u00fd\3\2\2\2*\u0109\3\2\2\2,\u0112")
        buf.write("\3\2\2\2.\u011f\3\2\2\2\60\u0127\3\2\2\2\62\u0139\3\2")
        buf.write("\2\2\64\u013b\3\2\2\2\66\u013d\3\2\2\28\u013f\3\2\2\2")
        buf.write(":\u0156\3\2\2\2<\u015c\3\2\2\2>\u015e\3\2\2\2@\u0160\3")
        buf.write("\2\2\2B\u0167\3\2\2\2D\u016e\3\2\2\2F\u0175\3\2\2\2H\u017a")
        buf.write("\3\2\2\2J\u0186\3\2\2\2L\u0196\3\2\2\2N\u019a\3\2\2\2")
        buf.write("P\u019e\3\2\2\2R\u01a5\3\2\2\2T\u01af\3\2\2\2V\u01b1\3")
        buf.write("\2\2\2X\u01b3\3\2\2\2Z\u01c2\3\2\2\2\\^\5\4\3\2]\\\3\2")
        buf.write("\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\2\2\3")
        buf.write("b\3\3\2\2\2cd\7\5\2\2dg\7:\2\2ef\7\t\2\2fh\7:\2\2ge\3")
        buf.write("\2\2\2gh\3\2\2\2hi\3\2\2\2im\7/\2\2jl\5\6\4\2kj\3\2\2")
        buf.write("\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2np\3\2\2\2om\3\2\2\2p")
        buf.write("q\7\60\2\2q\5\3\2\2\2rv\5\b\5\2sv\5\f\7\2tv\5\16\b\2u")
        buf.write("r\3\2\2\2us\3\2\2\2ut\3\2\2\2v\7\3\2\2\2wx\5\n\6\2xy\5")
        buf.write("\32\16\2y~\5\20\t\2z{\7\66\2\2{}\5\20\t\2|z\3\2\2\2}\u0080")
        buf.write("\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0081\3\2\2\2\u0080")
        buf.write("~\3\2\2\2\u0081\u0082\7\65\2\2\u0082\t\3\2\2\2\u0083\u008b")
        buf.write("\3\2\2\2\u0084\u008b\7\27\2\2\u0085\u008b\7\26\2\2\u0086")
        buf.write("\u0087\7\27\2\2\u0087\u008b\7\26\2\2\u0088\u0089\7\26")
        buf.write("\2\2\u0089\u008b\7\27\2\2\u008a\u0083\3\2\2\2\u008a\u0084")
        buf.write("\3\2\2\2\u008a\u0085\3\2\2\2\u008a\u0086\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008b\13\3\2\2\2\u008c\u008e\7\27\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\5\30\r\2\u0090\u0091\7:\2\2\u0091\u0092\7")
        buf.write("\61\2\2\u0092\u0093\5\22\n\2\u0093\u0094\7\62\2\2\u0094")
        buf.write("\u0095\5\"\22\2\u0095\r\3\2\2\2\u0096\u0097\7:\2\2\u0097")
        buf.write("\u0098\7\61\2\2\u0098\u0099\5\22\n\2\u0099\u009a\7\62")
        buf.write("\2\2\u009a\u009b\5\"\22\2\u009b\17\3\2\2\2\u009c\u009f")
        buf.write("\7:\2\2\u009d\u009e\7 \2\2\u009e\u00a0\5B\"\2\u009f\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\21\3\2\2\2\u00a1\u00ab")
        buf.write("\3\2\2\2\u00a2\u00a7\5\24\13\2\u00a3\u00a4\7\65\2\2\u00a4")
        buf.write("\u00a6\5\24\13\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2")
        buf.write("\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00a1\3\2\2\2\u00aa")
        buf.write("\u00a2\3\2\2\2\u00ab\23\3\2\2\2\u00ac\u00ad\5\26\f\2\u00ad")
        buf.write("\u00b2\7:\2\2\u00ae\u00af\7\66\2\2\u00af\u00b1\7:\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\25\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b6\5\32\16\2\u00b6\27\3\2\2\2\u00b7")
        buf.write("\u00bb\5 \21\2\u00b8\u00bb\5\36\20\2\u00b9\u00bb\5\34")
        buf.write("\17\2\u00ba\u00b7\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9")
        buf.write("\3\2\2\2\u00bb\31\3\2\2\2\u00bc\u00c0\5\36\20\2\u00bd")
        buf.write("\u00c0\5 \21\2\u00be\u00c0\5\34\17\2\u00bf\u00bc\3\2\2")
        buf.write("\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\33\3")
        buf.write("\2\2\2\u00c1\u00c4\5 \21\2\u00c2\u00c4\5\36\20\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\7\63\2\2\u00c6\u00c7\79\2\2\u00c7\u00c8\7")
        buf.write("\64\2\2\u00c8\35\3\2\2\2\u00c9\u00ca\7:\2\2\u00ca\37\3")
        buf.write("\2\2\2\u00cb\u00cc\t\2\2\2\u00cc!\3\2\2\2\u00cd\u00d1")
        buf.write("\7/\2\2\u00ce\u00d0\5$\23\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d7\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6\5")
        buf.write("&\24\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00db\7\60\2\2\u00db#\3\2\2\2\u00dc")
        buf.write("\u00de\7\26\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2")
        buf.write("\2\u00de\u00df\3\2\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e5")
        buf.write("\5\20\t\2\u00e1\u00e2\7\66\2\2\u00e2\u00e4\5\20\t\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e5\3")
        buf.write("\2\2\2\u00e8\u00e9\7\65\2\2\u00e9%\3\2\2\2\u00ea\u00eb")
        buf.write("\5(\25\2\u00eb\u00ec\7\65\2\2\u00ec\u00fc\3\2\2\2\u00ed")
        buf.write("\u00fc\5.\30\2\u00ee\u00fc\5\60\31\2\u00ef\u00f0\5\64")
        buf.write("\33\2\u00f0\u00f1\7\65\2\2\u00f1\u00fc\3\2\2\2\u00f2\u00f3")
        buf.write("\5\66\34\2\u00f3\u00f4\7\65\2\2\u00f4\u00fc\3\2\2\2\u00f5")
        buf.write("\u00f6\58\35\2\u00f6\u00f7\7\65\2\2\u00f7\u00fc\3\2\2")
        buf.write("\2\u00f8\u00f9\5:\36\2\u00f9\u00fa\7\65\2\2\u00fa\u00fc")
        buf.write("\3\2\2\2\u00fb\u00ea\3\2\2\2\u00fb\u00ed\3\2\2\2\u00fb")
        buf.write("\u00ee\3\2\2\2\u00fb\u00ef\3\2\2\2\u00fb\u00f2\3\2\2\2")
        buf.write("\u00fb\u00f5\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fc\'\3\2\2")
        buf.write("\2\u00fd\u00fe\5*\26\2\u00fe\u00ff\7.\2\2\u00ff\u0100")
        buf.write("\5B\"\2\u0100)\3\2\2\2\u0101\u010a\7:\2\2\u0102\u0103")
        buf.write("\5J&\2\u0103\u0104\5L\'\2\u0104\u010a\3\2\2\2\u0105\u0106")
        buf.write("\5,\27\2\u0106\u0107\7+\2\2\u0107\u0108\7:\2\2\u0108\u010a")
        buf.write("\3\2\2\2\u0109\u0101\3\2\2\2\u0109\u0102\3\2\2\2\u0109")
        buf.write("\u0105\3\2\2\2\u010a+\3\2\2\2\u010b\u0113\b\27\1\2\u010c")
        buf.write("\u0113\7:\2\2\u010d\u010e\7\61\2\2\u010e\u010f\5B\"\2")
        buf.write("\u010f\u0110\7\62\2\2\u0110\u0113\3\2\2\2\u0111\u0113")
        buf.write("\7\25\2\2\u0112\u010b\3\2\2\2\u0112\u010c\3\2\2\2\u0112")
        buf.write("\u010d\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u011c\3\2\2\2")
        buf.write("\u0114\u0115\f\6\2\2\u0115\u0116\7+\2\2\u0116\u0117\7")
        buf.write(":\2\2\u0117\u011b\5P)\2\u0118\u0119\f\4\2\2\u0119\u011b")
        buf.write("\5L\'\2\u011a\u0114\3\2\2\2\u011a\u0118\3\2\2\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d-\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\7\13\2")
        buf.write("\2\u0120\u0121\5<\37\2\u0121\u0122\7\16\2\2\u0122\u0125")
        buf.write("\5&\24\2\u0123\u0124\7\b\2\2\u0124\u0126\5&\24\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126/\3\2\2\2\u0127")
        buf.write("\u0128\7\17\2\2\u0128\u0129\7:\2\2\u0129\u012a\7.\2\2")
        buf.write("\u012a\u012b\5> \2\u012b\u012c\t\3\2\2\u012c\u012d\5>")
        buf.write(" \2\u012d\u012e\7\7\2\2\u012e\u012f\5\62\32\2\u012f\61")
        buf.write("\3\2\2\2\u0130\u0132\7/\2\2\u0131\u0133\5&\24\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\7")
        buf.write("\60\2\2\u0137\u013a\3\2\2\2\u0138\u013a\5&\24\2\u0139")
        buf.write("\u0130\3\2\2\2\u0139\u0138\3\2\2\2\u013a\63\3\2\2\2\u013b")
        buf.write("\u013c\7\4\2\2\u013c\65\3\2\2\2\u013d\u013e\7\6\2\2\u013e")
        buf.write("\67\3\2\2\2\u013f\u0140\7\20\2\2\u0140\u0141\5@!\2\u0141")
        buf.write("9\3\2\2\2\u0142\u0157\5T+\2\u0143\u0157\7:\2\2\u0144\u0145")
        buf.write("\5J&\2\u0145\u0146\7+\2\2\u0146\u0147\7:\2\2\u0147\u0157")
        buf.write("\3\2\2\2\u0148\u0149\5J&\2\u0149\u014a\7+\2\2\u014a\u014b")
        buf.write("\7:\2\2\u014b\u014c\5P)\2\u014c\u0157\3\2\2\2\u014d\u014e")
        buf.write("\7\61\2\2\u014e\u014f\5B\"\2\u014f\u0150\7\62\2\2\u0150")
        buf.write("\u0157\3\2\2\2\u0151\u0152\5J&\2\u0152\u0153\5L\'\2\u0153")
        buf.write("\u0157\3\2\2\2\u0154\u0157\7\25\2\2\u0155\u0157\7\24\2")
        buf.write("\2\u0156\u0142\3\2\2\2\u0156\u0143\3\2\2\2\u0156\u0144")
        buf.write("\3\2\2\2\u0156\u0148\3\2\2\2\u0156\u014d\3\2\2\2\u0156")
        buf.write("\u0151\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158\u0159\7+\2\2\u0159\u015a\7")
        buf.write(":\2\2\u015a\u015b\5P)\2\u015b;\3\2\2\2\u015c\u015d\5B")
        buf.write("\"\2\u015d=\3\2\2\2\u015e\u015f\5B\"\2\u015f?\3\2\2\2")
        buf.write("\u0160\u0161\5B\"\2\u0161A\3\2\2\2\u0162\u0163\5D#\2\u0163")
        buf.write("\u0164\t\4\2\2\u0164\u0165\5D#\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0168\5D#\2\u0167\u0162\3\2\2\2\u0167\u0166\3\2\2\2\u0168")
        buf.write("C\3\2\2\2\u0169\u016a\5F$\2\u016a\u016b\t\5\2\2\u016b")
        buf.write("\u016c\5D#\2\u016c\u016f\3\2\2\2\u016d\u016f\5F$\2\u016e")
        buf.write("\u0169\3\2\2\2\u016e\u016d\3\2\2\2\u016fE\3\2\2\2\u0170")
        buf.write("\u0171\5H%\2\u0171\u0172\t\6\2\2\u0172\u0173\5F$\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0176\5H%\2\u0175\u0170\3\2\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176G\3\2\2\2\u0177\u0178\t\7\2\2\u0178")
        buf.write("\u017b\5H%\2\u0179\u017b\5J&\2\u017a\u0177\3\2\2\2\u017a")
        buf.write("\u0179\3\2\2\2\u017bI\3\2\2\2\u017c\u017d\b&\1\2\u017d")
        buf.write("\u0187\5T+\2\u017e\u0187\7:\2\2\u017f\u0180\7\61\2\2\u0180")
        buf.write("\u0181\5B\"\2\u0181\u0182\7\62\2\2\u0182\u0187\3\2\2\2")
        buf.write("\u0183\u0187\7\25\2\2\u0184\u0187\5N(\2\u0185\u0187\7")
        buf.write("\24\2\2\u0186\u017c\3\2\2\2\u0186\u017e\3\2\2\2\u0186")
        buf.write("\u017f\3\2\2\2\u0186\u0183\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0186\u0185\3\2\2\2\u0187\u0193\3\2\2\2\u0188\u0189\f")
        buf.write("\t\2\2\u0189\u018a\7+\2\2\u018a\u0192\7:\2\2\u018b\u018c")
        buf.write("\f\b\2\2\u018c\u018d\7+\2\2\u018d\u018e\7:\2\2\u018e\u0192")
        buf.write("\5P)\2\u018f\u0190\f\6\2\2\u0190\u0192\5L\'\2\u0191\u0188")
        buf.write("\3\2\2\2\u0191\u018b\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0195\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194K\3\2\2\2\u0195\u0193\3\2\2\2\u0196\u0197\7\63\2")
        buf.write("\2\u0197\u0198\5B\"\2\u0198\u0199\7\64\2\2\u0199M\3\2")
        buf.write("\2\2\u019a\u019b\7,\2\2\u019b\u019c\7:\2\2\u019c\u019d")
        buf.write("\5P)\2\u019dO\3\2\2\2\u019e\u01a1\7\61\2\2\u019f\u01a2")
        buf.write("\5R*\2\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\7\62\2\2\u01a4")
        buf.write("Q\3\2\2\2\u01a5\u01aa\5B\"\2\u01a6\u01a7\7\66\2\2\u01a7")
        buf.write("\u01a9\5B\"\2\u01a8\u01a6\3\2\2\2\u01a9\u01ac\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abS\3\2\2")
        buf.write("\2\u01ac\u01aa\3\2\2\2\u01ad\u01b0\5Z.\2\u01ae\u01b0\5")
        buf.write("X-\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0U\3")
        buf.write("\2\2\2\u01b1\u01b2\t\b\2\2\u01b2W\3\2\2\2\u01b3\u01b4")
        buf.write("\7/\2\2\u01b4\u01b9\5Z.\2\u01b5\u01b6\7\66\2\2\u01b6\u01b8")
        buf.write("\5Z.\2\u01b7\u01b5\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bc\u01bd\7\60\2\2\u01bdY\3\2\2\2\u01be")
        buf.write("\u01c3\79\2\2\u01bf\u01c3\7\67\2\2\u01c0\u01c3\78\2\2")
        buf.write("\u01c1\u01c3\5V,\2\u01c2\u01be\3\2\2\2\u01c2\u01bf\3\2")
        buf.write("\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3[\3")
        buf.write("\2\2\2)_gmu~\u008a\u008d\u009f\u00a7\u00aa\u00b2\u00ba")
        buf.write("\u00bf\u00c3\u00d1\u00d7\u00dd\u00e5\u00fb\u0109\u0112")
        buf.write("\u011a\u011c\u0125\u0134\u0139\u0156\u0167\u016e\u0175")
        buf.write("\u017a\u0186\u0191\u0193\u01a1\u01aa\u01af\u01b9\u01c2")
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
                      "STRING_LIT", "INTEGER_LIT", "ID", "COMMENT", "WS", 
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
    STRING_LIT=54
    INTEGER_LIT=55
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

        def field(self):
            return self.getTypedRuleContext(BKOOLParser.FieldContext,0)


        def type_attribute(self):
            return self.getTypedRuleContext(BKOOLParser.Type_attributeContext,0)


        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declareContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

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
            self.state = 117
            self.field()
            self.state = 118
            self.type_attribute()
            self.state = 119
            self.var_declare()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 120
                self.match(BKOOLParser.COMMA)
                self.state = 121
                self.var_declare()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
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
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(BKOOLParser.STATIC)
                self.state = 133
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.match(BKOOLParser.FINAL)
                self.state = 135
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
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 138
                self.match(BKOOLParser.STATIC)


            self.state = 141
            self.return_type()
            self.state = 142
            self.match(BKOOLParser.ID)
            self.state = 143
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 144
            self.list_params()
            self.state = 145
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 146
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
            self.state = 148
            self.match(BKOOLParser.ID)
            self.state = 149
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 150
            self.list_params()
            self.state = 151
            self.match(BKOOLParser.ROUND_CLOSE)
            self.state = 152
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
            self.state = 154
            self.match(BKOOLParser.ID)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ASSIGN:
                self.state = 155
                self.match(BKOOLParser.ASSIGN)
                self.state = 156
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
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ROUND_CLOSE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.parameter()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SEMI:
                    self.state = 161
                    self.match(BKOOLParser.SEMI)
                    self.state = 162
                    self.parameter()
                    self.state = 167
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
            self.state = 170
            self.parameter_type()
            self.state = 171
            self.match(BKOOLParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 172
                self.match(BKOOLParser.COMMA)
                self.state = 173
                self.match(BKOOLParser.ID)
                self.state = 178
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
            self.state = 179
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.class_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.class_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.primitive_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
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
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INTEGER, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.state = 191
                self.primitive_type()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 192
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 195
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 196
            self.match(BKOOLParser.INTEGER_LIT)
            self.state = 197
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
            self.state = 199
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
            self.state = 201
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
            self.state = 203
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    self.local_attribute() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 210
                    self.statement() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 216
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
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 218
                self.match(BKOOLParser.FINAL)


            self.state = 221
            self.type_attribute()
            self.state = 222
            self.var_declare()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 223
                self.match(BKOOLParser.COMMA)
                self.state = 224
                self.var_declare()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
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

        def assignment_satement(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_satementContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def if_statement(self):
            return self.getTypedRuleContext(BKOOLParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(BKOOLParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Return_statementContext,0)


        def method_invo_statement(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invo_statementContext,0)


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
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.assignment_satement()
                self.state = 233
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.for_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.break_statement()
                self.state = 238
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.continue_statement()
                self.state = 241
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.return_statement()
                self.state = 244
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.method_invo_statement()
                self.state = 247
                self.match(BKOOLParser.SEMI)
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
            self.state = 251
            self.lhs()
            self.state = 252
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 253
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
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.operands(0)
                self.state = 257
                self.index_represent()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.prefix_attribute_invo(0)
                self.state = 260
                self.match(BKOOLParser.DOT)
                self.state = 261
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
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 266
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 267
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 268
                self.exp()
                self.state = 269
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 4:
                self.state = 271
                self.match(BKOOLParser.THIS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 280
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 274
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 275
                        self.match(BKOOLParser.DOT)
                        self.state = 276
                        self.match(BKOOLParser.ID)
                        self.state = 277
                        self.list_args_wrapped()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Prefix_attribute_invoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prefix_attribute_invo)
                        self.state = 278
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 279
                        self.index_represent()
                        pass

             
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 285
            self.match(BKOOLParser.IF)
            self.state = 286
            self.bool_exp()
            self.state = 287
            self.match(BKOOLParser.THEN)
            self.state = 288
            self.statement()
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 289
                self.match(BKOOLParser.ELSE)
                self.state = 290
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
            self.state = 293
            self.match(BKOOLParser.FOR)
            self.state = 294
            self.match(BKOOLParser.ID)
            self.state = 295
            self.match(BKOOLParser.ASSIGN_EQ)
            self.state = 296
            self.int_exp()
            self.state = 297
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 298
            self.int_exp()
            self.state = 299
            self.match(BKOOLParser.DO)
            self.state = 300
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
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(BKOOLParser.CURLY_OPEN)
                self.state = 304 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 303
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 306 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 308
                self.match(BKOOLParser.CURLY_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
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
            self.state = 313
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
            self.state = 315
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
            self.state = 317
            self.match(BKOOLParser.RETURN)
            self.state = 318
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
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 320
                self.literals()
                pass

            elif la_ == 2:
                self.state = 321
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 322
                self.operands(0)
                self.state = 323
                self.match(BKOOLParser.DOT)
                self.state = 324
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.state = 326
                self.operands(0)
                self.state = 327
                self.match(BKOOLParser.DOT)
                self.state = 328
                self.match(BKOOLParser.ID)
                self.state = 329
                self.list_args_wrapped()
                pass

            elif la_ == 5:
                self.state = 331
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 332
                self.exp()
                self.state = 333
                self.match(BKOOLParser.ROUND_CLOSE)
                pass

            elif la_ == 6:
                self.state = 335
                self.operands(0)
                self.state = 336
                self.index_represent()
                pass

            elif la_ == 7:
                self.state = 338
                self.match(BKOOLParser.THIS)
                pass

            elif la_ == 8:
                self.state = 339
                self.match(BKOOLParser.NIL)
                pass


            self.state = 342
            self.match(BKOOLParser.DOT)
            self.state = 343
            self.match(BKOOLParser.ID)
            self.state = 344
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
            self.state = 346
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
            self.state = 348
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
            self.state = 350
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
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.exp1()
                self.state = 353
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.NEQ) | (1 << BKOOLParser.EQ) | (1 << BKOOLParser.LT) | (1 << BKOOLParser.GT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 354
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
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
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.exp2()
                self.state = 360
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.AND) | (1 << BKOOLParser.OR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 361
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.exp3()
                self.state = 367
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FLOAT_DIV) | (1 << BKOOLParser.INT_DIV) | (1 << BKOOLParser.MOD) | (1 << BKOOLParser.CONCAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 368
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 374
                self.exp3()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def list_args_wrapped(self):
            return self.getTypedRuleContext(BKOOLParser.List_args_wrappedContext,0)


        def index_represent(self):
            return self.getTypedRuleContext(BKOOLParser.Index_representContext,0)


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
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.CURLY_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.INTEGER_LIT]:
                self.state = 379
                self.literals()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 380
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.ROUND_OPEN]:
                self.state = 381
                self.match(BKOOLParser.ROUND_OPEN)
                self.state = 382
                self.exp()
                self.state = 383
                self.match(BKOOLParser.ROUND_CLOSE)
                pass
            elif token in [BKOOLParser.THIS]:
                self.state = 385
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.NEW]:
                self.state = 386
                self.obj_create()
                pass
            elif token in [BKOOLParser.NIL]:
                self.state = 387
                self.match(BKOOLParser.NIL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 399
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 390
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 391
                        self.match(BKOOLParser.DOT)
                        self.state = 392
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 393
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 394
                        self.match(BKOOLParser.DOT)
                        self.state = 395
                        self.match(BKOOLParser.ID)
                        self.state = 396
                        self.list_args_wrapped()
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.OperandsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_operands)
                        self.state = 397
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 398
                        self.index_represent()
                        pass

             
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            self.state = 404
            self.match(BKOOLParser.SQUARE_OPEN)
            self.state = 405
            self.exp()
            self.state = 406
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
            self.state = 408
            self.match(BKOOLParser.NEW)
            self.state = 409
            self.match(BKOOLParser.ID)
            self.state = 410
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
            self.state = 412
            self.match(BKOOLParser.ROUND_OPEN)
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.NEW, BKOOLParser.CURLY_OPEN, BKOOLParser.ROUND_OPEN, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.INTEGER_LIT, BKOOLParser.ID]:
                self.state = 413
                self.list_exps_as_args()
                pass
            elif token in [BKOOLParser.ROUND_CLOSE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 417
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
            self.state = 419
            self.exp()
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 420
                self.match(BKOOLParser.COMMA)
                self.state = 421
                self.exp()
                self.state = 426
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
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.literal_replica()
                pass
            elif token in [BKOOLParser.CURLY_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
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
            self.state = 431
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
            self.state = 433
            self.match(BKOOLParser.CURLY_OPEN)
            self.state = 434
            self.literal_replica()
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 435
                self.match(BKOOLParser.COMMA)
                self.state = 436
                self.literal_replica()
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 442
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
            self.state = 448
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(BKOOLParser.INTEGER_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 447
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
                return self.precpred(self._ctx, 4)
         




