# Generated from HookInterpreter.g4 by ANTLR 4.8
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
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\5\6.\n\6\3\6\3\6\7\6\62\n\6\f\6")
        buf.write("\16\6\65\13\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\5\tD\n\t\3\t\3\t\3\t\5\tI\n\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\7\13S\n\13\f\13\16\13V\13\13\3")
        buf.write("\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\4\3\3\21")
        buf.write("\22\4\2\20\20\23\24\2Z\2\33\3\2\2\2\4\37\3\2\2\2\6!\3")
        buf.write("\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f8\3\2\2\2\16>\3\2\2\2\20")
        buf.write("C\3\2\2\2\22L\3\2\2\2\24T\3\2\2\2\26\34\7\5\2\2\27\34")
        buf.write("\7\6\2\2\30\34\5\22\n\2\31\34\5\n\6\2\32\34\5\6\4\2\33")
        buf.write("\26\3\2\2\2\33\27\3\2\2\2\33\30\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\3\3\2\2\2\37 \t\2\2\2 \5\3\2\2\2!\"\7\b\2\2\"#\7")
        buf.write("\16\2\2#$\7\23\2\2$%\7\t\2\2%&\7\23\2\2&\'\7\17\2\2\'")
        buf.write("(\5\4\3\2(\7\3\2\2\2)*\t\3\2\2*\t\3\2\2\2+.\5\f\7\2,.")
        buf.write("\5\16\b\2-+\3\2\2\2-,\3\2\2\2.\63\3\2\2\2/\60\7\3\2\2")
        buf.write("\60\62\5\f\7\2\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\5\4\3")
        buf.write("\2\67\13\3\2\2\289\5\b\5\29<\7\13\2\2:=\5\20\t\2;=\5\b")
        buf.write("\5\2<:\3\2\2\2<;\3\2\2\2=\r\3\2\2\2>?\7\7\2\2?@\5\f\7")
        buf.write("\2@\17\3\2\2\2AB\7\23\2\2BD\7\t\2\2CA\3\2\2\2CD\3\2\2")
        buf.write("\2DE\3\2\2\2EF\7\23\2\2FH\7\f\2\2GI\5\24\13\2HG\3\2\2")
        buf.write("\2HI\3\2\2\2IJ\3\2\2\2JK\7\r\2\2K\21\3\2\2\2LM\5\20\t")
        buf.write("\2MN\5\4\3\2N\23\3\2\2\2OP\5\b\5\2PQ\7\3\2\2QS\3\2\2\2")
        buf.write("RO\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3")
        buf.write("\2\2\2WX\5\b\5\2X\25\3\2\2\2\n\33\35-\63<CHT")
        return buf.getvalue()


class HookInterpreterParser ( Parser ):

    grammarFileName = "HookInterpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Declare'", "'Include'", "'.'", "'..'", "<INVALID>", 
                     "'('", "')'", "'<'", "'>'", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Whitespace", "BlockComment", 
                      "LineComment", "Declare", "Include", "Dot", "DoubleDot", 
                      "AssigmentOpreator", "OpenParanthesis", "CloseParanthesis", 
                      "OpenAngleBrackets", "CloseAngleBrackets", "FreeText", 
                      "End", "NewLine", "Identifier", "Digits" ]

    RULE_primaryExpression = 0
    RULE_ending = 1
    RULE_includeSentence = 2
    RULE_value = 3
    RULE_multiAssingment = 4
    RULE_assigmentWithOutDecl = 5
    RULE_assigmentWithDecl = 6
    RULE_functionCall = 7
    RULE_singleFunctionCall = 8
    RULE_values = 9

    ruleNames =  [ "primaryExpression", "ending", "includeSentence", "value", 
                   "multiAssingment", "assigmentWithOutDecl", "assigmentWithDecl", 
                   "functionCall", "singleFunctionCall", "values" ]

    EOF = Token.EOF
    T__0=1
    Whitespace=2
    BlockComment=3
    LineComment=4
    Declare=5
    Include=6
    Dot=7
    DoubleDot=8
    AssigmentOpreator=9
    OpenParanthesis=10
    CloseParanthesis=11
    OpenAngleBrackets=12
    CloseAngleBrackets=13
    FreeText=14
    End=15
    NewLine=16
    Identifier=17
    Digits=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PrimaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BlockComment(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.BlockComment)
            else:
                return self.getToken(HookInterpreterParser.BlockComment, i)

        def LineComment(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.LineComment)
            else:
                return self.getToken(HookInterpreterParser.LineComment, i)

        def singleFunctionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.SingleFunctionCallContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.SingleFunctionCallContext,i)


        def multiAssingment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.MultiAssingmentContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.MultiAssingmentContext,i)


        def includeSentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.IncludeSentenceContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.IncludeSentenceContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.match(HookInterpreterParser.BlockComment)
                    pass

                elif la_ == 2:
                    self.state = 21
                    self.match(HookInterpreterParser.LineComment)
                    pass

                elif la_ == 3:
                    self.state = 22
                    self.singleFunctionCall()
                    pass

                elif la_ == 4:
                    self.state = 23
                    self.multiAssingment()
                    pass

                elif la_ == 5:
                    self.state = 24
                    self.includeSentence()
                    pass


                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParser.BlockComment) | (1 << HookInterpreterParser.LineComment) | (1 << HookInterpreterParser.Declare) | (1 << HookInterpreterParser.Include) | (1 << HookInterpreterParser.FreeText) | (1 << HookInterpreterParser.Identifier) | (1 << HookInterpreterParser.Digits))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def End(self):
            return self.getToken(HookInterpreterParser.End, 0)

        def NewLine(self):
            return self.getToken(HookInterpreterParser.NewLine, 0)

        def EOF(self):
            return self.getToken(HookInterpreterParser.EOF, 0)

        def getRuleIndex(self):
            return HookInterpreterParser.RULE_ending

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnding" ):
                listener.enterEnding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnding" ):
                listener.exitEnding(self)




    def ending(self):

        localctx = HookInterpreterParser.EndingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ending)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (HookInterpreterParser.EOF - -1)) | (1 << (HookInterpreterParser.End - -1)) | (1 << (HookInterpreterParser.NewLine - -1)))) != 0)):
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

        def OpenAngleBrackets(self):
            return self.getToken(HookInterpreterParser.OpenAngleBrackets, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(HookInterpreterParser.Identifier)
            else:
                return self.getToken(HookInterpreterParser.Identifier, i)

        def Dot(self):
            return self.getToken(HookInterpreterParser.Dot, 0)

        def CloseAngleBrackets(self):
            return self.getToken(HookInterpreterParser.CloseAngleBrackets, 0)

        def ending(self):
            return self.getTypedRuleContext(HookInterpreterParser.EndingContext,0)


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
            self.state = 31
            self.match(HookInterpreterParser.Include)
            self.state = 32
            self.match(HookInterpreterParser.OpenAngleBrackets)
            self.state = 33
            self.match(HookInterpreterParser.Identifier)
            self.state = 34
            self.match(HookInterpreterParser.Dot)
            self.state = 35
            self.match(HookInterpreterParser.Identifier)
            self.state = 36
            self.match(HookInterpreterParser.CloseAngleBrackets)
            self.state = 37
            self.ending()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(HookInterpreterParser.Identifier, 0)

        def FreeText(self):
            return self.getToken(HookInterpreterParser.FreeText, 0)

        def Digits(self):
            return self.getToken(HookInterpreterParser.Digits, 0)

        def getRuleIndex(self):
            return HookInterpreterParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = HookInterpreterParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParser.FreeText) | (1 << HookInterpreterParser.Identifier) | (1 << HookInterpreterParser.Digits))) != 0)):
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


    class MultiAssingmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ending(self):
            return self.getTypedRuleContext(HookInterpreterParser.EndingContext,0)


        def assigmentWithOutDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.AssigmentWithOutDeclContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.AssigmentWithOutDeclContext,i)


        def assigmentWithDecl(self):
            return self.getTypedRuleContext(HookInterpreterParser.AssigmentWithDeclContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_multiAssingment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiAssingment" ):
                listener.enterMultiAssingment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiAssingment" ):
                listener.exitMultiAssingment(self)




    def multiAssingment(self):

        localctx = HookInterpreterParser.MultiAssingmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiAssingment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HookInterpreterParser.FreeText, HookInterpreterParser.Identifier, HookInterpreterParser.Digits]:
                self.state = 41
                self.assigmentWithOutDecl()
                pass
            elif token in [HookInterpreterParser.Declare]:
                self.state = 42
                self.assigmentWithDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HookInterpreterParser.T__0:
                self.state = 45
                self.match(HookInterpreterParser.T__0)
                self.state = 46
                self.assigmentWithOutDecl()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.ending()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigmentWithOutDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.ValueContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.ValueContext,i)


        def AssigmentOpreator(self):
            return self.getToken(HookInterpreterParser.AssigmentOpreator, 0)

        def functionCall(self):
            return self.getTypedRuleContext(HookInterpreterParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_assigmentWithOutDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigmentWithOutDecl" ):
                listener.enterAssigmentWithOutDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigmentWithOutDecl" ):
                listener.exitAssigmentWithOutDecl(self)




    def assigmentWithOutDecl(self):

        localctx = HookInterpreterParser.AssigmentWithOutDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assigmentWithOutDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.value()
            self.state = 55
            self.match(HookInterpreterParser.AssigmentOpreator)
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 56
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 57
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigmentWithDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Declare(self):
            return self.getToken(HookInterpreterParser.Declare, 0)

        def assigmentWithOutDecl(self):
            return self.getTypedRuleContext(HookInterpreterParser.AssigmentWithOutDeclContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_assigmentWithDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigmentWithDecl" ):
                listener.enterAssigmentWithDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigmentWithDecl" ):
                listener.exitAssigmentWithDecl(self)




    def assigmentWithDecl(self):

        localctx = HookInterpreterParser.AssigmentWithDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assigmentWithDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(HookInterpreterParser.Declare)
            self.state = 61
            self.assigmentWithOutDecl()
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

        def Dot(self):
            return self.getToken(HookInterpreterParser.Dot, 0)

        def values(self):
            return self.getTypedRuleContext(HookInterpreterParser.ValuesContext,0)


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
        self.enterRule(localctx, 14, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 63
                self.match(HookInterpreterParser.Identifier)
                self.state = 64
                self.match(HookInterpreterParser.Dot)


            self.state = 67
            self.match(HookInterpreterParser.Identifier)
            self.state = 68
            self.match(HookInterpreterParser.OpenParanthesis)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HookInterpreterParser.FreeText) | (1 << HookInterpreterParser.Identifier) | (1 << HookInterpreterParser.Digits))) != 0):
                self.state = 69
                self.values()


            self.state = 72
            self.match(HookInterpreterParser.CloseParanthesis)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleFunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(HookInterpreterParser.FunctionCallContext,0)


        def ending(self):
            return self.getTypedRuleContext(HookInterpreterParser.EndingContext,0)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_singleFunctionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleFunctionCall" ):
                listener.enterSingleFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleFunctionCall" ):
                listener.exitSingleFunctionCall(self)




    def singleFunctionCall(self):

        localctx = HookInterpreterParser.SingleFunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_singleFunctionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.functionCall()
            self.state = 75
            self.ending()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HookInterpreterParser.ValueContext)
            else:
                return self.getTypedRuleContext(HookInterpreterParser.ValueContext,i)


        def getRuleIndex(self):
            return HookInterpreterParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = HookInterpreterParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.value()
                    self.state = 78
                    self.match(HookInterpreterParser.T__0) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 85
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





