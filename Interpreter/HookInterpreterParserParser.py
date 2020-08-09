# Generated from .\Interpreter\HookInterpreterParser.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4\36\n\4\3\4\3\4\5\4\"\n\4\3\4\7\4%\n\4\f\4\16")
        buf.write("\4(\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\62\n\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\7\3\7\5\7?\n\7\3")
        buf.write("\7\3\7\5\7C\n\7\7\7E\n\7\f\7\16\7H\13\7\3\7\3\7\3\b\3")
        buf.write("\b\5\bN\n\b\3\b\3\b\3\b\5\bS\n\b\3\b\5\bV\n\b\3\b\5\b")
        buf.write("Y\n\b\3\b\3\b\3\b\3\b\3&\2\t\2\4\6\b\n\f\16\2\3\4\2\6")
        buf.write("\6\16\16\2g\2\25\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b+")
        buf.write("\3\2\2\2\n:\3\2\2\2\fF\3\2\2\2\16M\3\2\2\2\20\26\7\7\2")
        buf.write("\2\21\26\7\b\2\2\22\26\5\6\4\2\23\26\5\b\5\2\24\26\5\16")
        buf.write("\b\2\25\20\3\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3")
        buf.write("\2\2\2\25\24\3\2\2\2\26\3\3\2\2\2\27\30\t\2\2\2\30\5\3")
        buf.write("\2\2\2\31\32\7\t\2\2\32\33\7\5\2\2\33\35\7\r\2\2\34\36")
        buf.write("\7\5\2\2\35\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("!\7\n\2\2 \"\7\5\2\2! \3\2\2\2!\"\3\2\2\2\"&\3\2\2\2#")
        buf.write("%\13\2\2\2$#\3\2\2\2%(\3\2\2\2&\'\3\2\2\2&$\3\2\2\2\'")
        buf.write(")\3\2\2\2(&\3\2\2\2)*\5\4\3\2*\7\3\2\2\2+,\7\22\2\2,-")
        buf.write("\7\5\2\2-.\7\3\2\2./\7\25\2\2/\61\7\3\2\2\60\62\7\5\2")
        buf.write("\2\61\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64\5\4")
        buf.write("\3\2\64\t\3\2\2\2\65;\7\r\2\2\66\67\7\3\2\2\678\7\25\2")
        buf.write("\28;\7\3\2\29;\7\13\2\2:\65\3\2\2\2:\66\3\2\2\2:9\3\2")
        buf.write("\2\2;\13\3\2\2\2<>\5\n\6\2=?\7\5\2\2>=\3\2\2\2>?\3\2\2")
        buf.write("\2?@\3\2\2\2@B\7\4\2\2AC\7\5\2\2BA\3\2\2\2BC\3\2\2\2C")
        buf.write("E\3\2\2\2D<\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3")
        buf.write("\2\2\2HF\3\2\2\2IJ\5\n\6\2J\r\3\2\2\2KL\7\r\2\2LN\7\20")
        buf.write("\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\r\2\2PR\7\23\2")
        buf.write("\2QS\7\5\2\2RQ\3\2\2\2RS\3\2\2\2SU\3\2\2\2TV\5\f\7\2U")
        buf.write("T\3\2\2\2UV\3\2\2\2VX\3\2\2\2WY\7\5\2\2XW\3\2\2\2XY\3")
        buf.write("\2\2\2YZ\3\2\2\2Z[\7\24\2\2[\\\5\4\3\2\\\17\3\2\2\2\17")
        buf.write("\25\35!&\61:>BFMRUX")
        return buf.getvalue()


class HookInterpreterParserParser ( Parser ):

    grammarFileName = "HookInterpreterParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Declare'", "'='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "<INVALID>", "'.'", 
                     "'..'", "'Include'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Whitespace", 
                      "NewLine", "BlockComment", "LineComment", "Declare", 
                      "Equals", "Digits", "Name", "Identifier", "End", "Letter", 
                      "Dot", "DoubleDot", "Include", "OpenParanthesis", 
                      "CloseParanthesis", "NotNewLine" ]

    RULE_primaryExpression = 0
    RULE_sentenceEnding = 1
    RULE_variableDeclare = 2
    RULE_includeSentence = 3
    RULE_argument = 4
    RULE_arguments = 5
    RULE_functionCall = 6

    ruleNames =  [ "primaryExpression", "sentenceEnding", "variableDeclare", 
                   "includeSentence", "argument", "arguments", "functionCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Whitespace=3
    NewLine=4
    BlockComment=5
    LineComment=6
    Declare=7
    Equals=8
    Digits=9
    Name=10
    Identifier=11
    End=12
    Letter=13
    Dot=14
    DoubleDot=15
    Include=16
    OpenParanthesis=17
    CloseParanthesis=18
    NotNewLine=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BlockComment(self):
            return self.getToken(HookInterpreterParserParser.BlockComment, 0)

        def LineComment(self):
            return self.getToken(HookInterpreterParserParser.LineComment, 0)

        def variableDeclare(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.VariableDeclareContext,0)


        def includeSentence(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.IncludeSentenceContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = HookInterpreterParserParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_primaryExpression)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParserParser.BlockComment]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(HookInterpreterParserParser.BlockComment)
                pass
            elif token in [HookInterpreterParserParser.LineComment]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(HookInterpreterParserParser.LineComment)
                pass
            elif token in [HookInterpreterParserParser.Declare]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.variableDeclare()
                pass
            elif token in [HookInterpreterParserParser.Include]:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.includeSentence()
                pass
            elif token in [HookInterpreterParserParser.Identifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 18
                self.functionCall()
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


    class SentenceEndingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def End(self):
            return self.getToken(HookInterpreterParserParser.End, 0)

        def NewLine(self):
            return self.getToken(HookInterpreterParserParser.NewLine, 0)

        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_sentenceEnding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenceEnding" ):
                listener.enterSentenceEnding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenceEnding" ):
                listener.exitSentenceEnding(self)




    def sentenceEnding(self):

        localctx = HookInterpreterParserParser.SentenceEndingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentenceEnding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==HookInterpreterParserParser.NewLine or _la==HookInterpreterParserParser.End):
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


    class VariableDeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Declare(self):
            return self.getToken(HookInterpreterParserParser.Declare, 0)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.Whitespace)
            else:
                return self.getToken(HookInterpreterParserParser.Whitespace, i)

        def Identifier(self):
            return self.getToken(HookInterpreterParserParser.Identifier, 0)

        def Equals(self):
            return self.getToken(HookInterpreterParserParser.Equals, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.SentenceEndingContext,0)


        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_variableDeclare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclare" ):
                listener.enterVariableDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclare" ):
                listener.exitVariableDeclare(self)




    def variableDeclare(self):

        localctx = HookInterpreterParserParser.VariableDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(HookInterpreterParserParser.Declare)
            self.state = 24
            self.match(HookInterpreterParserParser.Whitespace)
            self.state = 25
            self.match(HookInterpreterParserParser.Identifier)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 26
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 29
            self.match(HookInterpreterParserParser.Equals)
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 30
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 33
                    self.matchWildcard() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 39
            self.sentenceEnding()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeSentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Include(self):
            return self.getToken(HookInterpreterParserParser.Include, 0)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.Whitespace)
            else:
                return self.getToken(HookInterpreterParserParser.Whitespace, i)

        def NotNewLine(self):
            return self.getToken(HookInterpreterParserParser.NotNewLine, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.SentenceEndingContext,0)


        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_includeSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeSentence" ):
                listener.enterIncludeSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeSentence" ):
                listener.exitIncludeSentence(self)




    def includeSentence(self):

        localctx = HookInterpreterParserParser.IncludeSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_includeSentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(HookInterpreterParserParser.Include)
            self.state = 42
            self.match(HookInterpreterParserParser.Whitespace)
            self.state = 43
            self.match(HookInterpreterParserParser.T__0)
            self.state = 44
            self.match(HookInterpreterParserParser.NotNewLine)
            self.state = 45
            self.match(HookInterpreterParserParser.T__0)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 46
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 49
            self.sentenceEnding()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(HookInterpreterParserParser.Identifier, 0)

        def NotNewLine(self):
            return self.getToken(HookInterpreterParserParser.NotNewLine, 0)

        def Digits(self):
            return self.getToken(HookInterpreterParserParser.Digits, 0)

        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = HookInterpreterParserParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParserParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(HookInterpreterParserParser.Identifier)
                pass
            elif token in [HookInterpreterParserParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(HookInterpreterParserParser.T__0)
                self.state = 53
                self.match(HookInterpreterParserParser.NotNewLine)
                self.state = 54
                self.match(HookInterpreterParserParser.T__0)
                pass
            elif token in [HookInterpreterParserParser.Digits]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(HookInterpreterParserParser.Digits)
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


    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParserParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParserParser.ArgumentContext,i)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.Whitespace)
            else:
                return self.getToken(HookInterpreterParserParser.Whitespace, i)

        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = HookInterpreterParserParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.argument()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HookInterpreterParserParser.Whitespace:
                        self.state = 59
                        self.match(HookInterpreterParserParser.Whitespace)


                    self.state = 62
                    self.match(HookInterpreterParserParser.T__1)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HookInterpreterParserParser.Whitespace:
                        self.state = 63
                        self.match(HookInterpreterParserParser.Whitespace)

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 71
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.Identifier)
            else:
                return self.getToken(HookInterpreterParserParser.Identifier, i)

        def OpenParanthesis(self):
            return self.getToken(HookInterpreterParserParser.OpenParanthesis, 0)

        def CloseParanthesis(self):
            return self.getToken(HookInterpreterParserParser.CloseParanthesis, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.SentenceEndingContext,0)


        def Dot(self):
            return self.getToken(HookInterpreterParserParser.Dot, 0)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.Whitespace)
            else:
                return self.getToken(HookInterpreterParserParser.Whitespace, i)

        def arguments(self):
            return self.getTypedRuleContext(HookInterpreterParserParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return HookInterpreterParserParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = HookInterpreterParserParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(HookInterpreterParserParser.Identifier)
                self.state = 74
                self.match(HookInterpreterParserParser.Dot)


            self.state = 77
            self.match(HookInterpreterParserParser.Identifier)
            self.state = 78
            self.match(HookInterpreterParserParser.OpenParanthesis)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParserParser.T__0) | (1 << HookInterpreterParserParser.Digits) | (1 << HookInterpreterParserParser.Identifier))) != 0):
                self.state = 82
                self.arguments()


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 85
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 88
            self.match(HookInterpreterParserParser.CloseParanthesis)
            self.state = 89
            self.sentenceEnding()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





