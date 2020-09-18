# Generated from .\Interpreter\HookInterpreter.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\5\2\26\n\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6-\n\6\3\7\3\7\3\7\7\7\62\n\7\f\7\16\7")
        buf.write("\65\13\7\3\7\3\7\3\b\3\b\5\b;\n\b\3\b\3\b\3\b\5\b@\n\b")
        buf.write("\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\17\20\2")
        buf.write("F\2\25\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b!\3\2\2\2\n")
        buf.write(",\3\2\2\2\f\63\3\2\2\2\16:\3\2\2\2\20\26\7\5\2\2\21\26")
        buf.write("\7\6\2\2\22\26\5\b\5\2\23\26\5\6\4\2\24\26\5\16\b\2\25")
        buf.write("\20\3\2\2\2\25\21\3\2\2\2\25\22\3\2\2\2\25\23\3\2\2\2")
        buf.write("\25\24\3\2\2\2\26\3\3\2\2\2\27\30\t\2\2\2\30\5\3\2\2\2")
        buf.write("\31\32\7\b\2\2\32\33\7\r\2\2\33\34\7\23\2\2\34\35\7\t")
        buf.write("\2\2\35\36\7\23\2\2\36\37\7\r\2\2\37 \5\4\3\2 \7\3\2\2")
        buf.write("\2!\"\7\7\2\2\"#\7\23\2\2#$\7\16\2\2$%\7\24\2\2%&\5\4")
        buf.write("\3\2&\t\3\2\2\2\'-\7\23\2\2()\7\r\2\2)*\7\24\2\2*-\7\r")
        buf.write("\2\2+-\7\21\2\2,\'\3\2\2\2,(\3\2\2\2,+\3\2\2\2-\13\3\2")
        buf.write("\2\2./\5\n\6\2/\60\7\3\2\2\60\62\3\2\2\2\61.\3\2\2\2\62")
        buf.write("\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2")
        buf.write("\65\63\3\2\2\2\66\67\5\n\6\2\67\r\3\2\2\289\7\23\2\29")
        buf.write(";\7\t\2\2:8\3\2\2\2:;\3\2\2\2;<\3\2\2\2<=\7\23\2\2=?\7")
        buf.write("\13\2\2>@\5\f\7\2?>\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7\f")
        buf.write("\2\2BC\5\4\3\2C\17\3\2\2\2\7\25,\63:?")
        return buf.getvalue()


class HookInterpreterParser ( Parser ):

    grammarFileName = "HookInterpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Declare'", "'Include'", "'.'", "'..'", "'('", "')'", 
                     "'\"'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Whitespace", "BlockComment", 
                      "LineComment", "Declare", "Include", "Dot", "DoubleDot", 
                      "OpenParanthesis", "CloseParanthesis", "DoubleQuotes", 
                      "Equals", "End", "NewLine", "Digits", "Name", "Identifier", 
                      "FreeText" ]

    RULE_primaryExpression = 0
    RULE_sentenceEnding = 1
    RULE_includeSentence = 2
    RULE_variableDeclare = 3
    RULE_argument = 4
    RULE_arguments = 5
    RULE_functionCall = 6

    ruleNames =  [ "primaryExpression", "sentenceEnding", "includeSentence", 
                   "variableDeclare", "argument", "arguments", "functionCall" ]

    EOF = Token.EOF
    T__0=1
    Whitespace=2
    BlockComment=3
    LineComment=4
    Declare=5
    Include=6
    Dot=7
    DoubleDot=8
    OpenParanthesis=9
    CloseParanthesis=10
    DoubleQuotes=11
    Equals=12
    End=13
    NewLine=14
    Digits=15
    Name=16
    Identifier=17
    FreeText=18

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
            return self.getToken(HookInterpreterParser.BlockComment, 0)

        def LineComment(self):
            return self.getToken(HookInterpreterParser.LineComment, 0)

        def variableDeclare(self):
            return self.getTypedRuleContext(HookInterpreterParser.VariableDeclareContext,0)


        def includeSentence(self):
            return self.getTypedRuleContext(HookInterpreterParser.IncludeSentenceContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(HookInterpreterParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)




    def primaryExpression(self):

        localctx = HookInterpreterParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_primaryExpression)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParser.BlockComment]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(HookInterpreterParser.BlockComment)
                pass
            elif token in [HookInterpreterParser.LineComment]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(HookInterpreterParser.LineComment)
                pass
            elif token in [HookInterpreterParser.Declare]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.variableDeclare()
                pass
            elif token in [HookInterpreterParser.Include]:
                self.enterOuterAlt(localctx, 4)
                self.state = 17
                self.includeSentence()
                pass
            elif token in [HookInterpreterParser.Identifier]:
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
            return self.getToken(HookInterpreterParser.End, 0)

        def NewLine(self):
            return self.getToken(HookInterpreterParser.NewLine, 0)

        def getRuleIndex(self):
            return HookInterpreterParser.RULE_sentenceEnding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenceEnding" ):
                listener.enterSentenceEnding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenceEnding" ):
                listener.exitSentenceEnding(self)




    def sentenceEnding(self):

        localctx = HookInterpreterParser.SentenceEndingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentenceEnding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(_la==HookInterpreterParser.End or _la==HookInterpreterParser.NewLine):
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


    class IncludeSentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Include(self):
            return self.getToken(HookInterpreterParser.Include, 0)

        def DoubleQuotes(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.DoubleQuotes)
            else:
                return self.getToken(HookInterpreterParser.DoubleQuotes, i)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.Identifier)
            else:
                return self.getToken(HookInterpreterParser.Identifier, i)

        def Dot(self):
            return self.getToken(HookInterpreterParser.Dot, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParser.SentenceEndingContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_includeSentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeSentence" ):
                listener.enterIncludeSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeSentence" ):
                listener.exitIncludeSentence(self)




    def includeSentence(self):

        localctx = HookInterpreterParser.IncludeSentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_includeSentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(HookInterpreterParser.Include)
            self.state = 24
            self.match(HookInterpreterParser.DoubleQuotes)
            self.state = 25
            self.match(HookInterpreterParser.Identifier)
            self.state = 26
            self.match(HookInterpreterParser.Dot)
            self.state = 27
            self.match(HookInterpreterParser.Identifier)
            self.state = 28
            self.match(HookInterpreterParser.DoubleQuotes)
            self.state = 29
            self.sentenceEnding()
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
            return self.getToken(HookInterpreterParser.Declare, 0)

        def Identifier(self):
            return self.getToken(HookInterpreterParser.Identifier, 0)

        def Equals(self):
            return self.getToken(HookInterpreterParser.Equals, 0)

        def FreeText(self):
            return self.getToken(HookInterpreterParser.FreeText, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParser.SentenceEndingContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_variableDeclare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclare" ):
                listener.enterVariableDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclare" ):
                listener.exitVariableDeclare(self)




    def variableDeclare(self):

        localctx = HookInterpreterParser.VariableDeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(HookInterpreterParser.Declare)
            self.state = 32
            self.match(HookInterpreterParser.Identifier)
            self.state = 33
            self.match(HookInterpreterParser.Equals)
            self.state = 34
            self.match(HookInterpreterParser.FreeText)
            self.state = 35
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
            return self.getToken(HookInterpreterParser.Identifier, 0)

        def DoubleQuotes(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.DoubleQuotes)
            else:
                return self.getToken(HookInterpreterParser.DoubleQuotes, i)

        def FreeText(self):
            return self.getToken(HookInterpreterParser.FreeText, 0)

        def Digits(self):
            return self.getToken(HookInterpreterParser.Digits, 0)

        def getRuleIndex(self):
            return HookInterpreterParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = HookInterpreterParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(HookInterpreterParser.Identifier)
                pass
            elif token in [HookInterpreterParser.DoubleQuotes]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(HookInterpreterParser.DoubleQuotes)
                self.state = 39
                self.match(HookInterpreterParser.FreeText)
                self.state = 40
                self.match(HookInterpreterParser.DoubleQuotes)
                pass
            elif token in [HookInterpreterParser.Digits]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(HookInterpreterParser.Digits)
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
                return self.getTypedRuleContexts(HookInterpreterParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.ArgumentContext,i)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = HookInterpreterParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.argument()
                    self.state = 45
                    self.match(HookInterpreterParser.T__0) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 52
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
                return self.getTokens(HookInterpreterParser.Identifier)
            else:
                return self.getToken(HookInterpreterParser.Identifier, i)

        def OpenParanthesis(self):
            return self.getToken(HookInterpreterParser.OpenParanthesis, 0)

        def CloseParanthesis(self):
            return self.getToken(HookInterpreterParser.CloseParanthesis, 0)

        def sentenceEnding(self):
            return self.getTypedRuleContext(HookInterpreterParser.SentenceEndingContext,0)


        def Dot(self):
            return self.getToken(HookInterpreterParser.Dot, 0)

        def arguments(self):
            return self.getTypedRuleContext(HookInterpreterParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = HookInterpreterParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 54
                self.match(HookInterpreterParser.Identifier)
                self.state = 55
                self.match(HookInterpreterParser.Dot)


            self.state = 58
            self.match(HookInterpreterParser.Identifier)
            self.state = 59
            self.match(HookInterpreterParser.OpenParanthesis)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParser.DoubleQuotes) | (1 << HookInterpreterParser.Digits) | (1 << HookInterpreterParser.Identifier))) != 0):
                self.state = 60
                self.arguments()


            self.state = 63
            self.match(HookInterpreterParser.CloseParanthesis)
            self.state = 64
            self.sentenceEnding()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




