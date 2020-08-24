# Generated from .\HookInterpreterParser.g4 by ANTLR 4.8
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
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4\36\n\4\3\4\3\4\5\4\"\n\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\68\n\6\3\7\3\7\5\7<\n\7\3\7\3\7\5\7@\n\7")
        buf.write("\7\7B\n\7\f\7\16\7E\13\7\3\7\3\7\3\b\3\b\5\bK\n\b\3\b")
        buf.write("\3\b\3\b\5\bP\n\b\3\b\5\bS\n\b\3\b\5\bV\n\b\3\b\3\b\3")
        buf.write("\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\4\2\6\6\16\16\2c\2\25")
        buf.write("\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b&\3\2\2\2\n\67\3\2")
        buf.write("\2\2\fC\3\2\2\2\16J\3\2\2\2\20\26\7\7\2\2\21\26\7\b\2")
        buf.write("\2\22\26\5\6\4\2\23\26\5\b\5\2\24\26\5\16\b\2\25\20\3")
        buf.write("\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3\2\2\2\25\24")
        buf.write("\3\2\2\2\26\3\3\2\2\2\27\30\t\2\2\2\30\5\3\2\2\2\31\32")
        buf.write("\7\t\2\2\32\33\7\5\2\2\33\35\7\r\2\2\34\36\7\5\2\2\35")
        buf.write("\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2\37!\7\n\2\2 \"")
        buf.write("\7\5\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#$\7\25\2\2$%")
        buf.write("\5\4\3\2%\7\3\2\2\2&\'\7\22\2\2\'(\7\5\2\2()\7\3\2\2)")
        buf.write("*\7\25\2\2*+\7\20\2\2+,\7\25\2\2,.\7\3\2\2-/\7\5\2\2.")
        buf.write("-\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\5\4\3\2\61\t\3\2")
        buf.write("\2\2\628\7\r\2\2\63\64\7\3\2\2\64\65\7\25\2\2\658\7\3")
        buf.write("\2\2\668\7\13\2\2\67\62\3\2\2\2\67\63\3\2\2\2\67\66\3")
        buf.write("\2\2\28\13\3\2\2\29;\5\n\6\2:<\7\5\2\2;:\3\2\2\2;<\3\2")
        buf.write("\2\2<=\3\2\2\2=?\7\4\2\2>@\7\5\2\2?>\3\2\2\2?@\3\2\2\2")
        buf.write("@B\3\2\2\2A9\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3")
        buf.write("\2\2\2EC\3\2\2\2FG\5\n\6\2G\r\3\2\2\2HI\7\r\2\2IK\7\20")
        buf.write("\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\r\2\2MO\7\23\2")
        buf.write("\2NP\7\5\2\2ON\3\2\2\2OP\3\2\2\2PR\3\2\2\2QS\5\f\7\2R")
        buf.write("Q\3\2\2\2RS\3\2\2\2SU\3\2\2\2TV\7\5\2\2UT\3\2\2\2UV\3")
        buf.write("\2\2\2VW\3\2\2\2WX\7\24\2\2XY\5\4\3\2Y\17\3\2\2\2\16\25")
        buf.write("\35!.\67;?CJORU")
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

        def NotNewLine(self):
            return self.getToken(HookInterpreterParserParser.NotNewLine, 0)

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
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 30
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 33
            self.match(HookInterpreterParserParser.NotNewLine)
            self.state = 34
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

        def NotNewLine(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParserParser.NotNewLine)
            else:
                return self.getToken(HookInterpreterParserParser.NotNewLine, i)

        def Dot(self):
            return self.getToken(HookInterpreterParserParser.Dot, 0)

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
            self.state = 36
            self.match(HookInterpreterParserParser.Include)
            self.state = 37
            self.match(HookInterpreterParserParser.Whitespace)
            self.state = 38
            self.match(HookInterpreterParserParser.T__0)
            self.state = 39
            self.match(HookInterpreterParserParser.NotNewLine)
            self.state = 40
            self.match(HookInterpreterParserParser.Dot)
            self.state = 41
            self.match(HookInterpreterParserParser.NotNewLine)
            self.state = 42
            self.match(HookInterpreterParserParser.T__0)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 43
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 46
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParserParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(HookInterpreterParserParser.Identifier)
                pass
            elif token in [HookInterpreterParserParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(HookInterpreterParserParser.T__0)
                self.state = 50
                self.match(HookInterpreterParserParser.NotNewLine)
                self.state = 51
                self.match(HookInterpreterParserParser.T__0)
                pass
            elif token in [HookInterpreterParserParser.Digits]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
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
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55
                    self.argument()
                    self.state = 57
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HookInterpreterParserParser.Whitespace:
                        self.state = 56
                        self.match(HookInterpreterParserParser.Whitespace)


                    self.state = 59
                    self.match(HookInterpreterParserParser.T__1)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HookInterpreterParserParser.Whitespace:
                        self.state = 60
                        self.match(HookInterpreterParserParser.Whitespace)

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 68
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(HookInterpreterParserParser.Identifier)
                self.state = 71
                self.match(HookInterpreterParserParser.Dot)


            self.state = 74
            self.match(HookInterpreterParserParser.Identifier)
            self.state = 75
            self.match(HookInterpreterParserParser.OpenParanthesis)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParserParser.T__0) | (1 << HookInterpreterParserParser.Digits) | (1 << HookInterpreterParserParser.Identifier))) != 0):
                self.state = 79
                self.arguments()


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HookInterpreterParserParser.Whitespace:
                self.state = 82
                self.match(HookInterpreterParserParser.Whitespace)


            self.state = 85
            self.match(HookInterpreterParserParser.CloseParanthesis)
            self.state = 86
            self.sentenceEnding()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





